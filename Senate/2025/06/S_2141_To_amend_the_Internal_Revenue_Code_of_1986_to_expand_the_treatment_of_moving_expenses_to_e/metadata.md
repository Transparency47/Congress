# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2141
- Title: Intelligence Community Workforce Agility Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2141
- Origin chamber: Senate
- Introduced date: 2025-06-23
- Update date: 2026-01-13T12:03:23Z
- Update date including text: 2026-01-13T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in Senate
- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-23: Introduced in Senate

## Actions

- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2141",
    "number": "2141",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Intelligence Community Workforce Agility Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-01-13T12:03:23Z",
    "updateDateIncludingText": "2026-01-13T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-23",
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
            "date": "2025-06-23T21:57:34Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-23T21:57:34Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "VA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "ME"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "OK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "AZ"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "KS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "SD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2141is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2141\nIN THE SENATE OF THE UNITED STATES\nJune 23, 2025 Mr. Cotton (for himself, Mr. Warner , Ms. Collins , Mr. Lankford , Mr. Kelly , Mr. Moran , Mr. Budd , Mr. Rounds , Mr. Young , Mr. Bennet , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the treatment of moving expenses to employees and new appointees in the intelligence community who move pursuant to a change in assignment that requires relocation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Intelligence Community Workforce Agility Protection Act of 2025 .\n#### 2. Expansion of treatment of moving expenses\n##### (a) Purpose\nThe purpose of this section is to facilitate the movement of members of the intelligence community to meet mission critical needs and to reduce unintended tax burdens imposed on public servants in relocating duty stations.\n##### (b) Deduction\nSection 217(k) of the Internal Revenue Code of 1986 is amended by inserting or an employee or new appointee of the intelligence community (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )) (other than a member of the Armed Forces of the United States) who moves pursuant to a change in assignment that requires relocation after to whom subsection (g) applies .\n##### (c) Exclusion for qualified moving expense reimbursements\nSection 132(g)(2) of the Internal Revenue Code of 1986 is amended by inserting , or an employee or new appointee of the intelligence community (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )) (other than a member of the Armed Forces of the United States) who moves pursuant to a change in assignment that requires relocation after change of station .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-06-23",
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
        "name": "Taxation",
        "updateDate": "2025-07-07T19:16:11Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2141is.xml"
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
      "title": "Intelligence Community Workforce Agility Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Intelligence Community Workforce Agility Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand the treatment of moving expenses to employees and new appointees in the intelligence community who move pursuant to a change in assignment that requires relocation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:05Z"
    }
  ]
}
```
