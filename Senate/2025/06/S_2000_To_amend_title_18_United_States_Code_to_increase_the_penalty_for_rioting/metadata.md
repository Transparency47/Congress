# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2000
- Title: Mitigating Extreme Lawlessness and Threats Act
- Congress: 119
- Bill type: S
- Bill number: 2000
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2000",
    "number": "2000",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Mitigating Extreme Lawlessness and Threats Act",
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
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T15:11:57Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2000is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2000\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to increase the penalty for rioting.\n#### 1. Short title\nThis Act may be cited as the Mitigating Extreme Lawlessness and Threats Act .\n#### 2. Riots\nSection 2101 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the flush text following paragraph (4), by striking subparagraph (A), (B), (C), or (D) and all that follows and inserting paragraph (1), (2), (3), or (4) of this subsection, shall be punished as provided in subsection (b). ;\n**(2)**\nby redesignating subsections (b) through (f) as subsections (c) through (g), respectively;\n**(3)**\nby inserting after subsection (a) the following:\n(b) The punishment for a violation of subsection (a) shall be\u2014 (1) a fine under this title, or a term of imprisonment of not more than ten years, or both; (2) if the defendant, in carrying out an activity described in subsection (a), committed an act of violence or aided or abetted any other person in committing an act of violence, a fine under this title, a term of imprisonment of not less than one year and not more than ten years, or both; or (3) if the defendant, in carrying out an activity described in subsection (a), assaulted a Federal law enforcement officer or member of the uniformed service, a fine under this title, or a term of imprisonment for any term of years, but not less than one year, or for life, or both. ; and\n**(4)**\nin subsection (c), as so redesignated, by striking subparagraph (A), (B), (C), or (D) of paragraph (1) of subsection (a) and inserting paragraph (1), (2), (3), or (4) of subsection (a) .",
      "versionDate": "2025-06-10",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-01T13:27:54Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2000is.xml"
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
      "title": "Mitigating Extreme Lawlessness and Threats Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mitigating Extreme Lawlessness and Threats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to increase the penalty for rioting.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:20Z"
    }
  ]
}
```
