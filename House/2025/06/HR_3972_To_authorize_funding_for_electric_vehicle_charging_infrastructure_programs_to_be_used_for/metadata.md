# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3972
- Title: Highway Funding Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3972
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-05T22:55:16Z
- Update date including text: 2025-12-05T22:55:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-13 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-13 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3972",
    "number": "3972",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Highway Funding Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:16Z",
    "updateDateIncludingText": "2025-12-05T22:55:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T20:53:02Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-12T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "IN"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3972ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3972\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Johnson of South Dakota (for himself, Mr. Shreve , and Mr. Hurd of Colorado ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize funding for electric vehicle charging infrastructure programs to be used for other highway projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Highway Funding Flexibility Act of 2025 .\n#### 2. Optimizing use of National Electric Vehicle Infrastructure Formula program funds\n##### (a) Definitions\nIn this section:\n**(1) Program**\nThe term program means the program under paragraph (2) in the matter under the heading highway infrastructure programs under the heading Federal Highway Administration under the heading Department of Transportation in title VIII of division J of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 1421) (commonly known as the National Electric Vehicle Infrastructure Formula Program ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) State**\nThe term State has the meaning given the term in section 101(a) of title 23, United States Code.\n##### (b) Optimization of funds\n**(1) In general**\nNotwithstanding any other provision of law, any amounts made available under the program that are unobligated as of the date of enactment of this Act\u2014\n**(A)**\nshall be used only for\u2014\n**(i)**\nthe construction, reconstruction, resurfacing, restoration, rehabilitation, or preservation of a Federal-aid highway;\n**(ii)**\na project to replace, rehabilitate, preserve, or protect 1 or more bridges on the National Bridge Inventory under section 144(b) of title 23, United States Code;\n**(iii)**\nimprovements that reduce the number of wildlife-vehicle collisions, such as wildlife crossing structures;\n**(iv)**\nprojects to preserve or provide additional parking for commercial motor vehicles that are eligible under section 1401 of MAP\u201321 ( 23 U.S.C. 137 note; Public Law 112\u2013141 ); or\n**(v)**\npreliminary engineering, engineering, or design-related services directly related to a project described in any of clauses (i) through (iv); and\n**(B)**\nmay not be used for the purposes described in paragraph (2) in the matter under the heading highway infrastructure programs under the heading Federal Highway Administration under the heading Department of Transportation in title VIII of division J of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 1421).\n**(2) Future fiscal years**\nNotwithstanding any other provision of law, any funds made available for the program for any fiscal year beginning after the date of enactment of this Act shall be distributed to States in accordance with the program on October 1 of that fiscal year and used as described in paragraph (1).\n##### (c) Set-Asides\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary shall distribute to States in accordance with paragraph (3)\u2014\n**(A)**\nany unobligated amounts under the program that are set aside for the Joint Office described in the program; and\n**(B)**\nany unobligated amounts under the program that are set aside for grants to States or localities that require additional assistance to strategically deploy electric vehicle charging infrastructure.\n**(2) Future fiscal years**\nNotwithstanding any other provision of law, any funds described in paragraph (1) that are made available for any fiscal year beginning after the date of enactment of this Act shall be distributed to States in accordance with paragraph (3) on October 1 of that fiscal year and used as described in paragraph (4).\n**(3) Distribution**\nThe amounts distributed under paragraphs (1) and (2) shall be distributed so that each State receives an amount equal to the proportion that\u2014\n**(A)**\nthe amount apportioned to the State for the applicable fiscal year under section 104(c) or section 165 of title 23, United States Code; bears to\n**(B)**\nthe total amount apportioned to all States for that fiscal year under section 104(c) and section 165 of that title.\n**(4) Use of funds**\nAmounts distributed under paragraphs (1) and (2) shall be used as described in subsection (b)(1).\n##### (d) Treatment\nThe amounts described in subsections (b) and (c) shall\u2014\n**(1)**\nnot be subject to any obligation limitation for Federal-aid highway and highway safety construction programs;\n**(2)**\nremain available until the date the funds would have remained available under the program; and\n**(3)**\nbe in addition to any other funding apportioned to States under section 104(c) and section 165 of title 23, United States Code.\n##### (e) Requirements\nAmounts described in subsections (b) and (c) shall be\u2014\n**(1)**\nexcept as otherwise provided in this section, administered as if apportioned under chapter 1 of title 23, United States Code;\n**(2)**\nsubject to the requirements of section 11101(e) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ); and\n**(3)**\nsubject to section 120 of title 23, United States Code.\n#### 3. Optimizing use of charging and fueling infrastructure grant funds\n##### (a) Definitions\nIn this section:\n**(1) Program**\nThe term program means the grant program under section 151(f) of title 23, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) State**\nThe term State has the meaning given the term in section 101(a) of title 23, United States Code.\n##### (b) Optimization of funds\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary shall distribute to States in accordance with paragraph (3) any amounts made available to carry out the program that are unobligated as of the date of enactment of this Act.\n**(2) Future fiscal years**\nAny amounts made available to carry out the program for a fiscal year that begins after the date of enactment of this Act shall be distributed to States in accordance with paragraph (3) on October 1 of that fiscal year.\n**(3) Distribution**\nThe amounts distributed under paragraphs (1) and (2) shall be distributed so that each State receives an amount equal to the proportion that\u2014\n**(A)**\nthe amount apportioned to the State for the applicable fiscal year under section 104(c) or section 165 of title 23, United States Code; bears to\n**(B)**\nthe total amount apportioned to all States for that fiscal year under section 104(c) and section 165 of that title.\n**(4) Uses of funds**\nAny amounts distributed under paragraphs (1) and (2)\u2014\n**(A)**\nshall be used only for the purposes described in section 2(b)(1)(A); and\n**(B)**\nmay not be used for any purposes described in the program.\n##### (c) Treatment\nThe amounts described in subsection (b) shall\u2014\n**(1)**\nbe subject to any obligation limitation for Federal-aid highway and highway safety construction programs;\n**(2)**\nremain available until the date the funds would have remained available under the program; and\n**(3)**\nbe in addition to any other funding apportioned to States under section 104(c) or section 165 of title 23, United States Code.\n##### (d) Requirements\nAmounts described in subsection (b) shall be\u2014\n**(1)**\nexcept as otherwise provided in this section, administered as if apportioned under chapter 1 of title 23, United States Code;\n**(2)**\nsubject to the requirements of section 11101(e) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ); and\n**(3)**\nsubject to section 120 of title 23, United States Code.",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1066",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Highway Funding Flexibility Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-03T13:42:22Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3972ih.xml"
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
      "title": "Highway Funding Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Highway Funding Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize funding for electric vehicle charging infrastructure programs to be used for other highway projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:41Z"
    }
  ]
}
```
