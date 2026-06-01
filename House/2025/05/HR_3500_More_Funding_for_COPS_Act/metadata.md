# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3500
- Title: More Funding for COPS Act
- Congress: 119
- Bill type: HR
- Bill number: 3500
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2025-09-11T08:06:27Z
- Update date including text: 2025-09-11T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-19: Introduced in House

## Actions

- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3500",
    "number": "3500",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "More Funding for COPS Act",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:27Z",
    "updateDateIncludingText": "2025-09-11T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T16:02:10Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "IA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3500ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3500\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Mr. Ryan (for himself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to reauthorize the public safety and community policing grant program under part Q of title I of that Act.\n#### 1. Short title\nThis Act may be cited as the More Funding for COPS Act .\n#### 2. Reauthorization of COPS ON THE BEAT grant program\nSection 1001(a)(11)(A) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a)(11)(A) ) is amended by striking $1,047,119,000 for each of fiscal years 2006 through 2009 and inserting $1,163,032,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-05-19",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-28T17:32:39Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3500ih.xml"
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
      "title": "More Funding for COPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "More Funding for COPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to reauthorize the public safety and community policing grant program under part Q of title I of that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:20Z"
    }
  ]
}
```
