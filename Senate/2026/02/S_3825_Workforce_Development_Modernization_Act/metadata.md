# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3825?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3825
- Title: Workforce Development Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 3825
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-03-02T17:30:13Z
- Update date including text: 2026-03-02T17:30:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3825",
    "number": "3825",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Workforce Development Modernization Act",
    "type": "S",
    "updateDate": "2026-03-02T17:30:13Z",
    "updateDateIncludingText": "2026-03-02T17:30:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T21:59:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "LA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3825is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3825\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Budd (for himself, Mr. Cassidy , Mr. Ricketts , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to expand the types of one-stop centers used to provide services.\n#### 1. Short title\nThis Act may be cited as the Workforce Development Modernization Act .\n#### 2. One-stop centers\nSection 121(e) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3151(e) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by striking 1 physical center in each local area of the State; and and inserting 1 physical or virtual center in each local area of the State, or at 1 or more physical or virtual centers shared by adjacent local areas and not less than 1 such center in each other local area of the State; ;\n**(B)**\nin subparagraph (C), by striking and at the end;\n**(C)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(E) may locate a physical or virtual center described in subparagraph (A) at a public institution of higher education. ;\n**(2)**\nin paragraph (3), by striking , the employment service and all that follows and inserting , in each State that has a physical one-stop center, the employment service offices in that State shall be colocated with the physical one-stop centers in that State. ;\n**(3)**\nby redesignating paragraph (4) as paragraph (3); and\n**(4)**\nby adding at the end the following:\n(5) Relationships with local areas and States For purposes of applying this Act in a situation in which 2 adjacent local areas share a physical or virtual one-stop center, a reference in this Act to a one-stop center that is in a local area or State shall be considered to be a reference to a one-stop center for that local area or State, respectively. (6) Virtual center In this subsection, the term virtual , used with respect to a one-stop center, means a terminal or other equipment that provides access to each of the programs, services, and activities described in paragraph (1). .\n#### 3. Conforming amendment\nSection 3(d) of the Wagner-Peyser Act ( 29 U.S.C. 49b(d) ) is amended by striking , employment service and all that follows and inserting , in each State that has a physical one-stop center, the employment service offices in that State shall be colocated with the physical one-stop centers in that State. .",
      "versionDate": "2026-02-10",
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
        "name": "Labor and Employment",
        "updateDate": "2026-03-02T17:30:12Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3825is.xml"
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
      "title": "Workforce Development Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Workforce Development Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Workforce Innovation and Opportunity Act to expand the types of one-stop centers used to provide services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:33:28Z"
    }
  ]
}
```
