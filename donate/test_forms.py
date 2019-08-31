from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

# Create your tests here.

class TestPaymentForm(TestCase):

    def test_donation_amount_is_required_and_prompted(self):
        form = MakePaymentForm({'total': ''})
        self.assertFalse(form.is_valid())
    
class TestOrderForm(TestCase):
    def test_postcode_can_be_left_blank(self):
        form = OrderForm({'full_name': 'User', 'phone_number': '12345678', 'country': 'Ireland', 'town_or_city': 'Dublin', 'street_address1': 'Street', 'street_address2':'Street',
        'county': 'Dublin'})
        self.assertTrue(form.is_valid())