import random 
import matplotlib.pyplot as plt
import numpy as np

agent_count = 5
runs_count = 10
days_count = 30

class Agent():
    hunter_count = 0
    collector_count = 0
    def __init__(self, name):
        self.name = name
        self.food = 2
        self.alive = True
    def live(self):
        self.food -= 1
        if self.food < 0:
            self.alive = False

class Hunter(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.strategy = "Hunter"
    def action(self):
        chance = random.random()
        if chance < 0.3:
            pass
        elif chance <  0.8:
            self.food += 1
        elif chance <=  1:
            self.food += 3
        if random.random() < 0.025:
            self.alive = False
    def breeding(self, newborns):
        while self.food > 4:
            self.food -= 1
            Hunter.hunter_count += 1
            newborns.append(Hunter(f"h{Hunter.hunter_count}"))

class Collector(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.strategy = "Collector"
    def action(self):
        chance = random.random()
        if chance < 0.2:
            pass
        elif chance <  0.7:
            self.food += 1
        elif chance <=  1:
            self.food += 2
    def breeding(self,newborns):
        if self.food > 4:
            self.food -= 1
            Collector.collector_count += 1
            newborns.append(Collector(f"c{Collector.collector_count}"))


all_runs_alive_all=[]
all_runs_alive_hunters=[]
all_runs_alive_collectors=[]

for run in range(runs_count):
    agents = []
    for i in range(agent_count):
        Hunter.hunter_count += 1
        Collector.collector_count += 1
        agents.append(Hunter(f"h{Hunter.hunter_count}"))
        agents.append(Collector(f"c{Collector.collector_count}"))

    newborn_count = 0
    newborn_count_c = 0
    newborn_count_h = 0
    days = []
    alive_all=[]
    alive_hunters=[]
    alive_collectors=[]

    for day in range(days_count):
        newborns = []
        
        for agent in agents:
            if agent.alive:
                agent.live()
            if agent.alive:
                agent.action()
            if agent.alive:
                agent.breeding(newborns)
        days.append(day+1)
        alive_all.append(len([c for c in agents if c.alive]))
        alive_hunters.append(len([c for c in agents if 'h' in c.name and c.alive]))
        alive_collectors.append(len([c for c in agents if 'c' in c.name and c.alive]))
        agents.extend(newborns)
        newborn_count += len(newborns)
        newborn_count_c += len([c for c in newborns if 'c' in c.name])
        newborn_count_h += len([c for c in newborns if 'h' in c.name])

    all_runs_alive_all.append(alive_all)
    all_runs_alive_hunters.append(alive_hunters)
    all_runs_alive_collectors.append(alive_collectors)


matrix_all = np.array(all_runs_alive_all)
matrix_hunters = np.array(all_runs_alive_hunters)
matrix_collectors = np.array(all_runs_alive_collectors)
average_alive_all = np.mean(matrix_all, axis=0)
average_alive_hunters = np.mean(matrix_hunters, axis=0)
average_alive_collectors = np.mean(matrix_collectors, axis=0)
plt.plot(days, average_alive_all, color="blue", linewidth=3, label="mean alive all")
plt.plot(days, average_alive_hunters, color="red", linewidth=2, label="mean alive hunters")
plt.plot(days, average_alive_collectors, color="green", linewidth=2, label="mean alive collectors")
plt.grid(True)
plt.legend()
plt.show()