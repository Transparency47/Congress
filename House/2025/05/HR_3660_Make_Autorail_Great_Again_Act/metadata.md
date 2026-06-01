# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3660
- Title: Make Autorail Great Again Act
- Congress: 119
- Bill type: HR
- Bill number: 3660
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-04-27T12:46:10Z
- Update date including text: 2026-04-27T12:46:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3660",
    "number": "3660",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Make Autorail Great Again Act",
    "type": "HR",
    "updateDate": "2026-04-27T12:46:10Z",
    "updateDateIncludingText": "2026-04-27T12:46:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:47:13Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3660ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3660\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prohibit any Federal funds from being provided to the Washington Metropolitan Area Transit Authority until such Authority is renamed the Washington Metropolitan Authority for Greater Access, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Make Autorail Great Again Act .\n#### 2. Renaming\n##### (a) In general\nNo Federal funds may be provided to the Washington Metropolitan Area Transit Authority until the Compact is amended to rename the Washington Metropolitan Area Transit Authority as the Washington Metropolitan Authority for Greater Access or the WMAGA and the Metrorail as the Trump Train .\n##### (b) Compact defined\nIn this section, the term Compact means the Washington Metropolitan Area Transit Regulation Compact, known as the Washington Metropolitan Area Transit Authority Compact, consented to by Congress under Public Law 89\u2013774 (80 Stat. 1324 et seq.).",
      "versionDate": "2025-05-29",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-04T11:19:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hr3660",
          "measure-number": "3660",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3660v00",
            "update-date": "2026-04-27"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Make Autorail Great Again Act</strong></p><p>This bill prohibits the Washington Metropolitan Area Transit Authority (WMATA) from receiving any federal funding until the\u00a0Washington Metropolitan Area Transit Authority Compact is amended to rename (1) WMATA as the Washington Metropolitan Authority for Greater Access or the WMAGA, and (2) the\u00a0Metrorail\u00a0as the Trump Train.</p>"
        },
        "title": "Make Autorail Great Again Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3660.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Autorail Great Again Act</strong></p><p>This bill prohibits the Washington Metropolitan Area Transit Authority (WMATA) from receiving any federal funding until the\u00a0Washington Metropolitan Area Transit Authority Compact is amended to rename (1) WMATA as the Washington Metropolitan Authority for Greater Access or the WMAGA, and (2) the\u00a0Metrorail\u00a0as the Trump Train.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr3660"
    },
    "title": "Make Autorail Great Again Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Autorail Great Again Act</strong></p><p>This bill prohibits the Washington Metropolitan Area Transit Authority (WMATA) from receiving any federal funding until the\u00a0Washington Metropolitan Area Transit Authority Compact is amended to rename (1) WMATA as the Washington Metropolitan Authority for Greater Access or the WMAGA, and (2) the\u00a0Metrorail\u00a0as the Trump Train.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr3660"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3660ih.xml"
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
      "title": "Make Autorail Great Again Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make Autorail Great Again Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit any Federal funds from being provided to the Washington Metropolitan Area Transit Authority until such Authority is renamed the Washington Metropolitan Authority for Greater Access, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T09:18:18Z"
    }
  ]
}
```
