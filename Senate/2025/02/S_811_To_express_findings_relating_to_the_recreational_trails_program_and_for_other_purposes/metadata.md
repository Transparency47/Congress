# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/811?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/811
- Title: RTP Full Funding Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 811
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-02-11T15:10:38Z
- Update date including text: 2026-02-11T15:10:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/811",
    "number": "811",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "RTP Full Funding Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T15:10:38Z",
    "updateDateIncludingText": "2026-02-11T15:10:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T21:18:20Z",
          "name": "Referred To"
        }
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ID"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "UT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s811is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 811\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Ms. Klobuchar (for herself, Mr. Risch , Mr. Welch , Mr. Budd , Mr. Curtis , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo express findings relating to the recreational trails program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the RTP Full Funding Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe recreational trails program under section 206 of title 23, United States Code\u2014\n**(A)**\nfunds development and maintenance of valuable trail infrastructure across the United States;\n**(B)**\nbenefits millions of diverse trail users, including users who participate in hiking, bicycling, in-line skating, equestrian use, cross-country skiing, snowmobiling, off-road motorcycling, all-terrain vehicle riding, 4-wheel off-highway vehicle driving, and other off-road motorized vehicle use;\n**(C)**\n**(i)**\nembraces the user-pay-user-benefit model of the Highway Trust Fund;\n**(ii)**\nis funded by a Federal tax on fuel used for nonhighway recreation;\n**(iii)**\nis funded on an annual basis of approximately $84,000,000; and\n**(iv)**\ndoes not receive the amounts collected from the average annual fuel tax, $281,000,000, that are paid into the Highway Trust Fund by nonhighway recreation vehicles;\n**(D)**\ncontributes significantly to national transportation, economic development, health, public land access and enjoyment, and other national priorities; and\n**(E)**\nshould be funded at a level commensurate with tax contributions from nonhighway vehicle recreation;\n**(2)**\nto ensure that Federal taxes collected from nonhighway recreation are appropriately returned to the States for the recreational trails program described in paragraph (1), an accurate estimate of the total amount of nonhighway fuel taxes collected\u2014\n**(A)**\nis necessary; and\n**(B)**\nshould be provided to Congress by the Federal Highway Administration at least 1 year before the date on which funding for Federal-aid highways, highway safety programs, and transit programs is anticipated to expire; and\n**(3)**\nthe recreational trails program under section 206 of title 23, United States Code, should be carried out through funding made available under section 133(h) of that title (commonly known as the Transportation Alternatives program ) without affecting other Federal highway programs.",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": {
          "name": "Parks, recreation areas, trails",
          "updateDate": "2026-02-11T15:10:38Z"
        }
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:22:25Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s811is.xml"
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
      "title": "RTP Full Funding Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RTP Full Funding Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to express findings relating to the recreational trails program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:52Z"
    }
  ]
}
```
