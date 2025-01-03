# -*- coding: utf-8 -*-
import argparse
import subprocess
import platform
import re


def traceroute(ip_address, progressive=False, output_file=None):
    # Détecte le système d'exploitation et utilise la commande appropriée
    if platform.system().lower() == "windows":
        cmd = ['tracert', ip_address]  # pour Windows
    else:
        cmd = ['traceroute', ip_address]  # pour Linux/macOS

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        results = []
        compte = 0 #Initialise un compteur pour voir où on en est
        for line in process.stdout:
            # Extraction des adresses IP avec une expression régulière
            match = re.search(r"\b(?:\d{1,3}.){3}\d{1,3}\b", line)
            if match:
                ip = match.group(0)
                compte+=1
                print(f'{compte} : {ip}')  # Affiche uniquement l'adresse IP
                results.append(ip)

            if progressive:
                input("Appuyez sur Entrée pour continuer...")

        # Enregistrer les résultats dans un fichier si demandé
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(results))
                print(f"Résultats enregistrés dans '{output_file}'")

    except Exception as e:
        print(f"Erreur : {e}")


def main():
    # Configuration de l'interface en ligne de commande
    parser = argparse.ArgumentParser(description="Traceroute pour une adresse IP spécifiée.")
    parser.add_argument("ip_address", type=str, help="L'adresse IP ou le nom de domaine à tracer.")
    parser.add_argument("-p", "--progressive", action="store_true", help="Activer l'exécution progressive.")
    parser.add_argument("-o", "--output-file", type=str, help="Fichier dans lequel enregistrer les résultats.")

    args = parser.parse_args()

    # Exécution de la fonction traceroute avec les options fournies
    traceroute(args.ip_address, args.progressive, args.output_file)


if __name__ == "__main__":
    main()
