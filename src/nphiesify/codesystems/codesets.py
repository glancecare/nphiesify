from typing import List
from enum import Enum, IntEnum
from pydantic import PositiveInt, ConfigDict

from nphiesify.datatypes.primitivetypes import (
    Code,
    Url,
    String,
)


def parse_code(text):
    return Code(text)


def parse_url(text):
    return Url(text)


def parse_string(text):
    return String(text)


def parse_positiveint(text):
    return PositiveInt(text)


class AbstractValueSet(Enum):
    """Abstract Class for Value Sets"""

    @classmethod
    def set_system_url(cls):
        return None

    @classmethod
    def get_system_url(cls):
        if url := cls.set_system_url():
            return parse_url(url)
        return None

    def __new__(cls, *args):
        value = args[0]
        obj = str.__new__(cls, parse_code(value))
        obj._value_ = value
        if len(args) > 1:
            obj.display = args[1]
        return obj

    @classmethod
    def display(cls, value):
        if value.display:
            return value.display
        return None

    def encode_url(self, url):
        return parse_url(url)

    @classmethod
    def values(cls) -> List[str]:
        vals = cls.__members__.values()
        vals = [x._value_ for x in vals]
        return vals

    @classmethod
    def names(cls) -> List[str]:
        vals = cls.__members__.values()
        vals = [x.display for x in vals]
        return vals


class AbstractStringEnum(str, AbstractValueSet):
    """Abstract Class for String Value Sets"""

    pass


class AbstractIntEnum(IntEnum, AbstractValueSet):
    """Abstract Class for Int Value Sets"""

    pass


class ContactPointSystem(AbstractStringEnum):
    """
    Telecommunications form for contact point.

    phone:  The value is a telephone number used for voice calls. Use of full
    international numbers starting with + is recommended to enable automatic
    dialing support but not required.

    fax:    Fax	The value is a fax machine. Use of full international numbers
    starting with + is recommended to enable automatic dialing support but not
    required.

    email:  Email	The value is an email address.

    pager:  The value is a pager number. These may be local pager numbers that
    are only usable on a particular pager system.

    url:    A contact that is not a phone, fax, pager or email address and is
    expressed as a URL. This is intended for various institutional or personal
    contacts including web sites, blogs, Skype, Twitter, Facebook, etc. Do not
    use for email addresses.

    sms:    A contact that can be used for sending an sms message
    (e.g. mobile phones, some landlines).

    other:  A contact that is not a phone, fax, page or email address and is
    not expressible as a URL. E.g. Internal mail address. This SHOULD NOT be
    used for contacts that are expressible as a
    URL (e.g. Skype, Twitter, Facebook, etc.) Extensions may be used to
    distinguish "other" contact types.


    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    PHONE = ("phone", "Phone")
    FAX = ("fax", "Fax")
    EMAIL = ("email", "Email")
    PAGER = ("pager", "Pager")
    URL = ("url", "Url")
    SMS = ("sms", "SMS")
    OTHER = ("other", "Other")

    @classmethod
    def set_system_url(cls):
        return "https://www.hl7.org/fhir/valueset-contact-point-system.html"


class ContactPointUse(AbstractStringEnum):
    """
    Use of contact point.

    home:	  A communication contact point at a home; attempted contacts for
    business purposes might intrude privacy and chances are one will contact
    family or other household members instead of the person one wishes to call.
    Typically used with urgent cases, or if no other contacts are available.

    work:	  An office contact point. First choice for business related contacts
    during business hours.

    temp:	  A temporary contact point. The period can provide more detailed
    information.

    old:     This contact point is no longer in use (or was never correct, but
    retained for records).

    mobile:  A telecommunication device that moves and stays with its owner.
    May have characteristics of all other use codes, suitable for urgent
    matters, not the first choice for routine business.
    """

    HOME = ("home", "Home")
    WORK = ("work", "Work")
    TEMP = ("temp", "Temp")
    OLD = ("old", "Old")
    MOBILE = ("mobile", "Mobile")


class AdministrativeGender(AbstractStringEnum):
    """
    Administrative Gender

    The gender of a person used for administrative purposes.

    male:    Male.
    female:  Female.
    other:   Other.
    unknown: Unknown.
    """

    male = ("male", "Male")
    female = ("female", "Female")
    other = ("other", "Other")
    unknown = ("unknown", "Unknown")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/administrative-gender"


class KSAAdministrativeGender(AbstractStringEnum):
    """
    The gender of a person used for administrative purposes.

    male:   Male.
    female: Female.
    unknown:Unknown.
    U:      Undetermined
    N:      Undifferentiated
    A:      Sex changed to Male
    B:      Sex changed to female
    C:      Not Completed

    http://nphies.sa/terminology/CodeSystem/ksa-administrative-gender
    """

    MALE = ("male", "Male")
    FEMALE = ("female", "Female")
    UNKNOWN = ("unknown", "Unknown")
    UNDETERMINDED = ("U", "Undetermined")
    UNDIFFERENTIATED = ("N", "Undifferentiated")
    SEX_CHANGED_TO_MALE = ("A", "Sex changed to Male")
    SEX_CHANGED_TO_FEMALE = ("B", "Sex changed to female")
    NOT_COMPLETED = ("C", "Not Completed")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/ksa-administrative-gender"


class MaritalStatusCodes(AbstractStringEnum):
    """
    Code System MaritalStatus

    Marital (civil) status of a patient as per the nphies adopted list of marital statuses

    L:  Legally Separated
    D:  Marriage contract has been declared dissolved and inactive
    M:  A current marriage contract is active
    U:  Currently not in a marriage contract.
    W:  The spouse has died

    http://terminology.hl7.org/CodeSystem/v3-MaritalStatus
    """

    LEGALLY_SEPARATED = ("L", "Legally Separated")
    DIVORCED = ("D", "Divorced")
    MARRIED = ("M", "Married")
    UNMARRIED = ("U", "unmarried")
    WIDOWED = ("W", "Widowed")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"


class PatientContactRelationshipCodes(AbstractStringEnum):
    """
    Patient Contact Relationship

    The nature of the relationship between the patient and the contact person.

    BP 	Billing contact person
    CP 	Contact person
    EP 	Emergency contact person
    PR 	Person preparing referral
    E 	Employer
    C 	Emergency Contact
    F 	Federal Agency
    I 	Insurance Company
    N 	Next-of-Kin
    S 	State Agency
    U 	Unknown

    http://terminology.hl7.org/CodeSystem/v2-0131
    """

    BILLING_CONTACT_PERSON = ("BP", "Billing contact person")
    CONTACT_PERSON = ("CP", "Contact person")
    EMERGENCY_CONTACT_PERSON = ("EP", "Emergency contact person")
    PERSON_PREPARING_REFERRAL = ("PR", "Person preparing referral")
    EMPLOYER = ("E", "Employer")
    EMERGENCY_CONTACT = ("C", "Emergency Contact")
    FEDERAL_AGENCY = ("F", "Federal Agency")
    INSURANCE_COMPANY = ("I", "Insurance Company")
    NEXT_OF_KIN = ("N", "Next-of-Kin")
    STATE_AGENCY = ("S", "State Agency")
    UNKNOWN = ("U", "Unknown")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/v2-0131"


class CommunicationLanguageCodes(AbstractStringEnum):

    ARABIC = ("ar", "Arabic")
    ENGLISH = ("en", "English")
    BENGALI = ("bn", "Bengali")
    CZECH = ("cs", "Czech")
    DANISH = ("da", "Danish")
    GERMAN = ("de", "German")
    GREEK = ("el", "Greek")
    FRENCH = ("fr", "French")
    SPANISH = ("es", "Spanish")
    HINDI = ("hi", "Hindi")

    @classmethod
    def get_system_url(cls):
        return "https://www.hl7.org/fhir/valueset-languages.html"


class OrganizationTypeCodes(AbstractStringEnum):
    HEALTHCARE_PROVIDER = ("prov", "Healthcare Provider")
    HOSPITAL_DEPARTMENT = ("dept", "Hospital Department")
    ORGANIZATIONAL_TEAM = ("team", "Organizational team")
    GOVERNMENT = ("govt", "Government")
    INSURANCE_COMPANY = ("ins", "Insurance Company")
    PAYER = ("pay", "Payer")
    EDUCATIONAL_INSTITUTE = ("edu", "Educational Institute")
    RELIGIOUS_INSTITUTION = ("reli", "Religious Institution")
    CLINICAL_RESEARCH_SPONSOR = ("crs", "Clinical Research Sponsor")
    COMMUNITY_GROUP = ("cg", "Community Group")
    NON_HEALTHCARE_BUSINESS = ("bus", "Non-Healthcare Business or Corporation")
    OTHER = ("other", "Other")

    @classmethod
    def get_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/organization-type"


class ContactEntityTypeCodes(AbstractStringEnum):

    BILL = ("BILL", "Billing")
    ADMIN = ("ADMIN", "Administrative")
    HUMAN_RESOURCE = ("HR", "Human Resource")
    PAYOR = ("PAYOR", "Payor")
    PATIENT = ("PATINF", "Patient")
    PRESS = ("PRESS", "Press")

    @classmethod
    def get_system_url(cls):
        return "https://www.hl7.org/fhir/organization.html"


class EndpointConnectionType(AbstractStringEnum):
    IHE_XCPD = ("ihe-xcpd", "IHE XCPD")
    IHE_XCA = ("ihe-xca", "IHE XCA")
    IHE_XDS = ("ihe-xds", "IHE XDS")
    IHE_IID = ("ihe-iid", "IHE IID")
    DICOM_WADO_RS = ("dicom-wado-rs", "DICOM WADO-RS")
    DICOM_QIDO_RS = ("dicom-qido-rs", "DICOM QIDO-RS")
    DICOM_WADO_URI = ("dicom-wado-uri", "DICOM WADO-URI")
    HL7_FHIR = ("hl7-fhir-rest", "HL7 FHIR")
    HL7_FHIR_MESSAGING = ("hl7-fhir-msg", "HL7 FHIR Messaging")
    HL7_V2_MLLP = ("hl7v2-mllp", "HL7 v2 MLLP")
    SECURE_EMAIL = ("secure-email", "Secure email")
    DIRECT_PROJECT = ("direct-project", "Direct Project")


class AdjudicationCodes(AbstractStringEnum):
    SUBMITTED_AMOUNT = ("submitted", "Submitted Amount")
    COPAY = ("copay", "CoPay")
    ELIGIBLE_AMOUNT = ("eligible", "Eligible Amount")
    DEDUCTIBLE = ("deductible", "Deductible")
    UNALLOCATED_DEDUCTIBLE = ("unallocdeduct", "Unallocated Deductible")
    ELIGIBLE_PERCENT = ("eligpercent", "Eligible %")
    TAX = ("tax", "Tax")
    BENEFIT_AMOUNT = ("benefit", "Benefit Amount")

    @classmethod
    def get_system_url(cls):
        return "https://www.hl7.org/fhir/valueset-adjudication.html"


class FinancialResourceStatusCodes(AbstractStringEnum):
    """
    Financial Resource Status Codes

    This value set includes Status codes.

    active: The instance is currently in-force.
    cancelled: The instance is withdrawn, rescinded or reversed.
    draft: A new instance the contents of which is not complete.
    entered_in_error: The instance was entered in error.

    https://www.hl7.org/fhir/valueset-fm-status.html
    """

    ACTIVE = ("active", "Active")
    CANCELLED = ("cancelled", "Cancelled")
    DRAFT = ("draft", "Draft")
    ENTERED_IN_ERROR = ("entered-in-error", "Entered in Error")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/fm-status"


class ClaimTypeCodes(AbstractStringEnum):
    """
    Claim Type Codes

    This value set includes Claim Type codes.

    institutional: Hospital, clinic and typically inpatient claims.
    oral: Dental, Denture and Hygiene claims.
    pharmacy: Pharmacy claims for goods and services.
    professional: Typically, outpatient claims from Physician, Psychological,
                  Chiropractor, Physiotherapy, Speech Pathology,
                  rehabilitative, consulting.
    vision: Vision claims for professional services and products such as
            glasses and contact lenses.

    https://www.hl7.org/fhir/valueset-claim-type.html
    """

    INSTITUTIONAL = ("institutional", "Institutional")
    ORAL = ("oral", "Dental")
    PHARMACY = ("pharmacy", "Pharmacy")
    PROFESSIONAL = ("professional", "Professional")
    VISION = ("vision", "Optical")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/claim-type"


class ClaimSubTypeCodes(AbstractStringEnum):
    """
    Claim Sub Type Codes

    ip: Hospital, clinic inpatient claims

    op: Outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy,
    Speech Pathology, rehabilitative, consultation

    emr: A claim for emergency services
    """

    IN_PATIENT = ("ip", "In Patient")
    OUT_PATIENT = ("op", "Out Patient")
    EMR = ("emr", "Emergency")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/claim-subtype"


class ClaimUseType(AbstractStringEnum):
    """
    Claim Use Type Codes

    The purpose of the Claim: predetermination, preauthorization, claim.

    claim:  The treatment is complete and this represents a Claim for the
    services.

    preauthorization:   The treatment is proposed and this represents a
    Pre-authorization for the services.

    predetermination:   The treatment is proposed and this represents a
    Pre-determination for the services.

    https://www.hl7.org/fhir/valueset-claim-use.html
    """

    CLAIM = ("claim", "Claim")
    PREAUTHORIZATION = ("preauthorization", "Preauthorization")
    PREDETERMINATION = ("predetermination", "Predetermination")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/claim-use"


class ProcessPriorityCodes(AbstractStringEnum):
    """
    Process Priority Codes

    This value set includes the financial processing priority codes.
    stat:       Immediately in real time.
    normal:     With best effort.
    deferred:   Later, when possible.
    """

    STAT = ("stat", "Immediate")
    NORMAL = ("normal", "Normal")
    DEFERRED = ("deferred", "Deferred")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/processpriority"


class FundsReservationCodes(AbstractStringEnum):
    """
    Funds Reservation Codes

    This code set includes sample funds reservation type codes.

    patient:    The payor is requested to reserve funds for the provision of
    the named services by any provider for settlement of future claims related
    to this request

    provider:   The payor is requested to reserve funds solely for the named
    provider for settlement of future claims related to this request

    none:   The payor is not being requested to reserve any funds for the
    settlement of future claims
    """

    PATIENT = ("patient", "Patient")
    PROVIDER = ("provider", "Provider")
    NONE = ("none", "None")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/fundsreserve"


class ClaimPayeeType(AbstractStringEnum):
    """
    Claim Payee Type Codes

    This value set includes sample Payee Type codes.

    subscriber  :The subscriber (policy holder) will be reimbursed.

    provider    :Any benefit payable will be paid to the provider (Assignment
    of Benefit).

    other       :Any benefit payable will be paid to a third party such as
    a guarrantor.

    https://www.hl7.org/fhir/valueset-payeetype.html
    """

    SUBSCRIBER = ("subscriber", "Subscriber")
    PROVIDER = ("provider", "Provider")
    OTHER = ("other", "Other")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/payeetype"


class ClaimCareTeamRoleCodes(AbstractStringEnum):
    """
    Claim Care Team Role Codes

    This value set includes sample Claim Care Team Role codes.

    primary: The primary care provider.
    assist:  Assisting care provider.
    supervisor:  Supervising care provider.
    other: Other role on the care team.

    https://www.hl7.org/fhir/valueset-claim-careteamrole.html
    """

    PRIMARY = ("primary", "Primary provider")
    ASSIST = ("assist", "Assisting Provider")
    SUPERVISOR = ("supervisor", "Supervising Provider")
    OTHER = ("other", "Other")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/claimcareteamrole"


class RelatedClaimRelationship(AbstractStringEnum):
    """
    Related Claim Relationship

    This code set includes sample Related Claim Relationship codes.

    prior:  A prior claim instance for the same intended suite of services

    associated: A claim for a different suite of services which is related
    the suite claimed here

    extend: A prior authorization for a suite of services which is to be extended
    by this authorization.

    http://nphies.sa/terminology/CodeSystem/related-claim-relationship
    """

    PRIOR = ("prior", "")
    ASSOCIATED = ("associated", "")
    EXTEND = ("extend", "")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/related-claim-relationship"


class PracticeSpeciality(AbstractStringEnum):
    ANESTHESIOLOGY_SPECIALTY = ("01.00", "Anesthesiology Specialty ")
    AMBULATORY_ANESTHESIA = ("01.01", "Ambulatory Anesthesia")
    ANESTHESIA_CARDIOLOGY = ("01.02", "Anesthesia Cardiology")
    NEURO_ANESTHESIA = ("01.03", "Neuro-Anesthesia")
    OBSTETRICS_ANESTHESIA = ("01.04", "Obstetrics Anesthesia ")
    PEDIATRICS_ANESTHESIA = ("01.05", "Pediatrics Anesthesia")
    PEDIATRICS_CARDIAC_ANESTHESIA = ("01.06", "Pediatrics Cardiac Anesthesia ")
    REGIONAL_ANESTHESIA = ("01.07", "Regional Anesthesia")
    VASCULAR_OR_THORACIC_ANESTHESIA = ("01.08", "Vascular / Thoracic Anesthesia")
    COMMUNITY_MEDICINE_SPECIALTY = ("02.00", "Community Medicine Specialty")
    COMMUNITY_HEALTH = ("02.01", "Community Health")
    DERMATOLOGY_SPECIALTY = ("03.00", "Dermatology Specialty")
    DERMATOLOGY_SURGERY = ("03.01", "Dermatology Surgery ")
    HAIR_IMPLANT_DERMATOLOGY = ("03.02", "Hair Implant Dermatology ")
    PEDIATRICS_DERMATOLOGY = ("03.03", "Pediatrics Dermatology ")
    EMERGENCY_MEDICINE_SPECIALTY = ("04.00", "Emergency Medicine Specialty ")
    ADULT_EMERGENCY_MEDICINE = ("04.01", "Adult Emergency Medicine ")
    PEDIATRICS_EMERGENCY_MEDICINE = ("04.02", "Pediatrics Emergency Medicine ")
    EAR_NOSE_AND_THROAT_SPECIALTY = ("05.00", "Ear, Nose & Throat Specialty ")
    ADULT_ENT = ("05.01", "Adult ENT")
    LARYNGOLOGY = ("05.02", "Laryngology")
    NEURO_OTOLOGY_AND_OTOLOGY = ("05.03", "Neuro - Otology & Otology ")
    NOSE_EAR_SURGERY = ("05.04", "Nose, Ear Surgery ")
    ORAL_AND_MAXILLOFACIAL_SURGERY = ("05.05", "Oral & Maxillofacial Surgery ")
    OTOLARYNGOLOGY = ("05.06", "Otolaryngology")
    PEDIATRICS_ENT = ("05.07", "Pediatrics ENT ")
    PEDIATRICS_OTOLARYNGOLOGY = ("05.08", "Pediatrics Otolaryngology")
    RHINOLOGY = ("05.09", "Rhinology ")
    AUDIOLOGY = ("05.10", "Audiology ")
    FAMILY_MEDICINE_SPECIALTY = ("06.00", "Family Medicine Specialty ")
    FAMILY_MEDICINE = ("06.01", "Family Medicine ")
    PRIMARY_CARE_OR_OPHTHALMOLOGY = ("06.02", "Primary Care / Ophthalmology ")
    PRIMARY_CARE_OR_PULMONARY = ("06.03", "Primary Care / Pulmonary ")
    PRIMARY_CARE_PREVENTIVE_PEDIATRICS = ("06.04", "Primary Care Preventive Pediatrics")
    PRIMARY_HEALTH_CARE = ("06.05", "Primary Health Care ")
    FORENSIC_MEDICINE_SPECIALTY = ("07.00", "Forensic Medicine Specialty ")
    INTERNAL_MEDICINE_SPECIALTY = ("08.00", "Internal Medicine Specialty ")
    ADOLESCENT_MEDICINE = ("08.01", "Adolescent Medicine ")
    CARDIOLOGY = ("08.02", "Cardiology ")
    DIABETICS_MEDICINE = ("08.03", "Diabetics Medicine")
    ENDOCRINOLOGY = ("08.04", "Endocrinology ")
    GASTROLOGYORGASTROENTEROLOGY = ("08.05", "Gastrology/Gastroenterology")
    GERIATRICS = ("08.06", "Geriatrics ")
    HEMATOLOGY = ("08.07", "Hematology ")
    INFECTIOUS_DISEASES = ("08.08", "Infectious Diseases ")
    NEPHROLOGY = ("08.09", "Nephrology")
    NUCLEAR_MEDICINE = ("08.10", "Nuclear Medicine")
    ONCOLOGY = ("08.11", "Oncology ")
    PALLIATIVE_MEDICINE = ("08.12", "Palliative Medicine ")
    PULMONOLOGYORCHEST_MEDICINE = ("08.13", "Pulmonology/Chest Medicine ")
    RHEUMATOLOGY = ("08.14", "Rheumatology ")
    SLEEP_MEDICINE = ("08.15", "Sleep Medicine ")
    SPORT_MEDICINE = ("08.16", "Sport Medicine")
    HEPATOLOGY = ("08.17", "Hepatology ")
    NEUROLOGY = ("08.18", "Neurology ")
    RADIATION_ONCOLOGY = ("08.19", "Radiation Oncology ")
    DIABETES_FOOT_CARE = ("08.20", "Diabetes Foot Care ")
    HEAD_AND_NECK_ONCOLOGY = ("08.21", "Head & Neck Oncology")
    HEMATOLOGY_STEM_CELL = ("08.22", "Hematology - Stem Cell")
    CONGENITAL_HEART_DISEASE = ("08.23", "Congenital Heart Disease ")
    BARIATRIC_MEDICINE = ("08.24", "Bariatric Medicine ")
    CARDIOTHORACIC = ("08.25", "Cardiothoracic")
    GENERAL_MEDICINE = ("08.26", "General Medicine ")
    MICROBIOLOGY_SPECIALTY = ("09.00", "Microbiology Specialty ")
    OBSTETRICS_AND_GYNECOLOGY_SPECIALTY = (
        "10.00",
        "Obstetrics & Gynecology Specialty ",
    )
    GYNECOLOGY_ONCOLOGY = ("10.01", "Gynecology Oncology ")
    INFERTILITY = ("10.02", "Infertility ")
    IVF = ("10.03", "IVF")
    PERINATOLOGY = ("10.04", "Perinatology ")
    UROGYNECOLOGY = ("10.05", "Urogynecology ")
    OBSTETRICS = ("10.06", "Obstetrics ")
    REPRODUCTIVE_ENDOCRINOLOGY_AND_INFERTILITY = (
        "10.07",
        "Reproductive Endocrinology & Infertility ",
    )
    GYNECOLOGY = ("10.08", "Gynecology ")
    MATERNAL_FETAL_MEDICINE = ("10.09", "Maternal Fetal Medicine ")
    OPHTHALMOLOGY_SPECIALTY = ("11.00", "Ophthalmology Specialty ")
    COMPREHENSIVE_OPHTHALMOLOGY = ("11.01", "Comprehensive Ophthalmology ")
    DISEASES_AND_SURGERY_OF_THE_RETINA = ("11.02", "Diseases & Surgery of the Retina ")
    GLAUCOMA = ("11.03", "Glaucoma ")
    NEURO_OPHTHALMOLOGY = ("11.04", "Neuro - Ophthalmology ")
    OCULAR_ONCOLOGY = ("11.05", "Ocular Oncology ")
    OCULOPLASTIC = ("11.06", "Oculoplastic ")
    OPHTHALMOLOGY = ("11.07", "Ophthalmology ")
    PEDIATRICS_OPHTHALMOLOGY_AND_STRABISMUS = (
        "11.08",
        "Pediatrics Ophthalmology & Strabismus ",
    )
    _PRIMARY_CARE_OR_OPHTHALMOLOGY = ("11.09", "Primary Care / Ophthalmology ")
    UVEITIS_OR_MEDICAL_RETINA = ("11.10", "Uveitis / Medical Retina ")
    OPTOMETRIC = ("11.11", "Optometric ")
    ANTERIOR_SEGMENT = ("11.12", "Anterior Segment ")
    ANAPLASTOLOGY = ("11.13", "Anaplastology ")
    MACULAR_DYSTROPHY = ("11.14", "Macular Dystrophy ")
    ABYPLOPIA = ("11.15", "Abyplopia ")
    OPHTHALMIC_PHOTOGRAPHY = ("11.16", "Ophthalmic Photography ")
    ORTHOPEDIC_SPECIALTY = ("12.00", "Orthopedic Specialty ")
    ONCOLOGY_ORTHOPEDIC = ("12.01", "Oncology Orthopedic ")
    ORTHOPEDIC_SURGERY = ("12.02", "Orthopedic Surgery ")
    PEDIATRICS_ORTHOPEDIC = ("12.03", "Pediatrics Orthopedic ")
    UPPER_LIMP_ORTHOPEDIC = ("12.04", "Upper Limp Orthopedic")
    PATHOLOGY_SPECIALTY = ("13.00", "Pathology Specialty ")
    BONE_AND_SOFT_TISSUE_PATHOLOGY = ("13.01", "Bone & Soft Tissue Pathology ")
    DERMATOPATHOLOGY = ("13.02", "Dermatopathology ")
    GAST_AND_HEPAT_PATHOLOGY = ("13.03", "Gast. & Hepat Pathology")
    HISTOPATHOLOGY = ("13.04", "Histopathology ")
    LYMPHOMA_PATHOLOGY = ("13.05", "Lymphoma Pathology")
    PATHOLOGY_DERMATOLOGY = ("13.06", "Pathology Dermatology ")
    RENAL_PATHOLOGY = ("13.07", "Renal Pathology")
    PEDIATRIC_SPECIALTY = ("14.00", "Pediatric Specialty")
    FETAL_MEDICINE = ("14.01", "Fetal Medicine ")
    NEONATAL_INTENSIVE_CARE_NICU_ = ("14.02", "Neonatal Intensive Care (NICU)")
    PEDIATRICS_IMAGING = ("14.03", "Pediatrics Imaging ")
    PEDIATRICS_ENDOCRINOLOGY = ("14.04", "Pediatrics Endocrinology ")
    PEDIATRICS_GASTROENTEROLOGY = ("14.05", "Pediatrics Gastroenterology ")
    PEDIATRICS_GENETICS = ("14.06", "Pediatrics Genetics ")
    PEDIATRICS_RHEUMATOLOGY = ("14.07", "Pediatrics Rheumatology")
    PEDIATRICS_SLEEP_MEDICINE = ("14.08", "Pediatrics Sleep Medicine ")
    _PEDIATRICS_ORTHOPEDIC = ("14.09", "Pediatrics Orthopedic")
    PEDIATRICS_HEMATOLOGY = ("14.10", "Pediatrics Hematology ")
    PEDIATRICS_INFECTIOUS_DISEASES = ("14.11", "Pediatrics Infectious Diseases")
    PEDIATRICS_INTENSIVE_CARE = ("14.12", "Pediatrics Intensive Care ")
    PEDIATRICS_NEPHROLOGY = ("14.13", "Pediatrics Nephrology")
    PEDIATRICS_PULMONARY_DISEASES = ("14.14", "Pediatrics Pulmonary Diseases ")
    _PRIMARY_CARE_PREVENTIVE_PEDIATRICS = (
        "14.15",
        "Primary Care Preventive Pediatrics ",
    )
    PEDIATRIC_NEUROLOGY = ("14.16", "Pediatric Neurology")
    FETAL_CARDIOLOGY = ("14.17", "Fetal Cardiology")
    NEONATOLOGY = ("14.18", "Neonatology ")
    PEDIATRIC_ALLERGY = ("14.19", "Pediatric Allergy ")
    PEDIATRIC_CARDIOLOGY = ("14.20", "Pediatric Cardiology")
    PEDIATRICS_SURGERY_SPECIALTY = ("15.00", "Pediatrics Surgery Specialty")
    PEDIATRICS_CARDIOLOGY = ("15.01", "Pediatrics Cardiology ")
    PEDIATRICS_NEUROSURGERY = ("15.02", "Pediatrics Neurosurgery ")
    PEDIATRICS_ONCOLOGY = ("15.03", "Pediatrics Oncology ")
    PEDIATRICS_PLASTIC_SURGERY = ("15.04", "Pediatrics Plastic Surgery ")
    PEDIATRICS_GENERAL_SURGERY = ("15.05", "Pediatrics General Surgery ")
    PEDIATRICS_HEMATOLOGYORONCOLOGY = ("15.06", "Pediatrics Hematology/Oncology ")
    PHYSICAL_MEDICINE_AND_REHABILITATION_SPECIALTY = (
        "16.00",
        "Physical Medicine & Rehabilitation Specialty ",
    )
    PHYSICAL_MEDICINE_AND_REHABILITATION = (
        "16.01",
        "Physical Medicine & Rehabilitation ",
    )
    OCCUPATIONAL_MEDICINE = ("16.02", "Occupational Medicine")
    PSYCHIATRY_SPECIALTY = ("17.00", "Psychiatry Specialty ")
    ADDICTION_MEDICINE = ("17.01", "Addiction Medicine ")
    CHILD_OR_ADOLESCENT_PSYCHIATRY = ("17.02", "Child / Adolescent Psychiatry ")
    CONSULTATION_LIAISON_PSYCHIATRY = ("17.03", "Consultation - Liaison Psychiatry ")
    FORENSIC_PSYCHIATRY = ("17.04", "Forensic Psychiatry ")
    GERIATRIC_PSYCHIATRY = ("17.05", "Geriatric Psychiatry ")
    MENTAL_HEALTH = ("17.06", "Mental Health ")
    MOOD_DISORDERS_PSYCHIATRY = ("17.07", "Mood Disorders Psychiatry ")
    PSYCHIATRY = ("17.08", "Psychiatry")
    REHABILITATION_PSYCHIATRY = ("17.09", "Rehabilitation Psychiatry ")
    SCHIZOPHRENIA = ("17.10", "Schizophrenia")
    PEDIATRIC_BEHAVIOR = ("17.11", "Pediatric Behavior ")
    YOUTH_STRESS_REDUCTION = ("17.12", "Youth Stress Reduction ")
    RADIOLOGY_SPECIALTY = ("18.00", "Radiology Specialty ")
    BODY_IMAGING = ("18.01", "Body Imaging ")
    BREAST_IMAGING = ("18.02", "Breast Imaging ")
    CARDIAC_IMAGING = ("18.03", "Cardiac Imaging ")
    CHEST_IMAGING = ("18.04", "Chest Imaging ")
    DIAGNOSTIC_NEURORADIOLOGY = ("18.05", "Diagnostic Neuroradiology")
    DIAGNOSTIC_RADIOLOGY = ("18.06", "Diagnostic Radiology")
    EMERGENCY_RADIOLOGY = ("18.07", "Emergency Radiology ")
    INTERVENTIONAL_NEURORADIOLOGY = ("18.08", "Interventional Neuroradiology ")
    INTERVENTIONAL_RADIOLOGY = ("18.09", "Interventional Radiology ")
    MUSCULOSKELETAL_IMAGING = ("18.10", "Musculoskeletal Imaging ")
    _PEDIATRICS_IMAGING = ("18.11", "Pediatrics Imaging ")
    _WOMENS_IMAGING = ("18.12", "Women's Imaging")
    SURGERY_SPECIALTY = ("19.00", "Surgery Specialty ")
    ARTHROPLASTY_SURGERY = ("19.01", "Arthroplasty Surgery ")
    BARIATRIC_SURGERY = ("19.02", "Bariatric Surgery ")
    COSMETIC_SURGERY = ("19.03", "Cosmetic Surgery ")
    CRANIOFACIAL_SURGERY = ("19.04", "Craniofacial Surgery ")
    ENDOCRINOLOGY_SURGERY = ("19.05", "Endocrinology Surgery ")
    FACIOPLASTIC = ("19.06", "Facioplastic ")
    FOOT_AND_ANKLE_SURGERY = ("19.07", "Foot & Ankle Surgery ")
    GENERAL_SURGERY = ("19.08", "General Surgery ")
    HAND_SURGERY = ("19.09", "Hand Surgery ")
    HEPATOBILIARY_AND_UPPER_GI_SURGERY = ("19.10", "Hepatobiliary & Upper GI Surgery ")
    NEUROSURGERY_SPINAL_SURGERY_ = ("19.11", "Neurosurgery (Spinal Surgery) ")
    NEUROSURGERY_OR_ONCOLOGY = ("19.12", "Neurosurgery / Oncology ")
    NEUROSURGERY_VASCULAR = ("19.13", "Neurosurgery Vascular ")
    PLASTIC_SURGERY_AND_RECONSTRUCTION = ("19.14", "Plastic Surgery & Reconstruction ")
    SKULL_BASE_SURGERY = ("19.15", "Skull Base Surgery ")
    SPINE_SURGERY = ("19.16", "Spine Surgery")
    THORACIC_SURGERYORCHEST_SURGERY = ("19.17", "Thoracic Surgery/Chest Surgery ")
    TRAUMA_SURGERY = ("19.18", "Trauma Surgery")
    VASCULAR_SURGERY = ("19.19", "Vascular Surgery ")
    COLORECTAL_SURGERY = ("19.20", "Colorectal Surgery ")
    TRANSPLANT_SURGERY = ("19.21", "Transplant Surgery ")
    LIVER_TRANSPLANT_SURGERY = ("19.22", "Liver Transplant Surgery ")
    RENAL_AND_PANCREAS_TRANSPLANT_SURGERY = (
        "19.23",
        "Renal and Pancreas Transplant Surgery ",
    )
    BREAST_SURGERY = ("19.24", "Breast Surgery ")
    CARDIOTHORACIC_SURGERY = ("19.25", "Cardiothoracic Surgery ")
    BURNS = ("19.26", "Burns")
    UROLOGY_SPECIALTY = ("20.00", "Urology Specialty ")
    GYNECOLOGY_UROLOGY = ("20.01", "Gynecology Urology ")
    LAPAROSCOPIC_UROLOGY = ("20.02", "Laparoscopic Urology ")
    NEURO_UROLOGY = ("20.03", "Neuro - Urology ")
    ONCOLOGY_UROLOGY = ("20.04", "Oncology Urology ")
    PEDIATRICS_UROLOGY = ("20.05", "Pediatrics Urology ")
    RECONSTRUCTION_UROLOGY = ("20.06", "Reconstruction Urology")
    CRITICAL_CARE = ("21.00", "Critical Care ")
    PEDIATRIC_CRITICAL_CARE_PICU_ = ("21.01", "Pediatric Critical Care (PICU) ")
    INTENSIVE_CARE_ICU_ = ("21.02", "Intensive Care (ICU) ")
    DENTAL = ("22.00", "Dental")
    PEDIATRIC_DENTAL = ("22.01", "Pediatric Dental")
    PROSTHODONTICS = ("22.02", "Prosthodontics ")
    ENDODONTICS = ("22.03", "Endodontics ")
    PERIODONTICS = ("22.04", "Periodontics ")
    ORTHODONTICS = ("22.05", "Orthodontics")
    DENTAL_IMPLANTS = ("22.06", "Dental Implants ")
    DENTAL_HYGIENE = ("22.07", "Dental Hygiene ")
    SPECIAL_NEEDS_DENTISTRY = ("22.08", "Special Needs Dentistry ")
    NEUROPHYSIOLOGY = ("23.00", "Neurophysiology")
    SPEECHORSPEECH_LANGUAGE_PATHOLOGY = ("24.00", "Speech/Speech Language Pathology ")
    INFECTION_CONTROL = ("25.00", "Infection Control ")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/practice-codes"


class PractitionerRole(AbstractStringEnum):
    """
    Practitioner Role

    Defines a set of codes that can be used to indicate the role of a Practitioner.

    doctor	Doctor	A qualified/registered medical practitioner
    nurse	Nurse	A practitioner with nursing experience that may be qualified/registered
    pharmacist	Pharmacist	A qualified/registered/licensed pharmacist
    researcher	Researcher	A practitioner that may perform research
    teacher	Teacher/educator	Someone who is able to provide educational services
    dentist	Dentist	A qualified/registered dentist
    physio	Physiotherapist	A qualified/registered Physiotherapist
    speech	Speechtherapist	A qualified/registered Speechtherapist
    ict	ICT professional	Someone who is qualified in Information and Communication Technologies
    """

    DOCTOR = ("doctor", "Doctor")
    NURSE = ("nurse", "Nurse")
    PHARMACIST = ("pharmacist", "Pharmacist")
    RESEARCHER = ("researcher", "Researcher")
    TEACHER = ("teacher", "Teacher")
    DENTIST = ("dentist", "Dentist")
    PHYSIO = ("physio", "Physiotherapist")
    SPEECH = ("speech", "Speechtherapist")
    ICT = ("ict", "ICT professional")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/practitioner-role"


class ClaimInformationCategoryCodes(AbstractStringEnum):
    """
    Claim Information Category Codes

    The general class of the information supplied: information; exception;
    accident, employment; onset, etc.


    info:   Codes conveying additional situation and condition information.
    onset:  Period, start or end dates of aspects of the Condition.
    attachment: Materials attached such as images, documents and resources.
    missingtooth:   Teeth which are missing for any reason, for example: prior
                    extraction, never developed.
    hospitalized:   An indication that the patient was hospitalized, the
                    period if known otherwise a Yes/No (boolean).
    employmentImpacted: An indication that the patient was unable to work, the
                        period if known otherwise a Yes/No (boolean).
    lab-test:   test code
    reason-for-visit:   Reason for visit
    days-supply:    Days Supply
    vital-sign-weight:  Weight
    vital-sign-systolic:    Systolic
    vital-sign-diastolic:   Diastolic
    icu-hours:  Number of hours spent in ICU
    ventilation-hours:  Number of hours under mechanical ventilation
    vital-sign-height:  Height
    chief-complaint:    A concise statement describing the symptom, problem,
                        condition, diagnosis, physician-recommended return,
                        or other reason for a medical encounter
    birth-weight:   Birth weight is the first weight of the new born, taken
                    just after he is born
    temperature:    The body temperature in degree celsius
    pulse:  Pulse rate per minute
    oxygen-saturation:  Blood oxygen saturation in %
    respiratory-rate:   Respiratory rate per minute
    last-menstrual-period:  Start date of last menstrual period

    """

    INFO = ("info", "Information")
    ONSET = ("onset", "Onset")
    ATTACHMENT = ("attachment", "Attachment")
    MISSINGTOOTH = ("missingtooth", "Missing Tooth")
    HOSPITALIZED = ("hospitalized", "Hospitalized")
    EMPLOYMENTIMPACTED = ("employmentImpacted", "EmploymentImpacted")
    LAB_TEST = ("lab-test", "lab-test")
    REASON_FOR_VISIT = ("reason-for-visit", "Reason for visit")
    DAYS_SUPPLY = ("days-supply", "Days Supply")
    VITAL_SIGN_WEIGHT = ("vital-sign-weight", "Weight")
    VITAL_SIGN_SYSTOLIC = ("vital-sign-systolic", "Systolic")
    VITAL_SIGN_DIASTOLIC = ("vital-sign-diastolic", "Diastolic")
    ICU_HOURS = ("icu-hours", "ICU Hours")
    VENTILATION_HOURS = ("ventilation-hours", "Ventilation Hours")
    VITAL_SIGN_HEIGHT = ("vital-sign-height", "Height")
    CHIEF_COMPLAINT = ("chief-complaint", "chief complaint")
    BIRTH_WEIGHT = ("birth-weight", "Birth Weight")
    TEMPERATURE = ("temperature", "Temperature")
    PULSE = ("pulse", "Pulse")
    OXYGEN_SATURATION = ("oxygen-saturation", "Oxygen Saturation")
    RESPIRATORY_RATE = ("respiratory-rate", "Respiratory Rate")
    LAST_MENSTRUAL_PERIOD = ("last-menstrual-period", "Last Menstrual Period")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/claim-information-category"


class VisitReasonCodes(AbstractStringEnum):
    """
    Visit Reason

    The reson for the visit to the healthcare provider.

    new-visit:  A new visit
    follow-up:  A follow up visit
    refill:     A refill
    walk-in:    A walk in visit
    referral:   A referral visit
    """

    NEW_VISIT = ("new-visit", "New Visit")
    FOLLOW_UP = ("follow-up", "Follow Up")
    REFILL = ("refill", "Refill")
    WALK_IN = ("walk-in", "Walk in")
    REFERRAL = ("referral", "Referral")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/visit-reason"


class MissingToothReasonCodes(AbstractStringEnum):
    """
    Missing Tooth Reason Codes

    This code set provides codes for reasons why a tooth is missing.

    e: Extraction
    c: Congenital
    u: Unknown
    o: Other
    """

    EXTRACTION = ("e", "Extraction")
    CONGENITAL = ("c", "Congenital")
    UNKNOWN = ("u", "Unknown")
    OTHER = ("o", "Other")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/missing-tooth-reason"


class DiagnosisTypeCodes(AbstractStringEnum):
    """
    Diagnosis Type

    This code set defines a set of codes that can be used to express the role
    of a diagnosis.

    admitting: The diagnosis given as the reason why the patient was admitted
    to the hospital.

    differential: One of a set of the possible diagnoses that could be
    connected to the signs, symptoms, and lab findings.

    secondary: A condition or complaint either coexisting with the principal
    diagnosis or arising during a service event or episode.

    discharge: The diagnosis given when the patient is discharged from the
    hospital.

    principal: The single medical diagnosis that is most relevant to the
    patient's chief complaint or need for treatment.
    """

    ADMITTING = ("admitting", "Admitting")
    DIFFERENTIAL = ("differential", "Differential")
    SECONDARY = ("secondary", "Secondary")
    DISCHARGE = ("discharge", "Discharge")
    PRINCIPAL = ("principal", "Principal")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/diagnosis-type"


class DiagnosisOnAdmissionCodes(AbstractStringEnum):
    """
    Diagnosis on Admission

    Code to indicate whether or not a diagnosis was present

    yes:    Diagnosis was present at time of inpatient admission.
    no:     Diagnosis was not present at time of inpatient admission.
    unknown:Documentation insufficient to determine if condition was present
    at the time of inpatient admission

    http://nphies.sa/terminology/CodeSystem/diagnosis-on-admission
    """

    YES = ("y", "Yes")
    NO = ("n", "No")
    UNKNOWN = ("u", "Unknown")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/diagnosis-on-admission"


class BenefitCategoryCodes(AbstractStringEnum):
    """
    Benefit Category

    A code to identify the general type of benefits under which products and
    services are provided.

    http://nphies.sa/terminology/CodeSystem/benefit-category
    """

    MEDICAL_CARE = ("1", "Medical Care")
    SURGICAL = ("2", "Surgical")
    CONSULTATION = ("3", "Consultation")
    DIAGNOSTIC_XRAY = ("4", "Diagnostic XRay")
    DIAGNOSTIC_LAB = ("5", "Diagnostic Lab")
    RENAL_SUPPLIES = ("6", "Renal Supplies")
    DIAGNOSTIC_DENTAL = ("7", "Diagnostic Dental")
    PERIODONTICS = ("8", "Periodontics")
    RESTORATIVE = ("9", "Restorative")
    ENDODONTICS = ("10", "Endodontics")
    MAXILLOFACIAL_PROSTHETICS = ("11", "Maxillofacial Prosthetics")
    ADJUNCTIVE_DENTAL_SERVICES = ("12", "Adjunctive Dental Services")
    HEALTH_BENEFIT_PLAN_COVERAGE = ("13", "Health Benefit Plan Coverage")
    DENTAL_CARE = ("14", "Dental Care")
    DENTAL_CROWNS = ("15", "Dental Crowns")
    DENTAL_ACCIDENT = ("16", "Dental Accident")
    HOSPITAL_ROOM_AND_BOARD = ("17", "Hospital Room and Board")
    MAJOR_MEDICAL = ("18", "Major Medical")
    MEDICALLY_RELATED_TRANSPORTATION = ("19", "Medically Related Transportation")
    IN_VITRO_FERTILIZATION = ("20", "In-vitro Fertilization")
    MRI_SCAN = ("21", "MRI Scan")
    DONOR_PROCEDURES = ("22", "Donor Procedures")
    MATERNITY = ("23", "Maternity")
    RENAL_DIALYSIS = ("24", "Renal Dialysis")
    MEDICAL_COVERAGE = ("25", "Medical Coverage")
    DENTAL_COVERAGE = ("26", "Dental Coverage")
    HEARING_COVERAGE = ("27", "Hearing Coverage")
    VISION_COVERAGE = ("28", "Vision Coverage")
    MENTAL_HEALTH = ("29", "Mental Health")
    OP_MEDICAL = ("30", "OP Medical")
    MAX_COPAY = ("31", "Max Copay")
    MEDICAL_EQUIPMENT = ("32", "Medical Equipment")
    ACUTE_PSYCHIATRIC_CASES = ("33", "Acute Psychiatric Cases")
    CHRONIC_PSYCHIATRIC_CASES = ("34", "Chronic Psychiatric Cases")
    ALZHEIMERS_DISEASE = ("35", "Alzheimer's Disease")
    INFERTILITY_AND_RELATED_PROCEDURES = ("36", "Infertility & Related Procedures")
    ORTHODONTIC_TREATMENT = ("37", "Orthodontic Treatment")
    CHECK_UPS = ("38", "Check ups")
    CIRCUMCISION_OF_MALE_NEWBORN = ("39", "Circumcision of male newborn")
    EAR_PIERCING_OF_FEMALE_NEWBORN = ("40", "Ear Piercing of female newborn")
    DENTAL_PROSTHESIS = ("41", "Dental Prosthesis")
    VISION_SURGERY = ("42", "Vision Surgery")
    OUTPATIENT_TREATMENT_EXPENSES_WITHIN_MINIMUM_UNIFIED_NETWORK = (
        "43",
        "Outpatient Treatment expenses-within minimum unified network",
    )
    OUTPATIENT_TREATMENT_EXPENSES_FOR_HOSPITAL_OUT_OF_THE_MINIMUM_UNIFIED_NETWORK = (
        "44",
        "Outpatient Treatment expenses-for hospital out of the minimum unified network",
    )
    OUTPATIENT_TREATMENT_EXPENSES_FOR_NON_HOSPITAL_OUT_OF_THE_MINIMUM_UNIFIED_NETWORK = (
        "45",
        "Outpatient Treatment expenses-for non-hospital out of the minimum unified network",
    )
    COMPANION_ROOM_AND_BOARD = ("46", "Companion Room and Board")
    REPATRIATION_OF_MORTAL_REMAINS = ("47", "Repatriation of Mortal Remains")
    ACQUIRED_VALVULAR_HEART_DISEASE = ("48", "Acquired valvular heart disease")
    AUTISM_MANAGEMENT = ("49", "Autism Management")
    DISABILITY_COMPENSATIONS = ("50", "Disability Compensations")
    OBESITY_SURGERY = ("51", "Obesity Surgery")
    NEWBORN_SCREENING_PROGRAMS_FOR_HEARING_IMPAIRMENT_AND_CRITICAL_CONGENITAL_HEART_DISEASE = (
        "52",
        "Newborn Screening Programs for Hearing Impairment & critical congenital heart disease",
    )
    HOME_HEALTHCARE = ("53", "Home Healthcare")
    LONG_TERM_CARE = ("54", "Long term care")
    REHABILITATION = ("55", "Rehabilitation ")
    PHARMACY = ("56", "Pharmacy")
    OP_PRESCRIBED_INVENTED_MEDICINES_WITH_GENERIC_ALTERNATIVE = (
        "57",
        "OP Prescribed Invented Medicines - with generic alternative",
    )
    ADVANCED_DENTAL_COVERAGE = ("58", "Advanced Dental Coverage")
    ADVANCED_HOMECARE_COVERAGE = ("59", "Advanced Homecare coverage")
    ADVANCED_OBESITY_MEDICAL_MANAGEMENT = ("60", "Advanced Obesity Medical Management")
    BASIC_AND_PREVENTIVE_DENTAL_COVERAGE = (
        "61",
        "Basic and Preventive Dental Coverage",
    )
    BASIC_HOMECARE_COVERAGE = ("62", "Basic Homecare coverage ")
    CONTRACEPTION_COVERAGE_BIRTH_CONTROL_ = (
        "63",
        "Contraception Coverage (Birth Control)",
    )
    HIP_AND_KNEE_REPLACEMENT = ("64", "Hip and Knee Replacement")
    IMPAIRMENT_MEDICAL_MANAGEMENT = ("65", "Impairment medical management")
    OP_PRESCRIBED_GENERIC_AND_INVENTED_MEDICINES_WITH_NO_GENERIC_ALTERNATIVE_AVAILABLE = (
        "66",
        "OP Prescribed Generic and Invented Medicines - with no generic alternative available",
    )
    OUTPATIENT_TREATMENT_EXPENSES_PRIMARY_CLINIC = (
        "67",
        "Outpatient Treatment expenses - Primary clinic",
    )
    OUTPATIENT_TREATMENT_EXPENSES_SPECIALIZED_CLINIC_WITH_REFERRAL = (
        "68",
        "Outpatient Treatment expenses - specialized clinic with referral",
    )
    OUTPATIENT_TREATMENT_EXPENSES_SPECIALIZED_CLINIC_WITHOUT_REFERRAL = (
        "69",
        "Outpatient Treatment expenses - specialized clinic without referral",
    )
    PEDIATRIC_VISION_COVERAGE = ("70", "Pediatric vision coverage")
    PSYCHIATRY_COVERAGE = ("71", "Psychiatry coverage")
    RENAL_TRANSPLANT = ("72", "Renal transplant")
    ROOT_CANAL_DENTAL_COVERAGE = ("73", "Root canal dental coverage")
    COMPLICATIONS_ARISING_FROM_TREATMENT_OF_A_COVERED_BENEFIT = (
        "74",
        "Complications arising from treatment of a covered benefit",
    )
    CONGENITAL_ANOMALIES = ("75", "Congenital anomalies")
    COSTS_OF_NATIONAL_PROGRAM_FOR_THE_EARLY_EXAMINATION_OF_NEWBORN_TO_LIMIT_IMPAIRMENT = (
        "76",
        "Costs of national program for the early examination of newborn to limit impairment",
    )
    DELIVERY_OF_PREMATURE_BABIES = ("77", "Delivery of premature babies")
    EMERGENCY_SERVICE_COVERAGE = ("78", "Emergency Service coverage")
    GENETIC_DISEASES = ("79", "Genetic diseases ")
    INPATIENT_MEDICAL_COVERAGE = ("80", "Inpatient Medical Coverage")
    LIFE_SUSTAINING_AND_INTERVENTIONS_ALTERING_MEDICAL_OUTCOMES = (
        "81",
        "Life sustaining and interventions altering medical outcomes",
    )
    MATERNITY_COMPLICATIONS_COVERAGE = ("82", "Maternity Complications Coverage")
    NEW_BORN_COVERAGE = ("83", "New-born coverage")
    TELEMEDICINE = ("84", "Telemedicine")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/benefit-category"


class ModifierTypeCodes(AbstractStringEnum):
    """
    Modifier type Codes

    This value set includes sample Modifier type codes.

    a	Repair of prior service or installation.
    b	Temporary service or installation.
    c	Treatment associated with TMJ.
    e	Implant or associated with an implant.
    rooh    A Rush service or service performed outside of normal office hours.
    x	None.
    """

    REPAIR = ("a", "Repair of prior service or installation")
    TEMP = ("b", "Temporary service or installation")
    TMJ = ("c", "TMJ treatment")
    IMPLANT = ("e", "Implant or associated with an implant")
    ROOH = ("rooh", "Rush or Outside of office hours")
    NONE = ("x", "None")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/modifiers"


class BodySiteCodes(AbstractStringEnum):
    """
    Body Site

    This code set includes Specific and identified anatomical location of the service provided to the patient (limb, tooth, etc.)

    E1:	Upper left, eyelid
    E2:	Lower left, eyelid
    E3:	Upper right, eyelid
    E4:	Lower right, eyelid
    F1:	Left hand, second digit
    F2:	Left hand, third digit
    F3:	Left hand, fourth digit
    F4:	Left hand, fifth digit
    F5:	Right hand, thumb
    F6:	Right hand, second digit
    F7:	Right hand, third digit
    F8:	Right hand, fourth digit
    F9:	Right hand, fifth digit
    FA:	Left hand, thumb
    LC:	Left circumflex coronary artery
    LD:	Left anterior descending coronary artery
    LM:	Left main coronary artery
    LT:	Left side (used to identify procedures performed on the left side of the body)
    RC:	Right coronary artery
    RI:	Ramus intermedius coronary artery
    RT:	Right side (used to identify procedures performed on the right side of the body)
    T1:	Left foot, second digit
    T2:	Left foot, third digit
    T3:	Left foot, fourth digit
    T4:	Left foot, fifth digit
    T5:	Right foot, great toe
    T6:	Right foot, second digit
    T7:	Right foot, third digit
    T8:	Right foot, fourth digit
    T9:	Right foot, fifth digit
    TA:	Left foot, great toe
    RIV:	right eye
    LIV:	left eye

    http://nphies.sa/terminology/CodeSystem/body-site
    """

    E1 = ("E1", "Upper left, eyelid")
    E2 = ("E2", "Lower left, eyelid")
    E3 = ("E3", "Upper right, eyelid")
    E4 = ("E4", "Lower right, eyelid")
    F1 = ("F1", "Left hand, second digit")
    F2 = ("F2", "Left hand, third digit")
    F3 = ("F3", "Left hand, fourth digit")
    F4 = ("F4", "Left hand, fifth digit")
    F5 = ("F5", "Right hand, thumb")
    F6 = ("F6", "Right hand, second digit")
    F7 = ("F7", "Right hand, third digit")
    F8 = ("F8", "Right hand, fourth digit")
    F9 = ("F9", "Right hand, fifth digit")
    FA = ("FA", "Left hand, thumb")
    LC = ("LC", "Left circumflex coronary artery")
    LD = ("LD", "Left anterior descending coronary artery")
    LM = ("LM", "Left main coronary artery")
    LT = (
        "LT",
        "Left side (used to identify procedures performed on the left side of the body)",
    )
    RC = ("RC", "Right coronary artery")
    RI = ("RI", "Ramus intermedius coronary artery")
    RT = (
        "RT",
        "Right side (used to identify procedures performed on the right side of the body)",
    )
    T1 = ("T1", "Left foot, second digit")
    T2 = ("T2", "Left foot, third digit")
    T3 = ("T3", "Left foot, fourth digit")
    T4 = ("T4", "Left foot, fifth digit")
    T5 = ("T5", "Right foot, great toe")
    T6 = ("T6", "Right foot, second digit")
    T7 = ("T7", "Right foot, third digit")
    T8 = ("T8", "Right foot, fourth digit")
    T9 = ("T9", "Right foot, fifth digit")
    TA = ("TA", "Left foot, great toe")
    RIV = ("RIV", "right eye")
    LIV = ("LIV", "left eye")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/body-site"


class SubSiteCodes(AbstractStringEnum):
    """
    Sub Site

    This code set contains codes to indicate the A sublocation region or
    surface of the bodySite, e.g. limb region or tooth surface(s).

    R	Right
    L	Left
    U	Upper
    D	Down
    A	Anterior
    P	Posterior
    I	interior
    E	Exterior

    http://nphies.sa/terminology/CodeSystem/subsite
    """

    RIGHT = ("R", "Right")
    LEFT = ("L", "Left")
    UPPER = ("U", "Upper")
    DOWN = ("D", "Down")
    ANTERIOR = ("A", "Anterior")
    POSTERIOR = ("P", "Posterior")
    INTERIOR = ("I", "Interior")
    EXTERIOR = ("E", "Exterior")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/subsite"


class FdiOralRegionCodes(AbstractStringEnum):
    """
    FDI Oral Region Codes

    http://nphies.sa/terminology/CodeSystem/fdi-oral-region
    """

    UPPER_RIGHT_PERMANENT_TEETH_1 = ("11", "UPPER RIGHT; PERMANENT TEETH # 1")
    UPPER_RIGHT_PERMANENT_TEETH_2 = ("12", "UPPER RIGHT; PERMANENT TEETH # 2")
    UPPER_RIGHT_PERMANENT_TEETH_3 = ("13", "UPPER RIGHT; PERMANENT TEETH # 3")
    UPPER_RIGHT_PERMANENT_TEETH_4 = ("14", "UPPER RIGHT; PERMANENT TEETH # 4")
    UPPER_RIGHT_PERMANENT_TEETH_5 = ("15", "UPPER RIGHT; PERMANENT TEETH # 5")
    UPPER_RIGHT_PERMANENT_TEETH_6 = ("16", "UPPER RIGHT; PERMANENT TEETH # 6")
    UPPER_RIGHT_PERMANENT_TEETH_7 = ("17", "UPPER RIGHT; PERMANENT TEETH # 7")
    UPPER_RIGHT_PERMANENT_TEETH_8 = ("18", "UPPER RIGHT; PERMANENT TEETH # 8")
    UPPER_LEFT_PERMANENT_TEETH_1 = ("21", "UPPER LEFT; PERMANENT TEETH # 1")
    UPPER_LEFT_PERMANENT_TEETH_2 = ("22", "UPPER LEFT; PERMANENT TEETH # 2")
    UPPER_LEFT_PERMANENT_TEETH_3 = ("23", "UPPER LEFT; PERMANENT TEETH # 3")
    UPPER_LEFT_PERMANENT_TEETH_4 = ("24", "UPPER LEFT; PERMANENT TEETH # 4")
    UPPER_LEFT_PERMANENT_TEETH_5 = ("25", "UPPER LEFT; PERMANENT TEETH # 5")
    UPPER_LEFT_PERMANENT_TEETH_6 = ("26", "UPPER LEFT; PERMANENT TEETH # 6")
    UPPER_LEFT_PERMANENT_TEETH_7 = ("27", "UPPER LEFT; PERMANENT TEETH # 7")
    UPPER_LEFT_PERMANENT_TEETH_8 = ("28", "UPPER LEFT; PERMANENT TEETH # 8")
    LOWER_LEFT_PERMANENT_TEETH_1 = ("31", "LOWER LEFT; PERMANENT TEETH # 1")
    LOWER_LEFT_PERMANENT_TEETH_2 = ("32", "LOWER LEFT; PERMANENT TEETH # 2")
    LOWER_LEFT_PERMANENT_TEETH_3 = ("33", "LOWER LEFT; PERMANENT TEETH # 3")
    LOWER_LEFT_PERMANENT_TEETH_4 = ("34", "LOWER LEFT; PERMANENT TEETH # 4")
    LOWER_LEFT_PERMANENT_TEETH_5 = ("35", "LOWER LEFT; PERMANENT TEETH # 5")
    LOWER_LEFT_PERMANENT_TEETH_6 = ("36", "LOWER LEFT; PERMANENT TEETH # 6")
    LOWER_LEFT_PERMANENT_TEETH_7 = ("37", "LOWER LEFT; PERMANENT TEETH # 7")
    LOWER_LEFT_PERMANENT_TEETH_8 = ("38", "LOWER LEFT; PERMANENT TEETH # 8")
    LOWER_RIGHT_PERMANENT_TEETH_1 = ("41", "LOWER RIGHT; PERMANENT TEETH # 1")
    LOWER_RIGHT_PERMANENT_TEETH_2 = ("42", "LOWER RIGHT; PERMANENT TEETH # 2")
    LOWER_RIGHT_PERMANENT_TEETH_3 = ("43", "LOWER RIGHT; PERMANENT TEETH # 3")
    LOWER_RIGHT_PERMANENT_TEETH_4 = ("44", "LOWER RIGHT; PERMANENT TEETH # 4")
    LOWER_RIGHT_PERMANENT_TEETH_5 = ("45", "LOWER RIGHT; PERMANENT TEETH # 5")
    LOWER_RIGHT_PERMANENT_TEETH_6 = ("46", "LOWER RIGHT; PERMANENT TEETH # 6")
    LOWER_RIGHT_PERMANENT_TEETH_7 = ("47", "LOWER RIGHT; PERMANENT TEETH # 7")
    LOWER_RIGHT_PERMANENT_TEETH_8 = ("48", "LOWER RIGHT; PERMANENT TEETH # 8")
    UPPER_RIGHT_DECIDUOUS_TEETH_1 = ("51", "UPPER RIGHT; DECIDUOUS TEETH # 1")
    UPPER_RIGHT_DECIDUOUS_TEETH_2 = ("52", "UPPER RIGHT; DECIDUOUS TEETH # 2")
    UPPER_RIGHT_DECIDUOUS_TEETH_3 = ("53", "UPPER RIGHT; DECIDUOUS TEETH # 3")
    UPPER_RIGHT_DECIDUOUS_TEETH_4 = ("54", "UPPER RIGHT; DECIDUOUS TEETH # 4")
    UPPER_RIGHT_DECIDUOUS_TEETH_5 = ("55", "UPPER RIGHT; DECIDUOUS TEETH # 5")
    UPPER_LEFT_DECIDUOUS_TEETH_1 = ("61", "UPPER LEFT; DECIDUOUS TEETH # 1")
    UPPER_LEFT_DECIDUOUS_TEETH_2 = ("62", "UPPER LEFT; DECIDUOUS TEETH # 2")
    UPPER_LEFT_DECIDUOUS_TEETH_3 = ("63", "UPPER LEFT; DECIDUOUS TEETH # 3")
    UPPER_LEFT_DECIDUOUS_TEETH_4 = ("64", "UPPER LEFT; DECIDUOUS TEETH # 4")
    UPPER_LEFT_DECIDUOUS_TEETH_5 = ("65", "UPPER LEFT; DECIDUOUS TEETH # 5")
    LOWER_LEFT_DECIDUOUS_TEETH_1 = ("71", "LOWER LEFT; DECIDUOUS TEETH # 1")
    LOWER_LEFT_DECIDUOUS_TEETH_2 = ("72", "LOWER LEFT; DECIDUOUS TEETH # 2")
    LOWER_LEFT_DECIDUOUS_TEETH_3 = ("73", "LOWER LEFT; DECIDUOUS TEETH # 3")
    LOWER_LEFT_DECIDUOUS_TEETH_4 = ("74", "LOWER LEFT; DECIDUOUS TEETH # 4")
    LOWER_LEFT_DECIDUOUS_TEETH_5 = ("75", "LOWER LEFT; DECIDUOUS TEETH # 5")
    LOWER_RIGHT_DECIDUOUS_TEETH_1 = ("81", "LOWER RIGHT; DECIDUOUS TEETH # 1")
    LOWER_RIGHT_DECIDUOUS_TEETH_2 = ("82", "LOWER RIGHT; DECIDUOUS TEETH # 2")
    LOWER_RIGHT_DECIDUOUS_TEETH_3 = ("83", "LOWER RIGHT; DECIDUOUS TEETH # 3")
    LOWER_RIGHT_DECIDUOUS_TEETH_4 = ("84", "LOWER RIGHT; DECIDUOUS TEETH # 4")
    LOWER_RIGHT_DECIDUOUS_TEETH_5 = ("85", "LOWER RIGHT; DECIDUOUS TEETH # 5")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/fdi-oral-region"


class SurfaceCodes(AbstractStringEnum):
    """
    Surface Codes

    This value set includes a list of the FDI tooth surface codes.

    M	Mesial	The surface of a tooth that is closest to the midline (middle) of the face.
    O	Occlusal	The chewing surface of posterior teeth.
    I	Incisal	The biting edge of anterior teeth.
    D	Distal	The surface of a tooth that faces away from the midline of the face.
    B	Buccal	The surface of a posterior tooth facing the cheeks.
    V	Ventral	The surface of a tooth facing the lips.
    L	Lingual	The surface of a tooth facing the tongue.
    MO	Mesioclusal	The Mesioclusal surfaces of a tooth.
    DO	Distoclusal	The Distoclusal surfaces of a tooth.
    DI	Distoincisal	The Distoincisal surfaces of a tooth.
    MOD	Mesioclusodistal	The Mesioclusodistal surfaces of a tooth

    http://nphies.sa/terminology/CodeSystem/fdi-tooth-surface
    """

    MESIAL = ("M", "Mesial")
    OCLUSAL = ("O", "Occlusal")
    INCISAL = ("I", "Incisal")
    DISTAL = ("D", "Distal")
    BUCCAL = ("B", "Buccal")
    VENTRAL = ("V", "Ventral")
    LINGUAL = ("L", "Lingual")
    MESIOCLUSAL = ("MO", "Mesioclusal")
    DISTOCLUSAL = ("DO", "Distoclusal")
    DISTOINCISAL = ("DI", "Distoincisal")
    MESIOCLUSODISTAL = ("MOD", "Mesioclusodistal")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/fdi-tooth-surface"


class CoverageTypeCodes(AbstractStringEnum):
    """
    Coverage Type

    Codes for the type of insurance product

    EHCPOL:     extended healthcare
    PUBLICPOL:  public healthcare

    http://nphies.sa/terminology/CodeSystem/coverage-type
    """

    EXTENDED_HEALTHCARE = ("EHCPOL", "extended healthcare")
    PUBLIC_HEALTHCARE = ("PUBLICPOL", "public healthcare")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/coverage-type"


class SubscriberRelationshipCodes(AbstractStringEnum):
    """
    SubscriberPolicyholder Relationship Codes

    This value set includes codes for the relationship between the Subscriber
    and the Beneficiary (insured/covered party/patient).

    child	The Beneficiary is a child of the Subscriber
    parent	The Beneficiary is a parent of the Subscriber
    spouse	The Beneficiary is a spouse or equivalent of the Subscriber
    common	Law Spouse	The Beneficiary is a common law spouse or equivalent of the Subscriber
    other	The Beneficiary has some other relationship the Subscriber
    self	The Beneficiary is the Subscriber
    injured	The Beneficiary is covered under insurance of the subscriber due to an injury.

    http://terminology.hl7.org/CodeSystem/subscriber-relationship
    """

    CHILD = ("child", "Child")
    PARENT = ("parent", "Parent")
    SPOUSE = ("spouse", "Spouse")
    COMMON = ("common", "Common")
    OTHER = ("other", "Other")
    SELF = ("self", "Self")
    INJURED = ("injured", "Injured Party")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/subscriber-relationship"


class CoverageClassCodes(AbstractStringEnum):
    """
    Coverage Class Codes

    This value set includes Coverage Class codes.

    group       An employee group
    subgroup    A sub-group of an employee group
    plan        A specific suite of benefits.
    subplan     A subset of a specific suite of benefits.
    class       A class of benefits.
    subclass    A subset of a class of benefits.
    sequence    A sequence number associated with a short-term continuance of
                the coverage.
    rxbin       Pharmacy benefit manager's Business Identification Number.
    rxpcn       A Pharmacy Benefit Manager specified Processor Control Number.
    rxid        A Pharmacy Benefit Manager specified Member ID.
    rxgroup     A Pharmacy Benefit Manager specified Group number.

    http://terminology.hl7.org/CodeSystem/coverage-class

    """

    GROUP = ("group", "Group")
    SUBGROUP = ("subgroup", "SubGroup")
    PLAN = ("plan", "Plan")
    SUBPLAN = ("subplan", "SubPlan")
    CLASS = ("class", "Class")
    SUBCLASS = ("subclass", "SubClass")
    SEQUENCE = ("sequence", "Sequence")
    RXBIN = ("rxbin", "RX BIN")
    RXPCN = ("rxpcn", "RX PCN")
    RXID = ("rxid", "RX Id")
    RXGROUP = ("rxgroup", "RX Group")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/coverage-class"


class CoverageCopayTypeCodes(AbstractStringEnum):
    """
    Coverage Copay Type

    Codes indicating the type of service for which a copay is specified and
    copayment maximum limit or rate. Copayment Type codes.

    gpvisit         An office visit for a general practitioner of a discipline.
    spvisit         An office visit for a specialist practitioner of a
                    discipline
    copaypct        A standard percentage applied to all classes or service or
                    product not otherwise specified.
    copay           A standard fixed currency amount applied to all classes or
                    service or product not otherwise specified.
    deductible      The accumulated amount of patient payment before the
                    coverage begins to pay for services.
    maxoutofpocket  The maximum amout of payment for services which a patient,
                    or family, is expected to incur - typically annually
    maxcopay        A maximum amout of payment for services which a patient is
                    expected to incur per episode.

    http://nphies.sa/terminology/CodeSystem/coverage-copay-type
    """

    GPVISIT = ("gpvisit", "GP Office Visit")
    SPVISIT = ("spvisit", "Specialist Office Visit")
    COPAYPCT = ("copaypct", "Copay Percentage")
    COPAY = ("copay", "Copay Amount")
    DEDUCTIBLE = ("deductible", "Deductible")
    MAXOUTOFPOCKET = ("maxoutofpocket", "Maximum out of pocket")
    MAXCOPAY = ("maxcopay", "maxcopay")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/coverage-copay-type"


class CoverageFinancialExceptionCodes(AbstractStringEnum):
    """
    Coverage Financial Exception

    This value set includes Coverage Financial Exception Codes.

    retired		Retired persons have all copays and deductibles reduced.
    foster		Children in the foster care have all copays and deductibles waived

    http://nphies.sa/terminology/CodeSystem/coverage-financial-exception
    """

    RETIRED = ("retired", "Retired")
    FOSTER = ("foster", "Foster child")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/coverage-financial-exception"


class BundleTypeCodes(AbstractStringEnum):
    """
    BundleType

    document:             The bundle is a document. The first resource is a
                          Composition.
    message:  	          The bundle is a message. The first resource is a
                          MessageHeader.
    transaction:          The bundle is a transaction - intended to be
                          processed by a server as an atomic commit.
    transaction-response: Transaction Response	The bundle is a transaction
                          response. Because the response is a transaction
                          response, the transaction has succeeded, and all
                          responses are error free.
    batch:              	The bundle is a set of actions - intended to be
                          processed by a server as a group of independent
                          actions.
    batch-response:       The bundle is a batch response. Note that as a batch,
                          some responses may indicate failure and others
                          success.
    history:              The bundle is a list of resources from a history
                          interaction on a server.
    searchset:            The bundle is a list of resources returned as a
                          result of a search/query interaction, operation, or
                          message.
    collection:           The bundle is a set of resources collected into a
                          single package for ease of distribution that imposes
                          no processing obligations or behavioral rules beyond
                          persistence.
    """

    DOCUMENT = ("document", "Document")
    MESSAGE = ("message", "Message")
    TRANSACTION = ("transaction", "Transaction")
    TRANSACTION_RESPONSE = ("transaction-response", "Transaction Response")
    BATCH = ("batch", "Batch")
    BATCH_RESPONSE = ("batch-response", "Batch Response")
    HISTORY = ("history", "History List")
    SEARCHSET = ("searchset", "Search Results")
    COLLECTION = ("collection", "Collection")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/bundle-type"


class NarrativeStatusCodes(AbstractStringEnum):
    """
    The status of a resource narrative.

    generated: The contents of the narrative are entirely generated from the
               core elements in the content.
    extension: The contents of the narrative are entirely generated from the
               core elements in the content and some of the content is
               generated from extensions. The narrative SHALL reflect the
               impact of all modifier extensions.
    additional: The contents of the narrative may contain additional
                information not found in the structured data. Note that there
                is no computable way to determine what the extra information
                is, other than by human inspection.
    empty: The contents of the narrative are some equivalent of
           "No human-readable text provided in this case".

    https://build.fhir.org/valueset-narrative-status.html
    """

    GENERATED = ("generated", "Generated")
    EXTENSION = ("extension", "Extension")
    ADDITIONAL = ("additional", "Additional")
    EMPTY = ("empty", "Empty")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/narrative-status"


class LensTypeCodes(AbstractStringEnum):
    """
    Lens Type

    Type of lens to be supplied for glasses or contacts.

    lens:     A lens to be fitted to a frame to comprise a pair of glasses.
    contact:  A lens to be fitted for wearing directly on an eye.

    http://nphies.sa/terminology/CodeSystem/lens-type
    """

    LENS = ("lens", "Lens")
    CONTACT = ("contact", "Contact")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/lens-type"


class VisionBaseCodes(AbstractStringEnum):
    """
    Vision Base

    A coded concept listing the base codes.

    up:     top.
    down:   bottom.
    in:     inner edge.
    out:    outer edge

    http://hl7.org/fhir/vision-base-codes
    """

    UP = ("up", "Top.")
    DOWN = ("down", "Bottom.")
    IN = ("in", "Inner edge.")
    OUT = ("out", "Outer edge")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/vision-base-codes"


class VisionEyesCodes(AbstractStringEnum):
    """
    Vision Eyes

    A coded concept listing the eye codes.

    right:  Right Eye.
    left:   Left Eye

    http://hl7.org/fhir/vision-eye-codes
    """

    RIGHT_EYE = ("right", "Right Eye.")
    LEFT_EYE = ("left", "Left Eye")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/vision-eye-codes"


class KSAMessageEventsCodes(AbstractStringEnum):
    """
    KSA Message Events
    The Saudi codeset for FHIR message events.

    Eligibility Request:            A message requesting the identified patients insurance, determination if the insurance is in force, and potentially requesting the table of benefits or other insurance details.
    Eligibility Response:	        A message responding to the Eligibility Request with errors or insurance details.
    Prior Authorization Request:    A request for prior authorization of products and services.
    Prior Authorization Response:   A response to a request for prior authorization of products and services.
    Claim Request:	                A request for adjudication of a claim for products and services.
    Claim Response:	                A response to a request for adjudication of a claim for products and services.
    Batch-Request:	                A request for adjudication of a batch of claims for products and services.
    Batch Response:	                A response for adjudication of a batch of claims for products and services.
    Status Check:	                A request to check on the processing status of a prior submission.
    Status Response:	            A response to a request to check on the processing status of a prior submission.
    Cancel Request:	                A request to cancel the processing, where complete or not,  of a prior submission such as a claim.
    Cancel Response:	            A response to request to cancel the processing, where complete or not,  of a prior submission such as a claim.
    Payment Notice:	                A notice providing the current status of a payment.
    Payment Reconciliation:	        A report of a payment and the allocation of the payment to the respective claims being settled.
    Communication Request:	        A request for supporting information for a previously submitted request.
    Communication:	                A provision of supporting information in response to a request or to support a prior submission.
    Acknowledgement:	            Message with just a MessageHeader, and optional referenced OperationOutcome if there are errors, to acknowledge the receipt of a request.
    Poll Request:	                A request for the next 'n' undelivered messages from the queue of undelivered messages for the requetor.
    Poll Response:	                A message responding to a poll-request containing up to 'n' requested undelivered messages.
    Advanced Authorization:	        A response without existing  request for prior authorization of products and services.
    Fraud Notification:	            A message from nphies to payer to notify about potential fraud existing in received claim
    Error Notice:	                A notice providing the error detected in the received message.

    http://nphies.sa/terminology/CodeSystem/ksa-message-events
    """

    ELIGIBILITY_REQUEST = ("eligibility-request", "Eligibility Request")
    ELIGIBILITY_RESPONSE = ("eligibility-response", "Eligibility Response")
    PRIORAUTH_REQUEST = ("priorauth-request", "Prior Authorization Request")
    PRIORAUTH_RESPONSE = ("priorauth-response", "Prior Authorization Response")
    CLAIM_REQUEST = ("claim-request", "Claim Request")
    CLAIM_RESPONSE = ("claim-response", "Claim Response")
    BATCH_REQUEST = ("batch-request", "Batch Request")
    BATCH_RESPONSE = ("batch-response", "Batch Response")
    STATUS_CHECK = ("status-check", "Status Check")
    STATUS_RESPONSE = ("status-response", "Status Response")
    CANCEL_REQUEST = ("cancel-request", "Cancel Request")
    CANCEL_RESPONSE = ("cancel-response", "Cancel Response")
    PAYMENT_NOTICE = ("payment-notice", "Payment Notice")
    PAYMENT_RECONCILIATION = ("payment-reconciliation", "Payment Reconciliation")
    COMMUNICATION_REQUEST = ("communication-request", "Communication Request")
    COMMUNICATION = ("communication", "Communication")
    ACKNOWLEDGEMENT = ("acknowledgement", "Acknowledgement")
    POLL_REQUEST = ("poll-request", "Poll Request")
    POLL_RESPONSE = ("poll-response", "Poll Response")
    ADVANCED_AUTHORIZATION = ("advanced-authorization", "Advanced Authorization")
    FRAUD_NOTIFICATION = ("fraud-notification", "Fraud Notification")
    ERROR_NOTICE = ("error-notice", "Error Notice")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/ksa-message-events"


class InfoReason(AbstractStringEnum):
    """
    InfoReason

    A code to indicate the reason for submitting the supporting information.

    Missing information:	Missing information that will be required for the adjudication and processing of the message
    Missing attachment: 	Missing attachment  that will be required for the adjudication and processing of the message
    Information correction:	Payer request to the provider to submitt a corrected information based on their agreement

    http://nphies.sa/terminology/CodeSystem/info-reason
    """

    MISSING_INFO = ("Missing-info", "Missing information")
    MISSING_ATTACH = ("Missing-attach", "Missing attachment")
    INFO_CORRECT = ("Info-correct", "Information correction")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/info-reason"


class EventStatus(AbstractStringEnum):
    """
    Event Status

    Codes identifying the lifecycle stage of an event.

    Preparation:	    The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation). Preparation stages may be tracked for billing purposes.
    In Progress:	    The event is currently occurring.
    Not Done:   	    The event was terminated prior to any activity beyond preparation. I.e. The 'main' activity has not yet begun. The boundary between preparatory and the 'main' activity is context-specific.
    On Hold:    	    The event has been temporarily stopped but is expected to resume in the future.
    Stopped:    	    The event was terminated prior to the full completion of the intended activity but after at least some of the 'main' activity (beyond preparation) has occurred.
    Completed:  	    The event has now concluded.
    Entered in Error:   This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "stopped" rather than "entered-in-error".).
    Unknown:        	The authoring/source system does not know which of the status values currently applies for this event. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.

    http://hl7.org/fhir/event-status
    """

    PREPARATION = ("preparation", "Preparation")
    IN_PROGRESS = ("in-progress", "In Progress")
    NOT_DONE = ("not-done", "Not Done")
    ON_HOLD = ("on-hold", "On Hold")
    STOPPED = ("stopped", "Stopped")
    COMPLETED = ("completed", "Completed")
    ENTERED_IN_ERROR = ("entered-in-error", "Entered in Error")
    UNKNOWN = ("unknown", "Unknown")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/event-status"


class CommunicationCategory(AbstractStringEnum):
    """
    CommunicationCategory

    Codes for general categories of communications such as alerts, instructions, etc.

    Alert:  	    The communication conveys an alert.
    Notification:	The communication conveys a notification.
    Reminder:   	The communication conveys a reminder.
    Instruction:   	The communication conveys an instruction
    Routine:        The request has normal priority.

    http://terminology.hl7.org/CodeSystem/communication-category
    """

    ALERT = ("alert", "Alert")
    NOTIFICATION = ("notification", "Notification")
    REMINDER = ("reminder", "Reminder")
    INSTRUCTION = ("instruction", "Instruction")
    ROUTINE = ("routine", "Routine")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/communication-category"


class RequestPriority(AbstractStringEnum):
    """
    Request Priority

    Identifies the level of importance to be assigned to actioning the request.

    Routine:	The request has normal priority.
    Urgent:	The request should be actioned promptly - higher priority than routine.
    ASAP:	The request should be actioned as soon as possible - higher priority than urgent.
    STAT:	The request should be actioned immediately - highest possible priority. E.g. an emergency

    http://hl7.org/fhir/request-priority
    """

    ROUTINE = ("routine", "Routine")
    URGENT = ("urgent", "Urgent")
    ASAP = ("asap", "ASAP")
    STAT = ("stat", "STAT")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/request-priority"


class ParticipationMode(AbstractStringEnum):
    """
    ParticipationMode

    Identifies the primary means by which an Entity participates in an Act.

    electronic data:	Participation by non-human-languaged based electronic signal
    physical presence:	Participation by direct action where subject and actor are in the same location. (The participation involves more than communication.)
    remote presence:	Participation by direct action where subject and actor are in separate locations, and the actions of the actor are transmitted by electronic or mechanical means. (The participation involves more than communication.)
    verbal:         	Participation by voice communication
    dictated:       	Participation by pre-recorded voice. Communication is limited to one direction (from the recorder to recipient).
    face-to-face:   	Participation by voice communication where parties speak to each other directly.
    telephone:      	Participation by voice communication where the voices of the communicating parties are transported over an electronic medium
    videoconferencing:	Participation by voice and visual communication where the voices and images of the communicating parties are transported over an electronic medium
    written:        	Participation by human language recorded on a physical material
    telefax:        	Participation by text or diagrams printed on paper that have been transmitted over a fax device
    handwritten:        Participation by text or diagrams printed on paper or other recording medium
    mail:           	Participation by text or diagrams printed on paper transmitted physically (e.g. by courier service, postal service).
    online written: 	Participation by text or diagrams submitted by computer network, e.g. online survey.
    email:          	Participation by text or diagrams transmitted over an electronic mail system.
    typewritten:    	Participation by text or diagrams printed on paper or other recording medium where the recording was performed using a typewriter, typesetter, computer or similar mechanism.

    http://terminology.hl7.org/CodeSystem/v3-ParticipationMode
    """

    ELECTRONIC = ("ELECTRONIC", "electronic data")
    PHYSICAL = ("PHYSICAL", "physical presence")
    REMOTE = ("REMOTE", "remote presence")
    VERBAL = ("VERBAL", "verbal")
    DICTATE = ("DICTATE", "dictated")
    FACE = ("FACE", "face-to-face")
    PHONE = ("PHONE", "telephone")
    VIDEOCONF = ("VIDEOCONF", "videoconferencing")
    WRITTEN = ("WRITTEN", "written")
    FAXWRIT = ("FAXWRIT", "telefax")
    HANDWRIT = ("HANDWRIT", "handwritten")
    MAILWRIT = ("MAILWRIT", "mail")
    ONLINEWRIT = ("ONLINEWRIT", "online written")
    EMAILWRIT = ("EMAILWRIT", "email")
    TYPEWRIT = ("TYPEWRIT", "typewritten")

    @classmethod
    def set_system_url(cls):
        return "http://terminology.hl7.org/CodeSystem/v3-ParticipationMode"


class CommunicationReason(AbstractStringEnum):
    """
    Communication Reason

    code indicating the reason or justification for the communication.

    Missing information:	Missing information that will be required for the adjudication and processing of the message
    Missing attachment:	    Missing attachment  that will be required for the adjudication and processing of the message
    Information correction:	Payer request to the provider to submitt a corrected information based on their agreement

    http://nphies.sa/terminology/CodeSystem/communication-reason
    """

    MISSING_INFO = ("missing-info", "Missing information")
    MISSING_ATTACH = ("missing-attach", "Missing attachment")
    INFO_CORRECT = ("info-correct", "Information correction")

    @classmethod
    def set_system_url(cls):
        return "http://nphies.sa/terminology/CodeSystem/communication-reason"


class RequestStatus(AbstractStringEnum):
    """
    RequestStatus

    Codes identifying the lifecycle stage of a request.

    Draft:	            The request has been created but is not yet complete or ready for action.
    Active:	            The request is in force and ready to be acted upon.
    On Hold:	        The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in the future.
    Revoked:	        The request (and any implicit authorization to act) has been terminated prior to the known full completion of the intended actions. No further activity should occur.
    Completed	        The activity described by the request has been fully performed. No further activity will occur.
    Entered in Error:	This request should never have existed and should be considered 'void'. (It is possible that real-world decisions were based on it. If real-world activity has occurred, the status should be "revoked" rather than "entered-in-error".).
    Unknown:	        The authoring/source system does not know which of the status values currently applies for this request. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.

    http://hl7.org/fhir/request-status
    """

    DRAFT = ("draft", "Draft")
    ACTIVE = ("active", "Active")
    ON_HOLD = ("on-hold", "On Hold")
    REVOKED = ("revoked", "Revoked")
    COMPLETED = ("completed", "Completed")
    ENTERED_IN_ERROR = ("entered-in-error", "Entered in Error")
    UNKNOWN = ("unknown", "Unknown")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/request-status"


class ClaimProcessingCodes(AbstractStringEnum):
    """
    Claim Processing Codes

    This value set includes Claim Processing Outcome codes.

    Queued:	    The Claim/Pre-authorization/Pre-determination has been received but processing has not begun.
    Processing: Complete	The processing has completed without errors
    Error:	    One or more errors have been detected in the Claim
    Partial:    Processing	No errors have been detected in the Claim and some of the adjudication has been performed.

    http://hl7.org/fhir/remittance-outcome
    """

    QUEUED = ("queued", "Queued")
    COMPLETE = ("complete", "Processing Complete")
    ERROR = ("error", "Error")
    PARTIAL = ("partial", "Partial Processing")

    @classmethod
    def set_system_url(cls):
        return "http://hl7.org/fhir/remittance-outcome"

class IssueTypeCodes(AbstractStringEnum):
    """
    A code that describes the type of issue for an OperationOutcome.
    """

    INVALID = ("invalid", "Invalid Content")
    STRUCTURE = ("structure", "Structural Issue")
    REQUIRED = ("required", "Required element missing")
    VALUE = ("value", "Element value invalid")
    INVARIANT = ("invariant", "Validation rule failed")
    SECURITY = ("security", "Security Problem")
    LOGIN = ("login", "Login Required")
    UNKNOWN = ("unknown", "Unknown User")
    EXPIRED = ("expired", "Session Expired")
    FORBIDDEN = ("forbidden", "Forbidden")
    SUPPRESSED = ("suppressed", "Information Suppressed")
    PROCESSING = ("processing", "Processing Failure")
    NOT_SUPPORTED = ("not-supported", "Content not supported")
    DUPLICATE = ("duplicate", "Duplicate")
    MULTIPLE_MATCHES = ("multiple-matches", "Multiple Matches")
    NOT_FOUND = ("not-found", "Not Found")
    DELETED = ("deleted", "Deleted")
    TOO_LONG = ("too-long", "Content Too Long")
    CODE_INVALID = ("code-invalid", "Invalid Code")
    EXTENSION = ("extension", "Unacceptable Extension")
    TOO_COSTLY = ("too-costly", "Operation Too Costly")
    BUSINESS_RULE = ("business-rule", "Business Rule Violation")
    CONFLICT = ("conflict", "Edit Version Conflict")
    LIMITED_FILTER = ("limited-filter", "Limited Filter Application")
    TRANSIENT = ("transient", "Transient Issue")
    LOCK_ERROR = ("lock-error", "Lock Error")
    NO_STORE = ("no-store", "No Store Available")
    EXCEPTION = ("exception", "Exception")
    TIMEOUT = ("timeout", "Timeout")
    INCOMPLETE = ("incomplete", "Incomplete Results")
    THROTTLED = ("throttled", "Throttled")
    INFORMATIONAL = ("informational", "Informational Note")
    SUCCESS = ("success", "Operation Successful")


    @classmethod
    def get_system_url(cls):
        return "https://www.hl7.org/fhir/valueset-issue-type.html"

class IssueSeverityCodes(AbstractStringEnum):
    """
    How the issue affects the success of the action for an OperationOutcome.
    """

    FATAL = ("fatal", "Fatal")
    ERROR = ("error", "Error")
    WARNING = ("warning", "Warning")
    INFORMATION = ("information", "Information")
    SUCCESS = ("success", "Success")

    @classmethod
    def get_system_url(cls):
        return "https://www.hl7.org/fhir/valueset-issue-severity.html"