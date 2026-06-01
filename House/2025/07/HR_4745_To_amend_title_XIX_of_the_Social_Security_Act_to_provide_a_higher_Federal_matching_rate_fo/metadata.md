# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4745
- Title: Medicaid Bump Act
- Congress: 119
- Bill type: HR
- Bill number: 4745
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-12T08:05:52Z
- Update date including text: 2026-05-12T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4745",
    "number": "4745",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Medicaid Bump Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:52Z",
    "updateDateIncludingText": "2026-05-12T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:00:35Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4745ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4745\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Tonko (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to provide a higher Federal matching rate for increased expenditures under Medicaid for behavioral health services (including those related to mental health and substance use), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medicaid Bump Act .\n#### 2. Higher Federal match for increased expenditures under Medicaid for behavioral health services\n##### (a) In general\nSection 1903 of the Social Security Act ( 42 U.S.C. 1396b ) is amended\u2014\n**(1)**\nin subsection (a)(5)\u2014\n**(A)**\nby striking an amount equal and inserting (A) an amount equal ; and\n**(B)**\nby adding at the end the following:\nand (B) subject to subsection (b)(6), an amount equal to 90 percent of the amount by which\u2014 (i) the sum of the amounts expended during such quarter which are attributable to the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or under a waiver of the plan) of behavioral health services (including those related to mental health and substance use), exceeds (ii) the sum of the amounts expended during the corresponding quarter in the 4-quarter period ending on March 31, 2019, which are attributable to the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or under a waiver of the plan) of such services, plus ; and\n**(2)**\nin subsection (b), by adding at the end the following new paragraph:\n(6) Accountability and maintenance of effort requirements for additional federal funding for increased expenditures for behavioral health services As a condition for receiving the funds the Secretary is otherwise obligated to pay to a State under subsection (a)(5)(B), a State shall meet the following requirements: (A) Supplement, not supplant The State shall use the funds received under such subsection to supplement, not supplant, the level of State funds expended for the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or under a waiver of the plan) of behavioral health services (including those related to mental health and substance use) through programs and activities in effect as of April 1, 2021. (B) Use of funds for activities that improve delivery of behavioral health services The State shall use the funds received under such subsection for activities that increase the capacity, efficiency, and quality in the provision of behavioral health services (including those related to mental health and substance use) delivered by providers, including through increases in payment rates for providers of those services and the adoption of other measures that ensure a reduction in staff turnover. .\n##### (b) Sub-Regulatory guidance\nNot later than 180 days after the date of enactment of this Act, the Secretary of Health and Human Services shall issue sub-regulatory guidance to States specifying the services that are behavioral health services for purposes of subparagraph (B) of section 1903(a)(5) of the Social Security Act ( 42 U.S.C. 1396b(a)(5) ), as added by subsection (a).\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to calendar quarters beginning on or after January 1 of the year beginning 1 year after the date of the enactment of this Act.\n#### 3. Report regarding behavioral health service\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary of Health and Human Services shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Finance of the Senate a report regarding behavioral health services (including those related to mental health and substance use) provided under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) in each State, specifying the payment rates for such services, the rationale for deriving such payment rates, and utilization of such services, as such data are available.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2410",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medicaid Bump Act",
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
        "updateDate": "2025-09-16T17:38:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hr4745",
          "measure-number": "4745",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4745v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Medicaid Bump Act</b></p> <p>This bill increases the Medicaid federal matching rate, also known as the Federal Medical Assistance Percentage (FMAP), for behavioral health expenses that exceed prior levels (i.e., as of March 31, 2019). The Centers for Medicare & Medicaid Services must specify which services are eligible for the increased FMAP. States must use funds to supplement state funding for programs in effect as of April 1, 2021, and to increase the capacity, efficiency, and quality of services.</p>"
        },
        "title": "Medicaid Bump Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4745.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicaid Bump Act</b></p> <p>This bill increases the Medicaid federal matching rate, also known as the Federal Medical Assistance Percentage (FMAP), for behavioral health expenses that exceed prior levels (i.e., as of March 31, 2019). The Centers for Medicare & Medicaid Services must specify which services are eligible for the increased FMAP. States must use funds to supplement state funding for programs in effect as of April 1, 2021, and to increase the capacity, efficiency, and quality of services.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4745"
    },
    "title": "Medicaid Bump Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicaid Bump Act</b></p> <p>This bill increases the Medicaid federal matching rate, also known as the Federal Medical Assistance Percentage (FMAP), for behavioral health expenses that exceed prior levels (i.e., as of March 31, 2019). The Centers for Medicare & Medicaid Services must specify which services are eligible for the increased FMAP. States must use funds to supplement state funding for programs in effect as of April 1, 2021, and to increase the capacity, efficiency, and quality of services.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4745"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4745ih.xml"
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
      "title": "Medicaid Bump Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Bump Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to provide a higher Federal matching rate for increased expenditures under Medicaid for behavioral health services (including those related to mental health and substance use), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:38Z"
    }
  ]
}
```
