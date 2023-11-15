import os
from translate import Translator

def translate_text(text, target_language='en'):
    translator= Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

# Example usage
journal_paper = """
Your journal paper text goes here.
"""

target_language = 'fr'  # Change it to your desired language code (e.g., 'es' for Spanish, 'de' for German)

translated_paper = translate_text(journal_paper, target_language)
print(translated_paper)