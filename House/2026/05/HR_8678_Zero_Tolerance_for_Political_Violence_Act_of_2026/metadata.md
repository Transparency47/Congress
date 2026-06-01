# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8678
- Title: Zero Tolerance for Political Violence Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8678
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-20T20:05:51Z
- Update date including text: 2026-05-20T20:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8678",
    "number": "8678",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Zero Tolerance for Political Violence Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T20:05:51Z",
    "updateDateIncludingText": "2026-05-20T20:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-05-07T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8678ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8678\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Carter of Georgia introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to include mandatory minimum sentences for the attempted assassination of a Member of Congress, a member of the Cabinet, a justice of the Supreme Court, the President, the Vice President, or certain presidential staff, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Zero Tolerance for Political Violence Act of 2026 .\n#### 2. Mandatory minimum sentences for assassination attempts of certain Federal officials\n##### (a) Congressional, Cabinet, and Supreme Court assassination attempts\nSection 351(c) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever attempts and inserting (1) Whoever attempts ;\n**(2)**\nby striking kill or ; and\n**(3)**\nby adding at the end the following:\n(2) Whoever attempts to kill any individual designated in subsection (a) of this section shall be punished by imprisonment for any term of years not less than 25, or for life. .\n##### (b) Presidential and Presidential staff assassination attempts\nSection 1751(c) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever attempts and inserting (1) Whoever attempts ;\n**(2)**\nby striking kill or ; and\n**(3)**\nby adding at the end the following:\n(2) Whoever attempts to kill any individual designated in subsection (a) of this section shall be punished by imprisonment for any term of years not less than 25, or for life. .",
      "versionDate": "2026-05-07",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-05-20T20:05:51Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8678ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Zero Tolerance for Political Violence Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Zero Tolerance for Political Violence Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to include mandatory minimum sentences for the attempted assassination of a Member of Congress, a member of the Cabinet, a justice of the Supreme Court, the President, the Vice President, or certain presidential staff, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:35Z"
    }
  ]
}
```
