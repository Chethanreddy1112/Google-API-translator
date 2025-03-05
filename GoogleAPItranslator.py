import googletrans
from googletrans import Translator

translator = Translator()
input_text = input("Enter Your Translation Text: ")
input_language = input("Enter Translation Language or Code: ")

try:
    translation = translator.translate(input_text, dest=input_language)
    print('Translated Text:', translation.text)
except Exception as e:
    print("Error:", e)
