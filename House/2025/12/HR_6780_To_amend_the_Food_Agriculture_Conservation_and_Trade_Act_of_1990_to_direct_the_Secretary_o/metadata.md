# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6780
- Title: Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act
- Congress: 119
- Bill type: HR
- Bill number: 6780
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-22T08:07:24Z
- Update date including text: 2026-05-22T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6780",
    "number": "6780",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:24Z",
    "updateDateIncludingText": "2026-05-22T08:07:24Z"
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-12-17T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:28:45Z",
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
          "date": "2025-12-17T14:02:45Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "DC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "WI"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6780ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6780\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Brownley (for herself, Mr. Khanna , Mr. Mullin , Mr. Lieu , Ms. Tokuda , and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Secretary of Agriculture to establish research centers of excellence for alternative protein innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nProtein innovation that produces high-quality foods using under-utilized biomass and biomanufacturing processes is an essential component of the bioeconomy.\n**(2)**\nThe United States has produced several groundbreaking biotechnological breakthroughs across the last decade that can diversify the food system.\n**(3)**\nIn recent years, multiple countries have dramatically increased public investments into alternative protein research and development.\n**(4)**\nAccording to the Department of Agriculture, every $1 of investment into agricultural research results in $20 of economic productivity.\n**(5)**\nAs of 2019, the plant-based food industry supported over 55,000 jobs in the United States, and the protein sector could create as many as 10,000,000 jobs globally by 2050.\n**(6)**\nDiversifying the protein supply of the United States will increase domestic supply chain resilience, decrease reliance on foreign grain and other commodities, and provide more choices to American consumers.\n**(7)**\nThe global demand for meat is predicted to double by 2050, thus increasing the need for additional food sources.\n**(8)**\nA diversified food system would improve global and domestic food security.\n**(9)**\nProtein innovation can strengthen national security, improve supply chain resilience, and lower the risk of bioterrorism.\n#### 3. Research centers of excellence for food and agriculture innovation\nSection 1673 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5926 ) is amended by adding at the end the following:\n(e) Centers of Excellence for Food and Agriculture Innovation (1) Recognition The Secretary shall recognize not fewer than 3 centers of excellence, one of which will be led by an 1890 Institution (as defined in section 2 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7601 )), to focus on the areas specified in paragraph (2) relating to the advancement of emerging and innovative food and agriculture with an emphasis on diversifying edible protein sources. (2) Areas of focus (A) Food biomanufacturing research and development A center of excellence recognized under paragraph (1) may carry out research, development, and education programs that support the quality, production, or cost-effectiveness of emerging and innovative foods that employ\u2014 (i) bioprocessing; (ii) biomanufacturing; and (iii) the conversion of biomass into proteins and fats at scale. (B) Student success and workforce development A center of excellence recognized under paragraph (1) may engage in activities to ensure that students have the skills and education needed to work in innovative food and agriculture industries, including agricultural science, technology, engineering, mathematics, and related fields of study. (3) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $15,000,000 for each of fiscal years 2026 through 2030. (4) Report Not later than 1 year after the date of enactment of the Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act , and every year thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report describing\u2014 (A) the resources invested in the centers of excellence recognized under paragraph (1); and (B) the work being done by such centers of excellence. .\n#### 4. Agriculture and Food Research Initiative\nSection 2(b)(2)(E) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b)(2)(E) ) is amended\u2014\n**(1)**\nby redesignating clauses (ii) through (v) as clauses (iii) through (vi), respectively; and\n**(2)**\nby inserting after clause (i) the following new clause:\n(ii) tools and production methods that increase the availability of edible protein sources using bioprocessing, biomanufacturing, and the conversion of under-utilized biomass into high-value ingredients; .\n#### 5. Agricultural Research Service\n##### (a) Establishment of national program\nThe Secretary of Agriculture, acting through the Administrator of the Agricultural Research Service (referred to in this section as the Secretary ), shall establish a new national program dedicated to protein security that increases rural prosperity and farmer profits, which is focused on\u2014\n**(1)**\nbioprocessing;\n**(2)**\nbiomanufacturing; and\n**(3)**\nthe conversion of under-utilized biomass into high-value ingredients.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out the program under this section $10,000,000 for each of fiscal years 2026 through 2030.\n#### 6. Food biomanufacturing and production grant program\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall establish a grant program to ensure that the United States has a viable domestic food biomanufacturing and production capability to support and sustain increased global demand for protein.\n##### (b) Eligible entities\nAn entity is eligible to receive a grant under subsection (a) if\u2014\n**(1)**\nsuch entity is\u2014\n**(A)**\na nonprofit or for-profit private entity;\n**(B)**\nan institution of higher education;\n**(C)**\na National Laboratory;\n**(D)**\na State or local government; or\n**(E)**\na consortium of entities described in subparagraphs (A) through (D); and\n**(2)**\nsuch entity\u2014\n**(A)**\nis headquartered in the United States and operates primarily within the United States;\n**(B)**\nis at least 51 percent owned and controlled by 1 or more individuals who are citizens of the United States; and\n**(C)**\ndeploys intellectual property and content that is owned by United States individuals.\n##### (c) Grants\n**(1) Use of funds**\nAn entity that receives a grant under this section shall use funds received through the grant\u2014\n**(A)**\nto carry out 1 or more demonstration projects for the advanced biomanufacturing, production, or bioprocessing of edible proteins and fats at scale;\n**(B)**\nto construct 1 or more new commercial-scale facilities for such advanced biomanufacturing, production, or bioprocessing; and\n**(C)**\nto retool, retrofit, or expand 1 or more existing facilities located in the United States and determined qualified by the Secretary for such advanced biomanufacturing, production, or bioprocessing.\n**(2) Amount of grants**\nThe amount of a grant awarded under this section shall be not less than $10,000,000 for an eligible entity carrying out 1 or more projects described in paragraph (1).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out the program under this section $50,000,000 for each of fiscal years 2026 through 2030.\n#### 7. Food bioworkforce development grant program\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall establish a competitive grant program to support food biomanufacturing and bioprocessing workforce development.\n##### (b) Eligible entity\nAn entity is eligible to receive a grant under this section if the entity is\u2014\n**(1)**\na governmental entity;\n**(2)**\na public, private, or cooperative organization organized on a for-profit or nonprofit basis; or\n**(3)**\nan Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) on a Federal or State reservation or any other federally recognized Indian Tribe.\n##### (c) Use of funds\nAn entity to which a grant is made under this section may use the grant funds to\u2014\n**(1)**\ntrain new and existing employees on food biomanufacturing and bioprocessing methods;\n**(2)**\nestablish a center for training, technology, and trade that will provide training to employees in food biomanufacturing and bioprocessing;\n**(3)**\nprovide higher-education scholarships to students pursuing careers in food biomanufacturing and bioprocessing, including at community colleges;\n**(4)**\nconduct regional, community, and local economic development planning and coordination for the purpose of increasing food biomanufacturing and bioprocessing;\n**(5)**\nprovide technical assistance to gain compliance with Federal, State, or local regulations related to food biomanufacturing and bioprocessing; or\n**(6)**\nfacilitate business and lending opportunities related to food biomanufacturing and bioprocessing, including identifying relevant information necessary for obtaining\u2014\n**(A)**\nprivate capital investments;\n**(B)**\nFederal and State loan guarantees;\n**(C)**\nFederal and State direct grants; or\n**(D)**\nother financial support mechanisms from Federal and State entities.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030.\n#### 8. National strategy on alternative proteins\n##### (a) Establishment of a national strategy on alternative proteins\nThe Secretary of Agriculture (referred to in this section as the Secretary ) shall\u2014\n**(1)**\nestablish a national strategy on protein security in coordination with the Secretaries concerned that meets the requirements of subsection (c); and\n**(2)**\nnot later than 1 year after the date of enactment of this Act, finalize such strategy.\n##### (b) Considerations\nWhen developing the national strategy under subsection (a), the Secretaries concerned shall consider\u2014\n**(1)**\nthe best available science related to edible protein diversification that is focused on bioprocessing, biomanufacturing, and the conversion of under-utilized biomass into high-value ingredients;\n**(2)**\nthe strategic benefits of expanding research, development, and production of protein diversification relating to\u2014\n**(A)**\nnational security and warfighter readiness;\n**(B)**\nagriculture opportunities for domestic farmers;\n**(C)**\nfood and agricultural innovation;\n**(D)**\nresilient supply chains; and\n**(E)**\ncross-cutting scientific advancements;\n**(3)**\nglobal competition and the economic benefits of protein diversification relating to\u2014\n**(A)**\nfuture economic productivity;\n**(B)**\njob creation in the biotechnology sector; and\n**(C)**\nexisting public investments and strategies of competitor countries; and\n**(4)**\nexisting policies and programs offered by the Federal and State governments that\u2014\n**(A)**\nfund open-access research and development at higher-learning institutions and government agencies;\n**(B)**\nincentivize private sector research and development;\n**(C)**\nsupport new and existing food biomanufacturers;\n**(D)**\nsupport farmers in the United States that produce crops and feedstocks that support protein diversification and food biomanufacturing; and\n**(E)**\nrepresent a barrier for effective\u2014\n**(i)**\nopen-access food biomanufacturing research and development;\n**(ii)**\nscale-up of food biomanufacturing; and\n**(iii)**\nregulatory oversight.\n##### (c) Contents\nThe national strategy shall\u2014\n**(1)**\nuse a whole-of-government approach to ensure that the United States remains the global leader of food biomanufacturing, bioprocessing, and bioworkforce development for future generations; and\n**(2)**\ninclude\u2014\n**(A)**\nobjectives to fulfill the purpose of the national strategy specified in paragraph (1), including interagency coordination;\n**(B)**\nbarriers to fulfill such purpose;\n**(C)**\nsolutions to the barriers identified in subsection (b)(4)(E); and\n**(D)**\na plan for the implementation of the national strategy.\n##### (d) Secretaries concerned defined\nIn this section, the term Secretaries concerned means\u2014\n**(1)**\nthe Secretary of Defense;\n**(2)**\nthe Secretary of Energy;\n**(3)**\nthe Secretary of Commerce;\n**(4)**\nthe Director of the National Science Foundation;\n**(5)**\nthe Director of the National Institutes of Health;\n**(6)**\nthe Commissioner of Food and Drugs;\n**(7)**\nthe Director of the Centers for Disease Control and Prevention;\n**(8)**\nthe Administrator of the Environmental Protection Agency; and\n**(9)**\nthe Director of the Office of Science and Technology Policy.\n#### 9. Rule of construction\nNothing in this Act, or an amendment made by this Act, shall be construed to support the production of insects for food or animal feed.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3528",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-22T20:41:09Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6780ih.xml"
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
      "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Secretary of Agriculture to establish research centers of excellence for alternative protein innovation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:40Z"
    }
  ]
}
```
