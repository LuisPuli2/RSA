# coding=utf-8
# RSA
import random

# Recibe dos números primos
def generaLlaves ():
	# Generamos dos números aleatorios (no tan grandes).
	p = getPrimo(10000,20000);
	q = getPrimo(10000,20000);
	# Calcular N = p*q
	N = p*q
	# Phi(N) = (p-1)(q-1)
	PhiN = (p-1)*(q-1)
	# Encontrar e que sea coprimo con N
	e = getCoprimo(N)
	# Calcular d que sea el inverso multiplicativo de e mod N
	pass

def cifra (e,N,M):
	pass

# Dados el mensaje, la llave privada y el entero N, decifra el mensaje. 
def decifra (d,N,M):
	pass

# Funciones Auxiliares #

# Dados dos números n y m 
def getPrimo(n,m):
	p = random.randint(n, m);
	# Lo hacemos impar si no lo es.
	if p%2 == 0:
		p += 1
	# Encontramos el primo más cercano. 
	while not esPrimo(p):
		# Lo incrementamos en 2 para solo contar impares.
		p += 2

	print(p)
	return p

# True si n es primo, false en otro caso
def esPrimo (p):
	limit = int(p**(.5))
	for i in range (2,limit+1):
		if p%i == 0:
			return False
	return True

# Dado un número, regresa un número que se primo relativo con él.
def getCorimo(n):
	pass

# Dados n y m, regresa su máximo común divisor.
def mcd (n,m):
	pass


if __name__ == '__main__':
	generaLlaves()