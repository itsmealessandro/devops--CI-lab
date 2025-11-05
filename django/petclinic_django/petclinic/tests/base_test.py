# petclinic/tests/base_test.py
from rest_framework.test import APITestCase
from petclinic.models import Owner, Pet, Vet, Specialty, Visit, Type

class BaseTestCase(APITestCase):
    """
    Base class for CRUD tests.
    Provides helper methods to create model instances.
    """

    # --- Owner ---
    def create_owner(self, first_name="Mario", last_name="Rossi"):
        return Owner.objects.create(
            first_name=first_name,
            last_name=last_name,
            address="Via Roma 12",
            city="L'Aquila",
            telephone="3331234567"
        )

    # --- Type ---
    def create_type(self, name="Dog"):
        return Type.objects.create(name=name)

    # --- Pet ---
    def create_pet(self, name="Fido", owner=None, type=None):
        owner = owner or self.create_owner()
        type = type or self.create_type()
        return Pet.objects.create(
            name=name,
            birth_date="2020-05-01",
            owner=owner,
            type=type
        )

    # --- Vet ---
    def create_vet(self, first_name="Luigi", last_name="Verdi"):
        return Vet.objects.create(first_name=first_name, last_name=last_name)

    # --- Specialty ---
    def create_specialty(self, name="Surgery"):
        return Specialty.objects.create(name=name)

    # --- Visit ---
    def create_visit(self, pet=None, description="Regular checkup"):
        pet = pet or self.create_pet()
        return Visit.objects.create(
            pet=pet,
            visit_date="2024-01-01",
            description=description
        )
