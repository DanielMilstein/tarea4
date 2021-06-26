#include "pais.h"
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

pais::pais(){

}

void pais::agregar_ciudad(double x, double y){
	city ciudad(x, y, n);
	ciudades.push_back(ciudad);
	n++;
}	

double pais::calcular(){
	vector<city> visited;
	vector<city> unvisited = ciudades;
	double x = 0;

	visited.push_back(unvisited.back());
	unvisited.pop_back();

	while (!unvisited.empty()){
		double min = 1000;
		int nombre_v;
		int nombre_uv;

		for (unsigned int i = 0; i < visited.size(); i++)
		{
			for (unsigned int k = 0; k < unvisited.size(); k++)
			{
				double d = distancia_edge(visited[i].coordX, visited[i].coordY, 
					unvisited[k].coordX, unvisited[k].coordY);
				if (d < min){
					min = d;
					nombre_v = visited[i].nombre;
					nombre_uv = unvisited[k].nombre;
				}
			}
			
		}
		pair<int, int> par = make_pair(nombre_v, nombre_uv);
		edges[par] = min;

		for (unsigned int i = 0; i < unvisited.size(); i++)
		{
			if (unvisited[i].nombre == nombre_uv)
			{
				visited.push_back(unvisited[i]);
				unvisited.erase(unvisited.begin() + i);
			}
		}
	}

	map<pair<int, int>, double>::iterator itr;
	for (itr = edges.begin(); itr != edges.end(); itr++){
		x += itr->second;
	}
	return x;
}

double pais::distancia_edge(double x1, double y1, double x2, double y2){		// √((x₂-x₁)² + (y₂-y₁)²) 

	double dist = sqrt((x2 - x1) * (x2 - x1) 
		+ (y2 - y1) * (y2 - y1));
	return dist;


}

double pais::distancia(int c1, int c2){
	if (edges.empty()){
		calcular();
	}

	//Copiar edges.
	map<pair<int,int>, double> vias = edges;

	pair<int,int> ideal = make_pair(c1,c2);
	pair<int,int> laedi = make_pair(c2,c1);
	map<pair<int,int>, double>::iterator i;
	for (i = vias.begin(); i != vias.end(); i++)
	{
		if (i->first == ideal || i->first == laedi){	//Caso base
			return i->second;
		}
	}

	map<pair<int,int>, double> vias_imag;	
	//Agregar todos las otras vias posible pero con valores infinitos.
	for (unsigned int i = 0; i < ciudades.size(); i++)
	{
		for (unsigned int k = 0; k < ciudades.size(); k++)
		{
			if (i==k){
				continue;
			}
			pair<int,int> inf = make_pair(i,k);
			vias_imag[inf] = 100000;
		}
	}

	for (map<pair<int,int>, double>::iterator it = vias.begin(); it != vias.end(); ++it)
	{
		vias_imag[it->first] = it->second;
		pair<int,int> alv = make_pair(it->first.second, it->first.first);
		vias_imag[alv] = it->second;
	}
	//Hasta aqui esto podria ser innecesario.

	//Imprime todas las vias 'imaginarias'
	for (map<pair<int,int>, double> ::iterator i = vias_imag.begin(); i != vias_imag.end(); ++i)
	{
		cout << i->first.first << "<->" << i->first.second << ": " << i->second << endl;
	}






	return 0;


}