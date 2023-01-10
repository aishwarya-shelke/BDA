from mrjob.job import MRJob

class Electricity(MRJob):
    
    def mapper(self, _, line):
        try:
            record = line.split(',')
            for key in record[1:-1]:
                yield int(record[0]), int(key)
        except ValueError:
            pass
            
    def reducer(self, key, values):
        val = list(values)
        yield key, f'Max: {max(val)}, Min: {min(val)}'

if __name__ == '__main__':
    Electricity.run()
