class Engine:
    def __init__(self):
        self.engine_type = "Electric"

    def start_engine(self):
        print(f"{self.engine_type} engine started.")

class NavigationSystem:
    def __init__(self):
        self.map_version = "2025.1"

    def navigate(self):
        print(f"Navigating using map version {self.map_version}.")

class SmartDrone(Engine, NavigationSystem):
    def __init__(self):
        Engine.__init__(self)
        NavigationSystem.__init__(self)
        self.drone_id = "X-99"

    def show_info(self):
        print(f"Drone ID:{self.drone_id}")
        print(f"Engine:{self.engine_type}")
        print(f"Map:{self.map_version}")

drone = SmartDrone()
drone.show_info()
drone.start_engine()
drone.navigate()