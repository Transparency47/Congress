# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3535
- Title: Stop Foreign Funds in Elections Act
- Congress: 119
- Bill type: HR
- Bill number: 3535
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-05-26T15:15:33Z
- Update date including text: 2026-05-26T15:15:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported by the Yeas and Nays: 11 - 0.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported by the Yeas and Nays: 11 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3535",
    "number": "3535",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Stop Foreign Funds in Elections Act",
    "type": "HR",
    "updateDate": "2026-05-26T15:15:33Z",
    "updateDateIncludingText": "2026-05-26T15:15:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 11 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
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
      "actionDate": "2025-05-21",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
            "date": "2026-05-14T17:17:33Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T14:04:25Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "ME"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3535ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3535\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Fitzpatrick (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to apply the prohibition against contributions and donations by foreign nationals in connection with elections to contributions or donations in connection with ballot initiatives and referenda.\n#### 1. Short title\nThis Act may be cited as the Stop Foreign Funds in Elections Act .\n#### 2. Prohibition on contributions and donations by foreign nationals in connection with ballot initiatives and referenda and recall elections\n##### (a) Prohibition\nSection 319(a)(1)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(a)(1)(A) ) is amended by inserting , including a State or local ballot initiative or referendum or recall election after State, or local election .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to contributions and donations made on or after the date of the enactment of this Act.",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in House"
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
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2026-05-26T15:15:33Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-05-26T15:15:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-23T17:19:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119hr3535",
          "measure-number": "3535",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3535v00",
            "update-date": "2025-08-15"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Foreign Funds in Elections Act</strong></p> <p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives, referenda, or recall elections.</p>"
        },
        "title": "Stop Foreign Funds in Elections Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3535.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Foreign Funds in Elections Act</strong></p> <p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives, referenda, or recall elections.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119hr3535"
    },
    "title": "Stop Foreign Funds in Elections Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Foreign Funds in Elections Act</strong></p> <p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives, referenda, or recall elections.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119hr3535"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3535ih.xml"
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
      "title": "Stop Foreign Funds in Elections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Foreign Funds in Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to apply the prohibition against contributions and donations by foreign nationals in connection with elections to contributions or donations in connection with ballot initiatives and referenda.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:28Z"
    }
  ]
}
```
