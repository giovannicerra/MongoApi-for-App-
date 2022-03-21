# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:24:24 2021

@author: Utente
"""
import pymongo
from bson import ObjectId #importo da bson l'ObjectId, un oggetto bson è un oggetto binary form json
import datetime
client = pymongo.MongoClient("mongodb://GiovanniC:1234@localhost:27017/")
#connessione al DB locale(ho creato anche un mongoDBatlas, le api non cambiano, basta solo cambiare il link di collegamento dal locale al DBatlas online)
db= client['mydb01']#creo un nuovo DB dal nome mydb01
collection= db['mycol01']#inserisco una collezione all'interno del nuov DB dal nome mycol01
print('DB connected')


#FUNZIONE CHE PERMETTE DI AGGIUNGERE UTENTI AL DB
def insert_data(docu):
 document=collection.insert_one(docu)#lo inserisco nella collection mycol01
 return document.inserted_id
#Richiamo le funzioni semplicemente con i seguenti comandi
#Inserisco la data 
datetime_object = datetime.datetime.today()
docu={'name':'Francesco', 'Aggiunto il':str(datetime_object)}#nuovo utente(volendo posso associare un _id personalizzato unico ad ogni utente, anche se già assegna automaticamente ma con una logica proprietaria)
id=insert_data(docu)#aggiungo al DB
print(id)#stampo l'ID utente 

#FUNZIONE PER AGGIORNARE UN SINGOLO UTENTE, QUALSIASI DATO DI ESSO, oppure se non esiste lo crea
def update_or_create(document_id, data):
    document=collection.update_one({'_id':ObjectId(document_id)},{"$set":data}, upsert=True)
    return document.acknowledged
#Richiamo le funzioni semplicemente con i seguenti comandi
##docu={'name':'fio', 'Aggiornato il':str(datetime_object)}
##update_or_create('61a60e52aae989d58223e793',docu,data)

#FUNZIONE CHE MI RESTITUISCE LA DATA DI MODIFICA DEL DOCUMENTO 
def get_single_data(document_id):
    Data= collection.find_one({'_id':ObjectId(document_id)})
    return Data 
##get_single_data=(document_id)

#STORICO DEI DATI (non sono sicuro se mi da solo una lista degli ID oppure anche lo storico devo verificare)
def get_multiple_data():
    data = collection.find()
    return list(data)

#FUNZIONE PER AGGIORNARE UN SINGOLO UTENTE,questa volta se non esiste non lo aggiunge
def update_existing(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged 

#FUNZIONE PER ELIMINARE UN SINGOLO UTENTE
def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged

#CHIUDE LA CONNESSIONE CON IL DB
client.close()