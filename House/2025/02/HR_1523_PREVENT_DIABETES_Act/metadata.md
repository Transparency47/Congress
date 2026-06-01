# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1523?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1523
- Title: PREVENT DIABETES Act
- Congress: 119
- Bill type: HR
- Bill number: 1523
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-03-06T19:06:18Z
- Update date including text: 2026-03-06T19:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1523",
    "number": "1523",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "PREVENT DIABETES Act",
    "type": "HR",
    "updateDate": "2026-03-06T19:06:18Z",
    "updateDateIncludingText": "2026-03-06T19:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:04:30Z",
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
          "date": "2025-02-24T17:04:25Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CO"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "WA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "IA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1523ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1523\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Ms. DeGette (for herself, Mr. Bilirakis , Mr. Crow , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the inclusion of virtual diabetes prevention program suppliers in the Medicare Diabetes Prevention Program Expanded Model, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Responsible and Effective Virtual Experiences through Novel Technology to Deliver Improved Access and Better Engagement with Tested and Evidence-based Strategies Act or the PREVENT DIABETES Act .\n#### 2. Inclusion of virtual diabetes prevention program suppliers in MDPP Expanded Model\n##### (a) In general\nNot later than January 1, 2026, the Secretary shall revise the regulations under parts 410 and 424 of title 42, Code of Federal Regulations, to provide that, for the period beginning January 1, 2026, and ending December 31, 2030\u2014\n**(1)**\nan entity may participate in the MDPP by offering only online MDPP services via synchronous or asynchronous technology or telecommunications if such entity meets the conditions for enrollment as an MDPP supplier (as specified in section 424.205(b) of title 42, Code of Federal Regulations (or a successor regulation));\n**(2)**\nif an entity participates in the MDPP in the manner described in paragraph (1) \u2014\n**(A)**\nthe administrative location of such entity shall be the address of the entity on file under the Diabetes Prevention Recognition Program; and\n**(B)**\nin the case of online MDPP services furnished by such entity to an MDPP beneficiary who was not located in the same State as the entity at the time such services were furnished, the entity shall not be prohibited from submitting a claim for payment for such services solely by reason of the location of such beneficiary at such time; and\n**(3)**\nno limit is applied on the number of times an individual may enroll in the MDPP.\n##### (b) Definitions\nIn this section:\n**(1) MDPP**\nThe term MDPP means the Medicare Diabetes Prevention Program conducted under section 1115A of the Social Security Act ( 42 U.S.C. 1315a ), as described in the final rule published in the Federal Register entitled Medicare and Medicaid Programs; CY 2024 Payment Policies Under the Physician Fee Schedule and Other Changes to Part B Payment and Coverage Policies; Medicare Shared Savings Program Requirements; Medicare Advantage; Medicare and Medicaid Provider and Supplier Enrollment Policies; and Basic Health Program (88 Fed. Reg. 78818 (November 16, 2023)) (or a successor regulation).\n**(2) Regulatory terms**\nThe terms Diabetes Prevention Recognition Program , full CDC DPRP recognition , MDPP beneficiary , MDPP services , and MDPP supplier have the meanings given each such term in section 410.79(b) of title 42, Code of Federal Regulations.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-02-24",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-21",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2263",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Telehealth Coverage Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-17T19:04:48Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-07-17T19:04:24Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-07-17T19:04:56Z"
          },
          {
            "name": "Digestive and metabolic diseases",
            "updateDate": "2025-07-17T19:04:05Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-17T19:04:16Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-17T19:05:02Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-07-17T19:04:32Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-17T19:03:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T14:37:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1523",
          "measure-number": "1523",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-08-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1523v00",
            "update-date": "2025-08-11"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Promoting Responsible and Effective Virtual Experiences through Novel Technology to Deliver Improved Access and Better Engagement with Tested and Evidence-based Strategies Act or the PREVENT DIABETES Act</strong></p><p>This bill\u00a0allows health care entities to provide virtual services under the Medicare Diabetes Prevention Program for an additional three years.</p><p>The Medicare Diabetes Prevention Program\u00a0offers Medicare beneficiaries who are at risk of developing Type 2 diabetes specialized training and education regarding diet, exercise, and other behavioral changes. The Centers for Medicare & Medicaid Services issued temporary authorization for entities participating in the program to provide these services virtually until December 31, 2027.</p><p>The bill extends the authorization for virtual services until December 31, 2030.</p>"
        },
        "title": "PREVENT DIABETES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1523.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Responsible and Effective Virtual Experiences through Novel Technology to Deliver Improved Access and Better Engagement with Tested and Evidence-based Strategies Act or the PREVENT DIABETES Act</strong></p><p>This bill\u00a0allows health care entities to provide virtual services under the Medicare Diabetes Prevention Program for an additional three years.</p><p>The Medicare Diabetes Prevention Program\u00a0offers Medicare beneficiaries who are at risk of developing Type 2 diabetes specialized training and education regarding diet, exercise, and other behavioral changes. The Centers for Medicare & Medicaid Services issued temporary authorization for entities participating in the program to provide these services virtually until December 31, 2027.</p><p>The bill extends the authorization for virtual services until December 31, 2030.</p>",
      "updateDate": "2025-08-11",
      "versionCode": "id119hr1523"
    },
    "title": "PREVENT DIABETES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Responsible and Effective Virtual Experiences through Novel Technology to Deliver Improved Access and Better Engagement with Tested and Evidence-based Strategies Act or the PREVENT DIABETES Act</strong></p><p>This bill\u00a0allows health care entities to provide virtual services under the Medicare Diabetes Prevention Program for an additional three years.</p><p>The Medicare Diabetes Prevention Program\u00a0offers Medicare beneficiaries who are at risk of developing Type 2 diabetes specialized training and education regarding diet, exercise, and other behavioral changes. The Centers for Medicare & Medicaid Services issued temporary authorization for entities participating in the program to provide these services virtually until December 31, 2027.</p><p>The bill extends the authorization for virtual services until December 31, 2030.</p>",
      "updateDate": "2025-08-11",
      "versionCode": "id119hr1523"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1523ih.xml"
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
      "title": "PREVENT DIABETES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PREVENT DIABETES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Responsible and Effective Virtual Experiences through Novel Technology to Deliver Improved Access and Better Engagement with Tested and Evidence-based Strategies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the inclusion of virtual diabetes prevention program suppliers in the Medicare Diabetes Prevention Program Expanded Model, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:37Z"
    }
  ]
}
```
