# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/305
- Title: Small Business Technological Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 305
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T22:47:27Z
- Update date including text: 2025-12-05T22:47:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-05-21 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-05-21 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/305",
    "number": "305",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Small Business Technological Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:47:27Z",
    "updateDateIncludingText": "2025-12-05T22:47:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
        "item": [
          {
            "date": "2025-05-21T14:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-29T18:55:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NH"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s305is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 305\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Young (for himself, Ms. Rosen , Mr. Budd , Mrs. Shaheen , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo authorize small business loans to finance access to modern business software, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Technological Act of 2025 .\n#### 2. Additional uses for small business administration business loans\n##### (a) In general\nSection 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) is amended by adding at the end the following:\n(38) Access to modern business software The Administration may provide loans under this subsection to finance, in whole or in part, business software or cloud computing services, or any such technology, that facilitates business operations, product or service delivery, the processing, payment, or tracking of payroll expenses, human resources, sales and billing functions, or accounting or tracking of supplies, inventory, records and expenses, including business tools that utilize artificial intelligence. .\n##### (b) Rule of construction\nNothing in the amendment made by subsection (a) shall be construed to\u2014\n**(1)**\nprovide that loans made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) before the date of enactment of this Act for the purposes described in paragraph (38) of such section 7(a), as added by subsection (a), were not permissible;\n**(2)**\nauthorize the use of loans made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) for research and development purposes; or\n**(3)**\nlimit the definition of working capital under the Small Business Act ( 15 U.S.C. 631 et seq. ).",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "915",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Business Technological Act of 2025",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-05-22T13:54:55Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-05-22T13:46:50Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-05-22T13:42:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-03T21:03:10Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s305is.xml"
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
      "title": "Small Business Technological Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T12:18:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Technological Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize small business loans to finance access to modern business software, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:41Z"
    }
  ]
}
```
