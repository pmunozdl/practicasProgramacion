class Bolos:

    def calcularRonda(self, partida, indice):
        return partida[indice][0] + partida[indice][1]

    def calcularPuntuacion(self, partida):
        resultado = 0

        for indice in range(10):
            if self.calcularRonda(partida, indice) == 10:
                resultado = resultado + self.comprobar(partida, indice)
            else:
                resultado = resultado + self.calcularRonda(partida, indice)
 
        return resultado

    def comprobar(self, partida, indice): #Comprueba si es strike o spare

        if (partida[indice][0] == 10 and partida[indice][1] == 0): # es strike

            strike = self.calcularRonda(partida, indice +1)

            if strike == 10:

                if partida[indice + 1][0] == 0:
                    return 10 + strike
                else:
                    strike = 10 + partida[indice + 2][0]
            return 10 + strike

        else: # es spare
            spare = partida[indice + 1][0]
            return 10 + spare
 