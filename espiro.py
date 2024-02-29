import PySimpleGUI as sg
from table2ascii import table2ascii, Merge, PresetStyle

demo = {'DATA': '01/12/22', 'CVF': '3.96', 'CVFPREVISTO': '3.22', 'POSCVF': '3.93', 'FEV1': '3.04',
        'FEV1PREVISTO': '2.66', 'POSFEV1': '3.54', 'FEV1/CVF PREV': '76.8%', 'FEF2575': '2.7', 'POSFEF2575': '4.14', 0: False}
# #valores = {'CVF': '', 'CVFPREVISTO': '', 'POSCVF': '', 'FEV1': '', 'FEV1PREVISTO': '', 'POSFEV1': '', 'FEF2575': '', 'POSFEF2575': '', 0: False}
# valores = demo


def main():
    global valores
    # CVF FEV1 FEF 25-75% FEV 75

    # Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira apenas números')],
        [sg.Text('Data:'), sg.Input(key='DATA', size=10)],
        [sg.Text('PRÉ CVF'), sg.Input(key='CVF', size=5), sg.Text('Previsto >'), sg.Input(
            key='CVFPREVISTO', size=5), sg.Text('PÓS CVF'), sg.Input(key='POSCVF', size=5)],
        [sg.Text('PRÉ FEV1'), sg.Input(key='FEV1', size=5), sg.Text('Previsto >'), sg.Input(
            key='FEV1PREVISTO', size=5), sg.Text('PÓS FEV1'), sg.Input(key='POSFEV1', size=5)],
        [sg.Text('Valor previsto para FEV1/CVF'),
         sg.Input(key='FEV1/CVF PREV', size=5)],
        [sg.Text('PRÉ FEF 25-75%'), sg.Input(key='FEF2575', size=5),
         sg.Text('PÓS FEF 25-75%'), sg.Input(key='POSFEF2575', size=5)],
        #[sg.Checkbox('Laudar?')],
        [sg.Button('Salvar')],
        [sg.Text(key='-SAÍDA-')]
    ]

    # Janela
    window = sg.Window('LaudAí - Espirometrias', layout,
                       element_justification='c')

    # Eventos
    while True:
        eventos, valores = window.read()  # type: ignore
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Laudar?':
            pass
        if eventos == 'Salvar':
            print(valores)
            sg.easy_print(tabela())
            # print(tabela())


def tabela():
    VF1CVFpre = round(
        (float(valores['FEV1']) / float(valores['CVF'])) * 100, 2)
    FEF2575CVFpre = round(
        float(valores['FEF2575']) / float(valores['CVF']) * 100, 2)
    tabela = table2ascii(
        # header=['DATA:', valores['DATA'], 'ESPIROMETRIA', Merge.LEFT, Merge.LEFT, Merge.LEFT, Merge.LEFT],
        body=[['DATA:', valores['DATA'], 'ESPIROMETRIA', Merge.LEFT, Merge.LEFT, Merge.LEFT, Merge.LEFT],
              ["CVF:", "Pré:", valores['CVF'], 'Previsto: >',
              valores['CVFPREVISTO'], "Pós:", valores['POSCVF']],
              ["VEF1:", "Pré:", valores['FEV1'], 'Previsto: >',
              valores['FEV1PREVISTO'], "Pós:", valores['POSFEV1']],
              ['VF1/CVF:', 'Pré:', VF1CVFpre, 'Previsto: >',
              valores['FEV1/CVF PREV'], Merge.LEFT, Merge.LEFT],
              ['FEF 25-75%:', 'Pré:', valores['FEF2575'], 'Pós:',
              valores['POSFEF2575'], Merge.LEFT, Merge.LEFT],
              ['FEF 25-75%/CVF:', 'Pré:', FEF2575CVFpre, Merge.LEFT, Merge.LEFT, Merge.LEFT, Merge.LEFT]],
        # footer=["SUM", "130", "140", "135", "130"],
        # alignments=Alignment.LEFT
        # number_alignments= Alignment.CENTER
        style=PresetStyle.minimalist
    )
    return tabela


if __name__ == '__main__':
    main()
    # print(tabela())
