# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2539
- Title: FISCAL Act
- Congress: 119
- Bill type: HR
- Bill number: 2539
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-02-25T20:00:40Z
- Update date including text: 2026-02-25T20:00:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2539",
    "number": "2539",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "FISCAL Act",
    "type": "HR",
    "updateDate": "2026-02-25T20:00:40Z",
    "updateDateIncludingText": "2026-02-25T20:00:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:01:25Z",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "SC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "LA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "GA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2539ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2539\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Carter of Louisiana (for himself and Ms. Mace ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Richard B. Russell National School Lunch Act to require schools to offer a variety of milk to students participating in the school lunch program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom in School Cafeterias and Lunches Act or the FISCAL Act .\n#### 2. Types of milk offered under the school lunch program\n##### (a) In general\nSection 9(a)(2) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758(a)(2) ) is amended\u2014\n**(1)**\nin the heading, by striking Fluid milk and inserting Milk ;\n**(2)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nby striking fluid milk. Such milk and inserting milk, including fluid milk and plant-based milk, which ;\n**(ii)**\nby inserting or, in the case of a plant-based milk not included under those guidelines, consistent with nutritional standards established by the Secretary after ( 7 U.S.C. 5341 ) ; and\n**(iii)**\nby inserting and after the semicolon;\n**(B)**\nin clause (ii), by striking ; and and inserting a period; and\n**(C)**\nby striking clause (iii);\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating subparagraph (C) as subparagraph (B); and\n**(5)**\nin subparagraph (B) (as so redesignated), in the matter preceding clause (i), by inserting or plant-based milk after fluid milk .\n##### (b) Conforming amendments\n**(1)**\nSection 14(f) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1762a(f) ) is amended, in the third sentence, by inserting or plant-based before milk .\n**(2)**\nSection 20(c) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769b(c) ) is amended by striking fluid .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FISCAL Act",
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
        "updateDate": "2025-05-06T17:40:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2539",
          "measure-number": "2539",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2539v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>"
        },
        "title": "FISCAL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2539.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr2539"
    },
    "title": "FISCAL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr2539"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2539ih.xml"
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
      "title": "FISCAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FISCAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom in School Cafeterias and Lunches Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Richard B. Russell National School Lunch Act to require schools to offer a variety of milk to students participating in the school lunch program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:27Z"
    }
  ]
}
```
