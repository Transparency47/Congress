# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/64?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/64
- Title: A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 64
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-05T21:55:54Z
- Update date including text: 2025-12-05T21:55:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/64",
    "number": "64",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
    "type": "S",
    "updateDate": "2025-12-05T21:55:54Z",
    "updateDateIncludingText": "2025-12-05T21:55:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T21:01:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s64is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 64\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Warner (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.\n#### 1. ZIP Code for Fairlawn, Virginia\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Commonwealth of Virginia is the only State in the United States where all cities are independent from their surrounding counties;\n**(2)**\nthese independent cities are not politically a part of the surrounding counties, even if they are located within their borders;\n**(3)**\nin Virginia these independent cities are subject to separate revenue collection and distribution practices related to roads, resources, and sales tax than neighboring counties;\n**(4)**\nthe sales tax collected from electronic commerce from the unincorporated community of Fairlawn, Virginia, located in Pulaski County, is often misallocated to the independent city of Radford, Virginia, because they share the same ZIP Codes; and\n**(5)**\nFairlawn, Virginia, should be eligible to obtain a separate and unique ZIP Code from the neighboring independent city of Radford, Virginia, for tax purposes.\n##### (b) ZIP Code designation\nNot later than 180 days after the date of the enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code applicable to Fairlawn, Virginia.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "279",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
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
            "name": "Postal service",
            "updateDate": "2025-02-24T19:39:47Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-02-24T19:39:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-20T15:07:21Z"
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
          "measure-id": "id119s64",
          "measure-number": "64",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s64v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>"
        },
        "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s64.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119s64"
    },
    "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the U.S. Postal Service to designate a single, unique ZIP Code applicable to Fairlawn, Virginia.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119s64"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s64is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:36Z"
    },
    {
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Fairlawn, Virginia, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T11:56:16Z"
    }
  ]
}
```
