# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/52?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/52
- Title: A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.
- Congress: 119
- Bill type: SRES
- Bill number: 52
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-03-06T11:57:01Z
- Update date including text: 2026-03-06T11:57:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S596-597)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-06-26 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-06-26 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-06-26 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 105.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S596-597)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-06-26 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-06-26 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-06-26 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 105.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/52",
    "number": "52",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.",
    "type": "SRES",
    "updateDate": "2026-03-06T11:57:01Z",
    "updateDateIncludingText": "2026-03-06T11:57:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 105.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S596-597)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-06-26T21:51:52Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:55:21Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-04T19:27:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres52is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 52\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Lankford (for himself, Mr. Coons , Mr. Tillis , and Mr. Kaine ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nRecognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.\nThat the Senate\u2014\n**(1)**\nrecognizes religious freedom as a fundamental human right;\n**(2)**\nrecognizes the critical importance of religious freedom in\u2014\n**(A)**\nsupporting democracy, good governance, and the rule of law;\n**(B)**\nencouraging pluralism and robust political participation; and\n**(C)**\nfostering global stability and peace;\n**(3)**\nexpresses grave concern over threats to religious freedom around the world, such as through harassment, violence, and imprisonment;\n**(4)**\ncondemns all efforts to suppress religious freedom, including through the criminalization of\u2014\n**(A)**\nreligious exercise in public or private;\n**(B)**\nthe choice to have no faith;\n**(C)**\nconversion from one religion to another;\n**(D)**\nadvocacy for religious freedom;\n**(E)**\nsharing and spreading religious messages and educational materials; and\n**(F)**\nconstruction and maintenance of religious holy sites;\n**(5)**\nsupports the invaluable work of religious freedom advocates in fighting for greater religious freedom around the world; and\n**(6)**\nurges the Department of State to\u2014\n**(A)**\ncontinue robust bilateral and multilateral engagement with allies and partners on religious freedom;\n**(B)**\nmaintain and expand support for human rights activists, journalists, and civil society leaders working to protect religious freedom in countries of particular concern and Special Watch List countries;\n**(C)**\nleverage all diplomatic and sanctions tools available to the United States Government to hold religious freedom violators accountable for their actions, including those authorized by the International Religious Freedom Act of 1998 ( 22 U.S.C. 6401 et seq. );\n**(D)**\ncontinue to impose sanctions on those responsible for violations of religious freedom pursuant to the Global Magnitsky Human Rights Act ( 22 U.S.C. 2656 note);\n**(E)**\nconsider human rights abuses and religious freedom violations in prioritizing partners for free trade agreements; and\n**(F)**\npromote religious freedom as an utmost priority for the United States in implementation of United States foreign policy.",
      "versionDate": "2025-02-04",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres52rs.xml",
      "text": "III\nCalendar No. 105\n119th CONGRESS\n1st Session\nS. RES. 52\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Lankford (for himself, Mr. Coons , Mr. Tillis , Mr. Kaine , Mrs. Britt , Mr. King , Mr. Merkley , Mr. Daines , and Ms. Rosen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nJune 26 (legislative day, June 24), 2025 Reported by Mr. Risch , without amendment\nRESOLUTION\nRecognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.\nThat the Senate\u2014\n**(1)**\nrecognizes religious freedom as a fundamental human right;\n**(2)**\nrecognizes the critical importance of religious freedom in\u2014\n**(A)**\nsupporting democracy, good governance, and the rule of law;\n**(B)**\nencouraging pluralism and robust political participation; and\n**(C)**\nfostering global stability and peace;\n**(3)**\nexpresses grave concern over threats to religious freedom around the world, such as through harassment, violence, and imprisonment;\n**(4)**\ncondemns all efforts to suppress religious freedom, including through the criminalization of\u2014\n**(A)**\nreligious exercise in public or private;\n**(B)**\nthe choice to have no faith;\n**(C)**\nconversion from one religion to another;\n**(D)**\nadvocacy for religious freedom;\n**(E)**\nsharing and spreading religious messages and educational materials; and\n**(F)**\nconstruction and maintenance of religious holy sites;\n**(5)**\nsupports the invaluable work of religious freedom advocates in fighting for greater religious freedom around the world; and\n**(6)**\nurges the Department of State to\u2014\n**(A)**\ncontinue robust bilateral and multilateral engagement with allies and partners on religious freedom;\n**(B)**\nmaintain and expand support for human rights activists, journalists, and civil society leaders working to protect religious freedom in countries of particular concern and Special Watch List countries;\n**(C)**\nleverage all diplomatic and sanctions tools available to the United States Government to hold religious freedom violators accountable for their actions, including those authorized by the International Religious Freedom Act of 1998 ( 22 U.S.C. 6401 et seq. );\n**(D)**\ncontinue to impose sanctions on those responsible for violations of religious freedom pursuant to the Global Magnitsky Human Rights Act ( 22 U.S.C. 2656 note);\n**(E)**\nconsider human rights abuses and religious freedom violations in prioritizing partners for free trade agreements; and\n**(F)**\npromote religious freedom as an utmost priority for the United States in implementation of United States foreign policy.",
      "versionDate": "2025-06-26",
      "versionType": "RS"
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
            "name": "Human rights",
            "updateDate": "2025-04-01T15:24:15Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-04-01T15:24:22Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-04-01T15:24:08Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-04-01T15:24:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-02-21T13:09:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "Senate",
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
          "measure-id": "id119sres52",
          "measure-number": "52",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres52v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes religious freedom as a fundamental human right and expresses concern over threats to religious freedom around the world, such as through harassment, violence, and imprisonment.</p>"
        },
        "title": "A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres52.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes religious freedom as a fundamental human right and expresses concern over threats to religious freedom around the world, such as through harassment, violence, and imprisonment.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119sres52"
    },
    "title": "A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes religious freedom as a fundamental human right and expresses concern over threats to religious freedom around the world, such as through harassment, violence, and imprisonment.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119sres52"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres52is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres52rs.xml"
        }
      ],
      "type": "RS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:25Z"
    },
    {
      "title": "A resolution recognizing religious freedom as a fundamental right, expressing support for international religious freedom as a cornerstone of United States foreign policy, and expressing concern over increased threats to and attacks on religious freedom around the world.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T11:56:20Z"
    }
  ]
}
```
