from webbot import Browser
from baixar import baixar
import time

# Ativo o navegador e entro no site do detran
web = Browser()
web.go_to('https://acesso.detran.mg.gov.br/veiculos/leiloes/editais')

configuracao = input("Configurou? S/n: ")

i = 0
parar = False  # Variavel de Parada do while
texto_array = []

print("\n---------- Sistema de Downloads de Tabela de veiculos -------------\n")
print("Processando quantidade de leiloes.....")

bd_principal = web.find_elements(
    tag='div', classname='pd-subcategory')   # Carregar divs

print("..... Procesamento Finalizado com Sucesso\n")

contador = len(bd_principal)
print('O numero de leiloes: {}\n'.format(contador))

contador_aux = contador - 1

for y in range(contador_aux):
    texto = bd_principal[y].text

    # INICIO - Tirada do texto de small
    x = texto.split()
    x.pop()
    texto = ' '.join(x)
    # FIM - Tirada do texto de small

    texto_array.append(texto)

print('----------------------- Iniciando Sistema ---------------------------\n')

while(parar == False):

    web.click(texto_array[i], tag='a')

    baixar(web)

    web.click('Editais de Leilões', tag='a')

    ################## Condição de parada ############################
    if texto_array[i].find('/2014') == -1:

        i += 1
        print(i)

    else:

        # Fechar Guia
        # web.close_current_tab()
        parar = True  # Parar while
