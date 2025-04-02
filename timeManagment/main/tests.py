from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client


class IndexPageTest(TestCase):
    def test_index_page(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'hi')  # Проверка содержимого страницы
