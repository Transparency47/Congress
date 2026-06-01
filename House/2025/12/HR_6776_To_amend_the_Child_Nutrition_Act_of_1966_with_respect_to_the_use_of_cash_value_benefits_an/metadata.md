# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6776
- Title: Farmers to Families Act
- Congress: 119
- Bill type: HR
- Bill number: 6776
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-22T08:07:38Z
- Update date including text: 2026-05-22T08:07:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6776",
    "number": "6776",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Farmers to Families Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:38Z",
    "updateDateIncludingText": "2026-05-22T08:07:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2025-12-17",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:08:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:27:53Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-17T14:08:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sponsorshipDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6776ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6776\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Underwood (for herself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Child Nutrition Act of 1966 with respect to the use of cash-value benefits and coupons for purchases of fresh, nutritious, unprepared foods from community supported agricultural entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers to Families Act .\n#### 2. Use of cash-value benefits and coupons for certain local foods\nThe Child Nutrition Act of 1966 is amended by inserting after section 17 ( 42 U.S.C. 1786 ) the following:\n18. Use of cash-value benefits and coupons for certain local foods (a) Purchases of certain local foods Not later than 18 months after the date of the enactment of this section, the Secretary shall allow cash-value benefit funds and coupon funds to be used by participants and recipients to purchase fresh, local, nutritious, unprepared foods, including pre-order boxes of such foods, from a covered agricultural entity. (b) Single EBT access device for cash-Value benefits and coupon funds (1) In general Not later than 18 months after the date of the enactment of this section, a State agency\u2014 (A) shall provide cash-value benefit funds and coupon funds through the electronic benefits transfer system of such State established pursuant to section 17(h)(12); (B) shall ensure such coupon funds can be accessed through the electronic benefits transfer access device provided to participants pursuant to section 17(h)(12); and (C) may provide different payment mechanisms on such access device that separate the funds stored on such access device based on if the funds are cash-value benefit funds or coupon funds. (2) Processing of payments (A) In general A State agency shall require a community supported agricultural entity to use a qualified payment device from the list established pursuant to subparagraph (B)(i) to accept payments from an electronic benefits transfer access device described in paragraph (1)(A). (B) Qualified payment device (i) Rulemaking Not later than 18 months after the date of the enactment of this section, the Secretary shall issue regulations establishing a list of payment devices that the Secretary determines to be qualified payment devices for the purposes of subparagraph (A). (ii) Criteria In issuing regulations under clause (i), the Secretary shall ensure that each payment device included on the list established pursuant to clause (i) is a singular device that can accept and process, without requiring an additional device, payments from an electronic benefits transfer access device described in paragraph (1)(A), including payments from cash-value benefit funds and coupon funds stored on such card. (iii) Updates The Secretary shall review and update on a regular basis the regulations issued under clause (i). (c) Definitions In this section: (1) Cash-value benefit The term cash-value benefit has the meaning given the term cash-value voucher in section 246.2 of title 7, Code of Federal Regulations (or successor regulations). (2) Covered agricultural entity The term covered agricultural entity means\u2014 (A) any food hub, farmers\u2019 market, or other distributor that markets local food from farmers to consumers; (B) a community supported agriculture program (as such term is defined in section 249.2 of title 7, Code of Federal Regulations (or successor regulations)); or (C) a farmer (as such term is defined in section 249.2 of title 7, Code of Federal Regulations (or successor regulations)). (3) Coupon The term coupon has the meaning given the term in section 17(m)(10). (4) Participant The term participant means a participant in the supplemental nutrition program for women, infants, and children under section 17. (5) Recipient The term recipient has the meaning given the term in section 17(m)(10). (6) State agency The term State agency means a State agency (as defined in subsection (b) of section 17) that administers a program pursuant to a grant under subsection (m) of such section. .\n#### 3. Farmers\u2019 market nutrition program for WIC participants\n##### (a) Inclusion of covered agricultural entities\nSection 17(m)(1) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m)(1) ) is amended\u2014\n**(1)**\nby striking foods at farmers\u2019 markets and (at the option of a State) roadside stands, as defined in the State plans submitted under this subsection and inserting foods, at\u2014 ; and\n**(2)**\nby adding at the end the following:\n(A) farmers\u2019 markets, as defined in the State plans submitted under this subsection; (B) roadside stands, as defined in the State plans submitted under this subsection; and (C) in accordance with section 18(a), covered agricultural entities (as such term is defined in section 18(c)). .\n##### (b) Automatic streamline of benefits\nSection 17(m)(5) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m)(5) ) is amended by adding at the end the following:\n(H) That each farmer (as such term is defined in section 249.2 of title 7, Code of Federal Regulations (or successor regulations)) is automatically authorized as a covered agricultural entity (as such term is defined in section 18(c)) for purposes of this subsection. .\n#### 4. WIC administrative support\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Agriculture shall include on a publicly available website of the Department of Agriculture\u2014\n**(1)**\na single application portal for producers to be\u2014\n**(A)**\nauthorized as a farmer for purposes of section 17(m) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m) ) to sell fresh, local, nutritious, unprepared foods to an individual described in paragraph (5)(A) of such section 17(m); and\n**(B)**\nin accordance with section 17(m)(5)(H) of such Act, authorized as a covered agricultural entity under section 18 of such Act, as added by this Act, to sell fresh, local, nutritious, unprepared foods to an individual described in paragraph (5)(A) of such section 17(m);\n**(2)**\nguidance for\u2014\n**(A)**\nState WIC offices administering WIC;\n**(B)**\nfarmers; and\n**(C)**\nfarmers\u2019 markets; and\n**(3)**\nbest practices for State agencies and local agencies carrying out\u2014\n**(A)**\na farmers\u2019 market nutrition program for WIC participants pursuant to a grant under section 17(m) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m) ); and\n**(B)**\nthe requirements under section 18 of such Act, as added by this Act.\n#### 5. Technical Assistance Center for farmers\u2019 market operators and farmers\n##### (a) Establishment\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Agriculture shall\u2014\n**(1)**\nestablish a Technical Assistance Center for farmers\u2019 market operators and farmers (in this section referred to as the Center ); and\n**(2)**\nto the extent practicable, consult on the design and scope of the Center with farmers, farmers\u2019 market managers, State agencies, and community organizations with experience in implementation of Federal nutrition benefits.\n##### (b) Administration\n**(1) Selection process**\nTo carry out the activities of the Center under subsection (c), the Secretary shall seek to enter into a cooperative agreement, on a competitive basis, with an eligible entity.\n**(2) Application**\nAn eligible entity seeking to enter into a cooperative agreement shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(3) Panel review**\n**(A) In general**\nNot later than 18 months after the date of the enactment of this Act, the Secretary shall establish a panel\u2014\n**(i)**\nto review applications submitted to the Secretary under paragraph (2); and\n**(ii)**\nto make recommendations to the Secretary with respect to selecting an eligible entity under paragraph (1) in accordance with subparagraph (C).\n**(B) Members**\nThe panel established under subparagraph (A) shall include at least\u2014\n**(i)**\n1 member with experience as a farmers\u2019 market manager; and\n**(ii)**\n1 member with experience providing technical assistance to farmers regarding accepting Federal nutrition benefits.\n**(C) Selection criteria**\nThe panel established under subparagraph (A) shall only recommend eligible entities to the Secretary with respect to selecting an eligible entity under paragraph (1) that the panel has determined to possess expertise in providing training and technical assistance to farmers\u2019 markets and farmers regarding Federal nutrition programs.\n**(4) Priority**\nIn selecting an eligible entity under paragraph (1), the Secretary shall give priority to an eligible entity that\u2014\n**(A)**\nhas experience engaging with Federal nutrition programs administered by the Department, such as FMNP, WIC, or other nutrition incentive programs; and\n**(B)**\nhas a history of effectively serving small and mid-sized farms, local agriculture, and underserved communities.\n**(5) Eligible entity defined**\nFor purposes of this subsection, the term eligible entity means\u2014\n**(A)**\na nonprofit organization;\n**(B)**\nan institution of higher education;\n**(C)**\na cooperative extension service;\n**(D)**\na regional food system network; or\n**(E)**\nany other entity with demonstrated capacity to carry out the activities described in subsection (c), as determined by the Secretary.\n##### (c) Activities\nThe Center shall provide services related to the programs under section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m) ) and section 18 of such Act, as added by this Act, including\u2014\n**(1)**\nassisting farmers and farmers\u2019 market operators with understanding and complying with eligibility, application, and authorization requirements\u2014\n**(A)**\nunder the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. );\n**(B)**\nunder the FMNP;\n**(C)**\nunder the SFMNP; and\n**(D)**\nfor accepting cash-value benefits;\n**(2)**\nproviding training to farmers\u2019 market managers and local farm vendors on how to accept electronic benefits transfer payments from recipients and participants of such programs, including guidance on the use of qualified payment devices authorized by the Secretary under section 18(b)(2)(B) of such Act, as added by this Act;\n**(3)**\ncreating, maintaining, and distributing resources and best practices for the acceptance and administration of nutrition benefits in farmers\u2019 market settings;\n**(4)**\nsharing implementation information with State agencies, local agencies, stakeholders and other technical assistance providers in a timely manner; and\n**(5)**\ncollecting and analyzing information on related program outcomes.\n##### (d) Annual report\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Center shall submit to the Secretary and relevant congressional committees a report that\u2014\n**(1)**\nsummarizes the activities of the Center, including the information collected pursuant to subsection (c)(5); and\n**(2)**\nmakes recommendations on how to encourage farmers and farmers\u2019 markets to engage with programs under section 17(m) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m) ) and section 18 of such Act, as added by this Act.\n#### 6. Definitions\nIn this Act:\n**(1) Cash-value benefit**\nThe term cash-value benefit has the meaning given the term cash-value voucher in section 246.2 of title 7, Code of Federal Regulations (or successor regulations).\n**(2) Cooperative extension service**\nThe term cooperative extension service has the meaning given such term in section 1404 of the Food and Agriculture Act of 1977 ( 7 U.S.C. 3103 ).\n**(3) Covered agricultural entity**\nThe term covered agricultural entity has the meaning given the term in section 18 of the Child Nutrition Act of 1966, as added by this Act.\n**(4) Farmer**\nThe term farmer has the meaning given the term in section 249.2 of title 7, Code of Federal Regulations (or successor regulations).\n**(5) FMNP**\nThe term FMNP means the farmers\u2019 market nutrition program for WIC participants under section 17(m) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(m) ).\n**(6) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(7) SFMNP**\nThe term SFMNP means the senior farmers\u2019 market nutrition program under section 4402 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007 ).\n**(8) WIC**\nThe term WIC means the special supplemental nutrition program for women, infants, and children under section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ).\n**(9) WIC terms**\nThe terms State agency and local agency have the meanings given the terms, respectively, in section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ).",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-21T16:11:16Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6776ih.xml"
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
      "title": "Farmers to Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmers to Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Nutrition Act of 1966 with respect to the use of cash-value benefits and coupons for purchases of fresh, nutritious, unprepared foods from community supported agricultural entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:40Z"
    }
  ]
}
```
