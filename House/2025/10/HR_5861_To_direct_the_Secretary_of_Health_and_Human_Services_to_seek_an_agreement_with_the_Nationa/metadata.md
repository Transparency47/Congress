# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5861?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5861
- Title: Legacy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5861
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-12-17T09:06:27Z
- Update date including text: 2025-12-17T09:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5861",
    "number": "5861",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Legacy Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:27Z",
    "updateDateIncludingText": "2025-12-17T09:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5861ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5861\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Suozzi (for himself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to seek an agreement with the National Academies of Sciences, Engineering, and Medicine to conduct a study on establishing a system for storing last wish documents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Legacy Act of 2025 .\n#### 2. Study on establishing system for storing and retrieving last wish documents\n##### (a) In general\nThe Secretary shall seek to enter into an agreement with the National Academies under which the National Academies conduct a study on establishing and maintaining a national, confidential, and secure system for storing and retrieving by an authorized agent a last wish document of an individual, at no cost to such individual.\n##### (b) Submission of status and results\nThe agreement entered into under subsection (a) shall require the National Academies to submit to the Secretary and Congress\u2014\n**(1)**\nnot later than 2 years after the date of enactment of this Act, the status of the study conducted under such agreement; and\n**(2)**\nnot later than 4 years after the date of enactment of this Act, the results of the study conducted under such agreement.\n##### (c) Definitions\nIn this Act:\n**(1) Last wish document**\nThe term last wish document includes\u2014\n**(A)**\nan advance directive;\n**(B)**\nan organ donor registration;\n**(C)**\na healthcare or medical proxy;\n**(D)**\na power of attorney; or\n**(E)**\na living will.\n**(2) National Academies**\nThe term National Academies means the National Academies of Sciences, Engineering, and Medicine.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-10-28",
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
        "name": "Health",
        "updateDate": "2025-11-26T15:22:58Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5861ih.xml"
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
      "title": "Legacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Legacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to seek an agreement with the National Academies of Sciences, Engineering, and Medicine to conduct a study on establishing a system for storing last wish documents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:19Z"
    }
  ]
}
```
