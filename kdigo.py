import math

unidade = 'mL/min/1.73m^2'

def ckdepi(Creatinina, Idade, Sexo):
    
    Creatinina = float(Creatinina.replace(',', '.'))
    Idade = int(Idade)
    
    if Sexo.upper() == 'H':
        kappa = 0.9
        alfa = -0.302
        mult_sexo = 1.0

    if Sexo.upper() == 'M':
        kappa = 0.7
        alfa = -0.241
        mult_sexo = 1.012

    TFG = round(142 * math.pow(min(Creatinina/kappa, 1), alfa) * math.pow(max(
        Creatinina/kappa, 1), -1.200) * math.pow(0.9938, Idade) * mult_sexo, 1)

    return TFG


def scoreKdigo(TFG):
    score = ''
    if TFG < 15:
        score = 'G5 (Falência Renal)'
    elif TFG < 30:
        score = 'G4 (Muito Reduzida)'
    elif TFG < 45:
        score = 'G3b (Moderadamente Reduzida)'
    elif TFG < 60:
        score = 'G3a (Leve a Moderadamente Reduzida)'
    elif TFG < 90:
        score = 'G2 (Levemente Reduzida)'
    else:
        score = 'G1 (Normal)'
        
    return score