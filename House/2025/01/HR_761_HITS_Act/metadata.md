# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/761
- Title: HITS Act
- Congress: 119
- Bill type: HR
- Bill number: 761
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T21:39:03Z
- Update date including text: 2025-12-05T21:39:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/761",
    "number": "761",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "HITS Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:39:03Z",
    "updateDateIncludingText": "2025-12-05T21:39:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-28T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr761ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 761\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Estes (for himself and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for an election to expense certain qualified sound recording costs otherwise chargeable to capital account.\n#### 1. Short title\nThis Act may be cited as the Help Independent Tracks Succeed Act or the HITS Act .\n#### 2. Treatment of certain qualified sound recording productions\n##### (a) Election To treat costs as expenses\nSection 181(a)(1) of the Internal Revenue Code of 1986 is amended by striking qualified film or television production, and any qualified live theatrical production, and inserting qualified film or television production, any qualified live theatrical production, and any qualified sound recording production .\n##### (b) Dollar limitation\nSection 181(a)(2) of such Code is amended by adding at the end the following new paragraph:\n(C) Qualified sound recording production Paragraph (1) shall not apply to so much of the aggregate cost of any qualified sound recording production, or to so much of the aggregate, cumulative cost of all such qualified sound recording productions in the taxable year, as exceeds $150,000. .\n##### (c) No other deduction or amortization deduction allowable\nSection 181(b) of such Code is amended by striking qualified film or television production or any qualified live theatrical production and inserting qualified film or television production, any qualified live theatrical production, or any qualified sound recording production .\n##### (d) Election\nSection 181(c)(1) of such Code is amended by striking qualified film or television production or any qualified live theatrical production and inserting qualified film or television production, any qualified live theatrical production, or any qualified sound recording production .\n##### (e) Qualified sound recording production defined\nSection 181 of such Code is amended by redesignating subsections (f) and (g) as subsections (g) and (h), respectively, and by inserting after subsection (e) the following new subsection:\n(f) Qualified sound recording production For purposes of this section, the term qualified sound recording production means a sound recording (as defined in section 101 of title 17, United States Code) produced and recorded in the United States. .\n##### (f) Bonus depreciation\n**(1) Qualified sound recording production as qualified property**\nSection 168(k)(2)(A)(i) of such Code is amended\u2014\n**(A)**\nby striking or at the end of subclause (IV), by adding or at the end of subclause (V), and by inserting after subclause (V) the following:\n(VI) which is a qualified sound recording production (as defined in subsection (f) of section 181) for which a deduction would have been allowable under section 181 without regard to subsections (a)(2) and (h) of such section or this subsection, ; and\n**(B)**\nin subclauses (IV) and (V) (as amended) by striking without regard to subsections (a)(2) and (g) both places it appears and inserting without regard to subsections (a)(2) and (h) .\n**(2) Production placed in service**\nSection 168(k)(2)(H) of such Code is amended by striking and at the end of clause (i), by striking the period at the end of clause (ii) and inserting , and , and by adding after clause (ii) the following:\n(iii) a qualified sound recording production shall be considered to be placed in service at the time of initial release or broadcast. .\n##### (g) Conforming amendments\n**(1)**\nThe heading for section 181 of such Code is amended to read as follows: Treatment of certain qualified productions . .\n**(2)**\nThe table of sections for part VI of subchapter B of chapter 1 of such Code is amended by striking the item relating to section 181 and inserting the following new item:\nSec. 181. Treatment of certain qualified productions. .\n##### (h) Effective date\nThe amendments made by this section shall apply to productions commencing in taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "194",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HITS Act",
      "type": "S"
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
        "updateDate": "2025-04-07T16:21:53Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr761ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HITS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HITS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Help Independent Tracks Succeed Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for an election to expense certain qualified sound recording costs otherwise chargeable to capital account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:21Z"
    }
  ]
}
```
