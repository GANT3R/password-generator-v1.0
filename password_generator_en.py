import PySimpleGUI as sg
import random as r
import os
import pyperclip


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_small = letters.lower()
numbers = '0123456789'
symbols = '!@$%-*&'
password_mix = ''


components_left = [
    [sg.Text('Password length')],
    [sg.Slider(range=(4, 30), default_value=12, orientation='h', key='-PASS_LEN-')],
    [sg.Checkbox('Numbers', key='-NUMB_BOX-', default=True)],
    [sg.Checkbox('Big letters', key='-BIG_L_BOX-')],
    [sg.Checkbox('Small letters', key='-SMALL_L_BOX-', default=True)],
    [sg.Checkbox('Specsymbols', key='-SYM_BOX-')],
]

components_right = [
    [sg.InputText('', size=(35,1), key='-OUTPUT1-'), sg.Button('Copy', size=(8,1), key='-COPY_PASS_1-')],
    [sg.InputText('', size=(35,1), key='-OUTPUT2-'), sg.Button('Copy', size=(8,1), key='-COPY_PASS_2-')],
    [sg.InputText('', size=(35,1), key='-OUTPUT3-'), sg.Button('Copy', size=(8,1), key='-COPY_PASS_3-')],
    [sg.InputText('', size=(35,1), key='-OUTPUT4-'), sg.Button('Copy', size=(8,1), key='-COPY_PASS_4-')],
    [sg.Checkbox('Autocopy first password', default=True, key='-AUTOCOPY_BOX-'), sg.Button('Generate', focus=True, size=(13,1), key='-GEN-'),
     sg.Button('Mix', size=(9,1),key= '-MIX-')]
]

components_templ = [
    [sg.Button('Template #1', k='-TEMP_1-'),sg.Button('', k='-!_TMP_1-'),sg.Button('Template #2', k='-TEMP_2-'),sg.Button('', k='-!_TMP_2-'),sg.Button('Template #3',k='-TEMP_3-'),sg.Button('', k='-!_TMP_3-')],
]


layout = [
    [
        sg.Column(components_left), sg.VSeparator(), sg.Column(components_right),
    ],
    [sg.HSeparator()],
    [sg.Column(components_templ)],
]

def numb_add():
    global password
    password += numbers
def s_let_add():
    global password
    password += letters_small
def b_let_add():
    global password
    password += letters
def sym_add():
    global password
    password += symbols
def gen():
    global length, i, password_out
    for i in range(length):
        password_out += r.choice(password)
def mix_all():
    global password_mix
    password_mix += values['-OUTPUT1-'] + '\n'
    password_mix += values['-OUTPUT2-'] + '\n'
    password_mix += values['-OUTPUT3-'] + '\n'
    password_mix += values['-OUTPUT4-']
    pyperclip.copy(password_mix)
    sg.popup('Protocol \"All in one\"')
    password_mix = ''
def temp_1():
    global password, length
    length = 12
    password = ''
    numb_add()
    s_let_add()
def temp_2():
    global password, length
    length = 12
    password = ''
    numb_add()
    s_let_add()
    b_let_add()
    sym_add()
def temp_3():
    global password, length
    length = 20
    password = ''
    numb_add()
    s_let_add()
    b_let_add()
    sym_add()

window = sg.FlexForm('Password generator', grab_anywhere=False)
window.Layout(layout)

while True:
    event, values = window.read()
    if event == '-GEN-':        #values["NUMB_BOX"] == True:
        password = ''
        password_out = ''
        length = int(values['-PASS_LEN-'])
        if values['-NUMB_BOX-'] == True:
            numb_add()
        if values['-BIG_L_BOX-'] == True:
            b_let_add()
        if values['-SMALL_L_BOX-'] == True:
            s_let_add()
        if values['-SYM_BOX-'] == True:
            sym_add()
        if password != '':
            gen()
        else:
            sg.popup('Choose min one element for password')
            continue
        window['-OUTPUT1-'].update(password_out)
        if values['-AUTOCOPY_BOX-'] == True:
            pyperclip.copy(password_out)
        password_out = ''
        gen()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    if event == '-TEMP_1-':
        temp_1()
        password_out = ''
        gen()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    if event == '-TEMP_2-':
        temp_2()
        password_out = ''
        gen()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    if event == '-TEMP_3-':
        temp_3()
        password_out = ''
        gen()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    if event == '-!_TMP_1-':
        tmp_1_info = 'Length - 12' + '\n'
        tmp_1_info += 'Numbers' + '\n'
        tmp_1_info += 'Small letters' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    if event == '-!_TMP_2-':
        tmp_1_info = 'Length - 12' + '\n'
        tmp_1_info += 'Numbers' + '\n'
        tmp_1_info += 'Small letters' + '\n'
        tmp_1_info += 'Big letters' + '\n'
        tmp_1_info += 'Symbols' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    if event == '-!_TMP_3-':
        tmp_1_info = 'Length - 20' + '\n'
        tmp_1_info += 'Numbers' + '\n'
        tmp_1_info += 'Small letters' + '\n'
        tmp_1_info += 'Big letters' + '\n'
        tmp_1_info += 'Symbols' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    if event == '-COPY_PASS_1-':
        password = values['-OUTPUT1-']
        pyperclip.copy(password)
        password = ''
    if event == '-COPY_PASS_2-':
        password = values['-OUTPUT2-']
        pyperclip.copy(password)
        password = ''
    if event == '-COPY_PASS_3-':
        password = values['-OUTPUT3-']
        pyperclip.copy(password)
        password = ''
    if event == '-COPY_PASS_4-':
        password = values['-OUTPUT4-']
        pyperclip.copy(password)
        password = ''
    if event == '-MIX-':
        if values['-OUTPUT1-'] != '' and values['-OUTPUT2-'] != '' and values['-OUTPUT3-'] != '' and values['-OUTPUT4-'] != '':
            mix_all()
        else:
            sg.popup('Unable to generate empty password')
    if event == sg.WINDOW_CLOSED:
        break