# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4529?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4529
- Title: Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act
- Congress: 119
- Bill type: HR
- Bill number: 4529
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-09-12T16:56:29Z
- Update date including text: 2025-09-12T16:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4529",
    "number": "4529",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act",
    "type": "HR",
    "updateDate": "2025-09-12T16:56:29Z",
    "updateDateIncludingText": "2025-09-12T16:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-17T13:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NC"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "OH"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IN"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "LA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TN"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-07-17",
      "state": "HI"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4529ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4529\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. David Scott of Georgia (for himself, Mr. Jackson of Illinois , Ms. Adams , Mr. Bishop , Ms. Brown , Mr. Carson , Mr. Carter of Louisiana , Mr. Cohen , Mr. Fields , Mr. Figures , Mr. Johnson of Georgia , Ms. Kelly of Illinois , Ms. McClellan , Ms. Sewell , Mr. Soto , Ms. Strickland , Mr. Thanedar , Ms. Tokuda , Ms. Waters , Ms. Williams of Georgia , Ms. Wilson of Florida , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase market access for Black farmers and socially disadvantaged farmers and ranchers, to ensure civil rights accountability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act .\n#### 2. Food hub grants to increase market access for socially disadvantaged farmers and ranchers\n##### (a) Definitions\nIn this section:\n**(1) Agricultural food product**\nThe term agricultural food product means a raw, cooked, or a processed edible substance, beverage, or ingredient produced and otherwise prepared for sale in the United States (including any insular area (as defined in section 1404 of the National Agricultural, Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 ))), derived from one or more agricultural commodities of United States origin, and used or intended for use or for sale in whole or in part for human consumption.\n**(2) Donated food**\nThe term donated food has the meaning given the term in section 250.2 of title 7 of the Code of Federal Regulations (or any successor regulation).\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\nan entity formed by two or more agricultural producers, not less than half of whom are members of a socially disadvantaged group; or\n**(B)**\na non-profit organization or Tribal organization with demonstrated experience working with socially disadvantaged farmers or ranchers.\n**(4) Eligible partner**\nThe term eligible partner means a non-profit organization, a State cooperative extension service or a college or university (as such terms are defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )), Tribal organization, or other State or local government entities with demonstrated experience in providing assistance such as grants management, technical assistance, and business plan development, to agricultural producers.\n**(5) Food hub**\nThe term food hub means a business or organization that actively manages the aggregation, distribution, and marketing of source-identified agricultural food products from producers for wholesale, retail, or institutional markets.\n**(6) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(7) Socially disadvantaged farmer or rancher**\nThe term socially disadvantaged farmer or rancher has the meaning given the term in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ).\n**(8) Socially disadvantaged group**\nThe term socially disadvantaged group has the meaning given the term in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ).\n**(9) Tribal organization**\nThe term Tribal organization has the meaning given the term in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n##### (b) Grants To increase market access\n**(1) In general**\nThe Secretary shall establish a program to make grants on a competitive basis to eligible entities to support new or expanding food hubs designed to increase market access for socially disadvantaged farmers and ranchers, but may also increase market access for other farmers and ranchers.\n**(2) Use of funds**\nAn eligible entity selected to receive a grants under this subsection may use grants funds\u2014\n**(A)**\nto purchase and develop land, buildings, and associated infrastructure for commercial or industrial properties, including expansion or modernization, for use in processing, distributing, aggregating, storing, transporting, or marketing agricultural food products;\n**(B)**\nto construct or equip facilities for use in processing, distributing, aggregating, storing, transporting, or marketing agricultural food products;\n**(C)**\nto purchase machinery and equipment for use in processing, distributing, aggregating, storing, transporting, or marketing agricultural food products;\n**(D)**\nfor general operating expenses directly related to a food hub, including planning and development related to the establishment or expansion of any food hub;\n**(E)**\nto provide marketing services for agricultural food products, including providing platforms (such as electronic or web-based platforms) for sales, inventory, and aggregation; and\n**(F)**\nto conduct other activities supporting the development or expansion of a food hub, as determined by the Secretary.\n**(3) Application**\n**(A) In general**\nAn eligible entity seeking a grant under this subsection shall submit to the Secretary an application that contains\u2014\n**(i)**\na description of the activities the eligible entity will carry out to support one or more new or existing food hubs, including a plan for each such food hub to process, distribute, store, or market agricultural food products for wholesale, retail, or institutional markets;\n**(ii)**\na description of the ways in which each such food hub that the eligible entity is proposing to establish or expand is designed to increase market access for socially disadvantaged farmers or ranchers;\n**(iii)**\nexcept as provided in subparagraph (B), a description of the eligible entity\u2019s demonstrated competency to develop and manage each such food hub, provide fiscal accountability, collect data, and prepare reports and other necessary documentation; and\n**(iv)**\nany other information, as determined by the Secretary.\n**(B) Requirement to include eligible partners**\nAn eligible entity that does not have one or more of the demonstrated competencies described in clause (iii) of subparagraph (A) shall submit to the Secretary in its application\u2014\n**(i)**\na list of one or more eligible partners such eligible entity is partnering with;\n**(ii)**\nthe responsibilities of each eligible partner in supporting such eligible entity; and\n**(iii)**\na description of the demonstrated competencies of the eligible partner or partners in performing such responsibilities.\n**(C) Eligible entities serving as eligible partners**\nAn eligible entity specified in subparagraph (B) of subsection (a)(3) seeking a grant under this section may serve as an eligible partner for other eligible entities in one or more grant applications under this subsection.\n**(4) Priority**\nIn making grants under this subsection, the Secretary may give priority to grant applications for food hubs that\u2014\n**(A)**\nbenefit underserved communities, as defined in section 310B(g)(9)(A)(ii) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(g)(9)(A)(ii) );\n**(B)**\naggregate, distribute, and market agricultural food products that meet the standards for donated foods, as determined by the Secretary; or\n**(C)**\nhave not been awarded a Department of Agriculture grant, including a grant under section 210A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c ), in the preceding or current fiscal year.\n**(5) Maximum grant term**\nThe term of a grant under this subsection may not exceed 5 years.\n**(6) No matching funds**\nAn eligible entity receiving a grant under this section shall not be required to provide non-Federal matching funds with respect to such grant.\n##### (c) Prioritizing Purchases for USDA Domestic Food Assistance Programs\n**(1) In general**\nThe Secretary shall establish a process\u2014\n**(A)**\nto prioritize the purchase of agricultural food products from socially disadvantaged farmers and ranchers, including from food hubs developed or expanded under this section, for use in Department of Agriculture programs that distribute agricultural food products within the United States (including any insular area (as defined in section 1404 of the National Agricultural, Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 ))); and\n**(B)**\nthat is designed to account for barriers to market entry faced by socially disadvantaged farmers and ranchers while maintaining the integrity of the purchasing process established under this subsection, including ensuring that any entity that is suspended or debarred from participation in any Federal program is not eligible to participate in the purchasing process established under this subsection.\n**(2) Waivers**\n**(A) In general**\nIn establishing the process described in paragraph (1), the Secretary may provide for the waiver of the full and open competition procedures for the award of Federal contracts, section 3324 of title 31, United States Code, and section 725 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agencies Appropriations Act, 2001 ( 7 U.S.C. 2209f ), if the Secretary identifies requirements under such sections and procedures as presenting barriers to market entry for socially disadvantaged farmers and ranchers.\n**(B) Notification**\nNot later than 10 days after providing for any waiver under subparagraph (A), the Secretary shall notify the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate of such waivers and provide a description of how such waivers would address barriers to market entry for socially disadvantaged farmers and ranchers for a particular agricultural food product.\n##### (d) Reports\nNot later than December 31, 2026, and each December thereafter until the completion of the grants awarded under subsection (b), the Secretary shall make publicly available on the Department of Agriculture\u2019s website and submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, a report that includes\u2014\n**(1)**\na description of the status of each grant awarded under subsection (b);\n**(2)**\nthe number of socially disadvantaged farmers and ranchers participating in the food hub supported by such grant in the previous fiscal year;\n**(3)**\nto the maximum extent practicable, the amount of agricultural food products produced by socially disadvantaged farmers and ranchers processed, distributed, aggregated, stored, or marketed by the food hub supported by such grant in the previous fiscal year; and\n**(4)**\nthe total amount of donated food purchased by the Secretary from food hubs supported with grants awarded under this section in the previous fiscal year.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out subsection (b) $100,000,000 for fiscal year 2026, to remain available until expended.\n#### 3. Agriculture hub credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45U. Agriculture hub credit (a) In general For purposes of section 38, the agriculture hub credit determined under this section for any taxable year is an amount equal to 25 percent of the qualified food hub expenses for the taxable year. (b) Qualified food hub expenses For purposes of this section, the term qualified food hub expenses means amounts paid or incurred by the taxpayer during the taxable year\u2014 (1) for agricultural food products from a food hub developed or expanded under section 2 of the Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act , and (2) in accordance with a contract certified by the Secretary of Agriculture under section 3(c) of the Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act . (c) Food hub The term food hub has the meaning given such term in section 2 of the Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act . (d) Termination This section shall not apply to taxable years beginning after the Secretary determines the grant program under section 2 of the Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act has ended. .\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (32), by striking plus at the end,\n**(B)**\nin paragraph (33), by striking the period at the end and inserting , plus , and\n**(C)**\nby adding at the end the following new paragraph:\n(34) the agriculture hub credit determined under section 45U(a). .\n**(2)**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45U. Agriculture hub credit. .\n**(3)**\nSection 280C of such Code is amended by adding at the end the following new subsection:\n(i) Agriculture hub credit Any deduction or other credit otherwise allowable with respect to an expense for which a credit is allowed under section 45U(a) shall be reduced by the amount of the credit under section 45U(a) with respect to such expense. If a credit is allowed under section 45U(a) with respect to property of a kind which would properly be included in the inventory of the taxpayer if on hand at the close of the taxable year or property held by the taxpayer primarily for sale to customers in the ordinary course of the trade or business of such taxpayer, opening inventory or purchases shall be reduced by the amount of the credit so allowed. .\n##### (c) Certification process\nNot later than 1 year after the date of enactment of this section, the Secretary of Agriculture shall issue regulations to establish a process to certify, at the request of entities seeking an agriculture hub credit section 45U of the Internal Revenue Code of 1986, as added by subsection (b), that a contract under which expenditures referred to in such section 45U are made\u2014\n**(1)**\nis not between related parties;\n**(2)**\nis the result of arm\u2019s length negotiations; and\n**(3)**\nmeets any other requirements, as determined by the Secretary of Agriculture, in consultation with the Secretary of Treasury.\n##### (d) Effective date\nThe amendments made by this section shall apply to expenses paid or incurred in taxable years beginning after December 31, 2025.\n#### 4. Civil rights accountability for USDA employees\n##### (a) In general\nThe Secretary of Agriculture shall ensure that officials and employees of the Department of Agriculture are held accountable in accordance with subsection (b) if, while in the course of their employment or in administering a Department of Agriculture program, such officials and employees are found to have engaged in any discriminatory actions, retaliatory actions, harassment, civil rights violations, or related misconduct, including any such actions or misconduct involving any of the following:\n**(1)**\nFailure to provide a receipt for service in accordance with section 2501A(e) of the Food, Agriculture, Conservation or Trade Act of 1990 ( 7 U.S.C. 2279\u20131(e) ) to any current or prospective applicants of or participants in Department of Agriculture programs.\n**(2)**\nProviding an inaccurate receipt for service under such section 2501A(e) to any current or prospective applicants of or participants in Department of Agriculture programs.\n**(3)**\nFailure to provide appropriate information regarding relevant programs and services at the Department of Agriculture, when requested by any current or prospective applicants of or participants in Department of Agriculture programs.\n**(4)**\nFailure to timely process applications or otherwise delaying program services to any current or prospective applicants of or participants in, Department of Agriculture programs.\n##### (b) Taking corrective action\nThe Secretary shall ensure that appropriate corrective action is taken with respect to any official or employee of the Department of Agriculture who has been found to have engaged in any of the actions, violations, or misconduct referred to in subsection (a) while in the course of such official\u2019s or employee\u2019s employment or in administering a Department of Agriculture program\u2014\n**(1)**\nin any administrative finding by the Department of Agriculture, including any final agency decision issued by the Assistant Secretary of Agriculture for Civil Rights and any civil rights compliance review or misconduct investigation conducted by the Department of Agriculture;\n**(2)**\nin any administrative or judicial proceeding;\n**(3)**\nin any civil rights settlement;\n**(4)**\nin any audit or investigation conducted by the Office of the Inspector General of the Department of Agriculture; or\n**(5)**\nin any investigation conducted by the Office of the Special Counsel.\n##### (c) Corrective action defined\nIn this section, the term corrective action means any action taken to respond to any of the actions, violations, or misconduct referred to in subsection (a) that\u2014\n**(1)**\nwould enhance civil rights at the Department of Agriculture, including any policy or programmatic changes to prevent similar misconduct from occurring in the future; and\n**(2)**\nmay include disciplinary actions, including\u2014\n**(A)**\nremoval from Federal service;\n**(B)**\nsuspension without pay;\n**(C)**\nany reduction in grade or pay; and\n**(D)**\nletter of reprimand.\n#### 5. Equitable relief\n##### (a) Equitable relief from ineligibility for loans, payments, or other benefits\nSection 1613 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 7996 ) is amended\u2014\n**(1)**\nby redesignating subsections (f) through (j) as subsections (g) through (k), respectively;\n**(2)**\nby inserting after subsection (e) the following:\n(f) Equitable relief by the Assistant Secretary of Agriculture for Civil Rights (1) In general The Assistant Secretary of Agriculture for Civil Rights (or a designee of the Secretary in the Office of the Assistant Secretary for Civil Rights, if no Assistant Secretary of Agriculture for Civil Rights is confirmed in accordance with section 218(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6918(b) )) may grant relief in accordance with subsections (b) through (d) to a participant who files a civil rights program complaint. (2) Decisions The decision by the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) to grant relief under this subsection shall not require prior approval by any officer or employee of the Department of Agriculture. (3) Other authority The authority provided to the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) under this subsection is in addition to any other applicable authority and does not limit other authority provided by law or the Secretary. ;\n**(3)**\nin subsection (g), as so redesignated, by striking or the State Conservationist and inserting the State Conservationist, or the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) ; and\n**(4)**\nin paragraph (1) of subsection (h), as so redesignated, by striking and (e) and inserting (e), and (f) .\n##### (b) Equitable relief for actions taken in good faith\nSection 366 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008a ) is amended\u2014\n**(1)**\nby amending subsection (b) to read as follows:\n(b) Limitation The Secretary may only provide relief to a farmer or rancher under subsection (a) if the Secretary determines that the farmer or rancher\u2014 (1) acting in good faith, relied on an action of, or the advice of, the Secretary (including any authorized representative of the Secretary) to the detriment of the farming or ranching operation of the farmer or rancher; or (2) failed to comply fully with the requirements of a program described in subsection (a)(1), but made a good faith effort to comply with the requirements. ;\n**(2)**\nby inserting after subsection (d) the following:\n(e) Equitable relief by the assistant secretary of agriculture for civil rights (1) In general The Assistant Secretary of Agriculture for Civil Rights (or a designee of the Secretary in the Office of the Assistant Secretary for Civil Rights, if no Assistant Secretary of Agriculture for Civil Rights is confirmed in accordance with section 218(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6918(b) )) may grant relief in accordance with subsections (a) through (d) to an individual who files a civil rights program complaint. (2) Decisions The decision by the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) to grant relief under this subsection shall not require prior approval by any officer or employee of the Department of Agriculture. (3) Other authority The authority provided to the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) under this subsection is in addition to any other applicable authority and does not limit other authority provided by law or the Secretary. ;\n**(3)**\nby redesignating subsection (e) as subsection (f); and\n**(4)**\nin subsection (f), as so redesignated, by striking Secretary and inserting Secretary, or the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) .\n#### 6. Burden of Proof for National Appeals Division Hearings\nSection 277(c)(4) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6997(c)(4) ) is amended to read as follows:\n(4) Burden of proof The agency shall bear the burden of proving by substantial evidence that the adverse decision of the agency was valid. .\n#### 7. Office of the Civil Rights Ombudsperson\nTitle III of the Federal Crop Insurance Reform and Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 2231b et seq. ) is amended by adding at the end the following:\n310. Office of the Civil Rights Ombudsperson (a) In general Not later than 120 days after the date of enactment of this section, the Secretary shall establish an Office of the Civil Rights Ombudsperson (in this section referred to as the Office ) within the Department. The Office shall be independent of Department agencies and offices. (b) Ombudsperson designation The Secretary shall designate a Civil Rights Ombudsperson (in this section referred to as the Ombudsperson ) for the Office. The Ombudsperson shall be considered a senior official of the Department and have a background in civil rights enforcement. (c) Office personnel The Ombudsperson shall appoint such employees as are necessary to perform the functions of the Office and for the administration of the Office. (d) Functions The functions of the Office shall be\u2014 (1) to assist producers and other customers of Department programs in navigating the civil rights review process; (2) to ensure that participants (as defined in section 271) are aware of the appeals process under subtitle H of title II, including informal hearings under section 275; (3) to promote awareness of the Office and its responsibilities among producers and other customers of Department programs; and (4) to raise issues and concerns with respect to, and make recommendations to the Secretary about, equitable access or implementation of Department programs. (e) Access to information (1) In general Subject to paragraph (2), the Secretary shall establish procedures to provide the Office access to all departmental records necessary to execute the functions of the Office under subsection (d). (2) Timelines The procedures described in paragraph (1) shall include a requirement that requests from the Office for departmental records shall be fulfilled not later than 60 days after the request is made. (f) Annual report Beginning not later than 1 year after the date of the enactment of this section, and annually thereafter, the Ombudsperson shall prepare and submit to the House Committee on Agriculture and the Senate Committee on Agriculture, Nutrition, and Forestry a report on\u2014 (1) the activities carried out by the Office; and (2) the findings and recommendations of the Office with respect to equitable access or implementation of Department programs. (g) Authorization of appropriations There is authorized to be appropriated such sums as are necessary to carry out this section for each of fiscal years 2026 through 2028. .",
      "versionDate": "2025-07-17",
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
        "updateDate": "2025-09-12T16:56:29Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4529ih.xml"
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
      "title": "Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Black Farmers and Socially Disadvantaged Farmers Increased Market Share Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase market access for Black farmers and socially disadvantaged farmers and ranchers, to ensure civil rights accountability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T05:18:35Z"
    }
  ]
}
```
