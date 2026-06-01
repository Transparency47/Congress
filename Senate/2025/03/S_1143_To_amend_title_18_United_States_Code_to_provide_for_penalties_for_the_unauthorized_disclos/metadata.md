# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1143
- Title: Stop Supreme Court Leakers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1143
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1143",
    "number": "1143",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Stop Supreme Court Leakers Act of 2025",
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
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T16:35:21Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1143is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1143\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Cassidy (for himself, Mrs. Hyde-Smith , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide for penalties for the unauthorized disclosure of confidential information by officers or employees of the Supreme Court, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Supreme Court Leakers Act of 2025 .\n#### 2. Obstruction of Supreme Court deliberations\n##### (a) In general\nChapter 73 of title 18, United States Code, is amended by adding at the end the following new section:\n1522. Obstruction of Supreme Court deliberations (a) Definition In this section, the term confidential information includes\u2014 (1) internal notes taken by an employee of the Supreme Court of the United States on cases heard by the Supreme Court; (2) any communication between the Chief Justice of the United States or an associate justice of the Supreme Court of the United States and an employee or officer of the Supreme Court; (3) a communication between officers and employees of the Supreme Court of the United States on a matter pending before the Supreme Court; (4) a draft opinion or a final opinion prior to the date on which such opinion is released to the public; (5) personal information of the Chief Justice of the United States or an associate justice of the Supreme Court of the United States that is not otherwise legally available to the public; and (6) any other information designated to be confidential by the Chief Justice of the United States prior to the date on which a violation of subsection (b) occurs. (b) Prohibition It shall be unlawful for any person, while serving as an officer or employee of the Supreme Court, to knowingly publish, divulge, disclose, or make known in any manner or to any extent not authorized by law any confidential information coming to that officer or employee in the course of the employment or official duties of that officer or employee. (c) Criminal penalties (1) In general Except as provided in paragraph (2), any individual who violates, or conspires to violate, subsection (b) shall be imprisoned not more than 10 years and fined under this title. (2) Internal notes Any individual who violates, or conspires to violate, subsection (a) with confidential information described in subsection (a)(1) shall be fined $10,000. .\n##### (b) Criminal forfeiture\nSection 982(a)(2)(B) of title 18, United States Code, is amended by striking 1029, or 1030 and inserting 1029, 1030, or 1522 .\n##### (c) Table of contents\nThe table of sections for chapter 73 of title 18, United States Code, is amended by adding at the end the following:\n1522. Obstruction of Supreme Court deliberations. .",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-04-11T13:02:46Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1143is.xml"
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
      "title": "Stop Supreme Court Leakers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Supreme Court Leakers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to provide for penalties for the unauthorized disclosure of confidential information by officers or employees of the Supreme Court, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:34Z"
    }
  ]
}
```
