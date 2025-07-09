import salabim as sim

sim.yieldless(False)

class ProcessData(sim.Component):
    def __init__(self, data):
        super().__init__()
        self.data = data
  
    def process(self):
        print(f'Processing {self.data}...')
        # simulate operation
        yield self.hold(10)
        print(f'{self.data} processed')
        result = self.data * 2
        print(f'Result: {result}')


env = sim.Environment()

print('start processing')
ProcessData('archivo.txt').activate()

env.run()