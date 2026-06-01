# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/223
- Title: Preventing Unjust Red Flag Laws Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 223
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-02-25T21:24:02Z
- Update date including text: 2025-02-25T21:24:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/223",
    "number": "223",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Preventing Unjust Red Flag Laws Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-25T21:24:02Z",
    "updateDateIncludingText": "2025-02-25T21:24:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:45Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr223ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 223\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Crenshaw introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit funding for the implementation and enforcement of Federal red flag orders.\n#### 1. Short title\nThis Act may be cited as the Preventing Unjust Red Flag Laws Act of 2025 .\n#### 2. Prohibition on funding for implementation and enforcement of red flag laws or rules\n##### (a) Prohibition on funding\nNone of the funds made available for any Federal department or agency may be used to\u2014\n**(1)**\nimplement or enforce Federal red flag laws; or\n**(2)**\nprovide assistance to States, local, tribal, or territorial government departments or agencies for the implementation or enforcement of red flag laws.\n##### (b) Red flag law defined\nIn this section, the term red flag law means a risk-based, temporary, and preemptive protective order that authorizes the removal of a firearm without due process.",
      "versionDate": "2025-01-07",
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
            "name": "Due process and equal protection",
            "updateDate": "2025-02-10T19:04:15Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-10T19:04:15Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-10T19:04:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-06T20:44:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr223",
          "measure-number": "223",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr223v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preventing Unjust Red Flag Laws Act of 2025</strong></p><p>This bill prohibits the use of federal funds to implement or enforce red flag laws. The term <em>red flag law</em> means a risk-based, temporary, and preemptive protective order that authorizes the removal of a firearm without due process.</p>"
        },
        "title": "Preventing Unjust Red Flag Laws Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr223.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Unjust Red Flag Laws Act of 2025</strong></p><p>This bill prohibits the use of federal funds to implement or enforce red flag laws. The term <em>red flag law</em> means a risk-based, temporary, and preemptive protective order that authorizes the removal of a firearm without due process.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr223"
    },
    "title": "Preventing Unjust Red Flag Laws Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Unjust Red Flag Laws Act of 2025</strong></p><p>This bill prohibits the use of federal funds to implement or enforce red flag laws. The term <em>red flag law</em> means a risk-based, temporary, and preemptive protective order that authorizes the removal of a firearm without due process.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr223"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr223ih.xml"
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
      "title": "Preventing Unjust Red Flag Laws Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Unjust Red Flag Laws Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit funding for the implementation and enforcement of Federal red flag orders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:18:28Z"
    }
  ]
}
```
