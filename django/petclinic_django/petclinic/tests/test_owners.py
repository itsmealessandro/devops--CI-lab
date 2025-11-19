from petclinic.tests.base_test import BaseTestCase
from petclinic.models import Owner
""" CRUD testing for owner """
""" test functionts runs in an lexicographic order"""
class OwnerTests(BaseTestCase):

    def test_create_owner(self):

        print("######################################")
        print("OWNER TESTING")

        print("-------------- create owner --------------")
        owner = self.create_owner()
        self.assertEqual(owner.id, 1) # id starts from 1 in djangoDB


    def test_read_owner(self):
        print("-------------- read owner --------------")




    def test_update_owner(self):
        print("-------------- update owner --------------")
        FIRST_NAME = "MARIO_UPDATED"
        LAST_NAME = "ROSSI_UPDATED"
        ADDRESS = "ADDRESS_UPDATED"
        CITY = "CITY_UPDATED"
        TELEPHONE = "TELEPHONE_UPDATED"
        owner = self.create_owner()
        print("old owner:")
        print(owner)
        querySet = Owner.objects.filter(id=owner.id)
        querySet.update(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            address=ADDRESS,
            city=CITY,
            telephone=TELEPHONE # no check for number sequence 
        )

        # print("owner before refresh_from_db")
        # print(owner)

        # Refresh instance from DB to get updated values
        owner.refresh_from_db()

        print("owner after refresh_from_db")
        print(owner)
        self.assertEqual(owner.first_name, FIRST_NAME)
        self.assertEqual(owner.last_name, LAST_NAME)
        self.assertEqual(owner.address, ADDRESS)
        self.assertEqual(owner.city, CITY)
        self.assertEqual(owner.telephone, TELEPHONE)


    def test_delete_owner(self):
        print("-------------- delete owner --------------")
        owner= self.create_owner();
        querySet = Owner.objects.filter(id=owner.id)
        querySet.delete()

        with self.assertRaises(Owner.DoesNotExist):
            Owner.objects.get(id=owner.id)
