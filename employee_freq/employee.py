from mrjob.job import MRJob

class EmployeeStats(MRJob):
    
    def mapper(self, key, value):
        try:
            _, _, _, dept_id = value.split(',')
            yield int(dept_id), 1
        except ValueError:
            pass
        
    def reducer(self, key, values):
        yield f'Department ID {key}', f'No. of employees: {sum(values)}'
        
if __name__ == '__main__':
    EmployeeStats.run()