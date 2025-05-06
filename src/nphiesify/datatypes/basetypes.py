from typing import Optional, Any, Pattern, List

from pydantic import BaseModel, Field


class Base:
    """Base for all types and resources"""

    __tmb_version__: str = "1.2.87"
    __tmb_release_date__: str = "28-12-2022"
    __fhir_type_name__: Optional[str] = None

    @classmethod
    def fhir_type_name(cls) -> Optional[str]:
        return cls.__fhir_type_name__


class Extension(Base, BaseModel):
    """
    Optional Extensions Element
    + Rule: Must have either extensions or value[x], not both
    """

    __fhir_type_name__: Optional[str] = "Extension"
    id: Optional[str] = Field(
        None,
        alias="id",
        description="Unique id for inter-element referencing",
    )
    url: Optional[str] = Field(
        None,
        alias="url",
        description="identifies the meaning of the extension",
        max_length=255,
        pattern=r"\S*",
    )
    value: Optional[Any] = Field(
        None,
        alias="value",
        description="Value of extension",
    )
    valueBoolean: Optional[bool] = Field(
        None,
        alias="valueBoolean",
        description="Value of extension",
    )
    valueString: Optional[str] = Field(
        None,
        alias="valueString",
        description="Value of extension",
    )


class Element(Base, BaseModel):
    """
    Base for all elements
    + Rule: All FHIR elements must have a @value or children
    """

    __fhir_type_name__: Optional[str] = "Element"

    id: Optional[str] = Field(
        None,
        alias="id",
        description="Unique id for inter-element referencing",
    )
    extension: Optional[List[Extension]] = Field(
        None,
        alias="extension",
        description="Additional content defined by implementations",
    )

    @classmethod
    def is_primitive(cls) -> bool:
        return False


class BackboneElement(Element):
    """Base for elements defined inside a resource"""

    __fhir_type_name__: Optional[str] = "BackboneElement"
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        alias="extension",
        description="Extensions that cannot be ignored even if unrecognized",
    )


class DataType(Element):
    """Reuseable Types"""

    __fhir_type_name__: Optional[str] = "DataType"


class BackboneType(Element):
    """Base for datatypes that can carry modifier extensions"""

    __fhir_type_name__: Optional[str] = "BackboneType"
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        alias="extension",
        description="Extensions that cannot be ignored even if unrecognized",
    )


class PrimitiveType:
    """Parent type for DataTypes with a simple value"""

    __fhir_type_name__: Optional[str] = "PrimitiveType"

    regex: Optional[Pattern] = None

    @classmethod
    def is_primitive(cls) -> bool:
        return True
