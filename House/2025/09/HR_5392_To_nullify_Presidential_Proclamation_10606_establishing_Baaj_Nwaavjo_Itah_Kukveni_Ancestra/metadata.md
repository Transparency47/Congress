# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5392
- Title: Northern Arizona Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5392
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-11-13T09:05:20Z
- Update date including text: 2025-11-13T09:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5392",
    "number": "5392",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Northern Arizona Protection Act",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:20Z",
    "updateDateIncludingText": "2025-11-13T09:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "WY"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AZ"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "ID"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5392ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5392\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Gosar (for himself, Mr. Crane , Ms. Hageman , and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo nullify Presidential Proclamation 10606, establishing Baaj Nwaavjo I\u2019tah Kukveni-Ancestral Footprints of the Grand Canyon National Monument and withdrawing certain land in Arizona from mineral entry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Northern Arizona Protection Act .\n#### 2. Restriction on use of Antiquities Act in certain areas in Arizona\n##### (a) Nullification of Presidential Proclamation\nPresidential Proclamation 10606 of August 8, 2023 (88 Fed. Reg. 55331, relating to the establishment of the Baaj Nwaavjo I\u2019tah Kukveni-Ancestral Footprints of the Grand Canyon National Monument), shall have no force or effect.\n##### (b) Restriction on future monument designations\nNo extension or establishment of national monuments within the area generally depicted as Baaj Nwaavjo I\u2019tah Kukveni-Ancestral Footprints of the Grand Canyon National Monument on the map titled Baaj Nwaavjo I\u2019tah Kukveni-Ancestral Footprints of the Grand Canyon National Monument and dated August 5, 2023, may be undertaken except by express authorization of Congress.",
      "versionDate": "2025-09-16",
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
        "name": "Native Americans",
        "updateDate": "2025-09-24T15:39:44Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5392ih.xml"
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
      "title": "Northern Arizona Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Northern Arizona Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify Presidential Proclamation 10606, establishing Baaj Nwaavjo I'tah Kukveni-Ancestral Footprints of the Grand Canyon National Monument and withdrawing certain land in Arizona from mineral entry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:26Z"
    }
  ]
}
```
