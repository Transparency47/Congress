# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/513
- Title: Help Our Kelp Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 513
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-03-26T11:03:17Z
- Update date including text: 2026-03-26T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/513",
    "number": "513",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Help Our Kelp Act of 2025",
    "type": "S",
    "updateDate": "2026-03-26T11:03:17Z",
    "updateDateIncludingText": "2026-03-26T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-02-11T17:12:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-11T17:12:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s513is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 513\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Merkley (for himself, Mr. King , Mr. Wyden , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Commerce to establish and carry out a grant program to conserve, restore, and manage kelp forest ecosystems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Help Our Kelp Act of 2025 .\n#### 2. Grants to conserve, restore, and manage kelp forest ecosystems\n##### (a) Establishment\nThe Administrator shall establish, not later than 180 days after the date of the enactment of this Act, and carry out a grant program under which the Administrator shall award grants to eligible entities described in subsection (b) to carry out eligible projects described in subsection (c) relating to the conservation, restoration, or management of kelp forest ecosystems.\n##### (b) Eligible entities\nTo be eligible for a grant under this section, an entity shall\u2014\n**(1)**\nbe\u2014\n**(A)**\na member of the fishing industry;\n**(B)**\nan institution of higher education;\n**(C)**\na nonprofit organization;\n**(D)**\nan Indian Tribe;\n**(E)**\na State agency; or\n**(F)**\na local government;\n**(2)**\nconsult or collaborate with any other entity described in paragraph (1) throughout the development or implementation of a project relating to the conservation, restoration, or management of kelp forest ecosystems; and\n**(3)**\nsubmit to the Administrator an application describing that project at such time, in such manner, and containing such information as the Administrator may require, including information regarding\u2014\n**(A)**\nwhat criteria will be used to monitor and evaluate the effectiveness of the project; and\n**(B)**\nthe qualifications of the applicant to conduct, monitor, and evaluate the project.\n##### (c) Eligible projects\nThe Administrator shall award grants to eligible entities for projects that\u2014\n**(1)**\naddress the greatest relative regional declines in kelp forest ecosystems;\n**(2)**\nfocus on elements such as\u2014\n**(A)**\nthe long-term resilience of kelp forest ecosystems;\n**(B)**\nlong-term socioeconomic resilience related to kelp forest ecosystems;\n**(C)**\nkelp forest seeding and connectivity;\n**(D)**\nreestablishing or recovering natural trophic relationships and structure to support the resilience of kelp forest ecosystems through actions such as predator control through targeted urchin removal and the recovery of sunflower sea stars;\n**(E)**\nmonitoring and assessment of kelp forest ecosystems;\n**(F)**\nintegration of Indigenous knowledge and cultural practices into restoration and monitoring of kelp forest ecosystems through consultation with Indian Tribes or promotion of Federal or State co-management with Indian Tribes; or\n**(G)**\nother efforts to restore kelp forest ecosystems and prevent large-scale losses of kelp forests; or\n**(3)**\nare identified by Indian Tribes or Federal or State restoration or management plans as focal areas for recovery of kelp forests and associated species.\n##### (d) Matching requirement\n**(1) In general**\nExcept as provided in paragraph (2), the amount of Federal funding received as a grant under this section by an eligible entity may not exceed 85 percent of the total cost of the project for which the grant is awarded. For the purposes of this paragraph, the non-Federal share of the costs of a project may be provided by in-kind contributions and other noncash support.\n**(2) Waiver**\nThe Administrator may waive all or part of the requirement in paragraph (1) if the Administrator determines that\u2014\n**(A)**\nno reasonable means are available through which an eligible entity applying for a grant under this section can meet that requirement;\n**(B)**\nthe probable benefit of the project outweighs the public interest in such requirement; and\n**(C)**\nthe project undertaken is established on lands owned by or held in trust for an Indian Tribe.\n##### (e) Guidelines and criteria\nThe Administrator shall\u2014\n**(1)**\nissue guidelines for implementation of the grant program established under subsection (a); and\n**(2)**\nestablish criteria for evaluating eligible projects, based on best practices, best available science, and community engagement, to rank eligible projects under subsection (c).\n##### (f) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator $5,000,000 for each of fiscal years 2026 through 2030 to carry out this section.\n**(2) Availability to Indian Tribes**\n**(A) In general**\nOf the amount authorized to be appropriated by paragraph (1) for a fiscal year, not less than $750,000 shall be available to award grants under this section to eligible entities that are Indian Tribes.\n**(B) Contingency; outreach**\nIf no Indian Tribe is awarded a grant under this section in a fiscal year\u2014\n**(i)**\nfor that fiscal year, the amount described in subparagraph (A) shall be made available to award grants under this section to other eligible entities; and\n**(ii)**\nthe Administrator shall conduct outreach to inform Indian Tribes and organizations that work with Indian Tribes of the grant program established under subsection (a).\n##### (g) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration.\n**(2) Fishing industry**\nThe term fishing industry means\u2014\n**(A)**\nprocessors;\n**(B)**\ncommercial fishermen; and\n**(C)**\nrecreational fishermen.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given that term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(5) Kelp forest ecosystem**\nThe term kelp forest ecosystem means a naturally occurring, biotic system dominated by canopy-forming, stipitate, or prostrate benthic macroalgae and associated taxa.\n**(6) Local government**\nThe term local government means a unit of general local government, a school district, or other special district established under State law.\n**(7) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986; and\n**(B)**\nexempt from tax under section 501(a) of such Code.",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "1124",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Help Our Kelp Act of 2025",
      "type": "HR"
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
            "updateDate": "2026-01-21T19:13:20Z"
          },
          {
            "name": "Aquatic ecology",
            "updateDate": "2026-01-21T19:13:20Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-01-21T19:13:20Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-01-21T19:13:20Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-01-21T19:13:20Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-01-21T19:13:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-02T20:29:48Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s513is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Help Our Kelp Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Commerce to establish and carry out a grant program to conserve, restore, and manage kelp forest ecosystems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:38Z"
    }
  ]
}
```
