# All Master have the same max Team size
# each master has a unique name, id, list of pokemon
# crit hit chance and crit bonus they will start the same for both master
# it coul vary between master and maybe we could eventually create items
# that increase crit chance or bonus

class Master():
    MAX_TEAM_SIZE = 3

    def __init__(self, name, id):
        self.name=name
        self.id=id
        self.pokemon=[]
        self.crit_chance = .125 
        self.crit_bonus = 100
    
    def catch(self, poke):
        # check if the team is full
        if len(self.pokemon) >= Master.MAX_TEAM_SIZE:
            return "You have too many Pokemon"
        # check if they already have that pokemon
        if poke.id in {p.id for p in self.pokemon}:
            return "You already caught this pokemon"
        # catch pokemon
        poke.master=self
        self.pokemon.append(poke)
        return f"You caught {poke.name}!"

    def release(self, name):
        # check if they have the pokemon
        if name not in {p.name for p in self.pokemon}:
            return False
        else:
            # if they do we will release the pokemon
            self.pokemon=list(filter(lambda poke: poke.name.lower() != name.lower(), self.pokemon))
            return True

    def show_team(self):
        for poke in self.pokemon:
            poke.display(30)