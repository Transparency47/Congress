# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/214?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/214
- Title: MEDAL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 214
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/214",
    "number": "214",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "MEDAL Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
            "date": "2025-05-21T20:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-23T18:22:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sponsorshipDate": "2025-01-23",
      "state": "AR"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "WV"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s214is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 214\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cruz (for himself and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the rate of the special pension payable to Medal of Honor recipients, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Monetary Enhancement for Distinguished Active Legends Act of 2025 or the MEDAL Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Medal of Honor is the highest and most prestigious military decoration of the United States.\n**(2)**\nTo earn the Medal of Honor, the deed of the person \u2026 must be so outstanding that it clearly distinguishes his gallantry beyond the call of duty from lesser forms of bravery .\n**(3)**\nThe actions of Medal of Honor recipients inspire bravery, and the willingness to give all, in those who serve in the Armed Forces and those who will serve in the future.\n**(4)**\nThose listed on the Medal of Honor Roll exemplify the best traits of members of the Armed Forces, a long and proud lineage of those who went beyond the call of duty.\n**(5)**\nPursuant to section 1562 of title 38, United States Code, the Secretary of Veterans Affairs shall pay monthly to each living person whose name has been entered on the Army, Navy, Air Force, and Coast Guard Medal of Honor Roll a special pension.\n**(6)**\nRecipients of the Medal of Honor have earned a substantial and historic increase to such special pension in recognition of their conspicuous gallantry, unwavering commitment, and heroic actions above and beyond the call of duty.\n#### 3. Increase in Department of Veterans Affairs special pension payable to Medal of Honor recipients\n##### (a) Increase in special pension payable to living Medal of Honor recipients\nParagraph (1) of section 1562(a) of title 38, United States Code, is amended by striking $1,406.73 and inserting $8,333.33 .\n##### (b) Amount of special pension payable to surviving spouses\nParagraph (2)(A) of such section is amended\u2014\n**(1)**\nby striking special pension under this section and inserting monthly ; and\n**(2)**\nby striking the period and adding at the end the following: a special pension under this section at the rate of $1,406.73, as adjusted from time to time under subsection (e). .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-12-01",
        "text": "Became Public Law No: 119-43."
      },
      "number": "695",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medal of Honor Act",
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
            "name": "Inflation and prices",
            "updateDate": "2025-03-21T19:22:03Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-21T19:22:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T19:19:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s214",
          "measure-number": "214",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s214v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Monetary Enhancement for Distinguished Active Legends Act of 2025 or the MEDAL Act of 2025</strong></p><p>This bill increases the monthly special pension for living Medal of Honor recipients from $1,406.73 to $8,333.33 and establishes a rate of $1,406.73 for the monthly special pension for surviving spouses of Medal of Honor recipients. Both amounts must be adjusted annually for inflation.</p>"
        },
        "title": "MEDAL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s214.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Monetary Enhancement for Distinguished Active Legends Act of 2025 or the MEDAL Act of 2025</strong></p><p>This bill increases the monthly special pension for living Medal of Honor recipients from $1,406.73 to $8,333.33 and establishes a rate of $1,406.73 for the monthly special pension for surviving spouses of Medal of Honor recipients. Both amounts must be adjusted annually for inflation.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s214"
    },
    "title": "MEDAL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Monetary Enhancement for Distinguished Active Legends Act of 2025 or the MEDAL Act of 2025</strong></p><p>This bill increases the monthly special pension for living Medal of Honor recipients from $1,406.73 to $8,333.33 and establishes a rate of $1,406.73 for the monthly special pension for surviving spouses of Medal of Honor recipients. Both amounts must be adjusted annually for inflation.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s214"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s214is.xml"
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
      "title": "MEDAL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MEDAL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Monetary Enhancement for Distinguished Active Legends Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to increase the rate of the special pension payable to Medal of Honor recipients, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:57Z"
    }
  ]
}
```
