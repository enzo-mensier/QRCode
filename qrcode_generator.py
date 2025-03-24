import qrcode

def generer_qr_code(url, nom_fichier="qrcode.png"):
  """Génère un QR code à partir d'une URL et l'enregistre dans un fichier.

  Args:
    url: L'URL à encoder dans le QR code.
    nom_fichier: Le nom du fichier dans lequel enregistrer le QR code.
  """

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(url)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  img.save(nom_fichier)

if __name__ == "__main__":
  url = input("Entrez l'URL à encoder : ")
  generer_qr_code(url)
  print(f"QR code généré et enregistré dans qrcode.png")