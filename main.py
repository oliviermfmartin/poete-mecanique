import RPi.GPIO as GPIO
import time
import os
import random
import pyttsx3

# Initialisation de GPIO et Pyttsx3
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
engine = pyttsx3.init()

# Définir le dossier contenant les fichiers de poèmes
poem_folder = "./poemes"

# Définir les propriétés de la voix et de la langue
voices = engine.getProperty('voices')

# Sélectionner une voix parmi les voix disponibles, par exemple voices[0] est la première voix dans la liste
voice = voices[0]
engine.setProperty('voice', voice.id)

# Sélectionner une langue pour la voix, par exemple 'fr' pour le français
engine.setProperty('language', 'fr')

# Boucle indéfiniment
while True:
    # Attendre la détection de mouvement
    while GPIO.input(14) == 0:
        time.sleep(0.1)
    # Mouvement détecté, sélectionner un fichier de poème aléatoire et le lire
    print("Mouvement détecté, lecture du poème...")
    poem_files = os.listdir(poem_folder)
    poem_file = os.path.join(poem_folder, random.choice(poem_files))
    with open(poem_file, 'r') as f:
        poem_text = f.read().replace('\n', ' ')
    engine.say(poem_text)
    engine.runAndWait()

