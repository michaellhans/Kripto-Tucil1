import PySimpleGUI as sg
import threading
from auto_key_vigenere import *
from default_full_vigenere import *
from extended_vigenere import *
from playfair import *
from affine import *
from hill import *
from util import *

def process_input(key, input_text, ciphere_type, cipher_format, encrypt_mode):
    print(ciphere_type)
    if (ciphere_type == 'Vigenere Ciphere'):
        if (encrypt_mode):
            output_text = vigenere_cipher(input_text, key)
        else: 
            output_text = decrypt_vigenere_cepher(input_text, key)

    elif (ciphere_type == 'Full Vigenere Ciphere'):
        if (encrypt_mode):
            output_text = vigenere_cipher(input_text, key, full_cipher_matrix)
        else: 
            output_text = decrypt_vigenere_cepher(input_text, key, full_cipher_matrix)

    elif (ciphere_type == 'Auto-key Vigenere Ciphere'):
        if (encrypt_mode):
            output_text = auto_key_vigenere_cipher(input_text, key)
        else: 
            output_text = decrypt_auto_key_vigenere_cepher(input_text, key)

    elif (ciphere_type == 'Extended Vigenere Ciphere'):
        if (encrypt_mode):
            output_text = extended_vigenere_cipher(input_text, key)
        else: 
            output_text = decrypt_extended_vigenere_cepher(input_text, key)

    # Hengky tambahin yak tengkyuu
    elif (ciphere_type == 'Playfair Ciphere'):
        None
    elif (ciphere_type == 'Affine Ciphere'):
        None
    elif (ciphere_type == 'Hill Ciphere'):
        None

    print("Input text\t:", input_text)
    print("Output text\t:", output_text)
    if (cipher_format == True):
        output_text = showPerFive(output_text)
    return output_text

def gui_execute():
    sg.theme('DarkAmber')   # Add a touch of color

    encryption_cipher = [
        'Vigenere Ciphere',
        'Full Vigenere Ciphere',
        'Auto-key Vigenere Ciphere',
        'Extended Vigenere Ciphere',
        'Playfair Ciphere',
        'Affine Ciphere',
        'Hill Ciphere'
    ]
    
    encrypt_mode = True

    # All the stuff inside your window.
    col1 = [[sg.Text('Key')],[sg.Multiline(size=(65,2), key='key')]]
    col2 = [[sg.Text('Ciphere Type')],[sg.Combo(encryption_cipher, default_value='Vigenere Ciphere',key='ciphere_type')]]
    col3 = [[sg.Text('Ciphere Text Format')],
        [sg.Radio('No Space', "CIPHER_FORMAT", default=True, key='ciphere_format_0')],
        [sg.Radio('Five Char Group', "CIPHER_FORMAT", default=False, key='ciphere_format_1')]
    ]

    layout = [  [sg.Text('Cryptography Simple Encryption', font =('Roboto', 30), justification ='center')],
                [sg.Text('_' * 130)],
                [sg.Text('Plain Text')],[sg.Multiline(size=(130,7), key='box_1')],
                [sg.Column(col1), sg.Column(col2), sg.Column(col3)],
                [sg.Text('_' * 130)],
                [sg.Text('Cipher Text')],[sg.Multiline(size=(130,7), key='box_2')],
                [sg.Text(' ' * 130)],
                [sg.Button('ENCRYPT NOW'), sg.Button('Decryption Mode'), sg.Button('Encryption Mode'), sg.Button('Exit', size = (10, 1))],
            ]

    timer_running, counter = False, 0

    # Create the Window
    width, height = sg.Window.get_screen_size()
    width, height = round(width * 0.6), round(height * 0.8)
    window = sg.Window('Cryptography Simple Encryption', layout, size=(width, height))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout = 10)
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        if event == 'Encryption Mode':
            encrypt_mode = True
        if event == 'Decryption Mode':
            encrypt_mode = False
        if event == "ENCRYPT NOW":
            key = preprocessPlainText(values['key'])
            input_text = preprocessPlainText(values['box_1'])
            ciphere_type = values['ciphere_type']
            ciphere_format = values['ciphere_format_1']
            output_text = process_input(key, input_text, ciphere_type, ciphere_format, encrypt_mode)
            window['box_2'].update(output_text)

    window.close()

if __name__ == "__main__":
    gui_thread = threading.Thread(target=gui_execute, args=())
    gui_thread.start()