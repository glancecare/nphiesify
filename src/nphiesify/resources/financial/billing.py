from typing import Union, List, Optional, Literal
from pydantic import Field, PositiveInt, ConfigDict

from nphiesify.datatypes import (
    Element,
    Code,
    Ref1,
    Ref2a,
    Ref2b,
    Ref3a,
    Ref3b,
    Ref4,
    IdentifierA,
    IdentifierB,
    CodeableConcept,
    Period,
    DateTime,
    Date,
    Boolean,
    String,
    SimpleQuantity,
    Attachment,
    Address,
    Money,
    Decimal,
    BackboneElement,
)


from nphiesify.resources.resources import DomainResource
from nphiesify.resources.base.individuals import Organization, Patient
from nphiesify.codesystems.codesets import ClaimUseType, FinancialResourceStatusCodes
from nphiesify.codesystems.codeableconcepts import (
    ClaimTypeCodeableConcept,
    ClaimSubTypeCodeableConcept,
    ProcessPriorityCodeableConcept,
    ClaimPayeeCodeableConcept,
    ClaimCareTeamRoleCodeableConcept,
    FundsReservationCodeableConcept,
    RelatedClaimRelationshipCodeableConcept,
    PracticeSpecialityCodeableConcept,
    ClaimInformationCategoryCodeableConcept,
    MissingToothReasonCodeableConcept,
    DiagnosisCodeableConcept,
    DiagnosisTypeCodesCodeableConcept,
    DiagnosisOnAdmissionCodeableConcept,
    BenefitCategoryCodeableConcept,
    TransportationSrcaCodeableConcept,
    ImagingCodeableConcept,
    LaboratoryCodeableConcept,
    MedicalDevicesCodeableConcept,
    OralHealthIpCodeableConcept,
    OralHealthOpCodeableConcept,
    MedicationCodesCodeableConcept,
    ProceduresCodeableConcept,
    ServicesCodeableConcept,
    ModifierTypeCodeableConcept,
    BodySiteCodeableConcept,
    BodySiteFdiOralRegionCodeableConcept,
    SubSiteCodeableConcept,
)


class ClaimRelationship(Element):
    """Prior or corollary claims"""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    claim: Optional[Ref3a] = Field(None, description="Reference to the related claim")
    relationship: Optional[RelatedClaimRelationshipCodeableConcept] = Field(
        None, description="How the reference claim is related"
    )
    reference: Optional[IdentifierA] = Field(None, description="File or case reference")


class ClaimPayee(Element):
    """Recipient of benefits payable"""
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    type: ClaimPayeeCodeableConcept = Field(
        ..., alias="type", description="Category of recipient"
    )
    party: Optional[Ref1] = Field(
        None, alias="party", description="Recipient reference"
    )


class ClaimCareTeam(Element):
    """Members of the care team"""
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    sequence: PositiveInt = Field(
        ..., alias="sequence", description="Order of care team"
    )
    provider: Ref1 = Field(
        ..., alias="provider", description="Practitioner or organization"
    )
    responsible: Optional[Boolean] = Field(
        None, alias="responsible", description="Indicator of the lead practitioner"
    )
    role: Optional[ClaimCareTeamRoleCodeableConcept] = Field(
        None, description="Function within the team"
    )
    # TODO: Add qualification data validation
    qualification: Optional[PracticeSpecialityCodeableConcept] = Field(
        None, description="Practitioner credential or specialization"
    )


class SupportingInfo(Element):
    "Supporting information"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    sequence: PositiveInt = Field(
        ..., alias="sequence", description="Order of care team"
    )
    category: ClaimInformationCategoryCodeableConcept = Field(
        ..., alias="category", description="Classification of the supplied information"
    )
    code: Optional[CodeableConcept] = Field(
        None, alias="code", description="Type of information"
    )
    timingDate: Optional[Date] = Field(None)
    timingPeriod: Optional[Period] = Field(None)
    valueBoolean: Optional[Boolean] = Field(None)
    valueString: Optional[String] = Field(None)
    valueQuantity: Optional[SimpleQuantity] = Field(None)
    valueAttachment: Optional[Attachment] = Field(None)
    valueReference: Optional[Union[Ref1, Ref2a, Ref2b, Ref3a, Ref3b, Ref4]] = Field(
        None
    )
    reason: Optional[MissingToothReasonCodeableConcept] = Field(
        None,
        alias="reason",
        description="This code set provides codes for reasons why a tooth is missing.",
    )


class Diagnosis(Element):
    """Pertinent diagnosis information"""
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    sequence: PositiveInt = Field(
        ..., alias="sequence", description="Diagnosis instance identifier"
    )
    diagnosisCodeableConcept: DiagnosisCodeableConcept = Field(
        ..., alias="diagnosisCodeableConcept", description="ICD10AM Code"
    )
    type: Optional[List[DiagnosisTypeCodesCodeableConcept]] = Field(
        None, alias="type", description="Timing or nature of the diagnosis"
    )
    onAdmission: Optional[DiagnosisOnAdmissionCodeableConcept] = Field(
        None, alias="onAdmission", description="Present on admission"
    )


class Insurance(Element):
    """Patient insurance information"""
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    sequence: PositiveInt = Field(
        ..., alias="sequence", description="Insurance instance identifier"
    )
    focal: Boolean = Field(
        ..., alias="focal", description="Coverage to be used for adjudication"
    )
    identifier: Optional[IdentifierA] = Field(
        None, alias="identifier", description="Pre-assigned Claim number"
    )
    coverage: Ref1 = Field(
        None, alias="coverage", description="Insurance information"
    )
    businessArrangement: Optional[String] = Field(
        None,
        alias="businessArrangement",
        description="Additional provider contract number",
    )
    preAuthRef: Optional[List[String]] = Field(
        None, alias="preAuthRef", description="Prior authorization reference number"
    )
    claimResponse: Optional[Ref1] = Field(
        None, alias="claimResponse", description="Adjudication results"
    )


class ClaimItem(Element):
    """Product or service provided"""
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    sequence: PositiveInt = Field(
        ..., alias="sequence", description="Item instance identifier"
    )
    careTeamSequence: Optional[List[PositiveInt]] = Field(
        None, alias="careTeamSequence", description="Applicable careTeam members"
    )
    diagnosisSequence: Optional[List[PositiveInt]] = Field(
        None, alias="diagnosisSequence", description="Applicable diagnoses"
    )
    procedureSequence: Optional[List[PositiveInt]] = Field(
        None, alias="procedureSequence", description="Applicable procedures"
    )
    informationSequence: Optional[List[PositiveInt]] = Field(
        None,
        alias="informationSequence",
        description="Applicable exception and supporting information",
    )
    category: Optional[BenefitCategoryCodeableConcept] = Field(
        None, alias="category", description="Benefit classification"
    )
    productOrService: Union[
        TransportationSrcaCodeableConcept,
        ImagingCodeableConcept,
        LaboratoryCodeableConcept,
        MedicalDevicesCodeableConcept,
        OralHealthIpCodeableConcept,
        OralHealthOpCodeableConcept,
        MedicationCodesCodeableConcept,
        ProceduresCodeableConcept,
        ServicesCodeableConcept,
    ] = Field(
        ...,
        alias="productOrService",
        description="Billing, service, product, or drug code",
    )
    modifier: Optional[List[ModifierTypeCodeableConcept]] = Field(
        None, alias="modifier", description="Product or service billing modifiers"
    )
    servicedDate: Optional[Date] = Field(None, alias="servicedDate")
    servicedPeriod: Optional[Period] = Field(None, alias="servicedPeriod")
    locationCodeableConcept: Optional[CodeableConcept] = Field(
        None, alias="locationCodeableConcept"
    )
    locationAddress: Optional[Address] = Field(None, alias="locationAddress")
    locationReference: Optional[Ref1] = Field(None, alias="locationReference")
    quantity: Optional[SimpleQuantity] = Field(
        None, alias="quantity", description="Count of products or services"
    )
    unitPrice: Optional[Money] = Field(
        None, alias="unitPrice", description="Fee, charge or cost per item"
    )
    factor: Optional[Decimal] = Field(
        None, alias="factor", description="Price scaling factor"
    )
    net: Optional[Money] = Field(None, alias="net", description="Total item cost")
    bodySite: Optional[
        Union[BodySiteCodeableConcept, BodySiteFdiOralRegionCodeableConcept]
    ] = Field(None, alias="bodySite", description="Anatomical location")
    subSite: Optional[List[SubSiteCodeableConcept]] = Field(
        None, alias="subSite", description="Anatomical sub-location"
    )
    # TODO: Implement udi, encounter, detail, Refer: https://www.hl7.org/fhir/claim.html


class Claim(DomainResource):
    """
    Claim, Pre-determination or Pre-authorization
    Ref: https://www.hl7.org/fhir/claim.html
    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["Claim"]

    identifier: Optional[List[IdentifierA]] = Field(
        None,
        alias="identifier",
    )
    type: ClaimTypeCodeableConcept = Field(...)
    status: FinancialResourceStatusCodes = Field(...)
    subType: Optional[ClaimSubTypeCodeableConcept] = Field(
        None, alias="subType", description="More granular claim type"
    )
    use: ClaimUseType = Field(..., alias="use")
    patient: Ref1 = Field(
        ..., alias="patient", description="The recipient of the products and services"
    )
    billablePeriod: Optional[Period] = Field(
        None, alias="billablePeriod", description="Relevant time frame for the claim"
    )
    created: Union[Date, DateTime] = Field(
        ..., alias="created", description="Resource creation date"
    )
    insurer: Optional[Ref1] = Field(..., alias="insurer", description="Target")
    provider: Optional[Ref1] = Field(
        ..., alias="provider", description="Party responsible for the claim"
    )
    priority: ProcessPriorityCodeableConcept = Field(...)
    fundsReserve: Optional[FundsReservationCodeableConcept] = Field(
        None, alias="fundsReserve", description="For whom to reserve funds"
    )
    related: Optional[List[ClaimRelationship]] = Field(
        None, description="Prior or corollary claims"
    )
    prescription: Optional[Ref1] = Field(
        None,
        alias="prescription",
        description="Prescription authorizing services and products",
    )
    originalPrescription: Optional[Ref1] = Field(
        None,
        alias="originalPrescription",
        description="Original prescription if superseded by fulfiller",
    )
    payee: Optional[ClaimPayee] = Field(
        None, alias="payee", description="Recipient of benefits payable"
    )
    referral: Optional[Ref1] = Field(
        None, alias="referral", description="Treatment referral"
    )
    facility: Optional[Ref1] = Field(
        None, alias="facility", description="Servicing facility"
    )
    careTeam: Optional[List[ClaimCareTeam]] = Field(
        None, alias="careTeam", description="Members of the care team"
    )
    supportingInfo: Optional[List[SupportingInfo]] = Field(
        None, alias="supportingInfo", description="Supporting Information"
    )
    diagnosis: Optional[List[Diagnosis]] = Field(
        None, alias="diagnosis", description="Nature of illness or problem"
    )
    insurance: List[Insurance] = Field(
        ..., alias="insurance", description="Patient insurance information"
    )
    item: Optional[List[ClaimItem]] = Field(
        None, alias="item", description="Product or service provided"
    )
    total: Optional[Money] = Field(None, alias="total", description="Total claim cost")


class _BaseAdjudicationDetail(BackboneElement):
    __fhir_type_name__ = "BaseAdjudicationDetail"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    detailSequence: Optional[PositiveInt] = Field(
        None, alias="detailSequence", description="Claim detail instance identifier"
    )
    noteNumber: Optional[PositiveInt] = Field(
        None, alias="noteNumber", description="Application note number"
    )
    adjudication: Optional["Adjudication"] = Field(
        None, alias="adjudication", description="Detail level adjudication details"
    )


class AdjudicationDetail(_BaseAdjudicationDetail):
    __fhir_type_name__ = "AdjudicationDetail"


class AdjudicationSubDetail(_BaseAdjudicationDetail):
    __fhir_type_name__ = "AdjudicationSubDetail"


class Adjudication(BackboneElement):
    __fhir_type_name__ = "Adjudication"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    category: Optional[CodeableConcept] = Field(
        None, alias="category", description="Type of adjudication information"
    )
    reason: Optional[CodeableConcept] = Field(
        None, alias="reason", description="Explanation of adjudication outcome"
    )
    amount: Optional[Money] = Field(None, alias="amount", description="Monetary amount")
    value: Optional[Decimal] = Field(
        None, alias="value", description="Non-monetary value"
    )


class ClaimResponseItem(BackboneElement):
    __fhir_type_name__ = "Item"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    itemSequence: Optional[PositiveInt] = Field(
        None, alias="itemSequence", description="Claim item instance identifier"
    )
    noteNumber: Optional[PositiveInt] = Field(
        None, alias="noteNumber", description="Applicable note numbers"
    )


class ClaimResponse(DomainResource):
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    identifier: Optional[List[IdentifierB]] = Field(
        None, alias="identifier", description="An identifier for this agent"
    )
    status: Optional[Code] = Field(
        None,
        alias="status",
        description="active | cancelled | draft | entered-in-error",
    )
    type: Optional[ClaimTypeCodeableConcept] = Field(
        None, alias="type", description="More granular claim type"
    )
    subType: Optional[CodeableConcept] = Field(
        None, alias="subType", description="More granular claim type"
    )
    use: Optional[Code] = Field(
        None, alias="code", description="claim | preauthorization | predetermination"
    )
    patient: Optional[Patient] = Field(
        None, alias="patient", description="The recipient of the products and services"
    )
    created: Optional[DateTime] = Field(
        None, alias="created", description="Response creation date"
    )
    insurer: Optional[Organization] = Field(
        None, alias="insurer", description="Party responsible for reimbursement"
    )
    requestor: Optional[Ref1] = Field(
        None,
        alias="requestor",
        description="Party responsible for the claim (Practitioner | PractitionerRole | Organization)",
    )
    request: Optional[Ref1] = Field(
        None, alias="request", description="Id of resource triggering adjudication"
    )
    outcome: Optional[Code] = Field(
        None, alias="outcome", description="queued | complete | error | partial"
    )
    disposition: Optional[str] = Field(
        None, alias="disposition", description="Disposition Message"
    )
    preAuthRef: Optional[str] = Field(
        None, alias="preAuthRef", description="Preauthorization reference"
    )
    preAuthPeriod: Optional[Period] = Field(
        None,
        alias="preAuthPeriod",
        description="Preauthorization reference effective period",
    )
    payeeType: Optional[CodeableConcept] = Field(
        None,
        alias="payeeType",
        description="Party to be paid any benefits payable (subscriber, provider, other)",
    )
    item: Optional[ClaimResponseItem] = Field(
        None, alias="item", description="Adjudication for claim line items"
    )
    # TODO: add rest of the fields
