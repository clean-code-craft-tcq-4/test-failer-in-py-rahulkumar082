from network_helper_pkg.network_ok_count import NETWORK_OK_COUNT
class network_stub:
    """
    This class is useful to stub network conditions. We are supposing that
    after max network attempts, we get atleast one bad network condition
    and return status 500
    """
    def __init__(self):
        self.max_network_attempts = NETWORK_OK_COUNT
        self.network_ok = 200
        self.network_not_ok = 500

    def network_alert_stub(self, celcius):
        print(f'ALERT: Temperature is {celcius} celcius')
        self.max_network_attempts -= 1
        if (self.max_network_attempts == 0):
            self.network_is_bad()
            return self.network_not_ok
        return self.network_ok

    def network_is_bad(self):
        self.fix_network()
    
    def fix_network(self):
        self.max_network_attempts = NETWORK_OK_COUNT