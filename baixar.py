import time


def baixar(web):

    bd_secundario = web.find_elements(
        tag='div', classname='pd-float')   # Carregar divs

    # Contador de PDFS
    contador_aux = len(bd_secundario)

    for y in range(contador_aux):
        texto_aux = bd_secundario[y].text
        print('Texto: {}\n'.format(texto_aux))
        if texto_aux.find('tab_veiculo') != -1 or texto_aux.find('tabela_veiculo') != -1 or texto_aux.find('tabela_de_veiculo') != -1:
            web.click('Download', tag='a', number=y+1)
            time.sleep(2)
    # return situacao
