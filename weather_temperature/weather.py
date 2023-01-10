from mrjob.job import MRJob

class WeatherStats(MRJob):
    
    def mapper(self, key, value):
        try:
            d, tmax, tmin, tavg = value.split(',')
            yield d, float(tavg)
        except ValueError:
            pass

    def reducer(self, key, values):
        for avg in values:
            yield key, "Cool" if avg < 50 else "Shiny"
        
if __name__ == '__main__':
    WeatherStats.run()