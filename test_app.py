from app import check_health
def test_health_check_success():
    assert check_health('https://api.github.com') == True
