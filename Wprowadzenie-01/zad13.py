książki = []

atrybutyKsiążki = ('Tytuł', 'Autor', 'Wydawca', 'Miejsce wydania', 'Rok wydania')

książka = {}

warunek = True
print("Wprowadź kilka książek:")

indeksKsiążki = 0
while warunek == True:

    książka[indeksKsiążki] = \
        {
            'tytuł': input("Tytuł: "),
            'autor': input("Autor: "),
            'wydawca': input("Wydawca: "),
            'miejsce_wydania': input("Miejsce wydania: "),
            'rok_wydania': input("Rok wydania: ")
        }

    indeksKsiążki = indeksKsiążki + 1

    decyzja = input("Czy chcesz wprowadzić następną książkę? (T/N): ")

    if decyzja == 'N': break
