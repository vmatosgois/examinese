from table2ascii import table2ascii, PresetStyle, Merge, Alignment
import datefinder #Atentar para datas incompletas, não contempladas por essa biblioteca
from datetime import datetime
from fuzzywuzzy import process # python-Levenshtein / rapidfuzz?
import toolboxy as tb

# Variaveis pré-declaradas

lista_de_datas = []
lista_remover = list()
master = dict()

espelho = { 'Hm': ['Hm'],
            'Hb': ['Hb'],
            'Ht': ['Ht'],
            'VCM': ['VCM', 'VGM'],
            'HCM': ['HCM', 'HGM'],
            'CHCM': ['CHCM'],
            'RDW': ['RDW'],
            'Reticulócitos': ['Reticulócitos', 'Reti'],
            'Leucócitos': ['Leucócitos', 'Leuco'],
            'Blastos': ['Blastos'],
            'Promielócitos': ['Promielócitos'],
            'Mielócitos': ['Mielócitos'],
            'Metamielócitos': ['Metamielócitos'],
            'Bastões': ['Bastões', 'Bast'],
            'Segmentados': ['Segmentados', 'Neut Segmentados', 'Neut', 'Neutrófilos'],
            'Eosinófilos': ['Eosinófilos', 'Eos', 'Eosi'], 
            'Linfócitos': ['Linfócitos', 'Linf', 'Linfo'],
            'Monócitos': ['Monócitos', 'Mono', 'Mon'],
            'Basófilos': ['Basófilos', 'Baso', 'Bas'],
            'Linf._Atípicos': ['Atípicos'],
            'Plaquetas': ['Plaquetas', 'Plaq', 'Pqt'],
            'LDH': ['LDH', 'DHL'],
            'VHS': ['VHS', 'Hemossedimentação', 'Hemosse'],
            'PCR': ['PCR'],
            'Colest._Total': ['CT', 'Colesterol Total', 'ColesT', 'Col total'],
            'HDL': ['Hdl'],
            'LDL': ['Ldl'], 
            'Triglicérides': ['TGL', 'Triglicérides', 'Trigli'],
            'CPK': ['CPK'],
            'CPK-MB': ['CPKMB', 'CKMB'],
            'Troponina': ['Troponina', 'Tropo'],
            'BNF': ['BNF'],
            'Ferro': ['Ferro', 'Fe'],
            'Ferritina': ['Ferritina'],
            'Sat._Transf.': ['Transferrina', 'Transfer'],
            'TIBIC': ['TIBIC'],
            'B12': ['B12'],
            'Ác._Fólico': ['Fólico', 'Ácido Fólico'],
            'Creatinina': ['Creatinina', 'Creat', 'Cr'],
            'Uréia': ['Ureia'],
            'Clearance': ['CKDEPI', 'Glomerular', 'Clearance'],
            'Ácido_Úrico': ['Ácido Úrico', 'Úrico'],
            'Sódio': ['Na', 'Sódio'],
            'Potássio': ['K', 'Potássio'],
            'Fósforo': ['P', 'Fósforo'],
            'Cálcio_Sérico': ['Cálcio Sérico', 'Ca Sérico', 'Cálcio', 'Ca'],
            'Cálcio_Ionizável': ['Cálcio Ionizável', 'Ca Ionizável'],
            'Magnésio': ['Mg', 'Magnésio'],
            'Cloro': ['Cl', 'Cloro'],
            'Proteínas': ['Proteínas', 'Ptn', 'Prot'],
            'Albumina': ['Albumina', 'Alb', 'Albu'],
            'Globulina': ['Globulina', 'Glob', 'Globu'],
            'Relação_A/G': ['a/g'],
            'Bili_Total': ['Bt', 'Bilirrubina Total'],
            'Bili_Direta': ['Bd', 'Bilirrubina Direta'],
            'Bili_Indireta': ['Bi', 'Bilirrubina Indireta'],
            'TGO_(AST)': ['TGO', 'AST'],
            'TGP_(ALT)': ['TGP', 'ALT'],
            'Fosfatase_Alc.': ['FA', 'Fosfatase Alcalina'],
            'Gama-GT': ['GGT', 'GamaGT'],
            'Amilase': ['Amilase'],
            'Lipase': ['Lipase'],
            'INR': ['INR', 'RNI'],
            'TTPA': ['TTPA'],
            'Ratio': ['Ratio'],
            'TAP': ['TAP'],
            'TS': ['TS', 'Sangramento'],
            'TC': ['TC', 'Coagulação'],
            'Glicemia_Jejum': ['GJ', 'Glicemia', 'Jejum', 'Glicemia de Jejum', 'Glicose'],
            'Glicemia_Pós-P': ['GPP', 'Prandial'],
            'Glicada': ['Hemoglobina Glicada', 'HBA1C', 'Glicada'], 
            'TSH': ['TSH'],
            'T4_Livre': ['T4 Livre', 'T4L'],
            'Vitamina_D': ['VitD', '25OHD', 'Vitamina D', 'VitD-Direta']
            }

merger = {'Sérico': ['Sérico', 'Serico', 'Seri'],
          'Ionizável': ['Ionizável', 'Ion', 'Ionizavel'],
          'CT': ['CT'],
          'Total': ['Total'],
          'Livre:': ['Livre'],
          'Ureia': ['Ureia', 'Ur'],
          'Úrico': ['Urico', 'Uric'],
          'Ultra': ['Ultra'],
          'Urinário': ['Urinário', 'Urinária'],
          'Direta': ['Direta', 'Dir', 'Dir'],
          'Indireta': ['Indireta', 'Indi'],
          'VitD': ['VitD']
          }


def boot():
    
    raw = '''(29/03/2022: HB 14,0 HT 43,3 LEUCO 9495 NEUT 40% (3798) LINFO 53% (5032) PLAQ 321800 | ACIDO URICO 3,8 | CALCIO SRICO 9,6 | HDL 81 | LDL 58 | CT 163 | CREAT 0,8 | CPK 73 | P 5,3 | GJ 109 | HBA1C 6,0% EDTA | MG 2,4 | K 4,1 | NA 140 | TGL 119 | UREIA 43 | 
28/12/2021): HB 15.2 HT 45 LEUCO 5300 PLAQ 298000 GJ 118 CREAT 0,98 AC URIC 3.2 HDL 53 LDL 86 CT 165 GJ 112 TG 130 U 29 TGO 30 CA 9.2 TGP 16 HB1AC 5.7% VITD 33 TSH 2,66 T4L 0,88 EAS NDN 
(17/01/2023): hb 15.3 ht 46 leuco 7200 plq 236300 tgp 16 tgo 20 hdl 59 ldl 48 ct 130 cr 0.9 cpk 101 gj 97 pos prandial 113 hba1c 5.8 mg 2.3 ca s 10.1 k 4.3 pt 6.8 alb 4.5 glob 2.3 a/g 2.0 na 139 tgl 114 ur 25 t4 livre 0.98 tsh 2.2 **vit d 27 EAS sem alterações
(01/02/23): Hb 13,1 Ht 39 Leuco 7400 Plaquetas 338000 Creat 1,2 (CKEDIP) Sódio 144 Glicose 89 Potássio 4,1 col tot 182 Ldl 60 IGF-1 354 BNF 12345 Troponina Ultra 12345 CPKMB 12345
'''
        
    return raw

def preset(raw, merger = merger):
    """Essa função faz a primeira passagem de reconhecimento do texto em exames de mais de duas palavras,
    remove caracteres especiais e retorna um texto reformulado.

    Args:
        raw (str): Texto original
        merger (dict, optional): Espelho utilizado como guia para o reconhecimento de palavras. Padrão: merger.

    Returns:
        str: Varíavel contendo texto reformulado 
    """
    global lista_de_datas
    
    tokens = raw.split()
    merged = []
    bugfix = []
    
    # BUG FIX - DO NOT REMOVE:
    datas = datefinder.find_dates(raw, source=True, strict=True)
    for d in datas:
        lista_de_datas.append(d[1])
    
    
    # Limpa caracteres especiais e espaços vazios, deixa tudo capitalizado
    tokens = [elemento.capitalize() for elemento in tokens]
    for _, string in enumerate(tokens):
        tokens[_] = string.strip(':()-,.*#|/%')
    
    # Remove entradas vazias
    for _ in range(tokens.count('')):
        tokens.remove('') 
         
    # Identifica exames comumente com mais de uma palavra e junta com separador _ para posterior reavaliação, ignora os demais
    for token in tokens:
        if token.replace('.', '').replace(',', '').isnumeric(): #Função de otimização
            merged.append(token)
            continue
        correspondencias = {chave: max(process.extract(token, valores, limit=1), key=lambda x:x[1]) for chave, valores in merger.items()}
        melhor_correspondecia = max(correspondencias.items(), key=lambda x: x[1][1])
        if melhor_correspondecia[1][1] > 80:
            merged.append(melhor_correspondecia[0])
            if merged[len(merged)-2].replace('.', '').replace(',', '').isnumeric() or merged[len(merged)-2] in lista_de_datas:
                continue
            merged[len(merged)-2] = '-'.join(merged[len(merged)-2:])
            merged.pop()
        else:
            merged.append(token)
    return ' '.join(merged)

def corretor(string, espelho=espelho):
    """Realiza o reconhecimento dos exames com base em um banco de dados cadastrado.

    Args:
        string (str): Texto reformulado pela função preset.
        espelho (dict, optional): Espelho utilizado para reconhecimento de palavras. Padrão: espelho.

    Returns:
        str: Texto reformulado com exames completos.
    """
    
    # Identifica os exames listados no espelho e corrige para a ortografia completa
    tokens = string.split()
    corrigido = []
    for token in tokens:
        if token.replace('.', '').replace(',', '').isnumeric(): #Função de otimização
            corrigido.append(token)
            continue
        correspondencias = {chave: max(process.extract(token, valores, limit=1), key=lambda x:x[1]) for chave, valores in espelho.items()}
        melhor_correspondencia = max(correspondencias.items(), key=lambda x: x[1][1])
        if melhor_correspondencia[1][1] > 80:
            corrigido.append(melhor_correspondencia[0])
        else:
            corrigido.append(token)
    return ' '.join(corrigido)


def is_word(str):
    """Verifica se a string fornecida é uma palavra. Definição: Contém pelo menos uma letra.

    Args:
        str (str): Palavra

    Returns:
        bool: Retorna True se a string contiver ao menos uma letra.
    """
    
    for character in str:
        if character.isalpha():
            return True

def processar_datas(texto):
    """Cria uma lista de datas extraída do texto original e lista termos a serem removidos do arquivo original.

    Args:
        texto (str): Texto fonte.

    Returns:
        list: Lista contendo outras listas com os exames e seus respectivos valores.
    """
    
    global lista_de_datas, lista_remover
    
    # Cria uma lista de datas - Suspenso devido a bug com função de datas
    
    # datas = datefinder.find_dates(texto, source=True, strict=True, first='day')
    # for d in datas:
    #     lista_de_datas.append(d[1])

    texto = texto.split()

    # Listar palavras a serem removidas
    was_alpha = False
    for index, linha in enumerate(texto):
        if is_word(linha) and was_alpha == False:
            was_alpha = True
        elif linha in lista_de_datas and was_alpha == True:
            lista_remover.append(index - 1)
            was_alpha = False
        elif is_word(linha) and was_alpha == True:
            lista_remover.append(index - 1)
        elif was_alpha == True and index+1<len(texto) and linha.isnumeric() and texto[index+1].isnumeric() and not texto[index+2].isnumeric():
            texto[index] = (texto[index], texto[index+1])
            lista_remover.append(index+1)
            was_alpha == False
        else:
            was_alpha = False

    texto_exames = texto 
    return texto_exames   


def spliter(texto_exames):
    """Separa exames em um dicionário por data.

    Args:
        texto_exames (list): Lista de exames e valores.

    Returns:
        list: Variável topo, contendo cabeçalho de datas.
        dict: Dicionário contendo datas ordenadas em ordem crescente com seus respectivos exames e valores.
    """
    
    global lista_remover
    
    master = {}
    
    #Tá confuso, mas funciona
    index = list()
    for d in lista_de_datas:
        index.append(texto_exames.index(d))
    
    #Lembrar de otimizar depois (Ele passa pelo mesmo número duas vezes)
    for i, line in enumerate(texto_exames):
        if line in lista_de_datas:
            master[line] = list()
            i = i+1
            while i not in index:
                if i not in lista_remover:
                    master[line].append(texto_exames[i])
                if i + 1 < len(texto_exames):
                    i = i+1
                else:
                    break
                
    # Converter as chaves do dicionário para o formato de data
    datas_formatadas = {datetime.strptime(data, '%d/%m/%y' if len(data) == 8 else '%d/%m/%Y'): valor for data, valor in master.items()}
    
    # Ordenar o dicionário por data
    master = {data.strftime('%d/%m/%Y'): valor for data, valor in sorted(datas_formatadas.items())}
    
    # Cabeçalho de datas
    topo = ['Data:']
    for data in master.keys():
        topo.append(data)
    
    return topo, master


def tinder(master):
    """Organiza os pares/grupos de exames de mesmo nome em uma lista única contendo seus respectivos valores
    entre todas as datas disponíveis. Insere '-' quando ausente. Converte números em float ou int.

    Args:
        master (dict): Dicionário contendo datas e respectivos exames

    Returns:
        dict: Dicionário completo contendo nomes de exames e todos os valores organizados.
    """

    exams = {}

    # Preenche o dicionário de exames com a chave sendo o nome do exame e o conteúdo uma lista com os valores já convertidos em float ou int
    for key in master.keys():
        for i in range(0, len(master[key]), 2):
            exam_name = master[key][i]
            exam_value = master[key][i+1] if i+1 < len(master[key]) else '-'
            if exam_name not in exams:
                exams[exam_name] = ['-'] * len(master)
            exams[exam_name][list(master.keys()).index(key)] = int(float(exam_value.replace(',', '.'))) if type(exam_value) == str and float(exam_value.replace(',', '.')) == int(float(exam_value.replace(',', '.'))) else float(exam_value.replace(',', '.')) if type(exam_value) == str else exam_value 

    return exams

def sort(exams):
    """Reordena dicionário com base em lista pré-definida. Exames não reconhecidos são inseridos no fim da lista.

    Args:
        exams (dict): Dicionário de exames e valores processados.

    Returns:
        dict: Dicionário ordenado
    """

    # Ordena segundo lista espelho
    sorted = {chave: exams[chave] for chave in espelho.keys() if chave in exams}
    
    # Insere no fim da lista exames que não foram identificados previamente
    resto = {chave: exams[chave] for chave in exams if chave not in sorted}
    
    sorted.update(resto)
    
    return sorted


def doc(sorted):
    """Reorganiza o dicionário e converte em lista no formato para o corpo da tabela

    Args:
        sorted (dict): Exames e valores

    Returns:
        list: Corpo da tabela
    """
    
    # Converte o dicionário de exames em uma lista de listas
    corpo = [[name] + values for name, values in sorted.items()]
    
    return corpo



def gerartabela(corpo, topo):
    """Gera a tabela final em ASCII.

    Args:
        corpo (list): Corpo da tabela contendo valores e exames.
        topo (list): Cabeçalho de datas
    """
    
    tabela = table2ascii(
        header=topo,
        body=corpo,
        # footer=["SUM", "130", "140", "135", "130"],
        alignments=Alignment.LEFT,
        number_alignments= Alignment.CENTER,
        style=PresetStyle.minimalist #thin_thick  # minimalist
    )
    
    output = tabela.replace('─','—').replace('━','=').replace(' - ', '   ')
    return output

def main(entry):
    """Função principal, executa programa.

    Args:
        entry (str): Entrada de texto inicial

    Returns:
        str: Tabela gerada pelo programa
    """
    
    if entry == 'demo':
        raw = boot()
    else:
        raw = entry
    merged = preset(raw)
    texto = corretor(merged)
    texto_exames = processar_datas(texto)
    topo, master = spliter(texto_exames)
    exams = tinder(master)
    sorted = sort(exams)
    corpo = doc(sorted)
    final = gerartabela(corpo, topo)
    
    # Limpeza de variáveis:
    
    lista_de_datas.clear()
    lista_remover.clear()
    master = {}
    
    return final
    
    
if __name__ == '__main__':
    print(main('demo'))
    ...