from typing import Optional, List, Union
from typing_extensions import Annotated

from pydantic import Field, model_validator, ConfigDict, PositiveInt

from nphiesify.datatypes.basetypes import Element

from nphiesify.datatypes.primitivetypes import (
    Base64Binary,
    Boolean,
    Code,
    Date,
    DateTime,
    Decimal,
    String,
    Uri,
    Url,
    Markdown,
)


class Attachment(Element):
    """
    Either .url must be supplied pointing to
    the attachment contents or .data must
    be supplied containing the attachment
    data
    """

    __fhir_type_name__: Optional[str] = "Attachment"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    contentType: Code = Field(
        ...,
        alias="contentType",
    )
    language: Optional[Code] = Field(
        None,
        alias="language",
    )
    data: Optional[Base64Binary] = Field(
        None,
        alias="data",
    )
    url: Optional[Url] = Field(
        None,
        alias="url",
    )
    size: Optional[PositiveInt] = Field(
        None,
        alias="size",
    )
    hash: Optional[Base64Binary] = Field(
        None,
        alias="hash",
    )
    title: String = Field(..., alias="title", max_length=250)
    creation: DateTime = Field(
        ...,
        alias="creation",
    )

    @model_validator(mode="before")
    def check_required_fields(cls, values):
        _data = values.get("data")
        _url = values.get("url")
        _size = values.get("size")
        _hash = values.get("hash")

        if not _data and not _url:
            raise ValueError("Either url or data must be present")
        elif _url and (not _size or not _hash):
            raise ValueError("size and hash should not be empty if url is given")

        return values


class Coding(Element):
    """
    A reference to a code defined by a terminology system
    + Warning: A Coding SHOULD NOT have a display unless a code is also present.
    Computation on Coding.display alone is generally unsafe.
    Consider using CodeableConcept.text
    """

    __fhir_type_name__: Optional[str] = "Coding"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    system: Url = Field(
        ...,
        alias="system",
    )
    code: Code = Field(
        ...,
        alias="code",
    )
    version: Optional[String] = Field(
        None,
        alias="version",
    )
    display: Optional[String] = Field(
        None,
        alias="display",
        max_length=100,
    )
    userSelected: Optional[Boolean] = Field(
        None,
        alias="userSelected",
    )

    @model_validator(mode="before")
    def validate_display(cls, values):
        if hasattr(cls, "_codeset") and "code" in values:
            _cls = cls._codeset.get_default()
            _codeset_obj = _cls(values["code"])
            if _codeset_obj and hasattr(_codeset_obj, "display"):
                values["display"] = _codeset_obj.display

            if _system_url := _cls.get_system_url():
                if "system" in values:
                    if values["system"] != _system_url:
                        raise ValueError(
                            f"Expecting system url as {_system_url} but received {values['system']}"
                        )
                values["system"] = _system_url

        return values


class CodeableConcept(Element):
    """Concept - reference to a terminology or just text"""

    __fhir_type_name__: Optional[str] = "CodeableConcept"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    coding: Optional[List[Coding]] = Field(
        None,
        alias="coding",
    )
    text: Optional[String] = Field(
        None,
        alias="text",
        max_length=100,
    )


class SimpleQuantity(Element):
    """The comparator is not used on a SimpleQuantity"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    value: Decimal = Field(
        ...,
        alias="value",
    )
    unit: Optional[String] = Field(
        None,
        alias="unit",
    )
    system: Optional[Uri] = Field(
        None,
        alias="system",
    )
    code: Optional[Code] = Field(
        None,
        alias="code",
    )


class QuantityBaseClass(Element):
    """A measured or measurable amount"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    value: Decimal = Field(
        ...,
        alias="value",
    )
    comparator: Optional[Code] = Field(
        None,
        alias="comparator",
    )


class Quantity1(QuantityBaseClass):
    """Used to identify a quantity value only"""

    __fhir_type_name__: Optional[str] = "Quantity1"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    unit: Optional[String] = Field(
        None,
        alias="unit",
    )
    system: Optional[Uri] = Field(
        None,
        alias="system",
    )
    code: Optional[Code] = Field(
        None,
        alias="code",
    )

    @model_validator(mode="before")
    def check_required_fields(cls, values):
        _system = values.get("system")
        _code = values.get("code")
        _unit = values.get("unit")

        if _unit and _system and _code:
            raise ValueError(
                "Either unit or (system and code) shall be provided, not both."
            )
        if not _unit and (not _system or not _code):
            raise ValueError("Either unit or (system and code) shall be provided.")
        return values


class Quantity2(QuantityBaseClass):
    """
    Used to identify a quantity value and the
    additional mandatory attributes
    Example: Claim.item.productOrService
    (medication quantity)
    """

    __fhir_type_name__: Optional[str] = "Quantity2"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    system: Uri = Field(
        ...,
        alias="system",
    )
    code: Code = Field(
        ...,
        alias="code",
    )


class Money(Element):
    """An amount of economic utility in some recognized currency"""

    __fhir_type_name__: Optional[str] = "Money"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    value: Decimal = Field(
        ...,
        alias="value",
        description="Numerical value (with implicit precision)",
    )
    currency: Code = Field(
        ...,
        alias="currency",
        description="ISO 4217 Currency Code",
    )


class Range(Element):
    """Set of values bounded by low and high"""

    __fhir_type_name__: Optional[str] = "Range"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    low: Optional[SimpleQuantity] = Field(
        None,
        alias="low",
        description="Low limit",
    )
    high: Optional[SimpleQuantity] = Field(
        None,
        alias="high",
        description="High limit",
    )


class IdentifierBaseClass(Element):
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    system: Uri = Field(
        ...,
        alias="system",
    )
    value: String = Field(..., alias="value", max_length=50)


class IdentifierA(IdentifierBaseClass):
    """
    Used to list the business identifier of the
    resource.
    Example (resource): claim
    """

    __fhir_type_name__: Optional[str] = "Identifier.a"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Optional[CodeableConcept] = Field(
        None,
        alias="type",
    )


class IdentifierB(IdentifierBaseClass):
    """
    A business unique identifier to identify a
    well-known entity based on the
    identification standards adopted by
    NPHIES
    Example: Patient. Identifier (Iqama or
    Saudi Health ID).
    """

    __fhir_type_name__: Optional[str] = "Identifier.b"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    # as used for patient, provider, payer, etc....
    type: CodeableConcept = Field(
        ...,
        alias="type",
    )


class Ref1(Element):
    """
    Reference using the full URL where the
    reference resource will be included
    within the bundle
    """

    __fhir_type_name__: Optional[str] = "Ref.1"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    reference: Url = Field(
        ...,
        alias="reference",
    )


class Ref2Base(Element):
    """Abstract Class for both Ref2a and Ref2b"""

    __fhir_type_name__: Optional[str] = "Ref.2"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    identifier: IdentifierB = Field(
        ...,
        alias="identifier",
    )


class Ref2a(Ref2Base):
    """
    It is used when providing well known
    identifiers rather than including a
    resource when there is only one valid
    resource type. It is used to reference a
    known identifier for clearly stated
    resource. Identifier captured within
    NPHIES registries
    Example: reference (Organization)
    """

    __fhir_type_name__: Optional[str] = "Ref.2a"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Optional[Uri] = Field(
        None,
        alias="type",
    )


class Ref2b(Ref2Base):
    """
    It is used when providing well known
    identifiers rather than including a
    resource when there is a choice of
    resource types. It is used to reference a
    known identifier for a choice of
    resources. Identifier captured within
    NPHIES registries.
    Example: Reference(Organization | Practitioner)
    """

    __fhir_type_name__: Optional[str] = "Ref.2b"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Uri = Field(
        ...,
        alias="type",
    )


class Ref3Base(Element):
    """Abstract Class for both Ref3a and Ref3b"""

    __fhir_type_name__: Optional[str] = "Ref.3"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    identifier: IdentifierA = Field(
        ...,
        alias="identifier",
    )


class Ref3a(Ref3Base):
    """
    It is used when providing the business
    identifier for a resource. (claim,
    eligibility, prescription, referral,) when
    there is only one valid resource type. It
    is used to reference a business
    identifier for clearly stated resource.
    Example: reference (Claim)
    """

    __fhir_type_name__: Optional[str] = "Ref.3a"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Optional[Uri] = Field(
        None,
        alias="type",
    )


class Ref3b(Ref3Base):
    """
    It is used when providing the business
    identifier for a resource. (claim,
    eligibility, prescription, referral...) when
    there is a choice of resource types. It is
    used to reference a business identifier
    for a choice of resources. Example:
    Reference(Claim | eligibilityRequest)
    """

    __fhir_type_name__: Optional[str] = "Ref.3b"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Uri = Field(
        ...,
        alias="type",
    )


class Ref4(Element):
    """
    It is used when providing either the
    name example(practitioner name) when
    the full resource information is unknown
    or a well known identifier
    """

    __fhir_type_name__: Optional[str] = "Ref.4"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Optional[Uri] = Field(
        None,
        alias="type",
    )
    identifier: Optional[IdentifierB] = Field(
        None,
        alias="identifier",
    )
    display: Optional[String] = Field(
        None,
        alias="display",
    )

    @model_validator(mode="before")
    def check_required_fields(cls, values):
        _type = values.get("type")
        _identifier = values.get("identifier")
        _display = values.get("display")

        if not _display and (not _identifier or not _type):
            raise ValueError(
                "Either display or (type and identifier) shall be provided"
            )
        return values


class Period(Element):
    __fhir_type_name__: Optional[str] = "Period"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    start: Union[DateTime, Date] = Field(
        ...,
        alias="start",
    )
    end: Union[DateTime, Date] = Field(
        ...,
        alias="end",
    )


class Address(Element):
    """
    BRVR at least one element from
    address text or combination of another
    element
    """

    __fhir_type_name__: Optional[str] = "Address"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    use: Optional[Code] = Field(
        None,
        alias="use",
    )
    type: Optional[Code] = Field(
        None,
        alias="type",
    )
    text: String = Field(..., alias="text")
    line: Optional[List[String]] = Field(
        None,
        alias="line",
    )
    city: Optional[String] = Field(
        None,
        alias="city",
    )
    district: Optional[String] = Field(
        None,
        alias="district",
    )
    state: Optional[String] = Field(
        None,
        alias="state",
    )
    postalCode: Optional[String] = Field(
        None,
        alias="postalCode",
    )
    country: Optional[String] = Field(
        None,
        alias="country",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
    )


class Annotation(Element):
    """
    Text node with attribution
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    authorReference: Optional[Ref1] = Field(None, alias="authorReference")
    authorString: Optional[String] = Field(None, alias="authorString", max_length=100)
    time: Optional[DateTime] = Field(
        None, alias="time", description="When the annotation was made"
    )
    text: Markdown = Field(
        ..., alias="text", description="The annotation - text content (as markdown)"
    )
