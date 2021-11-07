from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    public_id = Column(Integer)
    name = Column(String(50), unique=True)
    password = Column(String(50))
    admin = Column(Boolean)


@dataclass
class TypePokemon(Base):
    __tablename__ = 'types_pokemon'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<User {self.name!r}>'


@dataclass
class Pokemons(Base):
    __tablename__ = 'pokemons'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    number: int = Column(Integer)
    name: str = Column(String(100), unique=True)
    type1_id = Column(Integer, ForeignKey('types_pokemon.id'))
    type2_id = Column(Integer, ForeignKey('types_pokemon.id'))
    total: int = Column(Integer)
    hp: int = Column(Integer)
    attack: int = Column(Integer)
    defense: int = Column(Integer)
    sp_atk: int = Column(Integer)
    sp_def: int = Column(Integer)
    speed: int = Column(Integer)
    generation: int = Column(Integer)
    legendary: bool = Column(Boolean)
    type1: TypePokemon = relationship('TypePokemon', foreign_keys=[type1_id])
    type2: TypePokemon = relationship('TypePokemon', foreign_keys=[type2_id])

    def __init__(self, number=None, name=None):
        self.name = name
        self.number = number

    def __repr__(self):
        return f'name: {self.name}, id: {self.id}'
