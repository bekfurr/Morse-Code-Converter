import tkinter as tk

MORZE_LUGAT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_morze(text):
    morze_code = ''
    for char in text.upper():
        morze_code += MORZE_LUGAT.get(char, '') + ' '
    return morze_code.strip()


def morze_text(morse_code):
    morse_code += ' '
    m_sa = ''
    m_hi = ''
    for char in morse_code:
        if char != ' ':
            i = 0
            m_hi += char
        else:
            i += 1
            if i == 2:
                m_sa += ' '
            else:
                m_sa += list(MORZE_LUGAT.keys())[list(MORZE_LUGAT.values()).index(m_hi)]
                m_hi = ''
    return m_sa

def convert():
    input_text = input_maydon.get("1.0", "end-1c")
    if ozgar.get() == 1:
        result = text_morze(input_text)
    else:
        result = morze_text(input_text)
    output_maydon.delete("1.0", tk.END)
    output_maydon.insert(tk.END, result)

def clear_all():
    input_maydon.delete("1.0", tk.END)
    output_maydon.delete("1.0", tk.END)

oyna = tk.Tk()
oyna.title("Morze Kod Konvertori")

tk.Label(oyna, text="Kiritish:").grid(row=0, column=0, padx=10, pady=10)
input_maydon = tk.Text(oyna, height=5, width=50)
input_maydon.grid(row=0, column=1, padx=10, pady=10)

tk.Label(oyna, text="Chiqarish:").grid(row=1, column=0, padx=10, pady=10)
output_maydon = tk.Text(oyna, height=5, width=50)
output_maydon.grid(row=1, column=1, padx=10, pady=10)

ozgar = tk.IntVar()
ozgar.set(1)
tk.Radiobutton(oyna, text="Matndan Morzega", variable=ozgar, value=1).grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(oyna, text="Morzedan Matnga", variable=ozgar, value=2).grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(oyna, text="Konvertatsiya", command=convert)
convert_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(oyna, text="Tozalash", command=clear_all)
clear_button.grid(row=3, column=1, padx=10, pady=10)

oyna.mainloop()














