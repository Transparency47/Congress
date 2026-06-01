# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1130
- Title: Mining Schools Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1130
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1130",
    "number": "1130",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Mining Schools Act of 2025",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
            "date": "2025-03-25T23:38:03Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-25T23:38:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "ND"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "WV"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "UT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "SD"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AK"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AK"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1130is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1130\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Barrasso (for himself, Mr. Hickenlooper , Mr. Hoeven , Ms. Cortez Masto , Mr. Justice , Mr. Bennet , Mr. Curtis , Mr. Kelly , Mr. Rounds , Ms. Rosen , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Energy to provide technology grants to strengthen domestic mining education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Technology Grants to Strengthen Domestic Mining Education Act of 2025 or the Mining Schools Act of 2025 .\n#### 2. Technology grants to strengthen domestic mining education\n##### (a) Definitions\nIn this section:\n**(1) Board**\nThe term Board means the Mining Professional Development Advisory Board established by subsection (d)(1).\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(3) Mining industry**\nThe term mining industry means the mining industry of the United States, consisting of the search for, and extraction, beneficiation, refining, smelting, processing, reprocessing, and recycling of, naturally occurring metal and nonmetal minerals from the earth.\n**(4) Mining profession**\nThe term mining profession means the body of jobs directly relevant to\u2014\n**(A)**\nthe exploration, planning, execution, and remediation of metal and nonmetal mining sites; and\n**(B)**\nthe extraction, including the separation, refining, alloying, smelting, concentration, processing, reprocessing, and recycling, of mineral ores.\n**(5) Mining school**\nThe term mining school means\u2014\n**(A)**\na mining, metallurgical, geological, or mineral engineering program accredited by the Accreditation Board for Engineering and Technology, Inc., that is located at an institution of higher education, including a Tribal College or University (as defined in section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c(b) )); or\n**(B)**\na geology or engineering program or department that is located at a 4-year public institution of higher education located in a State the gross domestic product of which in 2021 was not less than $2,000,000,000 in the combined categories of \u201cMining (except oil and gas)\u201d and \u201cSupport activities for mining\u201d, according to the Bureau of Economic Analysis.\n**(6) Secretary**\nThe term Secretary means the Secretary of Energy.\n##### (b) Domestic mining education strengthening program\nThe Secretary, in consultation with the Secretary of the Interior (acting through the Director of the United States Geological Survey), shall\u2014\n**(1)**\nestablish a grant program to strengthen domestic mining education; and\n**(2)**\nunder the program established in paragraph (1), award competitive grants to mining schools for the purpose of recruiting and educating the next generation of mining engineers and other qualified professionals to meet the future energy and mineral needs of the United States.\n##### (c) Grants\n**(1) In general**\nIn carrying out the grant program established under subsection (b)(1), the Secretary shall award not more than 10 grants each year to mining schools.\n**(2) Selection requirements**\n**(A) In general**\nTo the maximum extent practicable, the Secretary shall select recipients for grants under paragraph (1) to ensure geographic diversity among grant recipients to ensure that region-specific specialties are developed for region-specific geology.\n**(B) Timeline**\nThe Secretary shall award the grants under paragraph (1) by not later than the later of\u2014\n**(i)**\nthe date that is 180 days after the start of the applicable fiscal year; and\n**(ii)**\nthe date that is 180 days after the date on which the Act making full-year appropriations for the Department of Energy for the applicable fiscal year is enacted.\n**(3) Recommendations of the Board**\n**(A) In general**\nIn selecting recipients for grants under paragraph (1) and determining the amount of each grant, the Secretary, to the maximum extent practicable, shall take into consideration the recommendations of the Board under subparagraphs (A) and (B) of subsection (d)(3).\n**(B) Selection statement**\nIn selecting recipients for grants under paragraph (1), the Secretary shall\u2014\n**(i)**\nin response to a recommendation from the Board, submit to the Board a statement that describes\u2014\n**(I)**\nwhether the Secretary accepts or rejects, in whole or in part, the recommendation of the Board; and\n**(II)**\nthe justification and rationale for any rejection, in whole or in part, of the recommendation of the Board; and\n**(ii)**\nnot later than 15 days after awarding a grant for which the Board submitted a recommendation, publish the statement submitted under clause (i) on the Department of Energy website.\n**(4) Use of funds**\nA mining school receiving a grant under paragraph (1) shall use the grant funds\u2014\n**(A)**\nto recruit students to the mining school; and\n**(B)**\nto enhance and support programs related to, as applicable\u2014\n**(i)**\nmining, mineral extraction efficiency, and related processing technology;\n**(ii)**\nemphasizing critical mineral and rare earth element exploration, extraction, and refining;\n**(iii)**\nreclamation technology and practices for active mining operations;\n**(iv)**\nthe development of reprocessing systems and technologies that facilitate reclamation that fosters the recovery of resources at abandoned mine sites;\n**(v)**\nmineral extraction, refining, processing, reprocessing, and recycling methods that reduce environmental and human impacts;\n**(vi)**\ntechnologies to extract, refine, separate, smelt, produce, or recycle minerals, including rare earth elements;\n**(vii)**\nreducing dependence on foreign energy and mineral supplies through increased domestic critical mineral production and recycling;\n**(viii)**\nenhancing the competitiveness of United States energy and mineral technology exports;\n**(ix)**\nthe extraction or processing of coinciding mineralization, including rare earth elements, within coal or other ores, coal or mineral processing byproduct, overburden, or residue from coal, minerals, or other ores;\n**(x)**\nenhancing technologies and practices relating to mitigation of acid mine drainage, reforestation, and revegetation in the reclamation of land and water resources adversely affected by mining;\n**(xi)**\nenhancing exploration and characterization of new or novel deposits, including rare earth elements and critical minerals within phosphate rocks, uranium-bearing deposits, and other nontraditional sources;\n**(xii)**\nmeeting challenges of extreme mining conditions, such as deeper deposits or cold region mining;\n**(xiii)**\nmineral economics, including analysis of supply chains, future mineral needs, and unconventional mining resources; and\n**(xiv)**\nmining practices that reduce environmental impact, including mining practices that reduce water usage, mitigate surface disturbance, and promote overall resource efficiency.\n##### (d) Mining Professional Development Advisory Board\n**(1) In general**\nThere is established an advisory board, to be known as the Mining Professional Development Advisory Board .\n**(2) Composition**\nThe Board shall be composed of 6 members, to be appointed by the Secretary not later than 180 days after the date of enactment of this Act, of whom\u2014\n**(A)**\n3 shall be individuals who are actively working in the mining profession and for the mining industry; and\n**(B)**\n3 shall have experience in academia implementing and operating professional skills training and education programs in the mining sector.\n**(3) Duties**\nThe Board shall\u2014\n**(A)**\nevaluate grant applications received under subsection (c) and make recommendations to the Secretary for selection of grant recipients under that subsection;\n**(B)**\npropose the amount of the grant for each applicant recommended to be selected under subparagraph (A); and\n**(C)**\nperform oversight to ensure that grant funds awarded under subsection (c) are used for the purposes described in paragraph (4) of that subsection.\n**(4) Term**\nA member of the Board shall serve for a term of 4 years.\n**(5) Vacancies**\nA vacancy on the Board\u2014\n**(A)**\nshall not affect the powers of the Board; and\n**(B)**\nshall be filled in the same manner as the original appointment was made by not later than 180 days after the date on which the vacancy occurs.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2033.\n#### 3. Repeal of the Mining and Mineral Resources Institutes Act\nThe Mining and Mineral Resources Institutes Act ( 30 U.S.C. 1221 et seq. ) is repealed.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2457",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mining Schools Act of 2025",
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
        "name": "Energy",
        "updateDate": "2025-04-04T16:49:01Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1130is.xml"
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
      "title": "Mining Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mining Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Technology Grants to Strengthen Domestic Mining Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to provide technology grants to strengthen domestic mining education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:37Z"
    }
  ]
}
```
