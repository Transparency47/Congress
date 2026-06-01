# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/403
- Title: Preventing Our Next Natural Disaster Act
- Congress: 119
- Bill type: HR
- Bill number: 403
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2025-10-09T08:05:31Z
- Update date including text: 2025-10-09T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-15 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-15 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/403",
    "number": "403",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001193",
        "district": "14",
        "firstName": "Eric",
        "fullName": "Rep. Swalwell, Eric [D-CA-14]",
        "lastName": "Swalwell",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Preventing Our Next Natural Disaster Act",
    "type": "HR",
    "updateDate": "2025-10-09T08:05:31Z",
    "updateDateIncludingText": "2025-10-09T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-15T15:35:54Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "DC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "HI"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 403\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Swalwell introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo enhance predisaster mitigation to prevent future natural disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Our Next Natural Disaster Act .\n#### 2. Definitions\nSection 203(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133(a) ) is amended to read as follows:\n(a) Definitions In this section, the following definitions apply: (1) High hazard risk The term high hazard risk means high rating of a natural hazard risk according to a tool such as the National Risk Index or another tool developed by the Federal Emergency Management Agency. (2) Environmental justice community The term environmental justice community means a community primarily composed of communities of color, low-income communities, or Tribal and indigenous communities, that experiences, or is at risk of experiencing, higher or more adverse human health or environmental effects than most communities. (3) Small impoverished community The term small impoverished community means a community that is comprised of 50,000 or fewer individuals and that is economically disadvantaged, as determined by the State in which the community is located and based on criteria established by the President. .\n#### 3. Technical assistance\nSection 203(e) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133(e) ) is amended by adding at the end the following:\n(3) Guidance The Administrator may develop guidance regarding how to incorporate climate change into\u2014 (A) the National Risk Index; (B) cost-benefit analyses; and (C) adopting improved relevant consensus-based codes, specifications, and standards to address natural hazards. (4) Building, restoration, or rehabilitation The Administrator may issue guidance to ensure that funds provided under this section are used to support the building, restoration, or rehabilitation of hazard mitigation projects that are\u2014 (A) planned and designed around the future projections of climate change over the life cycle of the project; and (B) built to withstand future flooding, wildfires, or other natural disasters. .\n#### 4. Criteria for assistance awards\nSection 203(g) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133(g) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (11);\n**(2)**\nby redesignating paragraph (12) as paragraph (13); and\n**(3)**\nby inserting after paragraph (11) the following:\n(12) and prioritize communities that are in high hazard risk communities, environmental justice communities, communities with low tax revenue base per capita, and communities with a low rate of code adoption and enforcement and infrastructure maintenance expenditures (the Administrator of the Federal Emergency Management Agency shall establish guidelines to develop measurable criteria to determine such priority for high hazard risk communities and integrate the data into a tool such as the National Risk Index and use the Resilience Analysis and Planning Tool to help target the communities with the greatest need of assistance); and .\n#### 5. Federal share\nSection 203(h)(2)) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133(h)(2) ) is amended to read as follows:\n(2) Small impoverished communities and environment justice communities Notwithstanding paragraph (1), the President may contribute up to 90 percent of the total cost of a mitigation activity carried out in a small impoverished community or an environmental justice community. .\n#### 6. National public infrastructure predisaster mitigation assistance\nSection 203(i)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133(i)(1) ) is amended\u2014\n**(1)**\nby striking 6 percent and inserting 15 percent ; and\n**(2)**\nby adding at the end the following: From such total amount made available from the Disaster Relief Fund, with respect to each major disaster, the President may set aside 2 percent of the estimated aggregate amount of the grants to be made pursuant to sections 403, 406, 407, 408, 410, 416, and 428 for the major disaster for community planning and capacity building assistance. .\n#### 7. Community outreach\nSection 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ) is amended by adding at the end the following:\n(m) Community outreach assistance The Administrator of the Federal Emergency Management Agency, in collaboration with organizations, such as the United States Cooperative Extension System and the Extension Disaster Education Network, shall provide community outreach to communities under this section, with a goal of increasing applications from communities with high hazard risk, environmental justice communities, communities with low tax revenue base per capita, and communities with a low rate of code adoption and enforcement and infrastructure maintenance expenditures, regarding how to plan and prioritize projects based on current climate conditions, future hazard risk, and social vulnerability assessments as well as how to successfully develop, submit, and administer a grant under this section. .\n#### 8. Improved data collection\nNot later than 3 years after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall establish a central Federal database at the Agency, in coordination with the Department of Housing and Urban Development, the Environment Protection Agency, the Economic Development Administration, the Small Business Administration, the Army Corps of Engineers, and any other relevant agencies the Administrator chooses to include, to consolidate funding data collected by all local, State, and Federal agencies involved in post-disaster response and predisaster mitigation spending and categorize the data by type of project, funding source, and hazard types using an user friendly database and interactive map. Such database shall also include\u2014\n**(1)**\nthe collection and posting of census track data and post aggregate demographic data, pursuant to the Paperwork Reduction Act ( 44 U.S.C. 3501 et seq. ) as well as any future guidance by such office on data equity on the impact of natural disaster and Federal recovery efforts to better allocate and trace funds; and\n**(2)**\npost-project evaluations by the Agency to analyze disaster spending and report findings on what may have been saved by proper predisaster mitigation.",
      "versionDate": "2025-01-14",
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
        "name": "Emergency Management",
        "updateDate": "2025-02-26T21:10:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr403",
          "measure-number": "403",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr403v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preventing Our Next Natural Disaster Act</strong></p><p>This bill modifies the Building Resilient Infrastructure and Communities (BRIC) grant program of the Federal Emergency Management Agency (FEMA).</p><p>Specifically, the bill</p><ul><li>increases the amount that may be set aside from FEMA's Disaster Relief Fund for BRIC from 6% to 15% of certain disaster grant amounts;</li><li>authorizes FEMA to set aside 2% from the BRIC 15% set-aside for assistance with community planning and capacity building;</li><li>provides a 90% federal cost share for BRIC grants to environmental justice communities, and increases the maximum number of people in small impoverished communities, which are also eligible for the 90% BRIC federal cost share; and</li><li>authorizes FEMA to develop guidance regarding how to incorporate climate change into the National Risk Index, benefit-cost analyses, and improved codes, specifications, and standards to address natural hazards.</li></ul><p>FEMA must</p><ul><li>prioritize BRIC assistance for high hazard risk communities, environmental justice communities, communities with low tax revenue base per capita, and communities with a low rate of code adoption and enforcement and infrastructure maintenance expenditures;</li><li>provide community outreach on project planning and grant administration; and</li><li>establish a central federal database to consolidate funding data collected by all local, state, and federal agencies involved in post-disaster response and pre-disaster mitigation spending and categorize the data by type of project, funding source, and hazard types using a user-friendly database and interactive map.</li></ul>"
        },
        "title": "Preventing Our Next Natural Disaster Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr403.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Our Next Natural Disaster Act</strong></p><p>This bill modifies the Building Resilient Infrastructure and Communities (BRIC) grant program of the Federal Emergency Management Agency (FEMA).</p><p>Specifically, the bill</p><ul><li>increases the amount that may be set aside from FEMA's Disaster Relief Fund for BRIC from 6% to 15% of certain disaster grant amounts;</li><li>authorizes FEMA to set aside 2% from the BRIC 15% set-aside for assistance with community planning and capacity building;</li><li>provides a 90% federal cost share for BRIC grants to environmental justice communities, and increases the maximum number of people in small impoverished communities, which are also eligible for the 90% BRIC federal cost share; and</li><li>authorizes FEMA to develop guidance regarding how to incorporate climate change into the National Risk Index, benefit-cost analyses, and improved codes, specifications, and standards to address natural hazards.</li></ul><p>FEMA must</p><ul><li>prioritize BRIC assistance for high hazard risk communities, environmental justice communities, communities with low tax revenue base per capita, and communities with a low rate of code adoption and enforcement and infrastructure maintenance expenditures;</li><li>provide community outreach on project planning and grant administration; and</li><li>establish a central federal database to consolidate funding data collected by all local, state, and federal agencies involved in post-disaster response and pre-disaster mitigation spending and categorize the data by type of project, funding source, and hazard types using a user-friendly database and interactive map.</li></ul>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr403"
    },
    "title": "Preventing Our Next Natural Disaster Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Our Next Natural Disaster Act</strong></p><p>This bill modifies the Building Resilient Infrastructure and Communities (BRIC) grant program of the Federal Emergency Management Agency (FEMA).</p><p>Specifically, the bill</p><ul><li>increases the amount that may be set aside from FEMA's Disaster Relief Fund for BRIC from 6% to 15% of certain disaster grant amounts;</li><li>authorizes FEMA to set aside 2% from the BRIC 15% set-aside for assistance with community planning and capacity building;</li><li>provides a 90% federal cost share for BRIC grants to environmental justice communities, and increases the maximum number of people in small impoverished communities, which are also eligible for the 90% BRIC federal cost share; and</li><li>authorizes FEMA to develop guidance regarding how to incorporate climate change into the National Risk Index, benefit-cost analyses, and improved codes, specifications, and standards to address natural hazards.</li></ul><p>FEMA must</p><ul><li>prioritize BRIC assistance for high hazard risk communities, environmental justice communities, communities with low tax revenue base per capita, and communities with a low rate of code adoption and enforcement and infrastructure maintenance expenditures;</li><li>provide community outreach on project planning and grant administration; and</li><li>establish a central federal database to consolidate funding data collected by all local, state, and federal agencies involved in post-disaster response and pre-disaster mitigation spending and categorize the data by type of project, funding source, and hazard types using a user-friendly database and interactive map.</li></ul>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr403"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr403ih.xml"
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
      "title": "Preventing Our Next Natural Disaster Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Our Next Natural Disaster Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance predisaster mitigation to prevent future natural disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T07:18:36Z"
    }
  ]
}
```
