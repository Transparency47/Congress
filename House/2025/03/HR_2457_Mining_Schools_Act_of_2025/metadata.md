# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2457
- Title: Mining Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2457
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-03-18T08:06:49Z
- Update date including text: 2026-03-18T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2457",
    "number": "2457",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Mining Schools Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T08:06:49Z",
    "updateDateIncludingText": "2026-03-18T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:00Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "UT"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "UT"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "CO"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NC"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "IL"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NV"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "CO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "CO"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2457ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2457\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Owens (for himself, Mr. Costa , Ms. Maloy , Ms. Pettersen , and Mr. Moore of Utah ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of Energy to provide technology grants to strengthen domestic mining education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Technology Grants to Strengthen Domestic Mining Education Act of 2025 or the Mining Schools Act of 2025 .\n#### 2. Technology grants to strengthen domestic mining education\n##### (a) Definitions\nIn this section:\n**(1) Board**\nThe term Board means the Mining Professional Development Advisory Board established by subsection (d)(1).\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(3) Mining industry**\nThe term mining industry means the mining industry of the United States, consisting of the search for, and extraction, beneficiation, refining, smelting, processing, reprocessing, and recycling of, naturally occurring metal and nonmetal minerals from the earth.\n**(4) Mining profession**\nThe term mining profession means the body of jobs directly relevant to\u2014\n**(A)**\nthe exploration, planning, execution, and remediation of metal and nonmetal mining sites; and\n**(B)**\nthe extraction, including the separation, refining, alloying, smelting, concentration, processing, reprocessing, and recycling of mineral ores.\n**(5) Mining school**\nThe term mining school means\u2014\n**(A)**\na mining, metallurgical, geological, or mineral engineering program accredited by the Accreditation Board for Engineering and Technology, Inc., that is located at an institution of higher education, including a Tribal College or University; or\n**(B)**\na geology or engineering program or department that is located at a 4-year public institution of higher education located in a State the gross domestic product of which in 2021 was not less than $2,000,000,000 in the combined categories of \u201cMining (except oil and gas)\u201d and \u201cSupport activities for mining\u201d, according to the Bureau of Economic Analysis.\n**(6) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(7) Tribal College or University**\nThe term Tribal College or University has the meaning given the term in section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c(b) ).\n##### (b) Domestic mining education strengthening program\nThe Secretary, in consultation with the Secretary of the Interior (acting through the Director of the United States Geological Survey), shall\u2014\n**(1)**\nestablish a grant program to strengthen domestic mining education; and\n**(2)**\nunder the program established under paragraph (1), award competitive grants to mining schools for the purpose of recruiting and educating the next generation of mining engineers and other qualified professionals to meet the future energy and mineral needs of the United States.\n##### (c) Grants\n**(1) In general**\nIn carrying out the grant program established under subsection (b)(1), the Secretary shall award not more than 10 grants each year to mining schools.\n**(2) Selection requirements**\n**(A) In general**\nTo the maximum extent practicable, the Secretary shall select recipients for grants under paragraph (1) to ensure geographic diversity among grant recipients to ensure that region-specific specialties are developed for region-specific geology.\n**(B) Timeline**\nThe Secretary shall award the grants under paragraph (1) by not later than the later of\u2014\n**(i)**\nthe date that is 180 days after the start of the applicable fiscal year; and\n**(ii)**\nthe date that is 180 days after the date on which the Act making full-year appropriations for the Department of Energy for the applicable fiscal year is enacted.\n**(3) Recommendations of the Board**\n**(A) In general**\nIn selecting recipients for grants under paragraph (1) and determining the amount of each grant, the Secretary, to the maximum extent practicable, shall take into consideration the recommendations of the Board under subparagraphs (A) and (B) of subsection (d)(3).\n**(B) Selection statement**\nIn selecting recipients for grants under paragraph (1), the Secretary shall\u2014\n**(i)**\nin response to a recommendation from the Board, submit to the Board a statement that describes\u2014\n**(I)**\nwhether the Secretary accepts or rejects, in whole or in part, the recommendation of the Board; and\n**(II)**\nthe justification and rationale for any rejection, in whole or in part, of the recommendation of the Board; and\n**(ii)**\nnot later than 15 days after awarding a grant for which the Board submitted a recommendation, publish the statement submitted under clause (i) on the Department of Energy website.\n**(4) Use of funds**\nA mining school receiving a grant under paragraph (1) shall use the grant funds\u2014\n**(A)**\nto recruit students to the mining school; and\n**(B)**\nto enhance and support programs related to, as applicable\u2014\n**(i)**\nmining, mineral extraction efficiency, and related processing technology;\n**(ii)**\nemphasizing critical mineral and rare earth element exploration, extraction, and refining;\n**(iii)**\nreclamation technology and practices for active mining operations;\n**(iv)**\nthe development of reprocessing systems and technologies that facilitate reclamation that fosters the recovery of resources at abandoned mine sites;\n**(v)**\nmineral extraction, refining, processing, reprocessing, and recycling methods that reduce environmental and human impacts;\n**(vi)**\ntechnologies to extract, refine, separate, melt, produce, or recycle minerals, including rare earth elements;\n**(vii)**\nreducing dependence on foreign energy and mineral supplies through increased domestic critical mineral production and recycling;\n**(viii)**\nenhancing the competitiveness of United States energy and mineral technology exports;\n**(ix)**\nthe extraction or processing of coinciding mineralization, including rare earth elements, within coal or other ores, coal or mineral processing byproduct, overburden, or residue from coal, minerals, or other ores;\n**(x)**\nenhancing technologies and practices relating to mitigation of acid mine drainage, reforestation, and revegetation in the reclamation of land and water resources adversely affected by mining;\n**(xi)**\nenhancing exploration and characterization of new or novel deposits, including rare earth elements and critical minerals within phosphate rocks, uranium-bearing deposits, and other nontraditional sources;\n**(xii)**\nmeeting challenges of extreme mining conditions, such as deeper deposits or cold region mining;\n**(xiii)**\nmineral economics, including analysis of supply chains, future mineral needs, and unconventional mining resources; and\n**(xiv)**\nmining practices that reduce environmental impact, including mining practices that reduce water usage, mitigate surface disturbance, and promote overall resource efficiency.\n##### (d) Mining Professional Development Advisory Board\n**(1) In general**\nThere is established an advisory board, to be known as the Mining Professional Development Advisory Board .\n**(2) Composition**\nThe Board shall be composed of 6 members, to be appointed by the Secretary not later than 180 days after the date of enactment of this Act, of whom\u2014\n**(A)**\n3 shall be individuals who are actively working in the mining profession and for the mining industry; and\n**(B)**\n3 shall have experience in academia implementing and operating professional skills training and education programs in the mining sector.\n**(3) Duties**\nThe Board shall\u2014\n**(A)**\nevaluate grant applications received under subsection (c) and make recommendations to the Secretary for selection of grant recipients under that subsection;\n**(B)**\npropose the amount of the grant for each applicant recommended to be selected under subparagraph (A); and\n**(C)**\nperform oversight to ensure that grant funds awarded under subsection (c) are used for the purposes described in paragraph (4) of that subsection.\n**(4) Term**\nA member of the Board shall serve for a term of 4 years.\n**(5) Vacancies**\nA vacancy on the Board\u2014\n**(A)**\nshall not affect the powers of the Board; and\n**(B)**\nshall be filled in the same manner as the original appointment was made by not later than 180 days after the date on which the vacancy occurs.\n#### 3. Repeal of the Mining and Mineral Resources Research Institute Act of 1984\nPublic Law 98\u2013409 ( 30 U.S.C. 1221 et seq. ) is repealed.\n#### 4. No additional funds authorized\nNo additional funds are authorized to carry out the requirements of this Act, and the activities authorized by this Act are subject to the availability of appropriations made in advance for such purposes.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "1130",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mining Schools Act of 2025",
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
        "name": "Energy",
        "updateDate": "2025-04-07T12:47:59Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2457ih.xml"
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
      "title": "Mining Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mining Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Technology Grants to Strengthen Domestic Mining Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to provide technology grants to strengthen domestic mining education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:21Z"
    }
  ]
}
```
