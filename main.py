import sys
from PyQt5 import QtWidgets
from snake_to_script_gui import SnakeToScriptGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = SnakeToScriptGui()
    main_window.show()
    return app.exec_()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)