# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1514
- Title: Quinault Indian Nation Land Transfer Act
- Congress: 119
- Bill type: S
- Bill number: 1514
- Origin chamber: Senate
- Introduced date: 2025-04-29
- Update date: 2025-11-30T06:57:25Z
- Update date including text: 2025-11-30T06:57:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in Senate
- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-04-29: Introduced in Senate

## Actions

- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1514",
    "number": "1514",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Quinault Indian Nation Land Transfer Act",
    "type": "S",
    "updateDate": "2025-11-30T06:57:25Z",
    "updateDateIncludingText": "2025-11-30T06:57:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T20:02:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1514is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1514\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2025 Ms. Cantwell (for herself and Mrs. Murray ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo take certain land in the State of Washington into trust for the benefit of the Quinault Indian Nation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quinault Indian Nation Land Transfer Act .\n#### 2. Land taken into trust for the benefit of the Quinault Indian Nation\n##### (a) In general\nSubject to valid existing rights, the approximately 72 acres of land located in the State of Washington and generally depicted as Allotment 1157 on the map entitled Quinault Indian Nation Land Transfer Act and dated February 2, 2024, shall be administratively transferred from the Forest Service to the Department of the Interior and taken into trust for the benefit of the Quinault Indian Nation.\n##### (b) Land part of reservation; Administration\nThe land taken into trust under subsection (a) shall be\u2014\n**(1)**\npart of the Quinault Indian Reservation; and\n**(2)**\nadministered by the Secretary of the Interior in accordance with the laws and regulations generally applicable to property held in trust by the United States for an Indian Tribe.\n##### (c) Gaming prohibited\nThe land taken into trust under subsection (a) shall not be eligible for gaming under the Indian Gaming Regulatory Act ( 25 U.S.C. 2701 et seq. ).\n##### (d) No impact on treaty rights\nNothing in this Act affects treaty rights under the Treaty between the United States and the Qui-nai-elt and Quil-leh-ute Indians, done at the Qui-nai-elt River July 1, 1855, and Olympia January 25, 1856 (12 Stat. 971) (commonly known as the Treaty of Olympia ).\n##### (e) Hazardous materials\nFor purposes of the taking of land into trust under subsection (a), the Secretary of the Interior\u2014\n**(1)**\nshall meet disclosure requirements for hazardous substances, pollutants, or contaminants under section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(2)**\nshall not otherwise be required to remediate or abate those hazardous substances, pollutants, or contaminants.",
      "versionDate": "2025-04-29",
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
        "actionDate": "2025-09-15",
        "text": "Placed on the Union Calendar, Calendar No. 244."
      },
      "number": "2389",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Quinault Indian Nation Land Transfer Act",
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
            "name": "Federal-Indian relations",
            "updateDate": "2025-05-20T19:13:28Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-05-20T19:13:28Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-05-20T19:13:28Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2025-05-20T19:13:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-23T12:37:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s1514",
          "measure-number": "1514",
          "measure-type": "s",
          "orig-publish-date": "2025-04-29",
          "originChamber": "SENATE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1514v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Quinault Indian Nation Land Transfer Act</strong></p><p>This bill administratively transfers approximately 72 acres of specified lands in Washington from the U.S. Forest Service to the Department of the Interior. Interior must take this land into trust for the benefit of the Quinault Indian Nation. Land taken into trust shall be part of the tribe's reservation.</p><p>The bill prohibits gaming on the land taken into trust.</p><p>The bill requires Interior, for purposes of taking the land into trust, to meet the disclosure requirements for hazardous substances, pollutants, or contaminants, without otherwise being required to\u00a0remediate or abate those hazardous substances, pollutants, or contaminants.</p>"
        },
        "title": "Quinault Indian Nation Land Transfer Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1514.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Quinault Indian Nation Land Transfer Act</strong></p><p>This bill administratively transfers approximately 72 acres of specified lands in Washington from the U.S. Forest Service to the Department of the Interior. Interior must take this land into trust for the benefit of the Quinault Indian Nation. Land taken into trust shall be part of the tribe's reservation.</p><p>The bill prohibits gaming on the land taken into trust.</p><p>The bill requires Interior, for purposes of taking the land into trust, to meet the disclosure requirements for hazardous substances, pollutants, or contaminants, without otherwise being required to\u00a0remediate or abate those hazardous substances, pollutants, or contaminants.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s1514"
    },
    "title": "Quinault Indian Nation Land Transfer Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Quinault Indian Nation Land Transfer Act</strong></p><p>This bill administratively transfers approximately 72 acres of specified lands in Washington from the U.S. Forest Service to the Department of the Interior. Interior must take this land into trust for the benefit of the Quinault Indian Nation. Land taken into trust shall be part of the tribe's reservation.</p><p>The bill prohibits gaming on the land taken into trust.</p><p>The bill requires Interior, for purposes of taking the land into trust, to meet the disclosure requirements for hazardous substances, pollutants, or contaminants, without otherwise being required to\u00a0remediate or abate those hazardous substances, pollutants, or contaminants.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s1514"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1514is.xml"
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
      "title": "Quinault Indian Nation Land Transfer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quinault Indian Nation Land Transfer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to take certain land in the State of Washington into trust for the benefit of the Quinault Indian Nation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:30Z"
    }
  ]
}
```
