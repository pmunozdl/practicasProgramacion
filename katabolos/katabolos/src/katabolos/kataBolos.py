class kataBolos:
    '''
    #def __init__(self):
     #   self.rolls = []

   # def roll(self, pins):
      #  self.rolls.append(pins)

   # def score(self):
      #  result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        return self.roll[rollIndex] + self.rolls[rollIndex + 1]        

'''
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
            if index < len(frame_scores) - 2:
                score += strike_score(frame_scores, index)
        elif frame_score != '-':
            score += int(frame_score)
        index = index + 1
        rolls = rolls + 1
    return score

def spare_score(frame_scores, index):
  # if frame_scores[index + 1] == '/':
     #   return 10 - frame_value(frame_scores[index])
    if index < 18:
        return 10 - frame_value(frame_scores[index - 1]) + frame_value(frame_scores[index + 1])
    elif index == 19:
        return 10 - frame_value(frame_scores[index - 1])

def strike_score(frame_scores, index):
    if frame_scores[index + 2] == '/':
        return 20
    elif index == 18:  
        return 10 + frame_value(frame_scores[index + 1])
    elif index == 19:
        return 10
    elif index < 18:
        return 10 + frame_value(frame_scores[index + 1]) + frame_value(frame_scores[index + 2])

def frame_value(frame):
    if frame == 'X':
        return 10
    if frame == '-':
        return 0
    return int(frame)