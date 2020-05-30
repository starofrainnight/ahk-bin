=======
ahk-bin
=======

.. image:: https://img.shields.io/pypi/v/ahk-bin.svg
    :target: https://pypi.python.org/pypi/ahk-bin

.. image:: https://travis-ci.org/starofrainnight/ahk-bin.svg?branch=master
    :target: https://travis-ci.org/starofrainnight/ahk-bin

.. image:: https://ci.appveyor.com/api/projects/status/github/starofrainnight/ahk-bin?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/ahk-bin

A python package that bundled with workable AutoHotkey binary which could works for 'ahk' package

Usage
--------

::

    import ahkbin
    from ahk import AHK

    # If your Scripts directory of python be placed in PATH, it should works
    # like a charm
    ahk = AHK()

    # Otherwise, you must specific the path which bundled in our package
    ahk = AHK(executable_path=ahkbin.get_executable())

License
---------

This package is licensed under GPLv2.

The license of AutoHotkey binary are described in LICENSE_AHK.txt
