# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1054
- Title: Honoring the lives of Minnesota State House Speaker Emerita Melissa Hortman and Mark Hortman.
- Congress: 119
- Bill type: HRES
- Bill number: 1054
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-18T16:28:18Z
- Update date including text: 2026-02-18T16:28:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House
- Latest action: 2026-02-10: Submitted in House

## Actions

- 2026-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1054",
    "number": "1054",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001234",
        "district": "3",
        "firstName": "Kelly",
        "fullName": "Rep. Morrison, Kelly [D-MN-3]",
        "lastName": "Morrison",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Honoring the lives of Minnesota State House Speaker Emerita Melissa Hortman and Mark Hortman.",
    "type": "HRES",
    "updateDate": "2026-02-18T16:28:18Z",
    "updateDateIncludingText": "2026-02-18T16:28:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-02-10T15:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1054ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1054\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Ms. Morrison submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nHonoring the lives of Minnesota State House Speaker Emerita Melissa Hortman and Mark Hortman.\nThat the House of Representatives\u2014\n**(1)**\nhonors the life of Speaker Emerita Melissa Hortman for her devotion and service to the people of Minnesota;\n**(2)**\nhonors the life of Mark Hortman for his devotion to his family and service to his community;\n**(3)**\nhonors the life of Gilbert Hortman for his devotion to Melissa, treats, and lying in the snow;\n**(4)**\nhonors the leadership of Speaker Emerita Melissa Hortman, who led with kindness and compassion, passion and pragmatism, and conviction and respect; and\n**(5)**\nhonors the legacy of Speaker Emerita Melissa Hortman for her exemplary record in working through political differences through civil discourse and a shared desire to make Minnesota and our country a better place for the next generation.",
      "versionDate": "2026-02-10",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2026-02-18T16:28:18Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1054ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Honoring the lives of Minnesota State House Speaker Emerita Melissa Hortman and Mark Hortman.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:33:50Z"
    },
    {
      "title": "Honoring the lives of Minnesota State House Speaker Emerita Melissa Hortman and Mark Hortman.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:21Z"
    }
  ]
}
```
