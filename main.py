# -*- coding: utf-8 -*-
import argparse
import subprocess
import platform


def traceroute(ip_address, progressive=False, output_file=None, input_file=None):
    # Si un fichier d'entrée est spécifié, on lit son contenu
    if input_file:
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"Contenu du fichier '{input_file}':\n{content}")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier '{input_file}': {e}")
            return

    # Détecte le système d'exploitation et utilise la commande appropriée
    if platform.system().lower() == "windows":
        cmd = ['tracert', ip_address]  # Commande tracert pour Windows
    else:
        cmd = ['traceroute', ip_address]  # Commande traceroute pour Linux/macOS

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        results = []
        for line in process.stdout:
            print(line.strip())  # Affiche chaque ligne de la sortie
            results.append(line.strip())  # Ajoute la ligne aux résultats

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
    parser.add_argument("-i", "--input-file", type=str, help="Fichier à lire avant d'exécuter traceroute.")

    args = parser.parse_args()

    # Exécution de la fonction traceroute avec les options fournies
    traceroute(args.ip_address, args.progressive, args.output_file, args.input_file)


if __name__ == "__main__":
    main()
