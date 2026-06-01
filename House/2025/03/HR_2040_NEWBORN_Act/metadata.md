# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2040
- Title: NEWBORN Act
- Congress: 119
- Bill type: HR
- Bill number: 2040
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-03-24T20:06:16Z
- Update date including text: 2026-03-24T20:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2040",
    "number": "2040",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "NEWBORN Act",
    "type": "HR",
    "updateDate": "2026-03-24T20:06:16Z",
    "updateDateIncludingText": "2026-03-24T20:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "AZ"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
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
      "sponsorshipDate": "2025-03-11",
      "state": "DC"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2040ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2040\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Cohen (for himself, Ms. Barrag\u00e1n , Ms. Budzinski , Mrs. Cherfilus-McCormick , Mr. Garc\u00eda of Illinois , Mr. Grijalva , Ms. Kaptur , Ms. Norton , Mr. Rutherford , Ms. Wasserman Schultz , and Ms. Omar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize funding for the creation and implementation of infant mortality pilot programs in standard metropolitan statistical areas with high rates of infant mortality, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nationally Enhancing the Well-being of Babies through Outreach and Research Now Act or the NEWBORN Act .\n#### 2. Infant mortality pilot programs\nSection 330H of the Public Health Service Act ( 42 U.S.C. 254c\u20138 ) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively;\n**(2)**\nby inserting after subsection (d) the following:\n(e) Infant Mortality Pilot Programs (1) In general The Secretary, acting through the Administrator, shall award grants to eligible entities to create, implement, and oversee infant mortality pilot programs. (2) Period of a grant The period of a grant under this subsection shall be up to 5 years. (3) Preference In awarding grants under this subsection, the Secretary shall give preference to\u2014 (A) eligible entities proposing to serve any of the 50 counties or groups of counties with the highest rates of infant mortality in the United States based on the most recent 3 years of available national infant mortality data, as determined by the Secretary; and (B) eligible entities whose proposed infant mortality pilot program would address\u2014 (i) birth defects; (ii) preterm birth and low birth weight; (iii) sudden infant death; (iv) maternal pregnancy complications; or (v) injuries to infants. (4) Use of funds Any infant mortality pilot program funded under this subsection may\u2014 (A) include the development of a plan that identifies the individual needs of each community to be served and strategies to address those needs; (B) provide outreach to at-risk mothers through programs deemed appropriate by the Administrator; (C) develop and implement standardized systems for improved access, utilization, and quality of social, educational, and clinical services to promote healthy pregnancies, full-term births, and healthy infancies delivered to women and their infants, such as\u2014 (i) counseling on infant care, feeding, and parenting; (ii) postpartum care; (iii) prevention of premature delivery; and (iv) additional counseling for at-risk mothers, including smoking cessation programs, drug treatment programs, alcohol treatment programs, nutrition and physical activity programs, postpartum depression and domestic violence programs, social and psychological services, dental care, and parenting programs; (D) establish a rural outreach program to provide care to at-risk mothers in rural areas; (E) establish a regional public education campaign, including a campaign to\u2014 (i) prevent preterm births; and (ii) educate the public about infant mortality; (F) provide for any other activities, programs, or strategies as identified by the plan; and (G) coordinate efforts between\u2014 (i) the health department of each county or other eligible entity to be served through the infant mortality pilot program; and (ii) existing entities that work to reduce the rate of infant mortality within the area of any such county or other eligible entity. (5) Limitation Of the funds received through a grant under this subsection for a fiscal year, an eligible entity shall not use more than 10 percent for program evaluation. (6) Reports on pilot programs (A) In general Not later than 1 year after receiving a grant, and annually thereafter for the duration of the grant period, each entity that receives a grant under paragraph (1) shall submit a report to the Secretary detailing its infant mortality pilot program. (B) Contents of report The reports required under subparagraph (A) shall include information such as the methodology of, and outcomes and statistics from, the grantee\u2019s infant mortality pilot program. (C) Evaluation The Secretary shall use the reports required under subparagraph (A) to evaluate, and conduct statistical research on, infant mortality pilot programs funded through this subsection. (7) Definitions For the purposes of this subsection: (A) Administrator The term Administrator means the Administrator of the Health Resources and Services Administration. (B) Eligible entity The term eligible entity means\u2014 (i) a county, city, territorial, or Tribal health department; or (ii) in the case of a State with a centralized health department, the State health department. (C) Tribal The term Tribal refers to an Indian tribe, a Tribal organization, or an Urban Indian organization, as such terms are defined in section 4 of the Indian Health Care Improvement Act . ;\n**(3)**\nin subsection (f), as so redesignated\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the heading, by striking Authorization of appropriations and inserting Healthy Start Initiative ; and\n**(ii)**\nby inserting (other than subsection (e)) after carrying out this section ;\n**(B)**\nby redesignating paragraph (2) as paragraph (3);\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Infant mortality pilot programs There is authorized to be appropriated $10,000,000 for each of fiscal years 2025 through 2029 to carry out subsection (e). ; and\n**(D)**\nin paragraph (3)(A), as so redesignated, by striking the program under this section and inserting the program under subsection (a) ; and\n**(4)**\nin paragraphs (2) and (3)(B) of subsection (g), as so redesignated, by striking subsection (e)(2)(B) and inserting subsection (f)(3)(B) .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "992",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NEWBORN Act",
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
        "name": "Health",
        "updateDate": "2025-03-26T15:56:24Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2040ih.xml"
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
      "title": "NEWBORN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NEWBORN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nationally Enhancing the Well-being of Babies through Outreach and Research Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize funding for the creation and implementation of infant mortality pilot programs in standard metropolitan statistical areas with high rates of infant mortality, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:58Z"
    }
  ]
}
```
