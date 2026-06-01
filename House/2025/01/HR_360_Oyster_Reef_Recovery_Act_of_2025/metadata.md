# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/360?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/360
- Title: Oyster Reef Recovery Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 360
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-03-19T08:05:40Z
- Update date including text: 2025-03-19T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/360",
    "number": "360",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "O000172",
        "district": "14",
        "firstName": "Alexandria",
        "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
        "lastName": "Ocasio-Cortez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Oyster Reef Recovery Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-19T08:05:40Z",
    "updateDateIncludingText": "2025-03-19T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:03:05Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MD"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr360ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 360\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Ocasio-Cortez (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of Commerce to establish the Oyster Reef Restoration and Conservation Program.\n#### 1. Short title\nThis Act may be cited as the Oyster Reef Recovery Act of 2025 .\n#### 2. Oyster Reef Restoration and Conservation Program\n##### (a) Oyster Reef Restoration and Conservation Program\n**(1) In general**\nThe Administrator shall establish a program for the conservation of oyster reefs, to be known as the Oyster Reef Restoration and Conservation Program .\n**(2) Program duties**\nIn carrying out the Program, the Administrator shall provide technical and financial assistance to covered entities to\u2014\n**(A)**\nidentify priorities for oyster reef restoration, including existing oyster reef sites and locations of historically significant oyster reefs with the potential for restoration;\n**(B)**\nevaluate the health of and threats to oyster reefs, including through mapping and water quality monitoring, and identify conservation actions to address such threats;\n**(C)**\nconduct voluntary planning, construction, assessment, protection, monitoring, restoration, and enhancement projects with respect to oyster reefs;\n**(D)**\nwork to ensure the health and resilience of existing and restored oyster reefs through adaptive management procedures based on the best available science;\n**(E)**\nbuild partnerships and capacity to carry out environmental conservation and stewardship measures with respect to oyster reefs;\n**(F)**\ndevelop and implement monitoring protocols to ensure the success of conservation, restoration, and enhancement measures with respect to oyster reefs;\n**(G)**\ncollaborate and share information with other covered entities and the public with respect to best management practices for the conservation, restoration, and enhancement of oyster reefs; and\n**(H)**\nsupport workforce training focused on coastal resilience and restoration concepts, principles, techniques, and implementation, especially to benefit underserved communities.\n**(3) Grant program**\n**(A) In general**\nThe Administrator shall establish a competitive grant program to award amounts to persons that submit an application under subparagraph (B) for the purposes of conducting research, planning, construction, assessments, management, building capacity, monitoring, collaborating and sharing information, or workforce training with respect to the conservation, restoration, enhancement, or management of oyster reefs.\n**(B) Applications**\nTo be eligible for a grant under this paragraph, a person shall submit to the Administrator an application in such form, at such time, and containing such information, including a sufficient demonstration that the project will not reasonably interfere with commercial or recreational fishing or other water-related uses of the relevant area, as the Administrator determines appropriate.\n##### (b) Rule of construction\nNothing in this section may be construed to preempt or limit the authority of a State or an Indian Tribe to manage oyster reefs or species of oysters.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section $15,000,000 for each of fiscal years 2026 through 2030.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na unit of the Federal or a State, local, or Tribal government;\n**(B)**\na nongovernmental institution;\n**(C)**\na nonprofit organization;\n**(D)**\nan institution of higher education;\n**(E)**\nthe shellfish industry; and\n**(F)**\na private individual or entity.\n**(3) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986; and\n**(B)**\nexempt from tax under section 501(a) of such Code.\n**(4) Program**\nThe term Program means the Oyster Reef Restoration and Conservation Program established under subsection (a)(1).\n**(5) Shellfish industry**\nThe term shellfish industry means shellfish growers and shellfish harvesters.",
      "versionDate": "2025-01-13",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-03-11T19:44:00Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-03-11T19:43:50Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-11T19:43:44Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-03-11T19:44:09Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-03-11T19:43:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-26T18:50:22Z"
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
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr360ih.xml"
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
      "title": "Oyster Reef Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Oyster Reef Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T06:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to establish the Oyster Reef Restoration and Conservation Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T06:33:32Z"
    }
  ]
}
```
