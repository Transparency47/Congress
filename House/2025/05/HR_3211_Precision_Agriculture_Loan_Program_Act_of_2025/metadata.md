# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3211
- Title: Precision Agriculture Loan Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3211
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2025-10-04T08:05:32Z
- Update date including text: 2025-10-04T08:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-06: Introduced in House

## Actions

- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3211",
    "number": "3211",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Precision Agriculture Loan Program Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:32Z",
    "updateDateIncludingText": "2025-10-04T08:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:02:50Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
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
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3211ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3211\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mr. Feenstra (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to establish a precision agriculture loan program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Precision Agriculture Loan Program Act of 2025 .\n#### 2. Precision agriculture loan program\nSubtitle F of title I of the Food, Conservation, and Energy Act of 2008 is amended by inserting after section 1614 ( 7 U.S.C. 8789 ) the following:\n1614A. Precision agriculture loan program (a) Definitions In this section: (1) Precision agriculture The term precision agriculture means managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. (2) Precision agriculture equipment The term precision agriculture equipment means any equipment or technology that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production, including\u2014 (A) Global Positioning System-based or geospatial mapping; (B) satellite or aerial imagery; (C) yield monitors; (D) soil mapping; (E) sensors for gathering data on crop, soil, or livestock conditions; (F) Internet of Things and telematics technologies; (G) data management software and advanced analytics; (H) network connectivity products and solutions; (I) Global Positioning System guidance or auto-steer systems; (J) variable rate technology for applying inputs, such as section control; and (K) any other technology, as determined by the Secretary, that leads to a reduction in, or improves efficiency of, crop and livestock production inputs, which may include seed, feed, fertilizer, chemicals, water, and time. (b) Program As soon as practicable after the date of enactment of this section, the Secretary shall establish a precision agriculture loan program to encourage the adoption of precision agriculture by providing funds to producers engaged in livestock or crop production for the purchase of precision agriculture equipment. (c) Administration The precision agriculture loan program under this section shall be administered by the Secretary, acting through the Deputy Administrator for Farm Programs of the Farm Service Agency. (d) Eligible producers A precision agriculture loan under this section shall be made available to any producer described in subsection (b) that, as determined by the Secretary\u2014 (1) has a satisfactory credit history; (2) will use the loan funds to purchase precision agriculture equipment; and (3) demonstrates an ability to repay the loan. (e) Term of loans A precision agriculture loan under this section shall have a maximum term of 12 years. (f) Loan amount The maximum aggregate loan amount of a precision agriculture loan under this section shall be $500,000. (g) Loan security Approval of a precision agriculture loan under this section shall require the borrower to provide loan security to the Secretary, in the form of\u2014 (1) a lien on the precision agriculture equipment being purchased; or (2) such other security as is acceptable to the Secretary. (h) Reporting (1) Definition of recipient producer In this subsection, the term recipient producer means an eligible producer described in subsection (d) that received a precision agriculture loan under this section during the fiscal year covered by the applicable report prepared under paragraph (2). (2) Preparation of report For each fiscal year, the Secretary shall prepare a report that includes\u2014 (A) aggregate data based on a review of each outstanding loan made by the Secretary under this section; and (B) a description of\u2014 (i) for the United States and for each State and county (or equivalent jurisdiction) in the United States\u2014 (I) the age of each recipient producer; (II) the duration during which each recipient producer has engaged in agricultural production; (III) the size of the farm or ranch of each recipient producer; (IV) the total amount provided as loans under this section for each category of equipment or technology described in subparagraphs (A) through (K) of subsection (a)(2) during the fiscal year covered by the report; and (V) the estimated input reduced or environmental benefits received per category of equipment or technology described in those subparagraphs with respect to which a loan was provided under this section during the fiscal year covered by the report or any prior fiscal year, including the estimated input reduced or environmental benefits received per category\u2014 (aa) during the fiscal year covered by the report with respect to\u2014 (AA) loans provided under this section during that fiscal year; and (BB) loans provided under this section during that fiscal year or any prior fiscal year; and (bb) in the aggregate with respect to all loans provided under this section during or prior to the fiscal year covered by the report; (VI) the race, ethnicity, and gender of each recipient producer; (VII) the 1 or more agricultural commodities or types of enterprise for which each loan provided under this section during the fiscal year was provided; (VIII) the amount of each loan provided under this section during the fiscal year; and (IX) the default rate of the loans made under this section during\u2014 (aa) the fiscal year covered by the report; (bb) each preceding fiscal year; and (cc) in the aggregate with respect to all loans provided under this section during or prior to the fiscal year covered by the report; and (ii) for each State and county (or equivalent jurisdiction) in the United States, the number of outstanding loans made under this section, according to the loan size cohort. (3) Submission of report The Secretary shall\u2014 (A) not later than 1 year after the date of enactment of this Act, and annually thereafter, submit the report described in paragraph (2) to\u2014 (i) the Committee on Agriculture, Nutrition, and Forestry of the Senate; (ii) the Committee on Appropriations of the Senate; (iii) the Committee on Agriculture of the House of Representatives; and (iv) the Committee on Appropriations of the House of Representatives; and (B) not later than 90 days after the date on which the report is submitted under subparagraph (A), make the report publicly available. (i) Authorization of appropriations There are authorized to be appropriated to the Secretary such sums as are necessary to carry out this section. .",
      "versionDate": "2025-05-06",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-05T14:10:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
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
          "measure-id": "id119hr3211",
          "measure-number": "3211",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-06",
          "originChamber": "HOUSE",
          "update-date": "2025-08-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3211v00",
            "update-date": "2025-08-26"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Precision Agriculture Loan Program Act of 2025</strong><strong></strong></p><p>This bill establishes a loan program within the Farm Service Agency to assist agricultural producers in purchasing precision agriculture equipment and technology, such as geospatial mapping, data management and analytics software, and network connectivity products and solutions. Under this program, the maximum aggregate loan amount of a precision agriculture loan\u00a0is $500,000.</p><p><em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality.</p>"
        },
        "title": "Precision Agriculture Loan Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3211.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Precision Agriculture Loan Program Act of 2025</strong><strong></strong></p><p>This bill establishes a loan program within the Farm Service Agency to assist agricultural producers in purchasing precision agriculture equipment and technology, such as geospatial mapping, data management and analytics software, and network connectivity products and solutions. Under this program, the maximum aggregate loan amount of a precision agriculture loan\u00a0is $500,000.</p><p><em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr3211"
    },
    "title": "Precision Agriculture Loan Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Precision Agriculture Loan Program Act of 2025</strong><strong></strong></p><p>This bill establishes a loan program within the Farm Service Agency to assist agricultural producers in purchasing precision agriculture equipment and technology, such as geospatial mapping, data management and analytics software, and network connectivity products and solutions. Under this program, the maximum aggregate loan amount of a precision agriculture loan\u00a0is $500,000.</p><p><em>Precision agriculture</em> refers to managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr3211"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3211ih.xml"
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
      "title": "Precision Agriculture Loan Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Precision Agriculture Loan Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T06:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Conservation, and Energy Act of 2008 to establish a precision agriculture loan program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T06:33:59Z"
    }
  ]
}
```
