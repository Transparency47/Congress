# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1514
- Title: Mississippi River Basin Fishery Commission Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1514
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-02-04T09:06:45Z
- Update date including text: 2026-02-04T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1514",
    "number": "1514",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Mississippi River Basin Fishery Commission Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T09:06:45Z",
    "updateDateIncludingText": "2026-02-04T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-19T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-12T21:43:20Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "LA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "IL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MS"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "WI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1514ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1514\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Ezell (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Mississippi River Basin Fishery Commission, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Mississippi River Basin Fishery Commission Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nSec. 4. Establishment of Mississippi River Basin Fishery Commission.\nSec. 5. Commission governance.\nSec. 6. Commission management duties.\nSec. 7. Commission grant program.\nSec. 8. Nonbinding authority.\nSec. 9. Withdrawal from the Commission.\nSec. 10. Report to Congress.\nSec. 11. Appropriations.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nManagement of the inland fishery resources of the Mississippi River Basin are shared by 31 States, multiple Federal agencies, and 2 Canadian provinces.\n**(2)**\nThe Mississippi River Basin is the fourth largest watershed in the world, and the largest watershed in the Nation, draining all or part of 31 States and 2 Canadian provinces. The watershed measures approximately 1,200,000 square miles, and covers 41 percent of the continental United States.\n**(3)**\nThe Mississippi River and its tributaries comprise 1 of the largest and most valuable ecosystems in the world.\n**(4)**\nThe Mississippi River Basin supports economically and culturally significant subsistence, commercial, and recreational fisheries.\n**(5)**\nStates within the Mississippi River Basin have formed multiple regional interstate partnerships, and 1 basin-wide partnership, to promote cooperation and communication among the conservation agencies to manage the interjurisdictional fishery resources of the basin. Twenty-eight Mississippi River Basin State fishery agencies, the United States Fish and Wildlife Service, the Bureau of Reclamation, the United States Geological Survey, the Tennessee Valley Authority, the Chippewa-Cree Tribe, and the Chickasaw Nation ratified the Mississippi Interstate Cooperative Resource Agreement in 1990 and formed the Mississippi Interstate Cooperative Resource Association (MICRA) in 1991 to improve the management of interjurisdictional fishery resources in the basin.\n**(6)**\nRecognizing the economic, ecologic, and cultural value of the diverse interjurisdictional fishery resources in the Mississippi River Basin and the complexity and severity of issues facing resource management agencies, Congress acknowledges the need for the establishment of a Mississippi River Basin Fishery Commission for basin-wide, inter-agency collaboration in the establishment of shared management objectives, and the collaborative planning, implementation, and evaluation of management actions to provide for the long-term biologic and economic sustainability of interjurisdictional fishery resources in the basin.\n**(7)**\nAs long-term sustainability of interjurisdictional fishery resources is dependent on the control of aquatic invasive species within the Mississippi River Basin, it is the further purpose of this Commission to provide for coordinated, inter-agency, basin-wide management, control, and removal of invasive carps and other prioritized aquatic invasive species within the basin.\n**(8)**\nBy consent of Congress, and as directed by Federal law under the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ) and the Interjurisdictional Fisheries Act of 1986 ( 16 U.S.C. 4101 et seq. ), sustainable fisheries within the United States coastal waters of the Pacific, Atlantic, and Caribbean Oceans, and the Gulf of Mexico, have been managed by multi-state commissions and fishery councils for many decades.\n**(9)**\nThe interjurisdictional and international fishery resources of the Great Lakes are cooperatively managed by the Great Lakes Fishery Commission, operating through the 1954 Convention on Great Lake Fisheries.\n**(10)**\nThe Mississippi River Basin Fishery Commission will improve the management and utilization of sustainable interjurisdictional fishery resources in the Mississippi River Basin through the development of a multi-agency program for the joint management and protection of such fishery resources.\n#### 3. Definitions\nIn this Act:\n**(1) Aquatic invasive species**\nThe term aquatic invasive species means a nonindigenous species that threatens the diversity or abundance of native species in, or the ecological stability of, infested waters, or commercial, agricultural, aquacultural, or recreational activities dependent on such waters.\n**(2) Commission**\nThe term Commission means the Mississippi River Basin Fishery Commission established under section 4.\n**(3) Director of fisheries**\nThe term director of fisheries means the individual in a State who is the highest designated officer in charge of fishery management employed by the State, regardless of the formal title of such individual.\n**(4) Eligible entity**\nThe term eligible entity includes\u2014\n**(A)**\nany political subdivision, agency, or department of a Mississippi River Basin State that regulates Mississippi River Basin fisheries;\n**(B)**\nan Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) or an entity controlled by an Indian Tribe that manages Mississippi River Basin fisheries;\n**(C)**\nthe United States Geological Survey;\n**(D)**\nthe United States Fish and Wildlife Service;\n**(E)**\nthe United States Army Corps of Engineers;\n**(F)**\nthe Engineer Research and Development Center of the United States Army Corps of Engineers; and\n**(G)**\nthe Tennessee Valley Authority.\n**(5) Fishery resource**\nThe term fishery resource means finfish, mollusks, crustaceans, and any other form of animal or plant life, other than mammals or birds.\n**(6) Interjurisdictional fishery resource**\nThe term interjurisdictional fishery resource means\u2014\n**(A)**\na fishery resource located in a fishery in waters under the jurisdiction of 2 or more Mississippi River Basin States;\n**(B)**\na fishery resource for which there exists an interstate fishery management plan; or\n**(C)**\na fishery resource that migrates between the waters under the jurisdiction of 2 or more Mississippi River Basin States.\n**(7) Invasive carp**\nThe term invasive carp means an aquatic invasive species of finfish that\u2014\n**(A)**\noriginated in Europe and Asia;\n**(B)**\nspread quickly once they are established in a body of water or waterway;\n**(C)**\ncause serious damage to the native fish populations, as well as economic and physical harm to humans; and\n**(D)**\ninclude the bighead carp, black carp, grass carp, and silver carp.\n**(8) Member entity**\nThe term member entity means an eligible entity that maintains an active membership in the Commission.\n**(9) Mississippi River Basin State**\nThe term Mississippi River Basin State means a State whose borders include waters that drain into the Mississippi River Basin, including Alabama, Arkansas, Colorado, Georgia, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maryland, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Pennsylvania, South Dakota, Tennessee, Texas, Virginia, West Virginia, Wisconsin, and Wyoming.\n**(10) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 4. Establishment of Mississippi River Basin Fishery Commission\n##### (a) In general\nThere is established in the Department of the Interior the Mississippi River Basin Fishery Commission.\n##### (b) Members of the Commission\nAny eligible entity may join the Commission by notifying the executive director and existing members of the Commission in writing of its intent to join the Commission.\n#### 5. Commission governance\n##### (a) Voting delegates\n**(1) States**\nWith respect to each eligible entity described in section 3(4)(A) that joins the Commission, the director of fisheries of such eligible entity shall serve as the voting delegate to represent such entity\u2019s interests on the Commission.\n**(2) Federal agencies and Indian tribes**\nWith respect to each eligible entity described in any of subparagraphs (B) through (G) of section 3(4) that joins the Commission, such entity shall appoint 1 individual to serve as the voting delegate to represent such entity\u2019s interests on the Commission.\n##### (b) Body corporate\nThe Commission shall be a body corporate with the powers and duties described in this Act. The member entities shall establish a governance structure for the Commission.\n##### (c) Executive director and staff\nThe Commission shall\u2014\n**(1)**\nappoint a full-time executive director and staff as needed to carry out the administrative duties of the Commission, who shall\u2014\n**(A)**\nprovide advice to, and carry out operational duties of, the Commission; and\n**(B)**\nhave no voting rights on the Commission; and\n**(2)**\nat its pleasure, appoint, remove, or discharge such executive director and staff, as may be needed, and fix and determine their duties, qualifications, and compensation.\n##### (d) Chair and vice chair\nThe Commission shall elect a Chair and a Vice Chair of the Commission from the member entities.\n##### (e) Rule and regulations\nThe Commission shall adopt rules and regulations for the conduct of its business.\n##### (f) Offices and meetings\nThe Commission\u2014\n**(1)**\nmay establish and maintain 1 or more offices for the transaction of its business, which shall be located within the Mississippi River Basin; and\n**(2)**\nmay meet at any time or place but not less often than annually.\n##### (g) Decision making\nThe Commission may make a recommendation or take an action regarding its general affairs only by an affirmative vote of a majority of the member entities. The Commission shall strive for unanimity in its decisions but shall operate by consensus in its decision making.\n##### (h) FACA not to apply\nChapter 10 of title 5, United States Code, shall not apply to the Commission.\n#### 6. Commission management duties\n##### (a) Overseeing sub-Basin fishery management\n**(1) In general**\nThe Commission shall oversee the management plans and the implementation and evaluation of the effectiveness of management actions of the 6 Mississippi River sub-basins described in paragraph (2) to provide for the long-term biologic and economic sustainability of interjurisdictional fisheries in the Mississippi River Basin.\n**(2) Sub-basins**\nThe 6 Mississippi River sub-basins are the Arkansas-Red-White, the Lower Mississippi, the Missouri, the Ohio, the Tennessee-Cumberland, and the Upper Mississippi.\n##### (b) Commission management plan\n**(1) In general**\nAs the framework for a management plan for the Commission, the Commission shall adopt and use the MICRA Joint Strategic Plan for Management of Mississippi River Fisheries, which\u2014\n**(A)**\nwas adopted and approved by 28 States in the Mississippi River Basin; and\n**(B)**\nestablishes a formal commitment to a set of strategic procedures for a coordinated, inter-agency approach to cooperatively managing self-sustaining interjurisdictional fishery resources in the Mississippi River Basin.\n**(2) Best methods, practices, and conditions**\nThe Commission shall work to research and implement the best scientific methods, best practices, and best conditions to bring about the conservation and sustainable management of interjurisdictional fisheries in the Mississippi River Basin.\n**(3) Strategies to control invasive species**\nThe Commission shall\u2014\n**(A)**\ndevelop and coordinate inter-agency and inter-basin strategies to prevent the introduction and control the abundance and spread of invasive carps and other prioritized aquatic invasive species within the Mississippi River Basin; and\n**(B)**\ndraft and recommend to the appropriate management agencies strategies and approaches for dealing with the conservation of interjurisdictional fisheries and the management and control of aquatic invasive species within the Mississippi River Basin.\n**(4) Consultation and advice**\nThe Commission shall consult with and advise the pertinent administrative agencies party to the Commission regarding problems connected with the fisheries in the Mississippi River Basin and recommend the adoption of such regulations as it determines advisable.\n**(5) Reexamination and evaluation of joint strategic plan**\nNot later than 30 years after the date of enactment of this Act, the Commission, in consultation with the Secretary, shall\u2014\n**(A)**\nreexamine and evaluate the Joint Strategic Plan described in paragraph (1) to\u2014\n**(i)**\ndetermine which portions of the Plan have been completed and which need updating; and\n**(ii)**\nadd new objectives, if any, to the Plan; and\n**(B)**\nissue a report to Congress on the status of interjurisdictional fishery populations and the state of the ongoing work to eradicate, manage, and control aquatic invasive species in the Mississippi River Basin in accordance with the management plan of the Commission.\n#### 7. Commission grant program\n##### (a) Establishment of grant program\nNot later than 2 years after the date of enactment of this Act, the Commission, in consultation with the Secretary, shall establish\u2014\n**(1)**\na competitive grant program to award grants to entities to carry out an eligible project; and\n**(2)**\na formula grant program to award grants to State member entities to carry out eligible interjurisdictional fisheries projects carried out in accordance with the recommendation of the Commission or the Joint Strategic Plan described in section 6(b)(1).\n##### (b) Entities eligible To receive grants\nThe Commission may provide\u2014\n**(1)**\nformula grants and competitive grants to State member entities; and\n**(2)**\ncompetitive grants to private entities, Federal agencies, nongovernmental organizations, public and private institutions of higher education, and partnerships between entities described in this subsection.\n##### (c) Competitive grants\n**(1) Applications**\nAn entity desiring a competitive grant under this section shall submit to the Commission an application at such time, in such manner, and containing such information as the Commission may require.\n**(2) Priority for entities providing matching funds**\nIn awarding competitive grants under this section, the Commission shall give priority to entities that will provide matching funds from non-Federal sources of not less than 10 percent of the grant award, which may be provided in cash or in-kind.\n##### (d) Formula grant program\nThe Commission shall determine the amount that each State member entity shall receive annually under the formula grant program.\n##### (e) Use of funds\nAn entity that receives a grant under this section shall use the grant funds\u2014\n**(1)**\nin the case of\u2014\n**(A)**\na competitive grant, in accordance with the goals and objectives of the Joint Strategic Plan described in section 6(b)(1) and each of the interjurisdictional fishery management plans of the 6 Mississippi River sub-basins described in section 6(a)(2); and\n**(B)**\na formula grant, to carry out eligible interjurisdictional fishery projects carried out in accordance with the recommendation of the Commission or the Joint Strategic Plan described in section 6(b)(1); and\n**(2)**\nonly for projects, research, personnel, work, and programs located wholly or partially in a Mississippi River Basin State.\n##### (f) Administrative costs\nAn entity awarded a grant under this section may use not more than 5 percent of the grant funds for administrative costs relating to the grant.\n##### (g) Report requirements\nNot later than 1 year after the disbursement of grant funding under this section, the Chair of the Commission shall submit to Congress a report on\u2014\n**(1)**\nthe entities awarded grants under this section;\n**(2)**\nthe amount each such grant;\n**(3)**\nhow such entities used the grant awards; and\n**(4)**\nhow such grant awards enhanced the management and sustainability of the interjurisdictional fisheries of the Mississippi River Basin.\n#### 8. Nonbinding authority\n##### (a) In general\nThe authority of the Commission shall be nonbinding.\n##### (b) Rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto limit the powers of any member entity that is a State to repeal or enact State laws; or\n**(2)**\nto limit the enforcement of any requirement by any member entity that is a State imposing additional conditions and restrictions to conserve its fisheries within the borders of the State.\n#### 9. Withdrawal from the Commission\nA member entity that intends to withdraw from the Commission shall submit a notice of intent to withdraw in writing not later than 6 months before the date of the withdrawal to\u2014\n**(1)**\nthe Commission; and\n**(2)**\neach of the other member entities of the Commission.\n#### 10. Report to Congress\nNot later than September 1 of each year after the date of enactment of this Act, the Commission shall submit a report to Congress which shall set forth the activities of the Commission during the previous year.\n#### 11. Appropriations\nThere are authorized to be appropriated\u2014\n**(1)**\n$1,000,000 for fiscal year 2026 to carry out the initial administrative steps necessary to set up operations, house, and administer the Commission;\n**(2)**\nto carry out sections 6 and 7\u2014\n**(A)**\n$30,000,000 for each of fiscal years 2027 through 2029, to remain available until expended; and\n**(B)**\n$50,000,000 for each of fiscal years 2030 through 2032, to remain available until expended; and\n**(3)**\n$500,000 for each of fiscal years 2026 through 2032 to the Secretary of the Interior for housing the Commission, to remain available until expended.",
      "versionDate": "2025-02-24",
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
        "actionDate": "2025-03-14",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1078",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mississippi River Basin Fishery Commission Act",
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
            "name": "Advisory bodies",
            "updateDate": "2025-12-11T16:59:41Z"
          },
          {
            "name": "Alabama",
            "updateDate": "2025-12-11T16:57:09Z"
          },
          {
            "name": "Arkansas",
            "updateDate": "2025-12-11T16:57:13Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-12-11T16:57:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T16:59:56Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-12-11T16:59:36Z"
          },
          {
            "name": "Georgia",
            "updateDate": "2025-12-11T16:57:21Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2025-12-11T16:57:27Z"
          },
          {
            "name": "Indiana",
            "updateDate": "2025-12-11T16:57:33Z"
          },
          {
            "name": "Iowa",
            "updateDate": "2025-12-11T16:57:38Z"
          },
          {
            "name": "Kansas",
            "updateDate": "2025-12-11T16:57:42Z"
          },
          {
            "name": "Kentucky",
            "updateDate": "2025-12-11T16:57:47Z"
          },
          {
            "name": "Louisiana",
            "updateDate": "2025-12-11T16:57:52Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-12-11T16:57:05Z"
          },
          {
            "name": "Maryland",
            "updateDate": "2025-12-11T16:57:56Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2025-12-11T16:58:00Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-12-11T16:58:05Z"
          },
          {
            "name": "Mississippi",
            "updateDate": "2025-12-11T16:58:10Z"
          },
          {
            "name": "Mississippi River",
            "updateDate": "2025-12-11T16:56:56Z"
          },
          {
            "name": "Missouri",
            "updateDate": "2025-12-11T16:58:14Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-12-11T16:58:20Z"
          },
          {
            "name": "Nebraska",
            "updateDate": "2025-12-11T16:58:24Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-12-11T16:58:28Z"
          },
          {
            "name": "New York State",
            "updateDate": "2025-12-11T16:58:34Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-12-11T16:58:39Z"
          },
          {
            "name": "North Dakota",
            "updateDate": "2025-12-11T16:58:43Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2025-12-11T16:58:48Z"
          },
          {
            "name": "Oklahoma",
            "updateDate": "2025-12-11T16:58:53Z"
          },
          {
            "name": "Pennsylvania",
            "updateDate": "2025-12-11T16:59:01Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2025-12-11T16:59:47Z"
          },
          {
            "name": "South Dakota",
            "updateDate": "2025-12-11T16:59:06Z"
          },
          {
            "name": "Tennessee",
            "updateDate": "2025-12-11T16:59:10Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-12-11T16:59:14Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-12-11T16:59:19Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-12-11T17:00:02Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-12-11T16:57:01Z"
          },
          {
            "name": "West Virginia",
            "updateDate": "2025-12-11T16:59:23Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2025-12-11T16:59:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-16T16:51:19Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1514ih.xml"
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
      "title": "Mississippi River Basin Fishery Commission Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mississippi River Basin Fishery Commission Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Mississippi River Basin Fishery Commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:18Z"
    }
  ]
}
```
