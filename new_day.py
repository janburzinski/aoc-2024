"""
usage:
- py new_day.py
- py new_day.py --day=x
"""

import sys
from datetime import datetime
import os
from pathlib import Path
import shutil

current_day = 1  # the current day we want to create


def create_day():
    # create folder for the day
    os.makedirs(f"day_{current_day}", exist_ok=True)

    # copy temp file and rename it
    temp_file = Path("temp.py")
    destination_file_p1 = Path(f"day_{current_day}") / f"p1_day_{current_day}.py"
    destination_file_p2 = Path(f"day_{current_day}") / f"p2_day_{current_day}.py"

    # make sure the destination directory exist
    destination_file_p1.parent.mkdir(parents=True, exist_ok=True)
    destination_file_p2.parent.mkdir(parents=True, exist_ok=True)

    # copy and rename the file
    shutil.copy(temp_file, destination_file_p1)
    shutil.copy(temp_file, destination_file_p2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # fetch the current day since nothing has been specialized
        current_day = datetime.now().day
        print(f"No day has been specifically set using the --day argument, so the current day is {current_day}")
    else:
        current_day = sys.argv[1].split("=")[1]
        print(f"Creating day {current_day}...")

    current_day = current_day
    create_day()

    print(f"FINIIIISHED creating day {current_day}")
