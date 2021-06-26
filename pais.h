#ifndef _PAIS
#define _PAIS
#include<vector>
#include <map>
#include "city.h"


using namespace std;


class pais
{
public:
		pais();
		

		vector<city> ciudades;
		int n = 0;

		map<pair<int, int>, double> edges;


		void agregar_ciudad(double, double);	//Obvio
		double calcular(); 		//Longitud total de la via.
		double distancia_edge(double, double, double, double);		//Entre 2 ciudades.	
		double distancia(int, int);
};

#endif