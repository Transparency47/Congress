# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/22?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/22
- Title: Disapproving of the rule submitted by the Department of Homeland Security relating to "Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers".
- Congress: 119
- Bill type: HJRES
- Bill number: 22
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-01-14T16:38:48Z
- Update date including text: 2026-01-14T16:38:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/22",
    "number": "22",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers\".",
    "type": "HJRES",
    "updateDate": "2026-01-14T16:38:48Z",
    "updateDateIncludingText": "2026-01-14T16:38:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:10:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres22ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 22\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Arrington (for himself, Mr. Self , and Mr. Moore of West Virginia ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nDisapproving of the rule submitted by the Department of Homeland Security relating to Modernizing H\u20131B Requirements, Providing Flexibility in the F\u20131 Program, and Program Improvements Affecting Other Nonimmigrant Workers .\nThat Congress disapproves the rule submitted by the Department of Homeland Security relating to Modernizing H\u20131B Requirements, Providing Flexibility in the F\u20131 Program, and Program Improvements Affecting Other Nonimmigrant Workers (89 Fed. Reg. 103054), and such rule shall have no force or effect.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-01-14T16:38:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hjres22",
          "measure-number": "22",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres22v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers</em> and published on December 18, 2024. The rule revises several regulations applicable to nonimmigrant visas for workers in specialty occupations (H-1B), nonimmigrant visas for students (F-1), and other visas, including by\u00a0</p><ul><li>adding to the criteria for\u00a0specialty occupations;\u00a0</li><li>extending the employment authorization period for F-1 visa holders who are beneficiaries of H-1B petitions; and\u00a0</li><li>requiring H-1B petitioners to have bona fide job offers for beneficiaries and have legal presence in, and be subject to the legal processes of, the United States.\u00a0</li></ul>"
        },
        "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres22.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers</em> and published on December 18, 2024. The rule revises several regulations applicable to nonimmigrant visas for workers in specialty occupations (H-1B), nonimmigrant visas for students (F-1), and other visas, including by\u00a0</p><ul><li>adding to the criteria for\u00a0specialty occupations;\u00a0</li><li>extending the employment authorization period for F-1 visa holders who are beneficiaries of H-1B petitions; and\u00a0</li><li>requiring H-1B petitioners to have bona fide job offers for beneficiaries and have legal presence in, and be subject to the legal processes of, the United States.\u00a0</li></ul>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hjres22"
    },
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers</em> and published on December 18, 2024. The rule revises several regulations applicable to nonimmigrant visas for workers in specialty occupations (H-1B), nonimmigrant visas for students (F-1), and other visas, including by\u00a0</p><ul><li>adding to the criteria for\u00a0specialty occupations;\u00a0</li><li>extending the employment authorization period for F-1 visa holders who are beneficiaries of H-1B petitions; and\u00a0</li><li>requiring H-1B petitioners to have bona fide job offers for beneficiaries and have legal presence in, and be subject to the legal processes of, the United States.\u00a0</li></ul>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hjres22"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres22ih.xml"
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
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:18:23Z"
    },
    {
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-1B Requirements, Providing Flexibility in the F-1 Program, and Program Improvements Affecting Other Nonimmigrant Workers\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:45Z"
    }
  ]
}
```
