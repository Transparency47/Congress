# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6074
- Title: To amend the Internal Revenue Code of 1986 to extend the enhancement of the health care premium tax credit.
- Congress: 119
- Bill type: HR
- Bill number: 6074
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-19T03:26:13Z
- Update date including text: 2025-12-19T03:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6074",
    "number": "6074",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
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
    "title": "To amend the Internal Revenue Code of 1986 to extend the enhancement of the health care premium tax credit.",
    "type": "HR",
    "updateDate": "2025-12-19T03:26:13Z",
    "updateDateIncludingText": "2025-12-19T03:26:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6074ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6074\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Underwood introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the enhancement of the health care premium tax credit.\n#### 1. Extension of enhancement of health care premium tax credit\n##### (a) Extension of rules To increase premium assistance amounts\nClause (iii) of section 36B(b)(3)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by striking through 2025 and inserting through 2028 , and\n**(2)**\nin the matter preceding subclause (I), by striking before January 1, 2026 and inserting before January 1, 2029 .\n##### (b) Extension of rule To allow credit to taxpayers whose household income exceeds 400 percent of poverty line\nSubparagraph (E) of section 36B(c)(1) of such Code is amended\u2014\n**(1)**\nin the heading, by striking through 2025 and inserting through 2028 , and\n**(2)**\nby striking before January 1, 2026 and inserting before January 1, 2029 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-11-18",
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
        "name": "Taxation",
        "updateDate": "2025-12-02T20:04:06Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6074ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the enhancement of the health care premium tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:38Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to extend the enhancement of the health care premium tax credit.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T09:07:17Z"
    }
  ]
}
```
