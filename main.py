import json
import os
from utils import calculate_areas, get_text

FILENAME = "MyData.json"

def main():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Перевірка наявності всіх ключів
            a = float(data['a'])
            r = float(data['r'])
            lang = data.get('lang', 'uk')

            # Приклад 2: Вивід результатів
            s_area, c_area = calculate_areas(a, r)
            
            print(f"{get_text('lang_label', lang)}")
            print(f"{get_text('side_label', lang)} {a}")
            print(f"{get_text('radius_label', lang)} {r}\n")
            print(f"{get_text('sq_res', lang)} {s_area}")
            print(f"{get_text('circ_res', lang)} {c_area}\n")

            if s_area > c_area:
                print(get_text('sq_bigger', lang))
            elif c_area > s_area:
                print(get_text('circ_bigger', lang))
            else:
                print(get_text('equal', lang))

        except (json.JSONDecodeError, KeyError, ValueError):
            run_input_mode()
    else:
        run_input_mode()

def run_input_mode():
    # Приклад 1: Введення даних
    try:
        a = input("Введіть сторону квадрата a: ")
        r = input("Введіть радіус кола R: ")
        lang = input("Введіть мову інтерфейсу (uk/en): ").lower()

        data = {
            "a": float(a),
            "r": float(r),
            "lang": lang
        }

        with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Дані збережено в файл {FILENAME}")
    except ValueError:
        print("Помилка: введіть числові значення.")

if __name__ == "__main__":
    main()