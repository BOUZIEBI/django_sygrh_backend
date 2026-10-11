from django.conf import settings
from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "roles"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class User(AbstractUser):

    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    # Dates
    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifier_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )
    
    # Relation avec Role
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
        db_column="role_uid"
    )

    class Meta:
        db_table = "users"
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username



class ValidationFiche(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
 
    class Meta:
        db_table = "validation_fiches"  
        ordering = ["libelle"]
 
    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)


class Statut(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
 
    class Meta:
        db_table = "statuts" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)


class Grade(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
 
    class Meta:
        db_table = "grades" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class SituationAdministrative(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    ) 
 
    class Meta:
        db_table = "situation_administratives" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Specialite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "specialites"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class SituationMatrimoniale(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "situation_matrimoniales" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Fonction(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "fonctions"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class TypeStructure(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "type_structures"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)


class Structure(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    libelle = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )

    abreviation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    slug = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    personne_contact = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone_personne_contact = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    anneecreation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    quartier = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    adressecomplete = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    siteweb = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    is_mode = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    typestructure = models.ForeignKey(
        TypeStructure,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="structures",
        db_column="type_structure_uid"
    )

    # ==========================================
    # RELATIONS UTILISATEURS
    # ==========================================

    cree_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="structures_crees",
        db_column="cree_par_uid"
    )

    modifie_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="structures_modifies",
        db_column="modifie_par_uid"
    )

    supprime_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="structures_supprimes",
        db_column="supprime_par_uid"
    )

    class Meta:
        db_table = "structures"
        verbose_name = "Structure"
        verbose_name_plural = "Structures"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle or ""
    


class TypeAgent(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "type_agents"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class TypeRecrutement(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "type_recrutements"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Conjoint(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    nom = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    prenoms = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    matricule_cnps = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    profession = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    is_mode = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "conjoints"
        verbose_name = "Conjoint"
        verbose_name_plural = "Conjoints"

    def __str__(self):
        return f"{self.nom or ''} {self.prenoms or ''}".strip()
    
    

class Genre(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "genres"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Conjoint(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "conjoints"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    

class Nationalite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "nationalites"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    
    
    
class NaturePieceidentite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "natures_piece_identite"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    

class Agent(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    nom = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    prenoms = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    matricule = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_naissance = models.DateTimeField(
        null=True,
        blank=True
    )

    lieu_naissance = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone_principal = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone_secondaire = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_professionnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_personnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    quartier = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    nom_jeune_fille = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    lieu_habitation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_recrutement = models.DateTimeField(
        null=True,
        blank=True
    )

    date_depart = models.DateTimeField(
        null=True,
        blank=True
    )

    nombre_enfant = models.IntegerField(
        default=0
    )

    nom_prenoms_pere = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    nom_prenoms_mere = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    numero_piece_identite = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    preinscrit_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    date_premiere_prise_service_dans_structure = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    date_premiere_prise_service_fonction_publique = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    # ==========================================
    # ETATS
    # ==========================================

    etat_handicap = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    is_deleted = models.BooleanField(
        default=False
    )

    est_preinscrit = models.BooleanField(
        default=False
    )

    # ==========================================
    # UTILISATEURS
    # ==========================================

    cree_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agent_cree_par",
        db_column="cree_par_uid"
    )

    modifie_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agent_modifie_par",
        db_column="modifie_par_uid"
    )

    supprime_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agent_supprime_par",
        db_column="supprime_par_uid"
    )

    # ==========================================
    # RELATIONS
    # ==========================================

    conjoint = models.ForeignKey(
        Conjoint,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="conjoint_uid"
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="genre_uid"
    )

    type_agent = models.ForeignKey(
        TypeAgent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="type_agent_uid"
    )

    nationalite = models.ForeignKey(
        Nationalite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="nationalite_uid"
    )

    type_recrutement = models.ForeignKey(
        TypeRecrutement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="type_recrutement_uid"
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="structure_uid"
    )

    fonction = models.ForeignKey(
        Fonction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="fonction_uid"
    )

    situation_matrimoniale = models.ForeignKey(
        SituationMatrimoniale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="situation_matrimoniale_uid"
    )

    specialite = models.ForeignKey(
        Specialite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="specialite_uid"
    )

    situation_administrative = models.ForeignKey(
        SituationAdministrative,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="situation_administrative_uid"
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="grade_uid"
    )

    statut = models.ForeignKey(
        Statut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="statut_uid"
    )

    validation_fiche = models.ForeignKey(
        ValidationFiche,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        db_column="validation_fiche_uid"
    )

    # ==========================================
    # CONFIGURATION
    # ==========================================

    class Meta:
        db_table = "agents"
        ordering = ["nom", "prenoms"]
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return f"{self.nom or ''} {self.prenoms or ''}".strip()
    
    

