import pytest
import json
from nphiesify.datatypes.complextypes import Attachment, DateTime, Base64Binary
from pydantic import ValidationError

from nphiesify.codesystems.codesets import (
    parse_code,
    parse_url,
    parse_positiveint,
    parse_string,
)


class TestAttachmentType:
    # Test if no url and no data
    def test_no_url_no_data(self):
        with pytest.raises(ValidationError):
            _ = Attachment(
                contentType=parse_code("Report"),
                language=parse_code("English"),
                title=parse_string("Report"),
                creation=DateTime("2021-07-15T11:56:59.976+00:00"),
            )

    # Test if no data and url
    def test_url_with_missing_attr(self):
        with pytest.raises(ValidationError):
            _ = Attachment(
                contentType=parse_code("Report"),
                language=parse_code("English"),
                title=parse_string("Report"),
                creation=DateTime("2021-07-15T11:56:59.976+00:00"),
                url=parse_url("http://nphies.sa/license/payer-license"),
            )

    # Test valid data
    def test_valid_data(self):
        attachment = Attachment(
            contentType=parse_code("Report"),
            language=parse_code("English"),
            title=parse_string("Report"),
            creation=DateTime("2021-07-15T11:56:59.976+00:00"),
            url=parse_url("http://nphies.sa/license/payer-license"),
            size=parse_positiveint(2),
            hash=Base64Binary("SGVsbG8gdGhlcmU="),
        )

        json_str = '{"contentType": "Report", "language": "English", "data": null, "url": "http://nphies.sa/license/payer-license", "size": 2, "hash": "SGVsbG8gdGhlcmU=", "title": "Report", "creation": "2021-07-15T11:56:59.976+00:00"}'

        attachment2 = Attachment(**json.loads(json_str))

        assert attachment == attachment2
