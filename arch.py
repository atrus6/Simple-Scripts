from subprocess import call
import sys

for line in sys.stdin:
  line = line.strip()
  call(['7z', 'a', '-t7z', line + '.7z', line])
