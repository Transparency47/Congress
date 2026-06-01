# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/13?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/13
- Title: Proposing an amendment to the Constitution of the United States limiting the pardon power of the President.
- Congress: 119
- Bill type: HJRES
- Bill number: 13
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-01-21T09:05:16Z
- Update date including text: 2026-01-21T09:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/13",
    "number": "13",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States limiting the pardon power of the President.",
    "type": "HJRES",
    "updateDate": "2026-01-21T09:05:16Z",
    "updateDateIncludingText": "2026-01-21T09:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:30:25Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres13ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 13\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Cohen (for himself, Mr. Johnson of Georgia , and Mr. Levin ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States limiting the pardon power of the President.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. The President shall not have the power to grant pardons and reprieves to\u2014 (1) the President\u2019s self; (2) any person, up to a third degree relation, of the President, or a spouse thereof; (3) any current or former member of the President\u2019s administration; (4) any person who worked on the President\u2019s presidential campaign as a paid employee; (5) any person or entity for an offense that was motivated by a direct and significant personal or pecuniary interest of any of the foregoing persons; or (6) any person or entity for an offense that was at the direction of, or in coordination with, the President. Any pardon issued for a corrupt purpose shall be invalid. . 2. The Congress shall have power to enforce this article by appropriate legislation. .",
      "versionDate": "2025-01-09",
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
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-01-15T18:33:52Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-15T18:33:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-01-10T13:24:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hjres13",
          "measure-number": "13",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres13v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment limiting the pardon power of the President.</p><p>The amendment prohibits the President from granting a pardon or reprieve to himself or herself, to relatives or members of the administration, to paid campaign employees, to a person or entity for an offense motivated by an interest of any of those people, or to a person or entity for an offense directed by or coordinated with the President.</p><p>The amendment also invalidates pardons issued for a corrupt purpose.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States limiting the pardon power of the President."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres13.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment limiting the pardon power of the President.</p><p>The amendment prohibits the President from granting a pardon or reprieve to himself or herself, to relatives or members of the administration, to paid campaign employees, to a person or entity for an offense motivated by an interest of any of those people, or to a person or entity for an offense directed by or coordinated with the President.</p><p>The amendment also invalidates pardons issued for a corrupt purpose.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hjres13"
    },
    "title": "Proposing an amendment to the Constitution of the United States limiting the pardon power of the President."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment limiting the pardon power of the President.</p><p>The amendment prohibits the President from granting a pardon or reprieve to himself or herself, to relatives or members of the administration, to paid campaign employees, to a person or entity for an offense motivated by an interest of any of those people, or to a person or entity for an offense directed by or coordinated with the President.</p><p>The amendment also invalidates pardons issued for a corrupt purpose.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hjres13"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres13ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States limiting the pardon power of the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:15Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States limiting the pardon power of the President.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:36Z"
    }
  ]
}
```
