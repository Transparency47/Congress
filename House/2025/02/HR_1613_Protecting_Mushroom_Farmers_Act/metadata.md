# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1613?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1613
- Title: Protecting Mushroom Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 1613
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-02-18T13:46:08Z
- Update date including text: 2026-02-18T13:46:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1613",
    "number": "1613",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Protecting Mushroom Farmers Act",
    "type": "HR",
    "updateDate": "2026-02-18T13:46:08Z",
    "updateDateIncludingText": "2026-02-18T13:46:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
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
          "date": "2025-02-26T15:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:45:37Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1613ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1613\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Ms. Houlahan (for herself and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to require the research and development of a policy to insure the production of mushrooms.\n#### 1. Short title\nThis Act may be cited as the Protecting Mushroom Farmers Act .\n#### 2. Research and development on mushrooms\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Mushrooms (A) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding a policy to insure\u2014 (i) the production of mushroom growing media; and (ii) the production of mushrooms. (B) Availability of policy Notwithstanding the second sentence of section 508(a)(1), and section 508(a)(2), the Corporation shall make a policy described in subparagraph (A) available if the requirements of section 508(h) are met. (C) Research and development described Research and development described in subparagraph (A) shall evaluate the effectiveness of policies described in that subparagraph, including policies that\u2014 (i) are based on the risk of\u2014 (I) pests, including mushroom phorid flies and sciarid flies; (II) fungal pathogens; and (III) viral pathogens; (ii) consider other causes of loss applicable to mushroom compost and mushroom production, such as\u2014 (I) a loss of electricity due to weather; and (II) loss of growing media due to excessive 5-year, 10-year, or 20-year rainfall events; (iii) consider appropriate best practices to minimize the risk of loss; (iv) consider whether to provide coverage for mushrooms under 1 policy or to provide coverage for various phases of production; (v) have streamlined reporting and paperwork requirements that take into account short propagation schedules, variable crop years, and the variety of mushrooms that may be produced in a single facility; and (vi) provide protection for revenue losses. (D) Report Not later than 2 years after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that describes\u2014 (i) the results of the research and development carried out under subparagraph (A); and (ii) any recommendations with respect to those results. .",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "updateDate": "2025-03-27T13:39:58Z"
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
          "measure-id": "id119hr1613",
          "measure-number": "1613",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1613v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Mushroom Farmers Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure\u00a0the production of mushrooms and mushroom-growing media. (The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified\u00a0FCIP requirements.</p><p>As part of the research and development, the bill requires an evaluation of the effectiveness of insurance for the production of mushrooms, including policies that (1) are based on the risk of specific pests and pathogens, (2) consider appropriate best practices to minimize the risk of loss, and (3) consider whether to provide coverage for mushrooms under one policy or to provide coverage for various phases of production.</p>"
        },
        "title": "Protecting Mushroom Farmers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1613.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Mushroom Farmers Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure\u00a0the production of mushrooms and mushroom-growing media. (The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified\u00a0FCIP requirements.</p><p>As part of the research and development, the bill requires an evaluation of the effectiveness of insurance for the production of mushrooms, including policies that (1) are based on the risk of specific pests and pathogens, (2) consider appropriate best practices to minimize the risk of loss, and (3) consider whether to provide coverage for mushrooms under one policy or to provide coverage for various phases of production.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1613"
    },
    "title": "Protecting Mushroom Farmers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Mushroom Farmers Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure\u00a0the production of mushrooms and mushroom-growing media. (The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified\u00a0FCIP requirements.</p><p>As part of the research and development, the bill requires an evaluation of the effectiveness of insurance for the production of mushrooms, including policies that (1) are based on the risk of specific pests and pathogens, (2) consider appropriate best practices to minimize the risk of loss, and (3) consider whether to provide coverage for mushrooms under one policy or to provide coverage for various phases of production.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1613"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1613ih.xml"
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
      "title": "Protecting Mushroom Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Mushroom Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to require the research and development of a policy to insure the production of mushrooms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:25Z"
    }
  ]
}
```
