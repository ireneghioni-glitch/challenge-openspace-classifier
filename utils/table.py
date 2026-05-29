class Seat:

    def __init__(self, free=True, occupant=None):
        self.free = free
        self.occupant = occupant
    
    def __str__(self):
        if self.free:
            return "This seat is empty."
        else:
            return f'{self.occupant}'
    
    def set_occupant(self, name):
        """allows to assign a seat to someone if it's free (True)"""
        if self.free:
            self.occupant = name
            self.free = False
            
    def remove_occupant(self):
        """removes someone from a seat.
        returns the name of the person occupying the seat before"""
        if not self.free:
            previous_occupant = self.occupant
            self.occupant = None
            self.free = True
            return previous_occupant


class Table:

    def __init__(self, capacity=4):
        """definition of table obj attributes:
        capacity --> int
        seats --> list of Seats() obj (size = capacity)"""
        self.capacity = capacity
        self.seats = [Seat() for _ in range(self.capacity)]
    
    def __str__(self):
        return f'{", ".join(str(seat) for seat in self.seats)}.'
    
    def has_free_spot(self):
        """returns True if a spot is available"""
        for seat in self.seats:
            if seat.free:
                return seat.free
        return False
    
    def assign_seat(self, name):
        """places someone at the table"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break
    
    def left_capacity(self):
        """returns updated table capacity as an int"""
        return sum(seat.free for seat in self.seats)