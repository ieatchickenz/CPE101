# Write your code for every function
# Project 2 - Moonlander Functions
# Author: 
# Version: 

from math import *

def showWelcome():
   print('Welcome aboard the Lunar Module Flight Simulator')
   print("\n   To begin you must specify the LM's initial altitude")
   print('   and fuel level.  To simulate the actual LM use')
   print('   values of 1300 meters and 500 liters, respectively.')
   print('\n   Good luck and may the force be with you!\n')
   
def getFuel():
   fuel = 0
   while not(fuel > 0):
        fuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
        if fuel > 0:
           return fuel
        else:
           print('ERROR: Amount of fuel must be positive, please try again')
   

def getAltitude():
   altitude = 0
   while altitude < 1 or altitude > 9999:
        altitude = int(input('Enter the initial altitude of the LM (in meters): '))
        if altitude >=1 and altitude <=9999:
           return altitude
        else:
           print('ERROR: Altitude must be between 1 and 9999, inclusive, please try again')
   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print('%13s'%'Elapsed Time:', end='')
   print('%5d'%elapsedTime, end=' ')
   print('s')
   print('%13s'%'Fuel:', end='')
   print('%5d'%fuelAmount, end=' ')
   print('l')
   print('%13s'%'Rate:', end='')
   print('%5d'%fuelRate, end=' ')
   print('l/s')
   print('%13s'%'Altitude:', end='')
   print('%8.2f'%altitude, end=' ')
   print('m')
   print('%13s'%'Velocity:', end='')
   print('%8.2f'%velocity, end=' ')
   print('m/s')

def getFuelRate(currentFuel):
    rate = 0
    while rate >=0 or rate <9:
       rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
       if rate <0 or rate >9:
           print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
       elif currentFuel <  rate:
           return abs(currentFuel)
       elif rate <= currentFuel:
           return abs(rate)
 
def updateAcceleration(gravity, fuelRate):
   return (float(gravity) * ((int(fuelRate)/5) - 1))
	
def updateAltitude(altitude, velocity, acceleration):
   if altitude < 0:
        return 0
   else:
        return (float(altitude) + float(velocity) + (float(acceleration)/2)) 

def updateVelocity(velocity, acceleration):
   return (float(velocity) + float(acceleration))

def updateFuel(fuel, fuelRate):
   return int(fuel) - int(fuelRate)

def displayLMLandingStatus(velocity):
   if velocity >= -1:
      print('Status at landing - The eagle has landed!')
   elif velocity > -10 and velocity < -1:
      print('Status at landing - Enjoy your oxygen while it lasts!') 
   else:
      print('Status at landing - Ouch - that hurt!') 

