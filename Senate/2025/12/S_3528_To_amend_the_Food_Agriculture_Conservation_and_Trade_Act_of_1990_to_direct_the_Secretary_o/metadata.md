# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3528
- Title: Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act
- Congress: 119
- Bill type: S
- Bill number: 3528
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-03-12T11:03:18Z
- Update date including text: 2026-03-12T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3528",
    "number": "3528",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
    "type": "S",
    "updateDate": "2026-03-12T11:03:18Z",
    "updateDateIncludingText": "2026-03-12T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-12-17T18:32:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-17T18:32:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3528is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3528\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Schiff (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Secretary of Agriculture to establish research centers of excellence for alternative protein innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nProtein innovation that produces high-quality foods using under-utilized biomass and biomanufacturing processes is an essential component of the bioeconomy.\n**(2)**\nThe United States has produced several groundbreaking biotechnological breakthroughs across the last decade that can diversify the food system.\n**(3)**\nIn recent years, multiple countries have dramatically increased public investments into alternative protein research and development.\n**(4)**\nAccording to the Department of Agriculture, every $1 of investment into agricultural research results in $20 of economic productivity.\n**(5)**\nAs of 2019, the plant-based food industry supported over 55,000 jobs in the United States, and the protein sector could create as many as 10,000,000 jobs globally by 2050.\n**(6)**\nDiversifying the protein supply of the United States will increase domestic supply chain resilience, decrease reliance on foreign grain and other commodities, and provide more choices to American consumers.\n**(7)**\nThe global demand for meat is predicted to double by 2050, thus increasing the need for additional food sources.\n**(8)**\nA diversified food system would improve global and domestic food security.\n**(9)**\nProtein innovation can strengthen national security, improve supply chain resilience, and lower the risk of bioterrorism.\n#### 3. Research centers of excellence for food and agriculture innovation\nSection 1673 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5926 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting of Agriculture (referred to in this section as the Secretary ) after The Secretary ; and\n**(2)**\nby adding at the end the following:\n(e) Centers of Excellence for Food and Agriculture Innovation (1) Recognition The Secretary shall recognize not fewer than 3 centers of excellence, one of which shall be led by an 1890 Institution (as defined in section 2 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7601 )), to focus on the areas specified in paragraph (2) relating to the advancement of emerging and innovative food and agriculture with an emphasis on diversifying edible protein sources. (2) Areas of focus (A) Food biomanufacturing research and development A center of excellence recognized under paragraph (1) may carry out research, development, and education programs that support the quality, production, or cost-effectiveness of emerging and innovative foods that employ\u2014 (i) bioprocessing; (ii) biomanufacturing; and (iii) the conversion of biomass into proteins and fats at scale. (B) Student success and workforce development A center of excellence recognized under paragraph (1) may engage in activities to ensure that students have the skills and education needed to work in innovative food and agriculture industries, including agricultural science, technology, engineering, mathematics, and related fields of study. (3) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $15,000,000 for each of fiscal years 2026 through 2030. (4) Report Not later than 1 year after the date of enactment of the Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act , and every year thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report describing\u2014 (A) the resources invested in the centers of excellence recognized under paragraph (1); and (B) the work being done by such centers of excellence. .\n#### 4. Agriculture and Food Research Initiative\nSection 2(b)(2)(E) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b)(2)(E) ) is amended\u2014\n**(1)**\nby redesignating clauses (ii) through (v) as clauses (iii) through (vi), respectively; and\n**(2)**\nby inserting after clause (i) the following new clause:\n(ii) tools and production methods that increase the availability of edible protein sources using bioprocessing, biomanufacturing, and the conversion of under-utilized biomass into high-value ingredients; .\n#### 5. Agricultural Research Service\n##### (a) Establishment of national program\nThe Secretary of Agriculture, acting through the Administrator of the Agricultural Research Service, shall establish a national program dedicated to protein security that increases rural prosperity and farmer profits, which is focused on\u2014\n**(1)**\nbioprocessing;\n**(2)**\nbiomanufacturing; and\n**(3)**\nthe conversion of under-utilized biomass into high-value ingredients.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out the program under this section $10,000,000 for each of fiscal years 2026 through 2030.\n#### 6. Food biomanufacturing and production grant program\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall establish a grant program to ensure that the United States has a viable domestic food biomanufacturing and production capability to support and sustain increased global demand for protein.\n##### (b) Eligible entities\nAn entity is eligible to receive a grant under subsection (a) if\u2014\n**(1)**\nsuch entity is\u2014\n**(A)**\na nonprofit or for-profit private entity;\n**(B)**\nan institution of higher education;\n**(C)**\na National Laboratory;\n**(D)**\na State or local government; or\n**(E)**\na consortium of entities described in subparagraphs (A) through (D); and\n**(2)**\nsuch entity\u2014\n**(A)**\nis headquartered in the United States and operates primarily within the United States;\n**(B)**\nis at least 51 percent owned and controlled by 1 or more individuals who are citizens of the United States; and\n**(C)**\ndeploys intellectual property and content that is owned by United States individuals.\n##### (c) Grants\n**(1) Use of funds**\nAn entity that receives a grant under this section shall use funds received through the grant\u2014\n**(A)**\nto carry out 1 or more demonstration projects for the advanced biomanufacturing, production, or bioprocessing of edible proteins and fats at scale;\n**(B)**\nto construct 1 or more new commercial-scale facilities for such advanced biomanufacturing, production, or bioprocessing; and\n**(C)**\nto retool, retrofit, or expand 1 or more existing facilities located in the United States and determined qualified by the Secretary for such advanced biomanufacturing, production, or bioprocessing.\n**(2) Amount of grants**\nThe amount of a grant awarded under this section shall be not less than $10,000,000.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out the program under this section $50,000,000 for each of fiscal years 2026 through 2030.\n#### 7. Food bioworkforce development grant program\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture shall establish a competitive grant program to support food biomanufacturing and bioprocessing workforce development.\n##### (b) Eligible entity\nAn entity is eligible to receive a grant under this section if the entity is\u2014\n**(1)**\na governmental entity;\n**(2)**\na public, private, or cooperative organization organized on a for-profit or nonprofit basis; or\n**(3)**\nan Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) on a Federal or State reservation or any other federally recognized Indian Tribe.\n##### (c) Use of funds\nAn entity to which a grant is made under this section shall use the grant funds to\u2014\n**(1)**\ntrain new and existing employees on food biomanufacturing and bioprocessing methods;\n**(2)**\nestablish a center for training, technology, and trade that will provide training to employees in food biomanufacturing and bioprocessing;\n**(3)**\nprovide higher-education scholarships to students pursuing careers in food biomanufacturing and bioprocessing, including at community colleges;\n**(4)**\nconduct regional, community, and local economic development planning and coordination for the purpose of increasing food biomanufacturing and bioprocessing;\n**(5)**\nprovide technical assistance to gain compliance with Federal, State, or local regulations related to food biomanufacturing and bioprocessing; or\n**(6)**\nfacilitate business and lending opportunities related to food biomanufacturing and bioprocessing, including identifying relevant information necessary for obtaining\u2014\n**(A)**\nprivate capital investments;\n**(B)**\nFederal and State loan guarantees;\n**(C)**\nFederal and State direct grants; or\n**(D)**\nother financial support mechanisms from Federal and State entities.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030.\n#### 8. National strategy on alternative proteins\n##### (a) Establishment of a national strategy on alternative proteins\nThe Secretary of Agriculture (referred to in this section as the Secretary ) shall\u2014\n**(1)**\nestablish a national strategy on protein security in coordination with the Secretaries concerned that meets the requirements of subsection (c); and\n**(2)**\nnot later than 1 year after the date of enactment of this Act, finalize such strategy.\n##### (b) Considerations\nWhen developing the national strategy under subsection (a), the Secretaries concerned shall consider\u2014\n**(1)**\nthe best available science related to edible protein diversification that is focused on bioprocessing, biomanufacturing, and the conversion of under-utilized biomass into high-value ingredients;\n**(2)**\nthe strategic benefits of expanding research, development, and production of protein diversification relating to\u2014\n**(A)**\nnational security and warfighter readiness;\n**(B)**\nagriculture opportunities for domestic farmers;\n**(C)**\nfood and agricultural innovation;\n**(D)**\nresilient supply chains; and\n**(E)**\ncross-cutting scientific advancements;\n**(3)**\nglobal competition and the economic benefits of protein diversification relating to\u2014\n**(A)**\nfuture economic productivity;\n**(B)**\njob creation in the biotechnology sector; and\n**(C)**\nexisting public investments and strategies of competitor countries; and\n**(4)**\nexisting policies and programs offered by the Federal Government and State governments that\u2014\n**(A)**\nfund open-access research and development at institutions of higher education and government agencies;\n**(B)**\nincentivize private sector research and development;\n**(C)**\nsupport new and existing food biomanufacturers;\n**(D)**\nsupport farmers in the United States that produce crops and feedstocks that support protein diversification and food biomanufacturing; and\n**(E)**\nrepresent a barrier for effective\u2014\n**(i)**\nopen-access food biomanufacturing research and development;\n**(ii)**\nscale-up of food biomanufacturing; and\n**(iii)**\nregulatory oversight.\n##### (c) Contents\nThe national strategy shall\u2014\n**(1)**\nuse a whole-of-government approach to ensure that the United States remains the global leader of food biomanufacturing, bioprocessing, and bioworkforce development for future generations; and\n**(2)**\ninclude\u2014\n**(A)**\nobjectives to fulfill the purpose of the national strategy specified in paragraph (1), including interagency coordination;\n**(B)**\nbarriers to fulfill such purpose;\n**(C)**\nsolutions to the barriers identified under subsection (b)(4)(E); and\n**(D)**\na plan for the implementation of the national strategy.\n##### (d) Secretaries concerned defined\nIn this section, the term Secretaries concerned means\u2014\n**(1)**\nthe Secretary of Defense;\n**(2)**\nthe Secretary of Energy;\n**(3)**\nthe Secretary of Commerce;\n**(4)**\nthe Director of the National Science Foundation;\n**(5)**\nthe Director of the National Institutes of Health;\n**(6)**\nthe Commissioner of Food and Drugs;\n**(7)**\nthe Director of the Centers for Disease Control and Prevention;\n**(8)**\nthe Administrator of the Environmental Protection Agency; and\n**(9)**\nthe Director of the Office of Science and Technology Policy.\n#### 9. Rule of construction\nNothing in this Act, or an amendment made by this Act, shall be construed to support the production of insects for food or animal feed.",
      "versionDate": "2025-12-17",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6780",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
      "type": "HR"
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
        "updateDate": "2026-01-14T16:30:15Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3528is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Producing Real Opportunities for Technology and Entrepreneurs Investing in Nutrition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Secretary of Agriculture to establish research centers of excellence for alternative protein innovation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:18:15Z"
    }
  ]
}
```
