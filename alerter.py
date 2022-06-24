from network_helper_pkg.network_status import network_stub

class alerter:
    def __init__(self) -> None:
        self.alert_failure_count = 0
        self.network_stub_obj = network_stub()

    def alert_in_celcius(self, farenheit):
        celcius = (farenheit - 32) * 5 / 9
        returnCode = self.network_stub_obj.network_alert(celcius)
        if returnCode != 200:
            self.alert_failure_count += 1
        return self.alert_failure_count
