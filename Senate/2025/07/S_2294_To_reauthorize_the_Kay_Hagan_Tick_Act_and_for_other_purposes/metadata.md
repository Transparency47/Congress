# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2294
- Title: Kay Hagan Tick Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 2294
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2025-09-08T20:37:06Z
- Update date including text: 2025-09-08T20:37:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4370-4371: 2)
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4370-4371: 2)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2294",
    "number": "2294",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Kay Hagan Tick Reauthorization Act",
    "type": "S",
    "updateDate": "2025-09-08T20:37:06Z",
    "updateDateIncludingText": "2025-09-08T20:37:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4370-4371: 2)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T22:23:29Z",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-15",
      "state": "ME"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "MO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2294is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2294\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Ms. Collins (for herself, Ms. Smith , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the Kay Hagan Tick Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kay Hagan Tick Reauthorization Act .\n#### 2. Reauthorization of programs\n##### (a) National strategy and regional centers of excellence in vector-Borne disease\nSection 317U of the Public Health Service Act ( 42 U.S.C. 247b\u201323 ) is amended\u2014\n**(1)**\nin subsection (b), in the matter preceding paragraph (1), by striking the Tick-Borne Disease Working Group established under section 2062 of the 21st Century Cures Act ( 42 U.S.C. 284s ) and other individuals, as appropriate and inserting appropriate individuals ; and\n**(2)**\nin subsection (f), by striking $10,000,000 for each of fiscal years 2021 through 2025 and inserting $8,000,000 for each of fiscal years 2026 through 2030 .\n##### (b) Enhanced support To assist health departments in addressing vector-Borne diseases\nSection 2822(c) of the Public Health Service Act ( 42 U.S.C. 300hh\u201332(c) ) is amended by striking $20,000,000 for each of fiscal years 2021 through 2025 and inserting $19,000,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-07-30",
        "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "2398",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kay Hagan Tick Reauthorization Act",
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
        "name": "Health",
        "updateDate": "2025-09-04T16:30:54Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2294is.xml"
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
      "title": "Kay Hagan Tick Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kay Hagan Tick Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Kay Hagan Tick Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:27Z"
    }
  ]
}
```
