import datetime
import math
from typing import List

from numpy import append


class Pessoa:
    def __init__(
        self,
        nome: str,
        sobrenome: str,
        data_de_nascimento: datetime.date,
    ) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor(
            (datetime.date.today() - self.data_de_nascimento).days / 365.2425
        )

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos"


class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: List[str]) -> None:
        self.pessoa = pessoa
        self.experiencias = experiencias

    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)

    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1]

    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e ja trabalhou em {self.quantidade_de_experiencias} empresas e atualmente trabalha na empresa {self.empresa_atual}"


rodrigo = Pessoa(
    nome="Rodrigo", sobrenome="Azevedo", data_de_nascimento=datetime.date(1994, 11, 9)
)
print(rodrigo)


curriculo_rodrigo = Curriculo(pessoa=rodrigo, experiencias=["XPTO"])
print(curriculo_rodrigo)
curriculo_rodrigo.adiciona_experiencia("XYZ")
print(curriculo_rodrigo)
