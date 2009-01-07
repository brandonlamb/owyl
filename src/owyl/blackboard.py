# -*- coding: utf-8 -*-
"""blackboard -- basic blackboard behaviors for Owyl



Copyright 2008 David Eyk. All rights reserved.

$Author$\n
$Rev$\n
$Date$
"""

__author__ = "$Author$"[9:-2]
__revision__ = "$Rev$"[6:-2]
__date__ = "$Date$"[7:-2]


import core

__all__ = ['checkBB', 'setBB',]

class Blackboard(dict):
    """A dict that defaults values to None.
    """
    def __init__(self, **kwargs):
        super(Blackboard, self).__init__(**kwargs)
        self.setdefault(None)

@core.task
def checkBB(**kwargs):
    """Check a value on the blackboard.

    @keyword blackboard: The blackboard object.

    @keyword key: The name of a key on the blackboard.
    @type key: A hashable object

    @keyword check: A function that takes the value on the blackboard
                    and returns a boolean.
    """
    bb = kwargs['blackboard']
    key = kwargs['key']
    check = kwargs.get('check', lambda x: x is not None)
    value = bb[key]
    result = check(value) and True or False # Always return a boolean.
    yield result

@core.task
def setBB(**kwargs):
    """Set a value on the blackboard.

    @keyword blackboard: The blackboard object.

    @keyword key: The name of a key on the blackboard.
    @type key: A hashable object

    @keyword value: The value to set on the key.
    """
    bb = kwargs['blackboard']
    key = kwargs['key']
    value = kwargs['value']
    bb[key] = value
    yield True


