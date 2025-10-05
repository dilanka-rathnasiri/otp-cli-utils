from dataclasses import dataclass, field

import pytest

from otp_cli_utils.services.otp_services import get_windows_for_time_period


@dataclass
class CaseDto:
    time_period: int
    expected: int
    test_id: str = field(init=False)

    def __post_init__(self):
        self.test_id = f"time period = {self.time_period}s, expected window count = {self.expected}"


exact_windows_time_periods_test_cases = [
    CaseDto(30, 0),
    CaseDto(60, 1),
    CaseDto(120, 3),
    CaseDto(0, -1),
]

non_multiples_windows_time_periods_test_cases = [
    CaseDto(31, 0),
    CaseDto(59, 0),
    CaseDto(121, 3),
]

test_cases = (
    exact_windows_time_periods_test_cases
    + non_multiples_windows_time_periods_test_cases
)

test_cases_arg_values = [(i.time_period, i.expected) for i in test_cases]

test_cases_ids = [i.test_id for i in test_cases]


@pytest.mark.parametrize(
    argnames="time_period, expected",
    argvalues=test_cases_arg_values,
    ids=test_cases_ids,
)
def test_window_count_calculation(time_period, expected):
    """
    Test the function with various time periods to verify window count calculation
    """
    assert get_windows_for_time_period(time_period) == expected
