# Smart Home Device Control System


class Device:
    def __init__(self, device_id, status):
        self.device_id = device_id
        self.status = status

    def turn_on(self):
        self.status = "on"
        return f"Device {self.device_id} is now {self.status}"

    def turn_off(self):
        self.status = "off"
        return f"Device {self.device_id} is now {self.status}"


class SmartDevice(Device):
    def __init__(self, device_id, status, connectivity):
        super().__init__(device_id, status)
        self.connectivity = connectivity
        self.connected = False

    def connect(self):
        if self.status == "on":
            self.connected = True
            return f"Device {self.device_id} is now connected via {self.connectivity}"
        else:
            return f"Turn on {self.device_id} first to connect."


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, status, connectivity, temperature = 50):
        super().__init__(device_id, status, connectivity)
        self.temperature = temperature
    
    def set_temperature(self, temp):
        if temp <= self.temperature:
            return self.turn_on()
        else:
            return self.turn_off()
        
    def display_info(self):
        return f"Device ID: {self.device_id}\nStatus: {self.status}\nConnectivity: {self.connectivity}"    
       
      

obj = SmartThermostat("thermostat1", "on", "Wi-Fi")
# print(obj.turn_on())
print(obj.connect())
obj.set_temperature(50)
print(obj.display_info())
