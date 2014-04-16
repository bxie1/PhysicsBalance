#!/usr/bin/python
#
# C++ version Copyright (c) 2006-2007 Erin Catto http://www.gphysics.com
# Python version Copyright (c) 2008 kne / sirkne at gmail dot com
# 
# Implemented using the pybox2d SWIG interface for Box2D (pybox2d.googlecode.com)
# 
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

from pyglet.window import key
import string

# While the testbed tests were created with Pygame in mind, Pyglet can also
# be used. To make the keyboard constants the same for both tests, this keymapper
# is used to map pygame key constants to pyglet ones. 
#
# Only basic keys are mapped for now: K_[a-z0-9], K_F[1-12] and K_COMMA.

def map_keys():
    keys = {}
    for letter in string.uppercase:
        keys['K_'+letter.lower()] = getattr(key, letter)
    for i in range(0,9):
        keys['K_%d'%i] = getattr(key, '_%d' % i)
    for i in range(1,12):
        keys['K_F%d'%i] = getattr(key, 'F%d' % i)
    keys['K_COMMA']=key.COMMA
    return keys

temp = globals() 
temp.update(map_keys())

del key
del string
del temp
