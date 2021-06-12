#include "pais.h"
#include <cmath>

using namespace std;

pais::pais(){

}



void pais::agregar_ciudad(double x, double y){
	ciudades[n] = make_pair(x,y);
	n++;
}	






double pais::calcular(){
	double x = 42;
	return x;
}









double pais::distancia(int c1, int c2){		// √((x₂-x₁)² + (y₂-y₁)²) pero en verdad no
	pair<double, double> ciud1 = ciudades[c1];
	pair<double, double> ciud2 = ciudades[c2];

	double dist = sqrt((ciud2.first - ciud1.first) * (ciud2.first - ciud1.first) 
		+ (ciud2.second - ciud1.second) * (ciud2.second - ciud1.second));
	return dist;


}
