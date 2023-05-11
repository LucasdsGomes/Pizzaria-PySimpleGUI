from PySimpleGUI import PySimpleGUI as sg

def janela_login():
    sg.theme('LightBrown9')
    layout=[
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('LightBrown9')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox(
            'Pizza de Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'),sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)

janela1, janela2 = janela_login(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza de Frango c/ Catupiry')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza Pepperoni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza de Frango c/ Catupiry')
