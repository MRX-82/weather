class WindDirection():
    """
    Give window rotations in number, send window rotation in text
    """
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


class FDR():
    @staticmethod
    def restructurizace(pogoda):
        weather_list = []
        for i in range(len(pogoda)-1):
            pogoda_directions = WindDirection()
            direct = pogoda_directions.wind_dir(pogoda[i][4])
            st_pogoda = (
                'date time:', pogoda[i][0],
                'temp:', pogoda[i][1], 'conditions:', pogoda[i][2],
                'wind speed:', pogoda[i][3], 'wind rotations:', direct
            )
            weather_list.append(st_pogoda)
        return weather_list
