# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2263?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2263
- Title: Control Tower Continuity Act
- Congress: 119
- Bill type: S
- Bill number: 2263
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2025-09-12T20:41:42Z
- Update date including text: 2025-09-12T20:41:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2263",
    "number": "2263",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Control Tower Continuity Act",
    "type": "S",
    "updateDate": "2025-09-12T20:41:42Z",
    "updateDateIncludingText": "2025-09-12T20:41:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T18:55:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2263is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2263\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to exempt air traffic controllers from certain mandatory separation requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Control Tower Continuity Act .\n#### 2. Exemptions from mandatory separation for air traffic controllers\n##### (a) Removal of age limitation\n**(1) In general**\nSection 8425(a) of title 5, United States Code, is amended, in the second sentence, by striking until that controller becomes 61 years of age .\n**(2) Conforming amendment**\nSection 8335(a) of title 5, United States Code, is amended, in the second sentence, by striking until that controller becomes 61 years of age .\n**(3) Effective date**\nThe amendments made by this subsection shall apply on or after 180 days after the date of enactment of this section.\n##### (b) Expiration of medical clearance\nNot later than 180 days after the date of enactment of this section, the Administrator of the Federal Aviation Administration shall update FAA Order 3930.3C, titled Air Traffic Control Specialist Health Program and issued on June 17, 2019, or any successor regulation, to require the medical clearance for any air traffic controllers that are 61 years of age or older to expire on the last day of the 6-month period following the date of examination required to obtain such clearance.",
      "versionDate": "2025-07-10",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-12T20:41:42Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2263is.xml"
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
      "title": "Control Tower Continuity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Control Tower Continuity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to exempt air traffic controllers from certain mandatory separation requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:29Z"
    }
  ]
}
```
