import galaxy as galaxy
import matplotlib.pyplot as plt
import pandas as pd



# sertain variables ( not all ) to set from the input interface
endtime =  365 # in days, the amount of days the simulation should run
time_interval = 24*60*60 #seconds, the amount of time after wich the location and velocity's of the planet is checked and recalculated, lower value = more accuracy

# end of variables to set!

time = 0 
time_stop = endtime * ( 24*60*60) 


stars = [] # list of al the stars to use in the simulator
planets = [] # list of al the planets to use in the simulator



# !!!!!! example star, planets and alien used for testing and show functionallity, must be removed for final product!!!!!

sun = galaxy.Star("sun", 1.9884*10**30, 0, 0) 
stars.append(sun)

# planet_1 = galaxy.Planet_manager.create_planet_physical_orbit(name, Star, mass, start_x, start_y, start_x_speed, start_y_speed) <- how the inputs should be organised for class planet_physical_orbit
planet_1 = galaxy.Planet_manager.create_planet_physical_orbit("earth", sun, 5.972*10**24, 1.496*10**11, 0, 0, 29750)
planets.append(planet_1)

# planet_2 = galaxy.Planet_manager.create_planet_circular_orbit(name, Star, mass, start_x, start_y,) <- how the inputs should be organised for class planet_circular_orbit
planet_2 = galaxy.Planet_manager.create_planet_circular_orbit("zamboria", sun, 5.972*10**24, 1.496*10**11, 0)
planets.append(planet_2)

# alien = galaxy.Alien(name, Star, mass, start_x, start_y, start_x_speed, start_y_speed) <- how the inputs should be organised for class aliens
# alien = galaxy.Alien( "rick", sun, 1, 1, 1, 1, 1)
# planets.append(alien)



#!!remove till here 

while time < time_stop: # here, the system checks if we have reached the day that we want to stop the simulation
    for p in planets:
        p.get_location(time_interval) # this refers to the imported simulator called galaxy to see wgere the objects are and are going
    
    time += time_interval
    
    current_day = time / (time_interval * ((24*60*60)/time_interval))
    progress = current_day / endtime *100
    print(f"Day: {int(current_day)} / {endtime} ({progress:.1f}%)") # these 3 lines add a loading bar as a way to see how far along the simulation is

# creating pandas data frame with al the location results from al the planets

rows = []
for planet in planets:
    row = { "name": planet.name }
    for time, (x, y) in enumerate(zip(planet.x_positions, planet.y_positions), start=1):
        row[f"x_position_at_time={time}"] = x
        row[f"y_position_at_time={time}"] = y
    rows.append(row)

df = pd.DataFrame(rows)
df.index = "planet_" + (df.index+1).astype(str)
print(df)


#!!!!!example plotter used for testing,must be removed for final product!!!!!
#creates an plot with the orbits the planets have followed

for Planet in planets:
    # print(planet.results())
    plt.plot(Planet.x_positions, Planet.y_positions, marker='.', label=Planet.name)    
    plt.xlabel("x")       
    plt.ylabel("y")
    plt.title("Baan in het x-y vlak")       
    plt.axis("equal")           # gelijke schaal (belangrijk!)
    plt.grid(True)

plt.legend(loc="upper left")
plt.show()

#!!remove till here


