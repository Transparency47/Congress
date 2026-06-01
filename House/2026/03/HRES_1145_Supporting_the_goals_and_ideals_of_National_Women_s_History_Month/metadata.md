# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1145
- Title: Supporting the goals and ideals of National Women's History Month.
- Congress: 119
- Bill type: HRES
- Bill number: 1145
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-02T18:53:47Z
- Update date including text: 2026-04-02T18:53:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House
- Latest action: 2026-03-27: Submitted in House

## Actions

- 2026-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1145",
    "number": "1145",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Supporting the goals and ideals of National Women's History Month.",
    "type": "HRES",
    "updateDate": "2026-04-02T18:53:47Z",
    "updateDateIncludingText": "2026-04-02T18:53:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:33:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1145ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1145\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Thompson of California submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the goals and ideals of National Women\u2019s History Month.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of National Women\u2019s History Month; and\n**(2)**\nrecognizes and honors the women and organizations in the United States that have fought for, and continue to promote, the teaching of women\u2019s history and the women\u2019s suffrage movement.",
      "versionDate": "2026-03-27",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-31",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "280",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the goals and ideals of National Women's History Month.",
      "type": "HRES"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-04-02T18:53:47Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1145ih.xml"
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
      "title": "Supporting the goals and ideals of National Women's History Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:26Z"
    },
    {
      "title": "Supporting the goals and ideals of National Women's History Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T08:06:25Z"
    }
  ]
}
```
