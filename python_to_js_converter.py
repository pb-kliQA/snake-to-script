import os
import sys
import tempfile
import subprocess


def python_to_javascript(python_code):
    """
    Convert Python code to JavaScript using Transcrypt.

    :param python_code: String containing Python code
    :return: String containing converted JavaScript code, or error message
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create a temporary Python file
        py_file = os.path.join(tmpdirname, "temp.py")
        with open(py_file, "w") as f:
            f.write(python_code)

        # Run Transcrypt on the temporary file
        try:
            result = subprocess.run(["transcrypt", "-b", "-n", py_file],
                                    cwd=tmpdirname,
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

            # Check if Transcrypt output mentions any errors
            if "Error" in result.stderr:
                return f"// Transcrypt Error:\n{result.stderr}"

            # Find the generated JavaScript file
            target_dir = os.path.join(tmpdirname, "__target__")
            js_file = os.path.join(target_dir, "temp.js")

            if os.path.exists(js_file):
                with open(js_file, "r") as f:
                    javascript_code = f.read()
                return javascript_code
            else:
                # If the expected file doesn't exist, try to find any .js file in the directory
                js_files = [f for f in os.listdir(target_dir) if f.endswith('.js')]
                if js_files:
                    with open(os.path.join(target_dir, js_files[0]), "r") as f:
                        javascript_code = f.read()
                    return javascript_code
                else:
                    return f"// Error: Transcrypt did not generate the expected JavaScript file.\n// Transcrypt output:\n{result.stdout}\n{result.stderr}"

        except subprocess.CalledProcessError as e:
            return f"// Error: Transcrypt failed to convert the code\n// {e.stderr}"
        except FileNotFoundError:
            return "// Error: Transcrypt is not installed or not in the system PATH.\n// Please install Transcrypt using: pip install transcrypt"
        except Exception as e:
            return f"// Error: Failed to convert\n// {str(e)}\n// {sys.exc_info()[0].__name__}: {sys.exc_info()[1]}"