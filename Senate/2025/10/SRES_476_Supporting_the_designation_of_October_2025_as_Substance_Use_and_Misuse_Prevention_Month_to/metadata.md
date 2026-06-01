# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/476
- Title: A resolution supporting the designation of October 2025 as "Substance Use & Misuse Prevention Month" to raise awareness of substance use and misuse in the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 476
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-12-02T16:33:51Z
- Update date including text: 2025-12-02T16:33:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7851)
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7851)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/476",
    "number": "476",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution supporting the designation of October 2025 as \"Substance Use & Misuse Prevention Month\" to raise awareness of substance use and misuse in the United States.",
    "type": "SRES",
    "updateDate": "2025-12-02T16:33:51Z",
    "updateDateIncludingText": "2025-12-02T16:33:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7851)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T16:21:13Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres476is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 476\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Ricketts (for himself and Mr. Schiff ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nSupporting the designation of October 2025 as Substance Use & Misuse Prevention Month to raise awareness of substance use and misuse in the United States.\nThat the Senate supports\u2014\n**(1)**\neffective programs to prevent substance use and misuse;\n**(2)**\nprograms to help stem the drug addiction and overdose epidemic in the United States; and\n**(3)**\nthe designation of October 2025 as Substance Use & Misuse Prevention Month .",
      "versionDate": "2025-10-30",
      "versionType": "IS"
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
        "updateDate": "2025-12-02T16:33:51Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres476is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution supporting the designation of October 2025 as \"Substance Use & Misuse Prevention Month\" to raise awareness of substance use and misuse in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-01T03:48:19Z"
    },
    {
      "title": "A resolution supporting the designation of October 2025 as \"Substance Use & Misuse Prevention Month\" to raise awareness of substance use and misuse in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T10:56:17Z"
    }
  ]
}
```
