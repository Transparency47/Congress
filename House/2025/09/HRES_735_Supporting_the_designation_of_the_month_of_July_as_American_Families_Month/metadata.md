# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/735?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/735
- Title: Supporting the designation of the month of July as "American Families Month".
- Congress: 119
- Bill type: HRES
- Bill number: 735
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-01-22T09:06:09Z
- Update date including text: 2026-01-22T09:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House
- Latest action: 2025-09-18: Submitted in House

## Actions

- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/735",
    "number": "735",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Supporting the designation of the month of July as \"American Families Month\".",
    "type": "HRES",
    "updateDate": "2026-01-22T09:06:09Z",
    "updateDateIncludingText": "2026-01-22T09:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:04:25Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "OK"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TN"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres735ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 735\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Cloud (for himself and Mr. Moore of Alabama ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nSupporting the designation of the month of July as American Families Month .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes that stably married mothers and fathers provide the best outcomes for children;\n**(2)**\nrecognizes the importance that the nuclear family has played in the success and prosperity of the United States;\n**(3)**\nacknowledges the far-reaching detrimental impacts that declining marriage rates have on the United States;\n**(4)**\ncalls for policies that support nuclear families and remove barriers to family formation; and\n**(5)**\nsupports the designation of American Families Month to raise awareness about the importance and benefits of strong, stably married families and to call the general public to actions that support and build strong, stably married families.",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-09-24T14:56:08Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres735ih.xml"
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
      "title": "Supporting the designation of the month of July as \"American Families Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T08:18:17Z"
    },
    {
      "title": "Supporting the designation of the month of July as \"American Families Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:07:16Z"
    }
  ]
}
```
