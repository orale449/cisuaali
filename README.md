# Automatic Desktop Organizer

## 🎯 Ohjelman tarkoitus
Tämän skriptin tarkoituksena on pitää tietokoneen työpöytä siistinä automaattisesti. Se käy läpi työpöydällä olevat irralliset tiedostot ja lajittelee ne automaattisesti omiin alikansioihinsa (esim. Kuvat, Dokumentit, Asennustiedostot) tiedostopäätteen perusteella. Skripti auttaa säästämään aikaa ja pitämään työtilan selkeänä.

## 💻 Järjestelmävaatimukset
* **Käyttöjärjestelmä:** Windows, macOS tai Linux.
* **Ajoaika:** Python 3.x asennettuna tietokoneelle.
* **Esiasennettavat kirjastot:** Skripti käyttää Pythonin sisäänrakennettuja standardikirjastoja (`os`, `shutil`, `sys`), joten erillisiä `pip install` -asennuksia ei tarvita.

## 🚀 Siirrettävyys (Portability)
Skripti on suunniteltu erittäin siirrettäväksi:
* Se tunnistaa automaattisesti nykyisen käyttäjän kotikansion ja työpöydän polun (`os.path.expanduser("~")`).
* Se huomioi sekä englanninkielisen (`Desktop`) että suomenkielisen (`Työpöytä`) kansion nimen.
* **Jos haluat ajaa skriptiä jossain muussa kansiossa** (esim. Lataukset-kansiossa), riittää että muutat `organizer.py`-tiedoston alaosasta `tyopoyta`-muuttujan osoittamaan haluttuun kansioon.

## ⚠️ Mahdolliset rajoitteet
* **Samanryhmäiset tiedostot, joilla on sama nimi:** Jos kohdekansiossa on jo samanniminen tiedosto, siirto saattaa epäonnistua tai vaatia lisätoimia (ohjelma heittää virheen eikä ylikirjoita dataa turvallisuussyistä).
* **Avoimet tiedostot:** Jos sinulla on dokumentti auki Wordissa samalla kun ajat skriptin, käyttöjärjestelmä voi lukita tiedoston, jolloin skripti ei pysty siirtämään sitä ennen kuin tiedosto suljetaan.
* Skripti ei osaa tällä hetkellä eritellä tiedostoja niiden sisällön tai luontipäivämäärän mukaan, vaan pelkästään tiedostopäätteen perusteella.

## 🛠️ Kehitysajatukset (Tulevaisuuden parannukset)
1. **Automaattinen nimeäminen duplikaateille:** Jos kohdekansiossa on jo `kuva.png`, skripti voisi nimetä uuden tiedoston muotoon `kuva_1.png` virheen sijaan.
2. **Ajastus (Cronjob / Task Scheduler):** Skriptin voisi asettaa pyörimään automaattisesti taustalla esimerkiksi joka ilta klo 20:00 tai aina tietokoneen käynnistyessä.
3. **Graafinen käyttöliittymä (GUI):** Yksinkertainen käyttöliittymä, jossa käyttäjä voi hiirellä klikkaamalla valita järjesteltävän kansion ja muokata sääntöjä ilman koodin avaamista.
