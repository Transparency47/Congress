# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/244?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/244
- Title: Veterans’ True Choice Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 244
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-02-25T09:06:17Z
- Update date including text: 2026-02-25T09:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/244",
    "number": "244",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veterans\u2019 True Choice Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:17Z",
    "updateDateIncludingText": "2026-02-25T09:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:35:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:37:04Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:35:30Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TN"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr244ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 244\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to provide eligibility for TRICARE Select to veterans with service-connected disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 True Choice Act of 2025 .\n#### 2. Eligibility for TRICARE for veterans with service-connected disabilities\n##### (a) In general\n**(1) Enrollment in TRICARE Select**\nSection 1075 of title 10, United States Code, is amended\u2014\n**(A)**\nin subsection (b)(1)(B), by inserting before the period at the end the following: , and covered veteran beneficiaries under subsection (h), other than Medicare-eligible beneficiaries described in such subsection (d)(2) ;\n**(B)**\nby redesignating subsections (h) and (i) as subsections (i) and (j), respectively; and\n**(C)**\nby inserting after subsection (g) the following new subsection:\n(h) Covered veteran beneficiaries (1) Subject to section 1086(d) of this title, a covered veteran beneficiary may elect to enroll in TRICARE Select during the annual open enrollment season of the TRICARE program. (2) The cost-sharing requirements under TRICARE Select for covered veteran beneficiaries shall be calculated pursuant to subsection (d)(1), regardless of the date of the original enlistment or appointment of the beneficiary in the uniformed services. (3) A dependent of a covered veteran beneficiary may not enroll in the TRICARE program solely by reason of the covered veteran beneficiary enrolling in the TRICARE program. .\n**(2) Enrollment in TRICARE for Life**\nSection 1086(d) of such title is amended\u2014\n**(A)**\nin paragraph (1), by inserting before the period at the end the following: or pursuant to section 1075(h) of this title ; and\n**(B)**\nin paragraphs (2) and (4), by inserting , or section 1075(h) of this title, after a person referred to in subsection (c) both places it appears.\n**(3) Definition**\nSection 1072 of such title is amended by adding at the end the following new paragraph:\n(16) The term covered veteran beneficiary means a veteran who\u2014 (A) is eligible to enroll in the system of patient enrollment under paragraph (1), (2), or (3) of section 1705 of title 38; and (B) is eligible to enroll in the TRICARE program only pursuant to\u2014 (i) section 1075(h) of this title; or (ii) section 1086(d) of this title by reason of being an individual who would be covered by section 1075(h) but for being a Medicare-eligible beneficiary covered by such section 1086(d). .\n**(4) Enrollment in VA health care**\nSection 1705 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) (1) A covered veteran beneficiary who enrolls in the TRICARE program may not be concurrently enrolled in the system of patient enrollment under subsection (a), and the Secretary may not furnish medical care to the covered veteran beneficiary under this chapter or other provision of law administered by the Secretary while the covered veteran beneficiary is so enrolled in the TRICARE program. (2) In this subsection, the terms covered veteran beneficiary and TRICARE program have the meaning given those terms in section 1072 of title 10. .\n##### (b) Memorandum of understanding\nThe Secretary of Veterans Affairs and the Secretary of Defense shall enter into a memorandum of understanding under which the Secretary of Veterans Affairs reimburses the Secretary of Defense for the costs of enrolling covered veteran beneficiaries in the TRICARE program pursuant to the amendments made by subsection (a), as jointly determined appropriate by the Secretaries.\n##### (c) Implementation\n**(1) Effective date**\nThe amendments made by this section shall take effect one year after the date of the enactment of this Act.\n**(2) Regulations**\nDuring the one-year period following the date on which the amendments made by this section take effect, the Secretary of Veterans Affairs and the Secretary of Defense shall each prescribe regulations to carry out such amendments.\n**(3) Phase in**\nDuring the one-year period following the date on which the regulations are prescribed under paragraph (2), the Secretaries shall phase in the enrollment of covered veteran beneficiaries in accordance with the annual open enrollment season of the TRICARE program.\n**(4) VA Center for Innovation for Care and Payment**\nThe Secretary of Veterans Affairs shall carry out this subsection through the Center for Innovation for Care and Payment of the Department of Veterans Affairs.\n##### (d) Reports\n**(1) Reports on implementation**\nOn a quarterly basis during the two-year period following the date of the enactment of this Act, the Secretary of Veterans Affairs and the Secretary of Defense shall jointly submit to the Committees on Veterans\u2019 Affairs and Armed Services of the Senate and the House of Representatives a report on the implementation of this Act and the amendments made by this Act.\n**(2) Annual reports**\nNot later than one year after the date on which the final report under paragraph (1) is required to be submitted, and annually thereafter, the Secretaries shall jointly submit to the Committees on Veterans\u2019 Affairs and Armed Services of the Senate and the House of Representatives a report on covered veteran beneficiaries enrolled in the TRICARE program.\n##### (e) Definitions\nIn this section, the terms covered veteran beneficiary and TRICARE program have the meaning given those terms in section 1072 of title 10, United States Code, as amended by subsection (a).",
      "versionDate": "2025-01-09",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-05T16:09:42Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-05T16:09:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:42:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr244",
          "measure-number": "244",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr244v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans' True Choice Act of 2025</strong></p><p>This bill allows covered veterans to receive coverage under TRICARE Select, a health care program of the Department of Defense (DOD). Veterans covered by this bill include those with service-connected disabilities, former prisoners of war, Purple Heart recipients, Medal of Honor recipients, those discharged from service due to disability, and those entitled to disability compensation.</p><p>The Department of Veterans Affairs (VA) must reimburse DOD's costs of enrolling eligible veteran beneficiaries in the program.</p><p>A covered veteran may not concurrently receive medical care from DOD and the VA.</p>"
        },
        "title": "Veterans\u2019 True Choice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr244.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans' True Choice Act of 2025</strong></p><p>This bill allows covered veterans to receive coverage under TRICARE Select, a health care program of the Department of Defense (DOD). Veterans covered by this bill include those with service-connected disabilities, former prisoners of war, Purple Heart recipients, Medal of Honor recipients, those discharged from service due to disability, and those entitled to disability compensation.</p><p>The Department of Veterans Affairs (VA) must reimburse DOD's costs of enrolling eligible veteran beneficiaries in the program.</p><p>A covered veteran may not concurrently receive medical care from DOD and the VA.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr244"
    },
    "title": "Veterans\u2019 True Choice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans' True Choice Act of 2025</strong></p><p>This bill allows covered veterans to receive coverage under TRICARE Select, a health care program of the Department of Defense (DOD). Veterans covered by this bill include those with service-connected disabilities, former prisoners of war, Purple Heart recipients, Medal of Honor recipients, those discharged from service due to disability, and those entitled to disability compensation.</p><p>The Department of Veterans Affairs (VA) must reimburse DOD's costs of enrolling eligible veteran beneficiaries in the program.</p><p>A covered veteran may not concurrently receive medical care from DOD and the VA.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr244"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr244ih.xml"
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
      "title": "Veterans\u2019 True Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T02:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 True Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to provide eligibility for TRICARE Select to veterans with service-connected disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T02:18:28Z"
    }
  ]
}
```
