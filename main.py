import RPi.GPIO as GPIO
import time
import os
import random
from gtts import gTTS
from playsound import playsound

# Initialisation de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

# Définir le dossier contenant les fichiers de poèmes
poem_folder = "./poemes"
audio_folder = "./audio"

# Sélectionner une langue pour la voix, par exemple 'fr' pour le français
language = 'fr'

# Liste des poèmes
poem_files = os.listdir(poem_folder)

# Créer le dossier de stockage pour les fichiers audio si nécessaire
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Boucle indéfiniment
while True:
    # Attendre la détection de mouvement
    while GPIO.input(4) == 0:
        time.sleep(0.5)
    
    # Mouvement détecté, sélectionner un fichier de poème aléatoire et le lire
    poem_file = os.path.join(poem_folder, random.choice(poem_files))
    audio_file = os.path.join(audio_folder, os.path.splitext(os.path.basename(poem_file))[0] + ".mp3")
   
    if os.path.exists(audio_file):
        print(f'Fichier audio trouvé: {audio_file}')

    else:
        print(f'Conversion du texte en audio pour le poème: {poem_file}')
        with open(poem_file, 'r') as f:
            poem_text = f.read().replace('\n', ' ')

        tts = gTTS(text=poem_text, lang=language)
        tts.save(audio_file)
        print(f'Fichier audio enregistré: {audio_file}')

    playsound(audio_file)
