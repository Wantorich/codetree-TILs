class Player :
    def __init__(self, id_, level_) :
        self.id_ = id_
        self.level_ = level_

id_, level_ = input().split()
player1 = Player(id_, level_)
player2 = Player(id_, level_)
player1.id_ = 'codetree'
player1.level_ = '10'

print(f'user {player1.id_} lv {player1.level_}')
print(f'user {player2.id_} lv {player2.level_}')