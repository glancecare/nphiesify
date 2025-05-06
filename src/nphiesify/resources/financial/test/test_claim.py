import json

from nphiesify.resources.financial.billing import Claim


class TestClaimLoad:
    def test_claim_request(self):
        claim_str = '''
        {
          "resourceType": "Claim",
          "id": "177363",
          "meta": {
            "profile": [
              "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/professional-priorauth|1.0.0"
            ]
          },
          "extension": [
            {
              "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-transfer",
              "valueBoolean": true
            }
          ],
          "identifier": [
            {
              "system": "http://sgh.com.sa/authorization",
              "value": "req_177363"
            }
          ],
          "status": "active",
          "type": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/claim-type",
                "code": "professional"
              }
            ]
          },
          "subType": {
            "coding": [
              {
                "system": "http://nphies.sa/terminology/CodeSystem/claim-subtype",
                "code": "op"
              }
            ]
          },
          "use": "preauthorization",
          "patient": {
            "reference": "http://sgh.com.sa/Patient/123454186"
          },
          "created": "2021-10-07",
          "insurer": {
            "reference": "http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db"
          },
          "provider": {
            "reference": "http://sgh.com.sa/Organization/b1b3432921324f97af3be9fd0b1a14ae"
          },
          "priority": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/processpriority",
                "code": "normal"
              }
            ]
          },
          "payee": {
            "type": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/payeetype",
                  "code": "provider"
                }
              ]
            }
          },
          "careTeam": [
            {
              "sequence": 1,
              "provider": {
                "reference": "http://sgh.com.sa/Practitioner/7"
              },
              "role": {
                "coding": [
                  {
                    "system": "http://terminology.hl7.org/CodeSystem/claimcareteamrole",
                    "code": "primary"
                  }
                ]
              },
              "qualification": {
                "coding": [
                  {
                    "system": "http://nphies.sa/terminology/CodeSystem/practice-codes",
                    "code": "08.26"
                  }
                ]
              }
            }
          ],
          "supportingInfo": [
            {
              "sequence": 1,
              "category": {
                "coding": [
                  {
                    "system": "http://nphies.sa/terminology/CodeSystem/claim-information-category",
                    "code": "reason-for-visit"
                  }
                ]
              },
              "code": {
                "coding": [
                  {
                    "system": "http://nphies.sa/terminology/CodeSystem/visit-reason",
                    "code": "new-visit"
                  }
                ]
              }
            }
          ],
          "diagnosis": [
            {
              "sequence": 1,
              "diagnosisCodeableConcept": {
                "coding": [
                  {
                    "system": "http://hl7.org/fhir/sid/icd-10-am",
                    "code": "S83.1"
                  }
                ]
              },
              "type": [
                {
                  "coding": [
                    {
                      "system": "http://nphies.sa/terminology/CodeSystem/diagnosis-type",
                      "code": "principal"
                    }
                  ]
                }
              ]
            }
          ],
          "insurance": [
            {
              "sequence": 1,
              "focal": true,
              "coverage": {
                "reference": "http://sgh.com.sa/Coverage/1333"
              }
            }
          ],
          "item": [
            {
              "sequence": 1,
              "careTeamSequence": [
                1
              ],
              "diagnosisSequence": [
                1
              ],
              "extension": [
                {
                  "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-tax",
                  "valueMoney": {
                    "value": 15.9,
                    "currency": "SAR"
                  }
                },
                {
                  "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-patient-share",
                  "valueMoney": {
                    "value": 0,
                    "currency": "SAR"
                  }
                },
                {
                  "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-package",
                  "valueBoolean": false
                }
              ],
              "productOrService": {
                "coding": [
                  {
                    "system": "http://nphies.sa/terminology/CodeSystem/services",
                    "code": "83620-00-10",
                    "display": "Physio Therapy"
                  }
                ]
              },
              "servicedDate": "2021-10-07",
              "quantity": {
                "value": 1
              },
              "unitPrice": {
                "value": 106,
                "currency": "SAR"
              },
              "net": {
                "value": 121.9,
                "currency": "SAR"
              }
            }
          ],
          "total": {
            "value": 121.9,
            "currency": "SAR"
          }
        }
        '''
        claim_obj = json.loads(claim_str)
        m = Claim(**claim_obj)
        assert m.resourceType == "Claim"
