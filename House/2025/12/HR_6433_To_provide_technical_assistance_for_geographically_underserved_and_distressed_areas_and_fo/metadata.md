# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6433?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6433
- Title: Rural Uplift and Revitalization Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 6433
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:06:58Z
- Update date including text: 2026-05-16T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4977)
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4977)
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6433",
    "number": "6433",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Rural Uplift and Revitalization Assistance Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:06:58Z",
    "updateDateIncludingText": "2026-05-16T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4977)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-04T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:03:04Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6433ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6433\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Davis of North Carolina (for himself and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide technical assistance for geographically underserved and distressed areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Uplift and Revitalization Assistance Act .\n#### 2. Technical assistance for geographically underserved and distressed areas\n##### (a) In general\nWithin 1 year after the date of the enactment of this section, the Secretary of Agriculture (in this section referred to as the Secretary ) shall directly, or through cooperative agreements, provide technical assistance and strengthen local capacity to improve access to rural development programs administered by the Secretary for local partners (including local governments, cooperatives, businesses, healthcare facilities and networks, community anchor institutions (as defined in section 60302(6) of the Digital Equity Act of 2021), and nonprofit organizations) in geographically underserved and distressed areas.\n##### (b) Reports\nBeginning 1 year after the date of the enactment of this section, the Secretary shall annually publish, make available to the public, and submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report on how the provision of technical assistance under subsection (a) has affected geographically underserved and distressed areas in the year covered by the report.\n##### (c) Definition of geographically underserved and distressed area\nIn this section, the term geographically underserved and distressed area means a rural area (as determined by the Secretary)\u2014\n**(1)**\nin a socially vulnerable community (as determined by the Secretary);\n**(2)**\nin a persistent poverty county (as determined by the Secretary);\n**(3)**\nin a economically distressed area (as determined by the Secretary); or\n**(4)**\nthat lacks adequate water services, sewer services, or decent housing in any region near the border between the United States and Mexico.",
      "versionDate": "2025-12-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-06T21:40:46Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6433ih.xml"
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
      "title": "Rural Uplift and Revitalization Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Uplift and Revitalization Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide technical assistance for geographically underserved and distressed areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:23Z"
    }
  ]
}
```
