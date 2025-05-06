import json

from nphiesify.resources.foundation.other import Bundle


class TestBundle:
    def test_pre_auth_dentail_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/2a - First Preauth Dental Request with multiple items.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 8

    def test_pre_auth_institutional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/1 - Preauth Institutional Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 8

    def test_pre_auth_pharmacy_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/4 - Preauth Pharmacy Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 6

    def test_pre_auth_professional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/5a - Preauth Professional Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 7

    def test_pre_auth_vision_prescription_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/6 - Preauth Vision Prescription Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 9

    def test_claim_dental_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/7a - Claim Dental Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 8

    def test_claim_institutional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/8 - Claim Institutional Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 8

    def test_claim_pharmacy_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/9 - Claim Pharmacy Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 6

    def test_claim_professional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/10 - Claim Professional Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 7

    def test_claim_professional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/10 - Claim Professional Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 7

    def test_claim_professional_request(self):
        with open(
            "nphiesify/resources/foundation/test/mock/11 - Claim Vision Request.json"
        ) as jsonfile:
            data = json.load(jsonfile)
            m = Bundle(**data)
            assert len(m.entry) == 8
