import googletrans

class Translator:
    def __init__(self):
        self.translator = googletrans.Translator()

    def translate(self, language, text):
        try:
            result = self.translator.translate(text, dest=language)
            if result:
                return result.text
            else:
                return None
        except Exception as e:
            raise e

def translate(language, text):
    translator = Translator()
    return translator.translate(language, text)