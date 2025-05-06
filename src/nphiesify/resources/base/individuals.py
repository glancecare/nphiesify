from typing import Optional, List, Any, Literal

from pydantic import Field, PositiveInt, ConfigDict

from nphiesify.datatypes import (
    IdentifierA,
    IdentifierB,
    Boolean,
    Element,
    BackboneElement,
    Code,
    String,
    Period,
    Integer,
    Url,
    Extension,
    Date,
    DateTime,
    Address,
    Attachment,
    Ref1,
)

from nphiesify.resources.resources import DomainResource
from nphiesify.codesystems.codesets import (
    ContactPointSystem,
    ContactPointUse,
    AdministrativeGender,
)
from nphiesify.codesystems.codeableconcepts import (
    CodeableConcept,
    CommunicationCodeableConcept,
    ContactTypeCodeableConcept,
    EndpointConnectionTypeCoding,
    KSAAdministrativeGenderCodeableConcept,
    MaritalStatusCodeableConcept,
    OrganizationTypeCodableConcept,
    PatientContactRelationshipCodeableConcept,
    PracticeSpecialityCodeableConcept,
    PractitionerRoleCodeableConcept,
)


class HumanName(Element):
    __fhir_type_name__: Optional[str] = "HumanName"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    use: Optional[Code] = Field(None, alias="use", )
    text: String = Field(..., alias="text", )
    family: Optional[String] = Field(None, alias="family", )
    given: Optional[List[String]] = Field(None, alias="given", )
    prefix: Optional[List[String]] = Field(None, alias="prefix", )
    suffix: Optional[List[String]] = Field(None, alias="suffix", )
    period: Optional[Period] = Field(None, alias="period", )


class ContactPoint(Element):
    """
    Details of a Technology mediated contact point (phone, fax, email, etc.)
    + Rule: A system is required if a value is provided.
    """

    __fhir_type_name__: Optional[str] = "ContactPoint"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    system: Optional[ContactPointSystem] = Field(
        None,
        alias="system",
        description="phone | fax | email | pager | url | sms | other",
    )
    value: Optional[String] = Field(
        None,
        alias="value",
        description="phone | fax | email | pager | url | sms | other",
    )
    use: Optional[ContactPointUse] = Field(
        None,
        alias="use",
        description="home | work | temp | old | mobile - purpose of this contact point",
    )
    rank: Optional[PositiveInt] = Field(
        None,
        alias="rank",
        description="Specify preferred order of use (1 = highest)",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        description="Time period when the contact point was/is in use",
    )


class GenderExtension(Extension):
    __fhir_type_name__: Optional[str] = "GenderExtension"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    url: Url = Field(
        "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-ksa-administrative-gender",
        alias="url",
        frozen=True,
    )
    valueCodeableConcept: KSAAdministrativeGenderCodeableConcept = Field(
        ..., alias="valueCodeableConcept"
    )


class IndividualGenderValueType(Element):
    __fhir_type_name__: Optional[str] = "IndividualGenderValueType"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    extension: List[GenderExtension] = Field(..., alias="extension")


class PatientContact(Element):
    """
    A contact party (e.g. guardian, partner, friend) for the patient
    + Rule: SHALL at least contain a contact's details or a reference to an organization

    https://www.hl7.org/fhir/patient.html
    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    relationship: Optional[List[PatientContactRelationshipCodeableConcept]] = Field(
        None,
        alias="relationship",
        title="Relationship",
        description="The kind of relationship",
    )
    name: Optional[HumanName] = Field(
        None,
        alias="name",
        title="Name",
        description="A name associated with the contact person",
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None, alias="telecom", description="A contact detail for the person"
    )
    address: Optional[List[Address]] = Field(
        None,
        alias="address",
        title="Address",
        description="Address for the contact person",
    )
    gender: Optional[AdministrativeGender] = Field(
        ...,
        alias="gender",
        title="Administrative Gender",
        description="The gender of a person used for administrative purposes.",
    )
    ksa_gender: Optional[IndividualGenderValueType] = Field(
        None,
        alias="_gender",
        title="Administrative Gender",
        description="The gender of a person used for administrative purposes as per the KSA Administrative Gender list",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        description="The period during which this contact person or organization is valid to be contacted relating to this patient",
    )


class Patient(DomainResource):
    """
    Information about an individual or animal receiving health care services

    https://www.hl7.org/fhir/patient.html
    """

    __fhir_type_name__: Optional[str] = "Patient"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["Patient"]

    identifier: Optional[List[IdentifierB]] = Field(
        None, alias="identifier", description="An identifier for this patient"
    )
    active: Optional[Boolean] = Field(
        None,
        alias="active",
        description="Whether this patient's record is in active use",
    )

    name: Optional[List[HumanName]] = Field(
        None, alias="name", description="A name associated with the patient"
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None, alias="telecom", description="A contact detail for the individual"
    )
    gender: Optional[AdministrativeGender] = Field(
        ...,
        alias="gender",
        title="Administrative Gender",
        description="The gender of a person used for administrative purposes.",
    )
    ksa_gender: Optional[IndividualGenderValueType] = Field(
        None,
        alias="_gender",
        title="Administrative Gender",
        description="The gender of a person used for administrative purposes as per the KSA Administrative Gender list",
    )
    birthDate: Optional[Date] = Field(
        None,
        alias="birthDate",
        title="Birth Date",
        description="The date of birth for the individual",
    )
    deceasedBoolean: Optional[Boolean] = Field(
        None,
        alias="deceasedBoolean",
    )
    deceasedDateTime: Optional[DateTime] = Field(
        None,
        alias="deceasedDateTime",
    )
    address: Optional[List[Address]] = Field(
        None,
        alias="address",
        title="Address",
        description="An address for the individual",
    )
    maritalStatus: Optional[MaritalStatusCodeableConcept] = Field(
        None,
        alias="maritalStatus",
        title="Marital Status",
        description="Marital (civil) status of a patient",
    )
    multipleBirthBoolean: Optional[Boolean] = Field(
        None, alias="multipleBirthBoolean", title="Multiple Birth Boolean"
    )
    multipleBirthInteger: Optional[Integer] = Field(
        None, alias="multipleBirthInteger", title="Multiple Birth Integer"
    )
    photo: Optional[List[Attachment]] = Field(
        None,
        alias="photo",
        title="Photo Attachment",
        description="Image of the patient",
    )
    contact: Optional[List[PatientContact]] = Field(
        None, alias="Name", title="A contact party"
    )
    managingOrganization: Optional[Ref1] = Field(
        None,
        alias="managingOrganization",
        title="Managing Organization",
        description="Organization that is the custodian of the patient record",
    )


class OrganizationContact(BackboneElement):
    """
    Contact for the organization for a certain purpose
    """

    __fhir_type_name__ = "Contact"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    purpose: Optional[ContactTypeCodeableConcept] = Field(
        None, alias="purpose", description="The type of contact"
    )
    name: Optional[HumanName] = Field(
        None, alias="name", description="A name associated with the contact"
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None,
        alias="telecom",
        description="Contact details (telephone, email, etc.) for a contact",
    )
    address: Optional[Address] = Field(
        None,
        alias="address",
        description="Visiting or postal addresses for the contact",
    )


class Endpoint(DomainResource):
    """
    The technical details of an endpoint that can be used for electronic services,
    such as for web services providing XDS.b or a REST endpoint for another FHIR server.
    This may include any security context information.

    https://www.hl7.org/fhir/endpoint.html
    """

    __fhir_type_name__ = "Endpoint"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    identifier: Optional[List[IdentifierB]] = Field(
        None,
        alias="identifier",
        description="Identifies this endpoint across multiple systems",
    )
    status: Optional[Code] = Field(
        None,
        alias="status",
        description="active | suspended | error | off | entered-in-error | test",
    )
    connectionType: Optional[EndpointConnectionTypeCoding] = Field(
        None,
        alias="connectionType",
        description="	Protocol/Profile/Standard to be used with this endpoint connection",
    )
    name: Optional[str] = Field(
        None, alias="name", description="A name that this endpoint can be identified by"
    )
    # Using Any as a type here instead of Organization to avoid circular reference
    managingOrganization: Optional[Any] = Field(
        None,
        alias="managingOrganization",
        description="Organization that manages this endpoint (might not be the organization that exposes the endpoint)",
    )
    contact: Optional[ContactPoint] = Field(
        None,
        alias="contact",
        description="Contact details for source (e.g. troubleshooting)",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        description="Interval the endpoint is expected to be operational",
    )
    payloadType: Optional[CodeableConcept] = Field(
        None,
        alias="payloadType",
        description="The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)",
    )
    payloadMimeType: Optional[Code] = Field(
        None,
        alias="payloadMimeType",
        description="Mimetype to send. If not specified, the content could be anything",
    )
    address: Optional[Url] = Field(
        None,
        alias="address",
        description="The technical base address for connecting to this endpoint",
    )
    header: Optional[str] = Field(
        None, alias="header", description="Usage depends on the channel type"
    )


class Organization(DomainResource):
    """
    A formally or informally recognized grouping of people or organizations formed for the purpose of achieving
    some form of collective action. Includes companies, institutions, corporations, departments, community groups,
    healthcare practice groups, payer/insurer, etc.

    https://www.hl7.org/fhir/organization.html
    """

    __fhir_type_name__: Optional[str] = "Organization"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["Organization"]

    identifier: Optional[List[IdentifierA]] = Field(
        None,
        alias="identifier",
        description="Identifies this organization across multiple systems",
    )
    active: Optional[Boolean] = Field(
        None,
        alias="active",
        description="Whether the organization's record is still in active use",
    )
    type: Optional[List[OrganizationTypeCodableConcept]] = Field(
        None, alias="type", description="Kind of organization"
    )
    name: Optional[str] = Field(
        None, alias="name", description="Name used for the organization"
    )
    alias: Optional[str] = Field(
        None,
        alias="alias",
        description="A list of alternate names that the organization is known as, or was known as in the past",
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None, alias="telecom", description="A contact detail for the organization"
    )
    partOf: Optional["Organization"] = Field(
        None,
        alias="partOf",
        description="The organization of which this organization forms a part",
    )
    contact: Optional[OrganizationContact] = Field(
        None,
        alias="contact",
        description="Contact for the organization for a certain purpose",
    )
    endpoint: Optional[Endpoint] = Field(
        None,
        alias="endpoint",
        description="Technical endpoints providing access to services operated for the organization",
    )


class Qualification(BackboneElement):
    __fhir_type_name__: Optional[str] = "Qualification"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    identifier: Optional[List[IdentifierB]] = Field(
        None,
        alias="identifier",
        description="An identifier for this qualification for the practitioner",
    )
    code: Optional[CodeableConcept] = Field(None, alias="code", )
    period: Optional[Period] = Field(
        None,
        alias="period",
        description="Period during which the qualification is valid",
    )
    issuer: Optional[Organization] = Field(
        None,
        alias="issuer",
        description="Organization that regulates and issues the qualification",
    )


class Practitioner(DomainResource):
    """
    A person who is directly or indirectly involved in the provisioning of healthcare.

    https://www.hl7.org/fhir/practitioner.html
    """

    __fhir_type_name__: Optional[str] = "Practitioner"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["Practitioner"]

    identifier: Optional[List[IdentifierB]] = Field(
        None, alias="identifier", description="An identifier for this agent"
    )
    active: Optional[Boolean] = Field(
        None,
        alias="active",
        description="Whether this practitioner's record is in active use",
    )
    name: Optional[List[HumanName]] = Field(
        None, alias="name", description="The name associated with the practitioner"
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None, alias="telecom", description="A contact detail for the practitioner"
    )
    address: Optional[List[Address]] = Field(
        None,
        alias="address",
        title="Address",
        description="An address for the practitioner",
    )
    gender: Optional[AdministrativeGender] = Field(
        None,
        alias="gender",
        title="Administrative Gender",
        description="The gender of a person used for administrative purposes.",
    )
    birthDate: Optional[Date] = Field(
        None,
        alias="birthDate",
        title="Birth Date",
        description="The date of birth for the practitioner",
    )
    photo: Optional[List[Attachment]] = Field(
        None,
        alias="photo",
        title="Photo Attachment",
        description="Image of the practitioner",
    )
    qualification: Optional[Qualification] = Field(
        None,
        alias="qualification",
        description="Certification, licenses, or training pertaining to the provision of care",
    )
    communication: Optional[CommunicationCodeableConcept] = Field(
        None,
        alias="communication",
        description="A language the practitioner can use in patient communication",
    )


class PractitionerRole(DomainResource):
    """
    A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

    https://build.fhir.org/practitionerrole.html

    TODO: Add more fields as needed
    """

    __fhir_type_name__: Optional[str] = "PractitionerRole"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: Literal["PractitionerRole"]

    identifier: Optional[List[IdentifierB]] = Field(
        None, alias="identifier", description="Identifiers for a role/location"
    )
    active: Optional[Boolean] = Field(
        None,
        alias="active",
        description="Whether this practitioner role record is in active use",
    )
    period: Optional[Period] = Field(
        None,
        alias="period",
        description="The period during which the practitioner is authorized to perform in these role(s)",
    )
    practitioner: Optional[Ref1] = Field(
        None,
        alias="practitioner",
        description="Practitioner that provides services for the organization",
    )
    organization: Optional[Ref1] = Field(
        None,
        alias="organization",
        description="Organization where the roles are available",
    )
    code: Optional[List[PractitionerRoleCodeableConcept]] = Field(
        None,
        alias="code",
        description="Roles which this practitioner may perform",
    )
    name: Optional[String] = Field(
        None,
        alias="name",
        description="Denormalized practitioner name, role, organization and location",
    )
    specialty: Optional[List[PracticeSpecialityCodeableConcept]] = Field(
        None,
        alias="specialty",
        description="Specific specialty of the practitioner",
    )
    location: Optional[List[Ref1]] = Field(
        None,
        alias="location",
        description="The location(s) at which this practitioner provides care",
    )
    healthcareService: Optional[List[Ref1]] = Field(
        None,
        alias="healthcareService",
        description="Healthcare services provided for this role's Organization/Location(s)",
    )
