# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2554
- Title: Lower Drug Costs for Families Act
- Congress: 119
- Bill type: HR
- Bill number: 2554
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-01-10T07:01:47Z
- Update date including text: 2026-01-10T07:01:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2554",
    "number": "2554",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Lower Drug Costs for Families Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:01:47Z",
    "updateDateIncludingText": "2026-01-10T07:01:47Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-04-01T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-01T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2554ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2554\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Horsford (for himself, Mrs. Cherfilus-McCormick , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to apply prescription drug inflation rebates to drugs furnished in the commercial market and to change the base year for rebate calculations.\n#### 1. Short title\nThis Act may be cited as the Lower Drug Costs for Families Act .\n#### 2. Application of prescription drug inflation rebates to drugs furnished in the commercial market\n##### (a) Part B drugs\n**(1) Application of prescription drug inflation rebates to drugs furnished in the commercial market**\nSection 1847A(i) of the Social Security Act (42 U.S.C. 1395w\u20133a(i)) is amended\u2014\n**(A)**\nin paragraph (1)(A)(i), by striking units and inserting billing units ;\n**(B)**\nin paragraph (2)(A), by striking for which payment is made under this part and inserting that would be payable under this part if such drug were furnished to an individual enrolled under this part ;\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)(i), by striking units and inserting billing units ; and\n**(ii)**\nby striking subparagraph (B) and inserting the following:\n(B) Total number of billing units For purposes of subparagraph (A)(i), the total number of billing units with respect to a part B rebatable drug is determined as follows: (i) Determine the total number of units equal to\u2014 (I) the total number of units, as reported under subsection (c)(1)(B) for each National Drug Code of such drug during the calendar quarter that is two calendar quarters prior to the calendar quarter as described in subparagraph (A), minus (II) the total number of units with respect to each National Drug Code of such drug for which payment was made under a State plan under title XIX (or waiver of such plan), as reported by States under section 1927(b)(2)(A) for the rebate period that is the same calendar quarter as described in subclause (I). (ii) Convert the units determined under clause (i) to billing units for the billing and payment code of such drug, using a methodology similar to the methodology used under this section, by dividing the units determined under clause (i) for each National Drug Code of such drug by the billing unit for the billing and payment code of such drug. (iii) Compute the sum of the billing units for each National Drug Code of such drug in clause (ii). .\n**(2) Change of base year for rebate calculation**\nSection 1847A(i) of the Social Security Act (42 U.S.C. 1395w\u20133a(i)) is amended\u2014\n**(A)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (D), by striking July 1, 2021 and inserting July 1, 2016 ; and\n**(ii)**\nin subparagraph (E), by striking January 2021 and inserting January 2016 ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking December 1, 2020 and inserting December 31, 2015 ; and\n**(II)**\nby striking January 2021 and inserting January 2016 ;\n**(ii)**\nin subparagraph (B), by striking December 1, 2020 and inserting December 31, 2015 ; and\n**(iii)**\nin subparagraph (C), by striking January 2021 and inserting January 2016 .\n**(3) Effective date**\nThe amendments made by this subsection shall apply with respect to calendar quarters beginning on or after January 1, 2026.\n##### (b) Covered part D drugs\n**(1) Application of prescription drug inflation rebates to drugs furnished in the commercial market**\nSection 1860D\u201314B of the Social Security Act ( 42 U.S.C. 1395w\u2013114b ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (A)(i), by striking the total number of units and all that follows through the semicolon and inserting the following: the total number of units that are used to calculate the average manufacturer price of such dosage form and strength with respect to such part D rebatable drug, as reported by the manufacturer of such drug under section 1927 for each month, with respect to such period; ; and\n**(II)**\nby striking subparagraph (B) and inserting the following:\n(B) Excluded units For purposes of subparagraph (A)(i), the Secretary shall exclude from the total number of units for a dosage form and strength with respect to a part D rebatable drug, with respect to an applicable period, the following: (i) Units of each dosage form and strength of such part D rebatable drug for which payment was made under a State plan under title XIX (or waiver of such plan), as reported by States under section 1927(b)(2)(A). (ii) Units of each dosage form and strength of such part D rebatable drug for which a rebate is paid under section 1847A(i). (iii) Beginning with plan year 2026, units of each dosage form and strength of such part D rebatable drug for which the manufacturer provides a discount under the program under section 340B of the Public Health Service Act. ; and\n**(ii)**\nin paragraph (6), by striking information .\u2014The Secretary and all that follows through rebatable covered part D drug dispensed and inserting the following: AMP reports .\u2014The Secretary shall provide for a method and process under which, in the case of a manufacturer of a part D rebatable drug that submits revisions to information submitted under section 1927 by the manufacturer with respect to such drug ; and\n**(B)**\nby striking subsection (d) and inserting the following:\n(d) Information For purposes of carrying out this section, the Secretary shall use information submitted by manufacturers under section 1927(b)(3) and information submitted by States under section 1927(b)(2)(A). .\n**(2) Change of base year for rebate calculation**\nSection 1860D\u201314B of the Social Security Act ( 42 U.S.C. 1395w\u2013114b ) is amended\u2014\n**(A)**\nin subsection (b)(5)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking October 1, 2021 and inserting October 1, 2016 ; and\n**(II)**\nby striking January 2021 and inserting January 2016 ; and\n**(ii)**\nin subparagraph (C), by striking January 2021 and inserting January 2016 ; and\n**(B)**\nin subsection (g)\u2014\n**(i)**\nin paragraph (3)\u2014\n**(I)**\nby striking January 1, 2021 and inserting January 1, 2016 ; and\n**(II)**\nby striking October 1, 2021 and inserting October 1, 2016 ; and\n**(ii)**\nin paragraph (4), by striking January 2021 and inserting January 2016 .\n**(3) Effective date**\nThe amendments made by this subsection shall take apply with respect to applicable periods (as defined in section 1860D\u201314B(g)(7) of the Social Security Act (42 U.S.C. 1395w\u2013114b(g)(7))) beginning on or after October 1, 2025.",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1186",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Drug Costs for Families Act",
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
        "name": "Health",
        "updateDate": "2025-04-06T14:21:03Z"
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
          "measure-id": "id119hr2554",
          "measure-number": "2554",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2554v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>"
        },
        "title": "Lower Drug Costs for Families Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2554.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr2554"
    },
    "title": "Lower Drug Costs for Families Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Lower Drug Costs for Families Act</b></p> <p>This bill applies certain Medicare prescription drug rebate requirements to prescription drugs that are available under private health insurance.</p> <p>Current law requires drug manufacturers to issue rebates to the Centers for Medicare & Medicaid Services for brand-name drugs without generic equivalents under Medicare that (1) cost $100 or more per year per individual, and (2) for which prices increase faster than inflation. Manufacturers that fail to comply are subject to civil penalties.</p> <p>The bill applies these requirements to prescription drugs that are available in the commercial market under private health insurance. It also indexes rebate calculations to drug prices in 2016 (as opposed to 2021).</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr2554"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2554ih.xml"
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
      "title": "Lower Drug Costs for Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lower Drug Costs for Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to apply prescription drug inflation rebates to drugs furnished in the commercial market and to change the base year for rebate calculations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:57Z"
    }
  ]
}
```
