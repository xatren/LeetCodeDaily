class MyCalendarTwo(object):
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        # Check for triple booking
        for i, j in self.overlaps:
            if start < j and end > i:
                return False  # Triple booking is not allowed
        
        # Check for overlaps with existing bookings
        for i, j in self.bookings:
            if start < j and end > i:
                # There's an overlap, add it to overlaps
                self.overlaps.append((max(start, i), min(end, j)))
        
        # Add the new booking
        self.bookings.append((start, end))
        return True