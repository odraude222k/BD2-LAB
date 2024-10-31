from query import Database
from teacher_crud import TeacherCRUD

uri = "bolt://34.238.136.154"
user = "neo4j"
password = "balances-tracker-passages"


db = Database(uri,user,password)
teacher_crud = TeacherCRUD(db)

#criando o professor chris lima
teacher_crud.create(name="Chris Lima",ano_nasc=1956,cpf='189.052.396-66')

#lendo o professor
result = teacher_crud.read(name="Chris Lima")
if result:
    print(f"Nome: {result['name']}, Ano de nascimento: {result['ano_nasc']}, CPF: {result['cpf']}")
else:
    print("Professor nao encontrado")

#update 
teacher_crud.update(name="Chris Lima", newcpf="162.052.777-77")