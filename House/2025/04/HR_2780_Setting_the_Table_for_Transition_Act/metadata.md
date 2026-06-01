# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2780
- Title: Setting the Table for Transition Act
- Congress: 119
- Bill type: HR
- Bill number: 2780
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-05-06T20:38:53Z
- Update date including text: 2025-05-06T20:38:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2780",
    "number": "2780",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Setting the Table for Transition Act",
    "type": "HR",
    "updateDate": "2025-05-06T20:38:53Z",
    "updateDateIncludingText": "2025-05-06T20:38:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2780ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2780\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Kennedy of New York introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo temporarily expand the supplemental nutrition assistance program income eligibility of households that include certain veterans.\n#### 1. Short title\nThis Act may be cited as the Setting the Table for Transition Act .\n#### 2. Temporary expanded SNAP income eligibility of households that include certain veterans\nFor the purpose of determining income under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) during the 100-day period that begins on the date a veteran receives a Report of Separation (DD form 214) of a household that includes a member who is a veteran, only the income of such veteran shall be considered.\n#### 3. Definition\nFor purposes of this Act, the term veteran means an individual who served in the active military, naval, or air service, and who was discharged or released therefrom under conditions other than dishonorable.\n#### 4. Effective date\nThis Act shall take effect 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-09",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T20:38:53Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2780ih.xml"
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
      "title": "Setting the Table for Transition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Setting the Table for Transition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To temporarily expand the supplemental nutrition assistance program income eligibility of households that include certain veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T04:03:29Z"
    }
  ]
}
```
