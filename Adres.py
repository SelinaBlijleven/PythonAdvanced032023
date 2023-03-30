'''
Implementatie van de Adres-klasse
'''
class Adres:

    # Al onze adressen zijn in Nederland
    land = "Nederland"

    def __init__(self, straat, huisnummer, postcode, stad):
        '''
        Constructor voor een adres

        :param  string  Straatnaam
        :param  int     Huisnummer
        :param  string  Postcode
        :param  string  Stad
        '''
        self.__straat = straat
        self.__huisnummer = huisnummer
        self.__postcode = postcode
        self.__stad = stad

    def __str__(self):
        '''
        Maak een weergave van het adres zoals bijvoorbeeld op
        brieven geprint wordt.

        :return string
        '''
        return f"{self.__straat} {self.__huisnummer}\n" \
               f"{self.__postcode}, {self.__stad}\n" \
               f"{self.land}"

# Lijst met adressen
adressen = [
    ['Maliesingel', 29, '3581BJ', "Utrecht"],
    ['Maliesingel', 27, '3581BX', "Utrecht"]
]

# We loopen over de adressen en maken voor elk een object aan.
# Vervolgens printen we de string-representatie.
for adres_info in adressen:
    # Pak de info uit de lijst uit in verschillende variabelen
    straat, huisnummer, postcode, stad = adres_info

    # Maak het adres object aan
    adres = Adres(straat, huisnummer, postcode, stad)

    # Door de print-functie aan te roepen maken we een string-representatie van het adres
    # en kunnen we ons object nu makkelijk inzien.
    print(adres)
