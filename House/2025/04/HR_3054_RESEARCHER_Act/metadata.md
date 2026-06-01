# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3054
- Title: RESEARCHER Act
- Congress: 119
- Bill type: HR
- Bill number: 3054
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2026-05-13T08:06:12Z
- Update date including text: 2026-05-13T08:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3054",
    "number": "3054",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "RESEARCHER Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:12Z",
    "updateDateIncludingText": "2026-05-13T08:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "ME"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OR"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DC"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CO"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3054ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3054\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Ms. McClellan (for herself, Ms. DelBene , Ms. Tlaib , Ms. Pingree , Ms. Lee of Pennsylvania , Ms. Tokuda , Mr. Thanedar , Ms. Bonamici , Mr. Tonko , Ms. Norton , Mrs. Cherfilus-McCormick , Mr. Frost , and Mr. Foster ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the Director of the Office of Science and Technology Policy to develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Relieving Economic Strain to Enhance American Resilience and Competitiveness in Higher Education and Research Act or the RESEARCHER Act .\n#### 2. Policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers\n##### (a) Definition\nIn this section:\n**(1) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(2) Graduate researchers**\nThe term graduate researchers means individuals enrolled in a degree program leading to an advanced degree who receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding.\n**(3) Postdoctoral researchers**\nThe term postdoctoral researchers means individuals in training-focused positions who have received a doctoral degree or equivalent and receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding.\n##### (b) OSTP guidelines\n**(1) In general**\nNot later than six months after the date of the enactment of this Act, the Director of the Office of Science and Technology Policy, in consultation with the National Science and Technology Council, the Committee on STEM Education, PCAST, institutions of higher education, graduate and postdoctoral organizations, and other relevant stakeholders, shall develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers.\n**(2) Requirements**\nIn developing the policy guidelines under paragraph (1), the Director of the Office of Science and Technology Policy shall include guidelines that address, to the extent practicable, the following:\n**(A)**\nOpportunities to increase stipends for graduate researchers and postdoctoral researchers, including indexing based on location.\n**(B)**\nIncreasing stipends for postdoctoral researchers conducting research in rural or underserved areas, or in States eligible to receive funding from the Established Program to Stimulate Competitive Research under section 113 of the National Science Foundation Authorization Act of 1988 ( 42 U.S.C. 1862g ), to support the recruitment and retention of researchers in such regions.\n**(C)**\nOpportunities to increase access to quality, affordable medical, dental, and vision care.\n**(D)**\nOpportunities to increase access to affordable housing and transportation.\n**(E)**\nOpportunities to reduce food insecurity.\n**(F)**\nOpportunities to address costs of caring for family members, including child care.\n**(3) Application**\n**(A) In general**\nThe Director of the Office of Science and Technology Policy shall encourage and monitor efforts of Federal research agencies to develop and implement policies based on the policy guidelines under paragraph (1).\n**(B) Federal research agency implementation**\nNot later than six months after receiving the policy guidelines under paragraph (1), the head of each Federal research agency shall\u2014\n**(i)**\ndevelop and implement policies with respect to financial instability of graduate researchers and postdoctoral researchers that are consistent with such policy guidelines; and\n**(ii)**\nbroadly disseminate such policies to current and potential recipients of research and development awards made by such agency.\n**(4) Updates**\nThe Director of the Office of Science and Technology Policy shall update the policy guidelines under paragraph (1) as the Director determines necessary.\n**(5) Report**\nNot later than one year after the date after the policy guidelines under paragraph (1) are developed and every five years thereafter, the Director of the Office of Science and Technology Policy shall submit to the Committee on Science, Space, and Technology, the Committee on Education and the Workforce, and the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing information relating to the following:\n**(A)**\nSuch policy guidelines.\n**(B)**\nProgress on the implementation of such guidelines by Federal research agencies.\n##### (c) Data collection\nThe Research and Development, Competition, and Innovation Act (enacted as division B of Public Law 117\u2013167 ) is amended\u2014\n**(1)**\nin section 10314(b) ( 42 U.S.C. 18994 )\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (D), by striking and after the semicolon;\n**(ii)**\nby redesignating subparagraph (E) as subparagraph (F); and\n**(iii)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) graduate researcher and postdoctoral researcher stipend amounts and financial instability (disaggregated, to the extent practicable, by demographics); and ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) Definitions In this subsection: (A) Institution of higher education The term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (B) Graduate researchers The term graduate researchers means individuals enrolled in a degree program leading to an advanced degree who receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding. (C) Postdoctoral researchers The term postdoctoral researchers means individuals in training-focused positions who have received a doctoral degree or equivalent and receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding. ; and\n**(2)**\nin paragraph (1) of section 10502(a) ( 42 U.S.C. 19152(a) ), by inserting graduate and postdoctoral research stipend amounts (disaggregated, to the extent practicable, by demographics), before and awarded budget .\n##### (d) Data on financial instability of graduate researchers and postdoctoral researchers\nThe Director of the National Science Foundation shall make awards, on a competitive basis, to institutions of higher education or nonprofit organizations (or consortia of such institutions or organizations) to collect and analyze data on financial instability of graduate researchers and postdoctoral researchers (disaggregated, to the extent practicable, by demographics).\n##### (e) National Academies assessment\n**(1) In general**\nNot later than two years after the date of the enactment of this Act, the Director of the National Science Foundation shall enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to undertake a study and issue a report on the status of financial instability of graduate researchers and postdoctoral researchers. To the extent feasible, the study shall include an assessment (disaggregated, to the extent practicable, by demographics) at a minimum of the immediately preceding five years of the following:\n**(A)**\nStipends relative to average local medical, dental, and vision expenses.\n**(B)**\nStipends relative to average local housing and transportation costs.\n**(C)**\nStipends relative to average local food costs.\n**(D)**\nStipends relative to average local costs of caring for family members, including child care costs.\n**(2) Report**\nNot later than two years after the date on which the agreement between the Director of the National Science Foundation and the National Academies of Sciences, Engineering, and Medicine is entered into pursuant to paragraph (1), the National Academies of Sciences, Engineering, and Medicine shall submit to Committee on Science, Space, and Technology, the Committee on Education and the Workforce, and the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing the results of the assessment under such paragraph and recommendations relating thereto regarding how Federal agencies, Congress, institutions of higher education, and other relevant entities may address financial instability of graduate researchers and postdoctoral researchers.\n##### (f) GAO study\nNot later than three years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Science, Space, and Technology, the Committee on Education and the Workforce, and the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate a report that\u2014\n**(1)**\nassesses the degree to which Federal research agencies have implemented the policy guidelines under subsection (b) and the effectiveness of such implementation;\n**(2)**\nincludes recommendations on potential changes to practices and policies to improve such guidelines and such implementation; and\n**(3)**\nincludes recommendations on additional data collection and research needed to monitor progress on reducing financial instability of graduate researchers and postdoctoral researchers.",
      "versionDate": "2025-04-29",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2800-2801)"
      },
      "number": "1664",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESEARCHER Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-21T13:57:28Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3054ih.xml"
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
      "title": "RESEARCHER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESEARCHER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Relieving Economic Strain to Enhance American Resilience and Competitiveness in Higher Education and Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the Office of Science and Technology Policy to develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:18Z"
    }
  ]
}
```
