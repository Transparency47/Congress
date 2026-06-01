# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/90
- Title: Historic Roadways Protection Act
- Congress: 119
- Bill type: S
- Bill number: 90
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/90",
    "number": "90",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Historic Roadways Protection Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-14",
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
            "date": "2026-02-04T22:02:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-14T20:27:57Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:00Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s90is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 90\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit the use of funds by the Secretary of the Interior to finalize and implement certain travel management plans in the State of Utah.\n#### 1. Short title\nThis Act may be cited as the Historic Roadways Protection Act .\n#### 2. Prohibition on use of use of funds to finalize and implement certain travel management plans in the State of Utah\n##### (a) Definitions\nIn this section:\n**(1) Applicable period**\nThe term applicable period means the period that begins on the date of enactment of this Act and ends on the date on which the Secretary certifies to Congress that each of the R.S. 2477 cases has been adjudicated.\n**(2) Covered travel management area**\nThe term covered travel management area means any of the following travel management areas in the State of Utah:\n**(A)**\nThe Henry Mountains and Fremont Gorge Travel Management Area.\n**(B)**\nThe Dinosaur (North) Travel Management Area.\n**(C)**\nThe Book Cliffs Travel Management Area (Vernal Field Office).\n**(D)**\nThe Nine Mile Canyon Travel Management Area (Vernal Field Office).\n**(E)**\nThe San Rafael Swell Travel Management Area.\n**(F)**\nThe Nine Mile Canyon Travel Management Area (Price Field Office).\n**(G)**\nThe Book Cliffs Travel Management Area (Moab Field Office).\n**(H)**\nThe Dolores River Travel Management Area.\n**(I)**\nThe Trail Canyon Travel Management Area.\n**(J)**\nThe Paunsaugunt Travel Management Area.\n**(3) R.S. 2477 case**\nThe term R.S. 2477 case means each of\u2014\n**(A)**\nBeaver County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013423\u2013CW);\n**(B)**\nBox Elder County and State of Utah v. United States (Case No. 1:12\u2013cv\u2013105\u2013DB);\n**(C)**\nCarbon County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013427\u2013DB);\n**(D)**\nDaggett County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013447\u2013RJS);\n**(E)**\nDuchesne County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013425\u2013CW);\n**(F)**\nEmery County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013429\u2013CW);\n**(G)**\nGarfield County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013478\u2013TC);\n**(H)**\nGrand County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013466\u2013DN);\n**(I)**\nIron County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013472\u2013BSJ);\n**(J)**\nJuab County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013462\u2013DB);\n**(K)**\nKane County and State of Utah v. United States (Case No. 2:12\u2013cv\u20131073\u2013CW) (consolidated with Case No. 2:11\u2013cv\u20131031\u2013CW; Case No. 2:12\u2013cv\u2013476\u2013CW).\n**(L)**\nMillard County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013451\u2013DB);\n**(M)**\nPiute County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013428\u2013CW);\n**(N)**\nRich County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013424\u2013DN);\n**(O)**\nSan Juan County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013467\u2013DAK);\n**(P)**\nSanpete County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013430\u2013DB);\n**(Q)**\nSevier County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013452\u2013DN);\n**(R)**\nTooele County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013477\u2013CW);\n**(S)**\nUintah County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013461\u2013DAK);\n**(T)**\nUtah County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013426\u2013CW);\n**(U)**\nWashington County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013471\u2013RJS); and\n**(V)**\nWayne County and State of Utah v. United States (Case No. 2:12\u2013cv\u2013434\u2013DN).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the Bureau of Land Management.\n##### (b) Prohibition on use of funds by the Secretary of the Interior to finalize and implement certain travel management plans\nDuring the applicable period, notwithstanding any other provision of law, the Secretary may not obligate or expend Federal funds\u2014\n**(1)**\nto finalize or implement, with respect to land within the boundary of the State of Utah, a new travel management plan for a covered travel management area; or\n**(2)**\nto implement, with respect to land within the boundary of the State of Utah\u2014\n**(A)**\nthe Indian Creek (Canyon Rims) Travel Management Plan;\n**(B)**\nthe San Rafael Desert Travel Management Plan;\n**(C)**\nthe San Rafael Swell Travel Management Plan; or\n**(D)**\nthe Labyrinth/Gemini Bridges Travel Management Plan.",
      "versionDate": "2025-01-14",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-14",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "376",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Historic Roadways Protection Act",
      "type": "HR"
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
            "name": "Land use and conservation",
            "updateDate": "2025-03-03T18:49:07Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-03-03T18:49:07Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-03-03T18:49:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:09:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119s90",
          "measure-number": "90",
          "measure-type": "s",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s90v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Historic Roadways Protection Act</strong></p><p>This bill prohibits the Bureau for Land Management (BLM) from closing historical roads on public lands in certain areas of Utah until the Federal District Court for Utah makes a decision on each of the\u00a0R.S. 2477 cases, which are cases brought by Utah and counties to keep historical roads on BLM land in Utah open for public use.</p><p>By way of background, a provision of the Mining Law of 1866, commonly known as\u00a0R.S. 2477, granted rights-of-way to states and counties across public lands for the construction of roads for public use in order to promote settlement of the American West. In 1976, Congress repealed R.S. 2477 when it enacted the Federal Land Policy and Management Act (FLPMA), but FLPMA preserved rights-of-way that had been established under R.S. 2477. After the BLM released travel management plans that closed some historical roads, Utah and 22 counties filed lawsuits about their rights-of-way across public lands for historical roads.</p><p>Until the BLM certifies that those cases have been decided, the bill prohibits the BLM from obligating or expending federal funds to (1) finalize or implement a new travel management plan for certain travel management areas in Utah; or (2) implement, with respect to land within the boundary of Utah, the Indian Creek (Canyon Rims) Travel Management Plan, the San Rafael Desert Travel Management Plan, the San Rafael Swell Travel Management Plan, or the Labyrinth/Gemini Bridges Travel Management Plan.</p>"
        },
        "title": "Historic Roadways Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s90.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Historic Roadways Protection Act</strong></p><p>This bill prohibits the Bureau for Land Management (BLM) from closing historical roads on public lands in certain areas of Utah until the Federal District Court for Utah makes a decision on each of the\u00a0R.S. 2477 cases, which are cases brought by Utah and counties to keep historical roads on BLM land in Utah open for public use.</p><p>By way of background, a provision of the Mining Law of 1866, commonly known as\u00a0R.S. 2477, granted rights-of-way to states and counties across public lands for the construction of roads for public use in order to promote settlement of the American West. In 1976, Congress repealed R.S. 2477 when it enacted the Federal Land Policy and Management Act (FLPMA), but FLPMA preserved rights-of-way that had been established under R.S. 2477. After the BLM released travel management plans that closed some historical roads, Utah and 22 counties filed lawsuits about their rights-of-way across public lands for historical roads.</p><p>Until the BLM certifies that those cases have been decided, the bill prohibits the BLM from obligating or expending federal funds to (1) finalize or implement a new travel management plan for certain travel management areas in Utah; or (2) implement, with respect to land within the boundary of Utah, the Indian Creek (Canyon Rims) Travel Management Plan, the San Rafael Desert Travel Management Plan, the San Rafael Swell Travel Management Plan, or the Labyrinth/Gemini Bridges Travel Management Plan.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s90"
    },
    "title": "Historic Roadways Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Historic Roadways Protection Act</strong></p><p>This bill prohibits the Bureau for Land Management (BLM) from closing historical roads on public lands in certain areas of Utah until the Federal District Court for Utah makes a decision on each of the\u00a0R.S. 2477 cases, which are cases brought by Utah and counties to keep historical roads on BLM land in Utah open for public use.</p><p>By way of background, a provision of the Mining Law of 1866, commonly known as\u00a0R.S. 2477, granted rights-of-way to states and counties across public lands for the construction of roads for public use in order to promote settlement of the American West. In 1976, Congress repealed R.S. 2477 when it enacted the Federal Land Policy and Management Act (FLPMA), but FLPMA preserved rights-of-way that had been established under R.S. 2477. After the BLM released travel management plans that closed some historical roads, Utah and 22 counties filed lawsuits about their rights-of-way across public lands for historical roads.</p><p>Until the BLM certifies that those cases have been decided, the bill prohibits the BLM from obligating or expending federal funds to (1) finalize or implement a new travel management plan for certain travel management areas in Utah; or (2) implement, with respect to land within the boundary of Utah, the Indian Creek (Canyon Rims) Travel Management Plan, the San Rafael Desert Travel Management Plan, the San Rafael Swell Travel Management Plan, or the Labyrinth/Gemini Bridges Travel Management Plan.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119s90"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s90is.xml"
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
      "title": "Historic Roadways Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Historic Roadways Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of funds by the Secretary of the Interior to finalize and implement certain travel management plans in the State of Utah.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:36Z"
    }
  ]
}
```
