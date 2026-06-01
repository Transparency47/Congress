# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1843
- Title: Second Chance Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1843
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-04-15T21:05:07Z
- Update date including text: 2026-04-15T21:05:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1843",
    "number": "1843",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Second Chance Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T21:05:07Z",
    "updateDateIncludingText": "2026-04-15T21:05:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T20:29:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "TX"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NC"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "RI"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "ND"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "VT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "AL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MN"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1843is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1843\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mrs. Capito (for herself, Mr. Booker , Mr. Cornyn , Mr. Durbin , Mr. Tillis , Mr. Whitehouse , Mr. Cramer , Mr. Welch , Mrs. Britt , Ms. Klobuchar , Mr. Justice , Mr. Coons , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo reauthorize the Second Chance Act of 2007.\n#### 1. Short title\nThis Act may be cited as the Second Chance Reauthorization Act of 2025 .\n#### 2. Improvements to existing programs\n##### (a) State and local reentry demonstration projects\nSection 2976 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10631 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (7), by striking and at the end;\n**(B)**\nin paragraph (8), by striking the period at the end; and\n**(C)**\nby adding at the end the following:\n(9) treating substance use disorders, including by providing peer recovery services, case management, and access to overdose education and overdose reversal medications; and (10) providing reentry housing services. ; and\n**(2)**\nin subsection (o)(1), by striking 2019 through 2023 and inserting 2026 through 2030 .\n##### (b) Grants for family-Based substance abuse treatment\nSection 2926(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10595a(a) ) is amended by striking 2019 through 2023 and inserting 2026 through 2030 .\n##### (c) Grant program To evaluate and improve educational methods at prisons, jails, and juvenile facilities\nSection 1001(a)(28) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a)(28) ) is amended by striking 2019, 2020, 2021, 2022, and 2023 and inserting 2026 through 2030 .\n##### (d) Careers training demonstration grants\nSection 115(f) of the Second Chance Act of 2007 ( 34 U.S.C. 60511(f) ) is amended by striking 2019, 2020, 2021, 2022, and 2023 and inserting 2026 through 2030 .\n##### (e) Offender reentry substance abuse and criminal justice collaboration program\nSection 201(f)(1) of the Second Chance Act of 2007 ( 34 U.S.C. 60521(f)(1) ) is amended by striking 2019 through 2023 and inserting 2026 through 2030 .\n##### (f) Community-Based mentoring and transitional service grants to nonprofit organizations\nSection 211(f) of the Second Chance Act of 2007 ( 34 U.S.C. 60531(f) ) is amended by striking 2019 through 2023 and inserting 2026 through 2030 .",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3552",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Second Chance Reauthorization Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-13T12:53:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119s1843",
          "measure-number": "1843",
          "measure-type": "s",
          "orig-publish-date": "2025-05-21",
          "originChamber": "SENATE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1843v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Second Chance Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2030 various federal grants for state, local, and tribal governments, nonprofit organizations, and service providers to support individuals who reenter the community following a period of incarceration.\u00a0</p><p>Specifically, the bill reauthorizes the following:</p><ul><li>grants for adult and juvenile offender reentry demonstration projects;</li><li>grants for family-based substance abuse treatment programs;</li><li>grants to evaluate and improve educational methods at prisons, jails, and juvenile facilities;</li><li>grants for career training education;\u00a0</li><li>the offender reentry substance abuse and criminal justice collaboration\u00a0program; and</li><li>grants to nonprofit organizations for community-based mentoring and transitional services.</li></ul>"
        },
        "title": "Second Chance Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1843.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Second Chance Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2030 various federal grants for state, local, and tribal governments, nonprofit organizations, and service providers to support individuals who reenter the community following a period of incarceration.\u00a0</p><p>Specifically, the bill reauthorizes the following:</p><ul><li>grants for adult and juvenile offender reentry demonstration projects;</li><li>grants for family-based substance abuse treatment programs;</li><li>grants to evaluate and improve educational methods at prisons, jails, and juvenile facilities;</li><li>grants for career training education;\u00a0</li><li>the offender reentry substance abuse and criminal justice collaboration\u00a0program; and</li><li>grants to nonprofit organizations for community-based mentoring and transitional services.</li></ul>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s1843"
    },
    "title": "Second Chance Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Second Chance Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2030 various federal grants for state, local, and tribal governments, nonprofit organizations, and service providers to support individuals who reenter the community following a period of incarceration.\u00a0</p><p>Specifically, the bill reauthorizes the following:</p><ul><li>grants for adult and juvenile offender reentry demonstration projects;</li><li>grants for family-based substance abuse treatment programs;</li><li>grants to evaluate and improve educational methods at prisons, jails, and juvenile facilities;</li><li>grants for career training education;\u00a0</li><li>the offender reentry substance abuse and criminal justice collaboration\u00a0program; and</li><li>grants to nonprofit organizations for community-based mentoring and transitional services.</li></ul>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s1843"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1843is.xml"
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
      "title": "Second Chance Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Second Chance Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Second Chance Act of 2007.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:45Z"
    }
  ]
}
```
