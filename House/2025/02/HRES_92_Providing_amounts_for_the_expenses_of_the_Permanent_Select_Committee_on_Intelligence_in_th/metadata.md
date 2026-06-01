# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/92?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/92
- Title: Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 92
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-04-25T19:31:55Z
- Update date including text: 2025-04-25T19:31:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-04 - Committee: Submitted in House
- Latest action: 2025-02-04: Submitted in House

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-04 - Committee: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/92",
    "number": "92",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress.",
    "type": "HRES",
    "updateDate": "2025-04-25T19:31:55Z",
    "updateDateIncludingText": "2025-04-25T19:31:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-04T17:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres92ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 92\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Crawford (for himself and Mr. Himes ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nProviding amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress.\n#### 1. Amounts for Committee Expenses\nFor the expenses of the Permanent Select Committee on Intelligence (hereafter in this resolution referred to as the Committee ), including the expenses of all staff salaries, there shall be paid, out of the applicable accounts of the House of Representatives for committee salaries and expenses, not more than $19,240,928 for the One Hundred Nineteenth Congress.\n#### 2. Session Limitations\nOf the amount specified in section 1\u2014\n**(1)**\nnot more than $9,538,983 shall be available for expenses incurred during the period beginning at noon on January 3, 2025, and ending immediately before noon on January 3, 2026; and\n**(2)**\nnot more than $9,701,945 shall be available for expenses incurred during the period beginning at noon on January 3, 2026, and ending immediately before noon on January 3, 2027.\n#### 3. Vouchers\nPayments under this resolution shall be made on vouchers authorized by the Committee, signed by the Chairman of the Committee, and approved in the manner directed by the Committee on House Administration.\n#### 4. Regulations\nAmounts made available under this resolution shall be expended in accordance with regulations prescribed by the Committee on House Administration.",
      "versionDate": "2025-02-04",
      "versionType": "IH"
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
            "name": "Congressional committees",
            "updateDate": "2025-02-14T18:16:23Z"
          },
          {
            "name": "House Permanent Select Committee on Intelligence",
            "updateDate": "2025-02-14T18:16:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-06T15:10:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hres92",
          "measure-number": "92",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres92v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides amounts for the expenses of the House Permanent Select Committee on Intelligence for the 119th Congress.</p>"
        },
        "title": "Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres92.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides amounts for the expenses of the House Permanent Select Committee on Intelligence for the 119th Congress.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hres92"
    },
    "title": "Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides amounts for the expenses of the House Permanent Select Committee on Intelligence for the 119th Congress.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hres92"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres92ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:26Z"
    },
    {
      "title": "Providing amounts for the expenses of the Permanent Select Committee on Intelligence in the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:05:58Z"
    }
  ]
}
```
