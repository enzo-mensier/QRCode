import qrcode

def generer_qr_code(url,fill_color,background_color,nom_fichier="qrcode.png"):
  """Génère un QR code à partir d'une URL et l'enregistre dans un fichier.

  Args:
    url: L'URL à encoder dans le QR code.
    nom_fichier: Le nom du fichier dans lequel enregistrer le QR code.
    fill_color: La couleur du QR code.
    background_color: La couleur de fond du QR code.
  """

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(url)
  qr.make(fit=True)

  img = qr.make_image(fill_color = fill_color,back_color = background_color)
  img.save(nom_fichier)

if __name__ == "__main__":

    print(fr"""
    +---------------------------------------------------------+
    |    ____    ____     __________  ____  ______            |
    |   / __ \  / __ \   / ____/ __ \/ __ \/ ____/            |
    |  / / / / / /_/ /  / /   / / / / / / / __/               |
    | / /_/ / / _, _/  / /___/ /_/ / /_/ / /___               |
    | \___\_\/_/_|_|__ \____/\____/_____/_____/_______  ____  |
    |   / ____/ ____/ | / / ____/ __ \/   |/_  __/ __ \/ __ \ |
    |  / / __/ __/ /  |/ / __/ / /_/ / /| | / / / / / / /_/ / |
    | / /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /_/ / _, _/  |
    | \____/_____/_/ |_/_____/_/ |_/_/  |_/_/  \____/_/ |_|   |
    +---------------------------------------------------------+
    |                CHOIX DES COULEURS                       |
    | 1- White , Black , Red , Green , Blue , Yellow , Purple |
    |    Pink , Orange, Brown , Gray                          |
    |                                                         |
    +---------------------------------------------------------+
    |                                                         |
    |                GENERATEUR QR CODE                       |
    |                                                         |
    """)
    url = input("    |  ENTREZ VOTRE URL : ")
    background_color = str(input("    |  ENTREZ LA COULEUR DE FOND SOUHAITEZ :"))
    fill_color = str(input("    |  ENTREZ LA COULEUR DE QR CODE SOUHAITEZ :"))
    print()

    generer_qr_code(url,fill_color,background_color)
    print("    |  QR CODE GENERER AVEC SUCCES !")
    print("    |  LE QR CODE EST ENREGISTRER DANS LE FICHIER : qrcode.png|")
    print("    |                                                         |")

    print("    +---------------------------------------------------------+")
