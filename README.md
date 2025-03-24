# Générateur de QR Codes Python

Ce script Python permet de générer des QR codes à partir d'URLs saisies par l'utilisateur.

## Prérequis

* Python 3.x installé sur votre système.
* Les bibliothèques Python `qrcode` et `Pillow` installées. Vous pouvez les installer avec les commandes suivantes :

    ```bash
    pip install qrcode
    pip install Pillow
    ```

## Utilisation

1.  **Téléchargez le script :**
    * Téléchargez le fichier `qrcode_generator.py` dans le répertoire de votre choix.
2.  **Exécutez le script :**
    * Ouvrez votre terminal et naviguez jusqu'au répertoire où vous avez enregistré le script.
    * Exécutez la commande suivante :

        ```bash
        python qrcode_generator.py
        ```

3.  **Saisissez l'URL :**
    * Le script vous demandera de saisir l'URL que vous souhaitez encoder dans le QR code.
    * Saisissez l'URL et appuyez sur Entrée.

4.  **Localisez le QR code :**
    * Le QR code sera généré et enregistré sous le nom `qrcode.png` dans le même répertoire que le script.
    * Vous pouvez ouvrir ce fichier avec n'importe quel visualiseur d'images.

## Personnalisation

Vous pouvez personnaliser l'apparence du QR code en modifiant les paramètres suivants dans le script :

* `nom_fichier` : Le nom du fichier de sortie (par défaut : `qrcode.png`).
* `fill_color` : La couleur des modules du QR code (par défaut : `black`).
* `back_color` : La couleur de fond du QR code (par défaut : `white`).
* `box_size` : La taille des modules du QR code (par défaut : 10).
* `border` : La taille de la bordure blanche autour du QR code (par défaut : 4).

## Exemple

Pour générer un QR code pour l'URL `https://www.example.com`, exécutez le script et saisissez l'URL lorsque vous y êtes invité. Le QR code sera enregistré dans le fichier `qrcode.png`.