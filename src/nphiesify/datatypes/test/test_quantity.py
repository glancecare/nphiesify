import json
import pytest
from nphiesify.datatypes.complextypes import (
    Decimal,
    Quantity1,
    Quantity2,
)

from pydantic import ValidationError

from nphiesify.codesystems.codesets import (
    parse_code,
    parse_url,
    parse_string,
)


class TestQuantity1:
    def test_all_data(self):
        with pytest.raises(ValidationError):
            _ = Quantity1(
                value=Decimal(10.1),
                comparator=parse_code("Patient"),
                unit=parse_string("Weight"),
                system=parse_url("http://nphies.sa/license/payer-license"),
                code=parse_code("weight"),
            )

    def test_valid_data(self):
        qty1 = Quantity1(
            value=Decimal(10.1),
            comparator=parse_code("Patient"),
            system=parse_url("http://nphies.sa/license/payer-license"),
            code=parse_code("weight"),
        )
        qty1_json = '{"value":10.1,"comparator":"Patient","unit":null,"system":"http://nphies.sa/license/payer-license","code":"weight"}'

        qty2 = Quantity1(
            value=Decimal(10.1),
            comparator=parse_code("Patient"),
            unit=parse_string("Weight"),
        )
        qty2_json = '{"value":10.1,"comparator":"Patient","unit":"Weight","system":null,"code":null}'

        assert qty1 == Quantity1(**json.loads(qty1_json)) and qty2 == Quantity1(
            **json.loads(qty2_json)
        )

    def test_data_from_json(self):
        qty1 = Quantity1(
            value=Decimal(10.1),
            comparator=parse_code("Patient"),
            system=parse_url("http://nphies.sa/license/payer-license"),
            code=parse_code("weight"),
        )

        qty2_json = json.loads(
            '{"value":10.1,"comparator":"Patient","unit":null,"system":"http://nphies.sa/license/payer-license","code":"weight"}'
        )
        qty2 = Quantity1(**qty2_json)

        assert qty1 == qty2


class TestQuantity2Type:
    def test_valid_data(self):
        qty1 = Quantity2(
            value=Decimal(10.1),
            comparator=parse_code("Patient"),
            system=parse_url("http://nphies.sa/license/payer-license"),
            code=parse_code("weight"),
        )

        qty2_json = json.loads(
            '{"value":10.1,"comparator":"Patient","system":"http://nphies.sa/license/payer-license","code":"weight"}'
        )
        qty2 = Quantity2(**qty2_json)

        assert qty1 == qty2

    def test_min_data(self):
        with pytest.raises(ValidationError):
            _ = Quantity2(
                value=Decimal(10.1),
                comparator=parse_code("Patient"),
            )
