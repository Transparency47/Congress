# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1103
- Title: Expressing support for the designation of the week beginning March 2, 2026, as "School Social Work Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1103
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-05-29T19:21:51Z
- Update date including text: 2026-05-29T19:21:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House
- Latest action: 2026-03-04: Submitted in House

## Actions

- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1103",
    "number": "1103",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Expressing support for the designation of the week beginning March 2, 2026, as \"School Social Work Week\".",
    "type": "HRES",
    "updateDate": "2026-05-29T19:21:51Z",
    "updateDateIncludingText": "2026-05-29T19:21:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
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
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:02:25Z",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1103ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1103\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Moore of Wisconsin (for herself, Ms. Scholten , and Ms. Garcia of Texas ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the week beginning March 2, 2026, as School Social Work Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of School Social Work Week ;\n**(2)**\nhonors and recognizes the contributions of school social workers to the successes of students in schools across the Nation; and\n**(3)**\nencourages the people of the United States to observe School Social Work Week with appropriate ceremonies and activities that promote awareness of the vital role of school social workers, in schools and in the community as a whole, in helping students prepare for their futures as productive citizens.",
      "versionDate": "2026-03-04",
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "196",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\".",
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
        "name": "Education",
        "updateDate": "2026-05-29T19:21:50Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1103ih.xml"
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
      "title": "Expressing support for the designation of the week beginning March 2, 2026, as \"School Social Work Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-18T13:33:23Z"
    },
    {
      "title": "Expressing support for the designation of the week beginning March 2, 2026, as \"School Social Work Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:06:29Z"
    }
  ]
}
```
