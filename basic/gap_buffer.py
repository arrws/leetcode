import numpy as np

class GapBuffer: 
    def __init__(self, max_gap: int = 10):
        self.max_gap = max_gap
        self.buffer = np.empty(2 * max_gap, dtype=object)
        self.a = 0
        self.b = len(self.buffer)

    def _gap(self):
        gap = self.b - self.a
        if gap == 0:
            # Resize buffer and shift elements after b
            old_len = len(self.buffer)
            self.buffer.resize(old_len + self.max_gap)
            # Move elements after b to make room for gap
            self.buffer[self.b + self.max_gap:] = self.buffer[self.b:old_len]
            self.b += self.max_gap

    def move(self, steps: int):
        if steps > 0:
            # Move right: copy characters from after gap to gap start
            self.buffer[self.a:self.a+steps] = self.buffer[self.b:self.b+steps]
        else:
            # Move left: copy characters from before gap to gap end
            self.buffer[self.b+steps:self.b] = self.buffer[self.a+steps:self.a]
        self.a += steps
        self.b += steps

    def insert(self, ch):
        self.buffer[self.a] = ch
        self.a += 1
        self._gap()

    def show(self):
        return np.concatenate([self.buffer[:self.a], self.buffer[self.b:]])


# Tests
if __name__ == "__main__":
    # Test basic insertion
    gb = GapBuffer()
    gb.insert('H')
    gb.insert('e')
    gb.insert('l')
    gb.insert('l')
    gb.insert('o')
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "Hello", f"Expected 'Hello', got '{result}'"
    print("✓ Basic insertion test passed")
    
    # Test cursor movement and insertion
    gb = GapBuffer()
    gb.insert('A')
    gb.insert('B')
    gb.insert('C')
    gb.move(-2)  # Move cursor back 2 positions
    gb.insert('X')
    gb.insert('Y')
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "AXYBC", f"Expected 'AXYBC', got '{result}'"
    print("✓ Cursor movement test passed")
    
    # Test moving to beginning
    gb = GapBuffer()
    gb.insert('1')
    gb.insert('2')
    gb.insert('3')
    gb.move(-3)  # Move to beginning
    gb.insert('0')
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "0123", f"Expected '0123', got '{result}'"
    print("✓ Move to beginning test passed")
    
    # Test buffer growth (trigger _gap)
    gb = GapBuffer(max_gap=3)
    for i in range(10):
        gb.insert(str(i))
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "0123456789", f"Expected '0123456789', got '{result}'"
    print("✓ Buffer growth test passed")
    
    # Test complex movement
    gb = GapBuffer()
    gb.insert('A')
    gb.insert('B')
    gb.insert('C')
    gb.insert('D')
    gb.insert('E')
    gb.move(-3)  # Cursor at position 2
    gb.insert('X')
    gb.move(2)   # Move right 2
    gb.insert('Y')
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "ABXCDYE", f"Expected 'ABXCDYE', got '{result}'"
    print("✓ Complex movement test passed")
    
    # Test moving forward
    gb = GapBuffer()
    gb.insert('A')
    gb.insert('B')
    gb.insert('C')
    gb.move(-2)  # Move back to position 1
    gb.move(1)   # Move forward to position 2
    gb.insert('X')
    result = ''.join(str(c) for c in gb.show() if c is not None)
    assert result == "ABXC", f"Expected 'ABXC', got '{result}'"
    print("✓ Forward movement test passed")
    
    print("\nAll tests passed!")
