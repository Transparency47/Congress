# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3034
- Title: Reliable Power Act
- Congress: 119
- Bill type: S
- Bill number: 3034
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3034",
    "number": "3034",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Reliable Power Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
          "date": "2025-10-23T14:36:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-15T19:37:24Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3034is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3034\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Power Act to require the Federal Energy Regulatory Commission to review regulations that may affect the reliable operation of the bulk-power system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reliable Power Act .\n#### 2. Commission review and comment for covered agency actions\nSection 215 of the Federal Power Act ( 16 U.S.C. 824o ) is amended\u2014\n**(1)**\nin subsection (g)\u2014\n**(A)**\nby striking The ERO and inserting the following:\n(1) In general The ERO ; and\n**(B)**\nby adding at the end the following:\n(2) Annual long-term assessment The assessments under paragraph (1) shall include an annual long-term assessment, which shall include\u2014 (A) an analysis of the ability of the bulk-power system to supply sufficient electric energy to maintain an adequate level of reliability, taking into account\u2014 (i) generation resource mix; (ii) transmission development; and (iii) electric energy demand trends; (B) an analysis of\u2014 (i) the risk of future electric energy supply shortfalls under normal and extreme weather conditions; and (ii) the risk of any such shortfalls within each region of the bulk-power system; and (C) a determination of whether additional generation resources are necessary to supply sufficient electric energy to maintain an adequate level of reliability during the assessment period. (3) Notice of generation inadequacy In conducting a long-term assessment under paragraph (2), if the ERO determines that the bulk-power system is at risk of not having adequate generation resources to supply sufficient electric energy to maintain an adequate level of reliability, the ERO shall publicly notify the Commission that the bulk-power system is in a state of generation inadequacy. (4) Data collection To conduct a long-term assessment under paragraph (2), the ERO may collect information and data from users, owners, and operators of the bulk-power system. ;\n**(2)**\nby redesignating subsections (h) through (k) as subsections (i) through (l), respectively; and\n**(3)**\nby inserting after subsection (g) the following:\n(h) Commission review and comment for covered agency actions (1) Definitions In this subsection: (A) Covered agency action The term covered agency action means a regulation that\u2014 (i) relates to, or otherwise directly affects, any generation resource in the bulk-power system; and (ii) on the date on which the applicable Federal agency receives notice from the Commission under paragraph (2)\u2014 (I) is under development to be proposed; or (II) is otherwise under consideration in a rulemaking proceeding. (B) Federal agency The term Federal agency means an Executive department (as defined in section 101 of title 5, United States Code) or any other Executive agency the head of which holds a Cabinet-level position. (2) Notice to Federal agencies If the ERO notifies the Commission under subsection (g)(3) that the bulk-power system is in a state of generation inadequacy, the Commission shall promptly notify the Department of Energy, the Environmental Protection Agency, and any other Federal agency the Commission determines appropriate of that state of generation inadequacy. (3) Submission of covered agency actions to the Commission (A) In general Not later than the applicable date described in subparagraph (B), the head of each Federal agency that receives a notification under paragraph (2) shall submit to the Commission for review and comment any covered agency action of the Federal agency. (B) Date described The date referred to in subparagraph (A) is\u2014 (i) the first date on which the applicable covered agency action is provided to the Office of Management and Budget or any other Federal agency for review and comment; (ii) if the applicable covered agency action is not provided to the Office of Management and Budget or any other Federal agency for review and comment, the date that is 90 days before the date on which the covered agency action is published in the Federal Register or otherwise made available for public inspection or comment; or (iii) if, as of the date on which the Federal agency receives the applicable notification under paragraph (2), the covered agency action has already been provided to the Office of Management and Budget or any other Federal agency for review and comment, or has already been published in the Federal Register or otherwise made available for public inspection or comment, the date that is 60 days after the date on which the Federal agency received the notification. (4) Commission comments The Commission, in consultation with the ERO and transmission organizations, shall, by order, provide to the Federal agency head that submitted to the Commission a covered agency action under paragraph (3)\u2014 (A) comments on the covered agency action, which may include an assessment of the effect of the covered agency action on rates, terms, and conditions for services pursuant to the authority of the Commission under sections 201 and 206; and (B) if applicable, recommendations for modifications to the covered agency action to prevent a significant negative impact on the ability of the bulk-power system to supply sufficient electric energy to maintain an adequate level of reliability. (5) Agency response The head of a Federal agency may not finalize a covered agency action that is submitted to the Commission under paragraph (3) until\u2014 (A) the agency head responds in writing to the Commission with an explanation of how the agency head modified, or why the agency head determined not to modify, the covered agency action in response to any comments and recommendations provided by the Commission under paragraph (4); and (B) the Commission determines that the covered agency action is not likely to have a significant negative impact on the ability of the bulk-power system to supply sufficient electric energy to maintain an adequate level of reliability. (6) Public availability of comments and responses A Federal agency head shall include any comments, recommendations, and responses relating to the covered agency action under paragraphs (4) and (5) in\u2014 (A) any submission of the covered agency action to the Federal Register for publication; and (B) any other place in which the covered agency action is otherwise made available for public inspection or comment. .",
      "versionDate": "2025-10-23",
      "versionType": "Introduced in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-29T17:42:33Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-29T17:42:33Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2026-04-29T17:42:33Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-04-29T17:42:33Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-29T17:42:33Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-29T17:42:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-12-03T18:31:21Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3034is.xml"
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
      "title": "Reliable Power Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reliable Power Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Power Act to require the Federal Energy Regulatory Commission to review regulations that may affect the reliable operation of the bulk-power system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:48Z"
    }
  ]
}
```
