from abc import ABCMeta, abstractmethod

class Transicao(metaclass = ABCMeta):
	@abstractmethod
	def execute(self):
		pass

class SELECIONAR(Transicao):
	def __init__(self, Transicao):
		self.trans = Transicao

	def execute(self):
		self.trans.SELECIONAR()

class INSERIR(Transicao):
	def __init__(self, Transicao):
		self.trans = Transicao

	def execute(self):
		self.trans.INSERIR()

class UPDATE(Transicao):
	def __init__(self, Transicao):
		self.trans = Transicao

	def execute(self):
		self.trans.UPDATE()

class TransicaoManager:
	def SELECIONAR(self):
		print('Realizando operação SELECIONAR!')

	def INSERIR(self):
		print('Realizando operação INSERIR!')

	def UPDATE(self):
		print('Realizando operação UPDATE!')


class TransicaoBroker:
	def __init__(self):
		self.__TransicaoQeueue = []

	def requestTransicao(self, Transicao):
		self.__TransicaoQeueue.append(Transicao)
		Transicao.execute()

if __name__ == '__main__':
	transiction = TransicaoManager()
	tr_SELECIONAR = SELECIONAR(transiction)
	tr_INSERIR = INSERIR(transiction)
	tr_update = UPDATE(transiction)

	brkr = TransicaoBroker()
	brkr.requestTransicao(tr_SELECIONAR)
	brkr.requestTransicao(tr_INSERIR)
	brkr.requestTransicao(tr_INSERIR)
	brkr.requestTransicao(tr_SELECIONAR)
	brkr.requestTransicao(tr_update)
	brkr.requestTransicao(tr_INSERIR)
	brkr.requestTransicao(tr_update)