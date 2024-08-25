import math

class Polygon:
    def __init__(self, n, R, length:'how many ploygons'=1):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._length = length
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
    
    # Making Class an iterable
    def __iter__(self):
        return self.PolygonIterator(self)
        
    class PolygonIterator:
        """
            Inner class that makes the Polygon class an iterable
            Parameter: It expects a Polygon object as a parameter
        """
        def __init__(self, polygon_obj) -> None:
            self.polygon_obj = polygon_obj
            self._index = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= self.polygon_obj._length:
                raise StopIteration
            else:
                result = self.polygon_obj
                self._index += 1
                return result