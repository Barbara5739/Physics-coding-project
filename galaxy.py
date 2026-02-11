from __future__ import annotations
import numpy as np
import math as math
from abc import ABC, abstractmethod


# the actual calculation

class galaxy:
    G = 6.6743*10**-11
    def __init__(self, name, mass, start_x: float = 0, start_y: float = 0):
        self.name = name
        self.mass = mass
        self.x = start_x
        self.y = start_y
        
class star(galaxy):
    def get_location(self):
        return self.x, self.y
    def get_mass(self):
        return self.mass


class planet(galaxy):
    def __init__ (self, name, mass, start_x: float = 0, start_y: float = 0, start_x_speed: float = 0, start_y_speed: float = 0):
        super().__init__(name,mass,start_x,start_y)
        self.vx = start_x_speed
        self.vy = start_y_speed
        self.x_positions = []
        self.y_positions = []

    @abstractmethod
    def get_location(self, time_interval):
        pass
    
     
    def set_refrence_star(self, star: star):
          self.refrence_x = star.x
          self.refrence_y = star.y
          self.refrence_mass = star.mass


class planet_circular_orbit(planet):

    def get_location(self, time_interval):
         self.r_constant
         self.time += time_interval
         theta = self.theta0 + self.omega * self.time
         self.x = self.refrence_x + self.r_constant * np.cos(theta)
         self.y = self.refrence_y + self.r_constant * np.sin(theta)

         self.x_positions.append(self.x.real)
         self.y_positions.append(self.y.real)

         return self.x,self.y,self.x_positions,self.y_positions
        
    def set_refrence_star(self, star: star):
          self.refrence_x = star.x
          self.refrence_y = star.y
          self.refrence_mass = star.mass
          self.r_constant = (((self.x-self.refrence_x)**2 + (self.y-self.refrence_y)**2))**0.5
          self.omega = ((((self.vx)**2 + (self.vy)**2))**0.5) / self.r_constant
          if self.y == 0:
              self.y = 1
          self.theta0 = (np.arctan2((self.y - self.refrence_y), (self.x - self.refrence_x)))
          self.time = 0

class planet_physical_orbit(planet):
    def get_location( self,time_interval ) :
         
        r = (((self.x-self.refrence_x)**2 + (self.y-self.refrence_y)**2))**0.5
        Fg = galaxy.G*(self.refrence_mass*self.mass)/r**2
        
        ax = -Fg * (self.x-self.refrence_x) / r / self.mass
        self.vx = self.vx + ax    * time_interval
        self.x = self.x + self.vx * time_interval
        self.x_positions.append(self.x.real)

        ay = -Fg * (self.y-self.refrence_y) / r / self.mass
        self.vy = self.vy + ay    * time_interval 
        self.y = self.y + self.vy * time_interval
        self.y_positions.append(self.y.real)
        
        return self.x,self.y,self.x_positions,self.y_positions


