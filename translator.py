import os
import time
from googletrans import Translator
from xml.etree import ElementTree as ET

# 번역기 초기화
translator = Translator()

# 사용자에게 어떤 언어로 번역할지 물어봅니다.
print("어떤 언어로 번역하시겠습니까?")
print("1. 한국어")
print("2. 일본어")
print("3. 중국어")
choice = input("선택: ")

# 사용자의 선택에 따라 대상 언어를 설정합니다.
if choice == '1':
    target_lang = 'ko'
elif choice == '2':
    target_lang = 'ja'
elif choice == '3':
    target_lang = 'zh-cn'
else:
    print("잘못된 선택입니다.")
    exit()

# 현재 디렉토리의 모든 XML 파일을 찾습니다.
for filename in os.listdir('.'):
    if not filename.endswith('.xml'):
        continue

    # 백업 파일을 생성합니다.
    os.rename(filename, filename + '_bak.xml')

    # XML 파일을 파싱합니다.
    tree = ET.parse(filename + '_bak.xml')
    root = tree.getroot()

    # 모든 <content> 태그를 찾습니다.
    for content in root.iter('content'):
        original_text = content.text

        # 플레이스홀더로 치환합니다.
        placeholder_text = original_text.replace('<LSTag', 'PLACEHOLDER1').replace('</LSTag>', 'PLACEHOLDER2')

        # 번역을 시도합니다.
        for i in range(10):
            try:
                translated = translator.translate(placeholder_text, dest=target_lang)
                break
            except Exception as e:
                print(f"번역 실패: {e}")
                time.sleep(10)
        else:
            print("번역에 실패했습니다. 다시 시도해주세요.")
            exit()

        # 플레이스홀더를 원래의 태그로 복원합니다.
        translated_text = translated.text.replace('PLACEHOLDER1', '<LSTag').replace('PLACEHOLDER2', '</LSTag>')

        # 번역된 텍스트를 콘솔에 출력합니다.
        print("----------")
        print(f"{filename}")
        print(f"번역 전: {original_text}")
        print(f"번역 후: {translated_text}")
        print("----------")

        # 번역된 텍스트를 XML에 적용합니다.
        content.text = translated_text

    # 번역된 XML을 저장합니다.
    tree.write(filename, encoding='utf-8')
