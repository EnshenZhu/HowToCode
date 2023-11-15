import os
from googletrans import Translator


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


if __name__ == "__main__":
    file_path = "./dataset/introduction.txt"  # Change this to the path of your TXT file
    target_language = 'zh-CN'  # Change this to the desired language code

    input_text = read_file(file_path)
    input_text = input_text.replace("\n", " ")
    input_text = input_text.replace("‘‘", " ")
    input_text = input_text.replace("’’", " ")
    # input_text = input_text.replace("‘", " ")
    input_text = input_text.replace("’", " ")

    output_file_path = f"identify.txt"
    write_file(output_file_path, input_text)

    # for i in input_text:
    #     if type(i) == "NoneType":
    #         print(i)

    translated_text = ""

    parse_text = input_text[:5001]
    part = translate_text(parse_text, target_language)
    translated_text = translated_text + part

    parse_text = input_text[5001:10000]
    part = translate_text(parse_text, target_language)
    translated_text = translated_text + part

    parse_text = input_text[10000:]
    part = translate_text(parse_text, target_language)
    translated_text = translated_text + part

    output_file_path = f"translated_paper_{target_language}.txt"
    write_file(output_file_path, translated_text)

    # print(f"Original text:\n{input_text}\n")
    # print(f"Translated text ({target_language}):\n{translated_text}")
    # print(f"Translated paper saved to {output_file_path}")
