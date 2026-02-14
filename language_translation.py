from deep_translator import GoogleTranslator

def translate_text():
    print("=== Language Translation Tool ===")

    text = input("Enter text to translate: ")
    source_lang = input("Enter source language code (e.g., en, hi, fr): ")
    target_lang = input("Enter target language code (e.g., en, hi, fr): ")

    try:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        print("\nTranslated Text:")
        print(translated)

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    translate_text()
