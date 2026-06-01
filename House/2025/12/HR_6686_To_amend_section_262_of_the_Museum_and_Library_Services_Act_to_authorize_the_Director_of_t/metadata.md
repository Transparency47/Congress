# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6686
- Title: No Cost Educational Resources Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6686
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-04-06T18:49:10Z
- Update date including text: 2026-04-06T18:49:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6686",
    "number": "6686",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "No Cost Educational Resources Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T18:49:10Z",
    "updateDateIncludingText": "2026-04-06T18:49:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:25Z",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6686ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6686\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mr. Foster introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend section 262 of the Museum and Library Services Act to authorize the Director of the Institute of Museum and Library Services to award grants to institutions of higher education for courses that use only publicly available digital resources for required reading assignments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Cost Educational Resources Act of 2025 .\n#### 2. Grants\nSection 262 of the Museum and Library Services Act ( 20 U.S.C. 9162 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking nationwide and to and inserting nationwide, to ; and\n**(ii)**\nby inserting , and to provide funding for open educational reading material courses after museums ;\n**(B)**\nin paragraph (4)(B), by striking and at the end;\n**(C)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(6) facilitating the adoption, adaption, and creation of open educational reading materials, and establishing more open educational reading material courses, pursuant to subsection (d). ;\n**(2)**\nin subsection (c), by striking The Director and inserting Except as provided in subsection (d), the Director ; and\n**(3)**\nby adding at the end the following:\n(d) Open educational reading material courses (1) Definitions For purposes of this section: (A) The term open educational reading material means a free digital text that is publicly available to be downloaded and redistributed. (B) The term open educational reading material course means a science, technology, engineering, or math course offered by an institution of higher education that uses only open educational reading materials as the form of the required readings for the course. (2) Application To receive a grant under subsection (a)(6), an institution of higher education shall submit to the Director an application that includes\u2014 (A) a description of how the institution of higher education\u2014 (i) plans to facilitate the adoption, adaption, and creation of open educational reading materials by assigning leadership of the grant implementation to library administrators and librarians; (ii) has collaborated with science, technology, engineering, and mathematics department faculty in developing the application and plans to continue to collaborate with such faculty in implementing the grant projects; and (iii) plans to collaborate with other institutions of higher education to facilitate the wider adoption, adaption, and creation of open educational reading materials throughout the higher education community; and (B) a plan to review the quality of the open educational reading materials used at such institution of higher education. (3) Priority In awarding grants under subsection (a)(6), the Director shall give priority to an institution of higher education that\u2014 (A) enrolls a high number of low-income or minority students, or both; and (B) plans\u2014 (i) to assign a member of the faculty and a librarian to coordinate the implementation of open educational reading material courses; (ii) to use library resources to facilitate the use of open educational reading materials; (iii) to use open educational reading materials as the form of the required readings for science, technology, engineering, and mathematics courses with high enrollment; and (iv) to provide incentives for faculty to use only open educational reading materials as the form of the required readings for their courses, such as monetary awards or dedicated work time to adopt, adapt, or create such materials. (4) Report Not later than 2 years after the date on which the first grant is awarded under subsection (a)(6), the Director shall submit to Congress a report that includes\u2014 (A) the number of grants awarded under subsection (a)(6); (B) an evaluation of the effect of such grants on increasing the number of science, technology, engineering, and mathematics courses using open educational reading materials as the form of required readings for such courses; and (C) an evaluation of the amount of money saved by students who enroll in open educational reading material courses in comparison to students who enroll in similar courses with required readings that are only available by purchase. .",
      "versionDate": "2025-12-12",
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
        "name": "Education",
        "updateDate": "2026-01-08T16:43:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-12",
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
          "measure-id": "id119hr6686",
          "measure-number": "6686",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-12",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6686v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-12-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Cost Educational Resources Act</strong> <strong>of 2025</strong></p><p>This bill authorizes the Institute of Museum and Library Services to award grants to institutions of higher education (IHEs) for facilitating the adoption, adaption, and creation of open educational reading materials and establishing more open educational reading material courses.</p><p><em>Open educational reading material</em> refers to a free digital text that is publicly available to be downloaded and redistributed.</p><p><em>Open educational reading material course</em> refers to a science, technology, engineering, or math course offered by an IHE that uses only open educational reading materials as the form of the required readings for the course.</p>"
        },
        "title": "No Cost Educational Resources Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6686.xml",
    "summary": {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Cost Educational Resources Act</strong> <strong>of 2025</strong></p><p>This bill authorizes the Institute of Museum and Library Services to award grants to institutions of higher education (IHEs) for facilitating the adoption, adaption, and creation of open educational reading materials and establishing more open educational reading material courses.</p><p><em>Open educational reading material</em> refers to a free digital text that is publicly available to be downloaded and redistributed.</p><p><em>Open educational reading material course</em> refers to a science, technology, engineering, or math course offered by an IHE that uses only open educational reading materials as the form of the required readings for the course.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6686"
    },
    "title": "No Cost Educational Resources Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Cost Educational Resources Act</strong> <strong>of 2025</strong></p><p>This bill authorizes the Institute of Museum and Library Services to award grants to institutions of higher education (IHEs) for facilitating the adoption, adaption, and creation of open educational reading materials and establishing more open educational reading material courses.</p><p><em>Open educational reading material</em> refers to a free digital text that is publicly available to be downloaded and redistributed.</p><p><em>Open educational reading material course</em> refers to a science, technology, engineering, or math course offered by an IHE that uses only open educational reading materials as the form of the required readings for the course.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6686"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6686ih.xml"
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
      "title": "No Cost Educational Resources Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:54:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Cost Educational Resources Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 262 of the Museum and Library Services Act to authorize the Director of the Institute of Museum and Library Services to award grants to institutions of higher education for courses that use only publicly available digital resources for required reading assignments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:48:44Z"
    }
  ]
}
```
