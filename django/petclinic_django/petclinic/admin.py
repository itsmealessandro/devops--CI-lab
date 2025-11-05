from django.contrib import admin
from .models import Vet, Specialty, VetSpecialty, Type, Owner, Pet, Visit, User, Role

admin.site.register([Vet, Specialty, VetSpecialty, Type, Owner, Pet, Visit, User, Role])
