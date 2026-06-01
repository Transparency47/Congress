# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1597?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1597
- Title: Paycheck Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1597
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2025-12-05T22:52:44Z
- Update date including text: 2025-12-05T22:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1597",
    "number": "1597",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Paycheck Protection Act",
    "type": "S",
    "updateDate": "2025-12-05T22:52:44Z",
    "updateDateIncludingText": "2025-12-05T22:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T22:37:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "UT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1597is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1597\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Sheehy (for himself, Mr. Lee , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to provide that agencies may not deduct labor organization dues from the pay of Federal employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paycheck Protection Act .\n#### 2. Labor organization dues not deductible from pay\n##### (a) Federal agencies\n**(1) In general**\nSection 7115 of title 5, United States Code, is amended to read as follows:\n7115. Labor organization dues not deductible from pay An agency may not deduct any amount from the pay of an employee for labor organization dues, fees, or political contributions. .\n**(2) Clerical amendment**\nThe table of sections for subchapter II of chapter 71 of title 5, United States Code, is amended by striking the item relating to section 7115 and inserting the following:\n7115. Labor organization dues not deductible from pay. .\n##### (b) Postal Service\n**(1) In general**\nSection 1205 of title 39, United States Code, is amended to read as follows:\n1205. Labor organization dues not deductible from pay The Postal Service may not deduct any amount from the pay of an employee for labor organization dues, fees, or political contributions. .\n**(2) Clerical amendment**\nThe table of sections for chapter 12 of title 39, United States Code, is amended by striking the item relating to section 1205 and inserting the following:\n1205. Labor organization dues not deductible from pay. .",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-03-25",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21."
      },
      "number": "2174",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paycheck Protection Act",
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
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-03T15:55:50Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-03T15:55:50Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-06-03T15:55:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-04T15:35:13Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1597is.xml"
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
      "title": "Paycheck Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Paycheck Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to provide that agencies may not deduct labor organizations dues from the pay of Federal employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:43Z"
    }
  ]
}
```
