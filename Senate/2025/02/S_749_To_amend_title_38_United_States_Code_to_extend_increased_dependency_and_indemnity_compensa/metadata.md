# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/749
- Title: Justice for ALS Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 749
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/749",
    "number": "749",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Justice for ALS Veterans Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
            "date": "2026-04-29T21:37:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-26T19:04:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-26T19:04:19Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "SD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "RI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "LA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "ND"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "WI"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s749is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 749\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Ms. Murkowski (for herself, Mr. Coons , Mr. Rounds , Mr. Whitehouse , Ms. Slotkin , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to extend increased dependency and indemnity compensation paid to surviving spouses of veterans who die from amyotrophic lateral sclerosis, regardless of how long the veterans had such disease prior to death, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for ALS Veterans Act of 2025 .\n#### 2. Extension of increased dependency and indemnity compensation to surviving spouses of veterans who die from amyotrophic lateral sclerosis\n##### (a) Extension\nSection 1311(a)(2) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting (A) before The rate ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) A veteran whom the Secretary determines died from amyotrophic lateral sclerosis shall be treated as a veteran described in subparagraph (A) without regard for how long the veteran had such disease prior to death. .\n##### (b) Applicability\nSubparagraph (B) of section 1311(a)(2) of title 38, United States Code, as added by subsection (a), shall apply to a veteran who dies from amyotrophic lateral sclerosis on or after October 1, 2022.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2026-01-15",
        "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs."
      },
      "number": "6636",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance sensible priorities.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-03",
        "text": "Subcommittee Hearings Held"
      },
      "number": "1685",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for ALS Veterans Act of 2025",
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
            "name": "Marriage and family status",
            "updateDate": "2025-08-29T17:04:01Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-08-29T17:04:01Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-08-29T17:04:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:53:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s749",
          "measure-number": "749",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s749v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Justice for ALS Veterans Act of 2025</strong></p><p>This bill extends increased dependency and indemnity compensation to the surviving spouse of a veteran whom the Department of Veterans Affairs has determined died from\u00a0amyotrophic lateral sclerosis (ALS or Lou Gehrig's disease) regardless of how long the veteran had such disease prior to death. Under current law, such compensation is paid for a service-connected disability that was rated totally disabling for a continuous period of at least eight years immediately preceding death.</p><p>Under the bill, such extension of increased compensation applies retroactively to veterans who died from\u00a0ALS on or after October 1, 2022.</p>"
        },
        "title": "Justice for ALS Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s749.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for ALS Veterans Act of 2025</strong></p><p>This bill extends increased dependency and indemnity compensation to the surviving spouse of a veteran whom the Department of Veterans Affairs has determined died from\u00a0amyotrophic lateral sclerosis (ALS or Lou Gehrig's disease) regardless of how long the veteran had such disease prior to death. Under current law, such compensation is paid for a service-connected disability that was rated totally disabling for a continuous period of at least eight years immediately preceding death.</p><p>Under the bill, such extension of increased compensation applies retroactively to veterans who died from\u00a0ALS on or after October 1, 2022.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s749"
    },
    "title": "Justice for ALS Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for ALS Veterans Act of 2025</strong></p><p>This bill extends increased dependency and indemnity compensation to the surviving spouse of a veteran whom the Department of Veterans Affairs has determined died from\u00a0amyotrophic lateral sclerosis (ALS or Lou Gehrig's disease) regardless of how long the veteran had such disease prior to death. Under current law, such compensation is paid for a service-connected disability that was rated totally disabling for a continuous period of at least eight years immediately preceding death.</p><p>Under the bill, such extension of increased compensation applies retroactively to veterans who died from\u00a0ALS on or after October 1, 2022.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s749"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s749is.xml"
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
      "title": "Justice for ALS Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Justice for ALS Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to extend increased dependency and indemnity compensation paid to surviving spouses of veterans who die from amyotrophic lateral sclerosis, regardless of how long the veterans had such disease prior to death, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:08Z"
    }
  ]
}
```
