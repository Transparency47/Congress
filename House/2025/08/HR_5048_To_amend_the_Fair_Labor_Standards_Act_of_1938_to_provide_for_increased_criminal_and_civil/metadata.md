# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5048
- Title: Don’t STEAL Act
- Congress: 119
- Bill type: HR
- Bill number: 5048
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2026-04-22T08:07:36Z
- Update date including text: 2026-04-22T08:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5048",
    "number": "5048",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Don\u2019t STEAL Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:36Z",
    "updateDateIncludingText": "2026-04-22T08:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
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
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:03:00Z",
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
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "PA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "WI"
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
      "sponsorshipDate": "2025-08-26",
      "state": "DC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "MI"
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
      "sponsorshipDate": "2025-08-26",
      "state": "NM"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "IN"
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
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "WA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "VT"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "OH"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "MI"
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
      "sponsorshipDate": "2025-08-26",
      "state": "HI"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "FL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-08-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CT"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5048ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5048\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Magaziner (for himself, Mr. Evans of Pennsylvania , Mr. Pocan , Ms. Norton , Mrs. Dingell , Ms. Stansbury , Mr. Boyle of Pennsylvania , Mr. Carson , Mr. Goldman of New York , Ms. Chu , Ms. Perez , Mr. Norcross , Mr. Jackson of Illinois , Ms. Balint , Mrs. Sykes , Mr. Khanna , Ms. Tlaib , Ms. Tokuda , Ms. Ocasio-Cortez , Mrs. Cherfilus-McCormick , Mrs. Watson Coleman , and Ms. Schakowsky ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to provide for increased criminal and civil penalties for wage theft.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t Stand for Taking Employed Americans\u2019 Livings Act or the Don\u2019t STEAL Act .\n#### 2. Right to full compensation\n##### (a) In general\nThe Fair Labor Standards Act of 1938 is amended by inserting after section 7 ( 29 U.S.C. 207 ) the following:\n8. Right to full compensation (a) Compensation \u2014 (1) In general Subject to section 7, an employer shall compensate an employee (who is described in subsection (b)) at a rate that is not less than the greater of\u2014 (A) the rate required by any contract, collective bargaining agreement, or other employment agreement (as such term is defined by the Secretary) that specifies how much such employer shall compensate such employee; or (B) the wage rate required under applicable Federal or State law. (b) Employee Engaged In Commerce The requirement under subsection (a) shall apply with respect to any employee who in any workweek is engaged in commerce or in the production of goods for commerce, or is employed in an enterprise engaged in commerce or in the production of goods for commerce. .\n##### (b) Conforming amendment\nSection 10 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 210 ) is repealed.\n##### (c) Prohibited Acts\nSection 15(a)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 215(a)(2) ) is amended by striking or section 7 and inserting , 7, or 8 .\n#### 3. Penalties for wage theft\n##### (a) Criminal penalties\nSubsection (a) of section 16 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216 ) is amended\u2014\n**(1)**\nby striking Any person and inserting (1) Except as provided by paragraph (2), any person ;\n**(2)**\nby striking subsection each place it appears and inserting paragraph ; and\n**(3)**\nby adding at the end the following:\n(2) (A) Any person who willfully violates section 3(m)(2)(B), 6, 7, or 8 of this Act, relating to wages, shall be\u2014 (i) in the case of a violation of section 3(m)(2)(B), 6, 7, or 8 relating to unpaid wages, or unpaid overtime compensation, in an amount greater than $1,000, fined in accordance with title 18, United States Code, imprisoned for not more than 5 years, or both; or (ii) in the case of a violation of section 3(m)(2)(B), 6, 7, or 8 relating to unpaid wages, or unpaid overtime compensation, in an amount equal to or less than $1,000, fined in accordance with title 18, United States Code, imprisoned for not more than 1 year, or both. (B) In determining the amount of a fine under subparagraph (A), the following factors shall be considered: (i) The gravity of the violation, including the number of employees affected and the value of the unlawfully kept wages. (ii) Whether the person charged has previously been convicted for a violation of section 3(m)(2)(B), 6, 7, or 8. (iii) The appropriateness of the penalty given the size of the business of the person convicted. .\n##### (b) Civil penalties\nSection 16 of such Act is further amended\u2014\n**(1)**\nin subsection (b), by striking or section 7 each place it appears and inserting , 7, or 8 ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking or 7 and inserting , 7, or 8 ; and\n**(B)**\nby striking and 7 and inserting , 7, and 8 ; and\n**(3)**\nin subsection (e), by striking or 7 and inserting , 7, or 8 .\n##### (c) Funds for Wage and Hour Division\nParagraph (5) of section 16(e) of such Act is amended\u2014\n**(1)**\nby striking 12, and inserting 12 and fines collected under subsection (a)(2) of this section, ; and\n**(2)**\nby adding at the end the following: Sums collected as fines under subsection (a)(2) shall be applied by the Wage and Hour Division of the Department of Labor to the costs of enforcing sections 3(m)(2)(B), 6, 7, and 8. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to violations of section 3(m)(2)(B), 6, 7, or 8 of the Fair Labor Standards Act of 1938 occurring on or after the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-08-26",
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
        "updateDate": "2025-09-19T17:12:08Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5048ih.xml"
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
      "title": "Don\u2019t STEAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-28T02:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t STEAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-28T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t Stand for Taking Employed Americans\u2019 Livings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-28T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to provide for increased criminal and civil penalties for wage theft.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-28T02:48:18Z"
    }
  ]
}
```
