import pytest
import json
from nphiesify.datatypes.complextypes import Coding, Url, Code, String

from pydantic import ValidationError

from nphiesify.codesystems.codesets import parse_url


class TestCoding:
    def test_valid_data(self, valid_full_url):
        cc = Coding(
            system=Url(valid_full_url), code=Code("PRC"), display=String("Iqama")
        )
        expected_result = {
            "system": parse_url(valid_full_url),
            "code": "PRC",
            "display": "Iqama",
        }
        assert cc == Coding(**expected_result)

    def test_required_fields(self, valid_full_url):
        with pytest.raises(ValidationError):
            _ = Coding(
                system=valid_full_url,
            )

    def test_extra_fields(self, valid_full_url):
        with pytest.raises(ValidationError):
            _ = Coding(
                system=valid_full_url, code="PRC", display="Iqama", extra="More Value"
            )

    def test_json_encoding(self, valid_full_url):
        cc = Coding(system=valid_full_url, code="PRC", display="Iqama")
        json_str = '{"id":null,"extension":null,"system":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db","code":"PRC","version":null,"display":"Iqama","userSelected":null}'
        assert cc.model_dump_json() == json_str

    def test_json_decoding(self, valid_full_url):
        json_str = json.loads(
            '{"id":null,"extension":null,"system":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db","code":"PRC","version":null,"display":"Iqama","userSelected":null}'
        )
        cc = Coding(system=valid_full_url, code="PRC", display="Iqama")
        assert cc == Coding(**json_str)
