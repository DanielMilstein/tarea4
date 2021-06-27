%module roadBuilder
%{
	#include"pais.h"
	#include"city.h"	
%}

%include"city.h"
%include"pais.h"

%include"std_vector.i"
%include"std_map.i"
%include"math.i"

namespace std{
	%template(vectorCity) vector<city>;
}