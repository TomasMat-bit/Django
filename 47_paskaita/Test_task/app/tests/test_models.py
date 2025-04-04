from django.test import TestCase
from app.models import Note

class NoteModelTest(TestCase):
    def test_str_method(self):
        note = Note.objects.create(title="Test Note", content="Test content")
        self.assertEqual(str(note), "Test Note")