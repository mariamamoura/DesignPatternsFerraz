import time

class AgenteViagem(object):
	def __init__(self):
		print("Agente de viagem: Vamos organizar sua viagem!\n")

	def organizarViagem(self,destino,modoViagem):
		print("Destino: {}\n".format(destino))

		self.meioTransporte = Empresa(destino = destino, modoViagem = modoViagem)
		self.meioTransporte.agendarViagem()

		self.hospedagem = Hotel()
		self.hospedagem.agendarQuarto()
		self.hospedagem.comida()

class Empresa(object):
	def __init__(self, destino ,modoViagem):
		print("Organizando viagem para: {} de: {}\n".format(destino,modoViagem))
		self.destino = destino
		self.modoViagem = modoViagem

	def agendarViagem(self):
		if self.modoViagem == 'carro':
			print("O cliente vai usar o próprio carro\n")
		elif self.modoViagem == 'avião':
			print("Agendando assentos para {} de AVIÃO!\n".format(self.destino))
		elif self.modoViagem == 'bus':
			print("Agendando assentos para {} de ÔNIBUS!\n".format(self.destino))

class Hotel(object):
	def __init__(self):
		print('Encontrando quarto pro cliente---\n')


	def quartoLivre(self):
		print('Checando disponibilidade de vagas\n')
		return True

	def agendarQuarto(self):
		if self.quartoLivre():
			print('Agendando quarto para cliente\n')

	def comida(self):
		print('Agendando refeições para clientes\n')

class cliente(object):
	def __init__(self, nome):
		print('{}: Yaay! Vou viajar!!'.format(nome))

	def falarComAgente(self):
		print('Hora de falar com o agente e organizar minha viagem\n')
		manager = AgenteViagem()
		manager.organizarViagem(destino='Sirinhaem',modoViagem='ônibus')

	def __del__(self):
		print('Eu: Obrigada, Sr. Agente!')

Me = cliente('Mariama')
Me.falarComAgente()
