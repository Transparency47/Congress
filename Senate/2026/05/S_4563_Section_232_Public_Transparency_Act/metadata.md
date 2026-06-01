# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4563?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4563
- Title: Section 232 Public Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 4563
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-29T07:23:31Z
- Update date including text: 2026-05-29T07:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4563",
    "number": "4563",
    "originChamber": "Senate",
    "policyArea": {},
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
    "title": "Section 232 Public Transparency Act",
    "type": "S",
    "updateDate": "2026-05-29T07:23:31Z",
    "updateDateIncludingText": "2026-05-29T07:23:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T15:05:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4563is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4563\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2026 Mr. Peters (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Trade Expansion Act of 1962 to require a deadline for publication of information contained in reports on findings of investigations relating to imports that impair national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Section 232 Public Transparency Act .\n#### 2. Deadline for publication of information contained in reports on investigations relating to imports that impair national security\nSubparagraph (B) of section 232(b)(3) of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862(b)(3) ) is amended to read as follows:\n(B) Not later than 270 days after the date on which an investigation is initiated under paragraph (1), or not later than the date on which the report is submitted to the President under subparagraph (A) with respect to that investigation, whichever is earlier, the Secretary shall publish in the Federal Register any portion of that report that does not contain classified information or proprietary information. .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4563is.xml"
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
      "title": "Section 232 Public Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Section 232 Public Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Trade Expansion Act of 1962 to require a deadline for publication of information contained in reports on findings of investigations relating to imports that impair national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:36Z"
    }
  ]
}
```
