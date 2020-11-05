def usun(text, letter):
    do_usuniecia = str(letter)

    #tekst_zmieniony1 = text.replace(do_usuniecia.upper(),"")
    #tekst_zmieniony = tekst_zmieniony1.replace(do_usuniecia.lower(),"")

    tekst_zmieniony = text.replace(do_usuniecia.upper(), "").replace(do_usuniecia.lower(), "")
    return tekst_zmieniony

text = "Bananowy Ananas"
print(usun(text,"a"))
