import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout
)

def test_invalid_car_type_branch():
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 0, False)

def test_valid_car_type_branch():
    assert annual_premium("hatchback", 30, 1, False) == 8000

def test_underage_driver_branch():
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 1, False)

def test_young_driver_branch():
    assert annual_premium("sedan", 20, 1, False) == 16000

def test_middle_age_driver_branch():
    assert annual_premium("sedan", 40, 1, False) == 12000

def test_senior_driver_branch():
    assert annual_premium("sedan", 60, 1, False) == 14000

def test_zero_claims_branch():
    assert annual_premium("sedan", 30, 0, False) == 9600

def test_one_claim_branch():
    assert annual_premium("sedan", 30, 1, False) == 12000

def test_more_than_two_claims_branch():
    assert annual_premium("sedan", 30, 3, False) == 24000

def test_anti_theft_true_branch():
    assert annual_premium("sedan", 30, 1, True) == 11500

def test_anti_theft_false_branch():
    assert annual_premium("sedan", 30, 1, False) == 12000

def test_negative_years_branch():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)

def test_five_years_branch():
    assert no_claim_bonus(5) == 50

def test_three_years_branch():
    assert no_claim_bonus(3) == 35

def test_one_year_branch():
    assert no_claim_bonus(1) == 20

def test_zero_years_branch():
    assert no_claim_bonus(0) == 0

def test_negative_damage_branch():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)

def test_negative_deductible_branch():
    with pytest.raises(ValueError):
        claim_payout(5000, 50000, -1000, False)

def test_valid_amounts_branch():
    assert claim_payout(5000, 50000, 1000, False) == 4000

def test_total_loss_branch():
    assert claim_payout(30000, 50000, 1000, True) == 50000

def test_not_total_loss_branch():
    assert claim_payout(5000, 50000, 1000, False) == 4000

def test_damage_within_deductible_branch():
    assert claim_payout(500, 50000, 1000, False) == 0

def test_damage_above_deductible_branch():
    assert claim_payout(5000, 50000, 1000, False) == 4000

def test_payout_exceeds_insured_value_branch():
    assert claim_payout(60000, 50000, 1000, False) == 50000

def test_payout_within_insured_value_branch():
    assert claim_payout(10000, 50000, 1000, False) == 9000