from app import check_health

def test_health_check_success():
    assert check_health('https://httpstat.us/200') == True

def test_health_check_fail():
    assert check_health('https://httpstat.us/500') == False
