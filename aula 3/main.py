from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

pokemon = db.collection.find({"types": {"$in":"water"}})
writeAJson(pokemon,"pokemons do tipo agua")

pokemon1 = db.collection.find({"weaknesses":"poison"})
writeAJson(pokemon1,"fraco contra veneno")

pokemon2 = db.collection.find({"weaknesses":{"$size": 2}})
writeAJson(pokemon2,"pokemons que possui duas fraquezas")


pokemon3 = db.collection.find({"type":{"$in":"fire"}})
writeAJson(pokemon3,"Pokemon do tipo fogo")

pokemon4 = db.collection.find({"weaknesses": {"$size": 3}})
writeAJson = (pokemon4,"Pokemons com tres fraquezas")