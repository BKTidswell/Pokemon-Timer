
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
	def __init__(self,name,species,level,favorite,can_evolve,date,img):
		self.name = name
		self.species = species
		self.level = level
		self.can_evolve = can_evolve
		self.favorite = favorite
		self.caughtDate = date
		self.img = img

#Common-ness
common = 100
uncommon = 25
rare = 10
ultra_rare = 5
legendary = 1

#Catch Rate
easy = 100
medium = 50
hard = 25
ultra_hard = 5

no_evo = 101

#Seperated by 10s to make it easier
pkmn_info_array = [
["Bulbasaur",16,["Ivysaur"],5,15,uncommon,medium,"Forest","001"],
["Ivysaur",32,["Venusaur"],16,31,rare,hard,"Forest","002"],
["Venusaur",no_evo,[None],32,50,rare,hard,"Forest","003"],
["Charmander",16,["Charmeleon"],5,15,uncommon,medium,"Volcano","004"],
["Charmeleon",36,["Charizard"],16,31,rare,hard,"Volcano","005"],
["Charizard",no_evo,[None],36,50,rare,hard,"Volcano","006"],
["Squirtle",16,["Wartortle"],5,15,uncommon,medium,"Beach","007"],
["Wartortle",36,["Blastoise"],16,35,rare,hard,"Beach","008"],
["Blastoise",no_evo,[None],36,50,rare,hard,"Beach","009"],
["Caterpie",7,["Metapod"],1,6,common,easy,"Forest","010"],

["Metapod",10,["Butterfree"],7,9,uncommon,easy,"Forest","011"],
["Butterfree",no_evo,[None],10,20,uncommon,medium,"Forest","012"],
["Weedle",7,["Kakuna"],1,6,common,easy,"Forest","013"],
["Kakuna",10,["Beedrill"],7,9,uncommon,easy,"Forest","014"],
["Beedrill",no_evo,[None],10,20,uncommon,medium,"Forest","015"],
["Pidgey",18,["Pidgeotto"],1,17,common,easy,"Forest","016"],
["Pidgeotto",36,["Pidgeot"],18,35,uncommon,medium,"Forest","017"],
["Pidgeot",no_evo,[None],36,50,rare,hard,"Forest","018"],
["Rattata",20,["Raticate"],1,19,common,easy,"Field","019"],
["Raticate",no_evo,[None],20,35,uncommon,medium,"Field","020"],

["Spearow",20,["Fearow"],1,19,common,easy,"Town","021"],
["Fearow",no_evo,[None],20,35,rare,medium,"Town","022"],
["Ekans",22,["Arbok"],10,21,common,easy,"Cave","023"],
["Arbok",no_evo,[None],22,40,rare,medium,"Cave","024"],
["Pikachu",25,["Raichu"],10,24,uncommon,medium,"Forest","025"],
["Raichu",no_evo,[None],25,50,rare,hard,"Forest","026"],
["Sandshrew",7,["Sandslash"],10,21,common,easy,"Cave","027"],
["Sandslash",no_evo,[None],22,40,rare,medium,"Cave","028"],
["Nidoran (F)",16,["Nidorina"],5,15,common,easy,"Field","029"],
["Nidorina",36,["Nidoqueen"],16,35,uncommon,medium,"Field","030"],

["Nidoqueen",no_evo,[None],36,50,rare,hard,"Field","031"],
["Nidoran (M)",16,["Nidorino"],5,15,common,easy,"Field","032"],
["Nidorino",36,["Nidoking"],16,35,uncommon,medium,"Field","033"],
["Nidoking",no_evo,[None],36,50,rare,easy,"Field","034"],
["Clefairy",35,["Clefable"],20,34,uncommon,medium,"Cave","035"],
["Clefable",no_evo,[None],35,45,rare,hard,"Cave","036"],
["Vulpix",35,["Ninetales"],20,34,uncommon,medium,"Volcano","037"],
["Ninetales",no_evo,[None],35,45,rare,hard,"Volcano","038"],
["Jigglypuff",35,["Wigglytuff"],20,34,uncommon,medium,"Field","039"],
["Wigglytuff",no_evo,[None],35,45,rare,hard,"Field","040"],

["Zubat",22,["Golbat"],10,21,common,easy,"Cave","041"],
["Golbat",no_evo,[None],22,40,uncommon,medium,"Cave","042"],
["Oddish",21,["Gloom"],10,20,common,easy,"Forest","043"],
["Gloom",40,["Vileplume"],21,39,uncommon,medium,"Forest","044"],
["Vileplume",no_evo,[None],40,50,rare,hard,"Forest","045"],
["Paras",24,["Parasect"],10,23,uncommon,medium,"Forest","046"],
["Parasect",no_evo,[None],24,35,rare,hard,"Forest","047"],
["Venonat",31,["Venomoth"],20,30,uncommon,medium,"Forest","048"],
["Venomoth",no_evo,[None],31,45,rare,hard,"Forest","049"],
["Diglett",26,["Dugtrio"],10,25,common,easy,"Cave","050"],

["Dugtrio",no_evo,[None],26,40,uncommon,medium,"Cave","051"],
["Meowth",28,["Persian"],15,27,uncommon,medium,"Field","052"],
["Persian",no_evo,[None],28,40,rare,hard,"Field","053"],
["Psyduck",33,["Golduck"],20,32,uncommon,medium,"Beach","054"],
["Golduck",no_evo,[None],33,45,rare,hard,"Beach","055"],
["Mankey",28,["Primeape"],15,27,uncommon,medium,"Field","056"],
["Primeape",no_evo,[None],28,40,rare,hard,"Field","057"],
["Growlithe",35,["Arcanine"],25,34,uncommon,medium,"Volcano","058"],
["Arcanine",no_evo,[None],35,50,rare,hard,"Volcano","059"],
["Poliwag",25,["Poliwhirl"],10,24,uncommon,medium,"Beach","060"],

["Poliwhirl",40,["Poliwrath"],25,39,rare,easy,"Beach","061"],
["Poliwrath",no_evo,[None],40,50,ultra_rare,hard,"Beach","062"],
["Abra",16,["Kadabra"],5,15,uncommon,medium,"Town","063"],
["Kadabra",40,["Alakazam"],16,39,rare,hard,"Town","064"],
["Alakazam",no_evo,[None],40,50,ultra_rare,hard,"Town","065"],
["Machop",28,["Machoke"],15,27,common,easy,"Field","066"],
["Machoke",40,["Machamp"],28,39,uncommon,medium,"Field","067"],
["Machamp",no_evo,[None],40,50,rare,hard,"Field","068"],
["Bellsprout",21,["Weepinbell"],10,20,common,easy,"Forest","069"],
["Weepinbell",35,["Victreebel"],21,34,uncommon,medium,"Forest","070"],

["Victreebel",no_evo,[None],35,45,common,easy,"Forest","071"],
["Tentacool",30,["Tentacruel"],20,29,common,easy,"Beach","072"],
["Tentacruel",no_evo,[None],30,40,uncommon,medium,"Beach","073"],
["Geodude",25,["Graveler"],15,24,common,easy,"Cave","074"],
["Graveler",40,["Golem"],25,39,uncommon,medium,"Cave","075"],
["Golem",no_evo,[None],40,50,rare,hard,"Cave","076"],
["Ponyta",40,["Rapidash"],25,39,common,easy,"Volcano","077"],
["Rapidash",no_evo,[None],40,45,rare,hard,"Volcano","078"],
["Slowpoke",37,["Slowbro"],20,36,uncommon,easy,"Beach","079"],
["Slowbro",no_evo,[None],37,45,rare,medium,"Beach","080"],

["Magnemite",30,["Magneton"],15,29,uncommon,medium,"Town","081"],
["Magneton",no_evo,[None],30,40,rare,hard,"Town","082"],
["Farfetch'd",no_evo,[None],20,40,rare,hard,"Field","083"],
["Doduo",31,["Dodrio"],20,30,common,easy,"Field","084"],
["Dodrio",no_evo,[None],31,45,uncommon,medium,"Field","085"],
["Seel",34,["Dewgong"],15,33,uncommon,medium,"Beach","086"],
["Dewgong",no_evo,[None],34,45,rare,hard,"Beach","087"],
["Grimer",38,["Muk"],20,37,uncommon,medium,"Town","088"],
["Muk",no_evo,[None],38,45,rare,hard,"Town","089"],
["Shellder",35,["Cloyster"],17,34,uncommon,medium,"Beach","090"],

["Cloyster",no_evo,[None],35,45,rare,easy,"Beach","091"],
["Gastly",25,["Haunter"],15,24,uncommon,medium,"Cave","092"],
["Haunter",40,["Gengar"],25,6,rare,hard,"Cave","093"],
["Gengar",no_evo,[None],40,50,ultra_rare,hard,"Cave","094"],
["Onix",no_evo,[None],30,40,rare,hard,"Cave","095"],
["Drowzee",26,["Hypno"],15,25,common,easy,"Town","096"],
["Hypno",no_evo,[None],26,40,rare,hard,"Town","097"],
["Krabby",28,["Kingler"],15,27,uncommon,medium,"Beach","098"],
["Kingler",no_evo,[None],28,40,rare,hard,"Beach","099"],
["Voltorb",30,["Electrode"],20,29,common,easy,"Town","100"],

["Electrode",no_evo,[None],30,40,rare,hard,"Town","101"],
["Exeggcute",35,["Exeggutor"],25,34,uncommon,medium,"Forest","102"],
["Exeggutor",no_evo,[None],35,45,rare,hard,"Forest","103"],
["Cubone",28,["Marowak"],15,27,common,easy,"Cave","104"],
["Marowak",no_evo,[None],28,40,rare,hard,"Cave","105"],
["Hitmonlee",no_evo,[None],30,40,rare,hard,"Town","106"],
["Hitmonchan",no_evo,[None],30,40,rare,hard,"Town","107"],
["Lickitung",no_evo,[None],25,35,rare,hard,"Field","108"],
["Koffing",35,["Weezing"],25,34,uncommon,medium,"Town","109"],
["Weezing",no_evo,[None],35,45,rare,hard,"Town","110"],

["Rhyhorn",42,["Rhydon"],30,41,uncommon,medium,"Cave","111"],
["Rhydon",no_evo,[None],42,50,rare,hard,"Cave","112"],
["Chansey",no_evo,[None],30,40,ultra_rare,hard,"Town","113"],
["Tangela",no_evo,[None],25,35,rare,hard,"Forest","114"],
["Kangaskhan",no_evo,[None],30,40,ultra_rare,hard,"Field","115"],
["Horsea",32,["Seadra"],20,31,uncommon,medium,"Beach","116"],
["Seadra",no_evo,[None],32,40,rare,hard,"Beach","117"],
["Goldeen",33,["Seaking"],20,32,uncommon,medium,"Beach","118"],
["Seaking",no_evo,[None],33,40,rare,hard,"Beach","119"],
["Staryu",35,["Starmie"],25,34,uncommon,medium,"Beach","120"],

["Starmie",no_evo,[None],35,45,rare,hard,"Beach","121"],
["Mr. Mime",no_evo,[None],30,40,rare,hard,"Town","122"],
["Scyther",no_evo,[None],30,40,rare,hard,"Forest","123"],
["Jynx",no_evo,[None],30,40,rare,hard,"Cave","124"],
["Electabuzz",no_evo,[None],35,45,rare,hard,"Town","125"],
["Magmar",no_evo,[None],35,45,rare,hard,"Volcano","126"],
["Pinsir",no_evo,[None],30,40,rare,hard,"Forest","127"],
["Tauros",no_evo,[None],30,40,rare,hard,"Field","128"],
["Magikarp",20,["Gyarados"],1,19,common,easy,"Beach","129"],
["Gyarados",no_evo,[None],20,50,rare,hard,"Beach","130"],

["Lapras",no_evo,[None],30,40,rare,hard,"Beach","131"],
["Ditto",no_evo,[None],30,40,uncommon,easy,"Town","132"],
["Eevee",30,["Vaporeon","Jolteon","Flareon"],20,30,uncommon,easy,"Town","133"],
["Vaporeon",no_evo,[None],30,40,rare,hard,"Beach","134"],
["Jolteon",no_evo,[None],30,40,rare,hard,"Town","135"],
["Flareon",no_evo,[None],30,40,rare,hard,"Volcano","136"],
["Porygon",no_evo,[None],30,40,rare,hard,"Town","137"],
["Omanyte",40,["Omastar"],30,39,rare,hard,"Cave","138"],
["Omastar",no_evo,[None],40,50,ultra_rare,hard,"Cave","139"],
["Kabuto",40,["Kabutops"],30,39,rare,hard,"Cave","140"],

["Kabutops",no_evo,[None],40,50,rare,hard,"Cave","141"],
["Aerodactyl",no_evo,[None],35,45,rare,hard,"Cave","142"],
["Snorlax",no_evo,[None],40,50,rare,hard,"Field","143"],
["Articuno",no_evo,[None],60,75,legendary,hard,"Cave","144"],
["Zapdos",no_evo,[None],60,75,legendary,hard,"Town","145"],
["Moltres",no_evo,[None],60,75,legendary,hard,"Volcano","146"],
["Dratini",30,["Dragonair"],20,29,rare,hard,"Beach","147"],
["Dragonair",55,["Dragonite"],30,54,ultra_rare,hard,"Beach","148"],
["Dragonite",no_evo,[None],55,65,legendary,hard,"Beach","149"],
["Mewtwo",no_evo,[None],60,80,legendary,hard,"Cave","150"],

["Mew",no_evo,[None],60,80,legendary,easy,"Cave","151"]
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
candy = 0
totalMinutes = 0
