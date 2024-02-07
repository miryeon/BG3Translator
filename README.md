# Baldur's Gate 3 Translator

## 소개
이 프로젝트는 "발더스 게이트 3" 게임의 텍스트를 다양한 언어로 번역하는 Python 스크립트입니다. `googletrans` 라이브러리를 사용하여, 모드의 대사, 설명, UI 텍스트 등을 사용자가 원하는 언어로 번역합니다.

## 기능
- 지원 언어: 한국어, 일본어, 중국어 (추가 언어 지원 가능)
- `googletrans`를 이용한 실시간 번역
- XML 파일 형식의 게임 텍스트 자동 번역
- 게임에 이용되는 특수 태그 번역 제외

## 사용 방법
1. 스크립트와 번역할 xml을 같은 경로에 둡니다.
2. 스크립트를 실행합니다.
3. 번역할 언어를 선택합니다 (예: `1` - 한국어, `2` - 일본어, `3` - 중국어).
4. 스크립트가 현재 디렉토리에있는 모든 xml을 번역합니다.

## 필요 조건
- Python 3 (설치 과정에서 PATH 설정)
- `googletrans` 라이브러리 (`pip install googletrans==3.1.0a0`로 설치)

## `googletrans` 사용법
이 스크립트는 `googletrans` 라이브러리를 사용하여 텍스트를 번역합니다. 이 라이브러리는 Google의 무료 번역 API를 활용하여 다양한 언어 간의 번역을 지원합니다. 

## 참고 사항
- 이 스크립트는 비공식적인 도구이며 "발더스 게이트 3"의 모드 번역을 담당하고있습니다.
- 번역 품질은 `googletrans` API에 따라 달라질 수 있습니다.
