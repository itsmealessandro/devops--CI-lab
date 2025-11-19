from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Specialty

class SpecialtyTests(BaseTestCase):
    def test_create_specialty(self):
        print("######################################")
        print("SPECIALTY TESTING")
        print("-------------- create specialty --------------")
        specialty = self.create_specialty()
        self.assertEqual(specialty.name, "Surgery")

    def test_read_specialty(self):
        print("-------------- read specialty --------------")
        specialty = self.create_specialty()
        read_specialty = Specialty.objects.get(id=specialty.id)
        self.assertEqual(read_specialty.name, specialty.name)

    def test_update_specialty(self):
        print("-------------- update specialty --------------")
        NAME = "Cardiology"
        specialty = self.create_specialty()
        
        Specialty.objects.filter(id=specialty.id).update(name=NAME)
        
        specialty.refresh_from_db()
        self.assertEqual(specialty.name, NAME)

    def test_delete_specialty(self):
        print("-------------- delete specialty --------------")
        specialty = self.create_specialty()
        Specialty.objects.filter(id=specialty.id).delete()
        
        with self.assertRaises(Specialty.DoesNotExist):
            Specialty.objects.get(id=specialty.id)
