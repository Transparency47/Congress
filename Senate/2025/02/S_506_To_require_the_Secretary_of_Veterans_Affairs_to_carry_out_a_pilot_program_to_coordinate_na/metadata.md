# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/506?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/506
- Title: Coordinating Care for Senior Veterans and Wounded Warriors Act
- Congress: 119
- Bill type: S
- Bill number: 506
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/506",
    "number": "506",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-07-30T20:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-11T15:53:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s506is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 506\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Moran (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to carry out a pilot program to coordinate, navigate, and manage care and benefits for veterans enrolled in both the Medicare program and the system of annual patient enrollment of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Coordinating Care for Senior Veterans and Wounded Warriors Act .\n#### 2. Pilot program on coordination of care between Department of Veterans Affairs and Medicare program\n##### (a) In general\nThe Secretary, in consultation with the Secretary of Health and Human Services, shall carry out a pilot program (in this section referred to as the pilot program ) to coordinate, navigate, and manage care and benefits for covered veterans.\n##### (b) Purposes of pilot program\nThe purposes of the pilot program are as follows:\n**(1)**\nTo improve access to health care services for covered veterans at medical facilities of the Department of Veterans Affairs, from health care providers under the Veterans Community Care Program under section 1703 of title 38, United States Code, from health care providers with which the Department has established a Veterans Care Agreement under section 1703A of such title, and from health care providers participating in the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(2)**\nTo improve outcomes of care received by covered veterans.\n**(3)**\nTo improve quality of care received by covered veterans.\n**(4)**\nTo lower costs of care received by covered veterans.\n**(5)**\nTo eliminate gaps in care and duplication of services and expenses for covered veterans.\n**(6)**\nTo improve care coordination for covered veterans, including coordination of patient information and medical records between providers.\n##### (c) Administration\n**(1) In general**\nThe Secretary shall carry out the pilot program through the Center for Innovation for Care and Payment of the Department of Veterans Affairs.\n**(2) Locations**\nThe Secretary shall carry out the pilot program in not less than three but not more than five Veterans Integrated Service Networks with a large number of covered veterans and varying degrees of urbanization, including\u2014\n**(A)**\nlocations that are in rural or highly rural areas, as determined through the use of the Rural-Urban Commuting Areas coding system of the Department of Agriculture; and\n**(B)**\nlocations that are medically underserved.\n##### (d) Case manager\n**(1) Assignment of case manager**\nIn carrying out the pilot program, the Secretary shall assign each covered veteran participating in the pilot program a case manager responsible for developing an individualized needs assessment for such veteran and, based on such assessment, a care coordination plan with defined treatment goals.\n**(2) Accessing services**\nA case manager assigned to a covered veteran under paragraph (1) is responsible for assisting such veteran in accessing services needed by such veteran and navigating the systems of care under the laws administered by the Secretary and under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n##### (e) Use of existing models\nIn designing the pilot program, the Secretary shall, to the extent practicable, use existing models, including value-based care models, used by commercial health care programs to improve access, health outcomes, quality, and customer experience and lower per capita costs.\n##### (f) Contracting with private sector entities\n**(1) In general**\nThe Secretary shall, to the greatest extent practicable, contract with private sector entities carrying out commercial health care programs for assistance in designing, implementing, and managing care and benefits under the pilot program, to include providing care coordination.\n**(2) Notification**\nIf the Secretary determines that contracting with private sector entities under paragraph (1) is not practicable, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives\u2014\n**(A)**\na notification of that determination;\n**(B)**\na description of the steps the Secretary has taken to contract with a private sector entity;\n**(C)**\na justification for why the Secretary has determined that contracting with a private sector entity is not practicable; and\n**(D)**\na plan for how the Secretary will carry out the pilot program without contracting with a private sector entity, including through the use of employees of the Department of Veterans Affairs or other government agencies, nonprofit organizations, or other entities.\n##### (g) Metrics\n**(1) In general**\nThe Secretary shall track metrics under the pilot program, including the following:\n**(A)**\nThe number of veterans participating in the pilot program, disaggregated by Veterans Integrated Service Network.\n**(B)**\nReliance on health care services administered by the Secretary.\n**(C)**\nReliance on health care services administered under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(D)**\nQuality of care, including patient outcomes.\n**(E)**\nCost of care.\n**(F)**\nAccess to care, including under the designated access standards developed by the Secretary under section 1703B of title 38, United States Code.\n**(G)**\nPatient satisfaction.\n**(H)**\nProvider satisfaction.\n**(I)**\nCare coordination, including timely information sharing and medical documentation return.\n**(2) Elements**\nIn tracking metrics under paragraph (1), the Secretary shall track information relating to\u2014\n**(A)**\nwhether care received by a covered veteran is related to a service-connected disability (as defined in section 101 of title 38, United States Code);\n**(B)**\nthe priority group under section 1705(a) of title 38, United States Code, through which each covered veteran was enrolled in the system of annual patient enrollment of the Department of Veterans Affairs under such section;\n**(C)**\nthe type of care and services provided to covered veterans; and\n**(D)**\nthe demographics of covered veterans participating in the pilot program, including age.\n##### (h) Duration\nThe Secretary shall carry out the pilot program for a three-year period beginning on the commencement of the pilot program.\n##### (i) Reports\n**(1) Development, implementation, results, and design of pilot program**\n**(A) In general**\nNot less frequently than quarterly during the two-year period beginning on the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the development, implementation, results, and design of the pilot program, including information on the metrics tracked under subsection (g).\n**(B) Final design**\nOne of the reports required under subparagraph (A) shall contain a description of the final design of the pilot program.\n**(2) Results of pilot program**\nNot later than one year after the submission of the final report under paragraph (1), and not less frequently than annually thereafter during the duration of the pilot program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the results of the pilot program.\n**(3) Final report**\nNot later than 180 days before the termination of the pilot program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a final report on the pilot program, which shall include the recommendation of the Secretary for whether the pilot program should be extended or made permanent.\n##### (j) Definitions\nIn this section:\n**(1) Covered veteran**\nThe term covered veteran means a veteran who is enrolled in both the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) and the system of annual patient enrollment of the Department of Veterans Affairs under section 1705(a) of title 38, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Veterans Affairs.",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-04",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "668",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-17T17:42:27Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-17T17:42:27Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-17T17:42:27Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-03-17T17:42:27Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-17T17:42:27Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-17T17:42:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T15:56:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
    "originChamber": "Senate",
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
          "measure-id": "id119s506",
          "measure-number": "506",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s506v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Coordinating Care for Senior Veterans and Wounded Warriors Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program to coordinate, navigate, and manage care and benefits for veterans who are enrolled in both the Medicare program and the VA health care system.</p>"
        },
        "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s506.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Coordinating Care for Senior Veterans and Wounded Warriors Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program to coordinate, navigate, and manage care and benefits for veterans who are enrolled in both the Medicare program and the VA health care system.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s506"
    },
    "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Coordinating Care for Senior Veterans and Wounded Warriors Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program to coordinate, navigate, and manage care and benefits for veterans who are enrolled in both the Medicare program and the VA health care system.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s506"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s506is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Coordinating Care for Senior Veterans and Wounded Warriors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to carry out a pilot program to coordinate, navigate, and manage care and benefits for veterans enrolled in both the Medicare program and the system of annual patient enrollment of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:46Z"
    }
  ]
}
```
