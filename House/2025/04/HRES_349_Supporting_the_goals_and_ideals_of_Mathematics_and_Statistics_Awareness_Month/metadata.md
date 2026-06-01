# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/349
- Title: Supporting the goals and ideals of Mathematics and Statistics Awareness Month.
- Congress: 119
- Bill type: HRES
- Bill number: 349
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House
- Latest action: 2025-04-24: Submitted in House

## Actions

- 2025-04-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/349",
    "number": "349",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Supporting the goals and ideals of Mathematics and Statistics Awareness Month.",
    "type": "HRES",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:07:15Z",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres349ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 349\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mrs. Kim (for herself, Mr. Tonko , Mr. Krishnamoorthi , and Mr. Kean ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nSupporting the goals and ideals of Mathematics and Statistics Awareness Month.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of Mathematics and Statistics Awareness Month to increase the visibility of mathematics and statistics as fields of study and to communicate the myriad benefits of education in mathematics and statistics;\n**(2)**\nrecognizes that mathematics and statistics underpin all of the STEM disciplines (science, technology, engineering, and mathematics), which are critical to the United States education system and economic prosperity; and\n**(3)**\ncelebrates the role that mathematics and statistics play in the everyday lives of all Americans, including in our technology, cybersecurity, news, games, literature, music, and education.",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-19T15:49:19Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres349ih.xml"
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
      "title": "Supporting the goals and ideals of Mathematics and Statistics Awareness Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T13:33:23Z"
    },
    {
      "title": "Supporting the goals and ideals of Mathematics and Statistics Awareness Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:05:28Z"
    }
  ]
}
```
