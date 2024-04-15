#Importando 
from pymongo import MongoClient

#Fazendo a conexão com o mongo
connection_String = "mongodb+srv://celsiuss01:P3!xinh0@celsiuss01.aekfhde.mongodb.net/"
client = MongoClient(connection_String)

#Fazendo a conexão com meu BANCO
db_connection = client["meuBanco"]

print("--------------------------------------------------------------------------------------------------------")
collection = db_connection.get_collection("telefone")
print(collection)
print("--------------------------------------------------------------------------------------------------------")

#Criando documento
collection.insert_one({
    "Numero": "(85) 99872-5788",
    "Linha": "Claro",
    "Tipo": "CASA"
})


#Lendo TODOS os registros
for article in collection.find(): print(article)
print("--------------------------------------------------------------------------------------------------------")

#Lendo apenas UM registro
print(collection.find_one({ "Numero": "(85) 98477-0980" }))


#Atualização de OBJETO para mudar ou adicionar
query = { "Linha": "CLARO" }
new_query = { "$set": { "Contato": "Wesley Santos" } }
collection.update_one(query, new_query)

for article in collection.find(): print(article)
print("--------------------------------------------------------------------------------------------------------")

#Deletando Obejo
collection.delete_many({
    "Numero": "(85) 99872-5788"
    })

for article in collection.find(): print(article)
print("--------------------------------------------------------------------------------------------------------")
