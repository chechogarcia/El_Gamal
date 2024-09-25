def letter_ascii(message):
    message_ascii = ""
    for i in message:
        for letter in i:
            aux = str(ord(letter))
            if len(aux)==2:
                message_ascii = message_ascii + aux  + "00"
            elif len(aux)==1:
                message_ascii =  message_ascii +  aux  + "00"
            else:
             message_ascii = message_ascii + aux + "00"
    message_ascii = int(message_ascii)
    return message_ascii

def ascii_letter(message_ascii):
    ascii = str(message_ascii)
    message = ""
    text = []
    aux = ""
    for i in range(0, len(ascii)):
        if ascii[i] != "0" :
            aux = aux + ascii[i]
        elif ascii[i] == "0" and i == (len(ascii) - 1):
            continue
        elif ascii[i] == "0" and ascii[i - 1] != "0" and ascii[i + 1] != "0":
            aux = aux + ascii[i]
        elif ascii[i] == "0" and ascii[i + 1] == "0" and i == (len(ascii) - 2):
            text.append(aux)
            aux = ""
        elif ascii[i] == "0" and ascii[i + 1] == "0" and ascii[i + 2] != "0" and i != (len(ascii) - 1):
            text.append(aux)
            aux = ""
        elif ascii[i] == "0" and ascii[i + 1] == "0" and ascii[i + 2] == "0":
            aux = aux + ascii[i]
    
    for i in text:
        message = message + chr(int(i))

    return message