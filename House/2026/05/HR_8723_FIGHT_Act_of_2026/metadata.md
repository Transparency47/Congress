# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8723?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8723
- Title: FIGHT Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8723
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-27T14:36:11Z
- Update date including text: 2026-05-27T14:36:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8723",
    "number": "8723",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "FIGHT Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-27T14:36:11Z",
    "updateDateIncludingText": "2026-05-27T14:36:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
          "date": "2026-05-11T14:30:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8723ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8723\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Bacon introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Welfare Act to prohibit gambling on animal fighting ventures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Inhumane Gambling and High-risk Trafficking Act of 2026 or the FIGHT Act of 2026 .\n#### 2. Animal fighting\nSection 26 of the Animal Welfare Act ( 7 U.S.C. 2156 ) is amended\u2014\n**(1)**\nby striking the section designation and header and all that follows through It shall be unlawful in subsection (a)(2) and inserting the following:\n26. Sponsoring or exhibiting an animal in, attending, causing an individual who has not attained the age of 16 to attend, or gambling on, an animal fighting venture (a) Sponsoring or exhibiting (1) In general It shall be unlawful for any person to knowingly sponsor or exhibit an animal in an animal fighting venture. (2) Attending or causing an individual who has not attained the age of 16 to attend It shall be unlawful ; and\n**(2)**\nin subsection (a), by adding at the end the following:\n(3) Animal venture gambling It shall be unlawful for any person to gamble on an animal fighting venture, including an in-person or broadcast event. .",
      "versionDate": "2026-05-11",
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
        "updateDate": "2026-05-27T14:36:11Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8723ih.xml"
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
      "title": "FIGHT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T07:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIGHT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T07:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fighting Inhumane Gambling and High-risk Trafficking Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T07:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Welfare Act to prohibit gambling on animal fighting ventures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T07:33:27Z"
    }
  ]
}
```
