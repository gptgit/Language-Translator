import translator

def main():
    print("Language Translator")
    print("------------------")

    language = input("Enter the language to translate (e.g. en, es, fr): ")
    text = input("Enter the text to translate: ")

    try:
        translated_text = translator.translate(language, text)
        print(f"Translated text: {translated_text}")
    except AttributeError as e:
        print(f"Error: Unable to translate text. Please check your internet connection and try again.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()