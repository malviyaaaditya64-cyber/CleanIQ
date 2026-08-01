from datetime import datetime


class PipelineManager:

    def __init__(self):
        self.steps = []

    def add_step(self, operation, details=""):

        self.steps.append(
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Operation": operation,
                "Details": details
            }
        )

    def get_pipeline(self):
        return self.steps

    def clear(self):
        self.steps.clear()