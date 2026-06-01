# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/384
- Title: A resolution authorizing the Majority Leader to move to proceed to the en bloc consideration of certain nominations.
- Congress: 119
- Bill type: SRES
- Bill number: 384
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-30T13:10:10Z
- Update date including text: 2025-09-30T13:10:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S6578)
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S6578)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/384",
    "number": "384",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution authorizing the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
    "type": "SRES",
    "updateDate": "2025-09-30T13:10:10Z",
    "updateDateIncludingText": "2025-09-30T13:10:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S6578)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T20:23:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres384is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 384\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Lankford submitted the following resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nAuthorizing the Majority Leader to move to proceed to the en bloc consideration of certain nominations.\n#### 1. En bloc consideration of certain nominations\n##### (a) Definition\nIn this section, the term covered nomination means a nomination to a position that is not a position\u2014\n**(1)**\nat level I of the Executive Schedule under section 5312 of title 5, United States Code;\n**(2)**\nas a judge of a district court of the United States;\n**(3)**\nas a judge of a court of appeals of the United States; or\n**(4)**\nas Chief Justice of the United States or as an Associate Justice of the Supreme Court of the United States.\n##### (b) Authorization\nIt shall be in order for the Majority Leader to move to proceed to the en bloc consideration of not more than 15 covered nominations that were reported to the Senate by the same committee of the Senate and placed on the calendar.\n##### (c) Consideration\nConsideration of a motion to proceed under subsection (b), and the en bloc consideration of the nominations that are the subject of the motion, shall be conducted in the same manner as if it were a motion to proceed to the consideration of a single nomination.",
      "versionDate": "2025-09-11",
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
        "name": "Congress",
        "updateDate": "2025-09-30T13:10:09Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres384is.xml"
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
      "title": "A resolution authorizing the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-13T02:18:23Z"
    },
    {
      "title": "A resolution authorizing the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T10:56:28Z"
    }
  ]
}
```
