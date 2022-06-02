from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestContactUs(TestCase):
    """A test class for testing contact us"""

    def test_contact_us_view(self):
        """Test the contact us view."""
        response = self.client.get(reverse('contact_us:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    def test_contact_us_form_success(self):
        response = self.client.post(reverse('contact_us:contact'), data={
                                    "subject": "Contact us", "from_email": "contact@example.com", "message": "Hello!"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Success")
