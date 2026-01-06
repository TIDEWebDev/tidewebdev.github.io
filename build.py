#!/bin/env python3

import os
import glob
import markdown
from pathlib import Path

CONTENT_ROOT = Path("text")
TEMPLATE_ROOT = Path("src")

WEBSITE_ROOT = Path("docs")
WEBSITE_GENERATED = Path("generated.txt")

def clear_generated():
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

def generate_html(content: str):
    content_text  = (CONTENT_ROOT / content).read_text()
    template_name_path = (CONTENT_ROOT / f"{content}.template")
    if os.path.isfile(template_name_path):
        template_name = template_name_path.read_text()
    else:
        print(
            f"Cannot find '{template_name_path}' for '{CONTENT_ROOT / content}'"
            )
        return ""

    template_text = (TEMPLATE_ROOT / template_name).read_text()

    return template_text.replace("{{CONTENT}}", markdown.markdown(content_text))

def create_parent_dirs(file_path: Path):
    file_path.parent.mkdir(exist_ok=True, parents=True)

script_dir = Path(__file__).parent.resolve()
os.chdir(script_dir)

if os.path.isfile(WEBSITE_GENERATED):
    clear_generated()
else:
    print(f"Cannot find '{WEBSITE_GENERATED}'")

generated = open(WEBSITE_GENERATED, "a")

for file_name in glob.glob(f"{CONTENT_ROOT}/**/*.md", recursive=True):
    relative_path = Path(*Path(file_name).parts[1:])

    output_path = Path(WEBSITE_ROOT) / relative_path
    output_path = output_path.with_suffix(".html")

    create_parent_dirs(output_path)
    with open(output_path, "w") as output:
        output.write(generate_html(relative_path))
        generated.write(f"{Path(*output_path.parts[1:])}\n")

        print(f"Created '{output_path}' for '{Path(file_name)}'")
