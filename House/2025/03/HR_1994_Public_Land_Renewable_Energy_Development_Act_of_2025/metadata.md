# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1994
- Title: Public Land Renewable Energy Development Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1994
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-05-12T18:14:08Z
- Update date including text: 2025-05-12T18:14:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1994",
    "number": "1994",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Public Land Renewable Energy Development Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-12T18:14:08Z",
    "updateDateIncludingText": "2025-05-12T18:14:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:54:08Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-10T16:05:40Z",
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
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NV"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1994ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1994\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Gosar (for himself, Mr. Amodei of Nevada , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo promote the development of renewable energy on public lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Land Renewable Energy Development Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nSec. 4. Limited grandfathering.\nSec. 5. Disposition of revenues.\n#### 3. Definitions\nIn this Act:\n**(1) Covered land**\nThe term covered land means land that is\u2014\n**(A)**\nFederal land administered by the Secretary; and\n**(B)**\nnot excluded from the development of solar or wind energy under\u2014\n**(i)**\na land use plan; or\n**(ii)**\nother Federal law.\n**(2) Federal land**\nThe term Federal land means\u2014\n**(A)**\npublic lands; and\n**(B)**\nlands of the National Forest System as described in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(3) Fund**\nThe term Fund means the Renewable Energy Resource Conservation Fund established by section 5(c)(1).\n**(4) Renewable energy project**\nThe term renewable energy project means a project carried out on covered land that uses wind or solar energy to generate energy.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 4. Limited grandfathering\n##### (a) Definition of project\nIn this section, the term project means a system described in section 2801.9(a)(4) of title 43, Code of Federal Regulations (as in effect on the date of the enactment of this Act).\n##### (b) Requirement To pay rents and fees\nUnless otherwise agreed to by the owner of a project, the owner of a project that applied for a right-of-way under section 501 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1761 ) on or before December 19, 2016, shall be obligated to pay with respect to the right-of-way all rents and fees in effect before the effective date of the rule of the Bureau of Land Management entitled Competitive Processes, Terms, and Conditions for Leasing Public Lands for Solar and Wind Energy Development and Technical Changes and Corrections (81 Fed. Reg. 92122 (December 19, 2016)).\n#### 5. Disposition of revenues\n##### (a) Disposition of revenues\n**(1) Availability**\nExcept as provided in paragraph (2), beginning on January 1, 2026, of amounts collected from a wind or solar project as bonus bids, rentals, fees, or other payments under a right-of-way, permit, lease, or other authorization the following shall be made available, without further appropriation or fiscal year limitation, as follows:\n**(A)**\nTwenty-five percent shall be paid by the Secretary of the Treasury to the State within the boundaries of which the revenue is derived.\n**(B)**\nTwenty-five percent shall be paid by the Secretary of the Treasury to the one or more counties within the boundaries of which the revenue is derived, to be allocated among the counties based on the percentage of land from which the revenue is derived.\n**(C)**\nTwenty-five percent shall be deposited in the Treasury and be made available to the Secretary to carry out the program established under this Act, including the transfer of the funds by the Bureau of Land Management to other Federal agencies and State agencies to facilitate the processing of renewable energy permits on Federal land, with priority given to using the amounts, to the maximum extent practicable without detrimental impacts to emerging markets, to expediting the issuance of permits required for the development of renewable energy projects in the States from which the revenues are derived.\n**(D)**\nTwenty-five percent shall be deposited in the Renewable Energy Resource Conservation Fund established by subsection (c).\n**(2) Exceptions**\nParagraph (1) shall not apply to the following:\n**(A)**\nAmounts collected under section 504(g) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1764(g) ).\n**(B)**\nAmounts deposited into the National Parks and Public Land Legacy Restoration Fund under section 200402(b) of title 54, United States Code.\n##### (b) Payments to States and counties\n**(1) In general**\nAmounts paid to States and counties under subsection (a)(1) shall be used consistent with section 35 of the Mineral Leasing Act ( 30 U.S.C. 191 ).\n**(2) Payments in lieu of taxes**\nA payment to a county under paragraph (1) shall be in addition to a payment in lieu of taxes received by the county under chapter 69 of title 31, United States Code.\n##### (c) Renewable Energy Resource Conservation Fund\n**(1) In general**\nThere is established in the Treasury a fund to be known as the Renewable Energy Resource Conservation Fund, which shall be administered by the Secretary, in consultation with the Secretary of Agriculture.\n**(2) Use of funds**\nThe Secretary may make amounts in the Fund available to Federal, State, local, and Tribal agencies to be distributed in regions in which renewable energy projects are located on Federal land. Such amounts may be used to\u2014\n**(A)**\nrestore and protect\u2014\n**(i)**\nfish and wildlife habitat for affected species;\n**(ii)**\nfish and wildlife corridors for affected species; and\n**(iii)**\nwetlands, streams, rivers, and other natural water bodies in areas affected by wind or solar energy development; and\n**(B)**\npreserve and improve recreational access to Federal land and water in an affected region through an easement, right-of-way, or other instrument from willing landowners for the purpose of enhancing public access to existing Federal land and water that is inaccessible or restricted.\n**(3) Partnerships**\nThe Secretary may enter into cooperative agreements with State and Tribal agencies, nonprofit organizations, and other appropriate entities to carry out the activities described in paragraph (2).\n**(4) Investment of Fund**\n**(A) In general**\nAmounts deposited in the Fund shall earn interest in an amount determined by the Secretary of the Treasury on the basis of the current average market yield on outstanding marketable obligations of the United States of comparable maturities.\n**(B) Use**\nInterest earned under subparagraph (A) may be expended in accordance with this subsection.\n**(5) Report to Congress**\nAt the end of each fiscal year, the Secretary shall submit a report to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate that includes a description of\u2014\n**(A)**\nthe amount collected as described in subsection (a), by source, during that fiscal year;\n**(B)**\nthe amount and purpose of payments during that fiscal year to each Federal, State, local, and Tribal agency under paragraph (2); and\n**(C)**\nthe amount remaining in the Fund at the end of the fiscal year.\n**(6) Intent of Congress**\nIt is the intent of Congress that the revenues deposited and used in the Fund shall supplement (and not supplant) annual appropriations for activities described in paragraph (2).",
      "versionDate": "2025-03-10",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:14:08Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1994ih.xml"
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
      "title": "Public Land Renewable Energy Development Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:57:54Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote the development of renewable energy on public lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:33:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Land Renewable Energy Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    }
  ]
}
```
