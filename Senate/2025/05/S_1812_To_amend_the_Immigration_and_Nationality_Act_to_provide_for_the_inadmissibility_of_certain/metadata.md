# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1812
- Title: Ban Birth Tourism Act
- Congress: 119
- Bill type: S
- Bill number: 1812
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1812",
    "number": "1812",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Ban Birth Tourism Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T18:28:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1812is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1812\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide for the inadmissibility of certain aliens seeking citizenship for children by giving birth in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ban Birth Tourism Act .\n#### 2. Inadmissibility of aliens seeking citizenship for children by giving birth in the United States\nSection 212(a)(10) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(10) ) is amended by adding at the end the following:\n(F) Aliens seeking citizenship for children by giving birth in the United States (i) In general Any alien seeking admission to the United States as a nonimmigrant under section 101(a)(15)(B) for the primary purpose of obtaining United States citizenship for a child by giving birth to such child in the United States is inadmissible. (ii) Rule of construction Nothing in this subparagraph may be construed to render inadmissible an alien seeking legitimate medical treatment relating to childbirth if obtaining citizenship for the child is not the primary purpose for seeking admission. .",
      "versionDate": "2025-05-20",
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
        "name": "Immigration",
        "updateDate": "2025-05-30T13:52:24Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1812is.xml"
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
      "title": "Ban Birth Tourism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ban Birth Tourism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to provide for the inadmissibility of certain aliens seeking citizenship for children by giving birth in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:30Z"
    }
  ]
}
```
