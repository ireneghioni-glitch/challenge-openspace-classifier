import random # imports random library
from utils.table import Table # imports Table class from table.py file in utils dir

class Openspace:
    # creation of Openspace calss

    def __init__(self, number_of_tables=6):
        """definition of openspace obj attributes:
        tables --> list of Table() ogj
        number_of_tables --> int"""
        self.number_of_tables = number_of_tables
        self.tables = [Table() for _ in range(self.number_of_tables)]
    
    def __str__(self):
        occupied_openspace = []
        for index, table in enumerate(self.tables):
            seated = [seat.occupant if seat.occupant != None else "This seat is empty." for seat in table.seats]
            # preparates for display of seated people at a single table
            if not all(seat.occupant for seat in table.seats): # eneterd only if all elements in seated list are none
                occupied_table = f'Table {index + 1} is not occupied by anyone.'
            else:
                occupied_table = f'Table {index + 1} is occupied by: {", ".join(seated)}'
            occupied_openspace.append(occupied_table) # for display of whole openspace situation
        return f'This openspace contains {self.number_of_tables} tables.\n{"\n".join(occupied_openspace)}'
    
    def organize(self, names):
        """randomly assigns people to Seat() obj in different Table() obj"""
        colleagues = names.copy() # made a list of names copy to work on, so the code will work also after the very first run
        random.shuffle(colleagues) # random sorting of elements in names list
        for table in self.tables:
            while table.left_capacity() > 0:
                if not colleagues:
                    return # makes the program exit the whole method, no more iteration through tables as soon as names reaches 0 elements
                table.assign_seat(colleagues.pop()) # assignin removed person to the table

    def display(self):
        """displays the tables occupation situation in a nice way"""
        return str(self) # returns the output of the __str__() method
    
    def store(self, filename):
        """stores the repartition in a file"""
        with open(filename, "w") as openspace_report:
            openspace_report.write(str(self))