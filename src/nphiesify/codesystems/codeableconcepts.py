from typing import List
from pydantic import Field
from nphiesify.datatypes import Coding, CodeableConcept, Url, Code

from nphiesify.codesystems.codesets import (
    KSAAdministrativeGender,
    MaritalStatusCodes,
    PatientContactRelationshipCodes,
    CommunicationLanguageCodes,
    ContactEntityTypeCodes,
    OrganizationTypeCodes,
    EndpointConnectionType,
    AdjudicationCodes,
    ClaimTypeCodes,
    ClaimSubTypeCodes,
    ProcessPriorityCodes,
    ClaimPayeeType,
    ClaimCareTeamRoleCodes,
    FundsReservationCodes,
    RelatedClaimRelationship,
    PracticeSpeciality,
    PractitionerRole,
    ClaimInformationCategoryCodes,
    MissingToothReasonCodes,
    DiagnosisTypeCodes,
    DiagnosisOnAdmissionCodes,
    BenefitCategoryCodes,
    ModifierTypeCodes,
    BodySiteCodes,
    FdiOralRegionCodes,
    SubSiteCodes,
    VisitReasonCodes,
    CoverageTypeCodes,
    SubscriberRelationshipCodes,
    CoverageClassCodes,
    CoverageCopayTypeCodes,
    CoverageFinancialExceptionCodes,
    LensTypeCodes,
    KSAMessageEventsCodes,
)


class KSAAdministrativeGenderCoding(Coding):
    code: KSAAdministrativeGender = Field(...)
    _codeset = KSAAdministrativeGender


class KSAAdministrativeGenderCodeableConcept(CodeableConcept):
    coding: List[KSAAdministrativeGenderCoding]


class MaritalStatusCoding(Coding):
    code: MaritalStatusCodes = Field(...)
    _codeset = MaritalStatusCodes


class MaritalStatusCodeableConcept(CodeableConcept):
    coding: List[MaritalStatusCoding]


class PatientContactRelationshipCoding(Coding):
    code: PatientContactRelationshipCodes = Field(...)
    _codeset = PatientContactRelationshipCodes


class PatientContactRelationshipCodeableConcept(CodeableConcept):
    coding: List[PatientContactRelationshipCoding]


class CommunicationCoding(Coding):
    code: CommunicationLanguageCodes = Field(...)
    _codeset = CommunicationLanguageCodes


class CommunicationCodeableConcept(CodeableConcept):
    coding: List[CommunicationCoding]


class OrganizationTypeCoding(Coding):
    code: OrganizationTypeCodes = Field(...)
    _codeset = OrganizationTypeCodes


class OrganizationTypeCodableConcept(CodeableConcept):
    coding: List[OrganizationTypeCoding]


class ContactTypeCoding(Coding):
    code: ContactEntityTypeCodes = Field(...)
    _codeset = ContactEntityTypeCodes


class ContactTypeCodeableConcept(CodeableConcept):
    coding: List[ContactTypeCoding]


class EndpointConnectionTypeCoding(Coding):
    code: EndpointConnectionType = Field(...)
    _codeset = EndpointConnectionType


class AdjudicationCoding(CodeableConcept):
    code: List[AdjudicationCodes]
    _codeset = AdjudicationCodes


class ClaimTypeCoding(Coding):
    code: ClaimTypeCodes = Field(...)
    _codeset = ClaimTypeCodes


class ClaimTypeCodeableConcept(CodeableConcept):
    coding: List[ClaimTypeCoding]


class ClaimSubTypeCoding(Coding):
    code: ClaimSubTypeCodes = Field(...)
    _codeset = ClaimSubTypeCodes


class ClaimSubTypeCodeableConcept(CodeableConcept):
    coding: List[ClaimSubTypeCoding]


class ProcessPriorityCoding(Coding):
    code: ProcessPriorityCodes = Field(...)
    _codeset = ProcessPriorityCodes


class ProcessPriorityCodeableConcept(CodeableConcept):
    coding: List[ProcessPriorityCoding]


class ClaimPayeeCoding(Coding):
    code: ClaimPayeeType = Field(...)
    _codeset = ClaimPayeeType


class ClaimPayeeCodeableConcept(CodeableConcept):
    coding: List[ClaimPayeeCoding]


class ClaimCareTeamRoleCoding(Coding):
    code: ClaimCareTeamRoleCodes = Field(...)
    _codeset = ClaimCareTeamRoleCodes


class ClaimCareTeamRoleCodeableConcept(CodeableConcept):
    coding: List[ClaimCareTeamRoleCoding]


class FundsReservationCoding(Coding):
    code: FundsReservationCodes = Field(...)
    _codeset = FundsReservationCodes


class FundsReservationCodeableConcept(CodeableConcept):
    coding: List[FundsReservationCoding]


class RelatedClaimRelationshipCoding(Coding):
    code: RelatedClaimRelationship = Field(...)
    _codeset = RelatedClaimRelationship


class RelatedClaimRelationshipCodeableConcept(CodeableConcept):
    coding: List[RelatedClaimRelationshipCoding]


class PracticeSpecialityCoding(Coding):
    code: PracticeSpeciality = Field(...)
    _codeset = PracticeSpeciality


class PracticeSpecialityCodeableConcept(CodeableConcept):
    coding: List[PracticeSpecialityCoding]


class PractitionerRoleCoding(Coding):
    code: PractitionerRole = Field(...)
    _codeset = PractitionerRole


class PractitionerRoleCodeableConcept(CodeableConcept):
    coding: List[PractitionerRoleCoding]


class ClaimInformationCategoryCoding(Coding):
    code: ClaimInformationCategoryCodes = Field(...)
    _codeset = ClaimInformationCategoryCodes


class ClaimInformationCategoryCodeableConcept(CodeableConcept):
    coding: List[ClaimInformationCategoryCoding]


class VisitReasonCoding(Coding):
    code: VisitReasonCodes = Field(...)
    _codeset = VisitReasonCodes


class VisitReasonCodeableConcept(CodeableConcept):
    coding: List[VisitReasonCoding]


class MissingToothReasonCoding(Coding):
    code: MissingToothReasonCodes = Field(...)
    _codeset = MissingToothReasonCodes


class MissingToothReasonCodeableConcept(CodeableConcept):
    coding: List[MissingToothReasonCoding]


class DiagnosisCoding(Coding):
    system: Url = Field("http://hl7.org/fhir/sid/icd-10-am", frozen=True)
    code: Code = Field(
        ...,
        alias="code",
        pattern=r"^(([A-Za-z][0-9]{1,2}?)|[Mm][0-9]{1,4}?)((\.|\/)?|((\.|\/)([0-9]+)?))$",
        description="ICD10AM Code",
    )


class DiagnosisCodeableConcept(CodeableConcept):
    coding: List[DiagnosisCoding]


class DiagnosisRelatedGroupCoding(Coding):
    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/diagnosis-related-group", frozen=True
    )
    code: Code = Field(
        ...,
        alias="code",
        description="DRG Code",
    )


class DiagnosisRelatedGroupCodeableConcept(CodeableConcept):
    coding: List[DiagnosisRelatedGroupCoding]


class DiagnosisTypeCodesCoding(Coding):
    code: DiagnosisTypeCodes = Field(...)
    _codeset = DiagnosisTypeCodes


class DiagnosisTypeCodesCodeableConcept(CodeableConcept):
    coding: List[DiagnosisTypeCodesCoding]


class DiagnosisOnAdmissionCoding(Coding):
    code: DiagnosisOnAdmissionCodes = Field(...)
    _codeset = DiagnosisOnAdmissionCodes


class DiagnosisOnAdmissionCodeableConcept(CodeableConcept):
    coding: List[DiagnosisOnAdmissionCoding]


class BenefitCategoryCoding(Coding):
    code: BenefitCategoryCodes = Field(...)
    _codeset = BenefitCategoryCodes


class BenefitCategoryCodeableConcept(CodeableConcept):
    coding: List[BenefitCategoryCoding]


class TransportationSrcaCoding(Coding):
    """This code set includes  Ambulance and transportation services (SRCA)"""

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/transportation-srca", frozen=True
    )


class TransportationSrcaCodeableConcept(CodeableConcept):
    coding: List[TransportationSrcaCoding]


class ImagingCoding(Coding):
    """This code set includes Imaging Procedures"""

    system: Url = Field("http://nphies.sa/terminology/CodeSystem/imaging", frozen=True)


class ImagingCodeableConcept(CodeableConcept):
    coding: List[ImagingCoding]


class LaboratoryCoding(Coding):
    """
    This code set includes  Laboratory tests, observations and Blood Bank
    products
    """

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/laboratory", frozen=True
    )


class LaboratoryCodeableConcept(CodeableConcept):
    coding: List[LaboratoryCoding]


class MedicalDevicesCoding(Coding):
    """This code set includes Medical devices"""

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/medical-devices", frozen=True
    )


class MedicalDevicesCodeableConcept(CodeableConcept):
    coding: List[MedicalDevicesCoding]


class OralHealthIpCoding(Coding):
    """This code set includes Oral Health - In-patient"""

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/oral-health-ip", frozen=True
    )


class OralHealthIpCodeableConcept(CodeableConcept):
    coding: List[OralHealthIpCoding]


class OralHealthOpCoding(Coding):
    """This code set includes  Oral Health - Out-patient"""

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/oral-health-op", frozen=True
    )


class OralHealthOpCodeableConcept(CodeableConcept):
    coding: List[OralHealthOpCoding]


class MedicationCodesCoding(Coding):
    """
    This code set This value set includes all drug or medicament substance
    codes and all pharmaceutical products
    """

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/medication-codes", frozen=True
    )


class MedicationCodesCodeableConcept(CodeableConcept):
    coding: List[MedicationCodesCoding]


class ProceduresCoding(Coding):
    """This code set includes  Procedures / Health interventions"""

    system: Url = Field(
        "http://nphies.sa/terminology/CodeSystem/procedures", frozen=True
    )


class ProceduresCodeableConcept(CodeableConcept):
    coding: List[ProceduresCoding]


class ServicesCoding(Coding):
    """
    This code set includes Room and Board, In-patient Rounding,
    Consultations, Services
    """

    system: Url = Field("http://nphies.sa/terminology/CodeSystem/services", frozen=True)


class ServicesCodeableConcept(CodeableConcept):
    coding: List[ServicesCoding]


class ModifierTypeCoding(Coding):
    code: ModifierTypeCodes = Field(...)
    _codeset = ModifierTypeCodes


class ModifierTypeCodeableConcept(CodeableConcept):
    coding: List[ModifierTypeCoding]


class BodySiteCoding(Coding):
    code: BodySiteCodes = Field(...)
    _codeset = BodySiteCodes


class BodySiteCodeableConcept(CodeableConcept):
    coding: List[BodySiteCoding]


class BodySiteFdiOralRegionCoding(Coding):
    code: FdiOralRegionCodes = Field(...)
    _codeset = FdiOralRegionCodes


class BodySiteFdiOralRegionCodeableConcept(CodeableConcept):
    coding: List[BodySiteFdiOralRegionCoding]


class SubSiteCoding(Coding):
    code: SubSiteCodes = Field(...)
    _codeset = SubSiteCodes


class SubSiteCodeableConcept(CodeableConcept):
    coding: List[SubSiteCoding]


class CoverageTypeCoding(Coding):
    code: CoverageTypeCodes = Field(...)
    _codeset = CoverageTypeCodes


class CoverageTypeCodeableConcept(CodeableConcept):
    coding: List[CoverageTypeCoding]


class SubscriberRelationshipCoding(Coding):
    code: SubscriberRelationshipCodes = Field(...)
    _codeset = SubscriberRelationshipCodes


class SubscriberRelationshipCodeableConcept(CodeableConcept):
    coding: List[SubscriberRelationshipCoding]


class CoverageClassCoding(Coding):
    code: CoverageClassCodes = Field(...)
    _codeset = CoverageClassCodes


class CoverageClassCodeableConcept(CodeableConcept):
    coding: List[CoverageClassCoding]


class CoverageCopayCoding(Coding):
    code: CoverageCopayTypeCodes = Field(...)
    _codeset = CoverageCopayTypeCodes


class CoverageCopayCodeableConcept(CodeableConcept):
    coding: List[CoverageCopayCoding]


class CoverageFinancialExceptionCoding(Coding):
    code: CoverageFinancialExceptionCodes = Field(...)
    _codeset = CoverageFinancialExceptionCodes


class CoverageFinancialExceptionCodeableConcept(CodeableConcept):
    coding: List[CoverageFinancialExceptionCoding]


class LensTypeCoding(Coding):
    code: LensTypeCodes = Field(...)
    _codeset = LensTypeCodes


class LensTypeCodeableConcept(CodeableConcept):
    coding: List[LensTypeCoding]


class KSAMessageEventsCoding(Coding):
    code: KSAMessageEventsCodes = Field(...)
    _codeset = KSAMessageEventsCodes
