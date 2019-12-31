#Project 2
#
#Name: Alex Petrov
#Instructor:S. Einakian
#Section: 01

from landerFuncs import *

fuelRate = elapsedTime = velocity = acceleration = 0
gravity = 1.62

showWelcome()
altitude = getAltitude()
fuel = currentFuel = fuelAmount = getFuel()

print ('\nLM state at retrorocket cutoff')

displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

print()

while altitude > 0 and fuelAmount > 0:
    fuelRate = getFuelRate(currentFuel)
    fuel = fuelAmount = currentFuel = updateFuel(fuel, fuelRate)
    altitude = updateAltitude(altitude, velocity, acceleration)
    acceleration = updateAcceleration(gravity, fuelRate)
    velocity = updateVelocity(velocity, acceleration)
    elapsedTime += 1
    displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
    print()

while altitude > 0 and fuelAmount <= 0:
    print ('OUT OF FUEL - Elapsed Time: {0:3d} Altitude: {1:7.2f} Velocity: {2:7.2f}'.format(elapsedTime, altitude, velocity))
    fuelRate = 0
    acceleration = updateAcceleration(gravity, fuelRate)
    fuel = currentFuel = fuelAmount = updateFuel(fuel, fuelRate)
    velocity = updateVelocity(velocity, acceleration)
    altitude = updateAltitude(altitude, velocity, acceleration)
    elapsedTime += 1
if altitude < 0:
       altitude = 0
       print ('\nLM state at landing/impact')
       displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
       print()
       displayLMLandingStatus(velocity)

