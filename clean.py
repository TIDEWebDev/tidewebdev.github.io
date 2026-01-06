#!/bin/env python3

import os
from pathlib import Path

WEBSITE_ROOT = Path("docs")
WEBSITE_GENERATED = Path("generated.txt")

if os.path.isfile(WEBSITE_GENERATED):
    with open(WEBSITE_GENERATED) as generated:
        for line in generated:
            file_name = line.rstrip()
            file_name = Path(WEBSITE_ROOT) / file_name

            if os.path.isfile(file_name):
                os.remove(file_name)
            else:
                print(
                    f"Cannot delete '{file_name}', listed "
                    f"in '{WEBSITE_GENERATED}'"
                    )

    os.remove(WEBSITE_GENERATED)
