import flet as ft
import pyperclip

def main(page: ft.Page):
    morse_dic = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': ' '}

    letter2num = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26'}

    morse_reverse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', ' ': ' '
    }

    num_reverse = {
        '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F',
        '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L',
        '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R',
        '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X',
        '25': 'Y', '26': 'Z'
    }

    def morse_enc(text):
        text = text.upper()  
        morse_txt = ''
        for letter in text:
            if letter in morse_dic:
                morse_txt += morse_dic[letter] + '/'
            elif letter == ' ':
                morse_txt += '//'
        return morse_txt

    def num_enc(text):
        text = text.upper()
        num_txt = ''
        for letter in text:
            if letter in letter2num:
                num_txt += letter2num[letter] + ' '
            elif letter == ' ':
                num_txt += '/ '
        return num_txt

    def piggy_enc(text):
        words = text.lower().split()
        result = []
        vowels = 'aeiou'

        for word in words:
            if word[0] in vowels:
                result.append(word + 'way')
            else:
                for i, letter in enumerate(word):
                    if letter in vowels:
                        result.append(word[i:] + word[:i] + 'ay')
                        break
        return ' '.join(result)

    def enc_clk(e):
        if not encr.value:
            rslt.value = "Please enter a message to encrypt"
            page.update()
            return

        if encry_chc.value == "Morse Code":
            rslt.value = morse_enc(encr.value)
        elif encry_chc.value == "Letter to Number":
            rslt.value = num_enc(encr.value)
        elif encry_chc.value == "Pig Latin":
            rslt.value = piggy_enc(encr.value)
        page.update()

    def copy(e):
        if rslt.value:
            pyperclip.copy(rslt.value)

    def morse_dec(text):
        try:
            words = text.strip('/').split('//')
            decrypted = ''
            for word in words:
                letters = word.strip('/').split('/')
                for letter in letters:
                    if letter in morse_reverse:
                        decrypted += morse_reverse[letter]
                decrypted += ' '
            return decrypted.strip()
        except:
            return "Invalid Morse Code format"

    def num_dec(text):
        try:
            words = text.split('/')
            decrypted = ''
            for word in words:
                numbers = word.strip().split()
                for num in numbers:
                    for key, value in letter2num.items():
                        if value == num:
                            decrypted += key
                decrypted += ' '
            return decrypted.strip()
        except:
            return "Invalid Number format"

    def piggy_dec(text):
        words = text.lower().split()
        result = []
        for word in words:
            if word.endswith('way'):
                result.append(word[:-3])
            elif word.endswith('ay'):
                word = word[:-2]
                while not word[0] in 'aeiou':
                    word = word[1:] + word[0]
                result.append(word)
        return ' '.join(result)

    def decry_clk(e):
        if not encr.value:
            rslt.value = "Please enter a message to decrypt"
            page.update()
            return

        if encry_chc.value == "Morse Code":
            rslt.value = morse_dec(encr.value)
        elif encry_chc.value == "Letter to Number":
            rslt.value = num_dec(encr.value)
        elif encry_chc.value == "Pig Latin":
            rslt.value = piggy_dec(encr.value)
        page.update()

    encr = ft.TextField(label="Enter message", width=400)

    encry_chc = ft.Dropdown(
        width=200,
        options=[ft.dropdown.Option("Morse Code"), ft.dropdown.Option("Letter to Number"), ft.dropdown.Option("Pig Latin")])

    rslt = ft.TextField(label="Result", read_only=True,width=400)

    encrypt_btn = ft.ElevatedButton("Encrypt", on_click=enc_clk)
    decrypt_btn = ft.ElevatedButton("Decrypt", on_click=decry_clk)
    copy_btn = ft.ElevatedButton("Copy", on_click=copy)

    page.add(encr, encry_chc, encrypt_btn, decrypt_btn, copy_btn, rslt)

ft.app(main)