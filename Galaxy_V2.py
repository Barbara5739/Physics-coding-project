from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math as math
from abc import ABC, abstractmethod 


class Galaxy:             # The upper most class of the galaxy system
    G = 6.6743*10**-11    # G is the universal gravitation constant that will be used througout the simulation, since this number is equal everywhere in the universe / galaxy, it belongs to this class.
    
    
    def __init__(self, name, mass, start_x: float = 0, start_y: float = 0):    # these are propperties that every object "spawned" inside our galaxy has, therefore they are already defined in the galaxy class to avoid repetition of code
        # super init
        self.name = name
        self.mass = mass
        self.x = start_x
        self.y = start_y
        
class Star(Galaxy):        # returns the value's of the star(s) in the galaxy system to use in plots
    #  Star class, static object in the galaxy like the sun
    def get_location(self):
        # get star's location
        return self.x, self.y
    def get_mass(self):
        # get star's mass
        return self.mass

class Moving_Object(Galaxy): # Class for moving objects in the galaxy like planets, comets, ufo's etc
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
        return f"Planet: {self.name} mass: {self.mass} orbiting around {self.reference_name}"
    
    @abstractmethod
    def get_location(self, time_interval):
        # get current location of the planet. Redefine in the subclass
        pass
    
    def get_loclist(self):
        return self.x_positions, self.y_positions

    def set_reference_Star(self, Star: Star):
        #   set data of reference star, this is the star around which the planets circulate
          self.reference_x, self.reference_y = Star.get_location( )
          self.reference_mass = Star.get_mass()


  
class Planet_physical_orbit(Moving_Object):
    def get_location(self, time_interval) :
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
        
        # return self.x_positions,self.y_positions
        return self.x, self.y
    

# class moon(Moving_Object):
#     # def __init__   if neccassary

#     def get_location(self, time_interval):
#         # return super().get_location(time_interval)
#         pass

class alien_visitor(Moving_Object):
  
#     !!!!!!!!!! Make use of moving objects
    def __init__(self, name, Star, mass_a, x_initial_a, y_initial_a, perihelion_distance_a, orbital_eccentricity_a):
        super().__init__(name, Star, mass_a, x_initial_a, y_initial_a) 
    #     self.mass_a = mass_a
    #     # single starting position
    #     self.x0 = x_initial_a
    #     self.y0 = y_initial_a
    #     # orbit lists
    #     self.x_positions = []
    #     self.y_positions = []
        # x_initial_a = 1.5e11
        self.day = 0
        self.distance_to = x_initial_a
        self.track = np.linspace(-x_initial_a, x_initial_a, 365)
        self.perihelion_distance = perihelion_distance_a
        self.orbital_eccentricity = orbital_eccentricity_a

# !!!!!!!! define method does nothing just two list 
    # def _define_initial_position_alien(self):  
    #     self.x_initial_a = []
    #     self.y_initial_a = []
    #     return self.x_initial_a, self.y_initial_a

# !!!!!!!  use a redefinition of get_location to calculate the position
#  and calculate the positions in the outside loop not in the class itself
    def get_location(self, time_interval) :
    # def plot_alien_visitor_orbit(self):
        # self.x_positions = []
        # self.y_positions = []
        ds = self.distance_to
        self.day += time_interval/ (24*3600)
        if self.day > 364:
            self.day = 0
        i = int(self.day)
        self.x = self.track[i]
        self.y = self.orbital_eccentricity * (self.x / ds)**2 * ds - self.perihelion_distance * ds

        self.x_positions.append(self.x)
        self.y_positions.append(self.y)
        return self.x, self.y
        # for x in np.linspace(-3*self.x, 3*self.x, 400):
        #     y = self.orbital_eccentricity * (x / AU)**2 * AU - self.perihelion_distance * AU
        #     self.x_positions.append(x)
        #     self.y_positions.append(y)

class Object_manager:
    # Class to instantiate the moving objects. 
    @staticmethod
    def create_planet_circular_orbit(name, Star: Star, mass, start_x: float, start_y: float, d =9):
          ### Mathematical fuction for orbit
                
          r_constant = (((start_x - Star.x)**2 + (start_y -Star.y)**2))**0.5 #distance between the planet and the star
          #get needed speed to achieve circular orbit with pyshics calculation
          vx, vy = Object_manager.get_needed_speed( r_constant, start_x, start_y, Star.mass, Star.x, Star.y) 
          # Create Physical planet for the asked distance to the star
          Planet = Object_manager.create_planet_physical_orbit(name, Star, mass, start_x, start_y, vx, vy)
          return Planet
    
    @staticmethod
    def create_planet_physical_orbit ( name, Star: Star, mass, start_x: float, start_y: float, start_x_speed: float = 0, start_y_speed: float = 0  ):
         # create Physics calculated orbit by speed mass planet, mass star and G force 
         Planet = Planet_physical_orbit(name, Star, mass, start_x, start_y, start_x_speed , start_y_speed)
         return Planet
   
    @staticmethod
    def create_alien_visitor(name, Star: Star, mass, start_x: float, start_y: float, perihelion_distance: float, orbital_eccentricity: float  ):
         # create Physics calculated orbit by speed mass planet, mass star and G force 
         Alien = alien_visitor(name, Star, mass, start_x, start_y, perihelion_distance , orbital_eccentricity)
         return Alien

    # @staticmethod
    # def create_moon( name, Star: Star, mass, start_x: float, start_y: float, start_x_speed: float = 0, start_y_speed: float = 0  ):
        # create Physics calculated orbit by speed mass planet, mass star and G force 
        #  Moon = Moon(name, Star, mass, start_x, start_y, start_x_speed , start_y_speed)
        #  return Moon
        

    @staticmethod
    def get_needed_speed( radius, x , y, reference_mass, reference_x, reference_y):
        # Calculate speed for needed radius
        omega = math.sqrt((Galaxy.G * reference_mass)/radius**3) #calculate angular velocity
        vt = radius * omega #linear tangential velocity
        theta = np.degrees(np.arctan2((y - reference_y), (x - reference_x))) # signed angle 
        vx = np.sin(theta) * vt   # Get x speed
        vy = np.cos(theta)* vt    # Get y speed
        return vx, vy

# class alien_visitor_old():
#     def __init__(self, mass_a, x_initial_a, y_initial_a, perihelion_distance_a, orbital_eccentricity_a):
    
      
#         self.mass_a = mass_a
#         # single starting position
#         self.x0 = x_initial_a
#         self.y0 = y_initial_a
#         # orbit lists
#         self.x_positions = []
#         self.y_positions = []
#         self.perihelion_distance = perihelion_distance_a
#         self.orbital_eccentricity = orbital_eccentricity_a

#     def _define_initial_position_alien(self):  
#         self.x_initial_a = []
#         self.y_initial_a = []
#         return self.x_initial_a, self.y_initial_a
#     def plot_alien_visitor_orbit(self):

#         self.x_positions = []
#         self.y_positions = []

#         for x in np.linspace(-3*AU, 3*AU, 400):
#             y = self.orbital_eccentricity * (x / AU)**2 * AU - self.perihelion_distance * AU
#             self.x_positions.append(x)
#             self.y_positions.append(y)
    

