# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3442
- Title: SNAP Administrator Retention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3442
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-04-17T08:07:23Z
- Update date including text: 2026-04-17T08:07:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3442",
    "number": "3442",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "SNAP Administrator Retention Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:23Z",
    "updateDateIncludingText": "2026-04-17T08:07:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
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
      "sponsorshipDate": "2025-05-15",
      "state": "MA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
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
      "sponsorshipDate": "2025-05-15",
      "state": "DC"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "KS"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "WA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "TN"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "GA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OH"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3442ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3442\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mrs. Hayes (for herself, Mr. Jackson of Illinois , Mr. Smith of Washington , Mr. Casten , Mr. McGovern , Mr. Carter of Louisiana , Ms. Norton , and Mr. Figures ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to increase the Federal cost share for supplemental nutrition assistance program administration to improve staffing and retention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SNAP Administrator Retention Act of 2025 .\n#### 2. Cost share for SNAP administration for staffing and retention\nSection 16 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025 ) is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by striking subsection (k) and inserting subsections (k) and (m) ; and\n**(2)**\nby adding at the end the following:\n(l) Wage standards for State agency personnel Not later than 1 year after the date of enactment of the SNAP Administrator Retention Act of 2025 , wages of State agency personnel administering the supplemental nutrition assistance program shall be\u2014 (1) not less than the appropriate rate of pay that would be payable to Federal employees under subchapter III of chapter 53 of title 5, United States Code; and (2) updated annually by not less than any increase in that rate of pay, including locality adjustments. (m) Administrative cost-Sharing for staffing and retention (1) In General On approval of a wage plan submitted by a State agency under paragraph (2), the Secretary shall pay to each State agency an amount equal to 100 percent of all administrative personnel costs incurred by the State agency in carrying out the supplemental nutrition assistance program, including all costs associated with\u2014 (A) processing, hiring, and training new employees in accordance with the standards described in section 11(e)(6)(B); (B) maintaining those personnel costs; and (C) complying with the wage standards described in subsection (l). (2) Approval of wage plans Not later than 1 year after the date of enactment of the SNAP Administrator Retention Act of 2025 , a State agency shall submit to the Secretary for approval the personnel wage plans implemented by the State agency to carry out subsection (l), including the position titles, duties, wages, and appropriate rates of pay of employees. (3) Maintenance of effort The Secretary shall make payments to a State agency under paragraph (1) only if the State agency uses the funds received\u2014 (A) to supplement, not supplant, non-Federal funds used for existing administrative personnel costs under subsection (a); and (B) for existing or additional full-time equivalent positions above the number of positions that were held in the State or sub-State area in fiscal year 2024. .",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1905",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SNAP Administrator Retention Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-10T22:54:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr3442",
          "measure-number": "3442",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-15",
          "originChamber": "HOUSE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3442v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>SNAP Administrator Retention Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to pay Supplemental Nutrition Assistance Program (SNAP) state agencies for 100% of SNAP administrative personnel costs. The bill also\u00a0requires that state SNAP agency administrators be paid at least the same amount as federal employees. (Under current law, FNS generally pays 50% of a state's administrative costs for SNAP.)</p><p>Specifically, FNS must pay a state agency for 100% of all SNAP administrative personnel costs that are part of an\u00a0FNS-approved state agency personnel wage plan. This must include all costs associated with hiring and training new employees, maintaining those personnel costs,\u00a0and\u00a0complying with wage standards. The state agency must use these funds (1) to supplement, not supplant, nonfederal funds used for existing administrative personnel costs; and (2) for existing or additional full-time positions that are above the number of positions that were held in FY2024.</p><p>The bill also requires that the wage standards for SNAP state agency administrators be (1) at least the same amount as the General Schedule (GS) pay rate for federal employees; and (2) updated annually based on any increase in the GS pay rate, including locality adjustments.</p>"
        },
        "title": "SNAP Administrator Retention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3442.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Administrator Retention Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to pay Supplemental Nutrition Assistance Program (SNAP) state agencies for 100% of SNAP administrative personnel costs. The bill also\u00a0requires that state SNAP agency administrators be paid at least the same amount as federal employees. (Under current law, FNS generally pays 50% of a state's administrative costs for SNAP.)</p><p>Specifically, FNS must pay a state agency for 100% of all SNAP administrative personnel costs that are part of an\u00a0FNS-approved state agency personnel wage plan. This must include all costs associated with hiring and training new employees, maintaining those personnel costs,\u00a0and\u00a0complying with wage standards. The state agency must use these funds (1) to supplement, not supplant, nonfederal funds used for existing administrative personnel costs; and (2) for existing or additional full-time positions that are above the number of positions that were held in FY2024.</p><p>The bill also requires that the wage standards for SNAP state agency administrators be (1) at least the same amount as the General Schedule (GS) pay rate for federal employees; and (2) updated annually based on any increase in the GS pay rate, including locality adjustments.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr3442"
    },
    "title": "SNAP Administrator Retention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Administrator Retention Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to pay Supplemental Nutrition Assistance Program (SNAP) state agencies for 100% of SNAP administrative personnel costs. The bill also\u00a0requires that state SNAP agency administrators be paid at least the same amount as federal employees. (Under current law, FNS generally pays 50% of a state's administrative costs for SNAP.)</p><p>Specifically, FNS must pay a state agency for 100% of all SNAP administrative personnel costs that are part of an\u00a0FNS-approved state agency personnel wage plan. This must include all costs associated with hiring and training new employees, maintaining those personnel costs,\u00a0and\u00a0complying with wage standards. The state agency must use these funds (1) to supplement, not supplant, nonfederal funds used for existing administrative personnel costs; and (2) for existing or additional full-time positions that are above the number of positions that were held in FY2024.</p><p>The bill also requires that the wage standards for SNAP state agency administrators be (1) at least the same amount as the General Schedule (GS) pay rate for federal employees; and (2) updated annually based on any increase in the GS pay rate, including locality adjustments.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr3442"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3442ih.xml"
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
      "title": "SNAP Administrator Retention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SNAP Administrator Retention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to increase the Federal cost share for supplemental nutrition assistance program administration to improve staffing and retention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:36Z"
    }
  ]
}
```
