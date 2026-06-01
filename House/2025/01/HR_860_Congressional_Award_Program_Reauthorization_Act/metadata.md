# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/860?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/860
- Title: Congressional Award Program Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 860
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-01-05T13:39:54Z
- Update date including text: 2026-01-05T13:39:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/860",
    "number": "860",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Congressional Award Program Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-01-05T13:39:54Z",
    "updateDateIncludingText": "2026-01-05T13:39:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr860ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 860\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Hudson (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo reauthorize the Congressional Award Act.\n#### 1. Short title\nThis Act may be cited as the Congressional Award Program Reauthorization Act .\n#### 2. Termination\n##### (a) In general\nSection 108 of the Congressional Award Act ( 2 U.S.C. 808 ) is amended by striking October 1, 2023 and inserting October 1, 2028 .\n##### (b) Retroactive effective date\nThe amendment made by subsection (a) shall take effect as if enacted on October 1, 2023.\n#### 3. Other amendments\nSection 102 of the Congressional Award Act ( 2 U.S.C. 802 ) is amended\u2014\n**(1)**\nin subsection (a), by striking Each medal shall consist of gold-plate over bronze, rhodium over bronze, or bronze and shall be struck in accordance with subsection (f). ; and\n**(2)**\nin subsection (f)(1), in the second sentence, by striking Subject to subsection (a), the and inserting The .",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-12-26",
        "text": "Signed by President."
      },
      "number": "284",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Congressional Award Program Reauthorization Act",
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
            "name": "Congressional tributes",
            "updateDate": "2025-04-23T13:52:18Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-04-23T13:52:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-05T20:56:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr860",
          "measure-number": "860",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-07-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr860v00",
            "update-date": "2025-07-18"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Congressional Award Program Reauthorization Act</strong></p><p>This bill reauthorizes through FY2028 the board that administers the Congressional Award Program, which promotes and recognizes service, initiative, and achievement in America's youth. The reauthorization is effective as if enacted on October 1, 2023. The bill also removes a requirement for program medals to consist of gold-plate over bronze, rhodium over bronze, or bronze.</p>"
        },
        "title": "Congressional Award Program Reauthorization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr860.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Award Program Reauthorization Act</strong></p><p>This bill reauthorizes through FY2028 the board that administers the Congressional Award Program, which promotes and recognizes service, initiative, and achievement in America's youth. The reauthorization is effective as if enacted on October 1, 2023. The bill also removes a requirement for program medals to consist of gold-plate over bronze, rhodium over bronze, or bronze.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119hr860"
    },
    "title": "Congressional Award Program Reauthorization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Award Program Reauthorization Act</strong></p><p>This bill reauthorizes through FY2028 the board that administers the Congressional Award Program, which promotes and recognizes service, initiative, and achievement in America's youth. The reauthorization is effective as if enacted on October 1, 2023. The bill also removes a requirement for program medals to consist of gold-plate over bronze, rhodium over bronze, or bronze.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119hr860"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr860ih.xml"
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
      "title": "Congressional Award Program Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Award Program Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Congressional Award Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:18:25Z"
    }
  ]
}
```
