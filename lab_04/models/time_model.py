import random


class TimeModel():
    def __init__(self, generator, processor, step: float) -> None:
        self.generator = generator
        self.processor = processor
        self.processed_tasks = 0
        self.step = step

    def start(self, total_tasks: int, repeat_rate: int) -> int:
        t_prev = 0
        t_current = self.step
        t_generator = self.generator.generate()
        t_processor = 0

        q_current_len = 0
        q_max_len = 0
        q_free = True

        while self.processed_tasks < total_tasks:
            if t_current > t_generator:
                q_current_len += 1
                if q_current_len > q_max_len:
                    q_max_len = q_current_len
                t_prev = t_generator
                t_generator += self.generator.generate()

            if t_current > t_processor:
                if q_current_len > 0:
                    q_prev = q_free
                    if q_free:
                        q_free = False
                    else:
                        self.processed_tasks += 1
                        if random.randint(0, 100) <= repeat_rate:
                            q_current_len += 1

                    q_current_len -= 1
                    if q_prev:
                        t_processor = t_prev + self.processor.generate()
                    else:
                        t_processor += self.processor.generate()
                else:
                    q_free = True

            t_current += self.step
        return q_max_len
