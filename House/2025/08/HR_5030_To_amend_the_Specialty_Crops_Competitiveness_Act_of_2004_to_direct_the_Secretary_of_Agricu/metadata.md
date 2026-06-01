# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5030?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5030
- Title: Specialty Crop Domestic Market Promotion and Development Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5030
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2026-05-16T08:07:52Z
- Update date including text: 2026-05-16T08:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5030",
    "number": "5030",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:52Z",
    "updateDateIncludingText": "2026-05-16T08:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
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
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:51:44Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "HI"
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
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NJ"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5030ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5030\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. Valadao (for himself, Mr. Harder of California , Ms. Brownley , Mr. Panetta , Mr. Costa , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Specialty Crops Competitiveness Act of 2004 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to eligible organizations to encourage the development, maintenance, and expansion of commercial domestic market for domestically produced specialty crop commodities.\n#### 1. Short title\nThis Act may be cited as the Specialty Crop Domestic Market Promotion and Development Program Act of 2025 .\n#### 2. Specialty crop domestic market promotion and development program\nTitle II of the Specialty Crops Competitiveness Act of 2004 ( 7 U.S.C. 7712a et seq. ) is amended by adding at the end the following:\n204. Specialty crop domestic market promotion and development program (a) In general For purposes of encouraging the development, maintenance, and expansion of the commercial domestic market for domestically produced specialty crop commodities, the Secretary of Agriculture, acting through the Administrator of the Agricultural Marketing Service, shall establish a program under which the Secretary will award grants to eligible organizations to implement a domestic market development program for specialty crops. (b) Application An eligible organization seeking a grant under this section shall submit to the Secretary\u2014 (1) an application at such time, in such manner, and containing such information as the Secretary may require; (2) a marketing plan that meets the requirements of subsection (c); and (3) a certification that any Federal funds received by such organization under this section will supplement, but not supplant, funds from non-Federal sources (including a private entity) to carry out a domestic market development program for specialty crops. (c) Marketing plan (1) In general A marketing plan submitted under subsection (b) shall\u2014 (A) describe the advertising or other demand-oriented, generic domestic promotion activities to be carried out by the eligible organization using funds awarded through a grant under this section; and (B) contain\u2014 (i) a description of the manner in which funds received by the eligible organization through a grant under this section, in conjunction with funds and services provided by the eligible organization, will be expended in implementing the marketing plan; (ii) the market goals to be achieved under the marketing plan; and (iii) such additional information as may be required by the Secretary. (2) Amendments A marketing plan approved under this section may be amended by the eligible organization submitting such plan at any time, subject to the approval of the Secretary. (d) Amount of grant (1) In general The Secretary shall justify, in writing, the level of funds awarded through a grant to an eligible organization and the level of matching funds to be required of the organization. (2) Matching funds The recipient of a grant under this section shall provide non-Federal matching funds equal to not less than 25 percent of the amount of the grant, or such other amount determined by the Secretary pursuant to paragraph (1). (3) In-kind support Non-Federal matching funds described in paragraph (2) may include in-kind support. (e) Multiyear basis The Secretary may provide assistance under this section on a multiyear basis. The Secretary shall conduct an annual review of any grant awarded on a multiyear basis to ensure that the eligible organization has complied with the marketing plan submitted under subsection (c). (f) Termination The Secretary may terminate any grant made, or to be made, under this section if the Secretary determines that the eligible organization receiving such grant\u2014 (1) is not adhering to the terms and conditions applicable to the grant; (2) is not implementing the marketing plan submitted under subsection (b) or is not adequately meeting the established goals of the plan; or (3) is not adequately contributing its own resources to the implementation of the plan. (g) Evaluations Beginning not later than 15 months after the first grant is awarded under this section to an eligible organization, the Secretary shall monitor the expenditures by eligible organizations made using grant funds, including the following: (1) A thorough accounting of such expenditures. (2) An evaluation of the effectiveness of the marketing plan of the eligible organization in developing, maintaining, or expanding the commercial domestic market for specialty crops. (h) Limitation on use of funds Funds received through a grant under this section may not be used\u2014 (1) to provide direct assistance to any domestic or foreign for-profit corporation for the corporation\u2019s use in promoting foreign-produced products; or (2) to provide direct assistance to any for-profit corporation that is not recognized as a small business concern (as described in section 3(a) of the Small Business Act ( 15 U.S.C. 632(a) )), other than\u2014 (A) a cooperative; (B) an association described in the Act of February 18, 1922 ( 7 U.S.C. 291 ); or (C) a nonprofit trade association. (i) Audits If, as a result of an evaluation or audit of activities of an eligible organization using funds made available through a grant under this section, the Secretary determines that a further review is justified in order to ensure compliance with the requirements of this section, the Secretary shall require the eligible organization to contract for an independent audit of the activities carried out using funds awarded under a grant under this section, including activities of any subcontractor of an eligible organization. (j) Eligible organization defined In this section, the term eligible organization means\u2014 (1) a United States agricultural trade organization or regional State-related organization that promotes the sale of United States produced and grown specialty crops and that does not profit directly from specific sales of United States specialty crops; (2) a cooperative organization or State agency that promotes the sale of United States produced and grown specialty crops; (3) a private organization that promotes the sale of United States produced and grown specialty crop commodities if the Secretary determines that such organization would significantly contribute to increased domestic purchases of United States produced specialty crop commodities; or (4) a specialty crop organization operating under Federal marketing orders. (k) Funding (1) Authorization of appropriations There is authorized to be appropriated to carry out this section $75,000,000 for fiscal year 2026 and each fiscal year thereafter. (2) Administrative expenses The Secretary may use funds made available under paragraph (1) to carry out this section for a fiscal year for expenses related to administering the program under this section. .",
      "versionDate": "2025-08-22",
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
        "actionDate": "2026-01-13",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "5059",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025",
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
        "updateDate": "2025-09-05T17:01:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-22",
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
          "measure-id": "id119hr5030",
          "measure-number": "5030",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-22",
          "originChamber": "HOUSE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5030v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-08-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Specialty Crop Domestic Market Promotion and Development Program Act of 2025</strong></p><p>This bill directs the Agricultural Marketing Service to establish a grant program to encourage the development, maintenance, and expansion of the commercial domestic market for domestically produced specialty crop commodities (e.g., for advertising or other demand-oriented, generic domestic promotion activities).</p><p>Organizations eligible\u00a0for the grant program include\u00a0those that promote U.S. produced and grown specialty crop sales and are (1) U.S. agricultural trade organizations or regional state-related organizations that do not profit directly from U.S. specialty crop sales, (2) cooperative organizations or state agencies, or (3) certain private organizations. Specialty crop organizations operating under federal marketing orders are also eligible for the grant program.</p>"
        },
        "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5030.xml",
    "summary": {
      "actionDate": "2025-08-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Specialty Crop Domestic Market Promotion and Development Program Act of 2025</strong></p><p>This bill directs the Agricultural Marketing Service to establish a grant program to encourage the development, maintenance, and expansion of the commercial domestic market for domestically produced specialty crop commodities (e.g., for advertising or other demand-oriented, generic domestic promotion activities).</p><p>Organizations eligible\u00a0for the grant program include\u00a0those that promote U.S. produced and grown specialty crop sales and are (1) U.S. agricultural trade organizations or regional state-related organizations that do not profit directly from U.S. specialty crop sales, (2) cooperative organizations or state agencies, or (3) certain private organizations. Specialty crop organizations operating under federal marketing orders are also eligible for the grant program.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr5030"
    },
    "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-08-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Specialty Crop Domestic Market Promotion and Development Program Act of 2025</strong></p><p>This bill directs the Agricultural Marketing Service to establish a grant program to encourage the development, maintenance, and expansion of the commercial domestic market for domestically produced specialty crop commodities (e.g., for advertising or other demand-oriented, generic domestic promotion activities).</p><p>Organizations eligible\u00a0for the grant program include\u00a0those that promote U.S. produced and grown specialty crop sales and are (1) U.S. agricultural trade organizations or regional state-related organizations that do not profit directly from U.S. specialty crop sales, (2) cooperative organizations or state agencies, or (3) certain private organizations. Specialty crop organizations operating under federal marketing orders are also eligible for the grant program.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr5030"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5030ih.xml"
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
      "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Specialty Crop Domestic Market Promotion and Development Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Specialty Crops Competitiveness Act of 2004 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to eligible organizations to encourage the development, maintenance, and expansion of commercial domestic market for domestically produced specialty crop commodities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:21Z"
    }
  ]
}
```
