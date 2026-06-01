# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1234
- Title: SSI Savings Penalty Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 1234
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-12-05T21:34:19Z
- Update date including text: 2025-12-05T21:34:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1234",
    "number": "1234",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "SSI Savings Penalty Elimination Act",
    "type": "S",
    "updateDate": "2025-12-05T21:34:19Z",
    "updateDateIncludingText": "2025-12-05T21:34:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T20:16:30Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "LA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "ME"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OK"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AK"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "RI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "SD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1234is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1234\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Ms. Cortez Masto (for herself, Mr. Cassidy , Mr. Wyden , Ms. Collins , Ms. Hassan , Mr. Lankford , Mrs. Murray , Ms. Murkowski , Mr. Whitehouse , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVI of the Social Security Act to update the resource limit for supplemental security income eligibility.\n#### 1. Short title\nThis Act may be cited as the SSI Savings Penalty Elimination Act .\n#### 2. Update in eligibility for the supplemental security income program\n##### (a) Update in resource limit for individuals and couples\nSection 1611(a)(3) of such Act ( 42 U.S.C. 1382(a)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking $2,250 and all that follows through the end of the subparagraph and inserting $20,000 in calendar year 2025, and shall be increased as described in section 1617(d) for each subsequent calendar year. ; and\n**(2)**\nin subparagraph (B), by striking $1,500 and all that follows through the end of the subparagraph and inserting $10,000 in calendar year 2025, and shall be increased as described in section 1617(d) for each subsequent calendar year. .\n##### (b) Inflation adjustment\nSection 1617 of such Act ( 42 U.S.C. 1382f ) is amended\u2014\n**(1)**\nin the section heading, by inserting ; inflation adjustment after benefits ; and\n**(2)**\nby adding at the end the following:\n(d) In the case of any calendar year after 2025, each of the amounts specified in section 1611(a)(3) shall be increased by multiplying each such amount by the quotient (not less than 1) obtained by dividing\u2014 (1) the average of the consumer price index for all urban consumers (all items; United States city average, as published by the Bureau of Labor Statistics of the Department of Labor) for the 12-month period ending with September of the preceding calendar year, by (2) such average for the 12-month period ending with September 2024. .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2540",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SSI Savings Penalty Elimination Act",
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
        "name": "Social Welfare",
        "updateDate": "2025-05-02T13:23:41Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1234is.xml"
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
      "title": "SSI Savings Penalty Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SSI Savings Penalty Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVI of the Social Security Act to update the resource limit for supplemental security income eligibility.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:52Z"
    }
  ]
}
```
