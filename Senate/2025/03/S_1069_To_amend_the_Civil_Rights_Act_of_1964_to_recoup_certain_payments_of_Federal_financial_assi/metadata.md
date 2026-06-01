# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1069?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1069
- Title: RECLAIM Act
- Congress: 119
- Bill type: S
- Bill number: 1069
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1069",
    "number": "1069",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "RECLAIM Act",
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
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T23:22:38Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1069is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1069\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Civil Rights Act of 1964 to recoup certain payments of Federal financial assistance.\n#### 1. Short title\nThis Act may be cited as the Recouping Educational Contributions Linked to Antisemitic Institutional Misconduct Act or the RECLAIM Act .\n#### 2. Effect on entire program of termination of or refusal to grant or to continue assistance\nSection 602 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20131 ) is amended, in paragraph (1) of the third sentence, by striking shall be limited in its effect to the particular program, or part thereof, in which such noncompliance has been so found, and inserting shall apply to the entire program or activity in which such noncompliance has been so found, .\n#### 3. Recouping certain payments of Federal financial assistance\nSection 602 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20131 ) is amended, in the third sentence\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (3); and\n**(2)**\nby inserting after found, the following: (2) by requiring a recipient to repay the amount of any Federal financial assistance provided to the recipient for a program or activity for a fiscal year during which the recipient is found (in accordance with the procedures described in paragraph (1)) to be in such noncompliance concerning the program or activity (without regard to whether the Federal financial assistance has been expended), which shall be collected as a claim of the United States Government in accordance with chapter 37 of title 31, United States Code, .\n#### 4. Limit on Federal financial assistance after certain injunctions\nSection 603 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20132 ) is amended\u2014\n**(1)**\nin the first sentence, by striking Any and inserting (a) Any ; and\n**(2)**\nby adding at the end the following:\n(b) If a court issues an injunction in a case, for a claim in which a recipient of Federal financial assistance for a program or activity is alleged to be in violation of this title\u2014 (1) the Federal department or agency empowered to extend the Federal financial assistance shall not provide any Federal financial assistance to the recipient until the earlier of\u2014 (A) the date on which the court certifies that the recipient is in compliance with the injunction; or (B) the date that is 1 year after the date of issuance of the injunction; (2) the Federal department or agency shall notify the other Federal departments and agencies covered by this title of the injunction; and (3) those Federal departments and agencies shall not provide any Federal financial assistance to the recipient until the earlier of the dates specified in paragraph (1). .",
      "versionDate": "2025-03-13",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-04-01T17:14:05Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1069is.xml"
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
      "title": "RECLAIM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:09:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RECLAIM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:09:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recouping Educational Contributions Linked to Antisemitic Institutional Misconduct Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:09:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Civil Rights Act of 1964 to recoup certain payments of Federal financial assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:08:20Z"
    }
  ]
}
```
