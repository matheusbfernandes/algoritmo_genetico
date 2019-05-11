import numpy as np


class AG(object):
    def __init__(self, limitantes, tam_populacao_inicial, taxa_mutacao, taxa_crossover, num_bits=10):
        self.limite_inferior = limitantes[0]
        self.limite_superior = limitantes[1]
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.num_bits = num_bits
        self.populacao = self._gerar_populacao_inicial(tam_populacao_inicial)
        for cromossomo in self.populacao:
            print(cromossomo)
            print(self._mapear_cromossomo(cromossomo))

    def _gerar_populacao_inicial(self, tam):
        cromossomos = []
        for _ in range(tam):
            cromossomos.append(np.random.randint(2, size=self.num_bits))
        return cromossomos

    @staticmethod
    def _converter_binario(cromossomo):
        s = "0b"
        for bit in cromossomo:
            s += str(bit)
        return int(s, 2)

    def _mapear_cromossomo(self, cromossomo):
        return self.limite_inferior + (self.limite_superior - self.limite_inferior) * self._converter_binario(cromossomo) / (2 ** self.num_bits - 1)