# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1236
- Title: FISCAL Act
- Congress: 119
- Bill type: S
- Bill number: 1236
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-02-25T16:57:01Z
- Update date including text: 2026-02-25T16:57:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1236",
    "number": "1236",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "FISCAL Act",
    "type": "S",
    "updateDate": "2026-02-25T16:57:01Z",
    "updateDateIncludingText": "2026-02-25T16:57:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
        "item": {
          "date": "2025-04-01T20:18:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "LA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1236is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1236\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Fetterman (for himself, Mr. Kennedy , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Richard B. Russell National School Lunch Act to require schools to offer a variety of milk to students participating in the school lunch program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom in School Cafeterias and Lunches Act or the FISCAL Act .\n#### 2. Types of milk offered under the school lunch program\n##### (a) In general\nSection 9(a)(2) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758(a)(2) ) is amended\u2014\n**(1)**\nin the heading, by striking Fluid milk and inserting Milk ;\n**(2)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nby striking fluid milk. Such milk and inserting milk, including fluid milk and plant-based milk, which ;\n**(ii)**\nby inserting or, in the case of a plant-based milk not included under those guidelines, consistent with nutritional standards established by the Secretary after ( 7 U.S.C. 5341 ) ; and\n**(iii)**\nby inserting and after the semicolon;\n**(B)**\nin clause (ii), by striking ; and and inserting a period; and\n**(C)**\nby striking clause (iii);\n**(3)**\nby striking subparagraph (B);\n**(4)**\nby redesignating subparagraph (C) as subparagraph (B); and\n**(5)**\nin subparagraph (B) (as so redesignated), in the matter preceding clause (i), by inserting or plant-based milk after fluid milk .\n##### (b) Conforming amendments\n**(1)**\nSection 14(f) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1762a(f) ) is amended, in the third sentence, by inserting or plant-based before milk .\n**(2)**\nSection 20(c) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769b(c) ) is amended by striking fluid .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2539",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FISCAL Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:41:23Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s1236",
          "measure-number": "1236",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1236v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>"
        },
        "title": "FISCAL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1236.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1236"
    },
    "title": "FISCAL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Freedom in School Cafeterias and Lunches Act or the FISCAL Act</strong></p><p>This bill revises requirements for milk provided by the National School Lunch Program of the Department of Agriculture (USDA) to require that schools offer plant-based milk.</p><p>Under current law, schools must provide a substitute for fluid milk for students whose disability restricts their diet (on receipt of a written statement from a licensed physician). Schools may also substitute a nondairy beverage for fluid milk for students who have an identified medical or other special dietary need (on receipt of a written statement from a medical authority or a\u00a0student's parent or legal guardian).</p><p>The bill eliminates the exceptions and documentation requirements. Instead, schools participating in the school lunch program must offer all students a plant-based milk option that is\u00a0consistent with (1) the most recent U.S. Dietary Guidelines, or (2) USDA-established nutritional standards\u00a0if the milk is\u00a0not included under those guidelines. </p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1236"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1236is.xml"
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
      "title": "FISCAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FISCAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom in School Cafeterias and Lunches Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Richard B. Russell National School Lunch Act to require schools to offer a variety of milk to students participating in the school lunch program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:29Z"
    }
  ]
}
```
