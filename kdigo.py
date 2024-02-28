import math

def ckdepi(Creatinina, Idade, Sexo='H'):
    kappa = 0.9
    alfa = -0.302
    mult_sexo = 1.0

    if Sexo.upper() == 'M':
        kappa = 0.7
        alfa = -0.241
        mult_sexo = 1.012

    TFG = 142 * math.pow(min(Creatinina/kappa, 1), alfa) * math.pow(max(
        Creatinina/kappa, 1), -1.200) * math.pow(0.9938, Idade) * mult_sexo

    return TFG


def scoreKdigo(Creatinina, Idade, Sexo='H'):
    TFG = ckdepi(Creatinina, Idade, Sexo)
    unidade = 'mL/min/1.73m^2'
    if TFG < 15:
        print('Estágio G5 (Falência Renal), com TFG de', round(TFG, 2), unidade)
    elif TFG < 30:
        print('Estágio G4 (Muito Reduzida), com TFG de', round(TFG, 2), unidade)
    elif TFG < 45:
        print('Estágio G3b (Moderadamente Reduzida), com TFG de',
              round(TFG, 2), unidade)
    elif TFG < 60:
        print('Estágio G3a (Leve a Moderadamente Reduzida), com TFG de',
              round(TFG, 2), unidade)
    elif TFG < 90:
        print('Estágio G2 (Levemente Reduzida), com TFG de',
              round(TFG, 2), unidade)
    else:
        print('Estágio G1 (Normal), com TFG de', round(TFG, 2), unidade)