class WindDirection():
    @staticmethod
    def wind_dir(wind_direction):
        if wind_direction >= 0 and wind_direction <= 45 or wind_direction >= 315 and wind_direction <=360:
            direction = 'Nord'
            return direction
        if wind_direction >= 46 and wind_direction <= 135:
            direction = 'East'
            return direction
        if wind_direction >= 136 and wind_direction <= 225:
            direction = 'Юг'
            return direction
        if wind_direction >= 226 and wind_direction <= 314:
            direction = 'West'
            return direction
