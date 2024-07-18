import sys
import os
from pathlib import Path
import ast
import re
import pickle
import traceback
import readline as _ # To increase the capabilities of "input()"

dir_path = Path(sys.argv[1])
if os.listdir(dir_path):
    raise Exception("Use a clean directory with DUMPREPL, please")
(dir_path / "DUMPREPL_OCCUPIED").touch()

last_object_index = 0

while True: # RREPL
    # Read
    input_buffer = ""
    while True: # Reading the expr
        input_ = input("... " if input_buffer else ">>> ")
        if not input_:
            break
        if input_buffer:
            input_buffer += "\n"
        input_buffer += input_

    # Replace
    def replacer(match):
        num: str = match.group(1)
        with (dir_path / num).open("rb") as f:
            bytes_ = f.read()
        return '__import__("pickle").loads(' + repr(bytes_) + ')'
    input_buffer = re.sub(r"\\(\d+)", replacer, input_buffer)

    # Evaluate
    if isinstance(ast.parse(input_buffer).body[0], ast.Expr):
        try:
            result = eval(input_buffer)
        except Exception:
            traceback.print_exc()
            continue
        if result is not None:
            # Print
            print(result)
        try:
            bytes_ = pickle.dumps(result)
        except pickle.PicklingError:
            pass
        else:
            with (dir_path / str(last_object_index)).open("wb") as f:
                f.write(bytes_)
            print("\\" + str(last_object_index))
            last_object_index += 1
    else:
        try:
            exec(input_buffer)
        except Exception:
            traceback.print_exc()
            continue

    # Loop
