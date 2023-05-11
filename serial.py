"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initialize a new serial number generator with a starting value."""
        self.start = start
        self.next_serial = start

    def generate(self):
        """Return the next serial number and update the generator."""
        result = self.next_serial
        self.next_serial += 1
        return result

    def reset(self):
        """Reset the generator to the initial state."""
        self.next_serial = self.start
