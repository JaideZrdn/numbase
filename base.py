class Numero:
    def __init__(self, valor, base):
        self.base = base
        self.valor = valor.upper()
        self.b10 = self._base10()
        self._valida()  # Verifica se o número está na base correta logo que o objeto é criado

    def __repr__(self):  # Método que retorna a representação do objeto
        if self.base != 10:
            return ("Número: " + str(self.valor) + " Base: " + str(self.base) +
                    "\nO número na base 10 é " + str(self.b10))
        else:
            return "Número: " + str(self.valor) + " Base: " + str(self.base)

    def mudabase(self, basedestino):  # Método que converte o número para a base desejada
        if basedestino < 2 or basedestino > 35:  # Verifica se a base é válida
            raise ValueError("Coloque uma base válida entre oi intervalo 2-->35")
        return Numero(self._convertebase(basedestino), basedestino)

    def _valida(self):  # Método que verifica se o número está numa base válida
        for i in range(len(self.valor)):
            digito = self._convertedigitos(i)
            if digito >= self.base:
                raise ValueError('O número digitado não está compreendido  na base escolhida')

    def _convertebase(self, basedestino):  # Método suporte para a conversão
        # Método caso as bases sejam iguais
        if self.base == basedestino:
            return self.valor
        # Método caso as bases não tenham relação logaritmina perfeita
        quociente = self.b10 // basedestino
        resto = self.b10 % basedestino
        if quociente == 0:
            if resto > 9:  # Verifica se o resto é uma letra e traduz ela para seu representante na base Hexa
                resto = chr(resto + ord('A') - 10)
            return str(resto)
        nova = Numero(str(quociente), 10)  # O objeto nova é criado para que o método seja chamado recursivamente
        if resto > 9:
            resto = chr(resto + ord('A') - 10)
        return nova._convertebase(basedestino) + str(resto)  # Concatena o resto com o resultado da chamada recursiva

    def _base10(self):  # Método que transforma o número pra base 10
        numerob10 = 0
        for i in range(len(self.valor)):
            digito = self._convertedigitos(i)
            numerob10 += digito*(self.base**(len(self.valor) - i - 1))  # calcula o valor em base 10 digíto a digíto
        return numerob10

    def _convertedigitos(self, i):
        char = self.valor[i]
        digito = 0
        if '0' <= char <= '9':  # Verifica se é um número
            digito = int(char)
        if 'A' <= char <= 'Z':  # Verifica se é uma letra e traduz ela para seu representante na base Hexa
            digito = int(ord(char) - ord('A') + 10)
        return digito
