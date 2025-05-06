import re
import json
import datetime
from dateutil import parser
from decimal import Decimal
from typing import Optional, Union, Any

from pydantic import (
    StringConstraints,
    Base64Str,
    ConfigDict,
    GetCoreSchemaHandler,
)
from pydantic_core import CoreSchema, core_schema


from nphiesify.datatypes.basetypes import PrimitiveType


Boolean = bool


class String(str, PrimitiveType):
    __fhir_type_name__: Optional[str] = "string"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(str)
        )


class Decimal(float, PrimitiveType):
    __fhir_type_name__: Optional[str] = "decimal"

    regex = re.compile(r"-?(0|[1-9][0-9]{0,17})(\.[0-9]{1,17})?([eE][+-]?[0-9]{1,9}})?")

    @classmethod
    def to_string(cls, value):
        """ """
        assert isinstance(value, Union[float, int, Decimal])
        return str(float(value))

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(float)
        )


class Url(String, PrimitiveType):
    """
    various types, e.g.
    "http:
    //somewhere.com/.../Resource/id"
    "mailto: name@domain.com"
    "urn: oid: 2.14.113344.2.15.12349876"
    """

    __fhir_type_name__: Optional[str] = "url"
    regex = re.compile(r"\S*")
    max_length = 255

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(String)
        )


class Uri(String, PrimitiveType):
    """
    various types, e.g.
    "Patient"
    "urn: uuid: 125371..."
    "urn: oid: 2.14.113344.2.15.12349876"
    """

    __fhir_type_name__: Optional[str] = "uri"
    regex = re.compile(r"\S*")
    max_length = 255

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(String)
        )


class Canonical(String, PrimitiveType):
    """
    A URI that refers to a resource by its canonical URL (resources with a url property).
    The canonical type differs from a uri in that it has special meaning in this specification,
    and in that it may have a version appended, separated by a vertical bar (|).
    Note that the type canonical is not used for the actual canonical URLs that are the target
    of these references, but for the URIs that refer to them, and may have the version suffix in them.
    Like other URIs, elements of type canonical may also have #fragment references. Unlike other URIs,
    canonical URLs are never relative - they are either absolute URIs, or fragment identifiers
    """

    __fhir_type_name__: Optional[str] = "canonical"
    regex = re.compile(r"\S*")
    max_length = 255

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(String)
        )


class Id(String, PrimitiveType):
    """
    Field Structure: Set of numbers and letters up to 64 characters
    """

    regex = re.compile(r"[A-Za-z0-9\-\.]{1,64}")
    min_length = 1
    max_length = 64
    __fhir_type_name__: Optional[str] = "id"

    def __init__(self, *args, **kwargs):
        value = args[0]
        self.__validate(value)
        StringConstraints.__init__(self)

    def __validate(self, value):
        if type(value) not in [String, str]:
            raise TypeError("Value of Id should be a string")
        if not value:
            raise ValueError("Value of Id cannot be empty")
        elif len(value) > 64:
            raise ValueError("Id should not be more than 64 charecters")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(String)
        )


class Code(String, PrimitiveType):
    """
    Indicates that the value is taken from a set of controlled strings defined
    elsewhere (see Using codes for further discussion). Technically, a code is
    restricted to a string which has at least one character and no leading or
    trailing whitespace, and where there is no whitespace other than single
    spaces in the contents
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    __fhir_type_name__: Optional[str] = "code"
    max_length = 30
    regex = re.compile(r"^[^\s]+(\s[^\s]+)*$")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(String)
        )


class Date(datetime.date, PrimitiveType):
    """YYYY-MM-DD"""

    __fhir_type_name__: Optional[str] = "date"
    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2]"
        r"[0-9]|3[0-1]))?)?"
    )

    def __new__(self, *args, **kwargs):
        if not args and not kwargs:
            raise ValueError("Date cannot be empty")
        if (
            len(args) == 1
            and isinstance(args[0], str)
            and not self.regex.match(args[0])
        ):
            raise ValueError("Date has to be in YYYY-MM-DD format")

        if len(args) == 1 and isinstance(args[0], str):
            d = parser.parse(args[0])
            return super().__new__(self, year=d.year, month=d.month, day=d.day)
        elif isinstance(len(args) == 1 and args[0], datetime.date):
            d = args[0]
            return super().__new__(self, year=d.year, month=d.month, day=d.day)
        return super().__new__(self, *args, **kwargs)

    def json(self):
        return json.dumps(self.isoformat())

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(datetime.date)
        )


class DateTime(datetime.datetime, PrimitiveType):
    """YYYY-MM-DDThh: mm: ss+zz: zz"""

    __fhir_type_name__: Optional[str] = "dateTime"
    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|"
        r"60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00)))?)?)?"
    )

    def __new__(self, *args, **kwargs):
        if not args and not kwargs:
            raise ValueError("Date cannot be empty")
        if (
            len(args) == 1
            and isinstance(args[0], str)
            and not self.regex.match(args[0])
        ):
            print("Date error occured")
            raise ValueError(
                "Date format has to foolow YYYY-MM-DDThh: mm: ss+zz: zz format"
            )

        if len(args) == 1 and isinstance(args[0], str):
            d = parser.parse(args[0])
            return super().__new__(
                self,
                year=d.year,
                month=d.month,
                day=d.day,
                hour=d.hour,
                minute=d.minute,
                second=d.second,
                microsecond=d.microsecond,
                tzinfo=d.tzinfo,
            )
        elif isinstance(len(args) == 1 and args[0], datetime.datetime):
            d = args[0]
            return super().__new__(
                self,
                year=d.year,
                month=d.month,
                day=d.day,
                hour=d.hour,
                minute=d.minute,
                second=d.second,
                microsecond=d.microsecond,
                tzinfo=d.tzinfo,
            )
        return super().__new__(self, *args, **kwargs)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(datetime.datetime)
        )


class Instant(DateTime):
    __fhir_type_name__: Optional[str] = "instant"


class Base64Binary(Base64Str, PrimitiveType):
    """A stream of bytes, base64 encoded (RFC 4648 )"""

    regex = re.compile(r"^(\s*([0-9a-zA-Z+=]){4}\s*)+$")
    __fhir_type_name__ = "base64Binary"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(Base64Str)
        )


class Integer(int, PrimitiveType):
    """A signed integer in the range −2,147,483,648..2,147,483,647
    (32-bit; for larger values, use decimal)"""

    regex = re.compile(r"-?([0]|([1-9][0-9]*))")
    __fhir_type_name__ = "integer"

    @classmethod
    def to_string(cls, value):
        """ """
        assert isinstance(value, int)
        return str(value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(int)
        )


class Integer64(Integer):
    """A signed integer in the range -9,223,372,036,854,775,808
    to +9,223,372,036,854,775,807 (64-bit).
    This type is defined to allow for record/time counters
    that can get very large"""

    regex = re.compile(r"[0]|[-+]?[1-9][0-9]*")
    __fhir_type_name__ = "integer64"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(Integer)
        )


class Markdown(StringConstraints, PrimitiveType):
    """A FHIR string (see below) that may contain markdown syntax for
    optional processing by a markdown presentation engine, in the GFM
    extension of CommonMark format (see below)"""

    regex = re.compile(r"\s*(\S|\s)*")
    __fhir_type_name__ = "markdown"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(StringConstraints)
        )


class Xhtml(str, PrimitiveType):
    """XHTML with rules as defined below. No extensions are possible,
    and the id property becomes and xml:id on the root element which
    is an xhtml div"""

    __fhir_type_name__ = "xhtml"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(str)
        )


class Oid(StringConstraints, PrimitiveType):
    """
    An OID represented as a URI (RFC 3001 icon); e.g. urn:oid:1.2.3.4.5
    """

    __fhir_type_name__: Optional[str] = "oid"
    regex = re.compile(r"urn:oid:[0-2](\.(0|[1-9][0-9]*))+")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(StringConstraints)
        )


class Uuid(StringConstraints, PrimitiveType):
    """
    A UUID (aka GUID) represented as a URI (RFC 4122 icon); e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520
    """

    __fhir_type_name__: Optional[str] = "uuid"
    regex = re.compile(
        r"urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    )

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls, handler.generate_schema(StringConstraints)
        )
