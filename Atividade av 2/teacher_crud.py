from neo4j import GraphDatabase
from query import Database

class TeacherCRUD:
    def __init__(self, db: Database):
        self.db = db

    def create(self,name,ano_nasc,cpf):
        query = """
        CREATE(:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.execute_query(query, {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})
        print(f"Professor {name} criado com sucesso")
    
    def read(self,name):
        query = """
        MATCH(t:Teacher{name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        result = self.db.execute_query(query, {"name": name})
        return result[0] if result else None
    
    def update(self,name, newcpf):
        query = """
        MATCH(t:Teacher{name: $name,})
        SET t.cpf = $newcpf
        RETURN t.name AS name, t.cpf AS cpf
        """
        result = self.db.execute_query(query,{"name": name,"newcpf": newcpf})
        if result:
            print(f"CPF do professor {name} atualizado para {newcpf}")
        else:
            print(f"Professor {name} nao encontrado")
    
    def delete(self,name):
        query = """
        MATCH(t:Teacher{name: $name})
        DELETE t
        """
        self.db.execute_query(query,{"name": name})
        print(f"Professor {name} deletado com sucesso")
