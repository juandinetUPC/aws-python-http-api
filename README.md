# TODO: modificar el readme
## En un entorno virtual usando Python3 , pip y la siguiente lista de dependencias (requirements.txt)
- click==8.1.3
- colorama==0.4.4
- Flask==2.1.2
- Flask-MySQLdb==1.0.1
- importlib-metadata==4.11.3
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- mysqlclient==2.1.0
- Werkzeug==2.1.2
- zipp==3.8.0



Si no está instalado, instalamos virtualenv

```powershell
pip install virtualenv
```

Para crear un ambiente virtual digitamos el siguiente comando:

```powershell
virtualenv -p python3 env
```

para poner a funcionar el entorno virtual, se debe ejecutar:

```powershell
.\env\Scripts\activate
```

Una vez iniciado el entorno virtual, se ejecuta el siguiente comando:

```powershell
pip install -r .\requirements.txt
```

Para correr la solución se ejecuta el siguiente comando:

```powershell
python .\src\app.py
```

Para correr los test unitarios se ejecuta el siguiente comando:

```powershell
python .\src\test_app.py
```
