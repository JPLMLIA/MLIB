"""
Test suite to invoke all of the mlib unit tests.
"""

import mlib.classification
import mlib.cluster
import mlib.color
import mlib.correlation
import mlib.datadict
import mlib.dimension_reduction
import mlib.equation
import mlib.numeric
import mlib.progressbar
import mlib.formatting
import mlib.flatfile
import mlib.mtypes
import mlib.IDL
import mlib.HDF5
import mlib.iterable
import mlib.latlon
import mlib.log
import mlib.memory
import mlib.mstring
import mlib.mtime
import mlib.plot
import mlib.plot3d
import mlib.plot_seaborn
import mlib.regex
import mlib.regression
import mlib.shell
import mlib.spanning


if __name__ == "__main__":
    import doctest
    import numpy as N

    N.set_printoptions(legacy='1.13')

    doctest.testmod(mlib.classification, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.cluster, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.color, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.correlation, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.datadict, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.dimension_reduction, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.equation, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.flatfile, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.formatting, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.HDF5, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.IDL, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.iterable, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.latlon, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.mstring, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.mtime, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.mtypes, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.numeric, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.plot, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.plot3d, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.plot_seaborn, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.regex, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.regression, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.shell, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.spanning, optionflags=doctest.ELLIPSIS)

    # Don't have tests defined
    # doctest.testmod(mlib.log, optionflags=doctest.ELLIPSIS)
    # doctest.testmod(mlib.memory, optionflags=doctest.ELLIPSIS)
    doctest.testmod(mlib.progressbar, optionflags=doctest.ELLIPSIS)
