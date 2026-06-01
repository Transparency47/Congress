# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/660
- Title: WISER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 660
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-08-23T08:05:27Z
- Update date including text: 2025-08-23T08:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/660",
    "number": "660",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "WISER Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-23T08:05:27Z",
    "updateDateIncludingText": "2025-08-23T08:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-01-23",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T22:41:06Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-23T15:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
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
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr660ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 660\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Brownley (for herself, Ms. Houlahan , Mr. Gottheimer , and Ms. Omar ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Veterans Affairs and the Secretary of Defense to carry out programs to provide to certain veterans who are women a compensation benefit and an upgrade to the discharge status of such veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Women Involuntarily Separated Earning Remittance Act of 2025 or the WISER Act of 2025 .\n#### 2. Programs to provide compensation benefit and discharge status upgrades for certain veterans who are women discharged pursuant to Executive Order 10240\n##### (a) Discharge status upgrade program\n**(1) In general**\nSubject to the availability of amounts made available in advance in appropriations Acts, the Secretary of Veterans Affairs, in coordination with the Secretary of Defense, shall establish and carry out a program to, subject to the eligibility criteria under subsection (c) and conditions to be prescribed by the Secretary of Defense, upgrade the discharge status of covered veterans.\n**(2) Applications**\nA covered veteran desiring to participate in such program shall submit to the Secretary of Veterans Affairs and the Secretary of Defense an application in such form, at such time, and containing such information and assurances as such Secretaries determine appropriate.\n**(3) Treatment of certain covered veterans**\nWith respect to the provision of benefits under the laws administered by the Secretary of Veterans Affairs, such Secretary shall treat a covered veteran who receives a discharge status upgrade pursuant to such program as if such covered veteran completed the duty to which such covered veteran was assigned at the time such covered veteran was separated from active military, naval, air, or space service.\n##### (b) Compensation benefit program\n**(1) In general**\nThe Secretary of Defense shall establish and carry out a program to provide to covered veterans, subject to the eligibility criteria under subsection (c) and paragraph (2), a one-time compensation benefit in the amount of $25,000.\n**(2) Surviving spouse eligibility**\nIf a covered veteran who satisfies the eligibility criteria under subsection (c) dies after the date of the enactment of this Act, the surviving spouse of such covered veteran shall be eligible for participation in the program under paragraph (1).\n**(3) Applications**\nA covered veteran, or the surviving spouse of a covered veteran, desiring to participate in such program shall submit to the Secretary of Defense an application in such form, at such time, and containing such information and assurances as the Secretary determines appropriate.\n**(4) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary of Defense such sums as may be necessary to carry out this subsection.\n##### (c) Eligibility criteria\n**(1) Irrebuttable presumption**\nThere is an irrebuttable presumption of eligibility for participation in the programs under subsections (a) and (b) for a covered veteran who was involuntarily separated from active military, naval, air, or space service pursuant to Executive Order 10240.\n**(2) Rebuttable presumptions**\nThere is a rebuttable presumption for eligibility for participation in such programs for a covered veteran who\u2014\n**(A)**\ngave birth to a child, obtained legal or physical custody of a child, or adopted a child during the 10-month period beginning after the date the veteran was separated from active military, naval, air, or space service; or\n**(B)**\nexperienced an incomplete pregnancy (including due to an abortion or miscarriage) during such 10-month period.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term active military, naval, air, or space service has the meaning given such term in section 101 of title 10, United States Code.\n**(2)**\nThe term covered veteran means a veteran who\u2014\n**(A)**\nis a woman; and\n**(B)**\nperformed active military, naval, air, or space service during the period beginning on April 27, 1951 and ending on February 23, 1976.",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-17T16:15:18Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2025-03-17T16:15:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:46:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr660",
          "measure-number": "660",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr660v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Women Involuntarily Separated Earning Remittance Act of 2025 or the WISER Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and the Department of Defense (DOD) to establish and implement certain programs to address the involuntary separation of women veterans who served during the period of April 27, 1951, through February 23, 1976, under Executive Order 10240. Such order provided for the involuntary separation of women from service for (1) being a parent via birth or adoption, (2) gaining custody of a child, (3) being a step-parent who lived with the child more than 30 days per year, (4) being pregnant, or (5) giving birth to a living child while serving.</p><p>The VA must establish and implement a program to upgrade the discharge status of such women veterans, and DOD must establish and implement a program to provide them with a one-time compensation of $25,000. Veterans must apply to participate in such programs.</p><p>For benefits purposes, the VA must treat veterans who receive a discharge status upgrade as if the veteran completed the duty to which the veteran was assigned at the time they were discharged from service.</p><p>If a veteran dies after the enactment of this bill, a surviving spouse is eligible to participate in the DOD compensation program.</p><p>The bill provides a rebuttable presumption of eligibility for the programs for a veteran who gave birth, obtained custody, adopted a child, or experienced an incomplete pregnancy during the 10-month period after the veteran was separated from service.</p>"
        },
        "title": "WISER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr660.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women Involuntarily Separated Earning Remittance Act of 2025 or the WISER Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and the Department of Defense (DOD) to establish and implement certain programs to address the involuntary separation of women veterans who served during the period of April 27, 1951, through February 23, 1976, under Executive Order 10240. Such order provided for the involuntary separation of women from service for (1) being a parent via birth or adoption, (2) gaining custody of a child, (3) being a step-parent who lived with the child more than 30 days per year, (4) being pregnant, or (5) giving birth to a living child while serving.</p><p>The VA must establish and implement a program to upgrade the discharge status of such women veterans, and DOD must establish and implement a program to provide them with a one-time compensation of $25,000. Veterans must apply to participate in such programs.</p><p>For benefits purposes, the VA must treat veterans who receive a discharge status upgrade as if the veteran completed the duty to which the veteran was assigned at the time they were discharged from service.</p><p>If a veteran dies after the enactment of this bill, a surviving spouse is eligible to participate in the DOD compensation program.</p><p>The bill provides a rebuttable presumption of eligibility for the programs for a veteran who gave birth, obtained custody, adopted a child, or experienced an incomplete pregnancy during the 10-month period after the veteran was separated from service.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr660"
    },
    "title": "WISER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women Involuntarily Separated Earning Remittance Act of 2025 or the WISER Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and the Department of Defense (DOD) to establish and implement certain programs to address the involuntary separation of women veterans who served during the period of April 27, 1951, through February 23, 1976, under Executive Order 10240. Such order provided for the involuntary separation of women from service for (1) being a parent via birth or adoption, (2) gaining custody of a child, (3) being a step-parent who lived with the child more than 30 days per year, (4) being pregnant, or (5) giving birth to a living child while serving.</p><p>The VA must establish and implement a program to upgrade the discharge status of such women veterans, and DOD must establish and implement a program to provide them with a one-time compensation of $25,000. Veterans must apply to participate in such programs.</p><p>For benefits purposes, the VA must treat veterans who receive a discharge status upgrade as if the veteran completed the duty to which the veteran was assigned at the time they were discharged from service.</p><p>If a veteran dies after the enactment of this bill, a surviving spouse is eligible to participate in the DOD compensation program.</p><p>The bill provides a rebuttable presumption of eligibility for the programs for a veteran who gave birth, obtained custody, adopted a child, or experienced an incomplete pregnancy during the 10-month period after the veteran was separated from service.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr660"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr660ih.xml"
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
      "title": "WISER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:56Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WISER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Women Involuntarily Separated Earning Remittance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs and the Secretary of Defense to carry out programs to provide to certain veterans who are women a compensation benefit and an upgrade to the discharge status of such veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:10Z"
    }
  ]
}
```
