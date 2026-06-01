# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/279
- Title: To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 279
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-01-06T14:54:55Z
- Update date including text: 2026-01-06T14:54:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/279",
    "number": "279",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-01-06T14:54:55Z",
    "updateDateIncludingText": "2026-01-06T14:54:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:31:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr279ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 279\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Griffith introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.\n#### 1. ZIP Code for Fairlawn, Virginia\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Commonwealth of Virginia is the only State in the United States where all cities are independent from their surrounding counties;\n**(2)**\nthese independent cities are not politically a part of the surrounding counties, even if they are located within their borders;\n**(3)**\nin Virginia these independent cities are subject to separate revenue collection and distribution practices related to roads, resources, and sales tax than neighboring counties;\n**(4)**\nthe sales tax collected from electronic commerce from the unincorporated community of Fairlawn, Virginia, located in Pulaski County, is often misallocated to the independent city of Radford, Virginia, because they share the same ZIP Codes; and\n**(5)**\nFairlawn, Virginia, should be eligible to obtain a separate and unique ZIP Code from the neighboring independent city of Radford, Virginia, for tax purposes.\n##### (b) ZIP Code designation\nNot later than 180 days after the date of the enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code applicable to Fairlawn, Virginia.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "64",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Postal service",
            "updateDate": "2025-02-24T19:23:31Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-02-24T19:23:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-20T15:06:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr279",
          "measure-number": "279",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr279v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>"
        },
        "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr279.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr279"
    },
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr279"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr279ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:28Z"
    },
    {
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:39Z"
    }
  ]
}
```
