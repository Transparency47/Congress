# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3647
- Title: SAFE CROSS Act
- Congress: 119
- Bill type: HR
- Bill number: 3647
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-02-11T09:06:10Z
- Update date including text: 2026-02-11T09:06:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3647",
    "number": "3647",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SAFE CROSS Act",
    "type": "HR",
    "updateDate": "2026-02-11T09:06:10Z",
    "updateDateIncludingText": "2026-02-11T09:06:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:45:48Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3647ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3647\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Mullin introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Railroad Administration to conduct a study to identify potential benefits and challenges of implementing and using sensors enabled with artificial intelligence as a safety measure at rail crossings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Study on AI For Enhanced Crossing Safety Act or the SAFE CROSS Act .\n#### 2. Study on AI-enabled sensors at rail crossings\n##### (a) Study\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Railroad Administration, acting through the Associate Administrator for Railroad Safety, shall conduct a study to identify any potential benefits and challenges of implementing and using sensors enabled with artificial intelligence at rail crossings as a safety measure to reduce pedestrian and traffic accidents.\n##### (b) Elements\nThe study in subsection (a) shall include the following:\n**(1)**\nA review by the Administrator of\u2014\n**(A)**\nany existing pilot program regarding the implementation of sensors enabled with artificial intelligence at rail crossings; and\n**(B)**\nany deployment of such sensors at rail crossings.\n**(2)**\nA cost-benefit analysis comparing sensors enabled with artificial intelligence and other safety enhancement measures that may be used at rail crossings, such as grade separations.\n**(3)**\nIdentification by the Administrator of best practices with respect to implementing and using sensors enabled with artificial intelligence at rail crossings.\n##### (c) Publication\nNot later than 30 days after the date on which the study under subsection (a) is complete, the Administrator shall publish to a publicly accessible website of the Office of Railroad Safety of the Federal Railroad Administration\u2014\n**(1)**\nthe results of the study; and\n**(2)**\nbest practices and recommendations of the Administrator with respect to implementing and using sensors enabled with artificial intelligence at rail crossings for use by\u2014\n**(A)**\nFederal, State, Tribal, and local governmental entities that regulate rail crossing safety; and\n**(B)**\nany private entity that is legally required to maintain safety technology at rail crossings.",
      "versionDate": "2025-05-29",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-16T17:26:09Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3647ih.xml"
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
      "title": "SAFE CROSS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE CROSS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Study on AI For Enhanced Crossing Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Railroad Administration to conduct a study to identify potential benefits and challenges of implementing and using sensors enabled with artificial intelligence as a safety measure at rail crossings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:26Z"
    }
  ]
}
```
