max_network_attempts = 4  # After that fail the network once (kind of real world scenario)
alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    global max_network_attempts
    max_network_attempts -= 1
    if (max_network_attempts == 0):
        max_network_attempts = 4
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


def test_alert():
        alert_in_celcius(400.5)
        assert(alert_failure_count == 0)
        alert_in_celcius(303.6)
        assert(alert_failure_count == 0)
        alert_in_celcius(400.5)
        assert(alert_failure_count == 0)
        alert_in_celcius(303.6)
        assert(alert_failure_count > 0) # Bad network reached

print(f'{alert_failure_count} alerts failed.')
test_alert()
print('All is well (maybe!)')
