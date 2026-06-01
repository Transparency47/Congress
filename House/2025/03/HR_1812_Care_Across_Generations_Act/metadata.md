# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1812
- Title: Care Across Generations Act
- Congress: 119
- Bill type: HR
- Bill number: 1812
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1812",
    "number": "1812",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Care Across Generations Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "RI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1812ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1812\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Strickland (for herself and Mr. Steil ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Older Americans Act of 1965 to establish a grant program for multigenerational activities for long-term care facilities.\n#### 1. Short title\nThis Act may be cited as the Care Across Generations Act .\n#### 2. Competitive grant program for the funding of multigenerational programs in long-term care facilities\nPart A of title IV of the Older Americans Act of 1965 ( 42 U.S.C. 3032 et seq. ) is amended by adding at the end the following:\n423. Competitive grant program for the funding of multigenerational programs in long-term care facilities (a) Establishment of grant program The Assistant Secretary shall award grants, on a competitive basis, to eligible entities to\u2014 (1) operate a qualified child care facility within the long-term care facility or contract with a qualified child care facility; (2) coordinate multigenerational activities between the integrated qualified child care facility and long-term care facility; and (3) build a new, or expand an existing, long-term care facility operated by the eligible entity for any of the purposes described in paragraph (1) or (2). (b) Application An entity seeking a grant under this section shall submit an application to the Assistant Secretary at such time, in such manner, and accompanied by such information as the Assistant Secretary may reasonably require; and in accordance the requirements specified in subsection (g). (c) Evaluation and report (1) Evaluation Each eligible entity receiving a grant under this section shall evaluate\u2014 (A) the effectiveness of the entity in operating a qualified child care facility within an long-term care facility as required under subsection (a)(1); (B) the effectiveness of the multigenerational activities coordinated under subsection (a)(2); and (C) the impact on older individuals and children of the 14 co-location and multigenerational activities carried out by the entity. (2) Report Each eligible entity receiving a grant under this section shall, not later than 6 months after the expiration of the period for which the grant is in effect, submit a report to the Assistant Secretary containing the evaluation under paragraph (1). (d) Report to congress Not later than 6 months after the Assistant Secretary receives all reports required under subsection (c)(2), the Assistant Secretary shall prepare and submit to the Committee on Education and Labor of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report that assesses the evaluations contained in the reports required under subsection (c)(2). The report required of the Assistant Secretary under this subsection shall include, at a minimum\u2014 (1) the names and addresses of all eligible entities that received grants under this section; (2) a description of the methods such eligible entities used in operating qualified child care facilities within long-term care facilities as required under subsection (a)(1); (3) a description of the methods such eligible entities used in coordinating multigenerational activities required under subsection (a)(2); (4) a strategy for disseminating the findings resulting from the projects carried out through grants under this section; and (5) any policy change recommendations relating to operating qualified child care facilities within long-term care facilities. (e) Definitions As used in this section: (1) Eligible entity The term eligible entity means an organization operating an long-term care facility that submits an application meeting the requirements under subsection (b). (2) Long-term care facility The term long-term care facility means\u2014 (A) any skilled nursing facility, as defined in section 1819(a) of the Social Security Act ( 42 U.S.C. 1395i\u20133(a) ); (B) any nursing facility, as defined in section 1919(a) of the Social Security Act ( 42 U.S.C. 1396r(a) ); (C) a board and care facility; and (D) any other adult care home, including an assisted living facility, similar to a facility or institution described in subparagraphs (A) through (C). (3) Multigenerational activity The term multigenerational activity shall have the meaning given such term in section 417(h)(1). (4) Qualified child care facility The term qualified child care facility means a facility\u2014 (A) the principal use of which is to provide child care assistance; and (B) that meets the requirements of all applicable laws and regulations of the State or local government in which the facility is located, including with respect to the licensing of the facility as a child care facility. (f) Grant periods Each grant awarded under subsection (a) shall be for a period of not less than 36 months. (g) Additional requirements An application submitted by an eligible entity pursuant to subsection (b) shall include a certification that, for purposes of infection control and prevention, such entity\u2014 (1) conducts a screening process for all visitors of such entity; and (2) is in compliance with all applicable state and local sanitation and infection control requirements. .",
      "versionDate": "2025-03-03",
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
        "name": "Social Welfare",
        "updateDate": "2025-03-21T17:21:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1812",
          "measure-number": "1812",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1812v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Care Across Generations Act</strong></p><p>This bill requires\u00a0the Administration on Aging to award grants for long-term care facilities (including assisted living and nursing homes) to offer child care services and to coordinate multigenerational activities among long-term care and child care participants. In lieu of directly operating a child care facility, a long-term care facility may opt to contract with an existing child care facility. Grant recipients may also use the funds to build or expand a facility to accommodate child care and multigenerational events. \u00a0</p>"
        },
        "title": "Care Across Generations Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1812.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Care Across Generations Act</strong></p><p>This bill requires\u00a0the Administration on Aging to award grants for long-term care facilities (including assisted living and nursing homes) to offer child care services and to coordinate multigenerational activities among long-term care and child care participants. In lieu of directly operating a child care facility, a long-term care facility may opt to contract with an existing child care facility. Grant recipients may also use the funds to build or expand a facility to accommodate child care and multigenerational events. \u00a0</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1812"
    },
    "title": "Care Across Generations Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Care Across Generations Act</strong></p><p>This bill requires\u00a0the Administration on Aging to award grants for long-term care facilities (including assisted living and nursing homes) to offer child care services and to coordinate multigenerational activities among long-term care and child care participants. In lieu of directly operating a child care facility, a long-term care facility may opt to contract with an existing child care facility. Grant recipients may also use the funds to build or expand a facility to accommodate child care and multigenerational events. \u00a0</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1812"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1812ih.xml"
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
      "title": "Care Across Generations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Care Across Generations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Older Americans Act of 1965 to establish a grant program for multigenerational activities for long-term care facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:53Z"
    }
  ]
}
```
