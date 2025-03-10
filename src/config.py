class LoggerConfig:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")


logger = LoggerConfig()
