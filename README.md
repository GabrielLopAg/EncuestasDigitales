# Preparación
1. Creación de un entorno virtual
1. Intalación de bibliotecas con el archivo *requirements.txt*

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