pseudo-python-lzo
=========
Python interface for lzop

## Overview

Yet another Python binding for LZO data compression library using subprocess.Popen.

You should not use this in production environment.
This is just a wrapper for invoking external process.
However, in other words, this will produce exactly same binary string as lzop unlike python-lzo.
(this is using lzop internaly!!)


## See also

python-lzo
- http://www.oberhumer.com/opensource/lzo/download/LZO-v1/python-lzo-1.08.tar.gz
