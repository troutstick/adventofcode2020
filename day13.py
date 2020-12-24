with open('inputs/day13.txt', 'r') as f:
    depart_time = int(f.__next__())
    buses = [x.strip() for x in f.__next__().split(',')]
    buses_in_service = [int(i) for i in filter(lambda c: c != 'x', buses)]
    wait_times = {(b - depart_time % b) : b for b in buses_in_service}
    min_time = min(wait_times)
    print(f"The answer to part 1 is {min_time * wait_times[min_time]}")

    bus_indexes = {int(buses[i]) : i for i in range(len(buses)) if buses[i] != 'x'}
    print(bus_indexes)