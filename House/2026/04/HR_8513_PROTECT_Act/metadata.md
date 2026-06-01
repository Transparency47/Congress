# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8513
- Title: PROTECT Act
- Congress: 119
- Bill type: HR
- Bill number: 8513
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-18T18:55:10Z
- Update date including text: 2026-05-18T18:55:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8513",
    "number": "8513",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "PROTECT Act",
    "type": "HR",
    "updateDate": "2026-05-18T18:55:10Z",
    "updateDateIncludingText": "2026-05-18T18:55:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:04:50Z",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NV"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8513ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8513\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Hill of Arkansas (for himself and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Secretary of Homeland Security to disseminate guidance regarding certain best practices relating to the handling of personally identifiable information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Resources and Oversight to Ensure Confidentiality of Those who serve Act or the PROTECT Act .\n#### 2. Dissemination of DHS guidance regarding certain best practices relating to the handling of personally identifiable information\n##### (a) In general\nNot later than one year after the date of the enactment of this Act and quadrennially thereafter, the Secretary of Homeland Security shall disseminate to Federal, State, and local government agencies and appropriate private sector entities guidance regarding best practices regarding the following:\n**(1)**\nThe handling by such agencies and entities of personally identifiable information of officers, officials, employees, and contractors of such agencies.\n**(2)**\nActions such officers, officials, and employees can take to ensure their safety.\n##### (b) Definition\nIn this section, the term personally identifiable information means any information that permits the identity of an individual to be directly or indirectly inferred, including any other information that is linked or linkable to such individual, regardless of whether such individual is a United States citizen, lawful permanent resident, or visitor to the United States.",
      "versionDate": "2026-04-27",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-18T18:55:09Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8513ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T08:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Resources and Oversight to Ensure Confidentiality of Those who serve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T08:23:35Z"
    },
    {
      "title": "PROTECT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T08:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security to disseminate guidance regarding certain best practices relating to the handling of personally identifiable information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T08:18:34Z"
    }
  ]
}
```
