class Hardware:
    def __init__(self, battery: str = "battery,", motherboard: str = "motherboard,", touchscreen: str = "touchscreen", camera: str = "camera") -> None:
        super().__init__()
        self.battery: str = battery
        self.motherboard: str = motherboard
        self.touchscreen: str = touchscreen
        self.camera: str = camera
    def printAll(self) -> None:
        print(f"phone components: \n{self.battery}\n{self.motherboard}\n{self.touchscreen}\n{self.camera}")

class Software:
    def __init__(self, app1: str = "Settings,", app2: str = "Files,", app3: str = "Calculator", app4: str = "Messenger") -> None:
        super().__init__()
        self.app1: str = app1
        self.app2: str = app2
        self.app3: str = app3
        self.app4: str = app4
    def printAll(self) -> None:
        print(f"phone apps: \n{self.app1}\n{self.app2}\n{self.app3}\n{self.app4}")
        

