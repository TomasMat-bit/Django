from django.test import TestCase
from ..forms import NoteForm

class NoteFormTest(TestCase):
    def test_validform(self):
        form_data = {
            'title': 'Testas',
            'content': 'Turinys',
        }
        form = NoteForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.is_valid(), True)

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'content': '',
        }
        form = NoteForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

