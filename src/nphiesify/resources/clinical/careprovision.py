from typing import List, Optional, Literal

from pydantic import Field, ConfigDict

from nphiesify.datatypes import (
    IdentifierA,
    DateTime,
    Ref1,
    BackboneElement,
    Decimal,
    Integer,
    SimpleQuantity,
    String,
    Annotation,
)
from nphiesify.resources.resources import DomainResource

from nphiesify.codesystems.codesets import (
    FinancialResourceStatusCodes,
    VisionEyesCodes,
    VisionBaseCodes,
)
from nphiesify.codesystems.codeableconcepts import LensTypeCodeableConcept


class LensPrism(BackboneElement):
    """
    Eye alignment compensation
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    amount: Decimal = Field(..., alias="amount", description="Amount of adjustment")
    base: VisionBaseCodes = Field(..., alias="base", description="up | down | in | out")


class LensSpecification(BackboneElement):
    """
    Vision lens authorization
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    product: LensTypeCodeableConcept = Field(
        ..., alias="product", description="Product to be supplied"
    )
    eye: VisionEyesCodes = Field(..., alias="eye", description="right | left")
    sphere: Optional[Decimal] = Field(
        None, alias="sphere", description="Power of the lens"
    )
    cylinder: Optional[Decimal] = Field(
        None, alias="cylinder", description="Lens power for astigmatism"
    )
    axis: Optional[Integer] = Field(
        None,
        alias="axis",
        description="Lens meridian which contain no power for astigmatism",
    )
    prism: Optional[List[LensPrism]] = Field(
        None, alias="prism", description="Eye alignment compensation"
    )
    add: Optional[Decimal] = Field(
        None, alias="add", description="Added power for multifocal levels"
    )
    power: Optional[Decimal] = Field(
        None, alias="power", description="Contact lens power"
    )
    backCurve: Optional[Decimal] = Field(
        None, alias="backCurve", description="Contact lens back curvature"
    )
    diameter: Optional[Decimal] = Field(
        None, alias="diameter", description="Contact lens diameter"
    )
    diameter: Optional[Decimal] = Field(
        None, alias="diameter", description="Contact lens diameter"
    )
    duration: Optional[SimpleQuantity] = Field(
        None, alias="duration", description="Lens wear duration"
    )
    color: Optional[String] = Field(None, alias="color", description="Color required")
    brand: Optional[String] = Field(None, alias="brand", description="Brand required")
    note: Optional[List[Annotation]] = Field(
        None, alias="note", description="Notes for coatings"
    )


class VisionPrescription(DomainResource):
    """
    Prescription for vision correction products for a patient
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["VisionPrescription"]

    identifier: Optional[List[IdentifierA]] = Field(
        None,
        alias="identifier",
        description="Business Identifier for vision prescription",
    )
    status: FinancialResourceStatusCodes = Field(
        None,
        alias="status",
        description="active | cancelled | draft | entered-in-error",
    )
    created: Optional[DateTime] = Field(
        None, alias="created", description="Response creation date"
    )
    patient: Ref1 = Field(
        ..., alias="patient", description="The recipient of the products and services"
    )
    dateWritten: DateTime = Field(
        ..., alias="dateWritten", description="When prescription was authorized"
    )
    prescriber: Ref1 = Field(
        ..., alias="prescriber", description="Who authorized the vision prescription"
    )
    lensSpecification: List[LensSpecification] = Field(
        ..., alias="lensSpecification", description="Vision lens authorization"
    )
