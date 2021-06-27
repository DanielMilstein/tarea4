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

double pais::distancia(int c1, int c2){ //prims desde c1 hasta que encuentre c2?
	if (edges.empty()){
		calcular();
	}

	//Copiar edges.
	map<pair<int,int>, double> vias = edges;

	pair<int,int> ideal = make_pair(c1,c2);
	pair<int,int> laedi = make_pair(c2,c1);
	map<pair<int,int>, double>::iterator itr;

	vector<pair<int,int>> incluye_c1;
	for (itr = vias.begin(); itr != vias.end(); itr++)
	{
		if (itr->first == ideal || itr->first == laedi){	//Caso base
			return itr->second;
		}

		if (itr->first.first == c1 || itr->first.second == c1)
		{
			incluye_c1.push_back(itr->first);
			itr = vias.erase(itr);
		}

	}
	vector<pair<int, int>> camino;
	vector<pair<int, int>> camino_def;
	unsigned int menor = 12345678;
	map<pair<int, int>, double> vias2 = vias;
	for (unsigned int i = 0; i < incluye_c1.size(); ++i)
	{
		camino.clear();
		camino.push_back(incluye_c1[i]);

		for(unsigned int k = 0; k < camino.size(); k++)
		{
			vias2 = vias;	
			for (map<pair<int,int>, double>::iterator iter = vias2.begin(); iter != vias2.end(); iter++)
			{
					if (iter->first.first == camino[k].first || iter->first.second == camino[k].first ||
						iter->first.first == camino[k].second || iter->first.second == camino[k].second)
					{
						camino.push_back(iter->first);
						iter = vias2.erase(iter);
					}

			}

			if (c2 == camino[k].first || c2 == camino[k].second)
			{
				if (camino.size() < menor){
					menor = camino.size();
				}
				break;
			}
		}
		if (camino_def.size() == 0)
		{
			camino_def = camino;
		}
		// if (camino_def.size() > menor)
		// {

		// 	camino_def = camino;
		// }
	}

	for (vector<pair<int,int>>:: iterator ij = camino_def.begin(); ij != camino_def.end(); ij++)
	{
		cout << ij->first << ", " << ij->second << endl;
	}
	
	return 0;


}


