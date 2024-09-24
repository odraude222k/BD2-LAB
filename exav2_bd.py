from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

uri = "neo4j+s://0f18afb0.databases.neo4j.io"
user = "neo4j"
password = "g7tnidCqSwKZvozT5AfrQQIycj5C6xCke1Nx8NtaOn0"
driver = GraphDatabase.driver(uri, auth=(user, password))

#Funcao 1: consultar casamento
def get_casamentos(tx):
    query = """
        MATCH (p1:Pessoa)-[r:CASADO_COM]->(p2:Pessoa)
        RETURN p1.nome AS Esposo, p2.nome AS Esposa, r.tempocasado AS Duracao
    """
    
    result = tx.run(query)
    return [{'Esposo': row['Esposo'], 'Esposa': row['Esposa'], 'Duracao': row['Duracao']} for row in result]

#Funcao 2: consultar filhos de uma pessoa especifica
def get_filhos(tx, pai_nome):
    query = """
        MATCH (pai:Pessoa {nome: $pai_nome})-[:PAI_DE]->(filho)
        RETURN filho.nome AS Filho
    """
    
    result = tx.run(query, pai_nome=pai_nome)
    return [{'Filho': row['Filho']} for row in result]

#Funcao 3: Consultar irmaos de uma pessoa especifica
def get_irmaos(tx, pessoa_nome):
    query = """
        MATCH (p:Pessoa {nome: $pessoa_nome})-[:IRMAO_DE]->(irmao)
        RETURN irmao.nome AS Irmao
    """
    
    result = tx.run(query, pessoa_nome=pessoa_nome)
    return [{'Irmao': row['Irmao']} for row in result]

def main():
    print("Bem-vindo ao sistema de consulta do banco de dados familiar!")
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar casamento")
        print("2. Consultar filhos de uma pessoa")
        print("3. Consultar irmaos de uma pessoa")
        print("4. Consultar filhos de uma pessoa")
        print("5. Sair")

        opcao = input("\nDigite o número da opção desejada: ")
        if opcao == '1':
            with driver.session() as session:
                casamentos = session.execute_read(get_casamentos)
                print("Casamentos na família:")
                for casamento in casamentos:
                    print(f"{casamento['Esposo']} casado com {casamento['Esposa']} por {casamento['Duracao']}")
        elif opcao == '2':
            pai_nome = input("Digite o nome do pai ou mãe para consultar os filhos: ")
            with driver.session() as session:
                filhos = session.execute_read(get_filhos, pai_nome)
                if filhos:
                    print(f"Filhos de {pai_nome}:")
                    for filho in filhos:
                        print(f"Filho: {filho['Filho']}")
                else:
                    print(f"{pai_nome} não tem filhos cadastrados.")
        elif opcao == '3':
            pessoa_nome = input("Digite o nome da pessoa para consultar os irmãos: ")
            with driver.session() as session:
                irmaos = session.execute_read(get_irmaos, pessoa_nome)
                if irmaos:
                    print(f"Irmãos de {pessoa_nome}:")
                    for irmao in irmaos:
                        print(f"Irmão: {irmao['Irmao']}")
                else:
                    print(f"{pessoa_nome} não tem irmãos cadastrados.")
        elif opcao == '5':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()

# Fechar a conexão com o driver
driver.close()
      
   

