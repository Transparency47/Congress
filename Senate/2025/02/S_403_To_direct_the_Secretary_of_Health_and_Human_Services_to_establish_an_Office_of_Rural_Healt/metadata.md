# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/403
- Title: Rural Health Focus Act
- Congress: 119
- Bill type: S
- Bill number: 403
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-01-14T16:35:57Z
- Update date including text: 2026-01-14T16:35:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/403",
    "number": "403",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Rural Health Focus Act",
    "type": "S",
    "updateDate": "2026-01-14T16:35:57Z",
    "updateDateIncludingText": "2026-01-14T16:35:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T16:15:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "GA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s403is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 403\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mrs. Hyde-Smith (for herself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Health Focus Act .\n#### 2. CDC Office of Rural Health\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, shall establish within the Centers for Disease Control and Prevention an office to be known as the Office of Rural Health, to be headed by a director selected by the Director of the Centers for Disease Control and Prevention.\n##### (b) Duties and authorities\nThe duties and authorities of the Director of the Office of Rural Health shall be limited to the following:\n**(1)**\nServing as the primary point of contact in the Centers for Disease Control and Prevention on matters pertaining to rural health.\n**(2)**\nAssisting the Director of the Centers for Disease Control and Prevention in conducting, coordinating, and promoting research regarding public health issues affecting rural populations, and in disseminating the results of such research.\n**(3)**\nWorking with all personnel and offices of the Centers for Disease Control and Prevention to develop, refine, coordinate, and promulgate policies, best practices, lessons learned, and innovative, successful programs to improve care and services (including through telehealth) for rural populations.\n**(4)**\nCoordinating and supporting rural health research, conducting and supporting educational outreach, and disseminating evidence-based interventions related to health outcomes, access to health care, and lifestyle challenges, to prevent death, disease, injury, and disability, and promote healthy behaviors in rural populations.\n**(5)**\nImproving the understanding of the health challenges faced by rural populations.\n**(6)**\nIdentifying disparities in the availability of health care and public health interventions for rural populations.\n**(7)**\nAwarding and administering grants, cooperative agreements, and contracts to provide technical assistance and other activities as necessary to support activities related to improving health and health care in rural areas.\n**(8)**\nCoordinating with the Federal Office of Rural Health Policy of the Health Resources and Services Administration, as needed, to facilitate cooperation on rural health initiatives and avoid duplication of efforts.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-04-30",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3102",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-14T16:35:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s403",
          "measure-number": "403",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s403v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Health Focus Act</strong></p><p>This bill provides statutory authority for the Office of Rural Health (ORH) within the Centers for Disease Control and Prevention (CDC). The\u00a0CDC established the ORH in 2023 in response to a congressional directive, and it currently leads the CDC\u2019s rural public health strategy.</p><p>Specifically, the bill requires the CDC to establish the ORH and select a director to head the ORH. The bill specifies the duties and authorities of the\u00a0ORH director, including improving understanding of particular challenges and implementing programs to improve health care for rural populations.\u00a0</p>"
        },
        "title": "Rural Health Focus Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s403.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Health Focus Act</strong></p><p>This bill provides statutory authority for the Office of Rural Health (ORH) within the Centers for Disease Control and Prevention (CDC). The\u00a0CDC established the ORH in 2023 in response to a congressional directive, and it currently leads the CDC\u2019s rural public health strategy.</p><p>Specifically, the bill requires the CDC to establish the ORH and select a director to head the ORH. The bill specifies the duties and authorities of the\u00a0ORH director, including improving understanding of particular challenges and implementing programs to improve health care for rural populations.\u00a0</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s403"
    },
    "title": "Rural Health Focus Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Health Focus Act</strong></p><p>This bill provides statutory authority for the Office of Rural Health (ORH) within the Centers for Disease Control and Prevention (CDC). The\u00a0CDC established the ORH in 2023 in response to a congressional directive, and it currently leads the CDC\u2019s rural public health strategy.</p><p>Specifically, the bill requires the CDC to establish the ORH and select a director to head the ORH. The bill specifies the duties and authorities of the\u00a0ORH director, including improving understanding of particular challenges and implementing programs to improve health care for rural populations.\u00a0</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s403"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s403is.xml"
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
      "title": "Rural Health Focus Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Health Focus Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:53Z"
    }
  ]
}
```
