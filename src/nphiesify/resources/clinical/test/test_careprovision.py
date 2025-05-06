import json

from nphiesify.resources.clinical.careprovision import VisionPrescription


class TestCareProvisionLoad:
    def test_vision_prescription_data(self):
        json_str = """
        {
            "resourceType": "VisionPrescription",
            "id": "1",
            "meta": {
              "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/vision-prescription|1.0.0"
              ]
            },
            "identifier": [
              {
                "system": "http://saudiopticalclinic.com.sa/visionprescription",
                "value": "2199055"
              }
            ],
            "status": "active",
            "created": "2021-08-28T14:56:49.034+03:00",
            "patient": {
              "reference": "http://saudiopticalclinic.com.sa/Patient/3"
            },
            "dateWritten": "2021-08-29T14:56:49.034+03:00",
            "prescriber": {
              "reference": "http://saudiopticalclinic.com.sa/Practitioner/7"
            },
            "lensSpecification": [
              {
                "product": {
                  "coding": [
                    {
                      "system": "http://nphies.sa/terminology/CodeSystem/lens-type",
                      "code": "lens"
                    }
                  ]
                },
                "eye": "left",
                "sphere": 1.5,
                "cylinder": 0.75,
                "axis": 110,
                "prism": [
                  {
                    "amount": 2,
                    "base": "up"
                  }
                ]
              },
              {
                "product": {
                  "coding": [
                    {
                      "system": "http://nphies.sa/terminology/CodeSystem/lens-type",
                      "code": "lens"
                    }
                  ]
                },
                "eye": "right",
                "sphere": 2.25,
                "cylinder": 0.75,
                "axis": 80
              }
            ]
        }
        """

        claim_obj = json.loads(json_str)
        m = VisionPrescription(**claim_obj)
        assert m.resourceType == "VisionPrescription"
