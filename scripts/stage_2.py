# Import from a zipfile using our own PathEntryFinder

import sys
from pathlib import Path
from typing import Final

from pycon_italia_2024.stage_2.finder import ZipFinder

ZIP_PATH: Final = Path("/tmp/pycon-italia-2024.zip")
assert ZIP_PATH.exists(), "Run scripts/_create_zip.py"

sys.path.append(str(ZIP_PATH))
sys.path_hooks.insert(0, ZipFinder.path_hook)

from what import FooBar

print(FooBar.hello_world)
