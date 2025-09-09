# class RingBuffer:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.len = 0
#         self.buffer = [None] * capacity
#         self.wp = 0
#         self.rp = 0
#
#     def _next(self, x):
#         return (x + 1) % self.capacity
#
#     def write(self, data):
#         if self.wp == self.rp and self.len > 0:
#             raise Exception("buffer full")
#         self.buffer[self.wp] = data 
#         self.wp = self._next(self.wp)
#         self.len += 1
#
#     def read(self):
#         if self.len == 0:
#             raise Exception("buffer empty")
#         data = self.buffer[self.rp]
#         self.rp = self._next(self.rp)
#         self.len -= 1
#         return data
#
#     def read_segment(self, p):
#         if self.len == 0:
#             raise Exception("buffer empty")
#
#         if p > self.len:
#             p = self.len
#
#         q = self.rp + p
#         from_front = q % len(self.buffer) if q > self.len else None
#         to_end = min(len(self.buffer), q)
#
#         segm = self.buffer[self.rp : to_end]
#         if from_front:
#             segm += self.buffer[:from_front]
#
#         self.rp = from_front if from_front else to_end
#         self.len -= p
#         return segm
#
#     def length(self):
#         return self.len


class RingArr():

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity

    def __getitem__(self, key):
        key = key % self.capacity
        return self.data[key]

    def __setitem__(self, key, value):
        key = key % self.capacity
        self.data[key] = value
    
    def __len__(self):
        return self.capacity


class RingBuffer: # smarter

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = RingArr(capacity)
        self.wp = 0
        self.rp = 0

    def write(self, data):
        if self.wp - self.rp == len(self.buffer):
            raise Exception("buffer full")
        self.buffer[self.wp] = data 
        self.wp += 1

    def read(self):
        if self.wp == self.rp:
            raise Exception("buffer empty")
        data = self.buffer[self.rp]
        self.rp += 1
        return data

    def read_segment(self, p):
        if self.wp == self.rp:
            raise Exception("buffer empty")
        p = min(p, self.wp - self.rp)
        segm = [self.buffer[self.rp + i] for i in range(p)]
        self.rp += p
        return segm
    
    def length(self):
        return self.wp - self.rp

if __name__ == "__main__":
    # Basic read/write
    buf = RingBuffer(3)
    buf.write("a")
    buf.write("b")
    assert buf.read() == "a"
    assert buf.read() == "b"
    print("✓ Basic read/write")

    # Empty buffer
    buf = RingBuffer(3)
    try:
        buf.read()
        assert False
    except Exception as e:
        assert str(e) == "buffer empty"
    print("✓ Empty buffer")

    # Full buffer
    buf = RingBuffer(3)
    buf.write("a")
    buf.write("b")
    buf.write("c")
    try:
        buf.write("d")
        assert False
    except Exception as e:
        assert str(e) == "buffer full"
    print("✓ Full buffer")

    # Wrap around
    buf = RingBuffer(3)
    buf.write(1)
    buf.write(2)
    buf.read()
    buf.write(3)
    assert buf.read() == 2
    assert buf.read() == 3
    print("✓ Wrap around")

    # Length tracking
    buf = RingBuffer(4)
    assert buf.length() == 0
    buf.write("a")
    buf.write("b")
    assert buf.length() == 2
    buf.read()
    assert buf.length() == 1
    print("✓ Length tracking")

    # Test read_segment basic
    buf = RingBuffer(5)
    buf.write("a")
    buf.write("b")
    buf.write("c")
    buf.write("d")
    result = buf.read_segment(2)
    assert result == ["a", "b"]
    assert buf.length() == 2
    result = buf.read_segment(2)
    assert result == ["c", "d"]
    assert buf.length() == 0
    print("✓ read_segment basic")

    # Test read_segment with wrap around
    buf = RingBuffer(3)
    buf.write(1)
    buf.write(2)
    buf.write(3)
    buf.read()  # Remove 1
    buf.write(4)  # Wrap around
    result = buf.read_segment(3)
    assert result == [2, 3, 4]
    assert buf.length() == 0
    print("✓ read_segment wrap around")

    # Test read_segment requesting more than available
    buf = RingBuffer(5)
    buf.write("x")
    buf.write("y")
    result = buf.read_segment(10)  # Request 10 but only 2 available
    assert result == ["x", "y"]
    assert buf.length() == 0
    print("✓ read_segment more than available")

    # Test read_segment on empty buffer
    buf = RingBuffer(3)
    try:
        buf.read_segment(1)
        assert False
    except Exception as e:
        assert str(e) == "buffer empty"
    print("✓ read_segment on empty")

    # Test read_segment with high counter values (wrap multiple times)
    buf = RingBuffer(3)
    for i in range(10):
        buf.write(i)
        buf.read()
    buf.write(100)
    buf.write(101)
    buf.write(102)
    result = buf.read_segment(3)
    assert result == [100, 101, 102]
    print("✓ read_segment with high counters")

    # Test partial read_segment
    buf = RingBuffer(4)
    buf.write("A")
    buf.write("B")
    buf.write("C")
    result = buf.read_segment(1)
    assert result == ["A"]
    assert buf.length() == 2
    result = buf.read_segment(1)
    assert result == ["B"]
    assert buf.length() == 1
    print("✓ read_segment partial reads")

    print("\nAll tests passed!")
