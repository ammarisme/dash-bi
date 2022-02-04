import unittest

from dash_app.base.urls import Url, display_page


class TestUrls(unittest.TestCase):
    def setUp(self):
        home_page_layout = 'home_page'
        dashboard_layout = 'dashboard'
        self.urlpatterns = [
            Url('/', home_page_layout),
            Url('/dashboard', dashboard_layout)
        ]

    def test_return_correct_layout(self):
        dash = display_page('/dashboard', self.urlpatterns)
        home = display_page('/', self.urlpatterns)
        error = display_page('/no-page', self.urlpatterns)
        self.assertEqual(dash, 'dashboard')
        self.assertEqual(home, 'home_page')
        self.assertEqual(error, '404')
