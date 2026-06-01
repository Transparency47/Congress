# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3118
- Title: Respect the Chief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3118
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-25T18:53:01Z
- Update date including text: 2025-11-25T18:53:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3118",
    "number": "3118",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Respect the Chief Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T18:53:01Z",
    "updateDateIncludingText": "2025-11-25T18:53:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T16:24:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3118is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3118\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require reporting on compliance with requirements to update leadership boards across the Department of Defense.\n#### 1. Short title\nThis Act may be cited as the Respect the Chief Act of 2025 .\n#### 2. Reporting on compliance with requirements to update leadership boards at military installations\n##### (a) Initial report\nNot later than January 31, 2026, the Secretary of Defense shall submit to the President and the congressional defense committees a report certifying compliance, during the preceding calendar year, with applicable requirements to update command and control leadership boards across the Department of Defense.\n##### (b) Subsequent reports\nNot later than 120 days after the inauguration of a new President or the confirmation of a new Secretary of Defense, the Secretary of Defense shall submit to the President and the congressional defense committees a report certifying that all command and control leadership boards across the Department of Defense have been updated to reflect the current Commander-in-Chief and other applicable leadership changes.\n##### (c) Congressional defense committees defined\nIn this section, the term congressional defense committees has the meaning given the term in section 101(a)(16) of title 10, United States Code.",
      "versionDate": "2025-11-06",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:53:01Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3118is.xml"
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
      "title": "Respect the Chief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T07:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respect the Chief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require reporting on compliance with requirements to update leadership boards across the Department of Defense.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:03:25Z"
    }
  ]
}
```
