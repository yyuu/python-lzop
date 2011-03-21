#!/usr/bin/env python

from contextlib import closing
from subprocess import Popen, PIPE

LZOP = '/usr/bin/lzop'

def compress(string, level=1):
  if not level in xrange(1, 9):
    raise(RuntimeError('compression level have to be between 1 and 9' % (level)))
  arg_level = '-%d' % (level)
  try:
    pipe = Popen([LZOP, arg_level, '--stdout'], stdin=PIPE, stdout=PIPE)
    with closing(pipe.stdin) as fp:
      fp.write(string)
    with closing(pipe.stdout) as fp:
      return fp.read()
  except Exception, error:
    raise

def decompress(string):
  try:
    pipe = Popen([LZOP, '--decompress', '--stdout'], stdin=PIPE, stdout=PIPE)
    with closing(pipe.stdin) as fp:
      fp.write(string)
    with closing(pipe.stdout) as fp:
      return fp.read()
  except Exception, error:
    raise

if __name__ == '__main__':
  s = 'asdfasdf'
  c = compress(s)
  d = decompress(c)
  print(s == d)
