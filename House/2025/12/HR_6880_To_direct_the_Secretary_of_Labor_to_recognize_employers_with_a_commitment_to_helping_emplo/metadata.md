# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6880
- Title: Honoring Family-Friendly Workplaces Act
- Congress: 119
- Bill type: HR
- Bill number: 6880
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-22T14:57:14Z
- Update date including text: 2026-01-22T14:57:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6880",
    "number": "6880",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Honoring Family-Friendly Workplaces Act",
    "type": "HR",
    "updateDate": "2026-01-22T14:57:14Z",
    "updateDateIncludingText": "2026-01-22T14:57:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:05Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6880ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6880\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Meng (for herself, Ms. Norton , Ms. Tlaib , and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Labor to recognize employers with a commitment to helping employees balance workplace responsibilities and family obligations.\n#### 1. Short title\nThis Act may be cited as the Honoring Family-Friendly Workplaces Act .\n#### 2. Definitions\nIn this Act:\n**(1) Employee; employer**\nThe terms employee and employer have the meanings given such terms in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 3. Certification program established\n##### (a) In general\nThe Secretary shall establish a national certification program to award certifications to recognize employers that have a commitment to helping employees balance employment responsibilities and family obligations (referred to in this section as family-friendly certifications ).\n##### (b) Criteria for certification\nIn order to be eligible to receive a family-friendly certification, an employer must carry out each of the following family-friendly employment policies and benefits:\n**(1)**\nAssistance paying for, or referring employees to, fertility or adoption services.\n**(2)**\nPaid family leave of not less than 12 weeks per year, including the option to use leave for any of the following reasons:\n**(A)**\nThe birth of a child of the employee and in order to care for such child.\n**(B)**\nThe placement of a child with the employee for adoption or foster care.\n**(C)**\nTo address the employee's own serious health condition, including pregnancy, childbirth, or pregnancy loss.\n**(D)**\nTo address the serious health condition (as defined in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 )) of a family member.\n**(E)**\nFor specific military caregiving and leave.\n**(3)**\nPaid sick days for employees that are separate from time accrued as part of a paid time off policy.\n**(4)**\nA subsidy for child care or policies that allow parents to work alongside their infants in safe settings.\n**(5)**\nPolicies that allow for flexible hours once a parent returns to work after a birth, adoption, or foster care placement.\n**(6)**\nIf feasible, policies that allow employees to work remotely as needed for reasons related to the care of a child.\n**(7)**\nLactation support, such as reimbursement of expressed breastmilk delivery while on travel, access to pumps, kits, and other lactation supplies and amenities, and access to lactation consultants and support.\n##### (c) Application\nAn employer who desires to receive a family-friendly certification from the Secretary under this section shall submit an application to the Secretary at such time, containing such information, and in such manner as the Secretary may require.\n##### (d) Award of certification\nThe Secretary shall review applications submitted under subparagraph (c) and award a family-friendly certification to an employer whose application demonstrates that the employer has met the requirements established under subsection (b) regarding family-friendly policies and benefits.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary.",
      "versionDate": "2025-12-18",
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
        "name": "Labor and Employment",
        "updateDate": "2026-01-22T14:57:13Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6880ih.xml"
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
      "title": "Honoring Family-Friendly Workplaces Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring Family-Friendly Workplaces Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to recognize employers with a commitment to helping employees balance workplace responsibilities and family obligations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:23Z"
    }
  ]
}
```
