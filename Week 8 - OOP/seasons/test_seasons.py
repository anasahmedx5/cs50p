from datetime import date
from seasons import getMin

def test_getMin():
    assert getMin(date(2025, 3, 1), date(2025, 3, 1)) == 0
    assert getMin(date(2025, 2, 28), date(2025, 3, 1)) == 1440
    assert getMin(date(2024, 3, 1), date(2025, 3, 1)) == 525600
    assert getMin(date(2023, 3, 1), date(2024, 3, 1)) == 527040
    assert getMin(date(2015, 3, 1), date(2025, 3, 1)) == 5260320
