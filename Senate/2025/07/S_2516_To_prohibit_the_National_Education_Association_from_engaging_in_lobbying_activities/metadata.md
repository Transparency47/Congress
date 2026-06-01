# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2516?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2516
- Title: TEACH Act
- Congress: 119
- Bill type: S
- Bill number: 2516
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-09-12T20:46:25Z
- Update date including text: 2025-09-12T20:46:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2516",
    "number": "2516",
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
    "title": "TEACH Act",
    "type": "S",
    "updateDate": "2025-09-12T20:46:25Z",
    "updateDateIncludingText": "2025-09-12T20:46:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:26:02Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2516is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2516\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the National Education Association from engaging in lobbying activities.\n#### 1. Short title\nThis Act may be cited as the Terminating Education Association Congressional Handouts Act or the TEACH Act .\n#### 2. Prohibition on NEA lobbying\n##### (a) In General\nChapter 1511 of title 36, United States Code, is amended by adding at the end the following new section:\n151109. Prohibition on lobbying (a) In General The corporation shall not engage in lobbying activities (as defined in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 )). (b) Annual certification; maintenance of records The corporation shall submit an annual certification to the Secretary of Education containing an assurance that the corporation has not engaged in any such lobbying activities. The corporation shall maintain such records as the Secretary of Education may require to facilitate an effective audit of the certification. (c) Penalty The penalty for a violation of the prohibition under subsection (a) shall be termination of the status of the corporation as a federally chartered corporation. .\n##### (b) Clerical amendment\nThe table of sections for chapter 1511 of title 36, United States Code, is amended by adding after the item relating to section 151108 the following:\n151109. Prohibition on lobbying. .",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-12T20:46:25Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2516is.xml"
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
      "title": "TEACH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TEACH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Terminating Education Association Congressional Handouts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the National Education Association from engaging in lobbying activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:27Z"
    }
  ]
}
```
