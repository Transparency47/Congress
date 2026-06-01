# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2337?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2337
- Title: PARENT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2337
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-11-20T09:06:56Z
- Update date including text: 2025-11-20T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2337",
    "number": "2337",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PARENT Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:56Z",
    "updateDateIncludingText": "2025-11-20T09:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:04:05Z",
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
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2337ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2337\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Mills (for himself and Mr. Harris of Maryland ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to clarify birthright citizenship, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prohibiting Automatic Rights to Enter National Territory Act of 2025 or as the PARENT Act of 2025 .\n#### 2. Clarification of birthright citizenship\nSection 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ) is amended by adding at the end the following:\n(j) For purposes of section 301(a), the term subject to the jurisdiction thereof means, with respect to a person born in the United States, that the person was born to a parent who is, at the time of the person\u2019s birth, a citizen of the United States or an alien who is a lawful permanent resident of the United States. .\n#### 3. Effective date\nThis Act, and the amendments made by this Act, shall apply to persons born after the date of enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "name": "Immigration",
        "updateDate": "2025-04-03T11:47:54Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2337ih.xml"
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
      "title": "PARENT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T09:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PARENT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prohibiting Automatic Rights to Enter National Territory Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to clarify birthright citizenship, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T09:48:25Z"
    }
  ]
}
```
