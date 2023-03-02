class Bolos:

    def bowling_score(self, frames):
        print(list(enumerate(frames)))
        acc = 0
        for index, x in list(enumerate(frames)):
            if x[0] == 10:
                if frames[index + 1][0] == 10:
                    tmp = frames[index + 1][0]
                    tmp2 = frames[index + 2][0]
                    acc += x[0] + tmp + tmp2
                else:
                    tmp = sum(frames[index + 1])
                    acc += x[0] + tmp
                    print(acc)
            else:
                if int(sum(x)) == 10:
                    tmp = frames[index + 1][0]
                    acc += sum(x) + tmp
                else:
                    acc += sum(x)
                    print(acc)
        return acc