# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/447?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/447
- Title: Reliability for Ratepayers Act
- Congress: 119
- Bill type: HR
- Bill number: 447
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-05-05T08:06:23Z
- Update date including text: 2026-05-05T08:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/447",
    "number": "447",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Reliability for Ratepayers Act",
    "type": "HR",
    "updateDate": "2026-05-05T08:06:23Z",
    "updateDateIncludingText": "2026-05-05T08:06:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-01-15T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr447ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 447\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Perez (for herself and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide compensation flexibility to address retention and hiring issues at the Bonneville Power Administration.\n#### 1. Short title\nThis Act may be cited as the Reliability for Ratepayers Act .\n#### 2. Compensation flexibility to address retention and hiring issues at the Bonneville Power Administration\nSection 10 of the Act of August 20, 1937 (commonly known as the Bonneville Project Act of 1937 ) (50 Stat. 736, chapter 720; 16 U.S.C. 832i ), is amended by striking the section designation and subsections (a) and (b) and inserting the following:\n10. Employment of personnel (a) Employee compensation program (1) In general Notwithstanding any other law, rule, regulation, or directive relating to the payment of Federal employees (other than chapter 83 of title 5, United States Code), the administrator shall develop, implement, and, as appropriate, update, based on the results of an annual review under paragraph (4), a compensation plan that specifies and fixes the compensation (including salary or any other pay, bonuses, benefits, incentives, and any other form of remuneration) for employees of the administrator, including members of the Senior Executive Service (as defined in section 2101a of title 5, United States Code). (2) Initial compensation plan (A) In general Not later than 1 year after the date of enactment of the Reliability for Ratepayers Act, the administrator shall, in consultation with the Director of the Office of Personnel Management, and subject to confirmation and approval by the Secretary of Energy, which shall not be unreasonably withheld, develop an initial compensation plan under paragraph (1). (B) Implementation Not later than 1 year after the date on which the initial compensation plan is developed under subparagraph (A), the administrator shall implement the initial compensation plan. (3) Requirements A compensation plan developed under paragraph (1) shall\u2014 (A) be based on an annual survey of the prevailing compensation for similar positions in the public sectors of the electric industry; (B) be consistent with the approved annual general and administrative budget of the administrator and encourage the widest diversified use of electric power at the lowest possible rates to consumers consistent with sound business principles; (C) provide that education, experience, level of responsibility, geographic differences, and retention and recruitment needs are to be taken into account in determining the compensation of employees of the administrator; and (D) provide that the individual total compensation of the administrator and any employee of the administrator shall be comparable to and competitive with similar positions among consumer-owned utilities in the Western Interconnection. (4) Annual review (A) In general Annually, the administrator shall review and update, as appropriate, the compensation plan developed under paragraph (1). (B) Compensation of the Administrator Notwithstanding any other law, rule, regulation, or directive relating to the payment of the administrator (other than chapter 83 of title 5, United States Code), the Secretary shall periodically review and update, as appropriate, the compensation of the administrator consistent with paragraph (3)(D). (C) Publication of information The administrator shall include in the quarterly public business review of the administrator or any other appropriate public review of the operations and finances of the administrator information on the applicable annual compensation plan review under subparagraph (A), including information on the amount of salaries of any employees whose annual salaries would exceed the annual rate payable for positions at Level IV of the Executive Schedule under section 5315 of title 5, United States Code. (5) Annual publication Annually, the administrator shall publish the compensation plan developed under paragraph (1) or updated under paragraph (4), as applicable. (b) Appointment; employment (1) In general The administrator may, as the administrator determines to be necessary to carry out this Act, subject to applicable civil service laws\u2014 (A) appoint any officers and employees; (B) employ laborers, mechanics, and workers for construction work or the operation and maintenance of electrical facilities; and (C) fix the compensation of individuals appointed under subparagraph (A) or (B), respectively, consistent with the applicable compensation plan developed under subsection (a)(1). (2) Exemption from certain civil service laws In carrying out the authority provided by paragraph (1), the administrator shall be exempt from chapters 34, 43, 51, 53, 57, and 59 of title 5, United States Code. (3) Application of merit system principles Employees of the administrator are subject to the application of the merit system principles set forth in section 2301 of title 5, United States Code, to the extent that the principles apply to a wholly owned Government corporation. (4) Employment of physicians The administrator may employ physicians, without regard to the civil service laws (including regulations), to perform physical examinations of employees of the administrator or prospective employees of the administrator who are or may become laborers, mechanics, and workers described in paragraph (1)(B). (5) Employment of experts The administrator may appoint, without regard to the civil service laws (including regulations), any experts that the administrator determines to be necessary to carry out the functions of the administrator under this Act. .",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-13T14:12:01Z"
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
          "measure-id": "id119hr447",
          "measure-number": "447",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr447v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reliability for Ratepayers Act</strong></p><p>This bill modifies provisions concerning the hiring and compensation of employees of the\u00a0Bonneville Power Administration (BPA), which is a nonprofit federal power marketing\u00a0administration that sells hydropower in the Northwest.</p><p>Specifically, it directs BPA\u00a0to develop and implement a\u00a0plan that specifies and fixes the compensation for its employees, including members of the Senior Executive Service. Within a year, BPA must develop an initial compensation plan, which must be approved by the Department of Energy. BPA must implement the plan no later than one year after the plan is developed. </p><p>The compensation plan must be based on an annual survey of the prevailing compensation for similar positions in the public sectors of the electric industry, provide compensation that is competitive with\u00a0similar positions among consumer-owned utilities in the Western Interconnection, be consistent with BPA's approved annual general and administrative budget, and meet other criteria as outlined in the bill.\u00a0</p><p>BPA must (1) annually review the compensation plan and make any updates as appropriate, and (2) publish the plan and any updates made to the plan.</p><p>The bill exempts\u00a0BPA\u00a0from certain civil service laws when it is carrying out its hiring authority.</p><p>Finally, the bill subjects BPA's employees\u00a0to certain merit system principles.</p>"
        },
        "title": "Reliability for Ratepayers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr447.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reliability for Ratepayers Act</strong></p><p>This bill modifies provisions concerning the hiring and compensation of employees of the\u00a0Bonneville Power Administration (BPA), which is a nonprofit federal power marketing\u00a0administration that sells hydropower in the Northwest.</p><p>Specifically, it directs BPA\u00a0to develop and implement a\u00a0plan that specifies and fixes the compensation for its employees, including members of the Senior Executive Service. Within a year, BPA must develop an initial compensation plan, which must be approved by the Department of Energy. BPA must implement the plan no later than one year after the plan is developed. </p><p>The compensation plan must be based on an annual survey of the prevailing compensation for similar positions in the public sectors of the electric industry, provide compensation that is competitive with\u00a0similar positions among consumer-owned utilities in the Western Interconnection, be consistent with BPA's approved annual general and administrative budget, and meet other criteria as outlined in the bill.\u00a0</p><p>BPA must (1) annually review the compensation plan and make any updates as appropriate, and (2) publish the plan and any updates made to the plan.</p><p>The bill exempts\u00a0BPA\u00a0from certain civil service laws when it is carrying out its hiring authority.</p><p>Finally, the bill subjects BPA's employees\u00a0to certain merit system principles.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr447"
    },
    "title": "Reliability for Ratepayers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reliability for Ratepayers Act</strong></p><p>This bill modifies provisions concerning the hiring and compensation of employees of the\u00a0Bonneville Power Administration (BPA), which is a nonprofit federal power marketing\u00a0administration that sells hydropower in the Northwest.</p><p>Specifically, it directs BPA\u00a0to develop and implement a\u00a0plan that specifies and fixes the compensation for its employees, including members of the Senior Executive Service. Within a year, BPA must develop an initial compensation plan, which must be approved by the Department of Energy. BPA must implement the plan no later than one year after the plan is developed. </p><p>The compensation plan must be based on an annual survey of the prevailing compensation for similar positions in the public sectors of the electric industry, provide compensation that is competitive with\u00a0similar positions among consumer-owned utilities in the Western Interconnection, be consistent with BPA's approved annual general and administrative budget, and meet other criteria as outlined in the bill.\u00a0</p><p>BPA must (1) annually review the compensation plan and make any updates as appropriate, and (2) publish the plan and any updates made to the plan.</p><p>The bill exempts\u00a0BPA\u00a0from certain civil service laws when it is carrying out its hiring authority.</p><p>Finally, the bill subjects BPA's employees\u00a0to certain merit system principles.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr447"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr447ih.xml"
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
      "title": "Reliability for Ratepayers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reliability for Ratepayers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide compensation flexibility to address retention and hiring issues at the Bonneville Power Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:18Z"
    }
  ]
}
```
