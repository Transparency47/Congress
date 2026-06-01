# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/915?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/915
- Title: Small Business Technological Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 915
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-05-21T08:08:26Z
- Update date including text: 2026-05-21T08:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/915",
    "number": "915",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Small Business Technological Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:26Z",
    "updateDateIncludingText": "2026-05-21T08:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
        "item": [
          {
            "date": "2026-05-20T21:46:44Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-04T17:05:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr915ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 915\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Alford (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo authorize small business loans to finance access to modern business software, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Technological Act of 2025 .\n#### 2. Additional uses for small business administration business loans\n##### (a) In general\nSection 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) is amended by adding at the end the following:\n(38) Access to modern business software The Administration may provide loans under this subsection to finance, in whole or in part, business software or cloud computing services, or any such technology, that facilitates business operations, product or service delivery, the processing, payment, or tracking of payroll expenses, human resources, sales and billing functions, or accounting or tracking of supplies, inventory, records and expenses, including business tools that utilize artificial intelligence. .\n##### (b) Rule of construction\nNothing in the amendment made by subsection (a) shall be construed to\u2014\n**(1)**\nprovide that loans made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) before the date of enactment of this Act for the purposes described in paragraph (38) of such section 7(a), as added by subsection (a), were not permissible;\n**(2)**\nauthorize the use of loans made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) for research and development purposes; or\n**(3)**\nlimit the definition of working capital under the Small Business Act ( 15 U.S.C. 631 et seq. ).",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-05-21",
        "text": "Committee on Small Business and Entrepreneurship. Hearings held."
      },
      "number": "305",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Business Technological Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-03-07T13:22:24Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr915ih.xml"
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
      "title": "Small Business Technological Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Technological Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize small business loans to finance access to modern business software, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:24Z"
    }
  ]
}
```
