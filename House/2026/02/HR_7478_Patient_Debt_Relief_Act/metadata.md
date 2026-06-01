# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7478
- Title: Patient Debt Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 7478
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-27T19:04:57Z
- Update date including text: 2026-02-27T19:04:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7478",
    "number": "7478",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Patient Debt Relief Act",
    "type": "HR",
    "updateDate": "2026-02-27T19:04:57Z",
    "updateDateIncludingText": "2026-02-27T19:04:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:03:35Z",
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
          "date": "2026-02-10T15:03:30Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NM"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MI"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "OH"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-10",
      "state": "DC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MN"
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
      "sponsorshipDate": "2026-02-10",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NV"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7478ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7478\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Vasquez (for himself, Ms. Stansbury , Mr. Ruiz , Ms. Castor of Florida , Mr. Thanedar , Ms. Clarke of New York , Ms. Schrier , Mr. Garcia of California , Ms. Barrag\u00e1n , Mr. Landsman , Mr. Frost , Ms. Norton , Ms. Craig , Mr. Garc\u00eda of Illinois , Ms. Simon , Mr. Goldman of New York , Mr. Horsford , and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to establish certain standards and requirements with respect to financial assistance and medical debt collection for hospitals participating in the Medicare program, and to amend title III of the Public Health Service Act to establish a grant program for purposes of medical debt relief.\n#### 1. Short title\nThis Act may be cited as the Patient Debt Relief Act .\n#### 2. Establishing standards and requirements with respect to financial assistance and medical debt collection as condition of participation in the Medicare program\nSection 1866 of the Social Security Act ( 42 U.S.C. 1395cc ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (X), by striking and at the end;\n**(B)**\nin subparagraph (Y), by striking the period at the end and inserting , and ; and\n**(C)**\nby inserting after subparagraph (Y) the following new subparagraph:\n(Z) in the case of a hospital, beginning January 1, 2028, to comply with the financial assistance and debt collection requirements described in subsection (l). ;\n**(2)**\nin subsection (b), by adding at the end the following new paragraph:\n(5) (A) A hospital that fails to comply with the requirements of subsection (a)(1)(Z) (relating to financial assistance and debt collection) is subject to a civil monetary penalty under this paragraph. (B) The Secretary may impose a civil monetary penalty in an amount specified by the Secretary (but not to exceed $1,000,000) for each instance of noncompliance with the requirements of subsection (a)(1)(Z), as determined by the Secretary, if\u2014 (i) not later than 90 days after the date on which the Secretary determines such noncompliance exists, the Secretary submits to such hospital a notification of such determination; and (ii) as of the date that is 45 days after such notification is sent, the Secretary determines that such hospital has not taken meaningful actions to come into compliance with such requirements. The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil monetary penalty under this paragraph in the same manner as such provisions apply to a penalty or proceeding under section 1128A(a). ; and\n**(3)**\nby adding at the end the following new subsection:\n(l) Financial assistance and debt collection requirements (1) In general For purposes of subsection (a)(1)(Z), the financial assistance and debt collection requirements are, with respect to a hospital\u2014 (A) the financial assistance and charity care requirements described in paragraph (2) ; and (B) the medical debt collection limitations described in paragraph (3) . (2) Financial assistance and charity care requirements For purposes of paragraph (1) , the requirements described in this paragraph are, with respect to a hospital, the following: (A) The hospital\u2014 (i) has established a charity care or financial assistance policy; (ii) has established minimum eligibility requirements with respect to such charity care or financial assistance policy, and has made such requirements publicly available; and (iii) has established a process for screening individuals furnished items or services by the hospital to determine whether each such individual may be eligible for assistance with respect to payment for such items or services pursuant to such charity care or financial assistance policy. (B) With respect to items or services furnished by the hospital to an individual who has applied for charity care or financial assistance under the policy described in subparagraph (A)(i) , the hospital\u2014 (i) determines, not later than 30 days before the date on which payment for such items or services is due, whether such individual is eligible for assistance with respect to such payment pursuant to such charity care or financial assistance policy; (ii) in the case that a hospital determines pursuant to clause (i) that an individual is ineligible for such charity care or financial assistance policy with respect to such payment, permits such individual to appeal such determination; and (iii) does not seek to collect such payment from such individual until the determination under clause (i) with respect to such individual has been made. (C) The hospital includes with any bill for payment with respect to items or services furnished by the hospital to an individual\u2014 (i) the minimum eligibility requirements described in subparagraph (A)(ii) with respect to the charity care or financial assistance policy of the hospital; (ii) notice of the medical debt collection limitations described in paragraph (3) , including the repayment program described in subparagraph (C)(ii) of such paragraph; and (iii) instructions for the individual to submit to the hospital any information that would be necessary for the hospital to make a determination with respect to the household income of such individual at the time such items or services were furnished for purposes of carrying out subparagraph (D) of such paragraph. (3) Medical debt collection limitations For purposes of paragraph (1) , the limitations described in this paragraph are, with respect to a hospital and medical debt owed to the hospital by an individual, that\u2014 (A) the hospital does not seek to place a lien on or foreclose upon the home of such individual in order to collect such medical debt; (B) the hospital does not seek to garnish the wages of such individual in order to collect such medical debt; (C) subject to subparagraph (D)(ii) , the hospital does not sell or assign such medical debt to a debt collector unless\u2014 (i) more than 1 year has elapsed since the date on which payment for such items or services was due; (ii) the hospital makes available to the individual a repayment program under which the individual may make minimum monthly payments (provided that each such payment does not exceed 4 percent of the gross monthly income of such individual) toward the medical debt, and such individual fails to make 4 or more consecutive monthly payments under such repayment program or otherwise declines to participate in such repayment program; and (iii) such debt collector agrees to abide by the limitations described in subparagraphs (A) and (B) for such hospital with respect to such medical debt; and (D) in the case that the hospital has received the necessary information to make the determination described in paragraph (2)(C)(iii) , if the hospital determines that the household income of such individual was not in excess of 250 percent of the poverty line for the size of the family involved for the most recent taxable year at the time the items or services that are the subject of such medical debt were furnished, the hospital\u2014 (i) does not impose an annual interest rate with respect to such payment; and (ii) does not sell or assign such medical debt to a debt collector. (4) Monitoring compliance (A) Audits Beginning January 1, 2029, and not less frequently than annually thereafter, the Secretary shall conduct an audit of a random sample of hospitals to determine whether each such hospital is in compliance with the requirements of paragraph (1) . (B) Online portal Not later than January 1, 2028, the Secretary shall establish a secure internet website portal (or other successor technology) to permit individuals to report the noncompliance of a hospital with the requirements of paragraph (1) , including noncompliance with the limitations described in subparagraphs (A) and (B) of paragraph (3) of a debt collector to which the hospital has sold or assigned medical debt. (5) Definitions In this subsection: (A) Debt collector The term debt collector has the meaning given such term in section 803(6) of the Fair Debt Collection Practices Act ( 15 U.S.C. 1692a(6) ). (B) Medical debt The term medical debt means, with respect to items or services furnished by a hospital to an individual, the debt (as defined in section 803(5) of the Fair Debt Collection Practices Act ( 15 U.S.C. 1692a(5) )) of such individual for such items or services. .\n#### 3. Medical debt relief program\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following new section:\n399V\u20138. Medical debt relief grant program (a) In general Not later than 1 year after the date of the enactment of this section, the Secretary shall establish a program under which the Secretary may make grants to not more than 1 eligible nonprofit organization to acquire and discharge the medical debt (as defined by the Secretary) of eligible individuals in accordance with this section. (b) Application An eligible nonprofit seeking a grant under this section shall submit an application at such time, in such form, and containing such information as the Secretary may require. (c) Use of funds Amounts provided under a grant under this section shall be used to\u2014 (1) identify eligible individuals; and (2) acquire and discharge the medical debt of such individuals. (d) Notice and reporting requirements (1) Notice requirement Not later than 60 days after an eligible nonprofit organization that has received a grant under this section acquires and discharges the medical debt of an eligible individual under subsection (c) , such eligible nonprofit organization shall notify such individual of such acquisition and discharge. (2) Reporting requirement Not less frequently than once per calendar quarter, an eligible nonprofit organization that has received a grant under this section shall submit to the Secretary a report containing the following information with respect to the preceding calendar quarter: (A) The actions taken by the eligible nonprofit organization to identify eligible individuals. (B) The number of eligible individuals whose medical debt was acquired and discharged by the eligible nonprofit organization, and the amount of medical debt so acquired and discharged. (C) Such other information as the Secretary may require. (e) Definitions In this section: (1) Eligible individual The term eligible individual means an individual with medical debt if, for the most recent taxable year\u2014 (A) such medical debt is equivalent to 5 percent or more of the modified adjusted gross income of such individual; or (B) the household income of such individual is not in excess of 400 percent of the poverty line for the size of the family involved. (2) Eligible nonprofit organization The term eligible nonprofit organization means a nonprofit organization with the mission of relieving individuals of their medical debt, as determined by the Secretary. (3) IRC terms The terms household income , modified adjusted gross income , and poverty line have the meaning given each such term in section 36B of the Internal Revenue Code of 1986 ( 26 U.S.C. 36B ). (f) Funding There is authorized to be appropriated for purposes of carrying out this section $100,000,000 for fiscal year 2027, to remain available until expended. .",
      "versionDate": "2026-02-10",
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
        "name": "Health",
        "updateDate": "2026-02-27T19:04:57Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7478ih.xml"
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
      "title": "Patient Debt Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Patient Debt Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish certain standards and requirements with respect to financial assistance and medical debt collection for hospitals participating in the Medicare program, and to amend title III of the Public Health Service Act to establish a grant program for purposes of medical debt relief.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:37Z"
    }
  ]
}
```
