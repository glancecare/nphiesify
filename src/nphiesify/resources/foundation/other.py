from typing import Union, List, Optional, Literal

from pydantic import Field, PositiveInt, ConfigDict
from typing_extensions import Annotated

from nphiesify.codesystems.codeableconcepts import KSAMessageEventsCoding
from nphiesify.codesystems.codesets import BundleTypeCodes
from nphiesify.datatypes import (
    Element,
    BackboneElement,
    Uri,
    Url,
    Ref1,
    Ref3b,
    Code,
    Id,
    Instant,
    String,
)
from nphiesify.resources.base.individuals import (
    Organization,
    Patient,
    Practitioner,
)
from nphiesify.resources.clinical.careprovision import VisionPrescription
from nphiesify.resources.financial.billing import Claim
from nphiesify.resources.financial.support import Coverage
from nphiesify.resources.resources import Resource


class MessageDestination(Element):
    """
    Sender or Receiver of a message
    """

    __fhir_type_name__: str = "MessageTransceiver"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    endpoint: Url = Field(
        ...,
        alias="endpoint",
    )
    receiver: Union[Ref1, Ref3b] = Field(
        ...,
        alias="receiver",
    )


class MessageSource(Element):
    """
    Source of message
    """

    __fhir_type_name__: str = "MessageSource"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    endpoint: Url = Field(
        ...,
        alias="endpoint",
    )


class MessageResponse(Element):
    """
    Response Schema part of the message header
    """

    __fhir_type_name__: str = "MessageResponse"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    code: Code = Field(
        ...,
        alias="code",
    )
    identifier: Id = Field(
        ...,
        alias="identifier",
    )


class MessageHeader(Resource):
    """
    A resource that defines a type of message that can be exchanged
    between systems
    + Warning: Name should be usable as an identifier for the module
    by machine processing applications such as code generation
    """

    resourceType: Literal["MessageHeader"]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    destination: Optional[List[MessageDestination]] = Field(
        None,
        alias="destination",
    )
    sender: Optional[Union[Ref1, Ref3b]] = Field(
        None,
        alias="sender",
    )
    eventCoding: KSAMessageEventsCoding = Field(
        ...,
        alias="eventCoding",
    )
    source: MessageSource = Field(
        ...,
        alias="source",
    )
    response: Optional[MessageResponse] = Field(
        None,
        alias="response",
    )
    focus: Optional[List[Ref1]] = Field(
        None,
        alias="focus",
    )


class BundleLink(BackboneElement):
    """
    Links related to this Bundle
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    relation: String = Field(
        ...,
        alias="relation",
        description="See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1",
    )
    url: Uri = Field(
        ...,
        alias="url",
        description="Reference details for the link",
    )


BundleEntryResourceType = Annotated[
    Union[
        MessageHeader,
        Claim,
        Organization,
        Patient,
        Coverage,
        Practitioner,
        VisionPrescription,
    ],
    Field(discriminator="resourceType"),
]


class BundleEntry(BackboneElement):
    """
    Entry in the bundle - will have a resource or information

    + Rule: must be a resource unless there's a request or response
    + Rule: fullUrl cannot be a version specific reference

    This repeating element order: For bundles of type 'document' and 'message',
    the first resource is special (must be Composition or MessageHeader
    respectively). For all bundles, the meaning of the order of entries
    depends on the bundle type
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    link: Optional[List[BundleLink]] = Field(
        None, alias="link", description="Links related to this Bundle"
    )
    fullUrl: Optional[Uri] = Field(
        None,
        alias="fullUrl",
        description="URI for resource (Absolute URL server address or URI for UUID/OID)",
    )
    resource: Optional[BundleEntryResourceType] = Field(
        None, alias="resource", description="A resource in the bundle"
    )


class Bundle(Resource):
    """
    A container for a collection of resources.

    One common operation performed with resources is to gather a collection of
    resources into a single instance with containing context. In FHIR this is
    referred to as "bundling" the resources together. These resource bundles
    are useful for a variety of different reasons, including:

    -   Returning a set of resources that meet some criteria as part of a
        server operation (see RESTful Search)
    -   Returning a set of versions of resources as part of the history
        operation on a server (see History)
    -   Sending a set of resources as part of a message exchange
    -   Grouping a self-contained set of resources to act as an exchangeable
        and persistable collection with clinical integrity - e.g. a clinical
        document (see Documents)
    -   Creating/updating/deleting a set of resources on a server as a single
        operation (including doing so as a single atomic transaction)
    -   Storing a collection of resources


    https://www.hl7.org/fhir/bundle.html
    """

    __fhir_type_name__: Optional[str] = "Bundle"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: String = Field("Bundle", frozen=True, alias="resourceType")
    identifier: Optional[Id] = Field(
        None,
        alias="identifier",
        description="Persistent identifier for the bundle",
    )
    type: BundleTypeCodes = Field(
        ...,
        alias="type",
        description="document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection",
    )
    timestamp: Optional[Instant] = Field(
        None, alias="timestamp", description="When the bundle was assembled"
    )
    total: Optional[PositiveInt] = Field(
        None, alias="total", description="If search, the total number of matches"
    )
    link: Optional[List[BundleLink]] = Field(
        None, alias="link", description="Links related to this Bundle"
    )
    entry: Optional[List[BundleEntry]] = Field(
        None, alias="entry", description="Entry in the bundle"
    )

class Issue(BackboneElement):
    """
    A single issue associated with the action
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    severity: IssueSeverityCodes = Field(..., alias="severity", description="fatal | error | warning | information | success")
    code: IssueTypeCodes = Field(..., alias="code", description="Error or warning code")
    details: Optional[CodeableConcept] = Field(None, alias="details", description="Additional details about the error")
    diagnostics: Optional[str] = Field(None, alias="diagnostics", description="Additional diagnostic information about the issue")
    expression: Optional[List[str]] = Field(None, alias="expression", description="FHIRPath of element(s) related to issue", examples=["[Patient.identifier[2].value]"])



class OperationOutcome(DomainResource):
    """
    A collection of error, warning, or information messages that result from a system action
    """

    __fhir_type_name__: Optional[str] = "OperationOutcome"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    resourceType: String = Field("OperationOutcome", frozen=True, alias="resourceType")

    issue: List[Issue] = Field(
        None,
        alias="issue",
        description="A single issue associated with the action",
    )
