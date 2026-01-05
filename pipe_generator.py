from pygame import time

class PipeGenerator():
    def __init__(self, interval: int):
        #time in ms between spawning of pipes
        self.interval = interval
        
        #start a clock
        self.clock = time.Clock()

    def update(self):
        if self.clock >= self.interval:
            #spawn a pipe
            self.clock.tick