""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrarĂ¡ las diferentes interfaces para repositorios
del dominio de vuelos

"""

from abc import ABC
from entregasalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioReservas(Repositorio, ABC):
    ...
 