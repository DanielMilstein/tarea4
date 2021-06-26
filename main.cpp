#include <iostream>
#include <string>
#include <map>
#include"pais.h"
#include"city.h"
#include<random>


using namespace std;

int main()
{
	random_device rd;
	default_random_engine rng(rd());
	uniform_real_distribution<double> distr(0, 500);
	int nciud = 10;


	pais p;

	for (int i = 0; i < nciud; i++)
	{
		double x = distr(rng);
		double y = distr(rng);
		p.agregar_ciudad(x, y);
	}
	vector<city>::iterator it;
	for (it = p.ciudades.begin() ; it != p.ciudades.end(); it++)
	{
		cout << it->nombre << ": " << it->coordX << " ,"<< it->coordY << endl;
	}

	cout << "La distancia total es: " << p.calcular() << endl;


	map<pair<int, int>, double>::iterator itr;
	for(itr = p.edges.begin(); itr != p.edges.end(); itr++){
		cout << itr->first.first << " <-> " << itr->first.second << ": " << itr->second << endl;
	}



	cout << "La distancia total es: " << p.calcular() << endl;

	cout << "La distancia entre 9 y 0 es: " << p.distancia(0,9) << endl;



	return 0;
}
