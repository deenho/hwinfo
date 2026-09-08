#!/usr/bin/env python3
import pathlib
import sys

if len(sys.argv) != 4:
    raise SystemExit(f'usage: {sys.argv[0]} INPUT OUTPUT NAME')

input_path = pathlib.Path(sys.argv[1])
output_path = pathlib.Path(sys.argv[2])
name = sys.argv[3]

data = input_path.read_bytes()
values = ','.join(f'0x{byte:02x}' for byte in data)

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    f'const unsigned char {name}[] = {{{values}}};\n'
    f'const unsigned int {name}_size = {len(data)};\n',
    encoding='ascii',
)
