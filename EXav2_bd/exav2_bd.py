"""""
criando os membros da familia stark
create(Rickard_Stark:Pessoa:Stark{nome: 'Rickard Stark', titulo:'O Príncipe de Winterfell',sexo:'M'})
create(Lyarra_Stark:Pessoa:Stark{nome: 'Lyarra Stark', titulo: 'Senhora de Winterfell',sexo:'F'})
create(Brandon_Stark:Pessoa:Stark{nome: 'Brandon Stark', titulo: 'herdeiro de Rickard Stark',sexo:'M'})
create(Benjen_Stark:Pessoa:Stark{nome: 'Benjen Stark', titulo: 'Primeiro Patrulheiro',sexo:'M'})
create(Eddard_Stark:Pessoa:Stark{nome: 'Eddard Stark', titulo: 'Mão do Rei (conselheiro real) Regente',sexo:'M'})
create(Catelyn_Stark:Pessoa:Stark{nome: 'Catelyn Stark', titulo: ' Senhora do Norte',sexo:'F'})
create(Rhaegar_Targaryen:Pessoa:Stark{nome: 'Rhaegar Targaryen', titulo: 'Príncipe de Pedra do Dragão e príncipe herdeiro do Trono de Ferro.',sexo:'M'})
create(Jon_Snow:Pessoa:Targaryen{nome: 'Jon Snow', titulo: 'Senhor Comandante da Patrulha da Noite',sexo:'M'})
create(Talisa_Maegyr:Pessoa:Stark{nome: 'Talisa Maegyr', titulo: 'curandeira',sexo:'F'})
create(Robb_Stark:Pessoa:Stark{nome: 'Robb Stark', titulo: 'Rei do Norte Rei do Tridente Senhor de Winterfell',sexo:'M'})
create(Arya_Stark:Pessoa:Stark{nome: 'Arya Stark', titulo: 'Princesa de Winterfell',sexo:'F'})
create(Bran_Stark:Pessoa:Stark{nome: 'Bran Stark', titulo: 'Rei dos Ândalos e dos Primeiros Homens',sexo:'M'})
create(Rickon_Stark:Pessoa:Stark{nome: 'Rickon Stark', titulo: 'O Príncipe de Winterfell',sexo:'M'})
create(Tyrion_Lannister:Pessoa:Lannister{nome: 'Tyrion Lannister', titulo: 'Mao da rainha',sexo:'M'})
create(Sansa_Stark:Pessoa:Stark{nome: 'Sansa Stark', titulo: 'A Princesa do Norte',sexo:'F'})
create(Ramsay_Bolton:Pessoa:Bolton{nome: 'Ramsay Bolton', titulo: 'Lorde de Winterfell Castelão de Dreadfort',sexo:'M'})
create(Lyanna_Stark:Pessoa:Stark{nome:'Lyanna Stark', titulo:'Princesa',sexo:'F'})

//fazendo relacionamentos

//casamento
create(Rickard_Stark)-[:CASADO_COM{tempocasado: '30 anos'}]->(Lyarra_Stark)
create(Lyarra_Stark)-[:CASADO_COM{tempocasado: '30 anos'}]->(Rickard_Stark)

create(Eddard_Stark)-[:CASADO_COM{tempocasado: '20 anos'}]->(Catelyn_Stark)
create(Catelyn_Stark)-[:CASADO_COM{tempocasado: '20 anos'}]->(Eddard_Stark)

create(Lyanna_Stark)-[:CASADO_COM{tempocasado: '2 anos'}]->(Rhaegar_Targaryen)
create(Rhaegar_Targaryen)-[:CASADO_COM{tempocasado: '2 anos'}]->(Lyanna_Stark)

create(Talisa_Maegyr)-[:CASADO_COM{tempocasado: '2 anos'}]->(Robb_Stark)
create(Robb_Stark)-[:CASADO_COM{tempocasado: '20 anos'}]->(Talisa_Maegyr)

create(Sansa_Stark)-[:CASADO_COM{tempocasado: '6 meses'}]->(Tyrion_Lannister)
create(Tyrion_Lannister)-[:CASADO_COM{tempocasado: '6 meses'}]->(Sansa_Stark)
create(Sansa_Stark)-[:CASADO_COM{tempocasado: '2 meses'}]->(Ramsay_Bolton)
create(Ramsay_Bolton)-[:CASADO_COM{tempocasado: '2 meses'}]->(Sansa_Stark)

//pais
create(Brandon_Stark)<-[:PAI_DE]-(Rickard_Stark)
create(Benjen_Stark)<-[:PAI_DE]-(Rickard_Stark)
create(Eddard_Stark)<-[:PAI_DE]-(Rickard_Stark)
create(Lyanna_Stark)<-[:PAI_DE]-(Rickard_Stark)

create(Brandon_Stark)<-[:PAI_DE]-(Lyarra_Stark)
create(Benjen_Stark)<-[:PAI_DE]-(Lyarra_Stark)
create(Eddard_Stark)<-[:PAI_DE]-(Lyarra_Stark)
create(Lyanna_Stark)<-[:PAI_DE]-(Lyarra_Stark)

create(Robb_Stark)<-[:PAI_DE]-(Eddard_Stark)
create(Bran_Stark)<-[:PAI_DE]-(Eddard_Stark)
create(Arya_Stark)<-[:PAI_DE]-(Eddard_Stark)
create(Rickon_Stark)<-[:PAI_DE]-(Eddard_Stark)
create(Sansa_Stark)<-[:PAI_DE]-(Eddard_Stark)

create(Robb_Stark)<-[:PAI_DE]-(Catelyn_Stark)
create(Bran_Stark)<-[:PAI_DE]-(Catelyn_Stark)
create(Arya_Stark)<-[:PAI_DE]-(Catelyn_Stark)
create(Rickon_Stark)<-[:PAI_DE]-(Catelyn_Stark)
create(Sansa_Stark)<-[:PAI_DE]-(Catelyn_Stark)

create(Jon_Snow)<-[:PAI_DE]-(Lyanna_Stark)
create(Jon_Snow)<-[:PAI_DE]-(Rhaegar_Targaryen)

//filhos
create(Brandon_Stark)-[:FILHO_DE]->(Rickard_Stark)
create(Benjen_Stark)-[:FILHO_DE]->(Rickard_Stark)
create(Eddard_Stark)-[:FILHO_DE]->(Rickard_Stark)
create(Lyanna_Stark)-[:FILHO_DE]->(Rickard_Stark)

create(Brandon_Stark)-[:FILHO_DE]->(Lyarra_Stark)
create(Benjen_Stark)-[:FILHO_DE]->(Lyarra_Stark)
create(Eddard_Stark)-[:FILHO_DE]->(Lyarra_Stark)
create(Lyanna_Stark)-[:FILHO_DE]->(Lyarra_Stark)

create(Robb_Stark)-[:FILHO_DE]->(Eddard_Stark)
create(Bran_Stark)-[:FILHO_DE]->(Eddard_Stark)
create(Arya_Stark)-[:FILHO_DE]->(Eddard_Stark)
create(Rickon_Stark)-[:FILHO_DE]->(Eddard_Stark)
create(Sansa_Stark)-[:FILHO_DE]->(Eddard_Stark)

create(Robb_Stark)-[:FILHO_DE]->(Catelyn_Stark)
create(Bran_Stark)-[:FILHO_DE]->(Catelyn_Stark)
create(Arya_Stark)-[:FILHO_DE]->(Catelyn_Stark)
create(Rickon_Stark)-[:FILHO_DE]->(Catelyn_Stark)
create(Sansa_Stark)-[:FILHO_DE]->(Catelyn_Stark)

create(Jon_Snow)-[:FILHO_DE]->(Lyanna_Stark)
create(Jon_Snow)-[:FILHO_DE]->(Rhaegar_Targaryen)
//IRMAOS
create(Brandon_Stark)-[:IRMAO_DE]->(Benjen_Stark)
create(Brandon_Stark)-[:IRMAO_DE]->(Eddard_Stark)
create(Brandon_Stark)-[:IRMAO_DE]->(Lyanna_Stark)

create(Benjen_Stark)-[:IRMAO_DE]->(Brandon_Stark)
create(Benjen_Stark)-[:IRMAO_DE]->(Eddard_Stark)
create(Benjen_Stark)-[:IRMAO_DE]->(Lyanna_Stark)

create(Eddard_Stark)-[:IRMAO_DE]->(Brandon_Stark)
create(Eddard_Stark)-[:IRMAO_DE]->(Benjen_Stark)
create(Eddard_Stark)-[:IRMAO_DE]->(Lyanna_Stark)

create(Lyanna_Stark)-[:IRMAO_DE]->(Brandon_Stark)
create(Lyanna_Stark)-[:IRMAO_DE]->(Benjen_Stark)
create(Lyanna_Stark)-[:IRMAO_DE]->(Eddard_Stark)

create(Robb_Stark)-[:IRMAO_DE]->(Bran_Stark)
create(Robb_Stark)-[:IRMAO_DE]->(Arya_Stark)
create(Robb_Stark)-[:IRMAO_DE]->(Rickon_Stark)
create(Robb_Stark)-[:IRMAO_DE]->(Sansa_Stark)

create(Bran_Stark)-[:IRMAO_DE]->(Robb_Stark)
create(Bran_Stark)-[:IRMAO_DE]->(Arya_Stark)
create(Bran_Stark)-[:IRMAO_DE]->(Rickon_Stark)
create(Bran_Stark)-[:IRMAO_DE]->(Sansa_Stark)

create(Arya_Stark)-[:IRMAO_DE]->(Robb_Stark)
create(Arya_Stark)-[:IRMAO_DE]->(Bran_Stark)
create(Arya_Stark)-[:IRMAO_DE]->(Rickon_Stark)
create(Arya_Stark)-[:IRMAO_DE]->(Sansa_Stark)

create(Rickon_Stark)-[:IRMAO_DE]->(Robb_Stark)
create(Rickon_Stark)-[:IRMAO_DE]->(Bran_Stark)
create(Rickon_Stark)-[:IRMAO_DE]->(Arya_Stark)
create(Rickon_Stark)-[:IRMAO_DE]->(Sansa_Stark)

create(Sansa_Stark)-[:IRMAO_DE]->(Robb_Stark)
create(Sansa_Stark)-[:IRMAO_DE]->(Bran_Stark)
create(Sansa_Stark)-[:IRMAO_DE]->(Arya_Stark)
create(Sansa_Stark)-[:IRMAO_DE]->(Rickon_Stark)

//tios
create(Brandon_Stark)-[:TIO_DE]->(Robb_Stark)
create(Brandon_Stark)-[:TIO_DE]->(Arya_Stark)
create(Brandon_Stark)-[:TIO_DE]->(Bran_Stark)
create(Brandon_Stark)-[:TIO_DE]->(Rickon_Stark)
create(Brandon_Stark)-[:TIO_DE]->(Sansa_Stark)
create(Brandon_Stark)-[:TIO_DE]->(Jon_Snow)

create(Benjen_Stark)-[:TIO_DE]->(Robb_Stark)
create(Benjen_Stark)-[:TIO_DE]->(Arya_Stark)
create(Benjen_Stark)-[:TIO_DE]->(Bran_Stark)
create(Benjen_Stark)-[:TIO_DE]->(Rickon_Stark)
create(Benjen_Stark)-[:TIO_DE]->(Sansa_Stark)
create(Benjen_Stark)-[:TIO_DE]->(Jon_Snow)

create(Lyanna_Stark)-[:TIO_DE]->(Robb_Stark)
create(Lyanna_Stark)-[:TIO_DE]->(Arya_Stark)
create(Lyanna_Stark)-[:TIO_DE]->(Bran_Stark)
create(Lyanna_Stark)-[:TIO_DE]->(Rickon_Stark)
create(Lyanna_Stark)-[:TIO_DE]->(Sansa_Stark)

create(Eddard_Stark)-[:TIO_DE]->(Jon_Snow)

//primos
create(Robb_Stark)-[:PRIMO_DE]->(Jon_Snow)
create(Arya_Stark)-[:PRIMO_DE]->(Jon_Snow)
create(Bran_Stark)-[:PRIMO_DE]->(Jon_Snow)
create(Rickon_Stark)-[:PRIMO_DE]->(Jon_Snow)
create(Sansa_Stark)-[:PRIMO_DE]->(Jon_Snow)

create(Robb_Stark)<-[:PRIMO_DE]-(Jon_Snow)
create(Arya_Stark)<-[:PRIMO_DE]-(Jon_Snow)
create(Bran_Stark)<-[:PRIMO_DE]-(Jon_Snow)
create(Rickon_Stark)<-[:PRIMO_DE]-(Jon_Snow)
create(Sansa_Stark)<-[:PRIMO_DE]-(Jon_Snow)
"""



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
        RETURN p1.nome AS Esposo, p2.nome AS Esposa, COLLECT(DISTINCT r.tempocasado)[0] AS Duracao
    """
    
    result = tx.run(query)
    return [{'Esposo': row['Esposo'], 'Esposa': row['Esposa'], 'Duracao': row['Duracao']} for row in result]

#Funcao 2: consultar filhos de uma pessoa especifica
def get_filhos(tx, pai_nome):
    query = """
        MATCH (pai:Pessoa {nome: $pai_nome})-[:PAI_DE]->(filho)
        RETURN DISTINCT(filho.nome) AS Filho
    """
    
    result = tx.run(query, pai_nome=pai_nome)
    return ([{'Filho': row['Filho']} for row in result])

#Funcao 3: Consultar irmaos de uma pessoa especifica
def get_irmaos(tx, pessoa_nome):
    query = """
        MATCH (p:Pessoa {nome: $pessoa_nome})-[:IRMAO_DE]->(irmao)
        RETURN DISTINCT(irmao.nome) AS Irmao
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
        print("4. Sair")

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
                irmaos = (session.execute_read(get_irmaos, pessoa_nome))
                if irmaos:
                    print(f"Irmãos de {pessoa_nome}:")
                    for irmao in irmaos:
                        print(f"Irmão: {irmao['Irmao']}")
                else:
                    print(f"{pessoa_nome} não tem irmãos cadastrados.")
        elif opcao == '4':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()

# Fechar a conexão com o driver
driver.close()
      
   

