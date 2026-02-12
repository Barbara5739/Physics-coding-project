import galaxy as galaxy
import matplotlib.pyplot as plt
import pandas as pd



# sertain variables ( not all ) to set from the input interface
endtime =  365 # in days, shoul
time_interval = 24*60*60 #seconds

# end of variables to set!
time = 0
time_stop = endtime * ( 24*60*60) 


stars = []
planets = []



# !!!!!! example star, planets and alien used for testing and show functionallity, must be removed for final product!!!!!

sun = galaxy.Star("sun", 1.9884*10**30, 0, 0) 
stars.append(sun)

# planet_1 = galaxy.Planet_manager.create_planet_physical_orbit(name, Star, mass, start_x, start_y, start_x_speed, start_y_speed)
planet_1 = galaxy.Planet_manager.create_planet_physical_orbit("earth", sun, 5.972*10**24, 1.496*10**11, 0, 0, 29750)
planets.append(planet_1)

# planet_2 = galaxy.Planet_manager.create_planet_circular_orbit(name, Star, mass, start_x, start_y,)
planet_2 = galaxy.Planet_manager.create_planet_circular_orbit("zamboria", sun, 5.972*10**24, 1.496*10**11, 0)
planets.append(planet_2)

# alien = galaxy.Alien(name, Star, mass, start_x, start_y, start_x_speed, start_y_speed)
alien = galaxy.Alien( "rick", sun, 1, 1, 1, 1, 1)
planets.append(alien)



#!!remove till here 

while time < time_stop:
    for p in planets:
        p.get_location(time_interval)
    
    time += time_interval
    #loading screen
    current_day = time / (time_interval * ((24*60*60)/time_interval))
    progress = current_day / endtime *100
    print(f"Day: {int(current_day)} / {endtime} ({progress:.1f}%)")

# creating pandas data frame with al the locations
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
