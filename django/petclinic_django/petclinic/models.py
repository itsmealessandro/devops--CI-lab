#INFO: this file is where the models strucutre are defined and then they will be migrated to DB
from django.db import models

class Vet(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=["last_name"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Specialty(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class VetSpecialty(models.Model):
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("vet", "specialty")


class Type(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    telephone = models.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=["last_name"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class Visit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    visit_date = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pet.name} - {self.visit_date}"


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=60)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    class Meta:
        unique_together = ("role", "username")

    def __str__(self):
        return f"{self.username} - {self.role}"
