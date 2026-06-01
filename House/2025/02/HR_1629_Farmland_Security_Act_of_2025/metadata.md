# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1629
- Title: Farmland Security Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1629
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-12-05T22:01:02Z
- Update date including text: 2025-12-05T22:01:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1629",
    "number": "1629",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Farmland Security Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:01:02Z",
    "updateDateIncludingText": "2025-12-05T22:01:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:00:50Z",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1629ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1629\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Ms. Perez (for herself and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Foreign Investment Disclosure Act of 1978 to remove the limitation on the amount of a civil penalty, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmland Security Act of 2025 .\n#### 2. Improving agricultural foreign investment disclosure\n##### (a) Civil penalty\nSection 3 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3502 ) is amended\u2014\n**(1)**\nin subsection (a), by striking the second sentence;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking The amount and inserting Except as provided in subsection (c), the amount ; and\n**(B)**\nby striking Act, and all that follows through the period at the end and inserting Act. ; and\n**(3)**\nby adding at the end the following:\n(c) Penalty for shell corporations (1) Definition of shell corporation In this subsection, the term shell corporation means a corporation, company, association, firm, partnership, society, joint stock company, trust, estate, or any other legal entity that has no or nominal operations. (2) Amount of penalty The amount of a civil penalty under subsection (a) for a foreign-owned shell corporation, as determined by the Secretary, shall be 100 percent of the fair market value, on the date of the assessment of the penalty, of the interest in agricultural land with respect to which the violation occurred. (3) Nonapplication of penalty A shell corporation shall not be subject to a civil penalty under this section if the shell corporation remedies a defective filing or failure to file not later than 60 days after the Secretary provides notice to the shell corporation of the defective filing or failure to file. .\n##### (b) Investigative actions\nSection 4 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3503 ) is amended\u2014\n**(1)**\nby striking The Secretary and inserting the following:\n(a) In general The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Audit The Secretary shall conduct an annual compliance audit of not less than 10 percent of the reports submitted under section 2 for the year covered by the audit to ensure the completeness and accuracy of reports submitted under that section. In conducting, such audit, the Secretary may consult with such other heads of such other Federal agencies as the Secretary determines appropriate. (c) Training The Secretary shall provide annual training to State and county-level personnel relating to identifying agricultural land for which\u2014 (1) a report is required to be submitted under section 2; but (2) no report has been submitted by the applicable foreign person. .\n##### (c) Reports\nSection 6 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3505 ) is amended\u2014\n**(1)**\nby striking the section designation and heading and all that follows through Not later than and inserting the following:\n6. Reports (a) To States Not later than ; and\n**(2)**\nby adding at the end the following:\n(b) To Congress (1) In general Not later than 180 days after the date of enactment of the Farmland Security Act of 2025 , and annually thereafter, the Secretary shall submit to Congress a report describing the results of the research carried out under paragraph (2). (2) Research The Secretary shall carry out research on\u2014 (A) the agricultural leasing activities in the United States of foreign persons, including the impact of those activities on family farms, rural communities, and the domestic food supply; (B) trends relating to the purchase of agricultural land in the United States by foreign-owned shell corporations; and (C) foreign ownership of agricultural production capacity and foreign participation in agricultural economic activity in the United States. .\n##### (d) Authorization of appropriations\nThe Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 et seq. ) is amended by adding at the end the following:\n11. Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this Act $2,000,000 for each of fiscal years 2025 through 2030. .",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-03-04",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "845",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farmland Security Act of 2025",
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
        "updateDate": "2025-05-09T15:34:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1629",
          "measure-number": "1629",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1629v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Farmland Security Act of 2025</strong></p><p>This bill\u00a0authorizes increased civil penalties for violations of the Agricultural Foreign Investment Disclosure Act of 1978 (AFIDA)\u00a0and increases Department of Agriculture (USDA) oversight of and research into foreign investment in agricultural land.\u00a0As background, AFIDA and the regulations that implemented the act require foreign investors who acquire, transfer, or hold an interest in U.S. agricultural land to report such holdings and transactions to USDA.</p><p>In general, the bill allows USDA to determine an appropriate civil penalty amount for an\u00a0AFIDA violation by removing the cap that currently\u00a0prohibits the civil penalty from exceeding 25% of the fair market value of the interest in the agricultural land\u00a0associated with the violation.</p><p>Under an exception in the bill, the civil penalty for a foreign-owned shell corporation is 100% of the fair market value of the interest in the agricultural land. The bill defines\u00a0a shell corporation to include a company, association, firm, partnership, society, joint stock company, trust, or estate that has no or nominal operations. The penalty does not apply if the shell corporation remedies a defective filing or failure to file within 60 days of USDA providing notice.</p><p>USDA must conduct annual compliance audits of at least 10% of the reports. Further, USDA must provide\u00a0state and county-level personnel certain annual training.</p><p>USDA must also annually conduct research and submit a report to Congress on foreign investment in agricultural land, including trends in the purchase of U.S. agricultural land by foreign-owned shell corporations.</p>"
        },
        "title": "Farmland Security Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1629.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmland Security Act of 2025</strong></p><p>This bill\u00a0authorizes increased civil penalties for violations of the Agricultural Foreign Investment Disclosure Act of 1978 (AFIDA)\u00a0and increases Department of Agriculture (USDA) oversight of and research into foreign investment in agricultural land.\u00a0As background, AFIDA and the regulations that implemented the act require foreign investors who acquire, transfer, or hold an interest in U.S. agricultural land to report such holdings and transactions to USDA.</p><p>In general, the bill allows USDA to determine an appropriate civil penalty amount for an\u00a0AFIDA violation by removing the cap that currently\u00a0prohibits the civil penalty from exceeding 25% of the fair market value of the interest in the agricultural land\u00a0associated with the violation.</p><p>Under an exception in the bill, the civil penalty for a foreign-owned shell corporation is 100% of the fair market value of the interest in the agricultural land. The bill defines\u00a0a shell corporation to include a company, association, firm, partnership, society, joint stock company, trust, or estate that has no or nominal operations. The penalty does not apply if the shell corporation remedies a defective filing or failure to file within 60 days of USDA providing notice.</p><p>USDA must conduct annual compliance audits of at least 10% of the reports. Further, USDA must provide\u00a0state and county-level personnel certain annual training.</p><p>USDA must also annually conduct research and submit a report to Congress on foreign investment in agricultural land, including trends in the purchase of U.S. agricultural land by foreign-owned shell corporations.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1629"
    },
    "title": "Farmland Security Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmland Security Act of 2025</strong></p><p>This bill\u00a0authorizes increased civil penalties for violations of the Agricultural Foreign Investment Disclosure Act of 1978 (AFIDA)\u00a0and increases Department of Agriculture (USDA) oversight of and research into foreign investment in agricultural land.\u00a0As background, AFIDA and the regulations that implemented the act require foreign investors who acquire, transfer, or hold an interest in U.S. agricultural land to report such holdings and transactions to USDA.</p><p>In general, the bill allows USDA to determine an appropriate civil penalty amount for an\u00a0AFIDA violation by removing the cap that currently\u00a0prohibits the civil penalty from exceeding 25% of the fair market value of the interest in the agricultural land\u00a0associated with the violation.</p><p>Under an exception in the bill, the civil penalty for a foreign-owned shell corporation is 100% of the fair market value of the interest in the agricultural land. The bill defines\u00a0a shell corporation to include a company, association, firm, partnership, society, joint stock company, trust, or estate that has no or nominal operations. The penalty does not apply if the shell corporation remedies a defective filing or failure to file within 60 days of USDA providing notice.</p><p>USDA must conduct annual compliance audits of at least 10% of the reports. Further, USDA must provide\u00a0state and county-level personnel certain annual training.</p><p>USDA must also annually conduct research and submit a report to Congress on foreign investment in agricultural land, including trends in the purchase of U.S. agricultural land by foreign-owned shell corporations.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1629"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1629ih.xml"
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
      "title": "Farmland Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmland Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Foreign Investment Disclosure Act of 1978 to remove the limitation on the amount of a civil penalty, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:33Z"
    }
  ]
}
```
