class SimulationParameters():
    def __init__(self):
        self.fiber_length = 0.0
        self.peak_power = 0.0
        self.pulse_width = 0.0
        self.fiber = ''
        self.pulse_shape = ''


class Fiber():
    def __init__(self):
        self.loss = 0.0 #m-1
        self.betas = [] #beta2, beta3, beta4 ...
        self.gamma = 0.0 # W-1m-1
        

class NLSSolver():
    
