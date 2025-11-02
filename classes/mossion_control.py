from classes.reports import Report


class MissionControl:
    def analyze_report(r: Report):
        if r.urgency_level>= 4:
            print("Immediate response required.")
        if r.urgency_level == 3:
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis.")