# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1124
- Title: Help Our Kelp Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1124
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-04-10T08:05:43Z
- Update date including text: 2026-04-10T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1124",
    "number": "1124",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Help Our Kelp Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:43Z",
    "updateDateIncludingText": "2026-04-10T08:05:43Z"
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
          "date": "2025-02-07T14:04:30Z",
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
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1124ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1124\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Huffman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of Commerce to establish and carry out a grant program to conserve, restore, and manage kelp forest ecosystems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Help Our Kelp Act of 2025 .\n#### 2. Grants to conserve, restore, and manage kelp forest ecosystems\n##### (a) Sense of Congress\nIt is the sense of Congress that the purposes of this section and the grants authorized by this section are to support native wild kelp forest ecosystems and restore native wild kelp to enable long term recovery of naturally functioning kelp forest ecosystems that do not involve commercial or mechanized harvesting.\n##### (b) Establishment\nNot later than 180 days after the date of the enactment of this section, the Administrator shall establish and carry out a grant program under which the Administrator shall award grants to eligible entities described in subsection (c) to carry out projects described in subsection (d) relating to the conservation, restoration, or management of kelp forest ecosystems.\n##### (c) Eligible entity\nTo be eligible for a grant under this section, an eligible entity shall\u2014\n**(1)**\nbe\u2014\n**(A)**\na member of the fishing industry;\n**(B)**\nan institution of higher education;\n**(C)**\na nonprofit organization;\n**(D)**\nan Indian Tribe;\n**(E)**\na State agency; or\n**(F)**\na local government;\n**(2)**\nconsult or collaborate with any of the other entities described in paragraph (1) throughout the development or implementation of a project relating to the conservation, restoration, or management of kelp forest ecosystems; and\n**(3)**\nsubmit to the Administrator an application describing such project at such time, in such manner, and containing such information as the Administrator may require, including information regarding what criteria will be used to monitor and evaluate the effectiveness of the project and the qualifications of the applicant to conduct, monitor, and evaluate the project.\n##### (d) Eligible projects\nThe Administrator shall award grants to eligible entities for projects that\u2014\n**(1)**\naddress greatest relative regional declines in kelp forest ecosystems;\n**(2)**\nfocus on elements such as\u2014\n**(A)**\nlong term ecosystem resilience of kelp forest ecosystems;\n**(B)**\nlong term socioeconomic resilience related to kelp forest ecosystems;\n**(C)**\nkelp forest seeding and connectivity;\n**(D)**\nre-establishing or recovering natural trophic relationships and structure to support resilience of kelp forest ecosystems through actions such as predator control through targeted urchin removal and recovery of sunflower sea stars;\n**(E)**\nmonitoring and assessment of kelp forest ecosystems;\n**(F)**\nintegration of Indigenous knowledge and cultural practices into restoration and monitoring of kelp forest ecosystems through consultation with Indian Tribes or promotion of Federal or State co-management with Indian Tribes; or\n**(G)**\nother efforts to restore kelp forest ecosystems and prevent large scale losses of kelp forests; or\n**(3)**\nare identified by Indian Tribes or Federal or State restoration or management plans as focal areas for recovery of kelp forests and associated species.\n##### (e) Matching requirement\n**(1) In general**\nExcept as provided in paragraph (2), the amount of Federal funding received as a grant under this section by an eligible entity may not exceed 85 percent of the total cost of the project for which a grant is awarded. For the purposes of this paragraph, the non-Federal share of project costs may be provided by in-kind contributions and other noncash support.\n**(2) Waiver**\nThe Administrator may waive all or part of the requirement in paragraph (1) if the Administrator determines that\u2014\n**(A)**\nno reasonable means are available through which an eligible entity applying for a grant under this section can meet such requirement;\n**(B)**\nthe probable benefit of such project outweighs the public interest in such requirement; and\n**(C)**\nthe project undertaken is established on lands owned by or held in trust for an Indian Tribe.\n##### (f) Guidelines and criteria\nThe Administrator shall\u2014\n**(1)**\nissue guidelines regarding the implementation of the grant program established under subsection (b); and\n**(2)**\nestablish criteria based on best practices, the best available science, and community engagement to rank eligible projects under subsection (d).\n##### (g) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator to carry out this section $5,000,000 for each of fiscal years 2026 through 2030.\n**(2) Availability to Indian Tribes**\n**(A) In general**\nOf the amount authorized to be appropriated by paragraph (1) for a fiscal year, subject to appropriations, not less than $750,000 shall be made available to award grants under this section to eligible entities that are Indian Tribes.\n**(B) Contingency; outreach**\nIf no Indian Tribe is awarded a grant under this section in a fiscal year\u2014\n**(i)**\nfor that fiscal year, the amount described in subparagraph (A) shall be made available to award grants under this section to other eligible entities; and\n**(ii)**\nthe Administrator shall conduct outreach to inform Indian Tribes and organizations that work with Indian Tribes of the grant program established under subsection (b).\n##### (h) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration.\n**(2) Fishing industry**\nThe term fishing industry means\u2014\n**(A)**\nprocessors;\n**(B)**\ncommercial fishermen; and\n**(C)**\nrecreational fishermen.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(5) Kelp forest ecosystem**\nThe term kelp forest ecosystem means a naturally occurring, biotic system dominated by canopy-forming, stipitate, or prostrate benthic macroalgae and associated taxa.\n**(6) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986; and\n**(B)**\nexempt from tax under section 501(a) of such Code.",
      "versionDate": "2025-02-07",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "513",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Help Our Kelp Act of 2025",
      "type": "S"
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
            "name": "Aquaculture",
            "updateDate": "2026-01-21T19:13:03Z"
          },
          {
            "name": "Aquatic ecology",
            "updateDate": "2026-01-21T19:13:03Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-01-21T19:13:03Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-01-21T19:13:03Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-01-21T19:13:03Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-01-21T19:13:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-02T20:28:07Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1124ih.xml"
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
      "title": "Help Our Kelp Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Help Our Kelp Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce to establish and carry out a grant program to conserve, restore, and manage kelp forest ecosystems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:18:28Z"
    }
  ]
}
```
