class Escalera:

	def __init__(self,escalones):
		'''Este metodo inicializa los atributos del objeto Escalera creado.
		Almacena para cada instancia, una cantidad entera de escalones que tiene
		la escalera y la cantidad de formas posibles que hay para subirla.'''
		if type(escalones) != int:
			print("Escalera() debe recibir un numero entero y recibio un",type(escalones))
			return
		self.escalones = escalones
		self.formas = Escalera.formas_posibles_subir_escalera(escalones)

	def mostrar_formas(self):
		'''Este metodo muestra en pantalla la cantidad de formas posibles de subir una escalera,
		acorde a la cantidad de escalones.'''
		if self.formas == 0:
			print("No hay forma de subir esta escalera porque tiene",self.escalones,"escalones.")
		else:
			print("Hay",self.formas,"formas posibles de subir una escalera de",self.escalones,"escalones")

	@staticmethod
	def formas_posibles_subir_escalera(n):
		'''Este metodo recibe la cantidad de escalones de una escalera y devuelve 
		la cantidad de formas posibles para subir dicha escalera.'''
		if n < 1:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 2
		else:
			return Escalera.formas_posibles_subir_escalera(n-1)+Escalera.formas_posibles_subir_escalera(n-2)

#Tests Unitarios
'''En estas pruebas unitarias, creo tres objetos escalera con la cantidad de escalones dados en ejemplo
del problema y verifico que la cantidad de formas correctas coincida.
Luego creo otros cuatro objetos mas, verifico que la cantidad de formas sea correcta y que los datos
incongruentes sean manejados de manera adecuada.
Finalmente compruebo que el objeto "Escalera" unicamente puede recibir numeros enteros como parametro.'''
def main():
	escalera_1 = Escalera(1)
	escalera_2 = Escalera(2)
	escalera_3 = Escalera(3)
	assert(escalera_1.formas == 1)
	assert(escalera_2.formas == 2)
	assert(escalera_3.formas == 3)

	escalera_4 = Escalera(8)
	escalera_5 = Escalera(9)
	escalera_6 = Escalera(10)
	escalera_7 = Escalera(-20)
	assert(escalera_4.formas == 34)
	assert(escalera_5.formas == 55)
	assert(escalera_6.formas == 89)
	assert(escalera_4.formas+escalera_5.formas == escalera_6.formas)
	assert(escalera_7.formas == 0)
	
	escalera_5.mostrar_formas()
	escalera_6.mostrar_formas()
	escalera_7.mostrar_formas()
	
	Escalera(1.5)
	Escalera('hola')
	Escalera([])

main()