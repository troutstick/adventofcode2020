with open("inputs/day1.txt", "r") as file:
    L = [int(line) for line in file]
    S = set(L)
    length = len(L)
    for n in S:
        if (2020 - n) in S:
            print(f"The answer is {n}*{2020 - n} = {n*(2020 - n)}")
            break

    done = False
    for i in range(length):
        for j in range(i+1,length):
            pair_val = L[i] + L[j]
            if (2020 - pair_val) in S:
                print(f"The three numbers are {L[i]}, {L[j]}, {2020 - pair_val}, the product of which is {L[i]*L[j]*(2020 - pair_val)}")
                done = True
                break
        if done:
            break


    
