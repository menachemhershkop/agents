class MissionControl(Report):
    def analyze_report(self):
        if self.urgency_level>= 4:
            print("Immediate response required.")
        if self.urgency_level == 3:
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis.")