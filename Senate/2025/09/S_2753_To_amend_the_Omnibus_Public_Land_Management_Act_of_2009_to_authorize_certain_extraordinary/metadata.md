# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2753
- Title: Urban Canal Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 2753
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-04-06T16:35:32Z
- Update date including text: 2026-04-06T16:35:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2753",
    "number": "2753",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Urban Canal Modernization Act",
    "type": "S",
    "updateDate": "2026-04-06T16:35:32Z",
    "updateDateIncludingText": "2026-04-06T16:35:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T16:02:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:06Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2753is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2753\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Risch (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Omnibus Public Land Management Act of 2009 to authorize certain extraordinary operation and maintenance work for urban canals of concern.\n#### 1. Short title\nThis Act may be cited as the Urban Canal Modernization Act .\n#### 2. Extraordinary operation and maintenance work performed by the Secretary of the Interior\n##### (a) Definitions\nSection 9601 of the Omnibus Public Land Management Act of 2009 ( 43 U.S.C. 510 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), (3), (4), (5), (6), and (7) as paragraphs (2), (3), (4), (5), (6), (7), and (1), respectively, and moving the paragraphs so as to appear in numerical order;\n**(2)**\nin paragraph (3) (as so redesignated), by striking et seq.) and inserting et seq.)) ;\n**(3)**\nin paragraph (4) (as so redesignated), by striking mean and inserting means ; and\n**(4)**\nby adding at the end the following:\n(8) Urban canal of concern The term urban canal of concern means a transferred works or segment of a transferred works that is a canal reach\u2014 (A) the failure of which would result in an estimated at-risk population of more than 100 individuals, as determined by the Secretary, pursuant to the guidelines and criteria developed under section 9602(a); and (B) that is determined by the Secretary to be classified as an urban canal reach. .\n##### (b) Extraordinary operation and maintenance work on urban canals of concern\nSection 9603 of the Omnibus Public Land Management Act of 2009 ( 43 U.S.C. 510b ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking (a) and all that follows through The Secretary and inserting the following:\n(a) Authorization (1) Project facilities The Secretary ; and\n**(B)**\nby adding at the end the following:\n(2) Urban canals of concern The Secretary or the transferred works operating entity may carry out, in accordance with subsection (b), any extraordinary operation and maintenance work on an urban canal of concern that the Secretary determines to be necessary pursuant to the guidelines and criteria set forth in section 9602(a). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraph (3) as paragraph (4); and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) Urban canals of concern Except in the case of emergency extraordinary operation and maintenance work carried out under subsection (c), of the total costs of extraordinary operation and maintenance work on an urban canal of concern conducted under subsection (a)(2)\u2014 (A) 35 percent shall be provided by the Secretary on a nonreimbursable basis; and (B) the remaining amounts shall be advanced by the Secretary in accordance with paragraph (2), to be repaid by the transferred works operating entity in accordance with that paragraph. ; and\n**(3)**\nby adding at the end the following:\n(e) Reimbursable funds Any reimbursable funds provided under this section shall be considered to be a non-Federal source of funds for purposes of any cost-sharing requirement for a Federal grant. .",
      "versionDate": "2025-09-10",
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
            "name": "Dams and canals",
            "updateDate": "2026-03-18T13:30:45Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-03-18T13:30:45Z"
          },
          {
            "name": "Urban and suburban affairs and development",
            "updateDate": "2026-03-18T13:30:45Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-18T13:30:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-04-06T16:35:31Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2753is.xml"
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
      "title": "Urban Canal Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Urban Canal Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Public Land Management Act of 2009 to authorize certain extraordinary operation and maintenance work for urban canals of concern.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:13Z"
    }
  ]
}
```
