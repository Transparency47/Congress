# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3707
- Title: NSF and USDA Interagency Research Act
- Congress: 119
- Bill type: HR
- Bill number: 3707
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-05-21T20:43:08Z
- Update date including text: 2026-05-21T20:43:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3707",
    "number": "3707",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "NSF and USDA Interagency Research Act",
    "type": "HR",
    "updateDate": "2026-05-21T20:43:08Z",
    "updateDateIncludingText": "2026-05-21T20:43:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-04T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3707ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3707\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Baird (for himself and Ms. Salinas ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Agriculture and the Director of the National Science Foundation to carry out cross-cutting and collaborative research and development activities focused on the joint advancement of Department of Agriculture and National Science Foundation mission requirements and priorities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NSF and USDA Interagency Research Act .\n#### 2. Department of Agriculture and National Science Foundation research and development coordination\n##### (a) In general\nThe Secretary of Agriculture (in this section referred to as the Secretary ) and the Director of the National Science Foundation (in this section referred to as the Director ) shall carry out cross-cutting and collaborative research and development activities focused on the joint advancement of Department of Agriculture and National Science Foundation mission requirements and priorities.\n##### (b) Memoranda of understanding\nThe Secretary and the Director shall coordinate the activities under subsection (a) through the establishment of memoranda of understanding or other appropriate interagency agreements. Such memoranda or agreements, as the case may be, shall require the use of a competitive, merit review process, as appropriate. Such activities may include components proposed by Federal agencies, institutions of higher education, nonprofit institutions, and other appropriate entities, as determined appropriate under the memoranda or agreements.\n##### (c) Coordination\nIn carrying out the activities under subsection (a), the Secretary and the Director may carry out the following:\n**(1)**\nConduct collaborative research in a variety of focus areas, such as the following:\n**(A)**\nPlant, animal, and microbial biology relevant to agricultural challenges.\n**(B)**\nFood and nutrition security.\n**(C)**\nRural economic revitalization.\n**(D)**\nCyber-physical systems.\n**(E)**\nSmart and connected communities.\n**(F)**\nAdvanced sensors and models of soil and plant processes.\n**(G)**\nNano-biosensing and analytical technologies to improve food safety, water quality, biosecurity, plant and animal diseases, and soil health.\n**(H)**\nMonitoring of food- or water-borne pathogens, allergens, and accidental, natural, or intentional bio- or chemical contaminants.\n**(I)**\nKey emerging technology areas, such as artificial intelligence, machine learning, automation, robotics, digital agriculture, distributed ledger technologies (including blockchain), and information and communication technology for agricultural uses.\n**(J)**\nDevelopment and testing of new precision agriculture tools.\n**(K)**\nWorkforce needs, education, and development.\n**(2)**\nPromote collaboration, open community-based development, and data and information sharing between Federal agencies, institutions of higher education, community colleges, area career and technical education schools, nonprofit institutions, and other appropriate entities by providing the necessary access and secure data and information transfer capabilities.\n**(3)**\nSupport research infrastructure, including new facilities, equipment, and broadband deployment, as the Secretary and Director determine necessary.\n**(4)**\nDevelop translational technologies for commercial utilization.\n**(5)**\nOrganize education, training, and research initiatives relating to STEM education and workforce development, which may include the following:\n**(A)**\nActivities supported by the Cooperative Extension System.\n**(B)**\nIndustrial partnership programs.\n**(C)**\nWorkshops for educating preschool through grade 12 teachers on how to increase agricultural literacy.\n**(D)**\nDevelopment of agricultural-based science curricula for kindergarten through grade 12 students.\n**(E)**\nDistribution of resources for educators to implement curricula, such as the workshops referred to in subparagraph (C).\n**(6)**\nAward grants to institutions of higher education, community colleges, area career and technical education schools, or eligible nonprofit institutions (or consortia thereof), to establish a Center for Agricultural Research, Education, and Workforce Development.\n**(7)**\nFacilitate relationships between public and private sector entities to carry out the activities specified in paragraphs (1) through (6) upon the termination of any memoranda of understanding or other appropriate interagency agreement entered into under subsection (b).\n##### (d) Agreements\nIn carrying out the activities under subsection (a), the Secretary and the Director are authorized to\u2014\n**(1)**\ncarry out reimbursable agreements between the Department of Agriculture, the National Science Foundation, and other entities in order to maximize the effectiveness of research and development; and\n**(2)**\ncollaborate with other Federal agencies, as appropriate.\n##### (e) Report\nNot later than two years after the date of the enactment of this Act, the Secretary and the Director shall submit to the appropriate committees of Congress a report detailing the following:\n**(1)**\nInteragency coordination between each Federal agency involved in the research and development activities carried out under this section.\n**(2)**\nPotential opportunities to expand the technical capabilities of the Department of Agriculture and the National Science Foundation.\n**(3)**\nCollaborative research achievements.\n**(4)**\nAreas of future mutually beneficial successes.\n**(5)**\nContinuation of coordination activities between the Department and the Foundation.\n##### (f) Research security\nThe activities authorized under this section shall be applied in a manner consistent with subtitle D of title VI of the Research and Development, Competition, and Innovation Act (enacted as division B of Public Law 117\u2013167 ; 42 U.S.C. 19231 et seq. ; popularly referred to as the CHIPS and Science Act ).\n##### (g) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means each of the following committees:\n**(A)**\nThe Committee on Agriculture of the House of Representatives.\n**(B)**\nThe Committee on Science, Space, and Technology of the House of Representatives.\n**(C)**\nThe Committee on Commerce, Science, and Transportation of the Senate.\n**(D)**\nThe Committee on Agriculture, Nutrition, and Forestry of the Senate.\n**(2) Area career and technical education school**\nThe term area career and technical education school has the meaning given such term in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ).\n**(3) Community college**\nThe term community college has the meaning given such term in section 3167B of the Department of Energy Science Education Enhancement Act ( 42 U.S.C. 7381c\u20133 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).",
      "versionDate": "2025-06-04",
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
        "actionDate": "2026-04-27",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Energy and Commerce, Agriculture, Oversight and Government Reform, Education and Workforce, the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Leadership in AI Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-06-18T13:42:43Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3707ih.xml"
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
      "title": "NSF and USDA Interagency Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-06T04:23:18Z"
    },
    {
      "title": "NSF and USDA Interagency Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-06T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture and the Director of the National Science Foundation to carry out cross-cutting and collaborative research and development activities focused on the joint advancement of Department of Agriculture and National Science Foundation mission requirements and priorities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-06T04:18:18Z"
    }
  ]
}
```
