from model.request import RequestGenerator, RequestProcessor


class Model:
    def __init__(self, generator: RequestGenerator, operators: list[RequestProcessor], computers: list[RequestProcessor]) -> None:
        self.generator = generator
        self.operators = operators
        self.computers = computers

    def event_mode(self):
        lost = 0
        generated_requests = self.generator.cnt

        self.generator.receivers = self.operators
        self.operators[0].receivers = [self.computers[0]]
        self.operators[1].receivers = [self.computers[0]]
        self.operators[2].receivers = [self.computers[1]]

        self.generator.next = self.generator.delay()
        self.operators[0].next = self.operators[0].delay()

        blocks = [self.generator,
                  self.operators[0], self.operators[1], self.operators[2],
                  self.computers[0], self.computers[1]]

        while self.generator.cnt >= 0:
            current_time = self.generator.next
            for block in blocks:
                if 0 < block.next < current_time:
                    current_time = block.next

            for block in blocks:
                if current_time == block.next:
                    if not isinstance(block, RequestProcessor):
                        next_generator = self.generator.generate()
                        if next_generator is not None:
                            next_generator.next = current_time + next_generator.delay()
                        else:
                            lost += 1
                        self.generator.next = current_time + self.generator.delay()
                    else:
                        block.process()
                        if block.queue == 0:
                            block.next = 0
                        else:
                            block.next = current_time + block.delay()

        return {"lost_percentage": lost / generated_requests * 100,
                "lost": lost}
