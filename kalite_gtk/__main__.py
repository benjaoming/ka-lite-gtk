#!/usr/bin/env python
# Copyright (c) Foundation for Learning Equality.
# See LICENSE for details.

from __future__ import print_function
from __future__ import unicode_literals

import sys

try:
    from gi.repository import Gtk
except ImportError:
    print(
        "Could not find GTK3, maybe you don't have it installed or you are "
        "running from a virtualenv."
    )
    sys.exit(1)


import os

sys.path.insert(0, os.path.abspath(os.getcwd()))


from kalite_gtk.mainwindow import MainWindow


def main(args=None):
    __ = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
