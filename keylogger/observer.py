class PatternObserver:
    def __init__(self, alert_file):
        self.alert_file = alert_file

    def notify(self, message):
        with open(self.alert_file, "a") as f:
            f.write(message + "\n")