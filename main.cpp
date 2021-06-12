#include <iostream>
#include <string>
#include <map>
#include"pais.h"
#include<random>


using namespace std;

int main()
{
	random_device rd;
	default_random_engine rng(rd());
	uniform_real_distribution<double> distr(0, 500);
	int nciud = 2000;


	pais p;

	for (int i = 0; i < nciud; i++)
	{
		double x = distr(rng);
		double y = distr(rng);
		p.agregar_ciudad(x, y);
	}


	for (int i = 0; i < nciud; i++)
	{
		cout << i << ".- " << p.ciudades[i].first << ", " << p.ciudades[i].second << endl;
	}

	for (int i = 0; i < nciud; ++i)
	{
		for (int k = 0; k < nciud; k++)
		{
			if (k != i){


				cout << "Distancia entre " << i << " y " << k << " es: " << p.distancia(i, k) << endl;
			}
		}
	}


	return 0;
}
