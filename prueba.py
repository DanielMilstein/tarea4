import roadBuilder as rb
from random import uniform, sample

def main():
	nciud = 10

	p = rb.pais()

	for i in range(nciud):
		p.agregar_ciudad(uniform(0,500), uniform(0,500))

	print(f"km construidos: {p.calcular()}")

	j,k = sample(range(nciud), 2)

	#print(f"Distancia a recorrer entre ciudades {j} y {k}: {p.distancia(j, k)}")
#Main
if __name__ == "__main__":
	main()