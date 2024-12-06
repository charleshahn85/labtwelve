import math

class UniversalGravity:
    
    G = 6.67430e-11  # m^3 kg^-1 s^-2

class Sun:
    def __init__(self, name, mass, radius, temp):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.temp = temp
        self.x = 0.0
        self.y = 0.0

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def __str__(self):
        return f'Sun({self.name}, Mass: {self.mass}, Radius: {self.radius}, Temp: {self.temp})'

class Planet:
    def __init__(self, name, mass, distance, radius, vel_x, vel_y, color):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.x = distance
        self.y = 0.0
        self.color = color

    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def get_x_vel(self):
        return self.vel_x

    def get_y_vel(self):
        return self.vel_y

    def set_x_vel(self, new_x_vel):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.vel_y = new_y_vel

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return f'Planet({self.name}, Mass: {self.mass}, Distance: {self.distance}, Color: {self.color})'

class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def add_sun(self, the_sun):
        self.the_sun = the_sun

    def add_planet(self, new_planet):
        self.planets.append(new_planet)

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        dt = 0.001  
        for planet in self.planets:
         
            planet.move_to(planet.get_x_pos() + dt * planet.get_x_vel(), 
                           planet.get_y_pos() + dt * planet.get_y_vel())
            
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x**2 + dist_y**2)
            
            acc_x = UniversalGravity.G * self.the_sun.get_mass() * dist_x / new_distance**3
            acc_y = UniversalGravity.G * self.the_sun.get_mass() * dist_y / new_distance**3
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)

class Simulation:
    def __init__(self, solar_system, width, height, num_periods):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods

    def run(self):
        for _ in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()

if __name__ == '__main__':
    solar_system = SolarSystem()
    the_sun = Sun("SOL", 1.989e30, 695700, 5778)  # Example values
    solar_system.add_sun(the_sun)
    
    earth = Planet("EARTH", 5.972e24, 1.496e11, 6371, 29780, 0, "green")
    solar_system.add_planet(earth)
    
    mars = Planet("MARS", 6.4171e23, 2.279e11, 3389.5, 24077, 0, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 1000)
    simulation.run()

