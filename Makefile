CC = g++
EXE = exe
FLAGS = -std=c++11 -Wall -Wextra -Wundef -Werror -Wuninitialized -Winit-self
DEPS = pais.o
DEPSH = $(DEPS:.o=.h)


$(EXE): main.o $(DEPS)
# 	$(CC) -o $(EXE) $(FLAGS) -Wl,-rpath=. main.o -L. -lfiguras
	$(CC) -o $(EXE)  $^


# $(lib): $(DEPS)
# 	$(CC) -shared $^ -o $(lib)

%.o: %.cpp %.h
	$(CC) $(FLAGS) -o $@ -c $<

main.o: main.cpp $(DEPSH)
	$(CC) $(FLAGS) -o main.o -c main.cpp

all: clean $(EXE)

run: $(EXE)
	./$(EXE)

clean:
	rm -f *.o *so
	rm -f $(EXE)
