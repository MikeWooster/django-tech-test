from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# class TestAdmin(TestCase):
#     def test_is_enabled(self):
#         client = Client()
#         response = client.post("/admin/", follow=True)
#         self.assertEqual(response.status_code, 200,
#                          "Bad status code - Admin page has not been enabled")


class TestBorrowingView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_is_enabled(self):
        response = self.client.get("/borrowing/")
        self.assertEqual(response.status_code, 200,
                         "Bad status code - Borrowing page unreachable")