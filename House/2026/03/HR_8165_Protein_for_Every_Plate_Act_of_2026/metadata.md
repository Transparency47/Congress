# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8165
- Title: Protein for Every Plate Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8165
- Origin chamber: House
- Introduced date: 2026-03-30
- Update date: 2026-04-13T20:53:33Z
- Update date including text: 2026-04-13T20:53:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-30: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-30: Introduced in House

## Actions

- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-30",
    "latestAction": {
      "actionDate": "2026-03-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8165",
    "number": "8165",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Protein for Every Plate Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-13T20:53:33Z",
    "updateDateIncludingText": "2026-04-13T20:53:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-30",
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
      "actionDate": "2026-03-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-30",
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
          "date": "2026-03-30T16:00:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8165ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8165\nIN THE HOUSE OF REPRESENTATIVES\nMarch 30, 2026 Mr. Pappas introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to increase the purchase of animal protein for fiscal years 2026 and 2027 to be included in food assistance distributed under the Emergency Food Assistance Act of 1983.\n#### 1. Short title\nThis Act may be cited as the Protein for Every Plate Act of 2026 .\n#### 2. Amendments\nSection 27(a)(2) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2036(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (D) by striking and at the end,\n**(2)**\nin subparagraph (E) and inserting the period at the end and inserting ; and , and\n**(3)**\nby adding at the end the following:\n(F) for each of the fiscal years 2026 and 2027, the sum obtained by adding the total dollar amount of commodities specified in subparagraph (E) for such fiscal year and $200,000,000 for the purchase of animal protein. .",
      "versionDate": "2026-03-30",
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
        "updateDate": "2026-04-13T20:53:32Z"
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
      "date": "2026-03-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8165ih.xml"
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
      "title": "Protein for Every Plate Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protein for Every Plate Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to increase the purchase of animal protein for fiscal years 2026 and 2027 to be included in food assistance distributed under the Emergency Food Assistance Act of 1983.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:42Z"
    }
  ]
}
```
