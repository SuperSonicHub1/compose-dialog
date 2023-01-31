#!/usr/bin/env python
# https://github.com/davatorium/rofi/blob/next/doc/rofi-script.5.markdown
from locale import getlocale
from pathlib import Path
from re import split

compose_path = Path('/usr/share/X11/locale/') / '.'.join(getlocale()) / 'Compose'

with compose_path.open() as f:
	for line in f:
		line = line.strip()
		if line.startswith("#"):
			continue
		# <dead_greek> <p>                        : "π"   U03C0 # GREEK SMALL LETTER PI
		left, right = line.split(':', maxsplit=1)
		keys = left.strip()
		right_chunks = right.split(maxsplit=2)
		if len(right_chunks) == 3:
			character, _, char_name = right_chunks 
			character_name = char_name.strip() 
		elif len(right_chunks) == 1:
			character = right_chunks[0]
			character_name = ""
		

		print(f"{keys}\t({character}, {character_name})\t\0icon\x1faccessories-character-map\x1fmeta\x1f{character_name.lower()}")
