from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Vet, Specialty, VetSpecialty, Type, Owner, Pet, Visit, User, Role

admin.site.register([Vet, Specialty, VetSpecialty, Type, Owner, Pet, Visit, User, Role])
