from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Type

class TypeTests(BaseTestCase):
    def test_create_type(self):
        print("######################################")
        print("TYPE TESTING")
        print("-------------- create type --------------")
        pet_type = self.create_type()
        self.assertEqual(pet_type.name, "Dog")

    def test_read_type(self):
        print("-------------- read type --------------")
        pet_type = self.create_type()
        read_type = Type.objects.get(id=pet_type.id)
        self.assertEqual(read_type.name, pet_type.name)

    def test_update_type(self):
        print("-------------- update type --------------")
        NAME = "Cat"
        pet_type = self.create_type()
        
        Type.objects.filter(id=pet_type.id).update(name=NAME)
        
        pet_type.refresh_from_db()
        self.assertEqual(pet_type.name, NAME)

    def test_delete_type(self):
        print("-------------- delete type --------------")
        pet_type = self.create_type()
        Type.objects.filter(id=pet_type.id).delete()
        
        with self.assertRaises(Type.DoesNotExist):
            Type.objects.get(id=pet_type.id)
