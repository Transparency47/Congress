# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2661
- Title: A bill to allow for the use of risk-based inspections for in-service breakout tanks.
- Congress: 119
- Bill type: S
- Bill number: 2661
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T20:06:40Z
- Update date including text: 2025-09-18T20:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2661",
    "number": "2661",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to allow for the use of risk-based inspections for in-service breakout tanks.",
    "type": "S",
    "updateDate": "2025-09-18T20:06:40Z",
    "updateDateIncludingText": "2025-09-18T20:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T21:24:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2661is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2661\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo allow for the use of risk-based inspections for in-service breakout tanks.\n#### 1. Risk-based inspections for in-service breakout tanks\n##### (a) In general\nBeginning on the date of enactment of this Act, an owner or operator of a pipeline facility (as defined in section 60101 of title 49, United States Code) may use risk-based inspections to comply with the relevant inspection requirements imposed under chapter 601 of title 49, United States Code, for in-service breakout tanks, including any relevant requirements established under chapter 195 of title 49, Code of Federal Regulations (or successor regulations).\n##### (b) Rulemaking\nAs soon as practicable after the date of enactment of this Act, the Secretary of Transportation, acting through the Administrator of the Pipeline and Hazardous Materials Safety Administration, shall revise section 195.432 of title 49, Code of Federal Regulations, to allow for risk-based inspections of in-service breakout tanks in accordance with subsection (a).",
      "versionDate": "2025-08-01",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-18T20:06:40Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2661is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow for the use of risk-based inspections for in-service breakout tanks.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:20Z"
    },
    {
      "title": "A bill to allow for the use of risk-based inspections for in-service breakout tanks.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T10:56:18Z"
    }
  ]
}
```
