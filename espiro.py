from table2ascii import table2ascii, PresetStyle, Merge, Alignment

#demo = {'DATA': '01/12/22', 'CVF': '3.96', 'CVFPREVISTO': '3.22', 'POSCVF': '3.93', 'FEV1': '3.04','FEV1PREVISTO': '2.66', 'POSFEV1': '3.54', 'FEV1/CVF PREV': '76.8%', 'FEF2575': '2.7', 'POSFEF2575': '4.14', 0: False}

demo = {'DATA': '',
           'PRE_CVF': '3.96',
           'CVF_PREVISTO': '3.22',
           'POS_CVF': '3.93',
           'PRE_FEV1': '3.04',
           'FEV1_PREVISTO': '',
           'POS_FEV1': '',
           'FEV1/CVF': '',
           'FEV1/CVF_PREVISTO': '76,8',
           'PRE_FEF2575': '',
           'FEF2575_PREVISTO': '',
           'POS_FEF2575': '',
           'FEF2575/CVF': ''
           }

valores = {'DATA': '',
           'PRE_CVF': '',
           'CVF_PREVISTO': '',
           'POS_CVF': '',
           'PRE_FEV1': '',
           'FEV1_PREVISTO': '',
           'POS_FEV1': '',
           'FEV1/CVF': '',
           'FEV1/CVF_PREVISTO': '',
           'PRE_FEF2575': '',
           'FEF2575_PREVISTO': '',
           'POS_FEF2575': '',
           'FEF2575/CVF': ''
           }
# valores = demo

# ---------------------------------- CODIGO FEITO ÀS PRESSAS, SUJEITO A ALTERAÇÕES ---------------------------------


def process_values(valores):
    """Testa os valores disponíveis um a um e tenta calcular valores relativos quando possível

    Args:
        valores (dict): Dicionário contendo entradas

    Returns:
        dict: dicionário modificado com valores relativos
    """
    
    comma = {key: valores[key].replace(',', '.') for key in valores.keys()}

    try:
        comma['FEV1/CVF'] = f"{round((float(comma['PRE_FEV1']) / float(comma['PRE_CVF'])) * 100, 1)}%"
    except:
        ...
        
    try:  
        comma['FEF2575/CVF'] = f"{round(float(comma['PRE_FEF2575']) / float(comma['PRE_CVF']) * 100, 1)}%"
    except:
        ...
        
    try:
        comma['PRE_CVF'] = f"{comma['PRE_CVF']} ({round(float(comma['PRE_CVF']) / float(comma['CVF_PREVISTO']) * 100, 1)}%)"
    except:
        ...
        
    try:
        comma['PRE_FEV1'] = f"{comma['PRE_FEV1']} ({round(float(comma['PRE_FEV1']) / float(comma['FEV1_PREVISTO']) * 100, 1)}%)"
    except:
        ...
    
    try:
        comma['PRE_FEF2575'] = f"{comma['PRE_FEF2575']} ({round(float(comma['PRE_FEF2575']) / float(comma['FEF2575_PREVISTO']) * 100, 1)}%)"
    except:
        ...
        
    try:
        comma['POS_CVF'] = f"{comma['POS_CVF']} ({round(float(comma['POS_CVF']) / float(comma['CVF_PREVISTO']) * 100, 1)}%)"
    except:
        ...
        
    try:
        comma['POS_FEV1'] = f"{comma['POS_FEV1']} ({round(float(comma['POS_FEV1']) / float(comma['FEV1_PREVISTO']) * 100, 1)}%)"
    except:
        ...
    
    try:
        comma['POS_FEF2575'] = f"{comma['POS_FEF2575']} ({round(float(comma['POS_FEF2575']) / float(comma['FEF2575_PREVISTO']) * 100, 1)}%)"
    except:
        ...
        
    fill_empty = {key: 'NI' for key in comma.keys() if comma[key] == ''}
    resto = {chave: comma[chave] for chave in comma.keys() if chave not in fill_empty}
    
    fill_empty.update(resto)

    return fill_empty
    

def refine (valores):
    """Reorganiza dados brutos antes de enviar para geração de tabela

    Args:
        valores (dict): Dicionário contendo exames pré-processados

    Returns:
        list: Listas contendo cabeçalho e corpo da tabela
    """
    
    topo = ['DATA:', valores['DATA'], 'ESPIROMETRIA', Merge.LEFT, Merge.LEFT, Merge.LEFT, Merge.LEFT]
    
    corpo=[   ["CVF:", "Pré:", valores['PRE_CVF'], 'Prev.:', valores['CVF_PREVISTO'], "Pós:", valores['POS_CVF']],
              ["FEV1:", "Pré:", valores['PRE_FEV1'], 'Prev.:', valores['FEV1_PREVISTO'], "Pós:", valores['POS_FEV1']],
              ['FEV1/CVF:', valores['FEV1/CVF'], 'Prev.:', valores['FEV1/CVF_PREVISTO']]+ [Merge.LEFT]*(len(topo)-4),
              ['FEF 25-75%:', 'Pré:', valores['PRE_FEF2575'], 'Prev.:', valores['FEF2575_PREVISTO'], 'Pós:', valores['POS_FEF2575']],
              ['FEF 25-75%/CVF:', valores['FEF2575/CVF']]+ [Merge.LEFT]*(len(topo)-2)]

    per_line = [[valores['PRE_CVF'], valores['CVF_PREVISTO'], valores['POS_CVF']],
                [valores['PRE_FEV1'], valores['FEV1_PREVISTO'], valores['POS_FEV1']],
                [valores['FEV1/CVF'], valores['FEV1/CVF_PREVISTO']],
                [valores['PRE_FEF2575'], valores['FEF2575_PREVISTO'], valores['POS_FEF2575']],
                [valores['FEF2575/CVF']]]
    
    index = []
    
    for l, line in enumerate(per_line):
        for v, variable in enumerate(line):
            if variable != 'NI':
                break
            if v == len(line)-1 and variable == 'NI':
                index.append(l)
                
    index.reverse()
    
    for r in index:
        corpo.pop(r)
    
    return corpo, topo
    
def tabela(corpo, topo):
    """Gera tabela

    Args:
        corpo (list): Corpo da tabela
        topo (list): Cabeçalho da tabela

    Returns:
        str: Tabela
    """
    tabela = table2ascii(
        header=topo,
        body=corpo,
        footer=['© Victor Matos, 2024'] + [Merge.LEFT]*(len(topo)-1),
        style=PresetStyle.minimalist
    ).replace('─','=').replace('━','=')
    return tabela

def main(valores):
    """Inicia a subrotina a partir de uma amostra de dados

    Args:
        valores (dict): Entrada de exames do usuário

    Returns:
        str: Tabela
    """
    
    processed = process_values(valores)
    refined_corpo, refined_topo = refine(processed)
    output = tabela(refined_corpo, refined_topo)
    
    return output

if __name__ == '__main__':
   print(main(valores))
