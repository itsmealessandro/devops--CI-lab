from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Vet

class VetTests(BaseTestCase):
    def test_create_vet(self):
        print("######################################")
        print("VET TESTING")
        print("-------------- create vet --------------")
        vet = self.create_vet()
        self.assertEqual(vet.first_name, "Luigi")
        self.assertEqual(vet.last_name, "Verdi")

    def test_read_vet(self):
        print("-------------- read vet --------------")
        vet = self.create_vet()
        read_vet = Vet.objects.get(id=vet.id)
        self.assertEqual(read_vet.first_name, vet.first_name)
        self.assertEqual(read_vet.last_name, vet.last_name)

    def test_update_vet(self):
        print("-------------- update vet --------------")
        FIRST_NAME = "Luigi_Updated"
        LAST_NAME = "Verdi_Updated"
        vet = self.create_vet()
        
        Vet.objects.filter(id=vet.id).update(
            first_name=FIRST_NAME,
            last_name=LAST_NAME
        )
        
        vet.refresh_from_db()
        self.assertEqual(vet.first_name, FIRST_NAME)
        self.assertEqual(vet.last_name, LAST_NAME)

    def test_delete_vet(self):
        print("-------------- delete vet --------------")
        vet = self.create_vet()
        Vet.objects.filter(id=vet.id).delete()
        
        with self.assertRaises(Vet.DoesNotExist):
            Vet.objects.get(id=vet.id)
