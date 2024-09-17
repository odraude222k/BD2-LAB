from pymongo import MongoClient
from bson.objectid import ObjectId

class PassageiroModel:
    def __init__(self, database):
        self.db = database

    def create_passageiro(self, nome: str, documento: str):
        try:
            res = self.db.passageiros.insert_one({"nome": nome, "documento": documento})
            print(f"Passageiro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o passageiro: {e}")
            return None

    def read_passageiro_by_id(self, id: str):
        try:
            res = self.db.passageiros.find_one({"_id": ObjectId(id)})
            print(f"Passageiro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler passageiro: {e}")
            return None

    def update_passageiro(self, id: str, nome: str, documento: str):
        try:
            res = self.db.passageiros.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nome": nome, "documento": documento}}
            )
            print(f"Passageiro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar passageiro: {e}")
            return None

    def delete_passageiro(self, id: str):
        try:
            res = self.db.passageiros.delete_one({"_id": ObjectId(id)})
            print(f"Passageiro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar passageiro: {e}")
            return None


class CorridaModel:
    def __init__(self, database):
        self.db = database

    def create_corrida(self, nota: int, distancia: float, valor: float, passageiro_id: str):
        try:
            passageiro = self.db.passageiros.find_one({"_id": ObjectId(passageiro_id)})
            if not passageiro:
                print("Passageiro não encontrado.")
                return None
            
            res = self.db.corridas.insert_one({
                "nota": nota,
                "distancia": distancia,
                "valor": valor,
                "passageiro_id": ObjectId(passageiro_id)
            })
            print(f"Corrida criada com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar a corrida: {e}")
            return None

    def read_corrida_by_id(self, id: str):
        try:
            res = self.db.corridas.find_one({"_id": ObjectId(id)})
            if res:
                passageiro = self.db.passageiros.find_one({"_id": res["passageiro_id"]})
                res["passageiro"] = passageiro
            print(f"Corrida encontrada: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler corrida: {e}")
            return None

    def update_corrida(self, id: str, nota: int, distancia: float, valor: float):
        try:
            res = self.db.corridas.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nota": nota, "distancia": distancia, "valor": valor}}
            )
            print(f"Corrida atualizada: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar corrida: {e}")
            return None

    def delete_corrida(self, id: str):
        try:
            res = self.db.corridas.delete_one({"_id": ObjectId(id)})
            print(f"Corrida deletada: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar corrida: {e}")
            return None


class MotoristaModel:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nota: int):
        try:
            res = self.db.motoristas.insert_one({"nota": nota})
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.motoristas.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler motorista: {e}")
            return None

    def update_motorista(self, id: str, nota: int):
        try:
            res = self.db.motoristas.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nota": nota}}
            )
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.motoristas.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar motorista: {e}")
            return None
