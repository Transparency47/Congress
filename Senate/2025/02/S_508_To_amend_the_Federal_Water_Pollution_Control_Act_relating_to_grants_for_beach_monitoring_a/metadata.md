# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/508
- Title: BEACH Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 508
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/508",
    "number": "508",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "BEACH Act of 2025",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
            "date": "2025-02-11T15:52:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-11T15:52:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s508is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 508\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Wyden (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Federal Water Pollution Control Act relating to grants for beach monitoring, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Beaches Environmental Assessment and Coastal Health Act of 2025 or the BEACH Act of 2025 .\n#### 2. Coastal Recreation Water Quality Monitoring And Notification\n##### (a) Program Development and Implementation Grants\nSection 406 of the Federal Water Pollution Control Act ( 33 U.S.C. 1346 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting , including nearby shallow upstream waters, after coastal recreation waters ; and\n**(ii)**\nby inserting or present on after adjacent to ;\n**(B)**\nin paragraph (3)(A)\u2014\n**(i)**\nin clause (i), by striking and at the end;\n**(ii)**\nby redesignating clause (ii) as clause (iii); and\n**(iii)**\nby inserting after clause (i) the following:\n(ii) in the case of a State that uses such grant to identify specific sources of contamination pursuant to paragraph (5), any data relating to such identified sources of contamination; and ; and\n**(C)**\nby adding at the end the following:\n(5) Identification of specific sources of contamination A State or local government receiving a grant under this subsection may use such grant to identify specific sources of contamination for coastal recreation waters, including nearby shallow upstream waters, adjacent to or present on beaches or similar points of access that are used by the public. ;\n**(2)**\nin subsection (g)(1)\u2014\n**(A)**\nby inserting , including nearby shallow upstream waters, after coastal recreation waters ; and\n**(B)**\nby inserting or present on after adjacent to ; and\n**(3)**\nin subsection (i), by striking $30,000,000 for each of fiscal years 2001 through 2005 and inserting $30,000,000 for each of fiscal years 2025 through 2029 .\n##### (b) Authorization of appropriations\nSection 8 of the Beaches Environmental Assessment and Coastal Health Act of 2000 ( Public Law 106\u2013284 ; 114 Stat. 877) is amended by striking 2001 through 2005 and inserting 2025 through 2029 .\n#### 3. Guidance\nIn providing guidance to States and local governments receiving grants under section 406 of the Federal Water Pollution Control Act ( 33 U.S.C. 1346 ), the Administrator of the Environmental Protection Agency shall ensure that such guidance reflects innovations in testing technologies for water contamination.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-01-22",
        "text": "Referred to the Subcommittee on Water Resources and Environment."
      },
      "number": "583",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BEACH Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-03-12T14:21:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s508",
          "measure-number": "508",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-07-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s508v00",
            "update-date": "2025-07-29"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Beaches Environmental Assessment and Coastal Health Act of 2025 or the BEACH Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and expands an existing program of the Environmental Protection Agency (EPA) that awards grants to states and local governments to (1) monitor the water quality of coastal recreational waters adjacent to beaches or similar points of access that are used by the public; and (2) notify the public, local governments, and the EPA when the water is not safe for recreational activities.</p><p>Specifically, the bill expands the program to allow the EPA to award grants for identifying sources of contamination (i.e., pathogens) for coastal recreation waters. It also allows grants to be used for monitoring and notification of contamination in (1) shallow waters upstream from recreational waters, and (2) recreational waters on beaches.</p>"
        },
        "title": "BEACH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s508.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Beaches Environmental Assessment and Coastal Health Act of 2025 or the BEACH Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and expands an existing program of the Environmental Protection Agency (EPA) that awards grants to states and local governments to (1) monitor the water quality of coastal recreational waters adjacent to beaches or similar points of access that are used by the public; and (2) notify the public, local governments, and the EPA when the water is not safe for recreational activities.</p><p>Specifically, the bill expands the program to allow the EPA to award grants for identifying sources of contamination (i.e., pathogens) for coastal recreation waters. It also allows grants to be used for monitoring and notification of contamination in (1) shallow waters upstream from recreational waters, and (2) recreational waters on beaches.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119s508"
    },
    "title": "BEACH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Beaches Environmental Assessment and Coastal Health Act of 2025 or the BEACH Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and expands an existing program of the Environmental Protection Agency (EPA) that awards grants to states and local governments to (1) monitor the water quality of coastal recreational waters adjacent to beaches or similar points of access that are used by the public; and (2) notify the public, local governments, and the EPA when the water is not safe for recreational activities.</p><p>Specifically, the bill expands the program to allow the EPA to award grants for identifying sources of contamination (i.e., pathogens) for coastal recreation waters. It also allows grants to be used for monitoring and notification of contamination in (1) shallow waters upstream from recreational waters, and (2) recreational waters on beaches.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119s508"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s508is.xml"
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
      "title": "BEACH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Water Pollution Control Act relating to grants for beach monitoring, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BEACH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Beaches Environmental Assessment and Coastal Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:25Z"
    }
  ]
}
```
