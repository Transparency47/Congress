# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1268
- Title: Safety Starts at the Top Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1268
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-05-01T15:45:42Z
- Update date including text: 2025-05-01T15:45:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1268",
    "number": "1268",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Safety Starts at the Top Act of 2025",
    "type": "S",
    "updateDate": "2025-05-01T15:45:42Z",
    "updateDateIncludingText": "2025-05-01T15:45:42Z"
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
          "date": "2025-04-02T22:14:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1268is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1268\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Markey introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49 of the United States Code, to revise the qualifications for organization designation authorization holders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safety Starts at the Top Act of 2025 .\n#### 2. Qualifications for ODA holders\n##### (a) In general\nSection 44736(c)(2) of title 49, United States Code, is amended to read as follows:\n(2) ODA holder The term ODA holder means an entity that\u2014 (A) is authorized to perform functions pursuant to a delegation made by the Administrator of the FAA under section 44702(d); and (B) in the case of an entity with at least $15,000,000,000 in annual gross revenue, certifies to the Administrator, on an annual basis, that the board of directors of such entity includes\u2014 (i) two representatives from labor organizations, including 1 representative from each labor organization that represents the employees of such entity that are directly involved in the design and manufacturing of aircraft; and (ii) two representatives with proven experience in aerospace safety and demonstrable outcomes related to such experience. .\n##### (b) Review of existing ODA holders\nNot later than 90 days after the date of enactment of this section, the Administrator of the Federal Aviation Administration shall rescind any delegation made under section 44702(d) of title 49, United States Code, to an entity that does not meet the requirements under paragraph (2) of such section 44736(c)(2), as amended by subsection (a).",
      "versionDate": "2025-04-02",
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
        "updateDate": "2025-05-01T15:45:42Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1268is.xml"
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
      "title": "Safety Starts at the Top Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safety Starts at the Top Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49 of the United States Code, to revise the qualifications for organization designation authorization holders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:07Z"
    }
  ]
}
```
