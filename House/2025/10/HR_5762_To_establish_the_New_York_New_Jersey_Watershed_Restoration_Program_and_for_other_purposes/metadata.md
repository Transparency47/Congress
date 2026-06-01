# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5762
- Title: New York-New Jersey Watershed Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5762
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2026-04-08T15:32:38Z
- Update date including text: 2026-04-08T15:32:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5762",
    "number": "5762",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "New York-New Jersey Watershed Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T15:32:38Z",
    "updateDateIncludingText": "2026-04-08T15:32:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
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
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
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
          "date": "2025-10-14T18:00:40Z",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "PA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5762ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5762\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Tonko (for himself, Ms. Malliotakis , Ms. Vel\u00e1zquez , Mr. Fitzpatrick , Ms. Gillen , Mr. Goldman of New York , Mr. Gottheimer , Mr. Kean , Mr. Latimer , Mr. Lawler , Mr. Mannion , Mrs. McIver , Mr. Meeks , Mr. Menendez , Ms. Meng , Mr. Norcross , Ms. Ocasio-Cortez , Mr. Pallone , Ms. Pou , Mr. Riley of New York , Mr. Ryan , Ms. Sherrill , Mr. Suozzi , Mr. Torres of New York , Mr. Van Drew , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the New York-New Jersey Watershed Restoration Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New York-New Jersey Watershed Protection Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Approved plan**\n**(A) In general**\nThe term approved plan means any plan for management of the Watershed\u2014\n**(i)**\nthat has been approved by a Federal, regional, State, Tribal, or local governmental entity, including State Wildlife Action Plans, Comprehensive Conservation Management Plans, and Watershed Improvement Plans; or\n**(ii)**\nthat is determined by the Secretary, in consultation with the entities described in clause (i), to contribute to the achievement of the purposes of this Act.\n**(B) Inclusions**\nThe term approved plan includes\u2014\n**(i)**\nthe New York-New Jersey Harbor & Estuary Program (HEP) Action Agenda;\n**(ii)**\nthe Hudson Raritan Comprehensive Restoration Plan;\n**(iii)**\nthe Hudson River Comprehensive Restoration Plan;\n**(iv)**\nthe Hudson River Estuary Program Action Agenda;\n**(v)**\nthe Mohawk River Action Agenda;\n**(vi)**\nthe Sustainable Raritan River Initiative Action Plan;\n**(vii)**\nthe Lower Passaic and Bronx & Harlem Federal Urban Waters Partnership Workplans;\n**(viii)**\nthe New Jersey Sports and Exhibition Authority Meadowlands Restoration Plan; and\n**(ix)**\nsuch other conservation projects in the region that achieve the purposes of this Act, as determined by the Secretary.\n**(2) Environmental justice**\nThe term environmental justice , with respect to the development, implementation, and enforcement of environmental laws, regulations, and policies, means the fair treatment and meaningful involvement of all people, regardless of race, color, national origin, or income.\n**(3) Foundation**\nThe term Foundation means the National Fish and Wildlife Foundation.\n**(4) Grant program**\nThe term grant program means the voluntary New York-New Jersey Watershed Restoration Grant Program established under section 4(a).\n**(5) Program**\nThe term program means the New York-New Jersey Watershed Restoration Program established under section 3(a).\n**(6) Restoration and protection**\nThe term restoration and protection means the conservation, stewardship, and enhancement of habitat for fish and wildlife, including water quality\u2014\n**(A)**\nto preserve and improve ecosystems and ecological processes on which those fish and wildlife depend; and\n**(B)**\nfor use and enjoyment by the public.\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(8) Watershed**\nThe term Watershed means the New York-New Jersey Watershed, which is composed of\u2014\n**(A)**\nall land area the surface water of which drains into the New York-New Jersey Harbor;\n**(B)**\nthe waters contained within that land area; and\n**(C)**\nthe estuaries associated with those watersheds.\n#### 3. New York-New Jersey Watershed Restoration Program\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall establish a nonregulatory program, to be known as the New York-New Jersey Watershed Restoration Program .\n##### (b) Purposes\nThe purposes of the program shall include\u2014\n**(1)**\ncoordinating restoration and protection activities among Federal, State, Tribal, local, and regional entities and conservation partners throughout the Watershed;\n**(2)**\ncarrying out coordinated restoration and protection activities, and providing for technical assistance for those activities, throughout the Watershed\u2014\n**(A)**\nto sustain and enhance fish and wildlife habitat;\n**(B)**\nto improve and maintain water quality to support fish, wildlife, and their habitats, as well as to improve opportunities for public access and recreation in the Watershed consistent with the ecological needs of fish and wildlife habitats;\n**(C)**\nto advance the use of natural climate solutions and natural infrastructure, including living shorelines and other green infrastructure techniques, to maximize the resilience of communities, natural systems, and habitats experiencing the impacts of climate change;\n**(D)**\nto engage the public, particularly communities experiencing environmental injustice, through outreach, education, and community involvement to increase capacity, support, and workforce development for coordinated restoration and protection activities in the Watershed;\n**(E)**\nto increase scientific capacity to support the planning, monitoring, and research activities necessary to carry out coordinated restoration and protection activities in the Watershed;\n**(F)**\nto provide for feasibility and planning studies for green infrastructure projects that achieve habitat restoration and stormwater management goals;\n**(G)**\nto support land conservation and management activities necessary to fulfill the Watershed-wide strategy adopted under subsection (c)(3);\n**(H)**\nto monitor environmental quality to assess progress toward the purposes of this Act; and\n**(I)**\nto improve fish and wildlife habitats, as well as opportunities for personal recreation, along rivers and shore fronts within communities experiencing environmental injustice; and\n**(3)**\ncarrying out restoration and protection activities necessary, as determined by the Secretary, for the implementation of approved plans.\n##### (c) Duties\nIn carrying out the program, the Secretary shall\u2014\n**(1)**\ndraw on existing and new approved plans for the Watershed, or portions of the Watershed;\n**(2)**\nwork in consultation with applicable management entities, including representatives of the New York-New Jersey Harbor and Estuary Program (HEP), the Hudson River Estuary Program, the Mohawk River Basin Program, the Sustainable Raritan River Initiative, the Federal Government, other State and local governments, and regional and nonprofit organizations, including environmental justice organizations, as appropriate, to identify, prioritize, and implement restoration and protection activities within the Watershed; and\n**(3)**\nadopt a Watershed-wide strategy that\u2014\n**(A)**\nsupports the implementation of a shared set of science-based restoration and protection activities developed in accordance with paragraph (2);\n**(B)**\ntargets cost-effective projects with measurable results;\n**(C)**\nmaximizes conservation outcomes;\n**(D)**\nprioritizes the needs of communities experiencing environmental injustice; and\n**(E)**\nimplements the grant program.\n##### (d) Consultation\nIn establishing the program, the Secretary shall consult with, as appropriate\u2014\n**(1)**\nthe heads of Federal agencies, including\u2014\n**(A)**\nthe Administrator of the Environmental Protection Agency;\n**(B)**\nthe Administrator of the National Oceanic and Atmospheric Administration;\n**(C)**\nthe Secretary of Agriculture;\n**(D)**\nthe Director of the National Park Service; and\n**(E)**\nthe heads of such other Federal agencies as the Secretary determines to be appropriate;\n**(2)**\nthe Governor of New York;\n**(3)**\nthe Governor of New Jersey;\n**(4)**\nthe Commissioner of the New York State Department of Environmental Conservation;\n**(5)**\nthe Director of the New Jersey Division of Fish and Wildlife;\n**(6)**\nthe New York-New Jersey Harbor & Estuary Program; and\n**(7)**\nother public agencies, Indian Tribes, and organizations with authority for the planning and implementation of conservation strategies in the Watershed, as determined appropriate by the Secretary.\n#### 4. New York-New Jersey watershed restoration grant program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a voluntary grant and technical assistance program, to be known as the New York-New Jersey Watershed Restoration Grant Program , to provide competitive matching grants to State, Tribal, and local governments, nonprofit organizations, institutions of higher education, and other eligible entities, as determined by the Secretary, to carry out the coordinated restoration and protection activities described in section 3(b)(2).\n##### (b) Criteria\nThe Secretary, in consultation with the individuals and entities referred to in section 3(d), shall develop criteria for the grant program to ensure that activities funded under the grant program\u2014\n**(1)**\naccomplish 1 or more of the purposes identified in section 3(b)(2); and\n**(2)**\nadvance the implementation of priority actions or needs identified in the Watershed-wide strategy adopted under section 3(c)(3).\n##### (c) Capacity building\nIn carrying out the grant program, the Secretary shall seek to increase the effectiveness of organizations that carry out restoration and protection activities described in section 3(b)(2) within the Watershed by addressing organizational capacity needs.\n##### (d) Cost-Share\n**(1) Federal share**\n**(A) In general**\nExcept as provided in subparagraph (B), the Federal share of the total cost of a restoration and protection activity carried out under the grant program shall be not more than 50 percent, as determined by the Secretary.\n**(B) Small, rural, and disadvantaged communities**\n**(i) In general**\nSubject to clause (ii) the Federal share of the total cost of a restoration and protection activity carried out under the grant program that serves a small, rural, or disadvantaged community shall be 90 percent, as determined by the Secretary.\n**(ii) Waiver**\nThe Secretary may increase the Federal share under clause (i) to 100 percent of the total cost of the restoration and protection activity if the Secretary determines that the grant recipient is unable to pay, or would experience significant financial hardship if required to pay, the non-Federal share.\n**(2) Non-Federal share**\n**(A) In general**\nThe non-Federal share of the total cost of a restoration and protection activity carried out under the grant program shall be not more than 50 percent, as determined by the Secretary.\n**(B) Form of payment**\nThe non-Federal share described in subparagraph (A) may be provided\u2014\n**(i)**\nin cash; or\n**(ii)**\nin the form of an in-kind contribution of services or materials.\n##### (e) Administration\n**(1) In general**\nThe Secretary may enter into an agreement to manage the grant program with\u2014\n**(A)**\nthe Foundation; or\n**(B)**\na similar organization that offers grant management services.\n**(2) Funding**\nIf the Secretary enters into an agreement under paragraph (1), the Foundation or similar organization selected, as applicable, shall\u2014\n**(A)**\nreceive the amounts made available to carry out the grant program under section 7 for each applicable fiscal year in an advance payment of the entire amount on October 1 of that fiscal year, or as soon as practicable thereafter;\n**(B)**\ninvest and reinvest those amounts for the benefit of the grant program; and\n**(C)**\nadminister the grant program to support partnerships between the public and private sectors in accordance with this Act.\n**(3) Requirements**\nIf the Secretary enters into an agreement with the Foundation under paragraph (1), any amounts received by the Foundation under this section shall be subject to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ), excluding section 10(a) of that Act ( 16 U.S.C. 3709(a) ).\n#### 5. Annual report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to Congress a report on the implementation of this Act, including a description of each activity that has received funding under this Act in the preceding fiscal year.\n#### 6. Prohibition on Federal land holdings\nThe Federal Government may not maintain ownership of any land acquired under this Act except for the purpose of promptly transferring ownership to an entity described in section 4(a).\n#### 7. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to the Secretary to carry out this Act $20,000,000 for each of fiscal years 2026 through 2031, of which not more than 5 percent shall be used for administrative costs of carrying out this Act.\n##### (b) Grant program\nOf the amounts made available to carry out this Act for each fiscal year, the Secretary shall use not less than 75 percent to carry out the grant program, including for technical assistance relating to the grant program.\n##### (c) Supplement, not supplant\nAmounts made available to carry out this Act for each fiscal year shall supplement, and not supplant, funding for other activities conducted by the Secretary in the Watershed.\n#### 8. Sunset\nThis Act shall cease to have force or effect on October 1, 2031.",
      "versionDate": "2025-10-14",
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
        "actionDate": "2025-09-29",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2926",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "New York-New Jersey Watershed Protection Act",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-08T18:01:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-14",
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
          "measure-id": "id119hr5762",
          "measure-number": "5762",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-14",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5762v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>New York-New Jersey Watershed Protection Act\u00a0of 2025</strong></p><p>This bill establishes programs to restore and protect the New York-New Jersey Watershed. The watershed is composed of all land area the surface water of which drains into the New York-New Jersey Harbor, the waters contained within that land area, and associated estuaries.</p><p>Specifically, the bill requires the U.S. Fish and Wildlife Service to establish the New York-New Jersey Watershed Restoration Program, a nonregulatory program, to coordinate restoration and protection activities among government entities and conservation partners throughout the watershed.</p><p>The bill also establishes the New York-New Jersey Watershed Restoration Grant Program, a voluntary grant and technical assistance program, to provide competitive matching grants to certain entities to implement restoration and protection activities for the watershed. The federal government may not maintain ownership of any land acquired under the bill except for the purpose of promptly transferring ownership to grant recipients.</p><p>The bill ceases to have force or effect on October 1, 2031.</p>"
        },
        "title": "New York-New Jersey Watershed Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5762.xml",
    "summary": {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New York-New Jersey Watershed Protection Act\u00a0of 2025</strong></p><p>This bill establishes programs to restore and protect the New York-New Jersey Watershed. The watershed is composed of all land area the surface water of which drains into the New York-New Jersey Harbor, the waters contained within that land area, and associated estuaries.</p><p>Specifically, the bill requires the U.S. Fish and Wildlife Service to establish the New York-New Jersey Watershed Restoration Program, a nonregulatory program, to coordinate restoration and protection activities among government entities and conservation partners throughout the watershed.</p><p>The bill also establishes the New York-New Jersey Watershed Restoration Grant Program, a voluntary grant and technical assistance program, to provide competitive matching grants to certain entities to implement restoration and protection activities for the watershed. The federal government may not maintain ownership of any land acquired under the bill except for the purpose of promptly transferring ownership to grant recipients.</p><p>The bill ceases to have force or effect on October 1, 2031.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5762"
    },
    "title": "New York-New Jersey Watershed Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New York-New Jersey Watershed Protection Act\u00a0of 2025</strong></p><p>This bill establishes programs to restore and protect the New York-New Jersey Watershed. The watershed is composed of all land area the surface water of which drains into the New York-New Jersey Harbor, the waters contained within that land area, and associated estuaries.</p><p>Specifically, the bill requires the U.S. Fish and Wildlife Service to establish the New York-New Jersey Watershed Restoration Program, a nonregulatory program, to coordinate restoration and protection activities among government entities and conservation partners throughout the watershed.</p><p>The bill also establishes the New York-New Jersey Watershed Restoration Grant Program, a voluntary grant and technical assistance program, to provide competitive matching grants to certain entities to implement restoration and protection activities for the watershed. The federal government may not maintain ownership of any land acquired under the bill except for the purpose of promptly transferring ownership to grant recipients.</p><p>The bill ceases to have force or effect on October 1, 2031.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5762"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5762ih.xml"
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
      "title": "New York-New Jersey Watershed Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New York-New Jersey Watershed Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the New York-New Jersey Watershed Restoration Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:14Z"
    }
  ]
}
```
