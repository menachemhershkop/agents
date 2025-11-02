# class Agente:
#     def __init__(self, code_name, clearance_level):
#         self.code=str(code_name)
#         self.__level=int(clearance_level)
#     def get_clearance_level():
#         pass
#     def set_clearance_level(self,level: int):
#         if level < 1 or level< 5:
#             return f' the level number is incorrect'
#         self.__level=level
#     def report(self):
#         print("Aagent", self.code ,"reporting. Clearance Level: ", self.level)
# class Mission:
#     def __init__(self,mission_name, target_location,assignet_agent=None):
#         self.mission=str(mission_name)
#         self.target=str(target_location)
#         self.agent=assignet_agent
#     def assignment(self):
#         pass
#     def brief(self):
#         print("Mission: ",self.mission,", Target: ", self.target, ", Agent:", self.agent.code)
# class Inteltools:
#     @staticmethod
#     def encrypt_message(msg: str):
#         return msg[::-1]
#     @staticmethod
#     def log_transmission(agent_name: str, message: str):
#         print(f'{agent_name} sent encrypted message: {message}')
# class Report:
#     def __init__(self,summary, urgency_level,submitted_by):
#         self.summary=summary
#         self.urgency_level=urgency_level
#         self.submitted_by=submitted_by
# class MissionControl(Report):
#     def analyze_report(self):
#         if self.urgency_level>= 4:
#             print("Immediate response required.")
#         if self.urgency_level == 3:
#             print("High priority. Monitor closely.")
#         else:
#             print("Routine analysis.")
#
# agent=Agente("Unit 8200",4)
# print(agent.set_clearance_level(4))