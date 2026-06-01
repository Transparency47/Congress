# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7888?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7888
- Title: Closing the Enhanced Prudential Standards Loophole Act
- Congress: 119
- Bill type: HR
- Bill number: 7888
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-03T21:07:44Z
- Update date including text: 2026-04-03T21:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7888",
    "number": "7888",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Closing the Enhanced Prudential Standards Loophole Act",
    "type": "HR",
    "updateDate": "2026-04-03T21:07:44Z",
    "updateDateIncludingText": "2026-04-03T21:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7888ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7888\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Ms. Waters introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Financial Stability Act of 2010 to apply the enhanced supervision and prudential standards applicable under such Act with respect to bank holding companies to large banks that do not have a bank holding company, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Closing the Enhanced Prudential Standards Loophole Act .\n#### 2. Enhanced supervision and prudential standards for banks with no bank holding company\nSection 165 of the Financial Stability Act of 2010 ( 12 U.S.C. 5365 ) is amended by adding at the end the following:\n(l) Application to banks with no bank holding company The provisions of this section shall apply to a bank that does not have a bank holding company to the same extent as such provisions apply to a bank holding company with the same amount of total consolidated assets as the bank. .",
      "versionDate": "2026-03-09",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-03T21:07:43Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7888ih.xml"
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
      "title": "Closing the Enhanced Prudential Standards Loophole Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Closing the Enhanced Prudential Standards Loophole Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Financial Stability Act of 2010 to apply the enhanced supervision and prudential standards applicable under such Act with respect to bank holding companies to large banks that do not have a bank holding company, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:34Z"
    }
  ]
}
```
