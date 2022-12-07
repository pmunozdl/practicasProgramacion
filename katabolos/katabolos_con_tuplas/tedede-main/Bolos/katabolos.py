class Bolos:

    def calcularScore(self, partida):
        print(list(enumerate(partida)))
        acc = 0
        for index, x in list(enumerate(partida)):
            if x[0] == 10:
                if partida[index + 1][0] == 10:
                    tmp = partida[index + 1][0]
                    tmp2 = partida[index + 2][0]
                    acc += x[0] + tmp + tmp2
                else:
                    tmp = sum(partida[index + 1])
                    acc += x[0] + tmp
                    print(acc)
            else:
                if sum(x) == 10:
                    tmp = partida[index + 1][0]
                    acc += sum(x) + tmp
                else:
                    acc += sum(x)
                    print(acc)
        return acc
