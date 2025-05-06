import json
import pytest
from nphiesify.datatypes.complextypes import (
    Url,
    Ref1,
    Ref2a,
    Ref2b,
    Ref3a,
    Ref3b,
    Ref4,
    IdentifierA,
    IdentifierB,
    Coding,
    CodeableConcept,
)

from pydantic import ValidationError

from nphiesify.codesystems.codesets import parse_url


class TestRef1Type:
    def test_valid_value(self, valid_full_url):
        ref = Ref1(reference=valid_full_url)
        expected_result = {
            "reference": parse_url(valid_full_url),
        }
        assert ref == Ref1(**expected_result)

    def test_no_value(self):
        with pytest.raises(ValidationError):
            _ = Ref1()

    def test_mail_url(self):
        url = "mailto:hello@world.com"
        ref = Ref1(reference=url)
        expected_result = {
            "reference": parse_url(url),
        }
        assert ref == Ref1(**expected_result)

    def test_urn_url(self):
        url = "urn:uuid:a7e4caf2-0441-40e5-97d2-5ae180275111"
        ref = Ref1(reference=url)
        expected_result = {
            "reference": parse_url(url),
        }
        assert ref == Ref1(**expected_result)

    def test_json_encoding(self, valid_full_url):
        ref = Ref1(reference=valid_full_url)
        assert (
            ref.model_dump_json()
            == '{"id":null,"extension":null,"reference":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db"}'
        )

    def test_json_decoding(self, valid_full_url):
        ref = Ref1(reference=valid_full_url)
        json_str = json.loads(
            '{"id":null,"extension":null,"reference":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db"}'
        )
        assert ref == Ref1(**json_str)


class TestRef2aType:
    def test_valid_value(self, valid_full_url):
        c = Coding(system=valid_full_url, code="PRC", display="Iqama")
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref2a(identifier=identifier)

        json_str = json.loads(
            '{"identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001", "type":{"coding":[{"system":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db","code":"PRC","display":"Iqama"}]}}}'
        )
        assert ref == Ref2a(**json_str)


class TestRef2bType:
    def test_valid_value(self, valid_full_url):
        c = Coding(system=valid_full_url, code="PRC", display="Iqama")
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref2b(type="Organization", identifier=identifier)

        json_str = json.loads(
            '{"type":"Organization","identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001","type":{"coding":[{"system":"http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db","code":"PRC","display":"Iqama"}]}}}'
        )
        assert ref == Ref2b(**json_str)

    def test_missing_type(self, valid_full_url):
        c = Coding(system=valid_full_url, code="PRC", display="Iqama")
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )

        with pytest.raises(ValidationError):
            _ = Ref2b(identifier=identifier)


class TestRef3aType:
    def test_valid_value(self):
        identifier = IdentifierA(
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref3a(identifier=identifier)

        json_str = json.loads(
            '{"identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001"}}'
        )
        assert ref == Ref3a(**json_str)


class TestRef3bType:
    def test_valid_value(
        self,
    ):
        identifier = IdentifierA(
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref3b(type="Organization", identifier=identifier)

        json_str = json.loads(
            '{"type":"Organization","identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001"}}'
        )
        assert ref == Ref3b(**json_str)

    def test_missing_type(self, valid_full_url):
        c = Coding(system=valid_full_url, code="PRC", display="Iqama")
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )

        with pytest.raises(ValidationError):
            _ = Ref3b(identifier=identifier)


class TestRef4Type:
    def test_valid_data(self):
        json_str = json.loads(
            '{"type":"Patient","identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001","type":{"coding":[{"system":"http://nphies.sa/license/payer-license","code":"PRC","display":"Iqama"}]}},"display":"Mr. Ahmed"}'
        )
        c = Coding(
            system=parse_url("http://nphies.sa/license/payer-license"),
            code="PRC",
            display="Iqama",
        )
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref4(type="Patient", identifier=identifier, display="Mr. Ahmed")
        assert ref == Ref4(**json_str)

    def test_minimum_required_data(self):
        with pytest.raises(ValidationError):
            _ = Ref4()

    def test_with_diplay_data(self):
        json_str = json.loads('{"display":"Mr. Ahmed"}')
        ref = Ref4(display="Mr. Ahmed")
        assert ref == Ref4(**json_str)

    def test_with_identifier_and_type_data(self):
        json_str = json.loads(
            '{"type":"Patient","identifier":{"system":"http://nphies.sa/license/payer-license","value":"N-I-00001","type":{"coding":[{"system":"http://nphies.sa/license/payer-license","code":"PRC","display":"Iqama"}]}}}'
        )
        c = Coding(
            system=parse_url("http://nphies.sa/license/payer-license"),
            code="PRC",
            display="Iqama",
        )
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        ref = Ref4(type="Patient", identifier=identifier)
        assert ref == Ref4(**json_str)

    def test_with_identifier_but_not_type_data(self):
        c = Coding(
            system=parse_url("http://nphies.sa/license/payer-license"),
            code="PRC",
            display="Iqama",
        )
        cc = CodeableConcept(coding=[c])
        identifier = IdentifierB(
            type=cc,
            system=parse_url("http://nphies.sa/license/payer-license"),
            value="N-I-00001",
        )
        with pytest.raises(ValidationError):
            _ = Ref4(identifier=identifier)
