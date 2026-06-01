# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/32?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/32
- Title: Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as "National School Counseling Week".
- Congress: 119
- Bill type: HJRES
- Bill number: 32
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-02-05T18:38:55Z
- Update date including text: 2026-02-05T18:38:55Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/32",
    "number": "32",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001156",
        "district": "38",
        "firstName": "Linda",
        "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
        "lastName": "S\u00e1nchez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as \"National School Counseling Week\".",
    "type": "HJRES",
    "updateDate": "2026-02-05T18:38:55Z",
    "updateDateIncludingText": "2026-02-05T18:38:55Z"
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
          "date": "2025-01-31T15:08:10Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres32ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 32\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. S\u00e1nchez (for herself, Mr. Panetta , Mr. Evans of Pennsylvania , Mrs. Dingell , Mr. Davis of Illinois , Mr. Johnson of Georgia , Ms. Norton , Mr. Grijalva , and Mr. Smith of Washington ) submitted the following joint resolution; which was referred to the Committee on Education and Workforce\nJOINT RESOLUTION\nExpressing support for designation of the week of February 3, 2025, through February 7, 2025, as National School Counseling Week .\nThat Congress\u2014\n**(1)**\nhonors and recognizes the contributions of school counselors to the success of students in the Nation\u2019s elementary and secondary schools; and\n**(2)**\nencourages the people of the United States to observe National School Counseling Week with appropriate ceremonies and activities that promote awareness of the crucial role school counselors play in preparing students for fulfilling lives as contributing members of society.",
      "versionDate": "2025-01-31",
      "versionType": "IH"
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
        "actionDate": "2026-02-02",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for designation of the week of February 2, 2026, through February 6, 2026, as \"National School Counseling Week\".",
      "type": "HJRES"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-03-26T19:14:27Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2025-03-26T19:14:27Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-26T19:14:27Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-03-26T19:14:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-04T12:27:21Z"
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
          "measure-id": "id119hjres32",
          "measure-number": "32",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres32v00",
            "update-date": "2025-02-05"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution honors the contributions of school counselors to the success of students in elementary and secondary schools.</p><p>The joint resolution encourages the observation of National School Counseling Week with ceremonies and activities that promote awareness of the crucial role school counselors play in preparing students for fulfilling lives as contributing members of society.</p>"
        },
        "title": "Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as \"National School Counseling Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres32.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution honors the contributions of school counselors to the success of students in elementary and secondary schools.</p><p>The joint resolution encourages the observation of National School Counseling Week with ceremonies and activities that promote awareness of the crucial role school counselors play in preparing students for fulfilling lives as contributing members of society.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hjres32"
    },
    "title": "Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as \"National School Counseling Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution honors the contributions of school counselors to the success of students in elementary and secondary schools.</p><p>The joint resolution encourages the observation of National School Counseling Week with ceremonies and activities that promote awareness of the crucial role school counselors play in preparing students for fulfilling lives as contributing members of society.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hjres32"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres32ih.xml"
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
      "title": "Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as \"National School Counseling Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T09:18:38Z"
    },
    {
      "title": "Expressing support for designation of the week of February 3, 2025, through February 7, 2025, as \"National School Counseling Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:48Z"
    }
  ]
}
```
