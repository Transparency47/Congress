# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7555
- Title: Audit the Pentagon Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7555
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-22T08:08:11Z
- Update date including text: 2026-05-22T08:08:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7555",
    "number": "7555",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000607",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Pocan, Mark [D-WI-2]",
        "lastName": "Pocan",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Audit the Pentagon Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:11Z",
    "updateDateIncludingText": "2026-05-22T08:08:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
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
      "sponsorshipDate": "2026-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "WY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MD"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7555ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7555\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Pocan (for himself, Mr. Biggs of Arizona , Ms. Omar , Ms. Simon , Mr. McGovern , Mrs. Ramirez , Ms. Schakowsky , Ms. Norton , Mr. DeSaulnier , Ms. Stansbury , Mr. Nadler , Ms. Lee of Pennsylvania , Ms. Moore of Wisconsin , Ms. Tlaib , Mrs. Foushee , Mrs. Watson Coleman , Mr. Garc\u00eda of Illinois , Mr. Davis of Illinois , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo ensure that the Department of Defense achieves a clean audit opinion on its financial statements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Audit the Pentagon Act of 2026 .\n#### 2. Findings\n**(1)**\nThe Pentagon failed its 8th consecutive audit in December 2025.\n**(2)**\nIn November 2023, upon failure of its 6th consecutive audit, the Pentagon was unable to account for hundreds of billions of dollars, accounting for 63 percent of its nearly $4 trillion in assets.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nas the overall defense budget is cut, the congressional defense committees and the Department of Defense should not endanger the Armed Forces by reducing wounded warrior accounts or vital protection (such as body armor) for members of the Armed Forces serving in harm\u2019s way;\n**(2)**\nthe valuation of legacy assets by the Department of Defense should be simplified without compromising essential controls or generally accepted government auditing standards; and\n**(3)**\nnothing in this Act should be construed to require or permit the declassification of accounting details about classified defense programs, and, as required by law, the Department of Defense should ensure financial accountability in such programs using proven practices, including using auditors with security clearances.\n#### 4. Department of Defense spending reductions in the absence of an unqualified audit opinion\n##### (a) In general\n**(1) Reductions**\nIf, during any fiscal year after fiscal year 2025, the Comptroller of the Department of Defense fails to certify to Congress that a department, agency, or other element of the Department of Defense has achieved an unqualified opinion on its full financial statements, the amount available for such department, agency, or element shall be reduced\u2014\n**(A)**\nfor the fiscal year during which such determination is made, by an amount equal to 0.5 percent; and\n**(B)**\nfor any subsequent fiscal year during which such determination is made, by an amount equal to 1.0 percent.\n**(2) Application of reductions**\nFor any fiscal year for which a reduction is made pursuant to paragraph (1) for a department, agency, or element, the amount of the reduction shall be applied on a pro rata basis against each program, project, and activity of such department, agency, or element for that fiscal year.\n**(3) Use of reduced amounts**\nThe amount of any reduction made under paragraph (1) shall be deposited in the General Fund of the Treasury and shall be available for purposes of deficit reduction.\n##### (b) Accounts excluded\nThe following accounts are excluded from any reductions under subsection (a):\n**(1)**\nMilitary personnel, reserve personnel, and National Guard personnel accounts of the Department of Defense.\n**(2)**\nThe Defense Health Program account of the Department of Defense.\n##### (c) Waiver\nThe President may waive subsection (a) with respect to an account if the President\u2014\n**(1)**\ncertifies that the application of such subsection to that account would\u2014\n**(A)**\nnegatively affect the national security of the United States or members of the Armed Forces who are deployed in combat zones; or\n**(B)**\naffect the Defense Health Program account; and\n**(2)**\nsubmits to the Committee on Appropriations and the Committee on the Budget of the House of Representatives and the Committee on Appropriations and the Committee on the Budget of the Senate a report on such waiver that includes a description of the specific activities that would be affected and why such activities are essential to the national security of the United States.\n##### (d) Report\nNot later than 60 days after a reduction takes effect under subsection (a), the Director of the Office of Management and Budget shall submit to Congress a report specifying each department, agency, or other element of the Department of Defense subject to reduction and the amount of the reduction.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe terms financial statement and external independent auditor have the meanings given those terms in section 3521(e) of title 31, United States Code.\n**(2)**\nThe term unqualified , with respect to the audit status of a financial statement, includes the characterizations clean and unmodified.",
      "versionDate": "2026-02-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-17T18:18:07Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7555ih.xml"
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
      "title": "Audit the Pentagon Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Audit the Pentagon Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that the Department of Defense achieves a clean audit opinion on its financial statements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T09:18:22Z"
    }
  ]
}
```
