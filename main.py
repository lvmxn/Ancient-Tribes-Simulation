import random 

agent_count = 5

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
        if self.food > 4:
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

agents = []
for i in range(agent_count):
    Hunter.hunter_count += 1
    Collector.collector_count += 1
    agents.append(Hunter(f"h{Hunter.hunter_count}"))
    agents.append(Collector(f"c{Collector.collector_count}"))


newborn_count = 0
newborn_count_c = 0
newborn_count_h = 0

for day in range(10):
    print(f"--- Day {day+1} ---")
    newborns = []
    
    for agent in agents:
        if agent.alive:
            agent.live()
        if agent.alive:
            agent.action()
        if agent.alive:
            agent.breeding(newborns)
            print(agent.name, agent.food, agent.alive)
    
    agents.extend(newborns)
    newborn_count += len(newborns)
    newborn_count_c += len([c for c in newborns if 'c' in c.name])
    newborn_count_h += len([c for c in newborns if 'h' in c.name])
    print(f"Newborns today: {len(newborns)}, Hunters: {len([c for c in newborns if 'h' in c.name])}, Collectors: {len([c for c in newborns if 'c' in c.name])}\n")

print(f"--- End ---\n Start agents: {agent_count} \n All agents: {len(agents)}, Hunters: {len([c for c in agents if 'h' in c.name])}, Collectors: {len([c for c in agents if 'c' in c.name])} \n Alive: {len([c for c in agents if c.alive])}, Hunters: {len([c for c in agents if 'h' in c.name and c.alive])}, Collectors: {len([c for c in agents if 'c' in c.name and c.alive])} \n Newborns: {newborn_count}, Hunters: {newborn_count_h}, Collectors: {newborn_count_c} \n Dead: {len([c for c in agents if not c.alive])}, Hunters: {len([c for c in agents if 'h' in c.name and not c.alive])}, Collectors: {len([c for c in agents if 'c' in c.name and not c.alive])}")