# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1073?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1073
- Title: Great Lakes Gateways Network Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1073
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-09-29T14:12:26Z
- Update date including text: 2025-09-29T14:12:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR E102)
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H607)
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR E102)
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H607)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1073",
    "number": "1073",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000009",
        "district": "9",
        "firstName": "Marcy",
        "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
        "lastName": "Kaptur",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Great Lakes Gateways Network Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-29T14:12:26Z",
    "updateDateIncludingText": "2025-09-29T14:12:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H607)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E102)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:07:15Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1073ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1073\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Kaptur (for herself and Mr. Joyce of Ohio ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to provide technical and financial assistance to identify, conserve, restore, and interpret natural, recreational, historical, and cultural resources within the Great Lakes Watershed, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Great Lakes Gateways Network Act of 2025 .\n#### 2. Great Lakes Gateways\n##### (a) Great Lakes Gateways Network\n**(1) In general**\nThe Secretary of the Interior (referred to in this section as the Secretary ), in cooperation with the Administrator of the Environmental Protection Agency (referred to in this section as the Administrator ), shall provide technical and financial assistance, in cooperation with other Federal agencies, State and local governments, nonprofit organizations, and the private sector to\u2014\n**(A)**\nidentify, conserve, restore, and interpret natural, recreational, historical, and cultural resources within the Great Lakes Watershed;\n**(B)**\nidentify and use the collective resources as Great Lakes Gateways sites for enhancing public education regarding and access to the Great Lakes;\n**(C)**\nlink the Great Lakes Gateways sites with trails, tour roads, scenic byways, and other connections as determined by the Secretary;\n**(D)**\ndevelop and establish Great Lakes Watertrails comprising water routes and connections to Great Lakes Gateways sites and other land resources within the Great Lakes Watershed; and\n**(E)**\ncreate a Great Lakes Gateways Network comprised of Great Lakes Gateways sites and Great Lakes Watertrails.\n**(2) Components**\nComponents of the Great Lakes Gateways Network may include\u2014\n**(A)**\nState or Federal parks or refuges;\n**(B)**\nhistoric seaports;\n**(C)**\narchaeological, cultural, historical, or recreational sites; or\n**(D)**\nother public access and interpretive sites as selected by the Secretary.\n##### (b) Great Lakes Gateways Grants Assistance Program\n**(1) In general**\nThe Secretary, in cooperation with the Administrator, shall establish a Great Lakes Gateways Grants Assistance Program to aid State and local governments, local communities, nonprofit organizations, and the private sector in conserving, restoring, and interpreting important historic, cultural, recreational, and natural resources within the Great Lakes Watershed.\n**(2) Criteria**\nThe Secretary, in cooperation with the Administrator, shall develop appropriate eligibility, prioritization, and review criteria for grants under this section.\n**(3) Matching funds and administrative expenses**\nA grant under this section\u2014\n**(A)**\nshall not exceed 50 percent of eligible project costs;\n**(B)**\nshall be made on the condition that non-Federal sources, including in-kind contributions of services or materials, provide the remainder of eligible project costs; and\n**(C)**\nshall be made on the condition that administrative expenses are not more than 10 percent of all eligible project costs.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $6,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-02-06",
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
            "name": "Canada",
            "updateDate": "2025-09-29T14:12:22Z"
          },
          {
            "name": "Environmental education",
            "updateDate": "2025-09-29T14:11:00Z"
          },
          {
            "name": "Great Lakes",
            "updateDate": "2025-09-29T14:10:54Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2025-09-29T14:11:38Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2025-09-29T14:11:43Z"
          },
          {
            "name": "Indiana",
            "updateDate": "2025-09-29T14:11:49Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-09-29T14:12:26Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2025-09-29T14:11:54Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-09-29T14:11:58Z"
          },
          {
            "name": "Navigation, waterways, harbors",
            "updateDate": "2025-09-29T14:11:10Z"
          },
          {
            "name": "New York State",
            "updateDate": "2025-09-29T14:12:03Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2025-09-29T14:12:09Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-09-29T14:11:04Z"
          },
          {
            "name": "Pennsylvania",
            "updateDate": "2025-09-29T14:12:13Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-09-29T14:11:23Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-09-29T14:10:49Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2025-09-29T14:12:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T14:24:28Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1073ih.xml"
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
      "title": "To direct the Secretary of the Interior to provide technical and financial assistance to identify, conserve, restore, and interpret natural, recreational, historical, and cultural resources within the Great Lakes Watershed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:49Z"
    },
    {
      "title": "Great Lakes Gateways Network Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:28:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Great Lakes Gateways Network Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:28:17Z"
    }
  ]
}
```
