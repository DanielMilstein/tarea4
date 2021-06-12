#ifndef _PAIS
#define _PAIS
#include<map>


using namespace std;


class pais
{
public:
		pais();
		

		map<int, pair<double, double>> ciudades;
		int n = 0;


		void agregar_ciudad(double, double);	//Obvio
		double calcular(); 		//Longitud total de la via.
		double distancia(int, int);		//Entre 2 ciudades.

	
};

#endif