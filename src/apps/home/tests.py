from django.test import TestCase
from .models import Bussiness

# Create your tests here.

class BussinessMethodTests(TestCase):
	def test_bussiness_name(self):
		bus=Bussiness(name='nametest')
		bus.save()
		self.assertEqual(bus.name,'nametest')

	def test_bussiness_get(self):
		bus=Bussiness(name='nametest')
		bus.save()
		bus2=Bussiness(name="")
		bus2=bus.get_bussiness()
		self.assertEquals(bus.name,bus2.name)
