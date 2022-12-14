# examen Ordinario Ingenieria del Software

Para realizar este ejercicio hemos decidido trabajar con python, usando el compilador pytest
y el gestor de paquetes poetry. 

Para la instalación hemos ejecutado los siguientes comandos:

Instalar editor de código (visual studio code)

'''
1) echo root | sudo -S rpm --import https://packages.microsoft.com/keys/microsoft.asc
'''

'''
2)sudo zypper addrepo https://packages.microsoft.com/yumrepos/vscode vscode
'''

'''
3) sudo zypper refresh
'''

'''
4) sudo zypper install code
'''

una vez instalado el editor de texto, instalamos poetry

'''
1)) curl -sSL https://install.python-poetry.org | python3 -
'''
en el bash (vi.bashrc) añadimos el path
'''
2) export PATH="/home/user/.local/bin:$PATH"
'''
actualizamos
'''
3) source .bashrc
'''
creamos proyecto, sustituyendo en el comando nombre por el nombre que le queramos dar al proyecto
'''
4)poetry new nombre
'''
Observamos que se nos han creado un directorio de src y uno de test. En el de src añadiremos la clase donde definiremos las funciones, y en tests la clase donde añadiremos las pruebas para comprobar que estas funciones se han implementado correctamente.

El compilador pytest ya está instalado, así que ya podemos empezar a trabajar. 
Para compilar el código (desde el directorio principal)

'''
poetry run pytest tests/test_clase.py
'''
Decisiones de diseño: