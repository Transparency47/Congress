# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/442
- Title: Quality Loss Adjustment Improvement for Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 442
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-05T22:08:32Z
- Update date including text: 2025-12-05T22:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/442",
    "number": "442",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000595",
        "district": "5",
        "firstName": "Julia",
        "fullName": "Rep. Letlow, Julia [R-LA-5]",
        "lastName": "Letlow",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Quality Loss Adjustment Improvement for Farmers Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:32Z",
    "updateDateIncludingText": "2025-12-05T22:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:05:16Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr442ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 442\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Letlow introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to modify a provision relating to quality loss adjustment coverage.\n#### 1. Short title\nThis Act may be cited as the Quality Loss Adjustment Improvement for Farmers Act .\n#### 2. Quality loss adjustment coverage\nSection 508(m) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(m) ) is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby striking subparagraph (A) and inserting the following:\n(A) Periodic review Beginning in calendar year 2025, and once every 5 years thereafter, the Corporation shall contract with a qualified person to conduct a review of the quality loss adjustment procedures of the Corporation, each of which shall be completed not later than 1 year after the date of commencement of the review. ;\n**(B)**\nin subparagraph (B), by striking Effective beginning not later than the 2004 reinsurance year, based on the review, the Corporation and inserting Based on each review conducted under subparagraph (A), the Corporation ;\n**(C)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(D)**\nby inserting after subparagraph (A) the following:\n(B) Stakeholder engagement Each review under subparagraph (A) shall include engagement from regionally diverse industry stakeholders for each agricultural commodity for which a quality loss adjustment is offered. ; and\n**(E)**\nby adding at the end the following:\n(D) Report On the completion of each review under subparagraph (A), the Corporation shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes\u2014 (i) findings from that review; (ii) changes to the quality loss adjustment procedures; and (iii) the stakeholder engagement for that review pursuant to subparagraph (B). ; and\n**(2)**\nby adding at the end the following:\n(7) Regional discount factors for soybeans (A) Definition of covered declaration In this paragraph, the term covered declaration means\u2014 (i) a disaster declaration by the Secretary; (ii) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ); or (iii) an emergency declared by the President under section 501 of that Act ( 42 U.S.C. 5191 ). (B) Discount factor In the event of a covered declaration for a State or region, or the occurrence of a salvage market for soybeans in a State or region, the Corporation shall establish a State or regional discount factor, as applicable, to reflect the average quality discounts applied to the local or regional market prices of the soybean crop. (C) Reporting requirement Any State or regional discount factor established under subparagraph (B) shall be included in\u2014 (i) the applicable periodic review conducted under paragraph (3)(A); and (ii) the report described in paragraph (3)(D). .",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1117",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Quality Loss Adjustment Improvement for Farmers Act",
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
        "updateDate": "2025-02-19T16:49:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr442",
          "measure-number": "442",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr442v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Quality Loss Adjustment Improvement for Farmers Act</strong></p><p>This bill directs the\u00a0Federal Crop Insurance Corporation (FCIC) to review and revise quality loss adjustment coverage\u00a0and provides for the establishment of a regional discount factor for soybeans, as needed.</p><p>The FCIC is a government corporation that\u00a0finances and administers the federal crop insurance program (FCIP) operations. Under the FCIP, farmers may\u00a0purchase insurance coverage against financial losses\u00a0caused by certain adverse growing and market conditions,\u00a0including for quality losses. The federal government subsidizes the premiums that farmers pay for these insurance policies.\u00a0</p><p>The bill directs the FCIC to contract with a qualified entity to conduct a review at least once every five years\u00a0of the quality loss adjustment procedures. Based on each review, the FCIC must make adjustments to the procedures. Each review must include engagement from regionally diverse industry stakeholders for each agricultural commodity for which a quality loss adjustment is offered.</p><p>The bill also directs the\u00a0FCIC, in certain circumstances, to establish a\u00a0state or regional discount factor for soybeans to reflect the average quality discounts applied to the local or regional market prices of the soybean crop. The FCIC must take this action\u00a0in the event of (1) specific emergency or disaster declarations for a state or region, or (2) the occurrence of a salvage market for soybeans in a state or region.</p>"
        },
        "title": "Quality Loss Adjustment Improvement for Farmers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr442.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quality Loss Adjustment Improvement for Farmers Act</strong></p><p>This bill directs the\u00a0Federal Crop Insurance Corporation (FCIC) to review and revise quality loss adjustment coverage\u00a0and provides for the establishment of a regional discount factor for soybeans, as needed.</p><p>The FCIC is a government corporation that\u00a0finances and administers the federal crop insurance program (FCIP) operations. Under the FCIP, farmers may\u00a0purchase insurance coverage against financial losses\u00a0caused by certain adverse growing and market conditions,\u00a0including for quality losses. The federal government subsidizes the premiums that farmers pay for these insurance policies.\u00a0</p><p>The bill directs the FCIC to contract with a qualified entity to conduct a review at least once every five years\u00a0of the quality loss adjustment procedures. Based on each review, the FCIC must make adjustments to the procedures. Each review must include engagement from regionally diverse industry stakeholders for each agricultural commodity for which a quality loss adjustment is offered.</p><p>The bill also directs the\u00a0FCIC, in certain circumstances, to establish a\u00a0state or regional discount factor for soybeans to reflect the average quality discounts applied to the local or regional market prices of the soybean crop. The FCIC must take this action\u00a0in the event of (1) specific emergency or disaster declarations for a state or region, or (2) the occurrence of a salvage market for soybeans in a state or region.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr442"
    },
    "title": "Quality Loss Adjustment Improvement for Farmers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quality Loss Adjustment Improvement for Farmers Act</strong></p><p>This bill directs the\u00a0Federal Crop Insurance Corporation (FCIC) to review and revise quality loss adjustment coverage\u00a0and provides for the establishment of a regional discount factor for soybeans, as needed.</p><p>The FCIC is a government corporation that\u00a0finances and administers the federal crop insurance program (FCIP) operations. Under the FCIP, farmers may\u00a0purchase insurance coverage against financial losses\u00a0caused by certain adverse growing and market conditions,\u00a0including for quality losses. The federal government subsidizes the premiums that farmers pay for these insurance policies.\u00a0</p><p>The bill directs the FCIC to contract with a qualified entity to conduct a review at least once every five years\u00a0of the quality loss adjustment procedures. Based on each review, the FCIC must make adjustments to the procedures. Each review must include engagement from regionally diverse industry stakeholders for each agricultural commodity for which a quality loss adjustment is offered.</p><p>The bill also directs the\u00a0FCIC, in certain circumstances, to establish a\u00a0state or regional discount factor for soybeans to reflect the average quality discounts applied to the local or regional market prices of the soybean crop. The FCIC must take this action\u00a0in the event of (1) specific emergency or disaster declarations for a state or region, or (2) the occurrence of a salvage market for soybeans in a state or region.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr442"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr442ih.xml"
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
      "title": "Quality Loss Adjustment Improvement for Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quality Loss Adjustment Improvement for Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to modify a provision relating to quality loss adjustment coverage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T06:48:20Z"
    }
  ]
}
```
