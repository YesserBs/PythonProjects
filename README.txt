Une fois le dossier téléchargé vous devriez seulment installer la librairie 'pygame' pour que le code s'éxecute

description:
C'est une immitation du jeu Ludo
Le principe consiste a lancer un dé et a déplacer le pion selon le résultat obtenu, tout d'abbord
- Si le pion est en prison (la case initiale):
	vous devez avoir un 6 au lancé du dé pour sortir
- Si vous sortez vous etes a la case 1
- Si (le résultat du dé + votre position) ne dépasse pas 10 (le nbr de cases):
	vous avancez
On répete ce processus jusqu'a arriver a la dernière case, a l'arrivé plus le nombre de coups est bas plus vous étes chanceux
