from __future__ import annotations
import numpy as np
import math as math
from abc import ABC, abstractmethod

class Galaxy:
    G = 6.6743*10**-11  # Make gravittional force global available 
    def __init__(self, name, mass, start_x: float = 0, start_y: float = 0):
        # super init
        self.name = name
        self.mass = mass
        self.x = start_x
        self.y = start_y
        
class Star(Galaxy):
    #  Star class, static object in the galaxy like the sun
    def get_location(self):
        # get star's location
        return self.x, self.y
    def get_mass(self):
        # get star's mass
        return self.mass


class Moving_Object(Galaxy): # Class for moving objects in the galaxy like planets, komets, ufo's etc
    def __init__ (self, name, Star: Star, mass, start_x: float, start_y: float, start_x_speed: float = 0, start_y_speed: float = 0  ):
        super().__init__(name, mass,start_x,start_y)
        #  set moving object own attributes
        self.reference_x, self.reference_y = Star.get_location()
        self.reference_mass = Star.get_mass()
        self.reference_name = Star.name
        self.vx = start_x_speed
        self.vy = start_y_speed
        self.x_positions = []
        self.y_positions = []

    def __str__(self) -> str:
        #  printable definition of the moving object
        return f"{self.name} {self.mass} orbiting around {self.reference_name}"
    

    @abstractmethod
    def get_location(self, time_interval):
        # get current location of the planet. Redefine in the subclass
        pass
    
     
    def set_reference_Star(self, Star: Star):
        #   set data of reference star, this is the star around which the planets circulate
          self.reference_x, self.reference_y = Star.get_location( )
          self.reference_mass = Star.get_mass()


  

class Planet_physical_orbit(Moving_Object):
    def get_location( self,time_interval ) :
        ###Physical function for orbit
        r = (((self.x-self.reference_x)**2 + (self.y-self.reference_y)**2))**0.5 #distance between the planet and the star
        Fg = Galaxy.G*(self.reference_mass*self.mass)/r**2 #gravitational force
        
        # Calculate the current x position in time
        ax = -Fg * (self.x-self.reference_x) / r / self.mass
        self.vx = self.vx + ax    * time_interval
        self.x = self.x + self.vx * time_interval
        # Store the x postion in a list
        self.x_positions.append(self.x.real)

        # Calculate the current y position in time
        ay = -Fg * (self.y-self.reference_y) / r / self.mass
        self.vy = self.vy + ay    * time_interval 
        self.y = self.y + self.vy * time_interval
         # Store the y postion in a list
        self.y_positions.append(self.y.real)
        
        return self.x,self.y,self.x_positions,self.y_positions
    


class Object_manager:
    # Class to instantiate the moving objects. 
    @staticmethod
    def create_planet_circular_orbit( name, Star: Star, mass, start_x: float, start_y: float, d =9):
          ### Mathematical fuction for orbit
          star_x, star_y = Star.get_location()
          star_mass = Star.get_mass()      
          r_constant = (((start_x - star_x)**2 + (start_y -star_y)**2))**0.5 #distance between the planet and the star
          #get needed speed to achieve circular orbit with pyshics calculation
          vx, vy = Object_manager.get_needed_speed( r_constant, start_x, start_y, star_mass, Star.x, Star.y) 
          # Create Physical planet for the asked distance to the star
          Planet = Object_manager.create_planet_physical_orbit(name, Star, mass, start_x, start_y, vx, vy)
          return Planet
    
    @staticmethod
    def create_planet_physical_orbit ( name, Star: Star, mass, start_x: float, start_y: float, start_x_speed: float = 0, start_y_speed: float = 0  ):
         # create Physics calculated orbit by speed mass planet, mass star and G force 
         Planet = Planet_physical_orbit(name, Star, mass, start_x, start_y, start_x_speed , start_y_speed)
         return Planet

    @staticmethod
    def get_needed_speed( radius, x , y, reference_mass, reference_x, reference_y):
        # Calculate speed for needed radius
        omega = math.sqrt((Galaxy.G * reference_mass)/radius**3) #calculate angular velocity
        vt = radius * omega #linear tangential velocity
        theta = np.degrees(np.arctan2((y - reference_y), (x - reference_x))) # signed angle 
        vx = np.sin(theta) * vt   # Get x speed
        vy = np.cos(theta)* vt    # Get y speed
        return vx, vy
