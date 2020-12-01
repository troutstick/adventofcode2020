with open("inputs/day1.txt", "r") as file:
    L = [int(line) for line in file]
    length = len(L)
    for i in range(length):
        for j in range(i+1,length):
            if L[i] + L[j] == 2020:
                print(f"The answer is {L[i]}*{L[j]} = {L[i]*L[j]}")
