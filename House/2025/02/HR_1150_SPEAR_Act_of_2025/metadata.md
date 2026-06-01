# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1150
- Title: SPEAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1150
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-03-11T17:56:29Z
- Update date including text: 2025-03-11T17:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1150",
    "number": "1150",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "W000829",
        "district": "8",
        "firstName": "Tony",
        "fullName": "Rep. Wied, Tony [R-WI-8]",
        "lastName": "Wied",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "SPEAR Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-11T17:56:29Z",
    "updateDateIncludingText": "2025-03-11T17:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:02:35Z",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1150ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1150\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Wied (for himself, Mr. Grothman , and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to exclude certain populations of the lake sturgeon from the authority of such Act.\n#### 1. Short title\nThis Act may be cited as the Sturgeon Protected and Exempt from Absurd Regulations Act of 2025 or the SPEAR Act of 2025 .\n#### 2. Exclusion of certain populations of lake sturgeon under Endangered Species Act of 1973\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe lake sturgeon (Acipenser fulvescens) holds a special place in the cultural fabric of Wisconsin, especially for the communities located on Lake Winnebago and the Winnebago System.\n**(2)**\nThrough the staunch dedication and close public-private collaboration of the Wisconsin Department of Natural Resources, Sturgeon for Tomorrow, the Sturgeon Advisory Committee, the Sturgeon Guard, and local fishing, sportsmen, and conservation groups, Wisconsin has become the global leader in lake sturgeon management.\n**(3)**\nAs a result of these efforts and the development and implementation of a comprehensive management plan, the Lake Winnebago system is home to a thriving lake sturgeon population, one of the largest in North America, and the most successful sustainable sturgeon fisheries in the world.\n**(4)**\nAn integral component of this management plan is the annual sturgeon spearing season that is meticulously managed and provides the data necessary, along with data from detailed spawning assessments, to maintain an accurate account of population levels needed and allowable maximum harvest rates to ensure the health and sustainability of the species.\n**(5)**\nMandatory registration stations are established to collect detailed data on the length, weight, sex, and tag status of each harvested fish and ensure strict seasonal harvest caps are followed.\n**(6)**\nThe spearing season has grown into a unique cultural event filled with strong traditions and community ties, drawing participants from throughout Wisconsin and many other States, and is crucial to the livelihoods of local communities and small businesses near the Winnebago System who rely on the annual season.\n**(7)**\nIt is vital that this long-standing and cherished tradition be protected and that Wisconsin is allowed to continue its successful Winnebago System and statewide management of lake sturgeon.\n##### (b) Exclusion from listing\nSection 4(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking The Secretary shall by regulation and inserting Except as provided in paragraph (4), the Secretary shall by regulation ; and\n**(2)**\nby adding at the end the following:\n(4) Applicability to lake sturgeon The Secretary may not make a determination under this subsection that any population of the lake sturgeon (Acipenser fulvescens) in Wisconsin is threatened or endangered. .",
      "versionDate": "2025-02-07",
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
        "name": "Animals",
        "updateDate": "2025-03-11T17:56:29Z"
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
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1150ih.xml"
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
      "title": "SPEAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPEAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sturgeon Protected and Exempt from Absurd Regulations Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to exclude certain populations of the lake sturgeon from the authority of such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:18:28Z"
    }
  ]
}
```
