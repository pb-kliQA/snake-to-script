import sys
from PyQt5 import QtWidgets
from snake_to_script_gui import SnakeToScriptGui
import traceback

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = SnakeToScriptGui()
    main_window.show()
    return app.exec_()

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("An error occurred:", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)