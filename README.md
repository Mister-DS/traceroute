# Script-Traceroute
## création d'un script qui reprendre le fonctionement de Traceroute

#Le script doit posséder deux options :

1. une option "-p"/"--progressive" qui, au lieu d'afficher la liste lorsque le traceroute est terminé (mode par défaut), permet de les afficher au fur et à mesure. (suggestion : utliser subprocess.Popen pour cette étape plutot que subprocess.run())
   
2. une option "-o"/"--output-file" qui prend un nom de fichiers en paramètre. Le résultat du traceroute sera enregistré dans ce fichier.
