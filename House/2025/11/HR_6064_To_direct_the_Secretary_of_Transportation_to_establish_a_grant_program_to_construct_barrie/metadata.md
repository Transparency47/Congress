# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6064
- Title: Protecting Homes from Trains Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6064
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-01-07T09:05:46Z
- Update date including text: 2026-01-07T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-17 - IntroReferral: Sponsor introductory remarks on measure. (CR E1069)
- 2025-11-18 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-17 - IntroReferral: Sponsor introductory remarks on measure. (CR E1069)
- 2025-11-18 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6064",
    "number": "6064",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Protecting Homes from Trains Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:46Z",
    "updateDateIncludingText": "2026-01-07T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E1069)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-18T18:19:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6064ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6064\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a grant program to construct barriers near rail lines that are adjacent to a residential structure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Homes from Trains Act of 2025 .\n#### 2. Grant program to construct barriers near rail lines adjacent to a residential structure\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this section, the Secretary of Transportation shall establish a program to provide grants to eligible recipients to design or construct a barrier to mitigate rail activity that may negatively impact a residential structure or its use, including\u2014\n**(1)**\ndamage caused by a train derailment;\n**(2)**\nnoise caused by a train; and\n**(3)**\nvibrations caused by a train.\n##### (b) Use of funds\nA grant provided under this section may be used to design or construct a barrier located\u2014\n**(1)**\nadjacent to a rail line; and\n**(2)**\nbetween the rail line and any residential area that\u2014\n**(A)**\nincludes structures; and\n**(B)**\nis affected, or potentially affected, by any rail activity described in subsection (a).\n##### (c) Eligible recipients\nThe Secretary may make a grant under the program established in subsection (a) to the following:\n**(1)**\nA State.\n**(2)**\nA group of States.\n**(3)**\nAn Interstate Compact.\n**(4)**\nA public agency or publicly chartered authority established by one or more States.\n**(5)**\nA political subdivision of a State.\n**(6)**\nAmtrak or another rail carrier that provides intercity rail passenger transportation.\n**(7)**\nA Class II railroad or Class III railroad or a holding company of a Class II or Class III railroad, or an association representing a Class II or III railroad.\n**(8)**\nAny rail carrier in partnership with one or more entities described in paragraphs (1) through (5).\n##### (d) Applications\nTo be eligible for a grant under the program established in subsection (a), an entity described in subsection (c) shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n##### (e) State defined\nIn this section, the term State means each of the several States, the District of Columbia, and each commonwealth, territory, or possession of the United States.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out the program established in subsection (a) $100,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-11-17",
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
        "updateDate": "2025-11-24T17:39:39Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6064ih.xml"
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
      "title": "Protecting Homes from Trains Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T13:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Homes from Trains Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a grant program to construct barriers near rail lines that are adjacent to a residential structure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:33:28Z"
    }
  ]
}
```
