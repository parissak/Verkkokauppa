# Asennusohje

## Paikallinen asennus

* Ladataan koneelle ohjelma github:in kautta zippinä ja puretaan se haluttuun paikkaan.
* Luodaan hakemiston sisälle Python-virtuaaliympäristö komennolla `python3 -m venv venv`.
* Otetaan virtuaaliympäristö käyttöön komennolla `source venv/bin/activate`.
* Otetaan Flask-kirjaston käyttöön komennolla `pip install Flask`.
* Asennetaan projektissa jo olemassa olevat riippuvuudet komennolla `pip install -r requirements.txt`. 
* Palvelinohjelmisto käynnistetään komennolla `python3 run.py`. Nyt palvelin on paikallisesti tavoitettavissa osoitteessa `http://localhost:5000`.
* Palvelin voidaan sammuttaa komentorivin kautta painamalla `CTRL+C`.  

## Asennus Herokuun
* Ladataan koneelle ohjelma github:in kautta zippinä ja puretaan se haluttuun paikkaan.
* Herokun käyttöön tarvitaan Herokun käyttäjätunnus sekä Herokun työvälineet komentoriville (eli Heroku CLI). 
* Siirrytään kansioon, mihin projekti on purettu ja luodaan sovellukselle paikka Herokuun komennolla `heroku create haluttunimi`, 
missä jälkimmäinen teksti on projektin haluttu nimi. 
* Lisätään paikalliseen versionhallintaan tieto Herokusta komennolla `git remote add heroku https://git.heroku.com/haluttunimi.git`.
* Lähetetään projekti Herokuun seuraavilla komennoilla `git add .`, `git commit -m "Initial commit"`, `git push heroku master`.
* Nyt sovellus on tarkasteltavana Herokun kautta. Sovelluksen osoite on selvitettävissä edellisten komentojen jälkeisestä 
tulosteesta tai Herokun tilin kautta.
