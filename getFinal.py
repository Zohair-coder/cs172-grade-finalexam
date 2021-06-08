import re
import os

def getFinal():
    files = os.listdir("./student_py")

    for file in files:
        py = re.findall(".*.py", file)
        if len(py) >= 1:
            return py[0] 