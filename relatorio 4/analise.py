from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, db):
        self.db = db
    def f1(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group":
             {"_id": "$data_compra", #agrupa por data de compra
              "total_vendas":{"$sum":1}#conta o numero de vendas por dia
              }},
        ])
        writeAJson(result,"total de vendas por dia")
        
    def f2(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",  # Agrupa por descrição do produto
                "quantidade_vendida": {"$sum": "$produtos.quantidade"}  # Soma as quantidades vendidas de cada produto
            }},
            {"$sort": {"quantidade_vendida": -1}},  # Ordena por quantidade vendida em ordem decrescente
            {"$limit": 1}  # Limita o resultado ao produto mais vendido
        ])
        writeAJson(result,"produto mais vendido")
    def f3(self):
        result = self.db.collection([
            {"$unwind": "$produtos"},
            {"$group":{
                "_id": "$cliente_id",#agrupa por cliente
                "total_gasto":{"$sum":{"$multiply":["$produtos.quantidade","$produtos.preco"]}}#calcula o total gasto em cada compra
            }},
            {"$sort": {"total_gasto":-1}},#agrupa o total gasto em ordem decrescente
            {"$limit":1}#limita o resultado ao cliente que mais gastou
        ])
        writeAJson(result,"Cliente que mais gastou em uma compra")
    def f4(self):
        result = self.db.collection([
            {"$unwind": "$produtos"},
            {"$group":{
                "_id": "$produtos.descricao", #agrupa por descricao do produto
                "quantidade_vendida":{"$sum":"$produtos.quantidade"}#soma a quantidade vendida
            }},
            {"$match":{"quantidade_vendida":{"$gt": 1}}},#filtra para produtos com mais de uma unidade vendida
            {"$sort":{"quantidade_vendida": -1}}#ordena por quantidade vendida em ordem decrescente
        ])
        writeAJson(result,"produtos com mais de uma unidade vendida")

