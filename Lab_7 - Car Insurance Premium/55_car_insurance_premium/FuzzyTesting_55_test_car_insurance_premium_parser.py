from hypothesis import given, strategies as st
from car_insurance_premium_parser import (
    normalize_registration,
    total_claim_amount,
    driver_age,
)

@given(st.text() | st.none())
def test_normalize_registration_no_crash(s):
    try:
        result = normalize_registration(s)
        assert isinstance(result, str)
    except Exception as e:
        assert False, f"normalize_registration crashed on {s!r} with: {e}"

@given(st.text() | st.none())
def test_total_claim_amount_no_crash(s):
    try:
        result = total_claim_amount(s)
        assert isinstance(result, int)
    except Exception as e:
        assert False, f"total_claim_amount crashed on {s!r} with: {e}"

@given(st.text() | st.none())
def test_driver_age_no_crash(s):
    try:
        result = driver_age(s)
        assert result is None or isinstance(result, int)
    except Exception as e:
        assert False, f"driver_age crashed on {s!r} with: {e}"