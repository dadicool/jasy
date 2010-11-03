#!/usr/bin/env python3

# Extend PYTHONPATH with 'lib'
import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), os.pardir, "lib")))

# Import JavaScript tooling
from js import *
import time, logging

start = time.time()

# Application specific code
session = Session()
session.addProject(Project("../../qooxdoo/qooxdoo/framework"))
session.addProject(Project("../../qooxdoo/qooxdoo/component/apiviewer"))
session.addProject(Project("../../unify/framework"))

# Locale data
session.addLocale("en_US")
#session.addLocale("de_DE")

# Variant data
session.addVariant("qx.debug", [ '"on"' ])
session.addVariant("qx.client", [ '"gecko"' ])
session.addVariant("qx.dynlocale", [ '"off"' ])
session.addVariant("qx.application", [ '"apiviewer.Application"' ])
session.addVariant("qx.globalErrorHandling", [ '"off"' ])
session.addVariant("qx.jstools", ["true"])
session.addVariant("qx.version", ["1.0"])
session.addVariant("qx.theme", ['"apiviewer.Theme"'])

optimization = set(["privates", "variables", "declarations", "blocks"])

# Boot Initializer
boot = "qx.core.Init.boot(apiviewer.Application);"


# Generate source loader (LabJS)
resolver = Resolver(session)
resolver.addClassName("apiviewer.Application")
resolver.addClassName("apiviewer.Theme")
sorter = Sorter(resolver.getIncludedClasses())
loader = Loader(sorter.getSortedClasses())
loader.generate("source.js", boot)


# Build version
for permutation in session.getPermutations():
    hashed = permutation.getHash()
    logging.info("Permutation: %s" % permutation)
    
    # Resolving dependencies
    resolver = Resolver(session, permutation)
    resolver.addClassName("apiviewer.Application")
    resolver.addClassName("apiviewer.Theme")
    classes = resolver.getIncludedClasses()

    # Sorting classes
    sorter = Sorter(classes, permutation)
    sortedClasses = sorter.getSortedClasses()
    
    # Compiling classes
    compressor = Compressor(sortedClasses, permutation, optimization, boot)
    compressor.compress("main-%s.js" % hashed)


# Info
logging.info("Runtime: %ims" % ((time.time()-start)*1000))

# Close session
session.close()