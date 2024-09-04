import unittest
from src.kataTenis import *
# Crear un partido entre dos jugadores


# Simular un juego
class TestPredicciones(unittest.TestCase):
    def test_muestraPuntosJuegos(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto jugador 1
        self.assertEqual(game.juego(),"0 - 0")
    
    def test_2muestraPuntosJuegos(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto jugador 1
        self.assertEqual(game.match_score(),"Sets: Player 1 0 - 0 Player 2, Games: Player 1 1 - 0 Player 2, Points: Player 1 0 - 0 Player 2")
    
    def test_muestraPuntosJuegos2(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        self.assertEqual(game.match_score(),"Sets: Player 1 0 - 0 Player 2, Games: Player 1 3 - 0 Player 2, Points: Player 1 0 - 0 Player 2")
    
    def test_muestraPuntosJuegos3(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 2")#40-A
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        self.assertEqual(game.match_score(),"Sets: Player 1 0 - 0 Player 2, Games: Player 1 2 - 1 Player 2, Points: Player 1 0 - 0 Player 2")
    
    def test_muestraSet(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        self.assertEqual(game.match_score(),"Sets: Player 1 1 - 0 Player 2, Games: Player 1 0 - 0 Player 2, Points: Player 1 0 - 0 Player 2")

    def test_muestraSet2(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1 (set)
        with self.assertRaises(ValueError) as context:
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 1")#Punto Jugador 1
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 1")#Punto Jugador 1
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 2")#40-40
            game.ganaPunto("Player 1")#A-40
            game.ganaPunto("Player 1")#Punto Jugador 1
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 1")#Punto Jugador 1
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 1")#Punto Jugador 1
            game.ganaPunto("Player 1")#15-0
            game.ganaPunto("Player 2")#15-15
            game.ganaPunto("Player 1")#30-15
            game.ganaPunto("Player 1")#40-15
            game.ganaPunto("Player 2")#40-30
            game.ganaPunto("Player 2")#40-40
            game.ganaPunto("Player 1")#A-40
            game.ganaPunto("Player 1")#Punto Jugador 1
        self.assertEqual(str(context.exception), f"Se han superado el límite de {game.max_sets} sets")

    def test_TieBreak(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#1-0 (TB)
        self.assertEqual(game.match_score(),"Sets: Player 1 0 - 0 Player 2, Games: Player 1 6 - 6 Player 2, Points: Tie Break -> Player 1 1 - 0 Player 2")

    def test_TieBreak2(self):
        game = Tenis("Player 1", "Player 2",1)
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 2")#0-15
        game.ganaPunto("Player 2")#0-30
        game.ganaPunto("Player 2")#0-40
        game.ganaPunto("Player 2")#Punto Jugador 2
        game.ganaPunto("Player 1")#15-0
        game.ganaPunto("Player 2")#15-15
        game.ganaPunto("Player 1")#30-15
        game.ganaPunto("Player 1")#40-15
        game.ganaPunto("Player 2")#40-30
        game.ganaPunto("Player 2")#40-40
        game.ganaPunto("Player 1")#A-40
        game.ganaPunto("Player 1")#Punto Jugador 1
        game.ganaPunto("Player 1")#1-0 (TB)
        game.ganaPunto("Player 1")#2-0 (TB)
        game.ganaPunto("Player 1")#3-0 (TB)
        game.ganaPunto("Player 1")#4-0 (TB)
        game.ganaPunto("Player 1")#5-0 (TB)
        game.ganaPunto("Player 2")#5-1 (TB)
        game.ganaPunto("Player 2")#5-2 (TB)
        game.ganaPunto("Player 2")#5-3 (TB)
        game.ganaPunto("Player 2")#5-4 (TB)
        game.ganaPunto("Player 2")#5-5 (TB)
        game.ganaPunto("Player 2")#5-6 (TB)
        game.ganaPunto("Player 1")#6-6 (TB)
        game.ganaPunto("Player 1")#7-6 (TB)
        game.ganaPunto("Player 1")#8-6 (TB) (gana punto)
        self.assertEqual(game.match_score(),"Sets: Player 1 1 - 0 Player 2, Games: Player 1 0 - 0 Player 2, Points: Player 1 0 - 0 Player 2")
#Probar ventajas (hecho)

#Probar sets (hecho)
#Poner limite sets
#Programar empate a 6 en juegos
#Programar final del partido (al mejor de 3 o 5 sets depende torneo)