# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/313
- Title: Stop Funding Global Terrorists Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 313
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-04-03T20:22:53Z
- Update date including text: 2025-04-03T20:22:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/313",
    "number": "313",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Stop Funding Global Terrorists Act of 2025",
    "type": "S",
    "updateDate": "2025-04-03T20:22:53Z",
    "updateDateIncludingText": "2025-04-03T20:22:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
        "item": {
          "date": "2025-01-29T20:46:34Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "LA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SC"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s313is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 313\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mrs. Capito (for herself, Mr. Cotton , Mrs. Britt , Mr. Cassidy , Mr. Scott of Florida , Mr. Cruz , Mrs. Blackburn , Mr. Tillis , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo restrict United States voluntary and assessed contributions to the United Nations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Funding Global Terrorists Act of 2025 .\n#### 2. Restriction on funding for United Nations\n##### (a) In general\nThe United States may not make any voluntary or assessed contributions to the United Nations for assistance in Afghanistan until the Secretary of State certifies to the appropriate congressional committees that\u2014\n**(1)**\nno United States funds are used in cash shipments by the United Nations into Afghanistan;\n**(2)**\nno specially designated global terrorist organization receives funds as a result of such cash shipments; and\n**(3)**\nno foreign terrorist organization receives funds as a result of such cash shipments.\n##### (b) Revocation\nIf, after making a certification pursuant to subsection (a), the Secretary determines that such certification is inaccurate, the Secretary shall\u2014\n**(1)**\nrevoke such certification; and\n**(2)**\nprovide to the appropriate congressional committees\u2014\n**(A)**\na notification of such revocation; and\n**(B)**\na detailed justification for such revocation.\n##### (c) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nCommittee on Foreign Relations and the Committee on Appropriations of the Senate; and\n**(B)**\nCommittee on Foreign Affairs and the Committee on Appropriations of the House of Representatives.\n**(2) Foreign terrorist organization**\nThe term foreign terrorist organization means an organization that has been designated as a foreign terrorist organization by the Secretary of State, pursuant to section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(3) Specially designated global terrorist organization**\nThe term specially designated global terrorist organization means an organization that has been designated as a specially designated global terrorist pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism).",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-03-21T15:13:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s313",
          "measure-number": "313",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s313v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Funding Global Terrorists Act of 2025</strong></p><p>This bill prohibits the United States from making any voluntary or assessed contributions to the United Nations (UN) for assistance to Afghanistan until the Department of State certifies to Congress that (1) no U.S. funds are used in cash shipments by the UN to Afghanistan, and (2) terrorist organizations do not receive funds as a result of such cash shipments. If the State Department later determines such a certification is inaccurate, it must revoke the certification and notify Congress.</p>"
        },
        "title": "Stop Funding Global Terrorists Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s313.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Funding Global Terrorists Act of 2025</strong></p><p>This bill prohibits the United States from making any voluntary or assessed contributions to the United Nations (UN) for assistance to Afghanistan until the Department of State certifies to Congress that (1) no U.S. funds are used in cash shipments by the UN to Afghanistan, and (2) terrorist organizations do not receive funds as a result of such cash shipments. If the State Department later determines such a certification is inaccurate, it must revoke the certification and notify Congress.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119s313"
    },
    "title": "Stop Funding Global Terrorists Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Funding Global Terrorists Act of 2025</strong></p><p>This bill prohibits the United States from making any voluntary or assessed contributions to the United Nations (UN) for assistance to Afghanistan until the Department of State certifies to Congress that (1) no U.S. funds are used in cash shipments by the UN to Afghanistan, and (2) terrorist organizations do not receive funds as a result of such cash shipments. If the State Department later determines such a certification is inaccurate, it must revoke the certification and notify Congress.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119s313"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s313is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stop Funding Global Terrorists Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Funding Global Terrorists Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restrict United States voluntary and assessed contributions to the United Nations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:28Z"
    }
  ]
}
```
