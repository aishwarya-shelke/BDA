from mrjob.job import MRJob
from re import compile

WORD_RE = compile(r"[\w']+")

class WordCount(MRJob):

    def mapper(self, key, value):
        for word in WORD_RE.findall(value):
            yield word.lower(), 1
    
    def reducer(self, key, values):
        yield key, sum(values)
        
if __name__ == '__main__':
    WordCount.run()