txt = input('Add text: ')
if txt.isnumeric():
    new_text = int(txt)
    b = bin(new_text)
    o = oct(new_text)
    h = hex(new_text)
    print(b, o, h, sep='\n')
else:
    if str.islower(txt) == True:
        print('Text is in ASCII standart!')
    else:
        print('Text is NOT in ASCII standart!')