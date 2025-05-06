from typing import List, Optional, Literal
from pydantic import Field, PositiveInt, ConfigDict

from nphiesify.datatypes import (
    Boolean,
    IdentifierA,
    String,
    Ref1,
    Period,
    Element,
    SimpleQuantity,
    Money,
)

from nphiesify.resources.resources import DomainResource

from nphiesify.codesystems.codesets import FinancialResourceStatusCodes
from nphiesify.codesystems.codeableconcepts import (
    CoverageTypeCodeableConcept,
    SubscriberRelationshipCodeableConcept,
    CoverageClassCodeableConcept,
    CoverageCopayCodeableConcept,
    CoverageFinancialExceptionCodeableConcept,
)


class CoverageClass(Element):
    """Additional coverage classifications"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: CoverageClassCodeableConcept = Field(
        ...,
        alias="type",
        description="Type of class such as 'group' or 'plan'",
    )
    value: String = Field(
        ...,
        alias="value",
        title="Value",
        description="Value associated with the type",
    )
    name: Optional[String] = Field(
        None,
        alias="name",
        title="Name",
        description="Human readable description of the type and value",
    )


class CoverageCostException(Element):
    """Exceptions for patient payments"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: CoverageFinancialExceptionCodeableConcept = Field(
        ...,
        alias="type",
        description="Exception category",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        title="Period",
        description="The effective period of the exception",
    )


class CoverageCostToBeneficiary(Element):
    """Patient payments for services/products"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: Optional[CoverageCopayCodeableConcept] = Field(
        ...,
        alias="type",
        description="Cost category",
    )
    valueQuantity: SimpleQuantity = Field(
        ..., alias="valueQuantity", title="Value Quantity"
    )
    valueMoney: Money = Field(..., alias="valueMoney", title="Value Money")
    exception: Optional[List[CoverageCostException]] = Field(
        None,
        alias="exception",
        title="Exception",
        description="Exceptions for patient payments",
    )


class Coverage(DomainResource):
    """
    Insurance or medical plan or a payment agreement

    The Coverage resource is intended to provide the high-level identifiers
    and descriptors of a specific insurance plan for a specific
    individual - essentially the insurance card information.
    This may alternately provide the individual or organization, selfpay,
    which will pay for products and services rendered.
    """

    resourceType: Literal["Coverage"]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    identifier: Optional[List[IdentifierA]] = Field(
        None,
        alias="identifier",
        title="Identifier",
        description="Business Identifier for the coverage",
    )
    status: FinancialResourceStatusCodes = Field(..., alias="status", title="Status")
    type: Optional[CoverageTypeCodeableConcept] = Field(
        None,
        alias="type",
        title="Type",
        description="Coverage category such as medical or accident",
    )
    policyHolder: Optional[Ref1] = Field(
        None,
        alias="policyHolder",
        title="Policy Holder",
        description="Owner of the policy",
    )
    subscriber: Optional[Ref1] = Field(
        None,
        alias="subscriber",
        title="Subscriber",
        description="Subscriber to the policy",
    )
    subscriberId: Optional[String] = Field(
        None,
        alias="subscriberId",
        title="Subscriber Id",
        description="ID assigned to the subscriber",
    )
    beneficiary: Ref1 = Field(
        ...,
        alias="beneficiary",
        title="Beneficiary",
        description="Plan beneficiary",
    )
    dependent: Optional[String] = Field(
        None,
        alias="dependent",
        title="Dependent",
        description="Dependent number",
    )
    relationship: Optional[SubscriberRelationshipCodeableConcept] = Field(
        None,
        alias="relationship",
        title="Relationship",
        description="Beneficiary relationship to the subscriber",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        title="Period",
        description="Coverage start and end dates",
    )
    payor: List[Ref1] = Field(
        ...,
        alias="payor",
        title="Payor",
        description="Issuer of the policy",
    )
    class_: Optional[List[CoverageClass]] = Field(
        None,
        alias="class",
        title="Class",
        description="Additional coverage classifications",
    )
    order: Optional[PositiveInt] = Field(
        None, alias="order", title="Order", description="Relative order of the coverage"
    )
    network: Optional[String] = Field(
        None,
        alias="network",
        title="Network",
        description="Insurer network",
    )
    costToBeneficiary: Optional[List[CoverageCostToBeneficiary]] = Field(
        None,
        alias="costToBeneficiary",
        title="Cost to Beneficiary",
        description="Patient payments for services/products",
    )
    subrogation: Optional[Boolean] = Field(
        None,
        alias="subrogation",
        title="Subrogation",
        description="Reimbursement to insurer",
    )
    contract: Optional[Ref1] = Field(
        None, alias="contract", title="Contract", description="Contract details"
    )
