class Person :
    def __init__(self, name, home, region) :
        self.name = name
        self.home = home
        self.region = region

    def print_(self) :
        print(f'name {self.name}')
        print(f'addr {self.home}')
        print(f'city {self.region}')

n = int(input())
cmp_, idx_ = "", 0
people = []
for i in range(n) :
    name, home, region = input().split()
    if cmp_ <= name :
        cmp_ = name
        idx_ = i
    people.append(Person(name, home, region))

people[idx_].print_()