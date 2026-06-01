# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/529?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/529
- Title: Honoring and celebrating National Boys and Girls Club Week of 2025.
- Congress: 119
- Bill type: HRES
- Bill number: 529
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2025-07-07T13:47:41Z
- Update date including text: 2025-07-07T13:47:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-06-23 - IntroReferral: Submitted in House
- 2025-06-23 - IntroReferral: Submitted in House
- Latest action: 2025-06-23: Submitted in House

## Actions

- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-06-23 - IntroReferral: Submitted in House
- 2025-06-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/529",
    "number": "529",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Honoring and celebrating National Boys and Girls Club Week of 2025.",
    "type": "HRES",
    "updateDate": "2025-07-07T13:47:41Z",
    "updateDateIncludingText": "2025-07-07T13:47:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:03:35Z",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres529ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 529\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Yakym (for himself and Ms. Scholten ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring and celebrating National Boys and Girls Club Week of 2025.\nThat the House of Representatives\u2014\n**(1)**\ncalls on the people of the United States to celebrate National Boys and Girls Club Week; and\n**(2)**\nencourages Americans to recognize and commend the Boys and Girls Clubs of America for building great futures for youth in communities throughout the United States.",
      "versionDate": "2025-06-23",
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
        "updateDate": "2025-07-07T13:47:41Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres529ih.xml"
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
      "title": "Honoring and celebrating National Boys and Girls Club Week of 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T08:49:24Z"
    },
    {
      "title": "Honoring and celebrating National Boys and Girls Club Week of 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T08:05:30Z"
    }
  ]
}
```
