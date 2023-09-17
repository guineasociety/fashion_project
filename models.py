from django.db import models

# Create your models here.


class Mesure(models.Model):
    SEXE = (("Femme", "Femme"),("Homme", "Homme"),)

    # Produit:
    date_creation = models.DateField("Date ", null=True, auto_now_add=True)
    code_client = models.CharField(max_length=200, null=False)
    picture = models.ImageField()
    sexe = models.CharField("Sexe", max_length=50, null=True, choices=SEXE)
    mesurer = models.BooleanField(default=False)

    # Client
    nom = models.CharField("Client", max_length=50, null=False)
    contact = models.CharField("Téléphone", max_length=50, null=False)


    # Finance:
    date_rdv = models.DateField("Date RDV", null=True)
    quantite = models.IntegerField(null=False)
    montant = models.IntegerField(null=False)
    avance = models.IntegerField(null=False)
    reste = models.IntegerField(null=False)
    etat = models.IntegerField(null=False)

    # Les dimensions :
    code = models.CharField("Code Mesure", max_length=50, null=True, unique=True)
    epaule = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    poitrine = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tourTaille = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bassin = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ceinture = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurTaille = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurHaut = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurPantalon = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurManche = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    cuisse = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cou = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    poignet = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    tourManche = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurRobe = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurJupe = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longueurSoutien = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.code


class Employe(models.Model):
    SEXE = (("Femme", "Femme"),
              ("Homme", "Homme"),)
    nom_employe = models.CharField("Prénom et Nom", max_length=50, null=True)
    matricule_employe = models.CharField("Matricule", max_length=50, null=True, unique=True)
    contact_employe = models.CharField("Téléphone", max_length=50, null=True)
    sexe_employe = models.CharField("Sexe", max_length=10, null=True, choices=SEXE)
    date_embauche = models.DateField("Date Embauche", null=True)
    poste_employe = models.CharField("Poste", max_length=50, null=True)
    competence_employe = models.CharField("Compétence", max_length=50, null=True)
    salaire_employe = models.CharField("Salaire", max_length=50, null=True)
    picture_employe = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return self.contact_employe


class Charge(models.Model):

    date_creation = models.DateField("Date Création", null=True, auto_now_add=True)
    charge = models.CharField(max_length=100, null=True)
    categorie = models.CharField("Service/Personne",max_length=100, null=True)

    montant_total = models.IntegerField("Montant total à payer", null=True)
    montant_paye = models.IntegerField("Montant Payé", null=True)
    montant_restant = models.IntegerField("Reste à payer", null=True)

    def __str__(self):
        return self.charge
