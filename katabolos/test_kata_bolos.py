import unittest

def computer_score(frames):
    score = 0
    index = 0
    while index < len(frames):
        frame = frames[index]
        if frame == "/":
            score = 10 - int(frames[index - 1]) + int(frames[index + 1])
        elif frame != '-':
            score += int(frame)
        index = index + 1
    return score

class BowlingTests(unittest.TestCase):
    def test_all_zeros(self):
        frames = "----------"
        score = computer_score(frames)
        self.assertEqual(0,score)

    def test_all_ones(self):
        frames = "1111111111"
        score = computer_score(frames)
        self.assertEqual(10,score)

    def test_a_spare(self): #semipleno
       frames = "1/111111111"
       score = computer_score(frames)
       self.assertEqual(19,score)

    def test_two_spare(self): # dos semipleno
       frames = "1/11111/111"
       score = computer_score(frames)
       self.assertEqual(28,score)

    def test_a_strike(self): #un pleno
        frames = "x111111111"
        score = computer_score(frames)
        self.assertEqual(20,score)