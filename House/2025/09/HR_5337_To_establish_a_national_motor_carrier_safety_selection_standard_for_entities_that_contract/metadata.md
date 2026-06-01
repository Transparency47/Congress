# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5337?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5337
- Title: Motor Carrier Safety Selection Standard Act of 2024
- Congress: 119
- Bill type: HR
- Bill number: 5337
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-03-30T13:34:27Z
- Update date including text: 2026-03-30T13:34:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-12 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-12 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5337",
    "number": "5337",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Motor Carrier Safety Selection Standard Act of 2024",
    "type": "HR",
    "updateDate": "2026-03-30T13:34:27Z",
    "updateDateIncludingText": "2026-03-30T13:34:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-12",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-11T13:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-12T21:44:20Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5337ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5337\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Stauber introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish a national motor carrier safety selection standard for entities that contract with certain motor carriers to transport goods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Motor Carrier Safety Selection Standard Act of 2024 .\n#### 2. Motor carrier selection standard of care\n##### (a) Selection standard\n**(1) In general**\nFor any claim of negligent selection of a motor carrier against a covered entity with respect to the covered entity contracting with a covered motor carrier for the shipment of goods or household goods, the covered entity shall be considered reasonable and prudent in the selection of that covered motor carrier if, not later than the date of shipment and not earlier than 45 days before that date, the covered entity verifies that the covered motor carrier\u2014\n**(A)**\nis registered under section 13902 of title 49, United States Code, as a motor carrier or a household goods motor carrier;\n**(B)**\nhas at least the minimum insurance coverage required by Federal and State law; and\n**(C)**\nhas been confirmed by the Federal Motor Carrier Safety Administration, including through a public confirmation described in subsection (c)(1), to be in compliance with all required Federal Motor Carrier Safety Administration safety standards to operate as a motor carrier.\n**(2) Sunset**\nParagraph (1) shall cease to be effective on the effective date of a regulation promulgated under subsection (c)(1).\n##### (b) Public confirmation\nThe public confirmation described in paragraph (1)(C) shall include 1 of the following statements, depending on the status of the motor carrier:\n**(1)**\nThis motor carrier is confirmed to meet all operating requirements of the Federal Motor Carrier Safety Administration (FMCSA) and is authorized to operate on the nation\u2019s roadways. .\n**(2)**\nThis motor carrier is not confirmed to operate on the nation\u2019s roadways and fails to meet 1 or more requirements of the Federal Motor Carrier Safety Administration (FMCSA) to operate as a motor carrier. .\n##### (c) Safety fitness rule\n**(1) Rulemaking**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall promulgate final regulations amending appendix B to part 385 of title 49, Code of Federal Regulations (or a successor regulation), to revise the methodology for issuance of motor carrier safety fitness determinations.\n**(2) Considerations**\nIn promulgating the regulations under paragraph (1), the Secretary shall consider the use of all available data to determine the fitness of a motor carrier.\n**(3) Factors for an unfit determination**\nThe regulations promulgated under paragraph (1) shall provide a procedure for the Secretary to determine whether a motor carrier is not fit to operate a commercial motor vehicle in or affecting interstate commerce in accordance with section 31144 of title 49, United States Code.\n**(4) Requirement**\nThe regulations promulgated under paragraph (1) shall include the requirements described in subsections (a)(1) and (b).\n##### (d) Exemption for individual shippers\nFor any claim of negligent selection of a motor carrier against a person acting as an individual shipper with respect to that person contracting with a covered motor carrier for the shipment of goods or household goods, that person shall, on demonstration that the person contracted with a covered motor carrier, be considered reasonable and prudent in the selection of that covered motor carrier without having to satisfy any of the requirements described in subsection (a)(1) (or any similar requirement in the regulations promulgated under subsection (c)(1)).\n##### (e) Savings clause\nNothing in this Act preempts or supersedes any State law (including regulations) relating to drayage.\n##### (f) Definitions\nIn this section:\n**(1) Covered entity**\n**(A) In general**\nThe term covered entity means a person acting as\u2014\n**(i)**\nexcept as provided in subparagraph (B), a shipper or consignee of goods;\n**(ii)**\na broker, a freight forwarder, or a household goods freight forwarder (as those terms are defined in section 13102 of title 49, United States Code);\n**(iii)**\nan ocean transportation intermediary (as defined in section 40102 of title 46, United States Code), when arranging for inland transportation as part of an international through movement involving ocean transportation between the United States and a foreign port;\n**(iv)**\nan indirect air carrier holding a Standard Security Program approved by the Transportation Security Administration, only to the extent that the person acting as an indirect air carrier is engaging in\u2014\n**(I)**\nactivities as an air carrier (as defined in section 40102 of title 49, United States Code); or\n**(II)**\nair commerce (as defined in that section);\n**(v)**\na customs broker licensed in accordance with section 111.2 of title 19, Code of Federal Regulations (or a successor regulation), only to the extent that the person acting as a customs broker is engaging in\u2014\n**(I)**\na movement under a customs bond; or\n**(II)**\na transaction involving customs business (as defined in section 111.1 of that title (or a successor regulation)); or\n**(vi)**\na motor carrier registered under chapter 139 of title 49, United States Code.\n**(B) Exclusion**\nThe term covered entity does not include a person acting as an individual shipper.\n**(2) Covered motor carrier**\nThe term covered motor carrier means a motor carrier or a household goods motor carrier that is subject to Federal motor carrier financial responsibility and safety regulations, except for motor carriers that operate commercial motor vehicles of passengers, as defined in section 31101(1)(B) of 49, United States Code.\n**(3) Household goods**\nThe term household goods has the meaning given the term in section 13102 of title 49, United States Code.\n**(4) Household goods motor carrier**\nThe term household goods motor carrier has the meaning given the term in section 13102 of title 49, United States Code.\n**(5) Individual shipper**\nThe term individual shipper has the meaning given the term in section 13102 of title 49, United States Code.\n**(6) Motor carrier**\nThe term motor carrier has the meaning given the term in section 13102 of title 49, United States Code, except for motor carriers that operate commercial motor vehicles of passengers, as defined in section 31101(1)(B) of 49, United States Code.\n**(7) Secretary**\nThe term Secretary means the Secretary of Transportation.",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-25T14:14:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr5337",
          "measure-number": "5337",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5337v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Motor Carrier Safety Selection Standard Act of 2024</strong></p><p>This bill establishes a standard of care for the selection of brokers and other entities that contract with motor carriers (e.g., trucking companies) for the shipment of goods or household goods. (A broker is the middle person between a shipper and a motor carrier. Brokers arrange for the transportation of property or household goods.)</p><p>Specifically, the bill requires such entities to verify that a transporting motor carrier (1) is properly registered with the Department of Transportation (DOT); (2) has obtained the minimum required insurance coverage; and (3) is in compliance with all Federal Motor Carrier Safety Administration safety standards, including through a public confirmation statement. Entities that comply with the verification requirements shall be considered reasonable and prudent in the selection of a covered motor carrier (for the purposes of a claim of negligent selection of a motor carrier).\u00a0</p><p>Further, DOT must promulgate final regulations that revise the methodology for issuing motor carrier safety fitness determinations. The regulations must provide a procedure for DOT to determine whether a motor carrier is not fit to operate a commercial motor vehicle that is in, or affects, interstate commerce.\u00a0</p><p>The bill exempts from the verification requirements an individual shipper (i.e., a shipper that owns the goods being transported and pays the tariff transportation charges) that contracts with a covered motor carrier.</p>"
        },
        "title": "Motor Carrier Safety Selection Standard Act of 2024"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5337.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Motor Carrier Safety Selection Standard Act of 2024</strong></p><p>This bill establishes a standard of care for the selection of brokers and other entities that contract with motor carriers (e.g., trucking companies) for the shipment of goods or household goods. (A broker is the middle person between a shipper and a motor carrier. Brokers arrange for the transportation of property or household goods.)</p><p>Specifically, the bill requires such entities to verify that a transporting motor carrier (1) is properly registered with the Department of Transportation (DOT); (2) has obtained the minimum required insurance coverage; and (3) is in compliance with all Federal Motor Carrier Safety Administration safety standards, including through a public confirmation statement. Entities that comply with the verification requirements shall be considered reasonable and prudent in the selection of a covered motor carrier (for the purposes of a claim of negligent selection of a motor carrier).\u00a0</p><p>Further, DOT must promulgate final regulations that revise the methodology for issuing motor carrier safety fitness determinations. The regulations must provide a procedure for DOT to determine whether a motor carrier is not fit to operate a commercial motor vehicle that is in, or affects, interstate commerce.\u00a0</p><p>The bill exempts from the verification requirements an individual shipper (i.e., a shipper that owns the goods being transported and pays the tariff transportation charges) that contracts with a covered motor carrier.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr5337"
    },
    "title": "Motor Carrier Safety Selection Standard Act of 2024"
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Motor Carrier Safety Selection Standard Act of 2024</strong></p><p>This bill establishes a standard of care for the selection of brokers and other entities that contract with motor carriers (e.g., trucking companies) for the shipment of goods or household goods. (A broker is the middle person between a shipper and a motor carrier. Brokers arrange for the transportation of property or household goods.)</p><p>Specifically, the bill requires such entities to verify that a transporting motor carrier (1) is properly registered with the Department of Transportation (DOT); (2) has obtained the minimum required insurance coverage; and (3) is in compliance with all Federal Motor Carrier Safety Administration safety standards, including through a public confirmation statement. Entities that comply with the verification requirements shall be considered reasonable and prudent in the selection of a covered motor carrier (for the purposes of a claim of negligent selection of a motor carrier).\u00a0</p><p>Further, DOT must promulgate final regulations that revise the methodology for issuing motor carrier safety fitness determinations. The regulations must provide a procedure for DOT to determine whether a motor carrier is not fit to operate a commercial motor vehicle that is in, or affects, interstate commerce.\u00a0</p><p>The bill exempts from the verification requirements an individual shipper (i.e., a shipper that owns the goods being transported and pays the tariff transportation charges) that contracts with a covered motor carrier.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr5337"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5337ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Motor Carrier Safety Selection Standard Act of 2024",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Motor Carrier Safety Selection Standard Act of 2024",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a national motor carrier safety selection standard for entities that contract with certain motor carriers to transport goods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:25Z"
    }
  ]
}
```
