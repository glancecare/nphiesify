import json

from nphiesify.resources.foundation.other import MessageHeader


class TestMessageHeader:
    def test_valid_data(self):
        message_header_json_str = '''
          {
            "resourceType": "MessageHeader",
            "id": "ad9317fe-a883-4f43-bcc8-b5a242fd9051",
            "meta": {
              "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/message-header|1.0.0"
              ]
            },
            "eventCoding": {
              "system": "http://nphies.sa/terminology/CodeSystem/ksa-message-events",
              "code": "priorauth-response"
            },
            "destination": [
              {
                "endpoint": "http://saudidentalclinic.com.sa/N-F-00003",
                "receiver": {
                  "type": "Organization",
                  "identifier": {
                    "system": "http://nphies.sa/license/provider-license",
                    "value": "N-F-00003"
                  }
                }
              }
            ],
            "sender": {
              "type": "Organization",
              "identifier": {
                "system": "http://nphies.sa/license/payer-license",
                "value": "N-I-00001"
              }
            },
            "source": {
              "endpoint": "http://nphies.sa/license/payer-license/N-I-00001"
            },
            "response": {
              "identifier": "54cf5884-662c-4f1d-85a2-a4a923a99051",
              "code": "ok"
            },
            "focus": [
              {
                "reference": "http://sni.com.sa/Claimresponse/619051"
              }
            ]
          }
          '''
        message_obj = json.loads(message_header_json_str)
        m = MessageHeader(**message_obj)
        assert m.model_dump(exclude_none=True) == message_obj
