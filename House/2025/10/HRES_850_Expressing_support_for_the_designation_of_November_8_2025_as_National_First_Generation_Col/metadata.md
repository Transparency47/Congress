# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/850?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/850
- Title: Expressing support for the designation of November 8, 2025, as "National First-Generation College Celebration Day".
- Congress: 119
- Bill type: HRES
- Bill number: 850
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-01-08T09:07:08Z
- Update date including text: 2026-01-08T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House
- Latest action: 2025-10-31: Submitted in House

## Actions

- 2025-10-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/850",
    "number": "850",
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
    "title": "Expressing support for the designation of November 8, 2025, as \"National First-Generation College Celebration Day\".",
    "type": "HRES",
    "updateDate": "2026-01-08T09:07:08Z",
    "updateDateIncludingText": "2026-01-08T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:05:25Z",
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
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "ID"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres850ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 850\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Moore of Wisconsin (for herself and Mr. Simpson ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of November 8, 2025, as National First-Generation College Celebration Day .\nThat the House of Representatives urges all people in the United States to\u2014\n**(1)**\ncelebrate National First-Generation College Celebration Day throughout the United States;\n**(2)**\nrecognize the important role that first-generation college students play in helping to develop the future workforce; and\n**(3)**\ncelebrate the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) and its programs that help historically excluded students access higher education.",
      "versionDate": "2025-10-31",
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
        "name": "Education",
        "updateDate": "2025-11-25T18:57:44Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres850ih.xml"
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
      "title": "Expressing support for the designation of November 8, 2025, as \"National First-Generation College Celebration Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-04T07:33:16Z"
    },
    {
      "title": "Expressing support for the designation of November 8, 2025, as \"National First-Generation College Celebration Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-01T08:05:23Z"
    }
  ]
}
```
