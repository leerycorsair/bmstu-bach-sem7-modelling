from model.base_generator import BaseGenerator


class RequestGenerator:
    def __init__(self, generator: BaseGenerator, cnt: int) -> None:
        self.generator = generator
        self.cnt = cnt
        self.receivers: RequestProcessor = []
        self.next = 0

    def generate(self) -> bool:
        self.cnt -= 1
        for receiver in self.receivers:
            if receiver.check_max():
                return receiver
        return None

    def delay(self) -> float:
        return self.generator.generate()


class RequestProcessor:
    def __init__(self, generator: BaseGenerator, max_queue_size: int = -1) -> None:
        self.generator = generator
        self.queue, self.received, self.max_queue, self.processed = 0, 0, max_queue_size, 0
        self.next = 0

    def check_max(self) -> bool:
        if self.max_queue == -1 or self.max_queue > self.queue:
            self.queue += 1
            self.received += 1
            return True
        return False

    def process(self) -> None:
        if self.queue > 0:
            self.queue -= 1
            self.processed += 1

    def delay(self) -> float:
        return self.generator.generate()
