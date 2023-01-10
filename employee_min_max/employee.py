from mrjob.job import MRJob

class EmployeeStats(MRJob):
    
    def mapper(self, key, value):
        try:
            id, _, _, sal, dept_id = value.split(',')
            yield int(dept_id), float(sal)
        except ValueError:
            pass
        
    def reducer(self, key, values):
        val = list(values)
        yield f'Department ID {key}', f'Max: ${max(val)}, Min: ${min(val)}'
        
if __name__ == '__main__':
    EmployeeStats.run()