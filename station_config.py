class Station:
    def __init__(self, cse, network, name, coordinates, masl):
        self.cse = cse
        self.network = network
        self.name = name
        self.latitude = coordinates[0]
        self.longitude = coordinates[1]
        self.masl = masl
        
class Sensor:
    def __init__(self, variable, depthfrom, depthto, station):
        self.variable = variable
        self.depthfrom = depthfrom
        self.depthto = depthto
        self.station = station