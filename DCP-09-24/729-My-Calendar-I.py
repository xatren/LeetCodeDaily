class MyCalendar(object):
    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        \\\
        :type start: int
        :type end: int
        :rtype: bool
        \\\
        for s, e in self.bookings:
            if s < end and start < e:
                return False
        self.bookings.append((start, end))
        self.bookings.sort()  # Keep the list sorted for efficient searching
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)