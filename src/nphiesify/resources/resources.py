from typing import Optional, List

from pydantic import Field, BaseModel, ConfigDict

from nphiesify.datatypes import (
    Base,
    Element,
    Id,
    Instant,
    Uri,
    Canonical,
    Coding,
    Xhtml,
    Code,
    Extension,
)

from nphiesify.codesystems.codesets import NarrativeStatusCodes


class Meta(Element):
    """Metadata about a resource"""

    __fhir_type_name__: Optional[str] = "Meta"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    versionId: Optional[Id] = Field(None, alias="versionId")
    lastUpdated: Optional[Instant] = Field(None, alias="lastUpdated")
    source: Optional[Uri] = Field(None, alias="source")
    profile: Optional[List[Canonical]] = Field(None, alias="profile")
    security: Optional[List[Coding]] = Field(None, alias="security")
    tag: Optional[List[Coding]] = Field(None, alias="tag")


class Narrative(Element):
    """
    Human-readable summary of the resource (essential clinical and
    business information)
    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    __fhir_type_name__: Optional[str] = "Narrative"
    status: NarrativeStatusCodes = Field(..., alias="status")
    div: Xhtml = Field(..., alias="div")


class Resource(Base, BaseModel):
    """
    Base Resource
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    __fhir_type_name__: Optional[str] = "Resource"
    id: Optional[Id] = Field(
        None,
        alias="id",
        description="Logical id of this artifact",
    )
    meta: Optional[Meta] = Field(
        None,
        alias="meta",
        description="Metadata about the resource",
    )
    implicitRules: Optional[Uri] = Field(
        None,
        alias="implicitRules",
    )
    language: Optional[Code] = Field(
        None,
        alias="language",
    )


class DomainResource(Resource):
    """
    A resource with narrative, extensions, and contained resources
    + Rule: If the resource is contained in another resource,
      it SHALL NOT contain nested Resources
    + Rule: If the resource is contained in another resource,
      it SHALL be referred to from elsewhere in the resource
      or SHALL refer to the containing resource
    + Rule: If a resource is contained in another resource,
      it SHALL NOT have a meta.versionId or a meta.lastUpdated
    + Rule: If a resource is contained in another resource,
      it SHALL NOT have a security label
    + Guideline: A resource should have narrative for robust management
    """

    __fhir_type_name__: Optional[str] = "DomainResource"
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    text: Optional[Narrative] = Field(
        None,
        alias="text",
        description="Text summary of the resource, for human interpretation",
    )
    contained: Optional[List[Resource]] = Field(
        None,
        alias="contained",
        description="Contained, inline Resources",
    )
    extension: Optional[List[Extension]] = Field(
        None,
        alias="extension",
        description="Additional content defined by implementations",
    )
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        alias="modifierExtension",
        description="Extensions that cannot be ignored",
    )
