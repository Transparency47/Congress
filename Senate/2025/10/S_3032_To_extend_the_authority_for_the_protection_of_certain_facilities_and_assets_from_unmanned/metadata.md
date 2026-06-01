# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3032
- Title: Counter-UAS Authority Extension Act
- Congress: 119
- Bill type: S
- Bill number: 3032
- Origin chamber: Senate
- Introduced date: 2025-10-22
- Update date: 2025-12-08T15:09:32Z
- Update date including text: 2025-12-08T15:09:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-22: Introduced in Senate
- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time. (Legislative Day October 21, 2025).
- 2025-10-22 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 206.
- Latest action: 2025-10-22: Introduced in Senate

## Actions

- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time. (Legislative Day October 21, 2025).
- 2025-10-22 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 206.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-22",
    "latestAction": {
      "actionDate": "2025-10-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3032",
    "number": "3032",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Counter-UAS Authority Extension Act",
    "type": "S",
    "updateDate": "2025-12-08T15:09:32Z",
    "updateDateIncludingText": "2025-12-08T15:09:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 206.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time. (Legislative Day October 21, 2025).",
      "type": "Calendars"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-22",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "IA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3032pcs.xml",
      "text": "II\nCalendar No. 206\n119th CONGRESS\n1st Session\nS. 3032\nIN THE SENATE OF THE UNITED STATES\nOctober 22 (legislative day, October 21), 2025 Mr. Peters (for himself and Ms. Ernst ) introduced the following bill; which was read the first time\nOctober 22, 2025 Read the second time and placed on the calendar\nA BILL\nTo extend the authority for the protection of certain facilities and assets from unmanned aircraft.\n#### 1. Short title\nThis Act may be cited as the Counter-UAS Authority Extension Act .\n#### 2. Extension of Counter-UAS authorities of the Department of Homeland Security and the Department of Justice\nSection 210G(i) of the Homeland Security Act of 2002 ( 6 U.S.C. 124n(i) ) is amended by striking September 30, 2025 and inserting September 30, 2028 .",
      "versionDate": "2025-10-22",
      "versionType": "Placed on Calendar Senate"
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
        "updateDate": "2025-12-08T15:09:32Z"
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
      "date": "2025-10-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3032pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Counter-UAS Authority Extension Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:15Z"
    },
    {
      "title": "A bill to extend the authority for the protection of certain facilities and assets from unmanned aircraft.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T10:56:20Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Counter-UAS Authority Extension Act",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2025-10-24T02:23:14Z"
    }
  ]
}
```
