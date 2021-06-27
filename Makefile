CC = g++
EXE = exe
FLAGS = -std=c++11 -Wall -Wextra -Wundef -Werror -Wuninitialized -Winit-self
DEPS = pais.o city.o
DEPSH = $(DEPS:.o=.h)
PYmac=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Headers/
PY=/usr/include/python3.8/


_roadBuilder.so: roadBuilder.cxx pais.o city.o
	g++ -fPIC -c roadBuilder.cxx -o roadBuilder.o -I$(PY)
	g++ -shared roadBuilder.o pais.o city.o -o _roadBuilder.so

$(EXE): main.o $(DEPS)
# 	$(CC) -o $(EXE) $(FLAGS) -Wl,-rpath=. main.o -L. -lfiguras
	$(CC) -o $(EXE)  $^

roadBuilder.cxx: pais.i pais.h city.h
	swig -python -c++ pais.i
	mv pais_wrap.cxx roadBuilder.cxx




%.o: %.cpp %.h
	$(CC) $(FLAGS) -fPIC -o $@ -c $<

main.o: main.cpp $(DEPSH)
	$(CC) $(FLAGS) -o main.o -c main.cpp

all: clean $(EXE)

run: $(EXE)
	./$(EXE)

clean:
	rm -f *.o *so
	rm -f $(EXE)
	rm -f roadBuilder.*
	rm -f -r __pycache__
	rm -f roadBuilder.py



# PY=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Headers/


# probador: main.o lib.o
# 	g++ -o $@ $^

# roadBuilder.cxx: pais.i pais.h city.h
# 	swig -python -c++ pais.i

#Va primero
# _roadBuilder.so: roadBuilder.cxx pais.o city.o
# 	g++ -fPIC -c roadBuilder.cxx -o roadBuilder.o -I$(PY)
# 	g++ -shared roadBuilder.o pais.o city.o -o _libroadBuilder.so
