# Le Poète Mécanique

Ce projet lit un poème aléatoire à voix haute lorsque le capteur de mouvement HC-SR501 détecte un mouvement. La voix synthétique utilisée pour lire le poème est fournie par la bibliothèque gTTS, qui utilise l'API de synthèse vocale de Google pour générer de la parole à partir de texte.

## Prérequis

- Raspberry Pi (ou similaire) avec un système d'exploitation compatible
- Capteur de mouvement HC-SR501

## Installation

1. Connectez le capteur de mouvement HC-SR501 à votre Raspberry Pi. Assurez-vous que les broches sont correctement connectées selon le schéma de câblage.
2. Installez la bibliothèque RPi.GPIO à l'aide de la commande suivante : `sudo apt-get install rpi.gpio`
3. Installez la bibliothèque gTTS et la bibliothèque playsound à l'aide de la commande suivante : `pip install gtts playsound`

## Utilisation

1. Placez le capteur de mouvement à l'endroit souhaité pour détecter les mouvements.
2. Exécutez le script Python en utilisant la commande suivante : `python main.py`
3. Lorsqu'un mouvement est détecté, un poème aléatoire sera lu à voix haute à l'aide de la voix synthétique configurée.

## Configuration

La voix synthétique utilisée pour lire le poème peut être configurée en définissant la propriété `language` sur un code de langue ISO 639-1 différent dans le fichier `main.py`. Le code 'fr' est utilisé par défaut pour le français.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à les partager en créant une issue ou une pull request.

## Licence

Ce projet est sous licence GNU. Voir le fichier LICENSE pour plus de détails.
