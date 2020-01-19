import sys
if sys.version_info < (3, 4):
  raise RuntimeError('At least Python 3.4 is required')
if sys.version_info[0] < 3:
  raise RuntimeError('At least Python 3 is required')
