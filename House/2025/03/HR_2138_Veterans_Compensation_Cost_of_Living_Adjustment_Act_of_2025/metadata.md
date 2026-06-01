# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2138?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2138
- Title: Veterans’ Compensation Cost-of-Living Adjustment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2138
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-18T05:08:09Z
- Update date including text: 2026-05-18T05:08:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2138",
    "number": "2138",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-18T05:08:09Z",
    "updateDateIncludingText": "2026-05-18T05:08:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-03-26T17:46:26Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-26T17:46:22Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "KY"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CO"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2138ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2138\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Luttrell (for himself, Mr. McGarvey , Mr. Weber of Texas , and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo increase, effective as of December 1, 2025, the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025 .\n#### 2. Increase in rates of disability compensation and dependency and indemnity compensation\n##### (a) Rate adjustment\nEffective on December 1, 2025, the Secretary of Veterans Affairs shall increase, in accordance with subsection (c), the dollar amounts in effect on November 30, 2025, for the payment of disability compensation and dependency and indemnity compensation under the provisions specified in subsection (b).\n##### (b) Amounts To be increased\nThe dollar amounts to be increased pursuant to subsection (a) are the following:\n**(1) Wartime disability compensation**\nEach of the dollar amounts under section 1114 of title 38, United States Code.\n**(2) Additional compensation for dependents**\nEach of the dollar amounts under section 1115(1) of such title.\n**(3) Clothing allowance**\nThe dollar amount under section 1162 of such title.\n**(4) Dependency and indemnity compensation to surviving spouse**\nEach of the dollar amounts under subsections (a) through (d) of section 1311 of such title.\n**(5) Dependency and indemnity compensation to children**\nEach of the dollar amounts under sections 1313(a) and 1314 of such title.\n##### (c) Determination of Increase\nEach dollar amount described in subsection (b) shall be increased by the same percentage as the percentage by which benefit amounts payable under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) are increased effective December 1, 2025, as a result of a determination under section 215(i) of such Act ( 42 U.S.C. 415(i) ).\n##### (d) Special rule\nThe Secretary of Veterans Affairs may adjust administratively, consistent with the increases made under subsection (a), the rates of disability compensation payable to persons under section 10 of Public Law 85\u2013857 (72 Stat. 1263) who have not received compensation under chapter 11 of title 38, United States Code.\n#### 3. Publication of adjusted rates\nThe Secretary of Veterans Affairs shall publish in the Federal Register the amounts specified in section 2(b), as increased under that section, not later than the date on which the matters specified in section 215(i)(2)(D) of the Social Security Act ( 42 U.S.C. 415(i)(2)(D) ) are required to be published by reason of a determination made under section 215(i) of such Act during fiscal year 2026.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2026-04-28",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "8552",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-11",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "4487",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-25",
        "text": "Became Public Law No: 119-42."
      },
      "number": "2392",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-13T14:29:19Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-05-13T14:29:19Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-05-13T14:29:19Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-05-13T14:29:19Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-05-13T14:29:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T14:20:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2138",
          "measure-number": "2138",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2138v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans' Compensation Cost-of-Living Adjustment Act of 2025</strong><strong></strong></p><p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children. Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1, 2025. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>"
        },
        "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2138.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans' Compensation Cost-of-Living Adjustment Act of 2025</strong><strong></strong></p><p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children. Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1, 2025. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2138"
    },
    "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans' Compensation Cost-of-Living Adjustment Act of 2025</strong><strong></strong></p><p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children. Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1, 2025. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2138"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2138ih.xml"
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
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase, effective as of December 1, 2025, the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:33:45Z"
    }
  ]
}
```
