#Project 1
#
#Name: Alex Petrov
#Instructor: S. Einakian
#Section: 01

import math

#takes a input of weight in pounds and coverts it to KG
#None -> float

def poundsToKG(pounds):   
    return(pounds*(0.453592))
   
#takes an input as a string and returns a mass in float form
#string -> float 
def getMassObject(object):
   if object == 't':
      return 0.1
   elif object == 'p':
      return 1.0
   elif object == 'r':
      return 3.0
   elif object == 'g':
      return 5.3
   elif object == 'l':
      return 9.07
   else:
      return 0.0

#takes an inputed distance between the teacher and student and calculates the velocity of the thrown object
#int -> int
def getVelocityObject(distance):
    dis = math.sqrt((9.8*distance)/2)
    return dis

#takes the values calculated by the previous three functions and returns the velocity of the skater
# float float float -> float
def getVelocitySkater(massSkater, massObject, velObject):
    return((massObject * velObject)/(massSkater))

 
