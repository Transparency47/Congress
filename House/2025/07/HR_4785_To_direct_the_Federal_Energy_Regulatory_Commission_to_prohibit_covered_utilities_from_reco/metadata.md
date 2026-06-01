# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4785?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4785
- Title: Ethics in Energy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4785
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-03-19T08:07:16Z
- Update date including text: 2026-03-19T08:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4785",
    "number": "4785",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Ethics in Energy Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:16Z",
    "updateDateIncludingText": "2026-03-19T08:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:03:05Z",
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-29",
      "state": "VA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "PA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4785ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4785\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Castor of Florida (for herself, Ms. Matsui , Ms. McClellan , Ms. Ocasio-Cortez , Ms. Pingree , Mr. Thanedar , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Energy Regulatory Commission to prohibit covered utilities from recovering covered expenses from ratepayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ethics in Energy Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Centralized service company**\nThe term centralized service company has the meaning given the term in section 367.1(a) of title 18, Code of Federal Regulations (or a successor regulation).\n**(2) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(3) Covered expense**\nThe term covered expense means a direct or indirect expense paid by a covered utility to\u2014\n**(A)**\nan external entity to perform political influence activities;\n**(B)**\na centralized service company, parent company, or other corporate affiliate\u2014\n**(i)**\nto perform a political influence activity; and\n**(ii)**\nthat invoices that covered utility for the expenses related to that political influence activity; or\n**(C)**\nan employee of that covered utility, in the form of a salary, that performs a political influence activity.\n**(4) Covered utility**\nThe term covered utility means\u2014\n**(A)**\nan electric utility company (as defined in section 367.1(a) of title 18, Code of Federal Regulations (or a successor regulation)) that had, in each of the 3 previous calendar years, sales or transmission services that exceeded\u2014\n**(i)**\n1,000,000 megawatt-hours of total annual sales;\n**(ii)**\n100 megawatt-hours of annual sales for resale;\n**(iii)**\n500 megawatt-hours of annual power exchanges delivered; or\n**(iv)**\n500 megawatt-hours of annual wheeling;\n**(B)**\na major natural gas company; and\n**(C)**\na centralized service company.\n**(5) Major natural gas company**\nThe term major natural gas company means a natural-gas company (as defined in section 2 of the Natural Gas Act ( 15 U.S.C. 717a )) whose combined gas transported or stored for a fee exceed 50,000,000 Dth in each of the 3 previous calendar years.\n**(6) Political influence activity**\nThe term political influence activity includes\u2014\n**(A)**\nany expense for the purpose of directly or indirectly influencing the possible\u2014\n**(i)**\nadoption of Federal, State, or local regulations, legislation, or ordinances; or\n**(ii)**\nrepeal or modification of existing Federal, State, or local regulations, legislation, or ordinances;\n**(B)**\nany expense for the purpose of directly or indirectly influencing elections or appointments of public officials or referenda;\n**(C)**\nany expense for the purpose of directly or indirectly influencing the approval, modification, or revocation of utility franchises;\n**(D)**\nany expense for the purpose of directly or indirectly influencing the public opinion with respect to Federal, State, or local\u2014\n**(i)**\nregulations, legislation, or ordinances;\n**(ii)**\nelections;\n**(iii)**\nreferenda; or\n**(iv)**\nutility rate setting;\n**(E)**\nany expense for the purpose of directly or indirectly influencing the decisions of Federal, State, or local government officials;\n**(F)**\nany expense relating to attendance or participation in, preparation for, or appeal of any formal proceeding before a regulatory commission;\n**(G)**\ndues or fees paid to trade associations or industry associations;\n**(H)**\nany contributions or other payments to an organization described in paragraph (3) or (4) of section 501(c) of the Internal Revenue Code of 1986; and\n**(I)**\nadvertising, marketing, or public relations expenses designed for the purpose of\u2014\n**(i)**\ninfluencing public opinion;\n**(ii)**\nincreasing goodwill toward a covered utility from the public or from public officials;\n**(iii)**\nimproving the reputation of a covered utility; or\n**(iv)**\npromoting or retaining the service provided by a covered utility.\n#### 3. Prohibition against recovering political activity expenses from ratepayers\n##### (a) Regulations\nNot later than 18 months after the date of enactment of this Act, the Commission shall promulgate regulations\u2014\n**(1)**\nto prohibit covered utilities from recovering covered expenses from ratepayers in proceedings before the Commission, in accordance with this section; and\n**(2)**\nto amend the applicable Uniform System of Accounts in title 18, Code of Federal Regulations (or successor regulations), to instruct covered utilities to place covered expenses in accounts that are presumptively not recoverable from ratepayers, in accordance with this section.\n##### (b) Report\n**(1) In general**\nThe Commission shall require that, not later than 18 months after the date of enactment of this Act, and annually thereafter, each covered utility shall submit to the Commission a report containing\u2014\n**(A)**\nan itemized list of expenses of the preceding year recorded in accounts relating to\u2014\n**(i)**\ncovered expenses;\n**(ii)**\noutside services or vendors; and\n**(iii)**\nthe operations of the covered utility with respect to administrative and general expenses; and\n**(B)**\nfor each expense or cost described in clauses (i) through (iii) of subparagraph (A), unredacted information with respect to each of the matters described in paragraph (2) that are applicable to that expense or cost.\n**(2) Matters described**\nThe matters referred to in paragraph (1)(B) for the expenses and costs described in clauses (i) through (iii) of paragraph (1)(A) are the following:\n**(A)**\nBilling amounts.\n**(B)**\nBilling dates.\n**(C)**\nThe identity of each payee for any external consultants or contracts.\n**(D)**\nIn the case of a payment made to a third-party vendor by a centralized service company, parent company, or other corporate affiliate of the covered utility, the identity of that third-party vendor.\n**(E)**\nThe job title, portion of salaries, and expenses, and all Uniform System of Account codes to which compensation was recorded for the employee, of covered utility staff with respect to any work performed relating to a covered expense.\n**(F)**\nAn explanation of the expense or cost that is sufficient to describe the purpose of the expense or cost.\n**(3) Reporting minimum removed**\nWith respect to any annual form that a covered utility submits to the Commission having a reporting threshold of $250,0000, the Commission shall remove that reporting threshold for the reporting of transactions with associated or affiliated companies on that annual form.\n##### (c) Enforcement\n**(1) In general**\nThe Commission shall monitor and investigate compliance and noncompliance with the regulations promulgated under this section.\n**(2) Penalty**\n**(A) In general**\nIn addition to any refunds that the Commission orders a covered utility to pay ratepayers, the Commission shall assess a penalty in accordance with subparagraph (B) against a covered utility that violates or fails or refuses to comply with the regulations promulgated under this section by charging a ratepayer a covered expense.\n**(B) Amount of penalty**\n**(i) In general**\nSubject to clause (ii), a penalty assessed under subparagraph (A) shall be\u2014\n**(I)**\nfor a covered expense charged to ratepayers in an amount less than $1,000,000, not less than the amount of that covered expense;\n**(II)**\nfor a covered expense charged to ratepayers in an amount not less than $1,000,000 and not more than $10,000,000, not less than double the amount of that covered expense; and\n**(III)**\nfor a covered expense charged to ratepayers in an amount more than $10,000,000, not less than triple the amount of that covered expense.\n**(ii) Limitation**\nThe amount of a penalty assessed under subparagraph (A) shall be not more than 20 times the amount of the applicable covered expense.\n**(3) No recovery from ratepayers**\nCovered utilities that are subject to a penalty under this subsection may not recover that penalty from ratepayers.\n**(4) Penalty distribution**\nWith respect to each penalty assessed and collected under this subsection\u2014\n**(A)**\n\u00bd of that penalty shall be distributed to ratepayers, through a rebate; and\n**(B)**\n\u00bd of that penalty shall be distributed to the Commission for the purpose of increasing resources for enforcing this section.\n**(5) Rule of construction**\nNothing in this Act prevents the Commission from issuing refunds or rebates to ratepayers for a covered expense that was recovered by a covered utility on a date before the date of enactment of this Act.",
      "versionDate": "2025-07-29",
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
        "name": "Energy",
        "updateDate": "2025-09-12T18:14:02Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4785ih.xml"
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
      "title": "Ethics in Energy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ethics in Energy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Energy Regulatory Commission to prohibit covered utilities from recovering covered expenses from ratepayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:32Z"
    }
  ]
}
```
