# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2707
- Title: FEED Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2707
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2025-10-23T11:18:17Z
- Update date including text: 2025-10-23T11:18:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2707",
    "number": "2707",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "FEED Act of 2025",
    "type": "S",
    "updateDate": "2025-10-23T11:18:17Z",
    "updateDateIncludingText": "2025-10-23T11:18:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T15:22:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2707is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2707\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Husted introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to exclude certain student income from eligibility determinations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Eligibility for Education and Development Act of 2025 or the FEED Act of 2025 .\n#### 2. Exclusion for income of students\nSection 5(d) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(d) ) is amended\u2014\n**(1)**\nin paragraph (18), by striking and at the end;\n**(2)**\nin paragraph (19)(B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(20) income received by a household member under the age of 21\u2014 (A) who\u2014 (i) is a student participating in career and technical education (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )); and (ii) lives with\u2014 (I) a natural, adoptive, or step parent; or (II) is under the parental control of a household member other than a parent described in subclause (I); (B) that is derived from an apprenticeship, internship, or work-based learning program that is a component of the career and technical education described in subparagraph (A)(i) in which the student is participating; and (C) that is determined by the Secretary through procedures established by the Secretary to verify the requirements in subparagraphs (A) and (B), including documentation of enrollment in career and technical education (as so defined) and confirmation of the age and household relationship of the household member. .",
      "versionDate": "2025-09-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-22T19:26:53Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2707is.xml"
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
      "title": "FEED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FEED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Food Eligibility for Education and Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to exclude certain student income from eligibility determinations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:23Z"
    }
  ]
}
```
