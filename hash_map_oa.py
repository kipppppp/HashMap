# This file implements a HashMap Class that can be used to
# store key-value pairs. A DynamicArray is used as the underlying data
# storage. Open addressing and quadratic probing is utilized to manage
# collisions.

from GIVEN_DATA_STRUCTURES import (DynamicArray, HashEntry, hash_function_1, hash_function_2)


class HashMapOA:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        NOT ORIGINAL
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        NOT ORIGINAL
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number to find the closest prime number
        NOT ORIGINAL
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        NOT ORIGINAL
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        NOT ORIGINAL
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        NOT ORIGINAL
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates the key-value pair in the given HashMap.
        If the key already exists, only the value is updated.
        Args:
            key
            value
        Returns:
            None
        """
        if self.table_load() >= 0.5:
            self.resize_table(2 * self._capacity)

        idx_initial = self._hash_function(key) % self._capacity
        idx = idx_initial
        x = 1
        while self._buckets[idx] is not None:
            if self._buckets[idx].key == key and not self._buckets[idx].is_tombstone:
                self._buckets[idx].value = value
                return
            elif self._buckets[idx].is_tombstone:
                self._buckets[idx].key = key
                self._buckets[idx].value = value
                self._buckets[idx].is_tombstone = False
                self._size += 1
                return
            idx = (idx_initial + (x**2)) % self._capacity
            x += 1

        self._buckets[idx] = HashEntry(key, value)
        self._size += 1

    def table_load(self) -> float:
        """
        Returns the load factor of the HashMap.
        (Number of elements) / (Number of buckets).
        Returns:
            Load factor
        """
        return round(self._size / self._capacity, 2)

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the HashMap.
        """
        return self._capacity - self._size

    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the underlying DynamicArray of the given HashMap.
        The new capacity must be a prime number greater than the current
        number of elements in the HashMap.
        All key-value pairs are rehashed.
        Args:
            new_capacity: New DynamicArray length
        Returns:
            None
        """
        cap = new_capacity
        if cap < self._size:
            return

        while not self._is_prime(cap):
            cap = self._next_prime(cap)

        key_value_da = self.get_keys_and_values()
        self._capacity = cap
        self.clear()

        for x in range(key_value_da.length()):
            self.put(key_value_da[x][0], key_value_da[x][1])

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key, else None.
        Args:
            key: Key to find
        Returns:
            Value if key found, else None
        """
        idx_initial = self._hash_function(key) % self._capacity
        idx = idx_initial
        x = 1
        while self._buckets[idx] is not None and x < self._capacity:
            if self._buckets[idx].key == key and not self._buckets[idx].is_tombstone:
                return self._buckets[idx].value
            idx = (idx_initial + (x**2)) % self._capacity
            x += 1
        return

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the HashMap, else False.
        An empty HashMap returns False.
        Args:
            key: Key to find
        Returns:
            bool: True if found, else False
        """
        idx_initial = self._hash_function(key) % self._capacity
        idx = idx_initial
        x = 1
        while self._buckets[idx] is not None and x < self._capacity:
            if self._buckets[idx].key == key and not self._buckets[idx].is_tombstone:
                return True
            idx = (idx_initial + (x ** 2)) % self._capacity
            x += 1
        return False

    def remove(self, key: str) -> None:
        """
        Remove the given key-value pair from the given HashMap.
        If the key does not exist, this method does nothing.
        Args:
            key: Key-Value pair to be removed
        Returns:
            None
        """
        idx_initial = self._hash_function(key) % self._capacity
        idx = idx_initial
        x = 1
        while self._buckets[idx] is not None and x < self._capacity:
            if self._buckets[idx].key == key and not self._buckets[idx].is_tombstone:
                self._buckets[idx].is_tombstone = True
                self._size -= 1
                return
            idx = (idx_initial + (x**2)) % self._capacity
            x += 1
        return

    def clear(self) -> None:
        """
        Clears the entire HashMap contents without changing the capacity.
        """
        self._buckets = DynamicArray()
        for x in range(self._capacity):
            self._buckets.append(None)
        self._size = 0

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a DynamicArray where each element is a tuple of (key,
        value) pair from the given HashMap.
        Returns:
            target_da
        """
        target_da = DynamicArray()
        for x in range(self._capacity):
            if self._buckets[x] is not None and not self._buckets[x].is_tombstone:
                target_tuple = self._buckets[x].key, self._buckets[x].value
                target_da.append(target_tuple)
        return target_da

    def __iter__(self):
        """
        Return the iterator.
        """
        self._index = 0
        # Track number of elements to return
        self._progress = self._capacity - self.empty_buckets()

        return self

    def __next__(self):
        """
        Obtain the next node and advance the iterator.
        """
        if self._progress <= 0:
            raise StopIteration

        self._index += 1

        # Find next active value
        while self._buckets[self._index] is None or self._buckets[self._index].is_tombstone:
            self._index += 1

        # Update element tracker
        self._progress -= 1
        return self._buckets[self._index]
