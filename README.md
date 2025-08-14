# moj-projekt
moje pierwsze repozytorium
# Prosty program liczący odsetki na koncie oszczędnościowym
Ten projekt to prosty kalkulator liczący zysk na koncie oszczędnościowym . Pobiera dane od użytkownika 

##Uruchomienie programu
1.Upewnij się ze masz zainstalowanego Pythona

#2.W terminalu wpisz :
python odsetki_na_koncie.py

#3.Podaj liczby :

#Podaj kwotę bazową:

#podaj liczbę lat (max.3):

#podaj obowiązujące oprocentowanie:

start_amount = float(input("Kwota bazowa: "))
years = int(input("Liczba lat: "))
interest_rate = float(input("Oprocentowanie (np. 0.08 dla 8%): "))
first_year = (start_amount * interest_rate ) + start_amount
print("po pierwszym roku", first_year)
second_year = (first_year * interest_rate ) +first_year
print("Po drugim roku", second_year)
third_year = (second_year * interest_rate ) + second_year
print("Po trzecim roku", third_year )
earn = third_year - start_amount
print("cAŁKOWITY ZYSK", int(earn))
