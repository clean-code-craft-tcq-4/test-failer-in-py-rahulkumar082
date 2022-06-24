from network_helper_pkg.network_ok_count import NETWORK_OK_COUNT
from abc import ABC, abstractmethod

class network(ABC):
    @abstractmethod
    def network_alert(self, celcius):
        pass

class network_real(network):
    def __init__(self):
        self.max_network_attempts = NETWORK_OK_COUNT
        self.network_ok = 200
        self.network_not_ok = 500
    
    def network_alert(self, celcius):
        # Do some socket magic in real time
        pass

class network_stub(network):
    def __init__(self):
        self.max_network_attempts = NETWORK_OK_COUNT
        self.network_ok = 200
        self.network_not_ok = 500

    def network_alert(self, celcius):
        print(f'ALERT: Temperature is {celcius} celcius')
        self.max_network_attempts -= 1
        if (self.max_network_attempts == 0):
            self.bad_network_fix()
            return self.network_not_ok
        return self.network_ok

    def bad_network_fix(self):
        self.fix_network()
    
    def fix_network(self):
        self.max_network_attempts = NETWORK_OK_COUNT