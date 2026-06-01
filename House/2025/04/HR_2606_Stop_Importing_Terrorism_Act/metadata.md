# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2606
- Title: Stop Importing Terrorism Act
- Congress: 119
- Bill type: HR
- Bill number: 2606
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-02-13T17:26:47Z
- Update date including text: 2026-02-13T17:26:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2606",
    "number": "2606",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Stop Importing Terrorism Act",
    "type": "HR",
    "updateDate": "2026-02-13T17:26:47Z",
    "updateDateIncludingText": "2026-02-13T17:26:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:00:30Z",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2606ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2606\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Ms. Mace introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to repeal an exception to the terrorism-related ground for inadmissibility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Importing Terrorism Act .\n#### 2. Repeal of exception to terrorism-related ground of inadmissibility\n##### (a) In general\nClause (ii) of section 212(a)(3)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(B) ) is repealed.\n##### (b) Deportability of aliens admitted pursuant to exception\nAny alien who was admitted to the United States pursuant to clause (ii) of section 212(a)(3)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(B) ) during the period beginning on January 20, 2021, and ending on the date of enactment of this Act, is deportable.",
      "versionDate": "2025-04-02",
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
        "name": "Immigration",
        "updateDate": "2025-04-08T16:37:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
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
          "measure-id": "id119hr2606",
          "measure-number": "2606",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-02",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2606v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Importing Terrorism Act</strong></p><p>This bill tightens U.S. admission restrictions on a spouse or child of certain individuals barred from the United States due to terrorist activity and makes deportable certain previously admitted individuals.</p><p>Under current law, the spouse or child of an individual who is inadmissible to the United States due to terrorist activity is barred from admission to the United States if the terrorist activity occurred within the last five years. However, there is an exception that applies to a spouse or child of such an individual (1) who did not know or should not have reasonably known of the terrorist activity, or (2) whom the consular officer or the Department of Justice has reasonable grounds to believe has renounced such activity.</p><p>The bill repeals this exception. The bill also deems deportable any individual admitted under this exception on or after January 20, 2021.\u00a0</p>"
        },
        "title": "Stop Importing Terrorism Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2606.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Importing Terrorism Act</strong></p><p>This bill tightens U.S. admission restrictions on a spouse or child of certain individuals barred from the United States due to terrorist activity and makes deportable certain previously admitted individuals.</p><p>Under current law, the spouse or child of an individual who is inadmissible to the United States due to terrorist activity is barred from admission to the United States if the terrorist activity occurred within the last five years. However, there is an exception that applies to a spouse or child of such an individual (1) who did not know or should not have reasonably known of the terrorist activity, or (2) whom the consular officer or the Department of Justice has reasonable grounds to believe has renounced such activity.</p><p>The bill repeals this exception. The bill also deems deportable any individual admitted under this exception on or after January 20, 2021.\u00a0</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr2606"
    },
    "title": "Stop Importing Terrorism Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Importing Terrorism Act</strong></p><p>This bill tightens U.S. admission restrictions on a spouse or child of certain individuals barred from the United States due to terrorist activity and makes deportable certain previously admitted individuals.</p><p>Under current law, the spouse or child of an individual who is inadmissible to the United States due to terrorist activity is barred from admission to the United States if the terrorist activity occurred within the last five years. However, there is an exception that applies to a spouse or child of such an individual (1) who did not know or should not have reasonably known of the terrorist activity, or (2) whom the consular officer or the Department of Justice has reasonable grounds to believe has renounced such activity.</p><p>The bill repeals this exception. The bill also deems deportable any individual admitted under this exception on or after January 20, 2021.\u00a0</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr2606"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2606ih.xml"
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
      "title": "Stop Importing Terrorism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Importing Terrorism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to repeal an exception to the terrorism-related ground for inadmissibility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T11:18:23Z"
    }
  ]
}
```
