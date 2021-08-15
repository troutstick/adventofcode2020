SRC=cpp
FILES=$(SRC)/main.cpp $(SRC)/day1.cpp



aoc_cpp : $(FILES)
	g++ -c $(FILES)
	g++ -o target/aoc2020.out main.o day1.o
	./target/aoc2020.out