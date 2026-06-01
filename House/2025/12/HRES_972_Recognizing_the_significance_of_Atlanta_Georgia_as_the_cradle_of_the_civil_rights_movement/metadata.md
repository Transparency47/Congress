# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/972
- Title: Recognizing the significance of Atlanta, Georgia, as the cradle of the civil rights movement.
- Congress: 119
- Bill type: HRES
- Bill number: 972
- Origin chamber: House
- Introduced date: 2025-12-19
- Update date: 2026-01-05T15:46:56Z
- Update date including text: 2026-01-05T15:46:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-19: Introduced in House
- 2025-12-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-12-19 - IntroReferral: Submitted in House
- 2025-12-19 - IntroReferral: Submitted in House
- Latest action: 2025-12-19: Submitted in House

## Actions

- 2025-12-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-12-19 - IntroReferral: Submitted in House
- 2025-12-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-19",
    "latestAction": {
      "actionDate": "2025-12-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/972",
    "number": "972",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Recognizing the significance of Atlanta, Georgia, as the cradle of the civil rights movement.",
    "type": "HRES",
    "updateDate": "2026-01-05T15:46:56Z",
    "updateDateIncludingText": "2026-01-05T15:46:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-19",
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
          "date": "2025-12-19T19:31:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "GA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "GA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres972ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 972\nIN THE HOUSE OF REPRESENTATIVES\nDecember 19, 2025 Mr. David Scott of Georgia (for himself, Mrs. McBath , Ms. Williams of Georgia , Mr. Bishop , and Mr. Johnson of Georgia ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the significance of Atlanta, Georgia, as the cradle of the civil rights movement.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes Atlanta\u2019s significance as the cradle of the civil rights movement for the city\u2019s immense contributions to the cause of equal rights; and\n**(2)**\nhonors Atlanta\u2019s role as a dynamic, vibrant city that continues to lead by example to show the success that is possible when Americans are given equal opportunities to pursue excellence.",
      "versionDate": "2025-12-19",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-01-05T15:46:56Z"
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
      "date": "2025-12-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres972ih.xml"
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
      "title": "Recognizing the significance of Atlanta, Georgia, as the cradle of the civil rights movement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T09:18:30Z"
    },
    {
      "title": "Recognizing the significance of Atlanta, Georgia, as the cradle of the civil rights movement.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T09:06:44Z"
    }
  ]
}
```
