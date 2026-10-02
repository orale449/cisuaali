# organizer.py
import os
import shutil
import sys
from config import DIRECTORY_MAPPING

def luo_kansio(polku):
    """Luo kansion jos sitä ei ole olemassa. Sisältää virheentarkastuksen."""
    try:
        if not os.path.exists(polku):
            os.makedirs(polku)
            print(f"Luotu uusi kansio: {polku}")
    except OSError as e:
        print(f"VIRHE: Kansiota {polku} ei voitu luoda. Syy: {e}", file=sys.stderr)

def hae_kohdekansio(tiedostopaate):
    """Etsii config.py-tiedostosta oikean kansion tiedostopäätteelle."""
    paate_pienellä = tiedostopaate.lower()
    for kansio, paatteet in DIRECTORY_MAPPING.items():
        if paate_pienellä in paatteet:
            return kansio
    return "Muut"  # Jos päätettä ei löydy listalta, se menee 'Muut'-kansioon

def jarjestele_tyopoyta(tyopoyta_polku):
    """Käy läpi työpöydän tiedostot ja siirtää ne oikeisiin kansioihin."""
    
    # Virheentarkastus: Tarkistetaan onko annettua polkua olemassa
    if not os.path.exists(tyopoyta_polku):
        print(f"VIRHE: Polkua '{tyopoyta_polku}' ei löydy. Tarkista polku config-vaiheesta.", file=sys.stderr)
        return

    print(f"Aloitetaan järjestely kansiossa: {tyopoyta_polku}\n" + "-"*40)

    # Käydään läpi kaikki kohteet työpöydällä
    try:
        kohteet = os.listdir(tyopoyta_polku)
    except PermissionError:
        print("VIRHE: Ei oikeuksia lukea kansiota.", file=sys.stderr)
        return

    for kohde in kohteet:
        koko_polku = os.path.join(tyopoyta_polku, kohde)

        # Varmistetaan, että käsitellään vain tiedostoja (ei kosketa jo olemassa oleviin kansioihin)
        if os.path.isfile(koko_polku):
            # Erotetaan tiedostonimi ja pääte (esim. 'kuva.png' -> 'kuva' ja '.png')
            _, paate = os.path.splitext(kohde)
            
            # Ohitetaan itse skriptitiedostot, etteivät ne siirrä itseään
            if kohde in ['organizer.py', 'config.py']:
                continue

            # Määritetään kohdekansio
            kansion_nimi = hae_kohdekansio(paate)
            kohdekansio_polku = os.path.join(tyopoyta_polku, kansion_nimi)

            # Luodaan kohdekansio tarvittaessa
            luo_kansio(kohdekansio_polku)

            # Siirretään tiedosto virheentarkastuksen kanssa
            uusi_sijainti = os.path.join(kohdekansio_polku, kohde)
            try:
                shutil.move(koko_polku, uusi_sijainti)
                print(f"Siirretty: {kohde} -> Kansiossa {kansion_nimi}")
            except Exception as e:
                print(f"VIRHE: Tiedoston {kohde} siirto epäonnistui: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Automaattinen työpöydän polun etsintä (toimii Windowsilla ja Mac/Linuxilla)
    kotikansio = os.path.expanduser("~")
    tyopoyta = os.path.join(kotikansio, "Desktop")
    
    # Suomenkielinen Windows saattaa käyttää nimeä "Työpöytä", varaudutaan siihen:
    if not os.path.exists(tyopoyta):
        tyopoyta = os.path.join(kotikansio, "Työpöytä")

    jarjestele_tyopoyta(tyopoyta)
    print("-"*40 + "\nJärjestely suoritettu!")
