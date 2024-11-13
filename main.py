import re
from collections import Counter
from typing import List, Tuple, Dict



VOWELS = set("اوي")
CONSONANTS = set("بتثجحخدذرزسشصضطظعغفقكلمنه")
ARABIC_DIACRITICS = re.compile(r'[\u064B-\u0652]')


def load_quran_verses(filename: str) -> List[str]:
    """
    بارگذاری آیات سوره یوسف از فایل متنی قرآن.
    
    Parameters:
    filename (str): نام فایل متنی قرآن

    Returns:
    List[str]: لیست آیات سوره یوسف
    """
    with open(filename, 'r', encoding='utf-8') as file:
        verses = [verse.strip() for verse in file.readlines() if verse.startswith('12|')]
    return verses


def extract_diacritics(text: str) -> List[str]:
    """
    استخراج الگوی حرکات عربی از متن.
    
    Parameters:
    text (str): متن ورودی

    Returns:
    List[str]: لیست کدهای یونی‌کد حرکات عربی
    """
    return ARABIC_DIACRITICS.findall(text)


def count_vowels_and_consonants(text: str) -> Tuple[int, int]:
    """
    شمارش تعداد حروف صدادار و بی‌صدا در یک متن.
    
    Parameters:
    text (str): متن ورودی

    Returns:
    Tuple[int, int]: تعداد حروف صدادار و بی‌صدا
    """
    vowel_count = sum(1 for char in text if char in VOWELS)
    consonant_count = sum(1 for char in text if char in CONSONANTS)
    return vowel_count, consonant_count


def get_word_counts(verses: List[str]) -> List[int]:
    """
    محاسبه تعداد کلمات در هر آیه.
    
    Parameters:
    verses (List[str]): لیست آیات

    Returns:
    List[int]: لیست تعداد کلمات در هر آیه
    """
    return [len(verse.split('|')[2].split()) for verse in verses]


def find_similar_weight_verses_by_groups(verses: List[str]) -> Dict[str, List[str]]:
    """
    پیدا کردن آیات هم‌وزن براساس تعداد کلمات، حروف و الگوی حرکات.
    
    Parameters:
    verses (List[str]): لیست آیات

    Returns:
    Dict[str, List[str]]: دیکشنری شامل آیات گروه اکثریت و سایر گروه‌ها
    """
    word_counts = get_word_counts(verses)
    word_count_groups = Counter(word_counts)
    baseline_count = word_count_groups.most_common(1)[0][0]

    verse_groups: Dict[int, List[str]] = {}
    for verse in verses:
        verse_text = verse.split('|')[2]
        word_count = len(verse_text.split())
        if word_count not in verse_groups:
            verse_groups[word_count] = []
        verse_groups[word_count].append(verse)

    grouped_verses = {"majority": [], "other": {}}
    for count, group_verses in verse_groups.items():
        if len(group_verses) < 2:
            continue

        vowel_cons_counts = [count_vowels_and_consonants(v.split('|')[2]) for v in group_verses]
        diacritic_patterns = [extract_diacritics(v.split('|')[2]) for v in group_verses]
        valid_verses = []
        for i, verse in enumerate(group_verses):
            verse_text = verse.split('|')[2]
            verse_vowel_cons_count = count_vowels_and_consonants(verse_text)
            verse_diacritic_pattern = extract_diacritics(verse_text)

            if (
                verse_vowel_cons_count in vowel_cons_counts
                and verse_diacritic_pattern in diacritic_patterns
            ):
                valid_verses.append(verse)
        if count == baseline_count:
            grouped_verses["majority"].extend(valid_verses)
        else:
            grouped_verses["other"][count] = valid_verses
    return grouped_verses


if __name__ == "__main__":
    filename = 'quran.txt'
    output_filename = 'similar_weight_verses_yusuf.txt'
    surah_yusuf = load_quran_verses(filename)
    grouped_verses = find_similar_weight_verses_by_groups(surah_yusuf)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write("مجموعه آیات اکثریت:\n")
        for verse in grouped_verses["majority"]:
            output_file.write(verse + '\n')

        for count, verses in grouped_verses["other"].items():
            if len(verses) >= 2:
                output_file.write(f"\nمجموعه آیات با تعداد کلمات برابر {count}:\n")
                for verse in verses:
                    output_file.write(verse + '\n')