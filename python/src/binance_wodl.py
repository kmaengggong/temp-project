import re

def find_words(text, length=None, include_chars=None, exclude_chars=None):
    # 텍스트를 소문자로 변환
    text = text.lower()
    
    # 포함/제외 문자 리스트도 소문자로 변환
    include_chars = [char.lower() for char in include_chars] if include_chars else []
    exclude_chars = [char.lower() for char in exclude_chars] if exclude_chars else []

    # 텍스트를 단어 단위로 분리
    words = re.findall(r'\b\w+\b', text)

    # 필터링 조건 적용
    filtered_words = []
    for word in words:
        if length is not None and len(word) != length:
            continue
        if include_chars and not all(char in word for char in include_chars):
            continue
        if exclude_chars and any(char in word for char in exclude_chars):
            continue
        filtered_words.append(word)
    
    return filtered_words

# 예제 사용
text = '''

'''

length = 8
include_chars = ['e', 'a', 'i', 'g']
exclude_chars = ['r', 't', 'u', 'o', 'p', 's', 'd', 'l', 'c', 'm', 'n']

result = find_words(text, length, include_chars, exclude_chars)
print("조건에 맞는 단어:", result)
