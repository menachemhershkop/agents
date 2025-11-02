from classes.agent import Agent
from classes.inteltools import Inteltools
from classes.mossion_control import MissionControl
from classes.reports import Report

if __name__=='__main__':
    agent=Agent('unit8200', 1)
    print(agent.get_clearance_level())
    agent.set_clearance_level(4)
    print(agent.get_clearance_level())
    report=Report("Winter is coming!",3,agent.code)
    mission=MissionControl
    mission.analyze_report(report)
    Inteltools.log_transmission(agent.code,report.summary)
