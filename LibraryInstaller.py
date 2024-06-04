import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista delle librerie da installare
libraries = ["webdriver-manager","selenium"]


# Installa ogni libreria nella lista
for library in libraries:
    install(library)

print("Le librerie sono state installate con successo.")
