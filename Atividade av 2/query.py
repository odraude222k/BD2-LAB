from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        """Inicializa a conexão com o banco de dados Neo4j."""
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """Fecha a conexão com o banco."""
        self.driver.close()

    def execute_query(self, query, parameters=None):
        """Executa uma query Cypher no banco de dados."""
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]
        
# questao 1

    def procura_renzo(db):
        query = """
        MATCH(t:Teacher{name: 'Renzo'})
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        result = db.execute_query(query)

        return result

    def prof_letraM(db):
        query = """
        MATCH(t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.cpf AS cpf
        """
        result = db.execute_query(query)
        return result

    def nome_todas_cidades(db):
        query = """
        MATCH(c:City)
        RETURN c.name AS city_name
        """

        result = db.execute_query(query)
        return result

    def busca_escola(db):
        query = """
        MATCH(s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS school_name, s.address AS address, s.number AS number
        """
        result = db.execute_query(query)
        return result
    
    #questao 2
    def ano_prof_novo_velho(db):
        query = """
        MATCH(t:Teacher)
        RETURN MIN(t.ano_nasc) AS mais_velho, MAX(t.ano_nasc) AS mais_novo
        """
        result = db.execute_query(query)
        return result
    
    def media(db):
        query = """
        MATCH(c:City)
        RETURN AVG(c.population) AS media_populacao
        """
        result = db.execute_query(query)
        return result
    
    def funcc(db):
        query = """
        MATCH(c:City{cep: '37540-000'})
        RETURN REPLACE(c.name, 'a','A') AS nome_modificado
        """
        result = db.execute_query(query)
        return result
    def funcd(db):
        query = """
        MATCH(t:teacher)
        RETURN SUBSTRING(t.name, 2, 1) AS caractere
        """
        result = db.execute_query(query)
        return result


