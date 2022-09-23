import requests
import ascii_magic 

class Pokemon():
    def __init__(self):
        self.name = ''
        self.id = -1
        self.hit_points = -1
        self.attack_points = -1
        self.defense_points = -1
        self.types = []
        self.image = ''
        self.master = None

    def create_from_name(self, name):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if not response.ok:
            return False
        data = response.json()

        self.name = data["name"]
        self.id = data["id"]
        self.hit_points = data["stats"][0]["base_stat"]
        self.attack_points = data["stats"][1]["base_stat"]
        self.defense_points = data["stats"][2]["base_stat"]
        self.image = data["sprites"]["other"]["home"]["front_default"]
        self.types = [ability['ability']['name'] for ability in data['abilities']]
        return True

    def display(self, cols=100):
        poke_img = ascii_magic.from_url(self.image, columns=cols)
        ascii_magic.to_terminal(poke_img)
    
    def display_stats(self):
        return f"""
        Name:\t\t{self.name}
        Hit Points:\t{self.hit_points}
        Attack Points:\t{self.attack_points}
        Defense Points:\t{self.defense_points}
        Types:\t\t{" ".join(self.types)}
        """

    def attack(self, enemy):
        attacking_power_self=self.attack_points - .5*enemy.defense_points
        attacking_power_enemy=enemy.attack_points - .5*self.defense_points

        if attacking_power_self <= 0:
            self.hit_points = 0
        
        if attacking_power_enemy <= 0:
            enemy.hit_points = 0
        
        while self.hit_points > 0 and enemy.hit_points > 0:
            chance_self = [True if n < self.master.crit_chance *1000 else False for n in range(1000)]
            chance_enemy = [True if n < enemy.master.crit_chance *1000 else False for n in range(1000)]

            enemy.hit_points -= int(attacking_power_self) if not chance_self \
                else int(attacking_power_self) * ((self.master.crit_bonus/100)+1)

            self.hit_points -= int(attacking_power_enemy) if not chance_enemy \
                else int(attacking_power_enemy) * ((enemy.master.crit_bonus/100)+1)
            

