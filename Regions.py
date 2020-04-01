class Region:
    name = ""
    ID = -1
    #x_value 
    #y_value
    adjoining_regions = []
    #elevation
##    int ID; (each region will have an id)
##    int x_value;
##    int y_value;
##    list&lt;int&gt; adjoining_regions;
##    int elevation; (in meters)
##    string wind_direction;(N,E,W,S)
##    double Temp; (the temperature)
##    double rainfall;
##    double drainage;
##    bool fire;
##    bool thunderstorm;
##    bool blizzard;
##    bool snowfall;
##    bool snow_cover;
##    bool flooding;
    def __init__(self, name):
        self.name = name
