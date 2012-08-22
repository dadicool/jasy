#
# Jasy - Web Tooling Framework
# Copyright 2010-2012 Zynga Inc.
#

__version__ = "0.8-alpha2"
__author__ = "Sebastian Werner <info@sebastian-werner.net>"

def info():
    from jasy.core.Logging import colorize

    print("Jasy is powerful web tooling framework inspired by SCons")
    print("Copyright (c) 2010-2012 Zynga Inc. %s" % colorize("http://zynga.com/", "underline"))
    print("Visit %s for details." % colorize("https://github.com/zynga/jasy", "underline"))
    print()

