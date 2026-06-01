# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1459
- Title: Protect the West Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1459
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-12-05T21:57:36Z
- Update date including text: 2025-12-05T21:57:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1459",
    "number": "1459",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Protect the West Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:57:36Z",
    "updateDateIncludingText": "2025-12-05T21:57:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
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
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:40:17Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:31:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1459ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1459\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Crow introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish an Outdoor Restoration Fund for restoration and resilience projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect the West Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Council**\nThe term Council means the Restoration Fund Advisory Council established by section 4(a).\n**(2) Covered authority**\nThe term covered authority means\u2014\n**(A)**\nthe good neighbor authority established by section 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a );\n**(B)**\nthe Water Source Protection Program under section 303 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6542 );\n**(C)**\nthe Watershed Condition Framework established under section 304 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6543 );\n**(D)**\nthe stewardship end result contracting program under section 604 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591c );\n**(E)**\nthe Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2101 et seq. );\n**(F)**\nthe Joint Chiefs' Landscape Restoration Partnership program;\n**(G)**\nthe Watershed Protection and Flood Prevention Act ( 16 U.S.C. 1001 et seq. );\n**(H)**\nthe emergency watershed protection program established under section 403 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2203 );\n**(I)**\nthe Collaborative Forest Landscape Restoration Program established under section 4003 of Public Law 111\u201311 ( 16 U.S.C. 7303 );\n**(J)**\nthe legacy roads and trails program of the Department of Agriculture;\n**(K)**\nthe working lands for wildlife program of the Department of Agriculture; and\n**(L)**\na conservation program under title XII of the Food Security Act of 1985 ( 16 U.S.C. 3801 et seq. ), including the Regional Conservation Partnership program under subtitle I of that title ( 16 U.S.C. 3871 et seq. ).\n**(3) Ecological integrity**\nThe term ecological integrity has the meaning given the term in section 219.19 of title 36, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(4) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State agency;\n**(B)**\na unit of local government;\n**(C)**\na Tribal government;\n**(D)**\na regional government or quasi-governmental organization;\n**(E)**\na special district; or\n**(F)**\na nonprofit organization.\n**(5) Fund**\nThe term Fund means the Outdoor and Watershed Restoration Fund established by section 3(a).\n**(6) Grant program**\nThe term grant program means the restoration and resilience grant program established by section 5(b).\n**(7) Restoration**\nThe term restoration has the meaning given the term in section 219.19 of title 36, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(8) Restoration and resilience project**\nThe term restoration and resilience project means a project carried out on Federal land, non-Federal land, or both, that is designed in accordance with the best available science to conduct restoration that measurably improves\u2014\n**(A)**\nforest conditions;\n**(B)**\nrangeland and native grassland health;\n**(C)**\nwatershed function; or\n**(D)**\nwildlife habitat.\n**(9) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(10) Wildland-urban interface**\nThe term wildland-urban interface has the meaning given the term in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 ).\n#### 3. Outdoor and Watershed Restoration Fund\n##### (a) Establishment\nThere is established in the Treasury an Outdoor and Watershed Restoration Fund.\n##### (b) Purpose\nThe purpose of the Fund is to provide funding for the grant program and the Restoration and Resilience Partnership Program under section 6.\n##### (c) Use\nAmounts in the Fund shall be used by the Secretary through a transparent process\u2014\n**(1)**\nin coordination with the Council, to carry out the grant program; and\n**(2)**\nto carry out the Restoration and Resilience Partnership Program under section 6.\n##### (d) Savings provisions\n**(1) Complementary programs**\nActivities carried out under this Act shall complement, not duplicate or replace, existing Federal conservation, restoration, and resilience programs.\n**(2) Applicable law**\nA restoration and resilience project on Federal land or non-Federal land developed or implemented using amounts provided under this Act shall be carried out in accordance with applicable law and available authorities.\n##### (e) Supplement, not supplant\nAmounts provided under this Act shall supplement, not supplant, any Federal, State, or other funds otherwise made available to an eligible entity for activities described in this Act.\n##### (f) Interagency flexibility and leverage\nTo facilitate interagency cooperation and enhance the speed and scale of results of activities carried out using amounts in the Fund\u2014\n**(1)**\nmatching funds or cost-sharing requirements of a covered authority may be satisfied through the contribution of funding from\u2014\n**(A)**\n1 or more other covered authorities; or\n**(B)**\nfunds appropriated under section 8; and\n**(2)**\nthe Secretary shall modify, expand, or streamline eligibility and verification criteria for covered authorities to maximize flexibility, speed, and use of Federal funds in the most effective manner to achieve outcomes of activities using amounts in the Fund.\n##### (g) Pay-for-Performance contract authority\nIn using amounts in the Fund, the Secretary may use a contract, grant agreement, or fixed amount award to purchase successfully implemented restoration and resilience project outcomes from qualifying projects, as determined by the Secretary, at a negotiated per-unit price.\n##### (h) Acceptance and use of contributions\n**(1) In general**\nThe Secretary of the Treasury, or a designee, may establish in the Treasury an account to accept contributions of non-Federal funds for the Fund.\n**(2) Deposit and use of contributions**\nContributions of non-Federal funds received for the Fund shall be\u2014\n**(A)**\ndeposited into the account established under paragraph (1); and\n**(B)**\navailable to the Secretary, without further appropriation and until expended, to carry out activities described in subsection (c).\n##### (i) Oversight\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Inspector General of the Department of Agriculture shall prepare and submit to the Committees on Agriculture, Nutrition, and Forestry and Appropriations of the Senate and the Committees on Agriculture, Natural Resources, and Appropriations of the House of Representatives a report describing the use, and any abuse or misuse, as applicable, of the Fund by the Secretary with respect to\u2014\n**(1)**\nthe grant program; and\n**(2)**\nthe Restoration and Resilience Partnership Program established by section 6.\n#### 4. Restoration Fund Advisory Council\n##### (a) Establishment\nThere is established a Restoration Fund Advisory Council to provide recommendations to the Secretary with respect to\u2014\n**(1)**\nthe disbursement of amounts from the Fund for the grant program;\n**(2)**\npriority-setting for landscapes; and\n**(3)**\nevaluation and monitoring for restoration and resilience project success.\n##### (b) Membership\nThe Council shall be composed of\u2014\n**(1)**\nthe Secretary;\n**(2)**\n12 members, to be appointed by the Secretary, of whom\u2014\n**(A)**\n3 shall be representatives from resource-dependent industries, including the agriculture, oil and gas, outdoor recreation, or forest products industries;\n**(B)**\n3 shall be national experts from each of the fields of natural resource restoration, economic development, and community and climate resilience;\n**(C)**\n3 shall be representatives of conservation, wildlife, or watershed organizations;\n**(D)**\n1 shall be a representative of State government;\n**(E)**\n1 shall be a representative of a unit of local government; and\n**(F)**\n1 shall be a representative of a Tribal government; and\n**(3)**\nas determined to be necessary by the Secretary, not more than 3 representatives from other Federal agencies.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the Council, shall submit to the Committee on Agriculture, Nutrition, and Forestry and the Committee on Appropriations of the Senate and the Committee on Agriculture, the Committee on Natural Resources, and the Committee on Appropriations of the House of Representatives a report describing\u2014\n**(1)**\nthe status of any restoration and resilience projects that received amounts from the Fund, including\u2014\n**(A)**\nenvironmental and climate benefits;\n**(B)**\nrestoration achievements;\n**(C)**\nattainment of restoration and habitat improvement objectives;\n**(D)**\njobs created and retained;\n**(E)**\nthe growth in outdoor industries that provide capacity to carry out restoration and resilience projects; and\n**(F)**\nprogress towards State-, Tribal-, and community-level resilience goals; and\n**(2)**\nrecommendations to improve coordination, align Federal, State, or Tribal resources or existing authorities, and expand workforce capacity in outdoor industries that provide capacity to carry out restoration and resilience projects through legislative and administrative changes.\n#### 5. Restoration and resilience grant program\n##### (a) Purposes\nThe purposes of this section are\u2014\n**(1)**\nto increase the capacity for\u2014\n**(A)**\nplanning, coordinating, and monitoring restoration and resilience projects on non-Federal land; and\n**(B)**\nproviding support for collaboration and monitoring on Federal land; and\n**(2)**\nto support, on non-Federal land\u2014\n**(A)**\nrestoration and resilience projects;\n**(B)**\nefforts to improve wildfire resistive construction and reduce risks within the home ignition zone; and\n**(C)**\nprojects to expand equitable outdoor access.\n##### (b) Establishment\nThere is established a restoration and resilience grant program, to be administered by the Secretary, with the guidance of the Council, to provide grants or pay-for-performance contracts from the Fund to eligible entities for the purposes described in subsection (a).\n##### (c) Regional coordination\nThe Secretary and the Council shall, to the maximum extent practicable\u2014\n**(1)**\nseek input from and coordinate with State or regional efforts, initiatives, and partnerships to restore ecological integrity on Federal land and non-Federal land; and\n**(2)**\ncomplement or support existing State or regional efforts, initiatives, and partnerships to restore ecological integrity on Federal land and non-Federal land.\n##### (d) Use of funds\n**(1) In general**\nThe Secretary shall use amounts in the Fund to provide capacity grants or pay-for-performance contracts under paragraph (2) and implementation grants or pay-for-performance contracts under paragraph (3).\n**(2) Capacity grants**\n**(A) In general**\nCapacity grants or pay-for-performance contracts shall be made available to eligible entities for the purpose described in subsection (a)(1).\n**(B) Application**\n**(i) In general**\nA grant or pay-for-performance contract under this paragraph may only be made to an eligible entity that submits to the Secretary an application at such time, in such manner, and containing or accompanied by such additional information as the Secretary, in consultation with the Council, may require, including the information required under clause (ii).\n**(ii) Contents**\nAn application submitted under clause (i) shall contain\u2014\n**(I)**\na clear and concise expression of interest;\n**(II)**\nan explanation for how funds would complement existing Federal funds;\n**(III)**\na description of how the proposed planning, coordinating, or monitoring of restoration and resilience projects would be carried out in accordance with the best available ecological restoration science; and\n**(IV)**\nan estimate of the number and duration of jobs that provide capacity to carry out restoration and resilience projects that would be created, or sustained, with the funds.\n**(C) Condition**\nTo the maximum extent practicable, the Secretary shall provide grant-writing training and mentoring opportunities for lower-capacity, less collaborative experience, or underserved communities and organizations to help lower the barriers to participation in, and create more inclusion in and opportunities under, the grant program.\n**(3) Implementation grants**\n**(A) In general**\nImplementation grants or pay-for-performance contracts shall be made available to eligible entities for the purpose described in subsection (a)(2).\n**(B) Application**\nA grant or pay-for-performance contract under this paragraph may be made only to an eligible entity that submits to the Secretary an application at such time, in such manner, and containing or accompanied by such information as the Secretary, in consultation with the Council, may require.\n**(C) Waiver**\nThe Secretary may waive matching requirements under covered authorities for applicants for grants or pay-for-performance contracts under this paragraph representing lower-capacity, less collaborative experience, or underserved communities and organizations and rural communities.\n##### (e) Priority\nIn carrying out the grant program, the Secretary, in consultation with the Council, shall give priority to projects that would\u2014\n**(1)**\ncreate or sustain jobs, employ local or regional labor, or expand the outdoor workforce to provide capacity to carry out restoration and resilience projects or equitable outdoor access through training and education programs;\n**(2)**\nbe developed through a collaborative process, relying on the best available social ecological restoration science, with multiple stakeholders representing diverse interests;\n**(3)**\naddress shared priorities for Federal and non-Federal partners;\n**(4)**\nadvance State, local, and Tribal plans relating to forests, water, wildlife, or equitable outdoor access;\n**(5)**\nutilize watershed data analytics to quantify, prioritize, and measure expected outcomes from proposed restoration activities;\n**(6)**\nbe carried out by or in lower-capacity, less collaborative experience, or underserved communities and organizations; or\n**(7)**\nimprove long-term economic security in the geographic region through restoration and resilience projects, equitable outdoor access, and the indirect benefits of those projects and access, particularly in geographic regions transitioning from fossil-fuel extraction.\n##### (f) Authorities\nEligible entities may use existing authorities when carrying out a restoration and resilience project, including a covered authority.\n#### 6. Restoration and resilience partnership program\n##### (a) Purposes\nThe purposes of this section are\u2014\n**(1)**\nto restore and improve the ecological integrity of forest, grassland, and rangeland ecosystems across the United States in partnership with State, local, and Tribal governments;\n**(2)**\nto create or sustain outdoor jobs by reducing the backlog of restoration and resilience projects on Federal land and non-Federal land;\n**(3)**\nto improve the resilience and carrying capacity of rangelands in the United States by preventing or mitigating invasive species, such as cheatgrass, that contribute to rangeland fire; and\n**(4)**\nto reduce uncharacteristic wildfires in the highest risk areas of the United States by carrying out, in accordance with applicable law, restoration and resilience projects.\n##### (b) Establishment\nThere is established a Restoration and Resilience Partnership Program, under which the Secretary shall carry out restoration and resilience projects in partnership areas designated under subsection (c)(1).\n##### (c) Designation of partnership areas\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Secretary shall designate, for the purposes of carrying out restoration and resilience projects under subsection (e), any areas of Federal land and non-Federal land that the Secretary determines to be appropriate.\n**(2) Submission of partnership areas by States and Tribes**\n**(A) In general**\nThe Governor of a State or an authorized representative of an Indian Tribe may submit to the Secretary, in writing, a request to designate certain Federal land or non-Federal land in the State or Indian Country, respectively, for restoration and resilience projects under subsection (e).\n**(B) Inclusions**\nA written request submitted under subparagraph (A) may include 1 or more maps or recommendations.\n##### (d) Requirements\nTo be eligible for designation under subsection (c), an area shall\u2014\n**(1)**\nhave a high or very high wildfire potential as determined by\u2014\n**(A)**\nthe map of the Forest Service entitled Wildfire Hazard Potential Version 2020 ;\n**(B)**\nany other mapping resource or data source approved by the Secretary that depicts the risk of wildfires; or\n**(C)**\nfire-risk assessment resources or mapping tools maintained by the applicable State;\n**(2)**\nhave high-priority wildlife habitat urgently in need of restoration, as determined by the Secretary, in consultation with eligible entities and the applicable Governor or representative of an Indian Tribe; or\n**(3)**\nin the case of Federal land, be in the wildland-urban interface.\n##### (e) Restoration and resilience projects\n**(1) In general**\nSubject to paragraphs (2) and (3), the Secretary shall carry out restoration and resilience projects on land designated under subsection (c).\n**(2) Priority**\nThe Secretary shall give priority to restoration and resilience projects that would\u2014\n**(A)**\nfocus on the reintroduction of characteristic, low-intensity fire in frequent fire regime ecosystems;\n**(B)**\nreduce hazardous fuels by focusing on small-diameter trees, thinning, and strategic fuel breaks;\n**(C)**\nmaximize the retention of old and large trees, as appropriate for the forest type;\n**(D)**\nmeasurably improve habitat conditions for at-risk wildlife;\n**(E)**\nmeasurably improve water quality or water quantity outcomes in waterways that flow through and out of priority areas;\n**(F)**\nestablish plans for measuring project success and environmental outcomes;\n**(G)**\npromote community and homeowner involvement in planning and implementing actions to mitigate the risk posed by wildfire in the wildland-urban interface;\n**(H)**\nemphasize proactive wildfire risk mitigation actions in the wildland-urban interface; and\n**(I)**\nincrease fire adaption in communities located within the wildland-urban interface.\n**(3) Coordination**\nThe Secretary shall carry out restoration and resilience projects under this subsection\u2014\n**(A)**\non Federal land, in coordination with the Secretary of the Interior, as applicable; and\n**(B)**\non non-Federal land, in coordination with eligible entities and other relevant stakeholders, as determined by the Secretary.\n**(4) Requirements**\n**(A) In general**\nA restoration and resilience project shall be carried out in accordance with\u2014\n**(i)**\nin the case of a restoration and resilience project carried out on Federal land, the management objectives of an applicable land or resource management plan; and\n**(ii)**\napplicable law.\n**(B) Inclusions**\nThe Secretary may use existing authorities when carrying out a restoration and resilience project on land designated under subsection (c), including any covered authority.\n**(C) Exclusions**\nA restoration and resilience project may not be carried out\u2014\n**(i)**\nin a wilderness area or designated wilderness study area;\n**(ii)**\nto construct a permanent road or trail;\n**(iii)**\non any Federal land on which, by an Act of Congress or Presidential proclamation, the removal of vegetation is restricted or prohibited;\n**(iv)**\nin an inventoried roadless area or comparable roadless area defined by a State-specific rule; or\n**(v)**\nto remove old growth stands (as defined in section 102(e)(1) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6512(e)(1) )).\n#### 7. Oversight\nNot later than 60 days after the date of enactment of this Act, the Secretary shall submit to Congress a report that, with respect to funding made available by the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 429) or Public Law 117\u2013169 (commonly known as the Inflation Reduction Act of 2022 ) for purposes of forestry\u2014\n**(1)**\nexplains the methodology for priority landscapes set by the Secretary;\n**(2)**\ndescribes the metrics the Secretary is using for measuring performance and outcomes; and\n**(3)**\ndescribes the allocation of funds to States, forests, and Indian Tribes.\n#### 8. Funding\n##### (a) In general\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, $60,000,000,000 for the Fund, to remain available until expended, of which\u2014\n**(1)**\n$20,000,000,000 shall be for the grant program; and\n**(2)**\n$40,000,000,000 shall be for the Restoration and Resilience Partnership Program under section 6, of which not less than $20,000,000,000 shall be for the conduct of restoration and resilience projects on Federal land under that section.\n##### (b) Workforce needs and expenses\nFunds made available under subsection (a)(2) shall be available for staffing, salary, and other workforce needs and expenses relating to the administration of the Restoration and Resilience Partnership Program under section 6.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "670",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protect the West Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-09T21:13:16Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1459ih.xml"
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
      "title": "Protect the West Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect the West Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an Outdoor Restoration Fund for restoration and resilience projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:31Z"
    }
  ]
}
```
