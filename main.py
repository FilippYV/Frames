# 5 минут секса

class CoolingSystem:
    def __init__(self, thermal_paste, system_cooling):
        self.thermal_paste = thermal_paste
        self.system_cooling = system_cooling

    def install_cooling_system(self):
        if self.wearing_a_radiator() is True and self.cooling_connected() is True and self.tower_is_bolted() is True:
            install_cooling_system = True
        else:
            install_cooling_system = False
        print('Install_cooling_system ', install_cooling_system)
        return install_cooling_system

    def tower_is_bolted(self):
        if self.thermal_paste_is_applied() is True:
            tower_is_bolted = True
        else:
            tower_is_bolted = False
        print('Tower_is_bolted ', tower_is_bolted)
        return tower_is_bolted

    def wearing_a_radiator(self):
        if self.system_cooling is True:
            wearing_a_radiator = True
        else:
            wearing_a_radiator = False
        print('Wearing_a_radiator ', wearing_a_radiator)
        return wearing_a_radiator

    def cooling_connected(self):
        if self.system_cooling is True:
            cooler_connected = True
        else:
            cooler_connected = False
        print('Cooler_connected ', cooler_connected)
        return cooler_connected

    def thermal_paste_is_applied(self):
        if self.thermal_paste is True and self.system_cooling is True:
            thermal_paste_is_applied = True
        else:
            thermal_paste_is_applied = False
        print('Thermal_paste_is_applied ', thermal_paste_is_applied)
        return thermal_paste_is_applied


if __name__ == '__main__':
    thermal_paste = False
    system_cooling = True
    new_C = CoolingSystem(thermal_paste, system_cooling)
    print('\nTarget function', new_C.install_cooling_system())
