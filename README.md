# Star system visualization

This code plots a visualization of a star system with various objects.

The code allows users to visualize a simplified star system based on the input of initial conditions. Planet, moon and and alien objects are created and their paths are visualized. Motion of the various objects is calculated either by using mathematical equations or physical equations that calculate the forces in a similar way to a real star system. 

Planets move on a circular (or elliptical) orbit around the central star, while moons move on circular orbits around planets. The 'alien' objects represent comets or asteroids that follow parabolic orbits.

Anyone interested in coding plots that move, or interested in visualizing various star systems could find this code useful. 


## Features

class sun: 
An object representing the star (the centre of the entire system). It is stationary, and it should always be plotted to aid visualization, as some of the orbits are calculated in a purely mathematical manner and will behave as if the star were there.

class planet:
Object(s) orbiting the sun on elliptical orbits. These orbits are based on physical formulas for the position of an object during an elliptical orbit. Experiment with the code: can you plot more than one planet? Two planets on the same orbit (like Earth and Theia)? Orbits with various radii?

class moon:
Moons have a circular orbit, and orbit a reference planet rather than a reference sun. Plotting them requires plotting at least one planet.

class alien:
This object follows a parabolic orbit. It enters the plot, then leaves; it does not stay in the simulated star system. This could represent an asteroid, a comet or even a green extraterrestrial looking around! The parabolic orbit is calculated using mathematical rather than physical formulas to limit complexity of the code, but the parabola mimics a true parabolic orbit using the orbital eccentricity and perihelion distance.

## Installation and Setup

### Prerequisites
To run this code, you will need:
- Python 3.8 or higher
- pip (Python package manager)
- numpy
- Matplotlib (pyplot and animation imported)
- pandas

__--> python packages used in the code include__ 
- math
- annotations from future
- ABC imported from abc
- sys

### Setup
__1. Clone the repository__

   git clone https://github.com/Barbara5739/Physics-coding-project

   cd Physics-coding-project
   
__2. install external packages__
   
   pip install -r requirements.txt
   
*a note on example data:*
The data saved in the file galaxy_objects.csv is a list of possible objects that can be created for this code. If you would like to create your own file, please keep the following information in mind:

 - the column "type": this specifies which class is being called (planet, moon, alien, etc.). For the planet class, this can be either CircularPlanet or PhysicsPlanet, which will create a circular orbit or an elliptical orbit, respectively.
 - for objects in the planet class: these objects do not have attributes orbital_eccentricity or perihelion_distance. These columns can be left blank
 - for all CircularPlanet orbits: the initial x and y speed is irrelevant. Fill in any number you like!
   
## Usage example:
Description
<img width="1254" height="948" alt="image" src="https://github.com/user-attachments/assets/2ac61e6c-651e-480c-a577-a7c0ff16a165" />

[GIF SHOWING WHAT IT DOES]

## Authors:
Csenge Barbara Andody-Tanczos

Aaliyah Leurs

Joep Drugmand

Maya Hauff

Maxine Sahrian

Nika Szafrańska

## Sources:
Parts of this code were created using ideas from the following sources:
- Movement of the 'alien': https://matplotlib.org/stable/gallery/animation/multiple_axes.html
- Reference for plot of parabolic orbit: https://stackoverflow.com/questions/30553585/graphing-a-parabola-using-matplotlib-in-python
- Visualisation of objects: https://towardsdatascience.com/simulate-a-tiny-solar-system-with-python-fbbb68d8207b/

## Contact:

b.andody-tanczos@student.maastrichtuniversity.nl

a.leurs@student.maastrichtuniversity.nl

j.drugmand@student.maastrichtuniversity.nl

m.hauff@student.maastrichtuniversity.nl

m.sahrian@student.maastrichtuniversity.nl

n.szafranska@student.maastrichtuniversity.nl
