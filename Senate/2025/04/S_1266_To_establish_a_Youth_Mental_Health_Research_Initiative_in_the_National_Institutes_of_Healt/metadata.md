# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1266?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1266
- Title: Youth Mental Health Research Act
- Congress: 119
- Bill type: S
- Bill number: 1266
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-12-05T22:06:04Z
- Update date including text: 2025-12-05T22:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1266",
    "number": "1266",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "Youth Mental Health Research Act",
    "type": "S",
    "updateDate": "2025-12-05T22:06:04Z",
    "updateDateIncludingText": "2025-12-05T22:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T20:51:29Z",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1266is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1266\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Ms. Klobuchar (for herself and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a Youth Mental Health Research Initiative in the National Institutes of Health for purposes of encouraging collaborative research to improve youth mental health.\n#### 1. Short title\nThis Act may be cited as the Youth Mental Health Research Act .\n#### 2. Collaborative research on youth mental health\nPart B of title IV of the Public Health Service Act ( 42 U.S.C. 284 et seq. ) is amended by adding at the end the following:\n409K. Collaborative research on youth mental health (a) In general The Director of NIH shall establish a Youth Mental Health Research Initiative, to be led by the Director of the National Institute of Mental Health, in collaboration with the Director of the Eunice Kennedy Shriver National Institute of Child Health and Human Development and the Director of the National Institute on Minority Health and Health Disparities, to coordinate and encourage collaboration among the national research institutes and national centers with respect to fundamental and applied research on youth mental health, including\u2014 (1) social, behavioral, cognitive, and developmental research, to build resilience and increase the capacity of communities to identify and care for youth at risk or in crisis; and (2) research to improve the targeting and delivery of mental health interventions in clinical and community settings where youth live, play, work, and learn. (b) Authorization of appropriations There are authorized to be appropriated to carry out this section $100,000,000 for each of fiscal years 2025 through 2030. .",
      "versionDate": "2025-04-02",
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2587",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Youth Mental Health Research Act",
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
        "name": "Health",
        "updateDate": "2025-05-02T13:25:44Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1266is.xml"
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
      "title": "Youth Mental Health Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Youth Mental Health Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Youth Mental Health Research Initiative in the National Institutes of Health for purposes of encouraging collaborative research to improve youth mental health.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:55Z"
    }
  ]
}
```
