# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1415?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1415
- Title: Housing Unhoused Disabled Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 1415
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-13T16:08:42Z
- Update date including text: 2026-04-13T16:08:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1415",
    "number": "1415",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Housing Unhoused Disabled Veterans Act",
    "type": "S",
    "updateDate": "2026-04-13T16:08:42Z",
    "updateDateIncludingText": "2026-04-13T16:08:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
            "date": "2025-04-10T16:11:23Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T16:11:23Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "LA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ID"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "ID"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1415is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1415\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Padilla (for himself, Mr. McCormick , Mr. Gallego , Mrs. Britt , Mr. Blumenthal , Mr. Cassidy , Mr. Crapo , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Unhoused Disabled Veterans Act .\n#### 2. Exclusion of certain disability benefits\nSection 3(b)(4)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(4)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (iv) and (v) as clauses (vi) and (vii), respectively; and\n**(2)**\nby inserting after clause (iii) the following:\n(iv) for the purpose of determining income eligibility with respect to the supported housing program under section 8(o)(19), any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion shall not apply to the income in the definition of adjusted income; (v) for the purpose of determining income eligibility with respect to any household receiving rental assistance under the supported housing program under section 8(o)(19) as it relates to eligibility for other types of housing assistance, any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion shall not apply to income in the definition of adjusted income; .\n#### 3. Treatment of certain disability benefits\n##### (a) In general\nWhen determining the eligibility of a veteran to rent a residential dwelling unit constructed on Department property on or after the date of the enactment of this Act, for which assistance is provided as part of a housing assistance program administered by the Secretary, the Secretary shall exclude from income any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code by such person.\n##### (b) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Department property**\nThe term Department property has the meaning given the term in section 901 of title 38, United States Code.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-02-11",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "965",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Unhoused Disabled Veterans Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-20T14:04:26Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1415is.xml"
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
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:23Z"
    }
  ]
}
```
