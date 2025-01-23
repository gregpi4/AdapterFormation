## install the package

create a virtualenv
```
python -m venv venv
```

install the requirements
```
pip install -r requirement.txt
```

Exercice 1 :

Vous souhaitez afficher des informations sur certains produits que les employés mangent. Pour cela, vous avez déjà réalisé une API sur le lien : 

Récupérez le code et suivez les étapes suivantes. Pour chaque étape, vous devez changer la version de l’api dans l’adapter (foodfacts/openfoodfact_adapter) :


0. exécutez le code en lançant la commande
```python
python main.py
```

1. V1 de l’api, L’architecte s’est rendue compte que l’API n’est pas isolé du reste du code, il vous demande de rectifier

2. V2 de l’api, les tests sautent, regardez pourquoi et rétablissez les

3. V3 de l’api, les tests sautent, regardez pourquoi et rétablissez-les

4. V4 de l’api, implémenter une nouvelle fonctionnalité, le calcul du fullness factor. Une méthode qui permet de le calculer est déjà proposé au sein du package dependency_sdk.formula. Le fullness factor devrait aussi être affiché lors de l’appel en ligne de commande.

5. V5 de l’api, l’api prend maintenant bien plus de temps qu’avant et échoue parfois. Modifiez votre code pour que vos appels réussissent 9 fois sur 10 tout en réduisant au maximum le temps passé à attendre

6. V6 de l’api, vos tests échouent régulièrement, faites quelque chose pour rétablir le service

7. Face au temps des tests qui a explosé, que proposez-vous ?

8. Vous apprenez qu’Openfoodfact subissait une attaque DDOS, ce qui explique la mauvaise disponibilité de l’application, que pensez de vos modifications ?

Exercice 2 :

Développez votre propre api !!
Utilisez le site web https://api.artic.edu/docs/#collections pour implémenter votre propre adapter qui récupère un lien vers l’image de l’oeuvre à partir de son nom. Le nom est supposé être correctement donné.
Attention, vous ne devez pas faire plus de 40 appels par minutes
