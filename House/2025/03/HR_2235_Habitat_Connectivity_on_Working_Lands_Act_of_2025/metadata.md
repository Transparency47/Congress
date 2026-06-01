# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2235
- Title: Habitat Connectivity on Working Lands Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2235
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-03-04T09:06:44Z
- Update date including text: 2026-03-04T09:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2235",
    "number": "2235",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Habitat Connectivity on Working Lands Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:44Z",
    "updateDateIncludingText": "2026-03-04T09:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:06:00Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MT"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NM"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2235ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2235\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Vasquez (for himself, Mr. Zinke , and Ms. Leger Fernandez ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to improve wildlife habitat connectivity and wildlife migration corridors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Habitat Connectivity on Working Lands Act of 2025 .\n#### 2. Conservation programs\n##### (a) Definitions\nSection 1240A of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131 ) is amended by adding at the end the following:\n(11) Habitat connectivity The term habitat connectivity means the degree to which landscape or habitat elements facilitate native species movement among seasonal habitats. (12) Big game species The term big game species means native species of large mammals including, wild deer, elk, pronghorn, wild sheep, and moose. .\n##### (b) Regional Conservation Partnership Program critical conservation areas\nSection 1271F(a)(2)(C) of the Food Security Act of 1985 ( 16 U.S.C. 3871f(a)(2)(C) ) is amended by inserting , including restoration and enhancement of wildlife habitat connectivity and wildlife migration corridors, with a focus on big game species before ; and .\n##### (c) Enrollment in the environmental quality incentives program and the conservation stewardship program of grassland enrolled in the conservation reserve program\n**(1) Environmental quality incentives program**\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended\u2014\n**(A)**\nin paragraph (6), by striking A producer and inserting Except as provided in paragraph (8), a producer ; and\n**(B)**\nby adding at the end the following:\n(8) Cost-share payments for grassland enrolled in the conservation reserve program (A) In general The Secretary may provide payments under the program for costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training with respect to eligible land that is\u2014 (i) enrolled in the conservation reserve program under section 1231(d)(2)(A); and (ii) of ecological significance, as described in section 1231(d)(2)(B)(iii). (B) Limitation A producer shall not be eligible for payments under subparagraph (A) for practices if the producer receives payments or other benefits for the same practice on the same land under another Federal program (other than the conservation reserve program under subchapter B of chapter 1). .\n**(2) Conservation stewardship program**\nSection 1240J(b) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201322(b) ) is amended\u2014\n**(A)**\nin paragraph (1), in the matter preceding subparagraph (A), by inserting and except as provided in paragraph (3), after paragraph (2), ; and\n**(B)**\nby adding at the end the following:\n(3) Cost-share payments for grassland enrolled in the conservation reserve program (A) In general The Secretary may provide payments under the program for costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training with respect to eligible land that is\u2014 (i) enrolled in the conservation reserve program under section 1231(d)(2)(A); and (ii) of ecological significance, as described in section 1231(d)(2)(B)(iii). (B) Limitation A producer shall not be eligible for payments under subparagraph (A) for conservation activities if the producer receives payments or other benefits for the same conservation activities on the same land under another Federal program (other than the conservation reserve program under subchapter B of chapter 1). (C) Emergency grazing and haying access preserved No priority resource concern, practice, or incentive pertaining to restoration and enhancement of wildlife habitat connectivity and wildlife migration corridors on the acres described above will prevent or alter emergency grazing and haying access for grassland acres enrolled in the conservation reserve program. .\n**(3) Payment limitation for rental payments under the conservation reserve program**\nSection 1234(g)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3834(g)(1) ) is amended by striking $50,000 and inserting $125,000 .\n##### (d) Increased payments under the environmental quality incentives program\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended\u2014\n**(1)**\nin paragraph (3)(F), by inserting and wildlife habitat connectivity before ; or ; and\n**(2)**\nin paragraph (7)(A)\u2014\n**(A)**\nin clause (iii), by striking or at the end;\n**(B)**\nin clause (iv), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(v) addresses the conservation and restoration of wildlife habitat, including wildlife habitat connectivity and wildlife migration corridors. .\n##### (e) Conservation practice standards\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended by adding at the end the following:\n(j) Addressing barriers to habitat connectivity (1) In general The Secretary shall\u2014 (A) to the maximum extent practicable, fully incorporate nonstructural methods to control livestock distribution, such as virtual fencing, into the conservation practice standards; and (B) provide for the appropriate range of conservation practices and resource mitigation measures available to landowners using nonstructural methods described in subparagraph (A). (2) Availability of adequate technical assistance The Secretary shall ensure that adequate technical assistance is available for the implementation of\u2014 (A) nonstructural methods described in paragraph (1)(A); and (B) other practices that support habitat connectivity (as that term is defined in section 1240A) through Federal conservation programs. .\n##### (f) Administrative requirements for conservation programs\nSection 1244 of the Food Security Act of 1985 ( 16 U.S.C. 3844 ) is amended by adding at the end the following:\n(q) Encouragement of habitat connectivity and big game corridors In carrying out any conservation program administered by the Secretary, the Secretary may, as appropriate, encourage\u2014 (1) the conservation of landscape corridors and hydrologic connectivity, where native big game species (as that term is defined in section 1240A) and ecological processes can transition from one habitat to another, in order to conserve native biodiversity and ensure resiliency against impacts from a range of stressors; and (2) the use of conservation practices that support the development, restoration, and maintenance of landscape corridors and hydrologic connectivity. .\n#### 3. High-priority research and extension areas\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Virtual fencing Research and extension grants may be made under this section for the purposes of\u2014 (A) understanding and addressing the barriers to the adoption of virtual fencing technology; and (B) studying the effects of virtual fencing technology on natural and cultural resources, such as\u2014 (i) sensitive riparian areas; and (ii) crucial winter range and stopover habitats for native big game species (as that term is defined in section 1240A of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131 )). .",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-05-06T17:01:36Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2235ih.xml"
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
      "title": "Habitat Connectivity on Working Lands Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Habitat Connectivity on Working Lands Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to improve wildlife habitat connectivity and wildlife migration corridors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:21Z"
    }
  ]
}
```
