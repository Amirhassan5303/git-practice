from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color='Green'):
        print('Shape constructor called')
        self.color = color