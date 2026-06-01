# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6697?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6697
- Title: EAT Healthy Foods from Local Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 6697
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-05-16T08:08:00Z
- Update date including text: 2026-05-16T08:08:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6697",
    "number": "6697",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001216",
        "district": "8",
        "firstName": "Kim",
        "fullName": "Rep. Schrier, Kim [D-WA-8]",
        "lastName": "Schrier",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "EAT Healthy Foods from Local Farmers Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:00Z",
    "updateDateIncludingText": "2026-05-16T08:08:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:07:02Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6697ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6697\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Ms. Schrier (for herself, Mr. Van Drew , and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Emergency Food Assistance Act of 1983 to provide additional agricultural products for distribution by emergency feeding organizations; and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Access To Healthy Foods from Local Farmers Act or the EAT Healthy Foods from Local Farmers Act .\n#### 2. Amendments\n##### (a) Purchase of priority agricultural products\nSection 203D of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7507 ) is amended\u2014\n**(1)**\nin subsection (a) by inserting or that State agencies purchase using funds made available under subsection (d), after distribution, ,\n**(2)**\nin subsection (b) by inserting or purchased after donated ,\n**(3)**\nby striking subsection (c),\n**(4)**\nin subsection (d)\u2014\n**(A)**\nby striking (d) and inserting (c) , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A) by striking subparagraphs (B) and (C) and inserting subparagraph (B) ,\n**(ii)**\nby striking subparagraph (B), and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B), and\n**(5)**\nby inserting after subsection (c) the following:\n(d) Projects for States To purchase certain commodities from eligible entities (1) Definitions In this subsection: (A) Project The term project means the purchase of priority agricultural products from eligible entities, and the distribution of those products to needy persons through emergency feeding organizations under subsection (a). (B) Priority agricultural product The term priority agricultural product means a fruit, vegetable, dairy, meat, seafood, grain, poultry, or other commodity food product, available for sale by eligible entities and that States determine to be appropriate for distribution through emergency feeding organizations and culturally or religiously relevant to the local communities that will distribute the products. (C) Eligible entity The term eligible entity means any of the following small businesses that is a grower, packer, processor, distributor, food-hub, or a cooperative, and that\u2014 (i) is\u2014 (I) underserved, including women-owned or veteran-owned; or (II) composed of, or sources agricultural products from, beginning farmers, or small or mid-sized farms that are structured as family farms; (ii) can deliver the priority agricultural products to emergency feeding organizations selected by the State as being most in need of the products; and (iii) that is committed to serving communities in need and forging strong relationships with emergency feeding organizations, public agencies, and Tribal governments through a project, as determined by the State. (2) Federal funding for projects (A) In general Subject to subparagraph (C) and paragraph (4), using funds made available under paragraph (5), the Secretary may provide funds to States to pay for the costs of carrying out a project. (B) Guidance Not later than 180 days after the date of enactment of this Act, the Secretary shall issue guidance to States\u2014 (i) to carry out this section; (ii) to inform States of their allocations under paragraph (3); (iii) to encourage States to partner with a wide range of emergency feeding organizations to reach communities in need, including those disproportionately impacted by food insecurity; and (iv) to inform States of public reporting requirements and minimum project performance standards, as developed by the Secretary. (C) Allocation (i) Eligibility for allocation The Secretary shall allocate funds made available under paragraph (5) based on the formula in effect under section 214(a), among States that submit a State plan of operation for a project that includes\u2014 (I) a list of eligible entities and emergency feeding organizations in the State that will operate the project in partnership with the State agency; (II) at the option of the State, a list of priority agricultural products located in the State that are available for purchase and transport to emergency feeding organizations to identify which foods may be included in the project; (III) a time line of when the project will begin operating; and (IV) a plan to comply with the standards set out in subparagraph (B)(iv). (ii) Reallocation If the Secretary determines that a State will not expend all the funds allocated to the State under clause (i), the Secretary shall reallocate the unexpended funds to other eligible States. (iii) Report Each State that receives funds allocated under this subparagraph shall submit to the Secretary financial reports on a regular basis describing the use of the funds. (3) Project purposes A State may only use Federal funds received under paragraph (2) for a project the purposes of which are\u2014 (A) to maintain and improve food and agricultural supply chain resiliency; (B) to provide food to individuals in need; and (C) to build relationships between the State, eligible entities and emergency feeding organizations through the purchase of food. (4) Cooperative agreements (A) In general A State agency that carries out a project using Federal funds received under this subsection may enter into cooperative agreements with State agencies of other States under section 203B(d) to maximize the use of commodities purchased under the project. (B) Submission Not later than 15 days after entering into a cooperative agreement under clause (i), a State agency shall submit such agreement to the Secretary. (5) Funding There is authorized to be appropriated to the Secretary to carry out this subsection $200,000,000 for each of fiscal years 2026 through 2030, to remain available until the end of the respective subsequent fiscal year. (6) Reporting Not later than 4 years after the effective date of this subsection, the Secretary shall submit to the Committee of Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report containing\u2014 (A) an evaluation of the effectiveness of this subsection in providing nutritious food to individuals in need, improving agricultural supply chain resiliency, and expanding economic opportunity for eligible entities; and (B) recommendations for the implementation of this subsection to improve nutrition outcomes. .\n##### (b) Conforming amendment\nSection 202A(b)(5) of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7503(b)(5) ) is amended by striking donated commodities received under section 203D(d) and inserting commodities donated under subsection (c), or purchased under subsection (d), of section 203D .\n#### 3. Intradepartmental coordination\n##### (a) Working group\nThe Secretary of Agriculture shall create a cross-agency working group within the office of the Secretary to work with relevant agencies and organizations of the Department of Agriculture and with stakeholders to review and reconsider how all Department procurement of priority agricultural products can be directed to support a wider range of agricultural producers and agricultural product distributors in a manner that meets the Department\u2019s overarching goals of nutrition security, greater access to culturally or religiously relevant foods for individuals and households, resilient local and regional food systems, rural job creation, and reversal of the concentration of the ownership of the resources for the production and distribution of agricultural products.\n##### (b) Annual report\nThe working group established under subsection (a) shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, an annual report describing the working group\u2019s accomplishments, suggestions, and recommendations for administrative actions and proposed legislation relating to the activities of such group under such subsection.",
      "versionDate": "2025-12-12",
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
        "updateDate": "2026-01-06T16:57:42Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6697ih.xml"
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
      "title": "EAT Healthy Foods from Local Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:54:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EAT Healthy Foods from Local Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Access To Healthy Foods from Local Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Emergency Food Assistance Act of 1983 to provide additional agricultural products for distribution by emergency feeding organizations; and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:48:43Z"
    }
  ]
}
```
