from mrjob.job import MRJob
from re import compile

class WordCount(MRJob):

    def mapper(self, key, value):
        for word in value.split(','):
            yield word.lower(), 1
    
    def reducer(self, key, values):
        yield key, sum(values)
        
if __name__ == '__main__':
    WordCount.run()