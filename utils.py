import math

def calculate_areas(a, r):
    """Обчислює площу квадрата та кола."""
    square_area = a ** 2
    circle_area = math.pi * (r ** 2)
    return round(square_area, 2), round(circle_area, 2)

def get_text(key, lang="uk"):
    """Функція для перекладу інтерфейсу."""
    translations = {
        "uk": {
            "lang_label": "Мова: Українська",
            "side_label": "Сторона квадрата a:",
            "radius_label": "Радіус кола R:",
            "sq_res": "Площа квадрата:",
            "circ_res": "Площа кола:",
            "sq_bigger": "Площа квадрата більше.",
            "circ_bigger": "Площа кола більше.",
            "equal": "Площі рівні.",
            "save_msg": "Дані збережено в файл MyData.json"
        },
        "en": {
            "lang_label": "Language: English",
            "side_label": "Square side a:",
            "radius_label": "Circle radius R:",
            "sq_res": "Square area:",
            "circ_res": "Circle area:",
            "sq_bigger": "Square area is larger.",
            "circ_bigger": "Circle area is larger.",
            "equal": "Areas are equal.",
            "save_msg": "Data saved to MyData.json"
        }
    }
    # Якщо мова не uk/en, використовуємо uk за замовчуванням
    res_lang = lang if lang in translations else "uk"
    return translations[res_lang].get(key, "")