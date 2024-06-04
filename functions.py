def lotindan_kirillga(lotin_matn):
    lotin_kirill_dict = {
        "A": "А", "B": "Б", "D": "Д", "E": "Э", "F": "Ф", "G": "Г", "H": "Ҳ", "I": "И", "J": "Ж", "K": "К", "L": "Л",
        "M": "М", "N": "Н", "O": "О", "P": "П", "Q": "Қ", "R": "Р", "S": "С", "T": "Т", "U": "У", "V": "В", "X": "Х",
        "Y": "Й", "Z": "З", "a": "а", "b": "б", "d": "д", "e": "э", "f": "ф", "g": "г", "h": "ҳ", "i": "и", "j": "ж",
        "k": "к", "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у",
        "v": "в", "x": "х", "y": "й", "z": "з", "Sh": "Ш", "sh": "ш", "Ch": "Ч", "ch": "ч", "Ng": "Нг", "ng": "нг",
        "O‘": "Ў", "o‘": "ў", "G‘": "Ғ", "g‘": "ғ", "‘": "ъ"}
    kirill_matn = ""
    i = 0
    while i < len(lotin_matn):
        if i+2 <= len(lotin_matn) and lotin_matn[i:i+2] in lotin_kirill_dict:
            kirill_matn += lotin_kirill_dict[lotin_matn[i:i+2]]
            i += 2
        elif i+1 <= len(lotin_matn) and lotin_matn[i:i+1] in lotin_kirill_dict:
            kirill_matn += lotin_kirill_dict[lotin_matn[i:i+1]]
            i += 1
        else:
            kirill_matn += lotin_matn[i]
            i += 1
    return kirill_matn


def kirilldan_lotinga(kirill_matn):
    kirill_lotin_dict = {
        "А": "A", "Б": "B", "Д": "D", "Э": "E", "Ф": "F", "Г": "G", "Ҳ": "H", "И": "I", "Ж": "J", "К": "K", "Л": "L",
        "М": "M", "Н": "N", "О": "O", "П": "P", "Қ": "Q", "Р": "R", "С": "S", "Т": "T", "У": "U", "В": "V", "Х": "X",
        "Й": "Y", "З": "Z", "а": "a", "б": "b", "д": "d", "э": "e", "ф": "f", "г": "g", "ҳ": "h", "и": "i", "ж": "j",
        "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "қ": "q", "р": "r", "с": "s", "т": "t", "у": "u",
        "в": "v", "х": "x", "й": "y", "з": "z", "Ш": "Sh", "ш": "sh", "Ч": "Ch", "ч": "ch", "Нг": "Ng", "нг": "ng",
        "Ў": "O‘", "ў": "o‘", "Ғ": "G‘", "ғ": "g‘", "ъ": "‘", "ы": "i", "Ы": "I", "Я": "Ya", "я": "ya", "Щ": "Sh", "щ": "sh"}
    lotin_matn = ""
    i = 0
    while i < len(kirill_matn):
        if i+2 <= len(kirill_matn) and kirill_matn[i:i+2] in kirill_lotin_dict:
            lotin_matn += kirill_lotin_dict[kirill_matn[i:i+2]]
            i += 2
        elif i+1 <= len(kirill_matn) and kirill_matn[i:i+1] in kirill_lotin_dict:
            lotin_matn += kirill_lotin_dict[kirill_matn[i:i+1]]
            i += 1
        else:
            lotin_matn += kirill_matn[i]
            i += 1
    return lotin_matn


def tekshir(matn):
    kirill_harf = 0
    lotin_harf = 0

    for harf in matn:
        if u'\u0400' <= harf <= u'\u04FF':
            kirill_harf += 1
        elif u'\u0041' <= harf <= u'\u005A' or u'\u0061' <= harf <= u'\u007A':
            lotin_harf += 1

    if kirill_harf > lotin_harf:
        return "Kirill"
    elif lotin_harf > kirill_harf:
        return "Lotin"
    else:
        return "Matnda hech qanday lotin yoki kirill harflari mavjud emas."
