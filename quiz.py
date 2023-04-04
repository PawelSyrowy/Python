import json

points = 0

def show_question(question):
    global points

    print()
    print(question["pytanie"])
    print("a:",question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer=input("Którą odpowiedź wybierasz? ")

    if answer==question["prawidlowa_odpowiedz"]:
        points+=1
        print("Prawidłowa odpowiedź brawo! Masz już",points,"punktów")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to:"+question["prawidlowa_odpowiedz"]+ ".")

with open("quiz.json") as json_file:
    questions=json.load(json_file)

    for i in range(0,len(questions)):
        show_question(questions[i])

print("To koniec gry, liczba zdobytych punktów to "+str(points)+".")

#walidacja wpisywanych danych
#losowanie pytań, więcej pytań
#zapisywanie które pytania już pokazywaliśmy użytkownikowi
#różne kategorie pytań
#różne poziomy trudności, różne punktowanie pytań,
#opcja nie wiem, a za złą odpowiedź błąd ujemny
#pół na pół jak w milionerach
#ranking najlepszych graczy