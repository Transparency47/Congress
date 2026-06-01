# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/923?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/923
- Title: Harriet Tubman Tribute Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 923
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2025-03-28T12:50:33Z
- Update date including text: 2025-03-28T12:50:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/923",
    "number": "923",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Harriet Tubman Tribute Act of 2025",
    "type": "S",
    "updateDate": "2025-03-28T12:50:33Z",
    "updateDateIncludingText": "2025-03-28T12:50:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T22:40:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s923is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 923\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mrs. Shaheen introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of the Treasury to redesign $20 Federal reserve notes so as to include a likeness of Harriet Tubman, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Harriet Tubman Tribute Act of 2025 .\n#### 2. Likeness of Harriet Tubman required to be included on the face of $20 Federal reserve notes\nThe eighth undesignated paragraph of section 16 of the Federal Reserve Act ( 12 U.S.C. 418 ) is amended by adding at the end the following new sentence: The Secretary of the Treasury shall ensure that the face of all $20 Federal reserve notes printed after December 31, 2030, shall bear the likeness of Harriet Tubman, except that the Secretary may delay such date by not more than 2 years if the Secretary submits to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a determination, after consultation with the Director of the Bureau of Engraving and Printing, the Board, and the Director of the United States Secret Service, that issuing such notes after December 31, 2030, would create an unacceptable risk of counterfeiting or to the safe, secure, and speedy functioning of the United States economy. .",
      "versionDate": "2025-03-10",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-28T12:50:33Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s923is.xml"
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
      "title": "Harriet Tubman Tribute Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Harriet Tubman Tribute Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Treasury to redesign $20 Federal reserve notes so as to include a likeness of Harriet Tubman, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:41Z"
    }
  ]
}
```
