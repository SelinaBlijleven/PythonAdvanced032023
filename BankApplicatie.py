import BankAccount

holder = "Lina"
balance = 1000

# Maak een account aan
account = BankAccount.BankAccount(holder, balance)

# Zijn we klaar?
klaar = False

# Start het keuzemenu
while not klaar:
    print(f"Welkom bij de bank {holder}")
    print("Typ 1 om geld te storten.")
    print("Typ 2 om geld op te nemen.")
    print("Typ 3 om je balans te bekijken.")
    print("Typ 4 om af te sluiten.")
    ans = input("Wat wil je doen?")

    if (not ans.isnumeric()):
        print("Vul alsjeblieft 1, 2 of 3 in.")
        continue

    # Handel de keuze van de gebruiker af
    ans = int(ans)
    if (ans == 1):
        account.deposit(10)
    elif (ans == 2):
        account.withdraw(10)
    elif (ans == 3):
        print(account.info())
    else:
        klaar = True

print("Bedankt voor uw bezoek!")