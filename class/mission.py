class Mission:
    def __init__(self,mission_name, target_location,assignet_agent=None):
        self.mission=str(mission_name)
        self.target=str(target_location)
        self.agent=assignet_agent
    def assignment(self):
        pass
    def brief(self):
        print("Mission: ",self.mission,", Target: ", self.target, ", Agent:", self.agent.code)