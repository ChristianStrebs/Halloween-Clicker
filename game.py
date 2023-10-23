import time

class game:
    def __init__(self):
        self.presents = 0
        self.elves = 0
        self.santas = 0
        self.reindeers = 0
        self.sleighs = 0
        self.workshops = 0
        self.factories = 0

    def play(self):
        self.presents += self.elves
        self.presents += self.santas * 10
        self.presents += self.reindeers * 100
        self.presents += self.sleighs * 1000
        self.presents += self.workshops * 10000
        self.presents += self.factories * 100000
        time.sleep(1)
        self.play()

    def buy_elf(self):
        if self.presents >= self.elves + 10:
            self.presents -= 10
            self.elves += 1
    
    def buy_santa(self):
        if self.presents >= self.santas + 100:
            self.presents -= 100
            self.santas += 1

    def buy_reindeer(self):
        if self.presents >= self.reindeers + 1000:
            self.presents -= 1000
            self.reindeers += 1

    def buy_sleigh(self):
        if self.presents >= self.sleighs + 10000:
            self.presents -= 10000
            self.sleighs += 1

    def buy_workshop(self):
        if self.presents >= self.workshops + 100000:
            self.presents -= 100000
            self.workshops += 1

    def buy_factory(self):
        if self.presents >= self.factories + 1000000:
            self.presents -= 1000000
            self.factories += 1
    
    def save_christmas(self):
        if self.presents >= 1000000000:
            self.presents -= 10000000
            return True
        else:
            return False

    def get_presents(self):
        return self.presents
    
    def get_elves(self):
        return self.elves
    
    def get_santas(self):
        return self.santas
    
    def get_reindeers(self):
        return self.reindeers
    
    def get_sleighs(self):
        return self.sleighs
    
    def get_workshops(self):
        return self.workshops
    
    def get_factories(self):
        return self.factories
    
    def get_all(self):
        return self.presents, self.elves, self.santas, self.reindeers, self.sleighs, self.workshops, self.factories
    
    def set_all(self, presents, elves, santas, reindeers, sleighs, workshops, factories):
        self.presents = presents
        self.elves = elves
        self.santas = santas
        self.reindeers = reindeers
        self.sleighs = sleighs
        self.workshops = workshops
        self.factories = factories

    def clicked_tree(self):
        self.presents += 1
        
