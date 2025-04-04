from django.test import TestCase
from app.forms import NoteForm

class NoteFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'title': 'Test Note', 'content': 'Test content'}
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'title': '', 'content': 'Test content'}
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)