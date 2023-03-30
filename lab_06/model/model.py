import random


class Event:
    def __init__(self, time: float, stage: str, type: str = "None", operator: str = "None") -> None:
        self.time = time
        # STAGES = ["New", "Generated", "Designed", "Built", "Certifyed", "Finished"]
        self.stage = stage
        # TYPES = ["Default", "Government"]
        self.type = type
        # OPERATORS = ["Middle", "Senior"]
        self.operator = operator

    def new_stage(self, delta: float, new_stage: str):
        return Event(self.time + delta, new_stage, self.type, self.operator)


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


class Model:
    def __init__(self,
                 generator,
                 operators,
                 builders,
                 certifiers) -> None:
        self.generator = generator
        self.operators = operators
        self.builders = builders
        self.certifiers = certifiers
        self.processed_tasks = {"Default": 0, "Government": 0}
        self.lost = {"Default": 0, "Government": 0}

    def total_processed(self):
        return self.processed_tasks["Default"] + self.processed_tasks["Government"]

    def start(self, total_tasks: int, g_rate: int, d_c_rate: int, g_c_rate: int):
        events = Events()
        events.append(Event(0, "New"))
        middle_flag = False
        senior_flag = False
        c_rates = {"Default": d_c_rate, "Government": g_c_rate}

        while self.total_processed() < total_tasks:
            e = events.pop(0)

            if e.stage == "New":
                if random.randint(0, 100) >= g_rate:
                    e.type = "Default"
                else:
                    e.type = "Government"
                new_e1 = e.new_stage(0, "Generated")
                events.append(new_e1)

                new_e2 = e.new_stage(self.generator.generate(),
                                     "New")
                events.append(new_e2)

            elif e.stage == "Generated":
                if (e.type == "Default" and middle_flag == False):
                    e.operator = "Middle"
                    middle_flag = True
                elif (e.type == "Default" and senior_flag == False) or \
                        (e.type == "Government" and senior_flag == False):
                    e.operator = "Senior"
                    senior_flag = True
                else:
                    self.lost[e.type] += 1
                    continue
                new_e = e.new_stage(self.operators[e.type].generate(),
                                    "Designed")
                events.append(new_e)

            elif e.stage == "Designed":
                if e.operator == "Middle":
                    middle_flag = False
                elif e.operator == "Senior":
                    senior_flag = False
                new_e = e.new_stage(self.builders[e.type].generate(),
                                    "Built")
                events.append(new_e)

            elif e.stage == "Built":
                new_e = e.new_stage(self.certifiers[e.type].generate(),
                                    "Certifyed")
                events.append(new_e)

            elif e.stage == "Certifyed":
                if random.randint(0, 100) >= c_rates[e.type]:
                    new_e = e.new_stage(0, "Finished")
                else:
                    new_e = e.new_stage(self.builders[e.type].generate(),
                                        "Built")
                events.append(new_e)

            elif e.stage == "Finished":
                self.processed_tasks[e.type] += 1

        return self.processed_tasks, self.lost
