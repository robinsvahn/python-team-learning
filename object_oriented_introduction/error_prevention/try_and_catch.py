##########################################################################################################################################################################################
print("###########################################################################################################################################################################################")
# Problematisk kod (om man skriver in något annat än en siffra kommer det bli ett error/exception)
print("Problematisk kod (om man skriver in något annat än en siffra kommer det bli ett error/exception)")

user_input = float(input("Please enter a number: "))

this_is_a_number = 5  # Här gör vi lite matematiska beräkningar bara för att bevisa att vi nu försäkrat oss att "user_input" är en siffra
sum = this_is_a_number + int(user_input)

# och en print, så man ser att det funkar
print(f"If we add 5 to your number, you get: {sum}")

#
#
#
#
#

##########################################################################################################################################################################################
print("###########################################################################################################################################################################################")
# Lösning med try except, användaren måste starta om programmet varje gång hen gör ett misstag, INTE fint!
print("Lösning med try except, användaren måste starta om programmet varje gång hen gör ett misstag, INTE fint!")
user_input = ""

try:  # Try definerar säger till datorn att vi nu kommer försöka något som kansnke kommer gå snett, och om det gör det, ska datorn inte crasha, utan hoppa till koden efter "except"
    # Försök transformera inputen till en float
    user_input = float(input("Please enter a number: "))

except ValueError:  # Om det misslyckas, hopa hit, annars hoppa över denna code
    print("The input was not a number, the program has now lost faith in you and will shutdown")
    import sys  # Importera en modul som möjliggör en direkt shutdown av programmet
    sys.exit()  # Stäng ner programmet

this_is_a_number = 5  # Här gör vi lite matematiska beräkningar bara för att bevisa att vi nu försäkrat oss att "user_input" är en siffra
sum = this_is_a_number + int(user_input)

# och en print, så man ser att det funkar
print(f"If we add 5 to your number, you get: {sum}")

#
#
#
#
#

###########################################################################################################################################################################################
print("###########################################################################################################################################################################################")
# Lösning med while loop, smidigt, flexibelt, sexigt.
print("Lösning med while loop, smidigt, kompakt, flexibelt, sexigt.")

# Be om user input UTAN att "transformera" den till en float
user_input = input("Please enter a number: ")

while(not user_input.isnumeric()):  # Kolla om inputen INTE är numerisk, detta funkar alltså bara för INTEGER, alltså heltal utan komma, men jag tycker att ett budget program inte behöver accceptera komma summor. (Om du inte håller med finns en fulare float lösning längre ner)
    user_input = input(
        "My dear friend, i said a number, now please stop beeing such a jackass, and write a whole NUMBER using only numerical symbols: ")  # Be usern om en ny input, tills den lyckas att skriva in ett positivt heltal.

this_is_a_number = 5  # Här gör vi lite matematiska beräkningar bara för att bevisa att vi nu försäkrat oss att "user_input" är en siffra
sum = this_is_a_number + int(user_input)

# och en print, så man ser att det funkar
print(f"If we add 5 to your number, you get: {sum}")

#
#
#
#
#

###########################################################################################################################################################################################
print("###########################################################################################################################################################################################")
# Lösning med en kombination av en while loop och en try except, för att funka när inputen även får vara ett komma tal, alltså float
print("Lösning med en kombination av en while loop och en try except, för att funka när inputen även får vara ett komma tal, alltså float")

while(True):  # en while som håller igång tills vi säger att den ska sluta med en "break", populärt bland akademiker och matematiker, men äcklande för programmerare
    try:
        user_input = float(input("Please enter a number: "))
        break
    except ValueError:
        print("That is not a number my friend, please write a number like 3.5, 45000, 9999.523, etc")
        continue


this_is_a_number = 5  # Här gör vi lite matematiska beräkningar bara för att bevisa att vi nu försäkrat oss att "user_input" är en siffra
sum = this_is_a_number + float(user_input)


# och en print, så man ser att det funkar
print(f"If we add 5 to your number, you get: {sum}")
