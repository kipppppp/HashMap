# This file implements a HashMap Class that can be used to
# store key-value pairs. A DynamicArray is used as the underlying data
# storage, while a LinkedList is utilized to manage collisions.


from GIVEN_DATA_STRUCTURES import (DynamicArray, LinkedList, hash_function_1)


class HashMapSC:
    def __init__(self, capacity: int = 11, function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        NOT ORIGINAL
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

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
        Increment from given number and the find the closest prime number
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
        Updates the key-value pair in the given hashmap.
        If the key already exists, only the value is updated.
        Else, a new key-value is added.
        Args:
            key
            value
        Returns:
            None
        """
        if self.table_load() >= 1.0:
            self.resize_table(2 * self._capacity)

        idx = self._hash_function(key) % self._capacity
        target = self._buckets[idx].contains(key)

        if target:
            target.value = value
        else:
            self._buckets[idx].insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the HashMap.
        Returns:
            counter: Number of empty buckets
        """
        counter = 0
        for x in range(self._capacity):
            if not self._buckets[x].length():
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        Returns the load factor of the HashMap.
        (Number of elements) / (Number of buckets).
        Returns:
            Load factor
        """
        return round(self._size / self._capacity, 2)

    def clear(self) -> None:
        """
        Clears the entire HashMap contents without changing the capacity.
        """
        self._buckets = DynamicArray()
        for x in range(self._capacity):
            self._buckets.append(LinkedList())
        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes underlying DynamicArray of the given HashMap.
        The new capacity must be a prime number and greater than 1.
        All key-value pairs are rehashed.
        Args:
            new_capacity: New DynamicArray length
        Returns:
            None
        """
        cap = new_capacity
        if cap < 1:
            return

        while not self._is_prime(cap):
            cap = self._next_prime(cap)

        key_value_da = self.get_keys_and_values()

        self._capacity = cap
        self.clear()

        for x in range(key_value_da.length()):
            self.put(key_value_da[x][0], key_value_da[x][1])

    def get(self, key: str):
        """
        Returns the value associated with the given key, else None.
        Args:
            key: Key to find
        Returns:
            target: Value if key found, else None
        """
        idx = self._hash_function(key) % self._capacity
        target = self._buckets[idx].contains(key)
        if target:
            return target.value
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
        idx = self._hash_function(key) % self._capacity
        if self._size == 0 or self._buckets[idx].contains(key) is None:
            return False
        return True

    def remove(self, key: str) -> None:
        """
        Remove the given key-value pair from the given HashMap.
        If the key does not exist, this method does nothing.
        Args:
            key: Key-value pair to be removed
        Returns:
            None
        """
        idx = self._hash_function(key) % self._capacity

        val = self._buckets[idx].remove(key)
        if val:
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a DynamicArray where each element is a tuple of (key, value)
        pair from the given HashMap.
        Returns:
            target_da
        """
        target_da = DynamicArray()
        for x in range(self._capacity):
            for node in self._buckets[x]:
                target_tuple = node.key, node.value
                if target_tuple[0] is not None:
                    target_da.append(target_tuple)
        return target_da


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Returns a tuple containing (DynamicArray of mode values, frequency).
    Only returns the highest frequency values.
    O(n) time complexity.
    Args:
        da: DynamicArray
    Returns:
        tuple: (DynamicArray of mode values, frequency)
    """
    map = HashMapSC()

    # Create HashMap of (Key, value-count) pairs
    for x in range(da.length()):
        if map.contains_key(da[x]):
            val = map.get(da[x])
            map.put(da[x], 1 + val)
        else:
            map.put(da[x], 1)

    target_da = DynamicArray()
    current_frequency = 0

    # Create array of (key, value-count) pairs
    count_da = map.get_keys_and_values()

    for x in range(count_da.length()):
        if count_da[x][1] > current_frequency:
            current_frequency = count_da[x][1]
            target_da = DynamicArray()
            target_da.append(count_da[x][0])
        elif count_da[x][1] == current_frequency:
            target_da.append(count_da[x][0])

    return target_da, current_frequency
