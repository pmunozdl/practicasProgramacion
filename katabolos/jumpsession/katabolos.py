class Partida:
    rondas = ["esta", "lista", "no", "sirve", "para", "absolutamente", "nada", "hola", "hola", "hola"]
 
    def te_paso_las_rondas(self, las_rondas):
        self.rondas = las_rondas
    def resultado(self):
        self.resultado_final = 0
        estraik = False
        for nr,elemento in enumerate(self.rondas):
            if estraik:
                if self.es_strike(elemento):
                    self.acumular(10+ self.rondas[nr+1][0])

                else:
                    self.acumular(elemento[0]+ elemento[1])
            estraik = self.es_strike(elemento)
            if nr == 10: 
                break
            self.acumular(elemento [0] + elemento[1])
        return self.resultado_final
    
    def acumular(self, valor):
        self.resultado_final = self.resultado_final + valor
    def es_strike(self,elemento):
        return elemento[0] == 10