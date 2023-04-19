# ComptaTruck
TP Flask Application


La société "ComptaTruck" souhaite développer une nouvelle application permettant de saisir les évènements comptable.



Développez une application Flask permettant :

- D'afficher une page d'accueil donnant des conseil d'utilisation

- D'afficher une page Ajout Ligne permettant de saisir via un formulaire une nouvelle ligne de compta. 

Ce formulaire devra comporter les champs

Numero facture
Libellé facture
Nom fournisseur
Montant facture HT
Montant facture TTC (HT + 20,6%)
Date acquittement
Un champs d'upload de la facture au format PDF
- D'afficher une page listant toutes les entrées compta sous forme de table, ainsi qu'un lien dans chaque ligne permettant de télécharger la facture correspondante.



Votre application devra avoir un design y propre en utilisant un framework CSS. ( Bootstrap sera utilisé fréquemment dans ce cours, mais vous pouvez utiliser ce TP pour découvrir le framework de votre choix MaterialDesign, Foundation, SemanticUI...)

Les données de votre application seront gérées soit dans une base de données SQLite, soit dans un une variable de type dict initiée dès le démarrage du serveur.

