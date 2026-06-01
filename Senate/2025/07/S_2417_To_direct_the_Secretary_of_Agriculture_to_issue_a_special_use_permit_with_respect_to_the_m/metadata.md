# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2417
- Title: Star-Spangled Summit Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2417
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-04-07T22:41:14Z
- Update date including text: 2026-04-07T22:41:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2417",
    "number": "2417",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Star-Spangled Summit Act of 2025",
    "type": "S",
    "updateDate": "2026-04-07T22:41:14Z",
    "updateDateIncludingText": "2026-04-07T22:41:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-23T22:41:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:22Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2417is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2417\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Curtis (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of Agriculture to issue a special use permit with respect to the maintaining of a flagpole bearing the flag of the United States at Kyhv Peak Lookout Point, Utah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Star-Spangled Summit Act of 2025 .\n#### 2. Special use permit for maintenance of covered flagpole at Kyhv Peak Lookout Point\n##### (a) Definitions\nIn this section:\n**(1) Covered flagpole**\nThe term covered flagpole means a flagpole bearing the flag of the United States.\n**(2) Kyhv Peak Lookout Point**\nThe term Kyhv Peak Lookout Point means the peak within the Uinta National Forest overlooking Utah Valley and located approximately at latitude 40\u00b016\u203218.14\u2033 N, longitude 111\u00b036\u203258.57\u2033 W.\n**(3) Qualified person**\nThe term qualified person means an individual that resides in, or a nonprofit entity or volunteer organization that carries out operations of the entity or organization in, Utah County, Utah, that has\u2014\n**(A)**\nexperience placing, maintaining, or otherwise caring for a covered flagpole; and\n**(B)**\nany other experience determined relevant by the Secretary.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Special use permit\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue a special use permit for a period of 10 years for the placing, if necessary, and maintenance of a covered flagpole at Kyhv Peak Lookout Point\u2014\n**(1)**\nto Robert S. Collins of Provo, Utah; or\n**(2)**\nif the individual described in paragraph (1) declines such permit, to a qualified person in accordance with this section.\n##### (c) Selection and issuance\n**(1) Application**\nExcept as provided in subsection (b)(1), to be eligible to be selected for a special use permit under this section, a qualified person shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Priority of issuance**\nExcept as provided in subsection (b)(1), in selecting a qualified person to receive a special use permit under this section, the Secretary shall prioritize the following qualified persons:\n**(A)**\nFirst, a qualified person that held a special use permit issued under this section for the preceding 10-year period.\n**(B)**\nSecond, a qualified person that the prior special use permit holder identifies.\n**(C)**\nThird, any other qualified person that submits an application under paragraph (1) that the Secretary determines appropriate.\n**(3) Terms and conditions**\nThe Secretary may impose such terms and conditions on a holder of a special use permit under this section as the Secretary determines necessary to ensure the proper care and maintenance of a covered flagpole.\n**(4) Land use fee exemption**\nThe Secretary shall not assess any land use fees with respect to a special use permit issued under this section.\n**(5) Notice of application**\nThe Secretary shall publish notice of the availability of any special use permit under this section on the website of the Forest Service and in a local Utah County, Utah, newspaper of record.\n##### (d) Subsequent special use permits\n**(1) In general**\nThe Secretary shall renew or issue a new 10-year special use permit not later than 180 days after the date that is the earliest of the following:\n**(A)**\nThe date that is 10 years after the date on which the Secretary issued the preceding permit.\n**(B)**\nThe date on which the holder of the current special use permit requests termination of such permit.\n**(C)**\nThe date on which a special use permit is subject to early termination under paragraph (2).\n**(2) Early termination**\nIf the Secretary determines that the holder of a special use permit under this section is not in compliance with the terms and conditions relating to such permit under subsection (c)(3), the Secretary may terminate the special use permit.\n##### (e) Limitation on holders of special use permit\nA holder of a special use permit under this section shall not accept anything of value in exchange for identifying a person under subsection (c)(2)(B).\n##### (f) Applicability of NEPA\nThe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) shall not apply to the issuance, renewal, or administration of a special use permit under this section, including any activities associated with the placing, maintenance, or removal of a covered flagpole at Kyhv Peak Lookout Point.\n##### (g) Access\nThe Secretary may authorize reasonable access to Kyhv Peak Lookout Point for the purpose of exercising rights under a special use permit issued under this section, subject to conditions necessary to protect public safety and natural resources.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-04-02",
        "text": "Placed on the Union Calendar, Calendar No. 504."
      },
      "number": "4684",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Star-Spangled Summit Act of 2026",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-23T18:23:36Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-23T18:23:36Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2026-01-23T18:23:36Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-01-23T18:23:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:06:43Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2417is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Star-Spangled Summit Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Star-Spangled Summit Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to issue a special use permit with respect to the maintaining of a flagpole bearing the flag of the United States at Kyhv Peak Lookout Point, Utah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:32Z"
    }
  ]
}
```
