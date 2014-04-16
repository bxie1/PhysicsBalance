import math
import cPickle as pickle

import Box2D as b2
from Box2D import *
from noveltySearch import *

from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn


"""begin with creating the world"""

worldAABB=b2AABB()
worldAABB.lowerBound = (-100, -100)
worldAABB.upperBound = (100, 100)
#set gravity; allow objects to settle
gravity = (0, -10) # for pybox2d < 2.0.2b1, this must be a b2Vec2
doSleep = True

#create the world object
world = b2World(worldAABB, gravity, doSleep)


#1. Define a body with a position, damping, etc
groundBodyDef = b2BodyDef()
groundBodyDef.position = (0, -10)

#2. Use the world object to create the body. 
groundBody = world.CreateBody(groundBodyDef)

#3. Define shapes with geometry, friction, density, etc. 
groundShapeDef = b2PolygonDef()
groundShapeDef.SetAsBox(50, 10)

#4. Create shapes on the body. 
groundBody.CreateShape(groundShapeDef)

# We now make a dynamic body...
bodyDef = b2BodyDef()
bodyDef.position = (0, 4)
body = world.CreateBody(bodyDef)

# Create shape...
shapeDef = b2PolygonDef()
shapeDef.SetAsBox(1, 1)
shapeDef.density = 1
shapeDef.friction = 0.3
body.CreateShape(shapeDef)
body.SetMassFromShapes()

timeStep = 1.0 / 60.0
velocityIterations = 10
positionIterations = 8


for i in range(60):
    world.Step(timeStep, velocityIterations, positionIterations)
    print body.position, body.angle
"""
simulation loop: reset the world simulation each trial
"""




