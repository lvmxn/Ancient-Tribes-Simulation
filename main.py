import random 

class Agent():
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

class Collector(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.strategy = "Collector"
    def action(self):
        chance = random.random()
        if chance < 0.15:
            pass
        elif chance <  0.7:
            self.food += 1
        elif chance <=  1:
            self.food += 2

agents=[Hunter("h1"),Hunter("h2"),Hunter("h3"),Hunter("h4"),Hunter("h5"),Collector("c1"),Collector("c2"),Collector("c3"),Collector("c4"),Collector("c5")]

for day in range(10):
    print(f"day:{day+1}")
    for agent in agents:
        if agent.alive:
            agent.live()
        if agent.alive:
            agent.action()
        print(agent.name,agent.food,agent.alive)
    print("\n")
