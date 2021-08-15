SRC=cpp
FILES=$(SRC)/*.cpp
OBJ=*.o



aoc_cpp : $(FILES)
	g++ -c $(FILES)
	g++ -o target/aoc2020.out $(OBJ)
	./target/aoc2020.out