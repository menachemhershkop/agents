class Agent:
    def __init__(self, code_name, clearance_level):
        self.code=str(code_name)
        self.__level=int(clearance_level)
    def get_clearance_level(self):
        return "Mission clearance level is", self.__level
    def set_clearance_level(self, level: int):
        if level < 1 or level> 5:
            return f' the level number is incorrect'
        self.__level=level

    def report(self):
        print("Aagent", self.code ,"reporting. Clearance Level: ", self.level)