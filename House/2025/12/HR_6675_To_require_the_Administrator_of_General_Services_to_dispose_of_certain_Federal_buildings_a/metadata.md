# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6675
- Title: DISPOSAL Act
- Congress: 119
- Bill type: HR
- Bill number: 6675
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-03T09:05:40Z
- Update date including text: 2026-02-03T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6675",
    "number": "6675",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "DISPOSAL Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:40Z",
    "updateDateIncludingText": "2026-02-03T09:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:10:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:38:57Z",
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
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "OK"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "IA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "SC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NC"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "SC"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "WY"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6675ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6675\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Steube (for himself, Mr. Clyde , Mrs. Bice , Mr. Bean of Florida , Mr. Feenstra , Mr. Moore of Alabama , Mrs. Biggs of South Carolina , Mr. Self , Mr. Harrigan , Mr. Norman , Ms. Hageman , and Mr. Roy ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Administrator of General Services to dispose of certain Federal buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disposing of Inactive Structures and Properties by Offering for Sale And Lease Act or the DISPOSAL Act .\n#### 2. Disposal of specified Federal buildings\n##### (a) Disposal\n**(1) In general**\nThe Administrator of General Services (referred to in this section as the Administrator ) shall dispose of the following Federal buildings:\n**(A)**\nThe Frances Perkins Federal Building, located at 200 Constitution Avenue NW in Washington, DC.\n**(B)**\nThe James V. Forrestal Building, located at 1000 Independence Avenue SW in Washington, DC.\n**(C)**\nThe Theodore Roosevelt Federal Building, located at 1900 E. Street NW in Washington, DC.\n**(D)**\nThe Robert C. Weaver Federal Building, located at 451 7th Street SW in Washington, DC.\n**(E)**\nThe Department of Agriculture South Building, located at 1400 Independence Avenue SW in Washington, DC.\n**(F)**\nThe Hubert H. Humphrey Federal Building, located at 200 Independence Avenue SW in Washington, DC.\n**(2) Sale or ground lease**\nIn disposing of a Federal building described in paragraph (1), the Administrator may\u2014\n**(A)**\nsell the Federal building for fair market value at highest and best use; or\n**(B)**\nenter into a ground lease with a term of up to 99 years.\n**(3) Discretion of Administrator regarding transactions**\n**(A) In general**\nFor any disposal under paragraph (1), the Administrator may approve sale or ground lease transactions under such terms and conditions that the Administrator determines are in the best interests of the United States.\n**(B) Inclusions**\nA transaction for any sale or ground lease under paragraph (1) may include\u2014\n**(i)**\nrelocating any Federal agency that is occupying the applicable Federal building as of the date of the sale to another Federal building; or\n**(ii)**\na leaseback of the applicable Federal building if the leaseback is for a period of not more than 5 years.\n**(4) Exemption from certain requirements**\nExcept as provided in subsection (e)(1)(D), a disposal under paragraph (1) shall be exempt from the requirements of, as applicable\u2014\n**(A)**\nsection 501 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11411 );\n**(B)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. );\n**(C)**\ndivision A of subtitle III of title 54, United States Code (formerly known as the National Historic Preservation Act ); and\n**(D)**\nchapters 5 and 87 of title 40, United States Code.\n**(5) Prohibition on foreign ownership**\n**(A) Definitions**\nIn this paragraph, the terms beneficial owner , foreign entity , and foreign person have the meanings given those terms in section 2 of the Secure Federal LEASEs Act ( 40 U.S.C. 585 note; Public Law 116\u2013276 ).\n**(B) Prohibition**\nIn conducting a disposal required under paragraph (1), the Administrator may not sell any Federal building described in that paragraph to, or enter into a ground lease with, any foreign person, any foreign entity, or any entity of which a foreign person is a beneficial owner.\n##### (b) Relocating Federal agencies\n**(1) Discretion of Administrator**\nSubject to the conditions described in this subsection, the Administrator is vested with the sole and absolute authority and discretion to select the area, site, or location for any Federal agency relocated from a Federal building described in subsection (a)(1).\n**(2) Consultation with the Federal agency**\nThe Administrator shall\u2014\n**(A)**\nconsult with the head of a Federal agency relocated from a Federal building described in subsection (a)(1); and\n**(B)**\ntake into consideration the mission-related need of that Federal agency to relocate to a specific geographic location.\n**(3) Prohibition on build-to-suit leases**\nThe Administrator shall not enter into a build-to-suit lease where the Administrator contracts with a developer, person, or any other entity to design and construct a new building specifically to meet the unique requirements of a Federal agency relocated from a Federal building described in subsection (a)(1).\n**(4) Advance notice**\nNot later than 30 days before the date on which the Administrator publicly announces the relocation of a Federal agency to a location outside of the District of Columbia, the Administrator shall provide to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives notice of that announcement.\n**(5) Exemptions**\nActions taken by the Administrator and funds made available to the Administrator to carry out this subsection shall not be subject to\u2014\n**(A)**\nsection 3307 of title 40, United States Code; or\n**(B)**\nchapter 33 of title 41, United States Code (commonly known as the Competition in Contracting Act ).\n##### (c) Net proceeds\n**(1) In general**\nOf the net proceeds received from a disposal required under subsection (a)(1)\u2014\n**(A)**\nsuch amount as may be required to implement this section (including the costs required to relocate a Federal agency from a Federal building described in subsection (a)(1)), as determined by the Administrator, shall be deposited into an account in the Federal Buildings Fund established by section 592(a) of title 40, United States Code (referred to in this subsection as the Fund ); and\n**(B)**\nany additional amounts after the deposit required under subparagraph (A) shall be deposited into the general fund of the Treasury for purposes of reducing the deficit.\n**(2) Future appropriation**\nOn deposit of amounts into the Fund under paragraph (1)(A), those amounts may be expended only subject to a specific future appropriation.\n##### (d) Preclusion of judicial review\nAny action taken by the Administrator to carry out this section shall not be subject to judicial review, including under\u2014\n**(1)**\nsubchapter V of chapter 35 of title 31, United States Code; and\n**(2)**\nsubchapter II of chapter 5, and chapter 7, of title 5, United States Code (commonly known as the Administrative Procedure Act ).\n##### (e) Miscellaneous provisions\n**(1) Additional Federal buildings to be disposed**\n**(A) In general**\nOn providing 30 days advance notice to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives, and subject to subparagraphs (C) and (E), the Administrator may include additional Federal buildings described in subparagraph (B) to the list of Federal buildings described in subsection (a)(1) that are required to be disposed of pursuant to that subsection.\n**(B) Federal buildings described**\nA Federal building referred to in subparagraphs (A) and (D) is any Federal building\u2014\n**(i)**\nunder the jurisdiction, custody, and control of the Administrator; and\n**(ii)**\nthat has a utilization below 60 percent, on average, over the 1-year period preceding the date on which the Administrator provides notice of the disposal of the Federal building pursuant to subparagraph (A).\n**(C) Limitation**\nIn modifying the list of Federal buildings to be disposed of under subparagraph (A), the Administrator may not add more than 20 additional Federal buildings each calendar year.\n**(D) Exemptions from certain requirements**\nWith respect to a Federal building described in subparagraph (B) that is added to the list of Federal buildings described in subsection (a)(1) pursuant to subparagraph (A) and disposed of pursuant to subsection (a)(1)\u2014\n**(i)**\nthe exemption from the requirements of section 501 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11411 ) shall only apply to that sale if the Federal building is larger than 100,000 square feet; and\n**(ii)**\nthe exemption from the requirements of division A of subtitle III of title 54, United States Code (formerly known as the National Historic Preservation Act ), shall only apply to that sale if the Federal building is designated as a National Historic Landmark pursuant to chapter 3021 of that title.\n**(E) Congressional disapproval**\nA notice submitted to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives under subparagraph (A) shall be considered a rule for purposes of section 802 of title 5, United States Code.\n**(2) Availability of appropriations**\nNotwithstanding any other provision of law, any amounts made available for obligation in the Federal Buildings Fund established by section 592(a) of title 40, United States Code, in any previous or subsequent Act shall be available until expended for the purpose of any expense associated with relocating a Federal agency occupying a Federal building described in subsection (a)(1).\n**(3) Effect on other law**\nNothing in this section limits or supersedes any authority otherwise available to the Administrator under any other provision of law and the authorities provided under this section are in addition to, and not in lieu of, any existing authorities.\n**(4) Sunset**\n**(A) Termination of authority**\nExcept as provided in subparagraph (B), the authority provided under this section terminates on December 31, 2028.\n**(B) Effect on prior actions**\nThe termination of authority under subparagraph (A) shall not affect\u2014\n**(i)**\nany action taken, any right or duty that matured, or any proceeding commenced under this section before that termination of authority; or\n**(ii)**\nthe continued enforcement or implementation of any final rule, order, agreement, or decision issued pursuant to that authority prior to that termination.",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-10-30",
        "text": "Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S7851)"
      },
      "number": "3091",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DISPOSAL Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-08T16:59:00Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6675ih.xml"
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
      "title": "DISPOSAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DISPOSAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disposing of Inactive Structures and Properties by Offering for Sale And Lease Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of General Services to dispose of certain Federal buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:19Z"
    }
  ]
}
```
