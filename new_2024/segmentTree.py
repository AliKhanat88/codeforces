class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)   # Segment tree array
        self.lazy = [0] * self.n         # Lazy propagation array (only half size)
        
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]  # Initialize leaves
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]  # Internal nodes

    def range_update(self, l, r, value):
        """Update range [l, r) by adding 'value'."""
        l += self.n
        r += self.n
        l0, r0 = l, r  # Save original l and r for updating lazy values

        # Update nodes in the range
        while l < r:
            if l & 1:
                self.tree[l] += value
                if l < self.n:
                    self.lazy[l] += value  # Mark lazy
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] += value
                if r < self.n:
                    self.lazy[r] += value  # Mark lazy
            l //= 2
            r //= 2

        # Update parents
        self._propagate_up(l0)
        self._propagate_up(r0 - 1)

    def _propagate_up(self, pos):
        """Propagate changes up the tree to maintain correct values."""
        while pos > 1:
            pos //= 2
            self.tree[pos] = (
                self.tree[2 * pos] + self.tree[2 * pos + 1] + self.lazy[pos]
            )

    def query(self, l, r):
        """Query range [l, r) for the sum."""
        self._apply_lazy_updates(l + self.n)
        self._apply_lazy_updates(r + self.n - 1)

        l += self.n
        r += self.n
        result = 0

        while l < r:
            if l & 1:
                result += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                result += self.tree[r]
            l //= 2
            r //= 2
        return result

    def _apply_lazy_updates(self, pos):
        """Apply any pending lazy updates downwards."""
        shift = pos.bit_length() - 1  # Number of shifts needed to reach root
        for s in range(shift, 0, -1):
            i = pos >> s
            if self.lazy[i] != 0:
                self.tree[2 * i] += self.lazy[i]
                self.tree[2 * i + 1] += self.lazy[i]

                if 2 * i < self.n:
                    self.lazy[2 * i] += self.lazy[i]
                    self.lazy[2 * i + 1] += self.lazy[i]
                
                self.lazy[i] = 0  # Clear lazy at current node
