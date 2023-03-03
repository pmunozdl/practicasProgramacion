class kataBolos:

    def bowling_score(self, frames):
        score = 0
        index = 0
        rolls = 0
        while index < len(frames) and rolls < 20:
            frames = frames.replace(" ", "")
            frame_score= frames[index]
            if frame_score == "/":
                score += self.spare_score(frames, index)
            elif frame_score == 'X':
                rolls = rolls + 1
                if index < len(frames) - 2:
                    score += self.strike_score(frames, index)
            elif frame_score != '-':
                score += int(frame_score)
            index = index + 1
            rolls = rolls + 1
        return score
    
    def get_frames(self, frames):
        self.frames = frames

    def spare_score(self, frame_scores, index):
    # if frame_scores[index + 1] == '/':
        #   return 10 - frame_value(frame_scores[index])
        if index < 18:
            return 10 - self.frame_value(frame_scores[index - 1]) + self.frame_value(frame_scores[index + 1])
        elif index == 19:
            return 10 - self.frame_value(frame_scores[index - 1])

    def strike_score(self,frame_scores, index):
        if frame_scores[index + 2] == '/':
            return 20
        elif index == 18:  
            return 10 + self.frame_value(frame_scores[index + 1])
        elif index == 19:
            return 10
        elif index < 18:
            return 10 + self.frame_value(frame_scores[index + 1]) + self.frame_value(frame_scores[index + 2])

    def frame_value(self, frame):
        if frame == 'X':
            return 10
        if frame == '-':
            return 0
        return int(frame)