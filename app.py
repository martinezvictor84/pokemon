from flask import Flask, request, jsonify
from models import Pokemons, TypePokemon
from auth import bp, token_required
import commands
from sqlalchemy import create_engine, desc, asc, or_
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(bp)
app.config['SECRET_KEY'] = 'secret-key-asdasjdhasduy'
app.cli.add_command(commands.create_db)
app.cli.add_command(commands.load_data)


@app.route("/pokemon", methods=['GET'])
@token_required
def pokemons(current_user):
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 0))
    query = Pokemons.query

    if request.args.get('is_legendary'):
        query = query.filter(
            Pokemons.legendary == request.args.get('is_legendary')
        )
    if request.args.get('type'):
        query = query.filter(
            or_(Pokemons.type1_id == request.args.get('type'),
                Pokemons.type2_id == request.args.get('type'))
        )
    if request.args.get('attack_gte'):
        query = query.filter(
            Pokemons.attack > request.args.get('attack_gte')
        )
    if request.args.get('defense_gte'):
        query = query.filter(
            Pokemons.defense > request.args.get('defense_gte')
        )
    if request.args.get('generation'):
        query = query.filter(
            Pokemons.generation == request.args.get('generation')
        )
    if request.args.get('order_by') and request.args.get('order_by_dir'):
        sort = desc(request.args.get('order_by')) \
            if request.args.get('order_by_dir') == 'desc' \
            else asc(request.args.get('order_by'))
        query = query.order_by(sort)
    return jsonify(query.limit(per_page).offset(per_page*page).all())


@app.route("/types", methods=['GET'])
@token_required
def types(current_user):
    return jsonify(TypePokemon.query.all())



