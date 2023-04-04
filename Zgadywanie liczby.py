import random

# Losujemy liczbę z zakresu 1-100
liczba = random.randint(1, 100)

print("Witaj w grze w zgadywanie liczby!")
print("Zgadnij, jaką liczbę wylosował komputer.")

# Ustawiamy początkową wartość liczby prób na 0
liczba_prob = 0

# Rozpoczynamy pętlę zgadywania
while True:
    # Zwiększamy liczbę prób
    liczba_prob += 1

    # Wczytujemy liczbę od użytkownika
    strzal = input("Podaj swoją liczbę: ")

    # Sprawdzamy, czy użytkownik podał poprawny typ danych
    try:
        strzal = int(strzal)
    except ValueError:
        print("To nie jest liczba! Spróbuj ponownie.")
        continue

    # Sprawdzamy, czy użytkownik zgadł liczbę
    if strzal == liczba:
        print("Gratulacje! Zgadłeś liczbę w", liczba_prob, "próbach.")
        break

    # Informujemy użytkownika, czy podał liczbę większą czy mniejszą od wylosowanej
    if strzal < liczba:
        print("Wylosowana liczba jest większa.")
    else:
        print("Wylosowana liczba jest mniejsza.")