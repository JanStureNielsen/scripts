#!/usr/bin/env python

import os.path
import sys
import zipfile

if len(sys.argv) != 2:
    sys.exit('Usage: {} <filename>'.format(os.path.basename(sys.argv[0])))

filename = sys.argv[1]

filenames = [line.strip() for line in sys.stdin]

prefix, _ = os.path.splitext(filename)

with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as outfile:
    for filename in filenames:
        try:
            outfile.write(filename, os.path.join(prefix, filename))
        except OSError as e:
            sys.exit('error: {}: {}'.format(filename, e.strerror))
