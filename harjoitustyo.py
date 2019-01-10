# CT60A0201 Ohjelmoinnin perusteet 2017
# Tekijä: Tuomas Ikonen
# Opiskelijanumero: 
# Päivämäärä: 1.12.2017
# Yhteistyö: Moodle, LUT-ohjelmointiopas, Google, Piazza
# Harjoitustyö 1
######################################################################

# Moduulit
import verolib as tax #verolib.py

# Luokka
class auto:
    vuosi = 0
    paasto = 0
    vero = 0
    
# Aliohjelmat
def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta:")
    print("1) Lue ajoneuvotiedot")
    print("2) Laske ja tulosta verot")
    print("3) Kirjoita CSV-tiedosto")
    print("4) Tulosta CSV-tiedoston data näytölle")
    print("0) Lopeta")
    try:
        syote = int(input("Valintasi: "))
        if 0 <= syote < 5:
            return syote
        else:
            print("Tuntematon valinta.")
    except Exception:
        print("Tuntematon valinta.")

def lueTiedosto():
    try:
        nimi = input("Anna luettavan tiedoston nimi: ")
        data = open(nimi, "r")
        print("Tiedosto " + "'" + nimi + "' " + "luettu.\n")
        for rivi in data:
            rivi
            break
        return data
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.\n")

def laskeTiedot(lista, data):
    while True:
        car = auto()
        rivi = data.readline()
        if rivi == "":
            break
        sarake = rivi.split(";")
        car.vuosi = int(sarake[1][0:4])
        car.paasto = int(sarake[33])
        car.vero = float(tax.vero(int(sarake[33])))
        lista.append(car)
    return lista

def tulostaTiedot(lista):
    t10 = []
    t11 = []
    t12 = []
    t13 = []
    t14 = []
    t15 = []
    t16 = []
    for car in lista:
        if car.vuosi == 2010:
            t10.append(car.vero)
        elif car.vuosi == 2011:
            t11.append(car.vero)
        elif car.vuosi == 2012:
            t12.append(car.vero)
        elif car.vuosi == 2013:
            t13.append(car.vero)
        elif car.vuosi == 2014:
            t14.append(car.vero)
        elif car.vuosi == 2015:
            t15.append(car.vero)
        elif car.vuosi == 2016:
            t16.append(car.vero)
    print("Verokertymät vuosittain 2010-luvulla ovat seuraavat:")
    print("2010", round(sum(t10)), "euroa.")
    print("2011", round(sum(t11)), "euroa.")
    print("2012", round(sum(t12)), "euroa.")
    print("2013", round(sum(t13)), "euroa.")
    print("2014", round(sum(t14)), "euroa.")
    print("2015", round(sum(t15)), "euroa.")
    print("2016", round(sum(t16)), "euroa.\n")

def lajittelu(lista):
    # 2010 eritelty
    a10 = []
    b10 = []
    c10 = []
    d10 = []
    e10 = []
    f10 = []
    g10 = []
    h10 = []
    i10 = []
    # 2011 eritelty
    a11 = []
    b11 = []
    c11 = []
    d11 = []
    e11 = []
    f11 = []
    g11 = []
    h11 = []
    i11 = []
    # 2012 eritelty
    a12 = []
    b12 = []
    c12 = []
    d12 = []
    e12 = []
    f12 = []
    g12 = []
    h12 = []
    i12 = []
    # 2013 eritelty
    a13 = []
    b13 = []
    c13 = []
    d13 = []
    e13 = []
    f13 = []
    g13 = []
    h13 = []
    i13 = []
    # 2014 eritelty
    a14 = []
    b14 = []
    c14 = []
    d14 = []
    e14 = []
    f14 = []
    g14 = []
    h14 = []
    i14 = []
    # 2015 eritelty
    a15 = []
    b15 = []
    c15 = []
    d15 = []
    e15 = []
    f15 = []
    g15 = []
    h15 = []
    i15 = []
    # 2016 eritelty
    a16 = []
    b16 = []
    c16 = []
    d16 = []
    e16 = []
    f16 = []
    g16 = []
    h16 = []
    i16 = []
    for car in lista:
        if car.vuosi == 2010:
            if car.paasto < 50:
                a10.append(car.vero)
            elif 50 <= car.paasto < 100:
                b10.append(car.vero)
            elif 100 <= car.paasto < 150:
                c10.append(car.vero)
            elif 150 <= car.paasto < 200:
                d10.append(car.vero)
            elif 200 <= car.paasto < 250:
                e10.append(car.vero)
            elif 250 <= car.paasto < 300:
                f10.append(car.vero)
            elif 300 <= car.paasto < 350:
                g10.append(car.vero)
            elif 350 <= car.paasto < 400:
                h10.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i10.append(car.vero)
        elif car.vuosi == 2011:
            if car.paasto < 50:
                a11.append(car.vero)
            elif 50 <= car.paasto < 100:
                b11.append(car.vero)
            elif 100 <= car.paasto < 150:
                c11.append(car.vero)
            elif 150 <= car.paasto < 200:
                d11.append(car.vero)
            elif 200 <= car.paasto < 250:
                e11.append(car.vero)
            elif 250 <= car.paasto < 300:
                f11.append(car.vero)
            elif 300 <= car.paasto < 350:
                g11.append(car.vero)
            elif 350 <= car.paasto < 400:
                h11.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i11.append(car.vero)
        elif car.vuosi == 2012:
            if car.paasto < 50:
                a12.append(car.vero)
            elif 50 <= car.paasto < 100:
                b12.append(car.vero)
            elif 100 <= car.paasto < 150:
                c12.append(car.vero)
            elif 150 <= car.paasto < 200:
                d12.append(car.vero)
            elif 200 <= car.paasto < 250:
                e12.append(car.vero)
            elif 250 <= car.paasto < 300:
                f12.append(car.vero)
            elif 300 <= car.paasto < 350:
                g12.append(car.vero)
            elif 350 <= car.paasto < 400:
                h12.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i12.append(car.vero)
        elif car.vuosi == 2013:
            if car.paasto < 50:
                a13.append(car.vero)
            elif 50 <= car.paasto < 100:
                b13.append(car.vero)
            elif 100 <= car.paasto < 150:
                c13.append(car.vero)
            elif 150 <= car.paasto < 200:
                d13.append(car.vero)
            elif 200 <= car.paasto < 250:
                e13.append(car.vero)
            elif 250 <= car.paasto < 300:
                f13.append(car.vero)
            elif 300 <= car.paasto < 350:
                g13.append(car.vero)
            elif 350 <= car.paasto < 400:
                h13.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i13.append(car.vero)
        elif car.vuosi == 2014:
            if car.paasto < 50:
                a14.append(car.vero)
            elif 50 <= car.paasto < 100:
                b14.append(car.vero)
            elif 100 <= car.paasto < 150:
                c14.append(car.vero)
            elif 150 <= car.paasto < 200:
                d14.append(car.vero)
            elif 200 <= car.paasto < 250:
                e14.append(car.vero)
            elif 250 <= car.paasto < 300:
                f14.append(car.vero)
            elif 300 <= car.paasto < 350:
                g14.append(car.vero)
            elif 350 <= car.paasto < 400:
                h14.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i14.append(car.vero)
        elif car.vuosi == 2015:
            if car.paasto < 50:
                a15.append(car.vero)
            elif 50 <= car.paasto < 100:
                b15.append(car.vero)
            elif 100 <= car.paasto < 150:
                c15.append(car.vero)
            elif 150 <= car.paasto < 200:
                d15.append(car.vero)
            elif 200 <= car.paasto < 250:
                e15.append(car.vero)
            elif 250 <= car.paasto < 300:
                f15.append(car.vero)
            elif 300 <= car.paasto < 350:
                g15.append(car.vero)
            elif 350 <= car.paasto < 400:
                h15.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i15.append(car.vero)
        elif car.vuosi == 2016:
            if car.paasto < 50:
                a16.append(car.vero)
            elif 50 <= car.paasto < 100:
                b16.append(car.vero)
            elif 100 <= car.paasto < 150:
                c16.append(car.vero)
            elif 150 <= car.paasto < 200:
                d16.append(car.vero)
            elif 200 <= car.paasto < 250:
                e16.append(car.vero)
            elif 250 <= car.paasto < 300:
                f16.append(car.vero)
            elif 300 <= car.paasto < 350:
                g16.append(car.vero)
            elif 350 <= car.paasto < 400:
                h16.append(car.vero)
            elif 400 <= car.paasto < 1000:
                i16.append(car.vero)
    # end of for
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedosto = open(nimi, "w", encoding="utf-8")
    tiedosto.write(";50;100;150;200;250;300;350;400;1000;\n")
    tiedosto.write("2010;"+str(round(sum(a10)))+";"+str(round(sum(b10)))+";"+str(round(sum(c10)))+";"
                   +str(round(sum(d10)))+";"+str(round(sum(e10)))+";"+str(round(sum(f10)))+";"
                   +str(round(sum(g10)))+";"+str(round(sum(h10)))+";"+str(round(sum(i10)))+";\n")
    tiedosto.write("2011;"+str(round(sum(a11)))+";"+str(round(sum(b11)))+";"+str(round(sum(c11)))+";"
                   +str(round(sum(d11)))+";"+str(round(sum(e11)))+";"+str(round(sum(f11)))+";"
                   +str(round(sum(g11)))+";"+str(round(sum(h11)))+";"+str(round(sum(i11)))+";\n")
    tiedosto.write("2012;"+str(round(sum(a12)))+";"+str(round(sum(b12)))+";"+str(round(sum(c12)))+";"
                   +str(round(sum(d12)))+";"+str(round(sum(e12)))+";"+str(round(sum(f12)))+";"
                   +str(round(sum(g12)))+";"+str(round(sum(h12)))+";"+str(round(sum(i12)))+";\n")
    tiedosto.write("2013;"+str(round(sum(a13)))+";"+str(round(sum(b13)))+";"+str(round(sum(c13)))+";"
                   +str(round(sum(d13)))+";"+str(round(sum(e13)))+";"+str(round(sum(f13)))+";"
                   +str(round(sum(g13)))+";"+str(round(sum(h13)))+";"+str(round(sum(i13)))+";\n")
    tiedosto.write("2014;"+str(round(sum(a14)))+";"+str(round(sum(b14)))+";"+str(round(sum(c14)))+";"
                   +str(round(sum(d14)))+";"+str(round(sum(e14)))+";"+str(round(sum(f14)))+";"
                   +str(round(sum(g14)))+";"+str(round(sum(h14)))+";"+str(round(sum(i14)))+";\n")
    tiedosto.write("2015;"+str(round(sum(a15)))+";"+str(round(sum(b15)))+";"+str(round(sum(c15)))+";"
                   +str(round(sum(d15)))+";"+str(round(sum(e15)))+";"+str(round(sum(f15)))+";"
                   +str(round(sum(g15)))+";"+str(round(sum(h15)))+";"+str(round(sum(i15)))+";\n")
    tiedosto.write("2016;"+str(round(sum(a16)))+";"+str(round(sum(b16)))+";"+str(round(sum(c16)))+";"
                   +str(round(sum(d16)))+";"+str(round(sum(e16)))+";"+str(round(sum(f16)))+";"
                   +str(round(sum(g16)))+";"+str(round(sum(h16)))+";"+str(round(sum(i16)))+";\n")
    tiedosto.close()
    print("CSV-tiedosto kirjoitettu.\n")
    return nimi

def tulostaTiedotKirjoitettu(nimi):
    print("CSV-tiedoston data on seuraava:")
    tiedosto = open(nimi, "r", encoding="utf=8")
    for rivi in tiedosto:
        print(rivi[:-1])
    print("")

def paaohjelma():
    tiedot = []
    while True:
        valinta = valikko()
        if valinta == 0:
            try:
                tiedosto.close()
                break
            except UnboundLocalError:
                break
        elif valinta == 1: # Avataan tiedosto käsittelyä varten.
            tiedosto = lueTiedosto()
        elif valinta == 2: # Lasketaan ja muokataan tiedot informatiivisempaan muotoon, minkä jälkeen tulostetaan.
            tiedot = laskeTiedot(tiedot, tiedosto)
            tulostaTiedot(tiedot)
        elif valinta == 3: # Lajitellaan tiedot tarkemmin ja kirjoitetaan tiedostoon.
            tiedostoKirjoitettu = lajittelu(tiedot)
        elif valinta == 4: # Tulostetaan kirjoitetun tiedoston data.
            tulostaTiedotKirjoitettu(tiedostoKirjoitettu)

# Ohjelma
paaohjelma()
print("Kiitos ohjelman käytöstä.")

######################################################################
# eof
