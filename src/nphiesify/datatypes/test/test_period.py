import json
import pytest

from nphiesify.datatypes.complextypes import DateTime, Period


class TestPeriod:
    def test_wrong_datetime_format(self):
        with pytest.raises(ValueError):
            _ = DateTime("23/01/23")

    def test_valid_data_from_str(self):
        start_date = DateTime("2023-01-23T21:56:57.024682")
        end_date = DateTime("2023-01-23T21:56:57.024682")
        period = Period(start=start_date, end=end_date)
        json_str = '{"start": "2023-01-23T21:56:57.024682", "end": "2023-01-23T21:56:57.024682"}'
        assert period == Period(**json.loads(json_str))

    def test_valid_data_from_date(self):
        start_date = DateTime(year=2023, month=1, day=23)
        end_date = DateTime(year=2023, month=1, day=23)
        period = Period(start=start_date, end=end_date)
        json_str = '{"start": "2023-01-23T00:00:00", "end": "2023-01-23T00:00:00"}'
        assert period == Period(**json.loads(json_str))
