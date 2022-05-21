import random
from random import randrange
from datetime import timedelta
from datetime import datetime
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def startAndEndGen():
    d1 = datetime.strptime('1/1/2021 09:15:32', '%d/%m/%Y %H:%M:%S')
    d2 = datetime.strptime('1/1/2022 16:15:32', '%d/%m/%Y %H:%M:%S')
    start=random_date(d1,d2)
    randInt=random.randint(7,40)
    end=start+timedelta(days=randInt)
    return start,end
#sprzetjednostkawojskowa
def generateId():
    return random.randint(1,50)
def generateSprzetJednostka():

    poczatek,koniec=startAndEndGen()
    idSprzetu=random.randint(1,50)
    idJednostki=random.randint(1,50)
    return poczatek,koniec,idSprzetu,idJednostki
def generateSprzet():
    typ = ["Powietrzna", "Ladowa", "Morska"]
    nazwa=["Rosomak", "Langusta", "Żbik" ,"Humvee","Destroy","Chwytacz", "Jaguar"]
    Stan=random.randint(1,5)
    Przeglad=startAndEndGen()
    MiniRanga=random.randint(1,20)
    return random.choice(typ),random.choice(nazwa),Stan,Przeglad,MiniRanga
def ZolnierzJednostka():
    Poczatek,Koniec=startAndEndGen()
    return Poczatek,Koniec
def Przeglad():
    Data=startAndEndGen()
    Opis=["Naprawa Sprzęgla","Wymiana oleju","Naprawa lufy","Czyszczenie w trudno dostepnych miejscach","Wszystko ok"]
    return random.choice(Opis),Data
def Remont():
    Data=startAndEndGen()
    Opis=["Remont Silniki","Remont Lufy","Remont zawieszenie","Remont systemow GPS"]
    return random.choice(Opis),Data
def Czesc():
    Opis=["Naped gasienicowy","armata czołgowa","błotniki","Wyrzutnie granatow dymnych","Przeciwlotniczy wielokalibrowy karabin maszynowy",
         "Przedział silnikowy","Wieżyczka dowódcy","Czołgowy karabin maszynowy sprzeżony z armatą","Pochylony pancerz przedni","Burtowy karabin maszynowy"]
    Cena=random.randint(1500,4000)
    return random.choice(Opis),Cena
def Jednostka():
    Nazwa=["Samodzielny Batalion Łączności KBW","Dowództwo 16 Brygady Wojsk Ochrony Pogranicza","4 Pułk KBW","33.Batalion Łączności","Batalion Mostowy","17.Pułk Piechoty"]
    return random.choice(Nazwa)
def Manewry():
    Poczatek,Koniec=startAndEndGen()
    return Poczatek,Koniec
def Zolnierz():
    Imie=["Przemek","Daniel","Bartosz","Pawel","Patryk","Stanislaw"]
    Nazwisko=["Kowalski","Nowak","Wiśniewska","Wójcik","Kowalczyk","Kamin","Lewandowski","Zieliński","Wozniak"]
    Stopien=random.randint(1,20)
    return random.choice(Imie),random.choice(Nazwisko),Stopien
def Adres():
    WojewodzctwoMiasto={"dolnośląskie":"Wrocław","kujawsko-pomorskie":"Toruń","Łódzkie":"Łódź","Opolskie":"Opole","Pomorskie":"Gdańsk"}
    Ulica=["Grodzka","3Maja","Kopernika","Gdańska","Polna","Krótka","szkolna"]
    Numer=random.randint(5,100)
    return random.choice()
def Dostawca():
    Nazwa=["Accuracy International","Beretta Holdinga","Winchester Repeating Arms Company","Herstal Group","Israel Military Industries"]
    return random.choice(Nazwa)

