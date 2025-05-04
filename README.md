# Langchain Service API

Quello che vedete è un esempio di una minuscola api che si occupa di ottenere un json in ingresso contenente un parametro query: ovvero una stringa contenente un prompt per un llm.
Dopodiché questa stringa viene inviata mediante langchain ad un llm e la risposta restituita sottoforma di stringa.

Il DAL è composto da un models.py che sfruttando SQLAlchemy descrive un oggetto chiamato PromptLog, ovvero un oggetto che tiene traccia di ogni log inviato al modello. Il db è un postgresql.
Per avviare il database, lanciare prima il docker-compose.yml (se si disponde di docker desktop) e dopo init_db.py

La libreria usata per la creazione dell'API è fast API. Questa viene dichiarata in main Api e l'applicazione viene creata in quel contesto. I controller dell'Api vengono gestiti su langChainService.py mentre le varie route vengono dichiarate e gestite su routes.py.
