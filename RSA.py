# coding=utf-8
# RSA
import random

# Variables globales.
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

# Genera las llaves para cifrar/descifrar con RSA.
def generaLlaves ():
	# Generamos dos números aleatorios (no tan grandes).
	p = getPrimo(1000,2000);
	q = getPrimo(1000,2000);
	# Calcular N = p*q
	N = p*q
	# Phi(N) = (p-1)(q-1)
	PhiN = (p-1)*(q-1)
	# Encontrar e que sea coprimo con N
	e = getCoprimo(PhiN)
	# Calcular d que sea el inverso multiplicativo de e mod N
	d = inverso(e,PhiN)

	print("Tus llaves públicas son: ")
	print(e,PhiN)
	print("Tu llave privada es: ")
	print("("+ str(d)+") \n")

	return (e,N,d)

# Dadas las llaves públicas y un mensaje, los cifra.
def cifra (e,N,M):
	print("Empieza cifrado, esto puede tardar un poco")
	cifrado = []
	temp = []
	# Recorremos el mensaje
	for char in M:
		# Ignoramos los espacios.
		# if char == ' ': continue
		m = alfabeto.index(char);
		# Agregamos el caracter ya cifrado.
		cifrado.append(modPow(m,e,N))

	return cifrado

# Dados el mensaje, la llave privada y el entero N, decifra el mensaje. 
def decifra (d,N,M):
	print("Empieza decifrado, esto puede tardar un poco")
	decifrado = ""
	for m in M:
		char = modPow(m,d,N)
		decifrado += alfabeto[char]

	print("Mensaje decifrado: ")
	print(decifrado)




# Funciones Auxiliares #

# Dados dos números n y m regresa un primo aproximado entre ese rango.
def getPrimo(n,m):
	p = random.randint(n, m);
	# Lo hacemos impar si no lo es.
	if p%2 == 0:
		p += 1
	# Encontramos el primo más cercano. 
	while not esPrimo(p):
		# Lo incrementamos en 2 para solo contar impares.
		p += 2

	return p

# True si n es primo, false en otro caso
def esPrimo (p):
	limit = int(p**(.5))
	for i in range (2,limit+1):
		if p%i == 0:
			return False
	return True

# Dado un número, regresa un número que se primo relativo con él.
def getCoprimo(n):
	e =  random.randint(1,n)
	while not (mcd(e,n) == 1):
		e = random.randint(1,n)
	return e

# Dados n y m, regresa su máximo común divisor.
def mcd (a,b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

def modPow (n,e,N):
	return (n**e)%N

# Método auxiliar para encontrar el inverso multiplicativo.
# Utiliza el algoritmo extendido de euclides.
def inverso(b, a):
	N = a
	x0, x1, y0, y1 = 1, 0, 0, 1
	while a != 0:
		q, b, a = b // a, a, b % a
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1

	# Para no regresar un número negativo.
	while(x0 < 0):
		x0 += N
	return x0


if __name__ == '__main__':
	e,N,d = generaLlaves()
	M = "y vos sabes en cambio extraer de ese paramo mi germen	 de alegria y regarlo mirandolo"
	# Lo pasamos a mayúsculas.
	M = M.upper();
	# Quitar acentos...
	# Cifrado
	cifrado = cifra(e,N,M)
	# Decifrado
	decifra (d,N,cifrado)