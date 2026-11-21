
def estimate_delivery(distance_km, speed_kmh=30):
    return (distance_km / speed_kmh) * 60


def test_delivery_estimate():
    assert estimate_delivery(10) == 20


def test_zero_distance():
    assert estimate_delivery(0) == 0

def test_intentional_failure():
    assert 2 + 2 == 5
