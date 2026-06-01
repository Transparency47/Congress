# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/745
- Title: Abundant American Resources Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 745
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-02-06T19:45:12Z
- Update date including text: 2026-02-06T19:45:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/745",
    "number": "745",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Abundant American Resources Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-06T19:45:12Z",
    "updateDateIncludingText": "2026-02-06T19:45:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:01:25Z",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WA"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr745ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 745\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Arrington (for himself, Mr. Newhouse , Ms. Maloy , Mr. Moore of Utah , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Director of the Bureau of Land Management and the Chief of the United States Forest Service to conduct a study of onshore mineral values and the Director of the Bureau of Ocean Energy Management to conduct a study of offshore mineral values.\n#### 1. Short title\nThis Act may be cited as the Abundant American Resources Act of 2025 .\n#### 2. Onshore and offshore mineral value studies\n##### (a) Onshore mineral study\nNot later than three years after the date of the enactment of this section\u2014\n**(1)**\nthe Director of the Bureau of Land Management, shall complete (including through a contract with a private entity) a study to determine the dollar value of liquid, gaseous, locatable, leasable, and salable minerals present in each covered onshore area under the jurisdiction of the Director; and\n**(2)**\nthe Chief of the Forest Service, shall complete (including through a contract with a private entity) a study to determine the dollar value of liquid, gaseous, and locatable minerals present in each covered onshore area under the jurisdiction of the Chief.\n##### (b) Offshore mineral study\nNot later than three years after the date of the enactment of this section, the Director of the Bureau of Ocean Energy Management shall complete (including through a contract with a private entity) a study to determine the dollar value of liquid, gaseous, and locatable minerals present in each covered offshore area under the jurisdiction of the Director.\n##### (c) Included and excluded areas\nThe studies required under subsections (a) and (b) shall\u2014\n**(1)**\ninclude co-managed areas; and\n**(2)**\nexclude\u2014\n**(A)**\nany unit of the National Park System; and\n**(B)**\nany national monument designated as an area of critical environmental concern before January 1, 2000.\n##### (d) Definitions\nIn this section\u2014\n**(1)**\nthe term area of critical environmental concern means an area that meets all of the criteria identified under section 1610.7\u20132(d) of title 43, Code of Federal Regulations;\n**(2)**\nthe term co-managed area means an area that is under the jurisdiction of two or more Federal agencies;\n**(3)**\nthe term covered onshore area means\u2014\n**(A)**\na national monument\u2014\n**(i)**\nthat is not a marine national monument; and\n**(ii)**\nthat was designated after December 31, 1999;\n**(B)**\nan area of critical environmental concern; and\n**(C)**\nan area that has been withdrawn from\u2014\n**(i)**\nentry under the general mining laws; or\n**(ii)**\noperation of the mineral leasing and mineral materials laws;\n**(4)**\nthe term covered offshore area means\u2014\n**(A)**\na marine national monument;\n**(B)**\nan offshore area that has been withdrawn from\u2014\n**(i)**\nentry under the general mining laws; or\n**(ii)**\noperation of the mineral leasing and mineral materials laws; and\n**(C)**\nan offshore area that is otherwise designated as an area under moratorium;\n**(5)**\nthe term liquid minerals includes crude oil; and\n**(6)**\nthe term gaseous minerals includes natural gas.",
      "versionDate": "2025-01-28",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-06T19:44:55Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-02-06T19:45:01Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2026-02-06T19:45:06Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-02-06T19:45:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T19:50:36Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr745ih.xml"
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
      "title": "Abundant American Resources Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Abundant American Resources Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the Bureau of Land Management and the Chief of the United States Forest Service to conduct a study of onshore mineral values and the Director of the Bureau of Ocean Energy Management to conduct a study of offshore mineral values.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:40Z"
    }
  ]
}
```
