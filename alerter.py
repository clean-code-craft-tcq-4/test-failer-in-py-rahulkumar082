from network_helper_pkg.network_stub import network_stub
from test_package.test_alerter import test_alert

alert_failure_count = 0
network_stub_obj = network_stub()

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_stub_obj.network_alert_stub(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 0
    return alert_failure_count

test_alert_obj = test_alert()
test_alert_obj.test_alert_functionality(alert_in_celsius_func=alert_in_celcius)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
