def letraA(data):
	lista_data = data.split('/')
	dici_data = {"ANO":lista_data[0], "MES":lista_data[1], "DIA":lista_data[2]}
	return dici_data

def letraB(ATIVO):

	ati = True
	if(ATIVO == strSIM):
		ati = True

	elif(ATIVO == strNAO):
	
		ati = False
	return ati

def letraC(Varia):

	listaS = Varia.split(‘:’)
	listaS = lista[:-1]	#pra tirar o \n
	return listaS

def letraD(arq):

	arq.seek(0,0)
	lis = arq.readlines 
	lis = arq.split(‘\n’)

	return lis

def main():

	arq = open(‘cadastro.txt’, r)
	lista_dic = []
	data = input(‘Insira a data’)
	result1 = letraA(data)
	print(result1)

	ATIVO = input(‘Insira se é SIM ou NÂO’)
	result2 = letraB(ATIVO)
	print(result2)

	Varia = input(‘Insira uma string no formato pedido’)
	result3 = letraC(Varia)
	print(result3)

	result4 = letraD(arq)
	print(result4)
	arq.seek(0,0)
	linha = arq.readlines
	lista = arq.split(‘:’)
	for linha in lista:
		cadastro = {‘CPF’:lista[0], ‘NOME’:lista[1], ‘DATA_DE_NASCIMENTO’:lista[3], /
				‘DATA_DE_CADASTRO’:lista[3], ‘ATIVO’:lista[4] }
		lista_dic += [cadastro]

	print(lista_dic)

main()
