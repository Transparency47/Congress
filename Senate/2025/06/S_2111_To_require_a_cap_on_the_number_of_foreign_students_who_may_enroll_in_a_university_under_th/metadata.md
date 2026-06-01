# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2111
- Title: American Students First Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2111
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2111",
    "number": "2111",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "American Students First Act of 2025",
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
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T16:35:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2111is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2111\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require a cap on the number of foreign students who may enroll in a university under the Student and Exchange Visitor Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Students First Act of 2025 .\n#### 2. Limitation on number of foreign students enrolled at United States universities\n##### (a) In general\nEach certificate issued to a university by the Director of U.S. Immigration and Customs Enforcement under the Student and Exchange Visitor Program shall limit the number of nonimmigrant students described in subparagraphs (F) and (M) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) who may enroll in the university to 10 percent of the student population of the university in an academic year.\n##### (b) Waiver\n**(1) In general**\nThe President or the Secretary of Homeland Security may waive the 10 percent cap under subsection (a) for national security purposes or if such a waiver is in the interests of the United States\n**(2) Limitation**\nIn the case of a waiver under paragraph (1), a university certified to participate in the Student and Exchange Visitor Program may enroll a number of nonimmigrant students described in subparagraphs (F) and (M) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) that is not more than 15 percent of the student population of the university in an academic year.",
      "versionDate": "2025-06-18",
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
        "updateDate": "2025-07-14T14:32:14Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2111is.xml"
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
      "title": "American Students First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Students First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a cap on the number of foreign students who may enroll in a university under the Student and Exchange Visitor Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:01Z"
    }
  ]
}
```
