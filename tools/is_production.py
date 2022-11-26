import sys


def is_production() -> bool:
  return True if ['-t', 'prod'] == sys.argv[1:] else False

