# Preparación
1. Creación de un entorno virtual
1. Intalación de bibliotecas con el archivo *requirements.txt*
## Variables de entorno
Deben de estar definidas las siguientes variables:
* DEBUG = 1
* MONGO_URI = mongodb+srv://{user}:{password}@cluster0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

# Ejecución
Para ejecutar el proyecto:
```bash
DEBUG=1 python live.py
```

# Git con aux.* en Windows
N caso de que SO cause conflicto con los archivos con nombre *aux*, desactive desde git la verificación de nombres con:
```bash
git config core.protectNTFS false
```