from cli import display, clear_screen


def main():
    try:
        display()
    except KeyboardInterrupt:
        print("\n\n⚠️Interrupción detectada (Ctrl + C).")
        exit_option = input(" ¿Desear salir? (y/n): ").lower() == "y"
        if exit_option:
            clear_screen()
            print("Exiting...")
        else:
            main()


if __name__ == "__main__":
    main()
