import unittest

def computer_score(frame_scores):
    score = 0
    index = 0
    rolls = 0
    while index < len(frame_scores) and rolls < 20:
        frame_score= frame_scores[index]
        if frame_score == "/":
            score += spare_score(frame_scores, index)
        elif frame_score == 'X':
            rolls = rolls + 1
            if index < len(frame_scores) -2:
                score += strike_score(frame_scores, index)
        elif frame_score != '-':
            score += int(frame_score)
        index = index + 1
        rolls = rolls + 1
    return score

def spare_score(frame_scores, index):
    return 10 - frame_value(frame_scores[index - 1]) + frame_value(frame_scores[index + 1])

def strike_score(frame_scores, index):
    if frame_scores[index + 2] == '/':
        return 20
    return 10 + frame_value(frame_scores[index + 1]) + frame_value(frame_scores[index + 2])

def frame_value(frame):
    if frame == 'X':
        return 10
    if frame == '-':
        return 0
    return int(frame)

    
class BowlingTests(unittest.TestCase):
    def test_all_zeros(self):
        frames = "--------------------"
        score = computer_score(frames)
        self.assertEqual(0,score)

    def test_all_ones(self):
        frames = "11111111111111111111"
        score = computer_score(frames)
        self.assertEqual(20,score)

    def test_a_spare(self): #semipleno
       frames = "1/1111111111111111111"
       score = computer_score(frames)
       self.assertEqual(29,score)

    def test_two_spare(self): # dos semipleno
       frames = "1/11111/1111111111111"
       score = computer_score(frames)
       self.assertEqual(38,score)

    def test_a_strike(self): #un pleno
        frames = "x1111111111111111111"
        score = computer_score(frames)
        self.assertEqual(30,score)

    def test_a_spare_then_strike(self): #semipleno y luego pleno
        frames = "1/X11111111111111111"
        score = computer_score(frames)
        self.assertEqual(48,score)

    def test_three_strikes(self): #tres plenos
        frames = "XXX11111111111111111"
        score = computer_score(frames)
        self.assertEqual(30+21+12+14,score)

    def test_a_spare_with_zero(self): #semipleno
       frames = "1/-1111111111111111111"
       score = computer_score(frames)
       self.assertEqual(27,score)
    
    def test_perfect_game(self):
        frames = "XXXXXXXXXXXX" #añadimos dos más por las tiradas extras con plenos
        score = computer_score(frames)
        self.assertEqual(300,score)
    
    def test_spare_at_end(self):
        frames = "------------------/5"
        score = computer_score(frames)
        self.assertEqual(15,score)

    def test_almost_perfect_game(self):
        frames = "XXXXXXXXXX9/"
        score = computer_score(frames)
        self.assertEqual(289,score)