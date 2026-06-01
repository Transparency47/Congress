# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/655?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/655
- Title: Expressing support for the designation of August 17, 2025, as "Marcus Garvey Recognition Day".
- Congress: 119
- Bill type: HRES
- Bill number: 655
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-19T15:24:45Z
- Update date including text: 2025-09-19T15:24:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-08-15 - IntroReferral: Submitted in House
- 2025-08-15 - IntroReferral: Submitted in House
- Latest action: 2025-08-15: Submitted in House

## Actions

- 2025-08-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-08-15 - IntroReferral: Submitted in House
- 2025-08-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/655",
    "number": "655",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the designation of August 17, 2025, as \"Marcus Garvey Recognition Day\".",
    "type": "HRES",
    "updateDate": "2025-09-19T15:24:45Z",
    "updateDateIncludingText": "2025-09-19T15:24:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
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
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:03:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "IN"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "IL"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OH"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres655ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 655\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Ms. Clarke of New York submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of August 17, 2025, as Marcus Garvey Recognition Day .\nThat the House of Representatives supports the designation of Marcus Garvey Recognition Day and the President issuing a proclamation calling upon the people of the United States to observe that day with appropriate ceremonies and activities.",
      "versionDate": "2025-08-15",
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
        "updateDate": "2025-09-19T15:24:45Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres655ih.xml"
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
      "title": "Expressing support for the designation of August 17, 2025, as \"Marcus Garvey Recognition Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-16T08:18:19Z"
    },
    {
      "title": "Expressing support for the designation of August 17, 2025, as \"Marcus Garvey Recognition Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-16T08:05:49Z"
    }
  ]
}
```
