def informacjeOTekscie(data_text):
    length = len(data_text)
    # print(length)

    letters = list()
    for i in range(length):
        letters.append(data_text[i])
        # print(letters)

    big_letters = data_text.upper()
    # print(big_letters)

    small_letters = data_text.lower()
    # print((small_letters))

    dane = \
        {
            'length': length,
            'letters': letters,
            'big_letters': big_letters,
            'small_letters': small_letters
        }

    return dane


def wyswietlSlownik(slownik):
    for klucz, wartosc in slownik.items():
        print("{} : {}".format(str(klucz), str(wartosc)))


tekst = "Krzysztof Szulc"

info = informacjeOTekscie(tekst)

wyswietlSlownik(info)