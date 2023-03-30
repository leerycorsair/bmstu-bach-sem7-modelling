
import random


class Event:
    def __init__(self, time: float, type: str) -> None:
        self.time = time
        self.type = type


class Events:
    def __init__(self) -> None:
        self.__pool: list[Event] = []

    def append(self, e: Event):
        i = 0
        while i < len(self.__pool) and self.__pool[i].time < e.time:
            i += 1
        if 0 < i < len(self.__pool):
            self.__pool.insert(i - 1, e)
        else:
            self.__pool.insert(i, e)

    def pop(self, index):
        return self.__pool.pop(index)


class EventModel():
    def __init__(self, generator, processor) -> None:
        self.generator = generator
        self.processor = processor
        self.processed_tasks = 0

    def start(self, total_tasks: int, repeat_rate: int) -> int:
        events = Events()
        events.append(Event(self.generator.generate(), 'g'))

        q_current_len = 0
        q_max_len = 0
        q_free = True
        q_process = False

        while self.processed_tasks < total_tasks:
            e = events.pop(0)

            if e.type == 'g':
                q_current_len += 1
                if q_current_len > q_max_len:
                    q_max_len = q_current_len
                new_e = Event(e.time + self.generator.generate(), 'g')
                events.append(new_e)
                if q_free:
                    q_process = True

            elif e.type == 'p':
                self.processed_tasks += 1
                if random.randint(0, 100) <= repeat_rate:
                    q_current_len += 1
                q_process = True

            if q_process:
                if q_current_len > 0:
                    q_current_len -= 1
                    new_e = Event(e.time + self.processor.generate(), 'p')
                    events.append(new_e)
                    q_free = False
                else:
                    q_free = True
                q_process = False

        return q_max_len
