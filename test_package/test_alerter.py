import random
from network_helper_pkg.network_ok_count import NETWORK_OK_COUNT
class test_alert:
    """
    Till NETWORK_OK_COUNT, we expect that network is working just
    fine, but after that, it fails. So alert_in_celsius_fun should
    return 1 then, as network code from network_stub is 500 (not-ok)
    """
    def test_alert_functionality(self, alert_in_celsius_func):
        for index in range(0, NETWORK_OK_COUNT-1):
            print_network_count_log(index, NETWORK_OK_COUNT)
            random_fahrenheit = round(random.uniform(10.0, 1000.0), 0)
            assert(alert_in_celsius_func(random_fahrenheit) == 0)
        # expect to fail this time
        random_fahrenheit = round(random.uniform(10.0, 1000.0), 0)
        assert(alert_in_celsius_func(random_fahrenheit) == 1)

def print_network_count_log(current_count, total_count):
    text = format_log(current_count, total_count)
    print(text)

def format_log(current_count, total_count):
    return f"""{total_count - current_count} retries left out of {total_count}\n
    Retrying..."""
