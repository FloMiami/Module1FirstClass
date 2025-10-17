from device import Device
from device_interface import DeviceInterface

class ManagedDevice(Device, DeviceInterface):
    def __init__(self, name, ip_address, os, location, status, compliance_status, technician):
        super().__init__(name, ip_address, os, location, status)
        self.compliance_status = compliance_status
        self.technician = technician

    def assign_technician(self, name):
        self.technician = name
        print(f"Technician assigned: {self.technician}")

    def print_properties(self):
        print("Managed Device Properties:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")