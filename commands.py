import click
from flask.cli import with_appcontext
from database import init_db
import csv
from models import Pokemons, TypePokemon
from database import db_session
from sqlalchemy.exc import IntegrityError


@click.command('create_db')
@with_appcontext
def create_db():
    print('creating db')
    init_db()
    print('created pokemon.db')


# https://cdn.traction.one/pokedex/pokemon/721.png
@click.command('load_data')
@with_appcontext
@click.option('--file')
def load_data(file):
    def get_type(name):
        t = search_type(name)
        if not t:
            t = TypePokemon(name=name)
            db_session.add(t)
            db_session.commit()
            types_pokemon.append(t)
            return t
        return t[0]

    def search_type(name):
        return [item for item in types_pokemon if item.name == name]

    types_pokemon = TypePokemon.query.all()
    with open("pokemon.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            pokemon = Pokemons()
            pokemon.number = row[0]
            pokemon.name = row[1]
            pokemon.type1_id = get_type(row[2]).id
            if row[3]:
                pokemon.type2_id = get_type(row[3]).id
            pokemon.total = row[4]
            pokemon.hp = row[5]
            pokemon.attack = row[6]
            pokemon.defense = row[7]
            pokemon.sp_atk = row[8]
            pokemon.sp_def = row[9]
            pokemon.speed = row[10]
            pokemon.generation = row[11]
            pokemon.legendary = True if row[12] == 'True' else False
            try:
                db_session.add(pokemon)
                db_session.commit()
            except IntegrityError as e:
                db_session.rollback()
                print(f'the {pokemon.name} already exist')
        db_session.close()
