from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Leggi il nome della canzone dal file Canzone.txt
with open('Canzone.txt', 'r') as file:
    song_name = file.readline().strip()

# Imposta il driver di Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Apri Google
    driver.get('https://www.google.com')

    # Aspetta qualche secondo per far caricare la pagina
    time.sleep(2)

    # Accetta i cookie (il selettore potrebbe dover essere aggiornato a seconda della lingua e dell'implementazione specifica della pagina)
    try:
        accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
        accept_cookies_button.click()
    except:
        print("Bottone dei cookie non trovato o non necessario su Google")

    # Aspetta qualche secondo per permettere l'interazione con i cookie
    time.sleep(2)

    # Cerca il nome della canzone con "lyrics" su Google
    search_query = song_name + " lyrics"
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Aspetta che i risultati della ricerca vengano caricati
    time.sleep(2)

    # Clicca sul primo risultato della ricerca
    first_result = driver.find_element(By.XPATH, '(//h3)[1]/../..')
    first_result.click()

    # Aspetta qualche secondo per permettere il caricamento della pagina
    time.sleep(3)

    # Estrai le lyrics dalla pagina (questa parte potrebbe variare a seconda della struttura del sito web)
    # Qui assumiamo che le lyrics siano contenute in un elemento <div> con una classe specifica
    try:
        lyrics_div = driver.find_element(By.XPATH, '//div[contains(@class, "Lyrics__Container")]')
        lyrics = lyrics_div.text
    except:
        # In caso non trovi l'elemento, possiamo provare un altro metodo
        lyrics_divs = driver.find_elements(By.XPATH, '//div[contains(@class, "lyric-text")]')
        lyrics = "\n".join([div.text for div in lyrics_divs])

    # Stampa e salva le lyrics in un file Lyrics.txt
    with open('Lyrics.txt', 'w') as file:
        file.write(lyrics)

    print(f"Le lyrics della canzone '{song_name}' sono state salvate nel file Lyrics.txt")

finally:
    # Chiudi il browser
    driver.quit()
