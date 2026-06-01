# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6297
- Title: PEACE Act
- Congress: 119
- Bill type: HR
- Bill number: 6297
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2026-05-07T08:05:28Z
- Update date including text: 2026-05-07T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6297",
    "number": "6297",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PEACE Act",
    "type": "HR",
    "updateDate": "2026-05-07T08:05:28Z",
    "updateDateIncludingText": "2026-05-07T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
            "date": "2025-12-03T16:02:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-25T16:03:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6297ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6297\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Mr. Fine (for himself and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Department of State to provide briefings on antisemitism in Europe.\n#### 1. Short title\nThis Act may be cited as the Protecting Europe from Antisemitic Crime and Extremism Act or the PEACE Act .\n#### 2. Briefings on antisemitism in Europe\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Assistant Secretary for European and Eurasian Affairs, in consultation with other relevant officials of the Department of State, should assess the persistent and growing threat of antisemitism and acts of international terrorism in Europe as a matter of importance to the foreign policy of the United States; and\n**(2)**\nthe Under Secretary for Political Affairs, acting through the Assistant Secretary for European and Eurasian Affairs, should diplomatically engage governments of countries of apparent concern on efforts for transatlantic cooperation to counter and address antisemitism and acts of international terrorism that may threaten transatlantic stability, the safety and security of United States citizens, and institutions abroad.\n##### (b) Briefing\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for two years, the Assistant Secretary for European and Eurasian Affairs shall provide a briefing to the appropriate congressional committees on the matters described in subsection (a).\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.",
      "versionDate": "2025-11-25",
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
        "name": "International Affairs",
        "updateDate": "2025-12-02T19:48:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-25",
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
          "measure-id": "id119hr6297",
          "measure-number": "6297",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-25",
          "originChamber": "HOUSE",
          "update-date": "2026-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6297v00",
            "update-date": "2026-02-18"
          },
          "action-date": "2025-11-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Europe from Antisemitic Crime and Extremism Act or the PEACE Act</strong></p><p>This bill requires the Department of State to periodically brief Congress over the next three years on (1) the threat of\u00a0antisemitism and acts of international terrorism in Europe; and (2) diplomatic engagements with certain governments on transatlantic cooperative efforts to counter antisemitism and acts of international terrorism that may threaten transatlantic stability, the safety and security of U.S. citizens, and institutions abroad.</p>"
        },
        "title": "PEACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6297.xml",
    "summary": {
      "actionDate": "2025-11-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Europe from Antisemitic Crime and Extremism Act or the PEACE Act</strong></p><p>This bill requires the Department of State to periodically brief Congress over the next three years on (1) the threat of\u00a0antisemitism and acts of international terrorism in Europe; and (2) diplomatic engagements with certain governments on transatlantic cooperative efforts to counter antisemitism and acts of international terrorism that may threaten transatlantic stability, the safety and security of U.S. citizens, and institutions abroad.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr6297"
    },
    "title": "PEACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Europe from Antisemitic Crime and Extremism Act or the PEACE Act</strong></p><p>This bill requires the Department of State to periodically brief Congress over the next three years on (1) the threat of\u00a0antisemitism and acts of international terrorism in Europe; and (2) diplomatic engagements with certain governments on transatlantic cooperative efforts to counter antisemitism and acts of international terrorism that may threaten transatlantic stability, the safety and security of U.S. citizens, and institutions abroad.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr6297"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6297ih.xml"
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
      "title": "PEACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T02:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Europe from Antisemitic Crime and Extremism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Department of State to provide briefings on antisemitism in Europe.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T02:33:23Z"
    }
  ]
}
```
