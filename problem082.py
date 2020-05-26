# Problem #82
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
#
# For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".


class File:

    # create a file with some hardcoded text
    def __init__(self):
        self.path = "files\\problem082.txt"
        # control the reading start
        self.offset = 0

        self._open("w")
        self.file.write("Hello world! This is the problem #82")
        self._close()

    # open the file
    def _open(self, mode="r"):
        self.file = open(self.path, mode)

    # close the file
    # open and close file are made like this, because when i need to read multiple times i can open and close once
    def _close(self):
        self.file.close()

    # read 7 character
    def _read7(self):
        # set the start
        self.file.seek(self.offset)
        message = self.file.read(7)
        # add to the offset to control the start
        self.offset += 7
        return message

    def read7(self):
        self._open()
        message = self._read7()
        self._close()
        return message

    def readN(self, n):
        full_message = ""

        self._open()

        # if the n is bigger, calculate how many times you need to read7
        repetition = n // 7
        for _ in range(repetition):
            message = self._read7()
            full_message += message

        # if needed to read the rest
        part = n % 7
        if part <= 7:
            message = self._read7()
            # read 7, but take only part of it
            full_message += message[:part]
            self.offset -= 7 - part

        self._close()

        return full_message


file = File()

print(file.read7())
print(file.readN(1))
print(file.readN(3))
print(file.readN(10))
print(file.read7())
print(file.read7())

print()

file = File()
print(file.readN(50))

# i am not used to file handling, so i spent most time studying how to use it. in total it took me one hour to do,
# but around 20 minutes coding the problem
