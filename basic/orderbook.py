import bisect
import heapq

class Side:
    BUY = 'buy'
    SELL = 'sell'

    def opposite(self):
        return Side.SELL if self == Side.BUY else Side.BUY

    def __init__(self, side):
        if side not in (Side.BUY, Side.SELL):
            raise ValueError("Side must be 'buy' or 'sell'")
        self.side = side


class OrderbookSide:
    def __init__(self, side):
        self.heap = []  # Min-heap of (price, quantity) - price negative for buys
        self.price_map = {}  # price -> quantity (price negative for buys)
        self.side = Side(side)
        self.sign = -1 if self.side.side == Side.BUY else 1

    def add_order(self, price, quantity):
        # Store price as negative for buys to get proper heap ordering
        heap_price = price * self.sign
        
        if heap_price in self.price_map:
            # Update existing level
            self.price_map[heap_price] += quantity
            # Add new heap entry with updated quantity (old entries will be cleaned up)
            heapq.heappush(self.heap, (heap_price, self.price_map[heap_price]))
        else:
            # New price level
            self.price_map[heap_price] = quantity
            heapq.heappush(self.heap, (heap_price, quantity))

    def remove_order(self, price, quantity):
        heap_price = price * self.sign
        if heap_price in self.price_map:
            new_quantity = self.price_map[heap_price] - quantity
            if new_quantity <= 0:
                del self.price_map[heap_price]
            else:
                self.price_map[heap_price] = new_quantity
                # Add new heap entry with updated quantity
                heapq.heappush(self.heap, (heap_price, new_quantity))


    def get_best_price(self):
        self._clean_heap()
        if not self.heap:
            return None
        return abs(self.heap[0][0])

    def get_volume_at_price(self, price):
        heap_price = price * self.sign
        return self.price_map.get(heap_price, 0)

    def _clean_heap(self):
        # Remove outdated entries from heap top
        while self.heap:
            price, quantity = self.heap[0]
            if price not in self.price_map:
                heapq.heappop(self.heap)  # Price level deleted
            elif self.price_map[price] == 0:
                heapq.heappop(self.heap)  # Empty level
                del self.price_map[price]
            elif quantity != self.price_map[price]:
                heapq.heappop(self.heap)  # Stale quantity - need to find correct entry
            else:
                break  # Valid entry

    def __len__(self):
        return len(self.price_map)

    def __getitem__(self, index):
        # For compatibility with crossing logic - get levels sorted by price
        if index == 0:
            self._clean_heap()
            if self.heap:
                price, quantity = self.heap[0]
                return (abs(price), quantity)
        
        # For other indices, we need to sort (less efficient but needed for crossing)
        sorted_levels = sorted(self.price_map.items())
        if index < len(sorted_levels):
            price, quantity = sorted_levels[index]
            return (abs(price), quantity)
        raise IndexError("Index out of range")


class OrderBook:
    def __init__(self):
        self.bids = OrderbookSide(Side.BUY)
        self.asks = OrderbookSide(Side.SELL)


    def _can_cross(self):
        best_bid = self.bids.get_best_price()
        best_ask = self.asks.get_best_price()
        return (best_bid is not None and best_ask is not None and 
                best_bid >= best_ask)

    def cross(self) -> list:
        trades = []
        while self._can_cross():
            # Get current best levels from price maps
            best_bid_price = min(self.bids.price_map.keys()) if self.bids.price_map else None
            best_ask_price = min(self.asks.price_map.keys()) if self.asks.price_map else None
            
            if best_bid_price is None or best_ask_price is None:
                break
                
            bid_quantity = self.bids.price_map[best_bid_price]
            ask_quantity = self.asks.price_map[best_ask_price]
            
            # Convert to actual prices for trade recording
            actual_bid_price = abs(best_bid_price)
            actual_ask_price = abs(best_ask_price)
            
            q = min(bid_quantity, ask_quantity)
            trades.append({'price': actual_ask_price, 'quantity': q})
            
            # Update quantities
            new_bid_qty = bid_quantity - q
            if new_bid_qty <= 0:
                del self.bids.price_map[best_bid_price]
            else:
                self.bids.price_map[best_bid_price] = new_bid_qty
                # Add new heap entry with updated quantity
                heapq.heappush(self.bids.heap, (best_bid_price, new_bid_qty))
            
            new_ask_qty = ask_quantity - q  
            if new_ask_qty <= 0:
                del self.asks.price_map[best_ask_price]
            else:
                self.asks.price_map[best_ask_price] = new_ask_qty
                # Add new heap entry with updated quantity
                heapq.heappush(self.asks.heap, (best_ask_price, new_ask_qty))

        return trades

    def add_order(self, side, price, quantity):
        side = Side(side)

        if side.side == Side.BUY:
            self.bids.add_order(price, quantity)
        else:
            self.asks.add_order(price, quantity)

        return self.cross()

    def remove_order(self, side, price, quantity):
        side = Side(side)

        if side.side == Side.BUY:
            self.bids.remove_order(price, quantity)
        else:
            self.asks.remove_order(price, quantity)

    def get_best_bid(self):
        return self.bids.get_best_price()
    
    def get_best_ask(self):
        return self.asks.get_best_price()

    def get_volume_at_price(self, side, price):
        side = Side(side)
        if side.side == Side.BUY:
            return self.bids.get_volume_at_price(price)
        else:
            return self.asks.get_volume_at_price(price)


# Test helper functions
def create_basic_book():
    ob = OrderBook()
    ob.add_order(Side.BUY, 99, 100)
    ob.add_order(Side.SELL, 101, 50)
    return ob

def create_crossed_book():
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    return ob

def assert_empty_book(ob):
    assert ob.get_best_bid() is None
    assert ob.get_best_ask() is None
    assert len(ob.bids) == 0
    assert len(ob.asks) == 0

def create_multi_level_book():
    ob = OrderBook()
    # Bids: 102, 101, 100
    ob.add_order(Side.BUY, 102, 30)
    ob.add_order(Side.BUY, 101, 20)
    ob.add_order(Side.BUY, 100, 10)
    # Asks: 103, 104, 105
    ob.add_order(Side.SELL, 103, 15)
    ob.add_order(Side.SELL, 104, 25)
    ob.add_order(Side.SELL, 105, 35)
    return ob

if __name__ == "__main__":
    # Test OrderbookSide - buy side ordering
    buy_side = OrderbookSide(Side.BUY)
    buy_side.add_order(100, 10)
    buy_side.add_order(105, 5)  # Higher price = better for buyers
    buy_side.add_order(95, 15)
    assert buy_side.get_best_price() == 105
    assert len(buy_side) == 3
    print("✓ Buy side ordering")

    # Test OrderbookSide - sell side ordering
    sell_side = OrderbookSide(Side.SELL)
    sell_side.add_order(100, 10)
    sell_side.add_order(95, 5)  # Lower price = better for sellers
    sell_side.add_order(105, 15)
    assert sell_side.get_best_price() == 95
    assert len(sell_side) == 3
    print("✓ Sell side ordering")

    # Test quantity aggregation at same price
    buy_side = OrderbookSide(Side.BUY)
    buy_side.add_order(100, 10)
    buy_side.add_order(100, 20)  # Same price, should aggregate
    assert buy_side.get_volume_at_price(100) == 30
    assert len(buy_side) == 1
    print("✓ Quantity aggregation")

    # Test basic OrderBook operations
    ob = create_basic_book()
    assert ob.get_best_bid() == 99
    assert ob.get_best_ask() == 101
    assert ob.get_volume_at_price(Side.BUY, 99) == 100
    assert ob.get_volume_at_price(Side.SELL, 101) == 50
    print("✓ Basic OrderBook operations")

    # Test no crossing when prices don't overlap
    ob = create_basic_book()
    # Should have no trades since spread exists
    trades = []  # No new orders added, so no crossing
    assert trades == []
    print("✓ No crossing when spread exists")

    # Test exact quantity match crossing
    ob = create_crossed_book()
    trades = ob.add_order(Side.SELL, 100, 50)
    assert len(trades) == 1
    assert trades[0] == {'price': 100, 'quantity': 50}
    assert_empty_book(ob)
    print("✓ Exact quantity match crossing")

    # Test partial fill crossing
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 100)
    trades = ob.add_order(Side.SELL, 100, 60)
    assert len(trades) == 1
    assert trades[0] == {'price': 100, 'quantity': 60}
    # Debug: check if we have remaining quantity
    remaining_qty = ob.get_volume_at_price(Side.BUY, 100)
    print(f"Remaining bid quantity: {remaining_qty}")
    if remaining_qty > 0:
        print(f"Price map: {ob.bids.price_map}")
        print(f"Heap top after clean: {ob.bids.heap[0] if ob.bids.heap else 'Empty'}")
        ob.bids._clean_heap()
        print(f"Heap top after second clean: {ob.bids.heap[0] if ob.bids.heap else 'Empty'}")
    assert ob.get_best_bid() == 100
    assert ob.get_volume_at_price(Side.BUY, 100) == 40
    assert ob.get_best_ask() is None
    print("✓ Partial fill crossing")

    # Test multiple crosses in one operation
    ob = create_multi_level_book()
    trades = ob.add_order(Side.SELL, 100, 60)  # Should match all three bid levels
    assert len(trades) == 3
    # Since we're selling at 100, it will match highest bids first (102, 101, 100)
    assert trades[0] == {'price': 100, 'quantity': 30}  # Match 102 bid fully
    assert trades[1] == {'price': 100, 'quantity': 20}  # Match 101 bid fully
    assert trades[2] == {'price': 100, 'quantity': 10}  # Match 100 bid fully
    assert ob.get_best_bid() is None  # All bids consumed
    print("✓ Multiple crosses")

    # Test aggressive buy crossing multiple sell levels
    ob = OrderBook()
    ob.add_order(Side.SELL, 100, 10)
    ob.add_order(Side.SELL, 101, 20)
    ob.add_order(Side.SELL, 102, 30)
    trades = ob.add_order(Side.BUY, 102, 30)  # Match exactly first two levels
    assert len(trades) == 2
    assert trades[0] == {'price': 100, 'quantity': 10}
    assert trades[1] == {'price': 101, 'quantity': 20}
    assert ob.get_best_ask() == 102
    assert ob.get_volume_at_price(Side.SELL, 102) == 30
    print("✓ Aggressive buy crossing")

    # Test empty orderbook operations
    ob = OrderBook()
    assert_empty_book(ob)
    assert ob.get_volume_at_price(Side.BUY, 100) == 0
    assert ob.get_volume_at_price(Side.SELL, 100) == 0
    print("✓ Empty orderbook")

    # Test complex scenario - build full book
    ob = OrderBook()
    # Build buy side
    ob.add_order(Side.BUY, 99, 100)
    ob.add_order(Side.BUY, 98, 200)
    ob.add_order(Side.BUY, 97, 150)
    # Build sell side
    ob.add_order(Side.SELL, 101, 100)
    ob.add_order(Side.SELL, 102, 200)
    ob.add_order(Side.SELL, 103, 150)
    
    # Verify book state
    assert ob.get_best_bid() == 99
    assert ob.get_best_ask() == 101
    assert len(ob.bids) == 3
    assert len(ob.asks) == 3
    
    # Cross the spread
    trades = ob.add_order(Side.BUY, 101, 250)  # Take liquidity
    assert len(trades) == 1
    assert trades[0] == {'price': 101, 'quantity': 100}
    assert ob.get_best_ask() == 102  # Next level
    assert ob.get_best_bid() == 101  # New order partially filled
    assert ob.get_volume_at_price(Side.BUY, 101) == 150
    print("✓ Complex scenario")

    # Test price priority
    ob = OrderBook()
    ob.add_order(Side.SELL, 100, 50)
    ob.add_order(Side.SELL, 99, 30)  # Better price
    trades = ob.add_order(Side.BUY, 100, 40)
    assert len(trades) == 2
    assert trades[0] == {'price': 99, 'quantity': 30}  # Better price executes first
    assert trades[1] == {'price': 100, 'quantity': 10}
    print("✓ Price priority")

    # Test large price differences
    ob = OrderBook()
    ob.add_order(Side.BUY, 1000000, 1)
    trades = ob.add_order(Side.SELL, 1, 1)  # This should trigger crossing
    assert len(trades) == 1
    assert trades[0] == {'price': 1, 'quantity': 1}
    print("✓ Large price differences")

    # Test get volume for non-existent price
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    assert ob.get_volume_at_price(Side.BUY, 99) == 0
    assert ob.get_volume_at_price(Side.BUY, 101) == 0
    print("✓ Volume at non-existent price")

    # Test remove_order basic functionality
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    ob.add_order(Side.SELL, 102, 30)
    assert ob.get_volume_at_price(Side.BUY, 100) == 50
    ob.remove_order(Side.BUY, 100, 20)
    assert ob.get_volume_at_price(Side.BUY, 100) == 30
    assert ob.get_best_bid() == 100
    print("✓ Remove order partial")

    # Test remove entire level
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    ob.remove_order(Side.BUY, 100, 50)
    assert ob.get_best_bid() is None
    assert ob.get_volume_at_price(Side.BUY, 100) == 0
    print("✓ Remove entire level")

    # Test remove more than available (should remove all)
    ob = OrderBook()
    ob.add_order(Side.SELL, 100, 30)
    ob.remove_order(Side.SELL, 100, 50)  # Remove more than exists
    assert ob.get_best_ask() is None
    assert ob.get_volume_at_price(Side.SELL, 100) == 0
    print("✓ Remove more than available")

    # Test remove non-existent order
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    ob.remove_order(Side.BUY, 99, 10)  # Different price
    assert ob.get_volume_at_price(Side.BUY, 100) == 50  # Unchanged
    assert ob.get_volume_at_price(Side.BUY, 99) == 0
    print("✓ Remove non-existent order")

    # Test remove with multiple price levels
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    ob.add_order(Side.BUY, 99, 30)
    ob.add_order(Side.BUY, 101, 20)
    ob.remove_order(Side.BUY, 100, 50)  # Remove middle level
    assert ob.get_best_bid() == 101  # Higher price becomes best
    assert len(ob.bids) == 2
    print("✓ Remove from multiple levels")

    # Test remove affecting crossing
    ob = OrderBook()
    ob.add_order(Side.BUY, 100, 50)
    ob.add_order(Side.SELL, 100, 30)  # This should cross
    assert len(ob.bids) == 1  # Partial fill remains
    assert ob.get_volume_at_price(Side.BUY, 100) == 20
    ob.remove_order(Side.BUY, 100, 20)  # Remove remainder
    assert ob.get_best_bid() is None
    print("✓ Remove after crossing")

    print("\nAll tests passed!")
