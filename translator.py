import os
import time
import xml.etree.ElementTree as ET
from googletrans import Translator

def select_language():
    languages = {"1": "ko", "2": "ja", "3": "zh-cn"}
    print("Select a language for translation:")
    print("1: Korean (한국어)")
    print("2: Japanese (日本語)")
    print("3: Chinese (中文)")
    choice = input("Enter your choice (1/2/3): ")
    return languages.get(choice, "ko")

def backup_file(file_path):
    backup_path = f"{file_path[:-4]}_bak.xml"
    with open(file_path, 'r', encoding='utf-8') as original:
        with open(backup_path, 'w', encoding='utf-8') as backup:
            backup.write(original.read())
    return backup_path

def translate_text(translator, text, dest_language):
    try_count = 0
    while try_count < 10:
        try:
            return translator.translate(text, dest=dest_language).text
        except Exception as e:
            print(f"Translation failed ({try_count + 1}/10): {e}, retrying in 10 seconds...")
            time.sleep(10)
            try_count += 1
    return text

def translate_file(file_path, language):
    tree = ET.parse(file_path)
    root = tree.getroot()
    translator = Translator()

    for i, content in enumerate(root.findall(".//content"), start=1):
        print(f"Translating file '{file_path}', content tag #{i}")
        original_text = content.text or ""
        # Replace <LSTag> tags with placeholders
        parts = original_text.split("&lt;LSTag")
        for j in range(1, len(parts)):
            sub_parts = parts[j].split("&gt;", 1)
            if len(sub_parts) > 1:
                parts[j] = "PLACEHOLDER" + sub_parts[0] + "PLACEHOLDER&gt;" + sub_parts[1]
        text_to_translate = "&lt;LSTag".join(parts)
        # Translate text
        translated_text = translate_text(translator, text_to_translate, language)
        # Restore <LSTag> tags
        parts = translated_text.split("PLACEHOLDER")
        for j in range(1, len(parts), 2):
            parts[j] = "&lt;LSTag" + parts[j] + "&gt;"
        content.text = "".join(parts)

    tree.write(file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    selected_language = select_language()
    for file in os.listdir('.'):
        if file.endswith('.xml'):
            print(f"Processing file: {file}")
            backup_path = backup_file(file)
            translate_file(file, selected_language)
            print(f"Finished processing {file}, backup created at {backup_path}")
