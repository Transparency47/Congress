# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7782
- Title: American Passport Card Accessibility Act
- Congress: 119
- Bill type: HR
- Bill number: 7782
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-26T19:35:55Z
- Update date including text: 2026-03-26T19:35:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7782",
    "number": "7782",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "American Passport Card Accessibility Act",
    "type": "HR",
    "updateDate": "2026-03-26T19:35:55Z",
    "updateDateIncludingText": "2026-03-26T19:35:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7782ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7782\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Underwood introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the Secretary of State from charging a fee for the issuance or reissuance of a passport card.\n#### 1. Short title\nThis Act may be cited as the American Passport Card Accessibility Act .\n#### 2. Prohibition on fees for passport cards\n##### (a) Prohibition\nNotwithstanding section 1 of the Act of June 1, 1920 ( 22 U.S.C. 214 ; commonly referred to as the Passport Act of 1920 ), the Secretary of State may not charge a fee for the issuance or reissuance of a passport card.\n##### (b) Expedited processing fees excepted\nThe prohibition in subsection (a) shall not apply to a fee assessed for the expedited processing of an application for issuance or reissuance of a passport card.",
      "versionDate": "2026-03-04",
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
        "name": "Immigration",
        "updateDate": "2026-03-26T19:35:55Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7782ih.xml"
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
      "title": "American Passport Card Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T07:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Passport Card Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T07:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of State from charging a fee for the issuance or reissuance of a passport card.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T07:18:23Z"
    }
  ]
}
```
