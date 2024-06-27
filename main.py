from pynput import keyboard
from colorama import init, Fore, Style

# Инициализируем colorama
init()

# Выводим сообщение в консоль красным цветом
print(Fore.RED + "JDFLAG" + Style.RESET_ALL)

# Создаем словарь замен для заглавных и строчных букв
replacement_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO', 'Ж': 'Z', 'З': 'Z',
    'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH',
    'Ъ': 'Y', 'Ы': 'I', 'Ь': 'Y', 'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
    'а': 'A', 'б': 'B', 'в': 'V', 'г': 'G', 'д': 'D', 'е': 'E', 'ё': 'YO', 'ж': 'Z', 'з': 'Z',
    'и': 'I', 'й': 'Y', 'к': 'K', 'л': 'L', 'м': 'M', 'н': 'N', 'о': 'O', 'п': 'P', 'р': 'R',
    'с': 'S', 'т': 'T', 'у': 'U', 'ф': 'F', 'х': 'H', 'ц': 'TS', 'ч': 'CH', 'ш': 'SH', 'щ': 'SCH',
    'ъ': 'Y', 'ы': 'I', 'ь': 'Y', 'э': 'E', 'ю': 'YU', 'я': 'YA'
}

# Создаем объект контроллера клавиатуры
controller = keyboard.Controller()

# Флаг для паузы
paused = False

# Функция для перехвата нажатий клавиш
def on_press(key):
    global paused
    if not paused:
        try:
            if hasattr(key, 'char') and key.char:
                char = key.char
                if char in replacement_dict:
                    new_char = replacement_dict[char]
                    # Удаляем оригинальный символ
                    controller.press(keyboard.Key.backspace)
                    controller.release(keyboard.Key.backspace)
                    # Вставляем замененный символ
                    controller.type(new_char)
        except AttributeError:
            pass

# Функция для перехвата отпускания клавиш
def on_release(key):
    global paused
    # Завершаем программу при нажатии F7
    if key == keyboard.Key.f7:
        return False
    # Ставим на паузу/снимаем с паузы при нажатии F6
    elif key == keyboard.Key.f6:
        paused = not paused
        if paused:
            print(Fore.YELLOW + "Пауза" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Возобновлено" + Style.RESET_ALL)

# Запускаем перехватчик клавиш
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
