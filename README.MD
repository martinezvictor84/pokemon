#Pokedex- Autolab
Proyecto desarrollado con Flask, costa de un Api que permite consultar los pokemons aplicando filtros y un cliente hecho con vueJs que permite visualizar la informacion.
el proyecto se encuentra desplegado en una instacia de ec2 de aws puede probarlo aqui http://ec2-54-146-183-65.compute-1.amazonaws.com:5000/static/login.html

## API
  Desarrollado con el framework Flask, permite consultar el listado de pokemons aplicando filtros y consultar el listado de tipos. 
### Autenticacion
  el api usa autenticacion con Json Web Tokens, a las peticiones se de debe agregar el token en el header ``Authorization``
#### Obtener el token
se realizar una peticion POST a

      http://ec2-54-146-183-65.compute-1.amazonaws.com:5000/login
Body
```json
{
    "username": "victor",
    "password": "1234"
}
````
Response
````json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0M2Q5ZWExYi05MzE2LTQwZDAtYTY4MS1iMTgxNmVjNTY4YTQiLCJleHAiOjE2MzYzMzk3MjV9.V9GBwvwkTpT1Ghtkc5CIAGVjN0Mr8v0xTwyC6nx06x0"
}
````
#### Ejemplo del header
      Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0NGEyMGVmMS00NzM4LTQ2NmEtOWFlMy1kNjZmODliMTBlOTMiLCJleHAiOjE2MzYwODM0ODR9.Uu5jK3xYAAqvsBQCfCmtdPFLsZWpym_L3PIMnZsBvPY
#### Registrase
#### Obtener el token
se realizar una peticion POST a

      http://ec2-54-146-183-65.compute-1.amazonaws.com:5000/register
Body
```json
{
    "username": "victor",
    "password": "1234"
}
```
### pokemons endpoint - GET
    http://ec2-54-146-183-65.compute-1.amazonaws.com:5000/pokemon
#### Parametos permitidos

* is_legendary (si es 1 solo los legendarios)
* type (filtra por tipo de pokemon)
* attack_gte (solo pokemons con ataque > )
* defense_gte (solo pokemons con defensa > )
* generation (filtra por generacion)[1,2,3,4,5,6]
* order_by (orderna por)[attack, defense, generation, number,hp, speed, sp_atk, sp_def]
* order_by_dir (direccion del orden)[asc, desc]
#### Parametros de paginacion
* page
* per_page
#### Ejemplo
````
 curl --location --request GET 'http://127.0.0.1:5000/pokemon?page=1&per_page=5&is_legendary=1&type=1&attack_gte=&defense_gte=&order_by=defense&order_by_dir=desc&generation=1' --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0NGEyMGVmMS00NzM4LTQ2NmEtOWFlMy1kNjZmODliMTBlOTMiLCJleHAiOjE2MzYwODM0ODR9.Uu5jK3xYAAqvsBQCfCmtdPFLsZWpym_L3PIMnZsBvPY'
````
### Tipos endpoint - GET
    http://ec2-54-146-183-65.compute-1.amazonaws.com:5000/types

## Cliente
  Cliente fue hecho con vueJs, permite:
* Registrarse
* Loguearse
* Vizualiar el listado de pokemons aplicando filtros
## Instruccion de configuracion.
### Requisitos

* python3.8
* pip
* virtualenv

### Pasos
* Clonar el proyecto
    ```sh
    $ git clone https://github.com/martinezvictor84/pokemon.git
    $ cd pokemon
    ```

* Configurar entorno virtual, instalar dependencias
    ```sh
    # si no tiene virtualenv instalado
    $ python3 -m pip install virtualenv
    # creamos el entorno virtual
    $ python3 -m virtualenv venv
    # Activamos el entorno virtual
    $ source venv/bin/activate
    # instalados los paquetes
    $ pip install -r requirements.txt
    ```

* Crear db y importar los datos
    ```sh
    # Creamos la base de datos, pokemon.db
    $ flask create_db
    # importamos los datos del archivos csv, pokemon.csv
    $ flask load_data
    ```
* Ejecuatar el proyecto
    ```sh
    # paramentos opciones, --host=0.0.0.0, --port
    $ flask run
    ```
  Abrir
  http://localhost:5000/static/login.html

# Autolab Flask Test

For this challenge, you need to develop an API with Flask and send the code (with your .git folder) as a zip file.

We will assess the following

1. Coding standards
2. Best practices
3. Authenticity
4. Complexity (optimal code)
5. Effective use of data structures
6. Re-useability of code
7. Innovation

## Challenge

You are tasked to develop an api with:

-   one endpoint, /pokemon
-   Allow one endpoint to be filtered and sorted with parameters
-   Develop a Python script to import the data into a (SQLite) database.
-   Add authentication (any)
-   Some form of simple test

### Notes
- Any library (next to flask) is allowed .
- keep it simple.
- Make sure your code is clean.
- Make sure you include your git history in the zip file (.git folder).
- You should use Flask and Python (Important!)
- Please write the instructions to run your solution
