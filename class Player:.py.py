class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    
    @property
    def name(self):
        return self.__name

    @property
    def endurance(self):
        return self.__endurance

    @property
    def sprint(self):
        return self.__sprint

    @property
    def dribble(self):
        return self.__dribble

    @property
    def passing(self):
        return self.__passing

    @property
    def shooting(self):
        return self.__shooting

   
    @name.setter
    def name(self, value):
        self.__name = value

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        return (
            f"Player: {self.__name}\n"
            f"Endurance: {self.__endurance}\n"
            f"Sprint: {self.__sprint}\n"
            f"Dribble: {self.__dribble}\n"
            f"Passing: {self.__passing}\n"
            f"Shooting: {self.__shooting}\n"
        )


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

   
    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    
    @name.setter
    def name(self, value):
        self.__name = value

    @rating.setter
    def rating(self, value):
        self.__rating = value

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"

p1 = Player("Messi", 95, 92, 97, 94, 93)
p2 = Player("Ronaldo", 90, 95, 89, 85, 96)
p3 = Player("Mbappe", 92, 98, 91, 86, 90)
p4 = Player("Neymar", 88, 90, 95, 93, 88)


team = Team("DreamTeam", 99)


print(team.add_player(p1))   
print(team.add_player(p2))   
print(team.add_player(p1))   


print(team.remove_player("Ronaldo"))  
print(team.remove_player("Ronaldo"))  


print(p3)  
print(p4)


print(team.add_player(p3))
print(team.add_player(p4))


print("\nDanh sách cầu thủ trong đội:")
for player in team.players:
    print(f"- {player.name}")
