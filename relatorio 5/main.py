from database import Database
from writeAJson import writeAJson
from personModel import PersonModel

db = Database(database="relatório5",collection="livros")
personModel = PersonModel (database=db)

personModel.create_person(3,"Lovecraft", 1980,70)

personModel.delete_person
