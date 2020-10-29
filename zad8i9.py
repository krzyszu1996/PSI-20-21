student1 = ("102175", "Nisha Morrow")
student2 = ("101101", "Tianna Mitchell")
student3 = ("118876", "Lorraine Cardenas")
student4 = ("103388", "Ariyan Tran")
student5 = ("142120", "Judy Howarth")
student6 = ("118497", "Savannah Hensley")
student7 = ("112620", "Luciano Barnett")
student8 = ("131978", "Fahima Howard")
student9 = ("128883", "Asiyah Dunkley")
student10 = ("144463", "Elisa Halliday")

lista_studentow = student1, student2, student3

for i in range(3):
    print(lista_studentow[i])

print(lista_studentow[2][1])

#nie jestem pewien czy to o to chodziło :/
#Przekształć poprzednie zadanie na słownik, a następnie dodaj
#pary zawierające wiek, adres email, rok urodzenia oraz adres.

slownik = {}
slownik = dict(lista_studentow)
slownik = dict(jeden=1, dwa=2, trzy=3)
slownik = dict({"102175":"Nisha Morrow", "101101":"Tianna Mitchell", "118876":"Lorraine Cardenas"})

print(slownik)

print(slownik["102175"])

print(slownik.keys())


