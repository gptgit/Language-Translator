import unittest
from language_translator.translator import Translator

class TestTranslator(unittest.TestCase):

    def test_translate(self):
        translator = Translator()
        self.assertEqual(translator.translate('en', 'Hello'), 'Bonjour')
        self.assertEqual(translator.translate('es', 'Hello'), 'Hola')
        self.assertEqual(translator.translate('fr', 'Hello'), 'Bonjour')

    def test_translate_invalid_language(self):
        translator = Translator()
        with self.assertRaises(Exception):
            translator.translate('invalid', 'Hello')

    def test_translate_invalid_text(self):
        translator = Translator()
        with self.assertRaises(Exception):
            translator.translate('en', '')

if __name__ == '__main__':
    unittest.main()