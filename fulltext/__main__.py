
from __future__ import absolute_import

import os
import sys
import logging

from docopt import docopt

import fulltext


HERE = os.path.abspath(os.path.dirname(__file__))


def _handle_open(path):
    with open(path, 'rb') as f:
        return fulltext.get(f)


def test_modules():
    path = os.path.join(HERE, "backends")
    for name in os.listdir(path):
        if not name.endswith('.py'):
            continue
        mod_name = "fulltext.backends.%s" % (
            os.path.splitext(os.path.basename(name))[0])
        mod = __import__(mod_name, fromlist=[' '])
        print(mod)


def main(args=sys.argv[1:]):
    """Extract text from a file.

    Commands:
        extract - extract text from path
        test    - make sure all deps are installed

    Usage:
        fulltext extract [-f] [-t] <path>...
        fulltext test

    Options:
        -f      Open file first.
    """
    opt = docopt(main.__doc__.strip(), args, options_first=True)

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())

    if opt['test']:
        test_modules()
    else:
        handler = fulltext.get

        if opt['-f']:
            handler = _handle_open

        for path in opt['<path>']:
            print(handler(path))


if __name__ == '__main__':
    main()
