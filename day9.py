def detect(numset, curr):
    for i in numset:
        if curr - i in numset:
            return True
    return False

with open('inputs/day9.txt', 'r') as file:
    numbers = [int(i) for i in file]
    num_prev = 25
    bad_xmas = None
    for i in range(num_prev, len(numbers)):
        S = set(numbers[i-num_prev:i])
        curr = numbers[i]
        if not detect(S, curr):
            bad_xmas = curr
            print(f"The answer to part 1 is {bad_xmas}")
            break
    
    start = 0
    end = 0
    total = 0            
    while total != bad_xmas:
        if total < bad_xmas:
            total += numbers[end]
            end += 1
        else:
            total -= numbers[start]
            start += 1
    L = numbers[start:end+1]
    print(f"The answer to part 2 is {max(L) + min(L)}")
