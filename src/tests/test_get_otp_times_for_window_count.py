from datetime import datetime, timedelta

from otp_cli_utils.services.otp_services import get_otp_times_for_window_count


def test_get_otp_times_for_window_count_zero():
    """
    Test the get_otp_times_for_window_count method with a window count of 0
    """
    now = datetime.now()
    result = get_otp_times_for_window_count(0)
    assert len(result) == 1
    assert now - result[0] < timedelta(seconds=1)


def test_get_otp_times_for_window_count_positive():
    """
    Test the get_otp_times_for_window_count method with a positive window count
    """
    window_count = 5
    now = datetime.now()
    result = get_otp_times_for_window_count(window_count)
    assert len(result) == window_count + 1
    for i, dt in enumerate(result):
        expected_dt = now - timedelta(seconds=30 * i)
        assert abs(expected_dt - dt) < timedelta(seconds=1)
