# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/82?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/82
- Title: Defund National Endowment for the Humanities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 82
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-03T09:06:15Z
- Update date including text: 2025-12-03T09:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/82",
    "number": "82",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Defund National Endowment for the Humanities Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-03T09:06:15Z",
    "updateDateIncludingText": "2025-12-03T09:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:04:45Z",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr82ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 82\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo provide that none of the funds made available to the National Endowment for the Humanities for any fiscal year may be used to carry out section 7 of the National Foundation on the Arts and the Humanities Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Defund National Endowment for the Humanities Act of 2025 .\n#### 2. Limitation\nNone of the funds made available to the National Endowment for the Humanities for any fiscal year may be used to carry out section 7 of the National Foundation on the Arts and the Humanities Act of 1965 ( 20 U.S.C. 956 ).\n#### 3. Effective date\nThis Act shall take effect on the 1st day of the 1st fiscal year that begins after the date of the enactment of this Act.",
      "versionDate": "2025-01-03",
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
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-14T19:16:20Z"
          },
          {
            "name": "Humanities programs funding",
            "updateDate": "2025-02-14T19:16:20Z"
          },
          {
            "name": "National Foundation on the Arts and the Humanities",
            "updateDate": "2025-02-14T19:16:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-01-31T13:27:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr82",
          "measure-number": "82",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr82v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defund National Endowment for the Humanities Act\u00a0of 2025</strong></p><p>This bill prohibits the use of any funds that are made available to the National Endowment for the Humanities of the National Foundation on the Arts and the Humanities to carry out the functions, programs, or activities of such endowment.</p>"
        },
        "title": "Defund National Endowment for the Humanities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr82.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund National Endowment for the Humanities Act\u00a0of 2025</strong></p><p>This bill prohibits the use of any funds that are made available to the National Endowment for the Humanities of the National Foundation on the Arts and the Humanities to carry out the functions, programs, or activities of such endowment.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr82"
    },
    "title": "Defund National Endowment for the Humanities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund National Endowment for the Humanities Act\u00a0of 2025</strong></p><p>This bill prohibits the use of any funds that are made available to the National Endowment for the Humanities of the National Foundation on the Arts and the Humanities to carry out the functions, programs, or activities of such endowment.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr82"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr82ih.xml"
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
      "title": "Defund National Endowment for the Humanities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defund National Endowment for the Humanities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that none of the funds made available to the National Endowment for the Humanities for any fiscal year may be used to carry out section 7 of the National Foundation on the Arts and the Humanities Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T06:18:29Z"
    }
  ]
}
```
