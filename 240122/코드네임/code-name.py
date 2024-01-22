class Agent :
    def __init__(self, code, score) :
        self.code = code
        self.score = score

agents = []
min_ = 100
min_idx = 0
for i in range(5) :
    code, score = input().split()
    score = int(score)
    agents.append(Agent(code, score))
    if score <= min_ :
        min_ = score 
        min_idx = i

print(agents[min_idx].code, agents[min_idx].score)