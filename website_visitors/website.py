from mrjob.job import MRJob

class WebsiteStats(MRJob):
    
    def mapper(self, key, value):
        try:
            records = value.split(',')
            for record in records[1:-1]:
                yield records[0], int(record)
        except ValueError:
            pass
        
    def reducer(self, key, values):
        val = list(values)
        yield key, f'Min: {min(val)}, Max: {max(val)}'
        
if __name__ == '__main__':
    WebsiteStats.run()