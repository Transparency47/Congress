# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3016?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3016
- Title: Combatting Hospital Monopolies Act
- Congress: 119
- Bill type: HR
- Bill number: 3016
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-05-28T16:05:20Z
- Update date including text: 2025-05-28T16:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3016",
    "number": "3016",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S000929",
        "district": "5",
        "firstName": "Victoria",
        "fullName": "Rep. Spartz, Victoria [R-IN-5]",
        "lastName": "Spartz",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Combatting Hospital Monopolies Act",
    "type": "HR",
    "updateDate": "2025-05-28T16:05:20Z",
    "updateDateIncludingText": "2025-05-28T16:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3016ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3016\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mrs. Spartz introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo give the Federal Trade Commission authority over certain tax-exempt organizations.\n#### 1. Short title\nThis Act may be cited as the Combatting Hospital Monopolies Act .\n#### 2. Authority of Federal Trade Commission Over Certain Tax-Exempt Organizations\nSection 4 of the Federal Trade Commission Act ( 15 U.S.C. 44 ) is amended, in the undesignated paragraph relating to the definition of the term Corporation \u2014\n**(1)**\nby striking , and any and inserting , any ; and\n**(2)**\nby inserting before the period at the end the following: , and any hospital organization or cooperative hospital service organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code .",
      "versionDate": "2025-04-24",
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
        "name": "Commerce",
        "updateDate": "2025-05-28T16:05:20Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3016ih.xml"
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
      "title": "Combatting Hospital Monopolies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combatting Hospital Monopolies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To give the Federal Trade Commission authority over certain tax-exempt organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:31Z"
    }
  ]
}
```
