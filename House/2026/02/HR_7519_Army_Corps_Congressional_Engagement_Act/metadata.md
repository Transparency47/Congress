# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7519?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7519
- Title: Army Corps Congressional Engagement Act
- Congress: 119
- Bill type: HR
- Bill number: 7519
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-02-27T17:36:41Z
- Update date including text: 2026-02-27T17:36:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7519",
    "number": "7519",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Army Corps Congressional Engagement Act",
    "type": "HR",
    "updateDate": "2026-02-27T17:36:41Z",
    "updateDateIncludingText": "2026-02-27T17:36:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7519ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7519\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Torres of New York (for himself and Mr. Latimer ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the District Commanders of the Corps of Engineers to provide to offices of Members of Congress annual briefings on projects funded or led by the Corps of Engineers in watersheds within such district, and for other purposes.\n#### 1. Short title\nThis Act may be referred to as the Army Corps Congressional Engagement Act .\n#### 2. Annual briefings on Corps of Engineers projects within United States watersheds\n##### (a) Annual briefing\nFor each calendar year beginning after the date of enactment of this Act, the District Commander of each district of the Corps of Engineers shall provide to each office of a Member of Congress for which the respective congressional district is located, fully or partially, in the district of the Corps of Engineers, an annual briefing, virtually or in-person at the discretion of the District Commander\u2014\n**(1)**\nregarding each project that is\u2014\n**(A)**\nlocated in the district of the Corps of Engineers and, fully or partially, in the respective congressional district;\n**(B)**\nfully or partially located within a watershed; and\n**(C)**\nfunded, partially funded, led, or partially led by the Corps of Engineers, or on which the Corps of Engineers has consulted during the period covered by the report;\n**(2)**\nconveying for each such project\u2014\n**(A)**\nthe location, including identification of any other congressional districts in which the project is being carried out;\n**(B)**\nthe status and progress towards project completion;\n**(C)**\nany delays, or potential delays, in the project timeline;\n**(D)**\nthe amount of funding expended by the Corps of Engineers, total and for the period covered by the report;\n**(E)**\nan estimation any additional funds required to complete the project;\n**(F)**\na list of project expenses for which funds were expended by the Corps of Engineers, since project inception and for the period covered by the report;\n**(G)**\na summary of any environmental impacts of the project and any identifiable impacts of the project on the community local to the project;\n**(H)**\na summary of any engagement between the Corps of Engineers and a non-Federal sponsor or the public with respect to the project; and\n**(I)**\nany opportunities identified by the District Commander for a related study or project authorization that may be carried out in the same congressional district in which the project is being carried out;\n**(3)**\ndetailing any request for additional appropriations for use in one or more such projects; and\n**(4)**\nthat includes a period during which the Member of Congress and staff of the office may ask questions regarding any project being carried out in the congressional district of the Member.\n##### (b) Failure to brief\n**(1) Written statement**\nFor each calendar year beginning after the date of enactment of this Act, if a District Commander has not provided an annual briefing required under subsection (a) by December 1 of the calendar year, the District Commander shall, prior to December 31 of the calendar year, submit to each office of a Member of Congress the District Commander has yet to brief as required under subsection (a) a written statement that includes\u2014\n**(A)**\nan explanation of why the briefing has not occurred;\n**(B)**\nindication of whether the District Commander has contacted the office about scheduling the briefing; and\n**(C)**\na description of how the District Commander plans to ensure that the briefing is scheduled as soon as possible.\n**(2) Investigation**\nIf a District Commander fails to submit a written statement required under paragraph (1), not later than 30 day after the date on which the written statement was due, the Inspector General of the Army shall submit to each office of a Member of Congress the District Commander has yet to brief as required under subsection (a) and the relevant Congressional Committees a report containing\u2014\n**(A)**\nthe results of an investigation of the Inspector General as to why the briefing did not occur during the calendar year in which it was required; and\n**(B)**\nrecommendations of the Inspector General to facilitate and ensure the briefing takes place as soon as possible.\n##### (c) Definitions\nIn this section:\n**(1) Member of Congress**\nThe term Member of Congress includes a Delegate to Congress and a Resident Commissioner to Congress.\n**(2) Relevant Congressional Committees**\nThe term relevant Congressional Committees means\u2014\n**(A)**\nthe Committee on Armed Services of the House of Representatives;\n**(B)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(C)**\nthe Committee on Armed Services of the Senate; and\n**(D)**\nthe Committee on Environment and Public Works of the Senate.",
      "versionDate": "2026-02-11",
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
        "name": "Congress",
        "updateDate": "2026-02-27T17:36:41Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7519ih.xml"
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
      "title": "Army Corps Congressional Engagement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Army Corps Congressional Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the District Commanders of the Corps of Engineers to provide to offices of Members of Congress annual briefings on projects funded or led by the Corps of Engineers in watersheds within such district, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:33Z"
    }
  ]
}
```
