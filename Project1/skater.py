#Project 1
#
#Name:Alex Petrov
#Instructor:S. Einakian
#Section:01

from funcs import *

def main():

#input all variables
    in_pounds = input('How much do you weigh (pounds)? ')
    in_distance = input('How far away is your professor (meters)? ')
    in_object = input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')

#print Nice Throw
    print('\nNice throw!', end = '')

#calculate what is needed using the inputs
    pounds = float(in_pounds)
    massSkater = poundsToKG(pounds)
    distance = float(in_distance)
    velObject = getVelocityObject(distance)
    massObject = getMassObject(in_object)
    VelSkater = getVelocitySkater(massSkater, massObject, velObject)
 
#issue prompts based on mass and vel
    if massObject <= 0.1:
       print(" You're going to get an F!")
    elif massObject > 0.1 and massObject <= 1.0:
       print(" Make sure your professor is OK.")
    else:
       if distance < 20:
          print(" How far away is the hospital?")
       else:
          print(" RIP professor.")

#print the velocity of the skater
    print("Velocity of skater: %.3f"%VelSkater,"m/s") 
    
#print prompts based on velocity
    if VelSkater < 0.2:
       print("My grandmother skates faster than you!")
    elif VelSkater >= 0.2 and VelSkater <= 1.0:
       print()
    else:
       print("Look out for that railing!!!")  


if __name__ == '__main__':
   main()
