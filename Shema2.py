import RPi.GPIO as GPIO   # Importe la bibliothèque pour contrôler les GPIO du Raspberry Pi
import time              # Importe la bibliothèque pour gérer le temps (utile pour ajouter des pauses si nécessaire)

GPIO.setmode(GPIO.BCM)   # Définit la numérotation des broches selon le schéma BCM (GPIOxx)

# Définition des numéros de broches utilisés
PIN_BUTTON = 12          # Broche GPIO 12 utilisée pour le bouton
RED_LED = 14             # Broche GPIO 14 utilisée pour la LED rouge
GREEN_LED = 15           # Broche GPIO 15 utilisée pour la LED verte

# Configuration des broches :
GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
# Configure la broche du bouton en entrée avec une résistance de tirage interne vers la masse (pull-down)
# Cela évite que l'entrée soit flottante (indéterminée)

GPIO.setup(GREEN_LED, GPIO.OUT)  # Configure la broche de la LED verte en sortie
GPIO.setup(RED_LED, GPIO.OUT)    # Configure la broche de la LED rouge en sortie

try:
    while True:                      # Boucle infinie : exécute en continu le code à l’intérieur
        button = GPIO.input(PIN_BUTTON)  # Lit l’état du bouton à chaque boucle (mise à jour en continu)
        
        if button == GPIO.HIGH:      # Si l’état du bouton est à HIGH (bouton appuyé)
            GPIO.output(GREEN_LED, GPIO.HIGH)  # Allume la LED verte (envoie un signal électrique)
            GPIO.output(RED_LED, GPIO.LOW)     # Éteint la LED rouge
        else:                        # Sinon (bouton non appuyé)
            GPIO.output(GREEN_LED, GPIO.LOW)   # Éteint la LED verte
            GPIO.output(RED_LED, GPIO.HIGH)    # Allume la LED rouge

except KeyboardInterrupt:
    # Permet de quitter proprement avec Ctrl+C
    print("\nProgramme interrompu par l’utilisateur.")

finally:
    GPIO.cleanup()   # Nettoie les configurations des GPIO (remet les broches dans leur état initial)
    print("GPIO nettoyés correctement.")
