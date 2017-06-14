#!/usr/bin/env python
"""\
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py <input> <output>
"""

# 出于python3的需要, 这里把words_data文件处理为word_data_unix

original = "word_data.pkl"
destination = "word_data_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content) - outsize))
