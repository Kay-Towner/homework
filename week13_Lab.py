#by Kay Towner


import math
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

"""Part 1."""
#1. Azimuth and Altitude vs ascension and declination and galactic coordinates
#2. celestial, galactic is a bit to large (literally galaxy sized)
#3. RA is measured in time, hours, min, sec
#4. 1 stands for the distance from the center of the galaxy

"""Part 1.2."""
distance = 100 * u.m
print(distance)

time = 50 * u.s
print(time)

velocity = distance / time
print(velocity)

#reads out m/s meters per second

distance2 = distance.to(u.km)
print(distance2)

#read out 0.1 km

"""Part 1.3."""
sundist = 1.0 * u.AU

sundist2 = sundist.to(u.parsec)
print("dist:",sundist2)

sundist3= sundist2.to(u.km)
print("dist:",sundist3)

marsdist = 1.5 * u.AU
marsdist2 = marsdist.to(u.km)
print("dist Mars:",marsdist2)

#224396806.04999998 km

jupdist = 5.2 * u.AU
jupdist2 = jupdist.to(u.parsec)
print("dist Jupter:", jupdist2)

#2.521031141769587e-05 pc

"""Part 1.4."""
c = SkyCoord.from_name('crab nebula')
print("Degree:",c.dec.degree)
crabdeg = c.dec.degree
cragra = c.ra.hour

K = SkyCoord.from_name("KIC 2010607")
print('declination:', K.dec.degree)
print('ra:', K.ra.hour)
kra = K.ra.hour
kdeg = K.dec.degree

S = SkyCoord.from_name("Sgr A*")
print('Dist from center', S.ra.hour)
print('Dist from the midplane ', S.dec.degree)

som = SkyCoord.from_name("Sombrero Galaxy")
print("Degree:", som.dec.degree)

L = SkyCoord.from_name("Lagoon Nebula")
#had a bit of trouble here:
##print('declination:', L.dec.degree)
##ra = L.ra.hour
##newra = ra.to(u.hms)
##print(ra)
##print(newra)

"""Part 1.5."""
objkic = SkyCoord(ra= kra, dec= kdeg, frame='icrs')

objcrab = SkyCoord(ra= crabra, dec= crabdeg, frame='icrs')

sep = objkic.seperation(objcrab)
print("The seperation it:", sep)
print("The seperation in arcsecond is:", sep.arcsecond)
print("The seperation in parsecs is:", sep.parsec)















