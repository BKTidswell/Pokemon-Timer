
class Pkmn_Data:
	def __init__(self,species,evolution_lvl,evolution,min_lvl,max_lvl,rarity,catch_rate,loc,img):
		self.species = species
		self.evolution_lvl = evolution_lvl
		self.evolution = evolution
		self.minLvl = min_lvl
		self.maxLvl = max_lvl
		self.rarity = rarity
		self.catch_rate = catch_rate
		self.loc = loc
		self.img = img


class Pkmn_Captured:
	def __init__(self,name,species,level,favorite,can_evolve,img):
		self.name = name
		self.species = species
		self.level = level
		self.can_evolve = can_evolve
		self.favorite = favorite
		self.img = img

#Common-ness
common = 100
uncommon = 50
rare = 25
legendary = 5

#Catch Rate
easy = 100
medium = 50
hard = 25
ultra_hard = 5

no_evo = 101


pkmn_info_array = [
["Bulbasaur",16,["Ivysaur"],1,15,uncommon,medium,"Forest","001"],
["Ivysaur",32,["Venusaur"],16,31,rare,hard,"Forest","002"],
["Venusaur",no_evo,[None],32,50,rare,hard,"Forest","003"],
["Charmander",16,["Charmeleon"],1,15,uncommon,medium,"Volcano","004"],
["Charmeleon",36,["Charizard"],16,31,rare,hard,"Volcano","005"],
["Charizard",no_evo,[None],36,50,rare,hard,"Volcano","006"],
["Squirtle",16,["Wartortle"],1,15,uncommon,medium,"Beach","007"],
["Wartortle",36,["Blastoise"],16,35,rare,hard,"Beach","008"],
["Blastoise",no_evo,[None],36,50,rare,hard,"Beach","009"]
]

core_pkmn_dict = {}
pkmn_env = {}

for pkmn in pkmn_info_array:
	core_pkmn_dict[pkmn[0]] = Pkmn_Data(pkmn[0],pkmn[1],pkmn[2],pkmn[3],pkmn[4],pkmn[5],pkmn[6],pkmn[7],pkmn[8])

	if pkmn[7] not in pkmn_env.keys():
		pkmn_env[pkmn[7]] = [ [pkmn[0]] , [pkmn[5]] ]
	else:
		pkmn_env[pkmn[7]][0].append(pkmn[0])
		pkmn_env[pkmn[7]][1].append(pkmn[5])

caughtPokemon = []
