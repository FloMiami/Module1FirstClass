from abc import ABC, abstractmethod

class DeviceInterface(ABC):
    @abstractmethod
    def print_properties(self):
        pass