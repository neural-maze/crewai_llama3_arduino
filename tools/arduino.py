import re
import subprocess

from crewai_tools import BaseTool, tool


# class CompileAndUploadToArduinoTool(BaseTool):
#     name: str = "CompileAndUploadToArduinoTool"
#     description: str = "Compiles and Uploads an Arduino Sketch script to an Arduino"
#     ino_file_dir: str = "The directory that contains the ino file"
#     board_fqbn: str = "The board type, e.g. 'arduino:avr:uno'"
#     port: str = "The port where the Arduino is connected"
#
#     def __init__(self, ino_file_dir: str, board_fqbn: str = "arduino:avr:uno", port: str = "/dev/cu.usbmodem1201",
#                  **kwargs):
#         super().__init__(**kwargs)
#         self.ino_file_dir = ino_file_dir
#         self.board_fqbn = board_fqbn
#         self.port = port
#
#     def _fix_ino_file(self):
#         """
#         This is a helper method for fixing the output .ino file when Llama3 adds some unintended text
#         that invalidates the compilation.
#         """
#         with open(f"{self.ino_file_dir}/tmp.ino", "r") as f:
#             content = f.read()
#
#         pattern = r'```.*?\n(.*?)```'
#         match = re.search(pattern, content, re.DOTALL).group(1).strip()
#
#         with open(f"{self.ino_file_dir}/tmp.ino", "w") as f:
#             f.write(match)
#
#     def _run(self):
#         self._fix_ino_file()
#
#         try:
#             subprocess.check_call([
#                 "arduino-cli", "compile", "--fqbn", self.board_fqbn, self.ino_file_dir
#             ])
#             subprocess.check_call([
#                 "arduino-cli", "upload", "--port", self.port, "--fqbn", self.board_fqbn, self.ino_file_dir
#             ])
#         except subprocess.CalledProcessError:
#             print("Compilation failed ...")
#


# TODO: Improve this code and make it a class instead of this @tool
@tool("CompileAndUploadToArduinoTool")
def compile_and_upload_to_arduino_tool():
    """
    Compiles and uploads a Sketch script into an Arduino
    """
    ino_file_dir: str = "./tmp"
    board_fqbn: str = "arduino:avr:uno"
    port: str = "/dev/cu.usbmodem1201"

    with open(f"{ino_file_dir}/tmp.ino", "r") as f:
        content = f.read()

    pattern = r'```.*?\n(.*?)```'
    match = re.search(pattern, content, re.DOTALL).group(1).strip()

    with open(f"{ino_file_dir}/tmp.ino", "w") as f:
        f.write(match)
    try:
        subprocess.check_call([
            "arduino-cli", "compile", "--fqbn", board_fqbn, ino_file_dir
        ])
        subprocess.check_call([
            "arduino-cli", "upload", "--port", port, "--fqbn", board_fqbn, ino_file_dir
        ])
    except subprocess.CalledProcessError:
        print("Compilation failed ...")

    return "Compilation successful"
