# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3907
- Title: ENROLL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3907
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-12-05T21:38:17Z
- Update date including text: 2025-12-05T21:38:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3907",
    "number": "3907",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "ENROLL Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:38:17Z",
    "updateDateIncludingText": "2025-12-05T21:38:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3907ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3907\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Ms. Castor of Florida (for herself and Mr. Evans of Pennsylvania ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Patient Protection and Affordable Care Act to provide for additional requirements with respect to the navigator program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expand Navigators\u2019 Resources for Outreach, Learning, and Longevity Act of 2025 or the ENROLL Act of 2025 .\n#### 2. Providing for additional requirements with respect to the navigator program\n##### (a) In general\nSection 1311(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(i) ) is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(C) Selection of recipients In the case of an Exchange established and operated by the Secretary within a State pursuant to section 1321(c), in awarding grants under paragraph (1), the Exchange shall\u2014 (i) select entities to receive such grants based on an entity\u2019s demonstrated capacity to carry out each of the duties specified in paragraph (3); (ii) not take into account whether or not the entity has demonstrated how the entity will provide information to individuals relating to group health plans that are not qualified health plans; and (iii) ensure that, each year, the Exchange awards such a grant to at least 1 entity described in this paragraph that is a community and consumer-focused nonprofit group. ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (C), by inserting after qualified health plans the following: , State Medicaid plans under title XIX of the Social Security Act, and State children\u2019s health insurance programs under title XXI of such Act ;\n**(B)**\nin subparagraph (D), by striking and at the end;\n**(C)**\nin subparagraph (E), by striking the period and inserting ; and ;\n**(D)**\nby adding at the end the following:\n(F) conduct public education activities in plain language to raise awareness of the requirements of and the protections provided under qualified health plans. ; and\n**(E)**\nby adding at the end the following flush left sentence:\nThe duties specified in the preceding sentence may be carried out by such a navigator at any time during a year.\n**(3)**\nin paragraph (4)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by striking not ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nby inserting not before be ; and\n**(ii)**\nby striking ; or and inserting a semicolon;\n**(C)**\nin clause (ii)\u2014\n**(i)**\nby inserting not before receive ; and\n**(ii)**\nby striking the period and inserting a semicolon; and\n**(D)**\nby adding at the end the following new clause:\n(iii) maintain physical presence in the State of the Exchange so as to allow in-person assistance to consumers. ; and\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nby striking Funding .\u2014Grants under and inserting\nFunding .\u2014 (A) State Exchanges Grants under ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) Federal Exchanges For purposes of carrying out this subsection, with respect to an Exchange established and operated by the Secretary within a State pursuant to section 1321(c), the Secretary shall obligate $100,000,000 out of amounts collected through the user fees on participating health insurance issuers pursuant to section 156.50 of title 45, Code of Federal Regulations (or any successor regulations) for fiscal year 2026 and each subsequent fiscal year. Such amount for a fiscal year shall remain available until expended. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-06-11",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2024",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ENROLL Act of 2025",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2025-07-01T12:53:33Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3907ih.xml"
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
      "title": "ENROLL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ENROLL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expand Navigators\u2019 Resources for Outreach, Learning, and Longevity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Patient Protection and Affordable Care Act to provide for additional requirements with respect to the navigator program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T06:18:28Z"
    }
  ]
}
```
