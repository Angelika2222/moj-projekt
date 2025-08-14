print ("To jest mój projekt do zadania 3 w automatyzacji")


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