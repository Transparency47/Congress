# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4062?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4062
- Title: MONARCH Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4062
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2026-04-06T19:14:16Z
- Update date including text: 2026-04-06T19:14:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-20 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-20 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4062",
    "number": "4062",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "MONARCH Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T19:14:16Z",
    "updateDateIncludingText": "2026-04-06T19:14:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:02:15Z",
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
          "date": "2025-06-20T15:02:10Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "DC"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "HI"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "OR"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "AZ"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "MI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4062ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4062\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Mr. Panetta (for himself, Mr. Carbajal , Ms. Norton , Ms. Tokuda , Mr. Costa , Mr. Krishnamoorthi , Mr. Min , Ms. Bonamici , Mr. Stanton , and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo encourage and facilitate efforts by States and other stakeholders to conserve and sustain the western population of monarch butterflies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe population of western monarch butterflies is at imminent risk of extinction;\n**(2)**\nover the past 3 decades, the population of western monarch butterflies has declined by more than 99 percent due to prolonged drought, loss of milkweed and native pollinator habitat, loss of breeding and overwintering habitat, and climate change;\n**(3)**\nin 2020, the population of western monarch butterflies reached a new historic low of 1,914 butterflies, falling below the predicted extinction threshold for the third year in a row;\n**(4)**\nin 2024, the population of western monarch butterflies reached the second lowest on record, with less than 10,000 butterflies recorded;\n**(5)**\nthe extinction of the population of migratory western monarch butterflies is now likely to occur within the next 2 decades if urgent action is not taken;\n**(6)**\nactively restoring native milkweed and nectar plants, monarch overwintering habitat, and other pollinator habitat, and ensuring that key habitats are protected from destruction, are critical to ensuring the survival of western monarch butterflies and can also help facilitate conservation of other essential pollinators; and\n**(7)**\nenhancing pollinator populations can result in improved pollination services for neighboring land, including agriculture and wildlife ecosystems.\n#### 3. Definitions\nIn this Act:\n**(1) Conservation**\nThe term conservation means the use of each method or procedure necessary to protect habitats of western monarch butterflies and other pollinators within the range of western monarch butterflies, including\u2014\n**(A)**\nthe protection, restoration, and management of overwintering, breeding, and migratory habitats;\n**(B)**\nassistance in the development and implementation of national, regional, State, Tribal, and local conservation and management plans; and\n**(C)**\ncommunity outreach and education.\n**(2) Fund**\nThe term Fund means the Western Monarch Butterfly Rescue Fund established by section 5(a).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(4) Tribal government**\nThe term Tribal government means the governing body of a federally recognized Indian Tribe.\n**(5) Western monarch butterfly**\nThe term western monarch butterfly means the monarch butterfly population that overwinters along the coast of the State of California and breeds across the States of California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah.\n#### 4. Western monarch butterfly conservation grant program\n##### (a) In general\nSubject to the availability of funds and in consultation with other relevant Federal agencies, amounts deposited in the Fund shall be available to the Secretary to provide grants for projects for the conservation of western monarch butterflies, and other pollinators within the range of western monarch butterflies, for which project proposals are approved by the Secretary in accordance with this section.\n##### (b) Project proposals\n**(1) Eligible entities**\nAn entity that is eligible to receive a grant for a project under this section is\u2014\n**(A)**\na relevant local government or Tribal government agency, research institution, or nonprofit organization with expertise required for the conservation of western monarch butterflies and other pollinators within the range of western monarch butterflies; and\n**(B)**\nany other entity, as determined appropriate by the Secretary, with the expertise required for the conservation of western monarch butterflies and other pollinators within the range of western monarch butterflies.\n**(2) Federal partnership opportunities**\nA State or Federal agency\u2014\n**(A)**\nmay not be a lead entity or receive a grant for a project under this section; but\n**(B)**\nmay be included as a partner or collaborator on a project that receives a grant under this section.\n**(3) Required elements**\nA proposal for a project under this section shall include\u2014\n**(A)**\na statement of the purposes of the project;\n**(B)**\nthe name of the entity with overall responsibility for the project;\n**(C)**\na description of\u2014\n**(i)**\nthe qualifications of the entity that will conduct the project;\n**(ii)**\nmethods for project implementation and outcome assessment; and\n**(iii)**\nanticipated outcomes;\n**(D)**\nassurances that the project will be implemented in consultation with relevant wildlife management authorities, Tribal governments, and other appropriate local government, State government, and Federal Government agencies;\n**(E)**\nassurances that the conservation efforts outlined in the proposal do not conflict with food safety measures or practices;\n**(F)**\ninformation that demonstrates the clear potential of the project to contribute to the conservation and recovery of western monarch butterflies and other pollinators within the range of western monarch butterflies; and\n**(G)**\nsuch other information as the Secretary may require.\n##### (c) Project review and approval\nThe Secretary shall annually\u2014\n**(1)**\nsolicit project proposals for funding under this section; and\n**(2)**\nreview each proposal described in paragraph (1) on a timeline that recognizes the urgency of the declining number of western monarch butterflies and other pollinators within the range of western monarch butterflies to determine whether the proposal meets the criteria described in subsection (d).\n##### (d) Criteria for approval\nThe Secretary may approve a project proposal under this section if the proposal demonstrates a likelihood that the project will contribute to the conservation of western monarch butterfly populations in the wild.\n##### (e) Technical assistance\nThe Secretary shall provide technical assistance for a project that receives a grant under this section.\n##### (f) Project reporting\n**(1) In general**\nEach entity that receives a grant for a project under this section shall submit to the Secretary, at such intervals as the Secretary may require, reports that include any information that the Secretary determines is necessary to evaluate the progress and success of the project for the purposes of ensuring positive results, assessing problems, and fostering improvements.\n**(2) Availability to State legislatures**\nAt the request of the Governor of the State in which a project is conducted, each entity that receives a grant for a project under this section shall submit each report under paragraph (1) to the State legislature of that State.\n**(3) Availability to the public**\nThe Secretary shall make available to the public, in a timely manner\u2014\n**(A)**\neach report submitted under paragraph (1); and\n**(B)**\nany other documents relating to projects for which a grant is provided under this section.\n#### 5. Western Monarch Butterfly Rescue Fund\n##### (a) Establishment\nThere is established in the Treasury of the United States a fund, to be known as the Western Monarch Butterfly Rescue Fund .\n##### (b) Administrative expenses\nOf the amounts available in the Fund for each fiscal year, the Secretary may expend not more than 3 percent to pay the administrative expenses necessary to carry out this Act.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated for deposit into the Fund $12,500,000 for each of fiscal years 2026 through 2030, to remain available until expended.\n#### 6. Implementation of the Western Monarch Butterfly Conservation Plan\n##### (a) In general\nThe Secretary shall enter into an agreement with the National Fish and Wildlife Foundation pursuant to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ) to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan prepared by the Western Association of Fish and Wildlife Agencies and dated January 2019.\n##### (b) Administration\nSection 10(a) of the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3709(a) ) shall not apply with respect to\u2014\n**(1)**\nthe agreement entered into under subsection (a); or\n**(2)**\namounts made available to carry out this section.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $12,500,000 for each of fiscal years 2026 through 2030.\n#### 7. Report to Congress\nNot later than January 31 of each year, the Secretary shall submit to Congress a report describing the status of western monarch butterflies, including, with respect to the year for which the report is submitted\u2014\n**(1)**\na summary of the projects for which the Secretary has provided funding under section 4 and an evaluation of those projects; and\n**(2)**\na summary of the projects for which the Secretary has provided funding through the Western Monarch Butterfly Conservation Plan prepared by the Western Association of Fish and Wildlife Agencies and dated January 2019.",
      "versionDate": "2025-06-20",
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2128",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MONARCH Act of 2025",
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
        "name": "Animals",
        "updateDate": "2025-07-14T14:27:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-20",
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
          "measure-id": "id119hr4062",
          "measure-number": "4062",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-20",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4062v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-06-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>"
        },
        "title": "MONARCH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4062.xml",
    "summary": {
      "actionDate": "2025-06-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4062"
    },
    "title": "MONARCH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4062"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4062ih.xml"
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
      "title": "MONARCH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MONARCH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Monarch Action, Recovery, and Conservation of Habitat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To encourage and facilitate efforts by States and other stakeholders to conserve and sustain the western population of monarch butterflies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:29Z"
    }
  ]
}
```
