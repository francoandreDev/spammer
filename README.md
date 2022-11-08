
# Message Spammer Program

1. Estructura base:

   - .env
     - Virtual environment (entorno virtual).
       En git bash write python -m venv .env o .algo.
       To activate use this script: source (.env o .algo)/Scripts/Activate.
       To deactivate use this script: deactivate.
       No toques el archivo .env fuera de esos comandos solo deja la carpeta cerrada y deja que los scripts hagan el trabajo.
   - .vscode
     - settings.json (add words to workspace)
       You can use cntrl + . -> add to workspace settings.
   - classes
     Poo logic.
   - main
     The file will execute (run).
   - __init__.py
     for you can use imports and exports from local files.
   - .gitignore
     No subo .gitignore para que no se vea exactamente que no subo, tampoco el .env ya que es personal de cada máquina, tienes que crear el tuyo.
   - package.json
     For use scripts use npm run (script) for example npm run start.
   - README.md
     markdown file for resume the project as a guide for other programmers.
   - requirements
     The place where you see what the project needs, package with versions for install all at the same time see the package.json in line 5.

2. Classes:

    - Name in PascalCase.
    - Constructor execute when the class is call and looks like NameClass(): def __init__(self) -> None: self.variable = 0 name = NameClass()
      name.variable // 0.
    - Have variables and methods.

3. Methods:
   - Functions:
     Reserved word call def + name_function (snake_case).
     Es la forma de tener código encapsulado para reutilizar solo llamando a dicho nombre asi name_function() solo que cada vez podrías pasar
     diferentes parámetros o argumentos a tu función dándole dinamismo.
   - Methods:
     Si el constructor es un método pre-definido el nombre método es básicamente el nombre que recibe una función que vive (esta escrita) dentro
     de una clase.

4. ErrorHandler:
   - try: Evitará que el codigo se detenga por un error, en su lugar va a entrar al except.
   - except: Aquí manejas el error para corregirlo en caso que vuelva a salir el error volverá a entrar aquí.
   - finally: Además de lo que haya pasado independientemente ocurre esto.

5. __name__ == "__main__":
   Esta condición solo es accesible cuando el programa esta corriendo es un indicador para cualquiera que es codigo destinado a ejecutarse.

6. Por si algún día lo necesitas:
  import sys
  import os

  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))

  Con eso ya debería funcionar pero encontré otra mejor solución
