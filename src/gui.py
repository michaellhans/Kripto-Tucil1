import PySimpleGUI as sg
import threading

from PySimpleGUI.PySimpleGUI import GREENS
from auto_key_vigenere import *
from default_full_vigenere import *
from extended_vigenere import *
from playfair import *
from affine import *
from hill import *
from util import *
from os import path
import numpy

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

    elif (ciphere_type == 'Playfair Ciphere'):
        if (encrypt_mode):
            output_text = encryptPlayfairCipher(input_text.lower(), key).upper()
        else: 
            output_text = decryptPlayfairCipher(input_text.lower(), key)
    elif (ciphere_type == 'Affine Ciphere'):
        if (encrypt_mode):
            output_text = encryptAffineCipher(input_text.lower(), 26, int(key[0]), int(key[1])).upper()
        else: 
            output_text = decryptAffineCipher(input_text.lower(), 26, int(key[0]), int(key[1]))
    elif (ciphere_type == 'Hill Ciphere'):
        if (encrypt_mode):
            output_text = encryptHillCipher(input_text.lower(), key).upper()
        else: 
            output_text = decryptHillCipher(input_text.lower(), key)

    # print("Input text\t:", input_text)
    # print("Output text\t:", output_text)
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
    col3 = [[sg.Text('Ciphere Text Format')],
        [sg.Radio('No Space', "CIPHER_FORMAT", default=True, key='ciphere_format_0')],
        [sg.Radio('Five Char Group', "CIPHER_FORMAT", default=False, key='ciphere_format_1')]
    ]
    #col4 = [[sg.Text('Name', size =(2, 1)), sg.Input()]]

    layout = [  [sg.Text('Cryptography Simple Encryption', font =('Roboto', 30), justification ='center')],
                [sg.Text('_' * 130)],
                [sg.Text("Choose file: "), sg.Input(), sg.FileBrowse(key='-IN2-'), sg.Button("Submit"),
                sg.Radio('Text File', "FILE_TYPE", default=True, key='is_text'), sg.Radio('Binary File', "FILE_TYPE", default=False, key='is_binary')],
                [sg.Text('Plain Text', key='-IN-')],[sg.Multiline(size=(130,7), key='box_1')],
                [sg.Column(col1), sg.Column(col2), sg.Column(col3)],
                [sg.Text('_' * 130)],
                [sg.Text('Cipher Text', key='-OUT-')],[sg.Multiline(size=(130,7), key='box_2')],
                [sg.Text('Encryption Mode', key='-MODE-')],
                [sg.Button('PROCESS NOW', button_color="Green"), sg.Button('Decryption Mode'), sg.Button('Encryption Mode'), sg.Button('Save Output'), sg.Button('Exit', size = (10, 1))],
            ]

    timer_running, counter = False, 0

    # Create the Window
    width, height = sg.Window.get_screen_size()
    width, height = round(width * 0.6), round(height * 0.8)
    window = sg.Window('Cryptography Simple Encryption', layout, size=(width, height))
    
    # variables
    ext_text = ""
    output_text = ""
    output_filename = ""
    is_binary = False

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout = 10)
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        if event == 'Encryption Mode':
            encrypt_mode = True
            window['-OUT-'].update("Cipher Text")
            window['-IN-'].update("Plain Text")
            window['-MODE-'].update("Encryption Mode")
        if event == 'Decryption Mode':
            encrypt_mode = False
            window['-OUT-'].update("Plain Text")
            window['-IN-'].update("Cipher Text")
            window['-MODE-'].update("Decryption Mode")
        if event == "PROCESS NOW":
            ciphere_type = values['ciphere_type']
            ciphere_format = values['ciphere_format_1']
            input_text = preprocessPlainText(values['box_1'])
            is_binary = values['is_binary']
            if (ciphere_type == "Hill Ciphere"):
                # ex: 17 17 5; 21 18 21; 2 2 19
                key = np.matrix(values['key'])
            elif (ciphere_type == "Affine Ciphere"):
                # format m, b (ex: 7, 10)
                key = values['key'].split(",")
            elif (ciphere_type == "Extended Vigenere Ciphere"):
                key = values['key']
            else:
                key = preprocessPlainText(values['key'])
            if (is_binary):
                if (ext_text == ""):
                    sg.Popup("The binary file is not selected!")
                else:
                    if (ciphere_type != "Extended Vigenere Ciphere"):
                        sg.Popup("The binary file can be only encrypted or decrypted by Extended Vigenere Ciphere!")
                    else:
                        output_text = process_input(key, ext_text, ciphere_type, ciphere_format, encrypt_mode)
                        saveBinaryFile(output_text, output_filename, encrypt_mode)
                        window['box_2'].update("The output binary file is saved on the saved files folder!")
            else:
                output_text = process_input(key, input_text, ciphere_type, ciphere_format, encrypt_mode)
                window['box_2'].update(output_text)
        if event == "Save Output":
            saveOutputText(output_text, output_filename, encrypt_mode)
        if event == "Submit":
            is_binary = values['is_binary']
            ciphere_type = values['ciphere_type']
                
            print(str(values['-IN2-']))
            head, output_filename = path.split(str(values['-IN2-']))
            if (str(values['-IN2-']).endswith(".txt") == False) and (is_binary == True):
                ext_text = readBinary(values['-IN2-'])
                window['box_1'].update("Binary file detected, will not be shown in this box!")
            elif (str(values['-IN2-']).endswith(".txt") == True) and (is_binary == False):
                ext_text = ""
                text = readFile(values['-IN2-'])
                window['box_1'].update(text)
            else:
                sg.Popup("The file type and browsed file is not synchronized!")

    window.close()

if __name__ == "__main__":
    gui_thread = threading.Thread(target=gui_execute, args=())
    gui_thread.start()