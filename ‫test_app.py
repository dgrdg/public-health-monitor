from app import check_health

def test_health_check_success():
    # این سایت همیشه وضعیت 200 دارد
    assert check_health("https://httpstat.us/200") == True

def test_health_check_fail():
    # این سایت همیشه وضعیت 500 دارد
    assert check_health("https://httpstat.us/500") == False
