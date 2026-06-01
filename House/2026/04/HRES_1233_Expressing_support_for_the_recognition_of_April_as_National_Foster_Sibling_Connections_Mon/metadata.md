# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1233
- Title: Expressing support for the recognition of April as National Foster Sibling Connections Month.
- Congress: 119
- Bill type: HRES
- Bill number: 1233
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-15T17:10:18Z
- Update date including text: 2026-05-15T17:10:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-04-29 - IntroReferral: Submitted in House
- Latest action: 2026-04-29: Submitted in House

## Actions

- 2026-04-29 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-04-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1233",
    "number": "1233",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Expressing support for the recognition of April as National Foster Sibling Connections Month.",
    "type": "HRES",
    "updateDate": "2026-05-15T17:10:18Z",
    "updateDateIncludingText": "2026-05-15T17:10:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
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
          "date": "2026-04-29T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1233ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1233\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Nunn of Iowa (for himself, Ms. Moore of Wisconsin , and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the recognition of April as National Foster Sibling Connections Month.\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the recognition of National Foster Sibling Connections Month;\n**(2)**\nacknowledges the critical importance of sibling relationships for children and youth in foster care;\n**(3)**\nencourages Federal, State, Tribal, and local agencies to prioritize policies and practices that promote sibling placement and lifelong connection;\n**(4)**\nsupports efforts to improve data collection and transparency regarding sibling relationships and separations in foster care; and\n**(5)**\ncalls upon policymakers, child welfare professionals, advocates, and the public to raise awareness of and address the needs of siblings impacted by foster care.",
      "versionDate": "2026-04-29",
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
        "name": "Families",
        "updateDate": "2026-05-15T17:10:18Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1233ih.xml"
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
      "title": "Expressing support for the recognition of April as National Foster Sibling Connections Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T09:48:54Z"
    },
    {
      "title": "Expressing support for the recognition of April as National Foster Sibling Connections Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T08:06:55Z"
    }
  ]
}
```
