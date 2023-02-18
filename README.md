# Le Poète Mécanique

Ce projet lit un poème aléatoire à voix haute lorsque le capteur de mouvement HC-SR501 détecte un mouvement. La voix synthétique utilisée pour lire le poème peut être configurée pour une voix et une langue spécifiques en utilisant la bibliothèque Pyttsx3.

## Prérequis

- Raspberry Pi (ou similaire) avec un système d'exploitation compatible
- Capteur de mouvement HC-SR501

## Installation

1. Connectez le capteur de mouvement HC-SR501 à votre Raspberry Pi. Assurez-vous que les broches sont correctement connectées selon le schéma de câblage.
2. Installez la bibliothèque RPi.GPIO à l'aide de la commande suivante : `sudo apt-get install rpi.gpio`
3. Installez la bibliothèque Pyttsx3 à l'aide de la commande suivante : `pip install pyttsx3`

## Utilisation

1. Placez le capteur de mouvement à l'endroit souhaité pour détecter les mouvements.
2. Exécutez le script Python en utilisant la commande suivante : `python main.py`
3. Lorsqu'un mouvement est détecté, un poème aléatoire sera lu à voix haute à l'aide de la voix synthétique configurée.

## Configuration

La voix synthétique utilisée pour lire le poème peut être configurée en modifiant les propriétés de la voix et de la langue dans le fichier `main.py`. Vous pouvez sélectionner une voix différente en choisissant un élément différent de la liste `voices`, et vous pouvez sélectionner une langue différente en définissant la propriété `language` sur un code de langue ISO 639-1 différent.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à les partager en créant une issue ou une pull request.

## Licence

Ce projet est sous licence GNU. Voir le fichier LICENSE pour plus de détails.
