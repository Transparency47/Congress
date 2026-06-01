# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8715?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8715
- Title: Make DTE Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 8715
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-27T13:22:35Z
- Update date including text: 2026-05-27T13:22:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8715",
    "number": "8715",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Make DTE Pay Act",
    "type": "HR",
    "updateDate": "2026-05-27T13:22:35Z",
    "updateDateIncludingText": "2026-05-27T13:22:35Z"
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
          "date": "2026-05-07T13:01:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8715ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8715\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Ms. Tlaib introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to provide for the enhancement of a penalty for an investor-owned electric or gas utility that increases rates within the 2-year period occurring before or after the assessment of the penalty.\n#### 1. Short title\nThis Act may be cited as the Make DTE Pay Act .\n#### 2. Clean Air Act penalty enhancement\nSection 120(b) of the Clean Air Act ( 42 U.S.C. 7420(b) ) is amended\u2014\n**(1)**\nin paragraph (8), by striking and after the semicolon;\n**(2)**\nin paragraph (9), by striking (d)(4). and inserting (d)(4); and ; and\n**(3)**\nby adding after paragraph (9) the following:\n(10) notwithstanding any other provision of this section, require the State or the Administrator to, with respect to a noncomplying stationary source that is owned or operated by an investor-owned electric utility or gas utility, adjust the amount of the penalty assessed, by increasing the penalty by an amount that is equal to the amount of the original assessment, for each rate increase that the utility\u2014 (A) received in the 2-year period preceding the original assessment of the penalty; and (B) seeks in the 2-year period following the original assessment (regardless of whether such rate increase is approved or is pending before a regulatory authority). .",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-27T13:22:35Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8715ih.xml"
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
      "title": "To amend the Clean Air Act to provide for the enhancement of a penalty for an investor-owned electric or gas utility that increases rates within the 2-year period occurring before or after the assessment of the penalty.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T08:08:22Z"
    },
    {
      "title": "Make DTE Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T07:54:49Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make DTE Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T07:54:48Z"
    }
  ]
}
```
