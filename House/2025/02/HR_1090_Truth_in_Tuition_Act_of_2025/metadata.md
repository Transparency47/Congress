# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1090?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1090
- Title: Truth in Tuition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1090
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1090",
    "number": "1090",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
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
    "title": "Truth in Tuition Act of 2025",
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
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:00:45Z",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "DC"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1090ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1090\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Perez (for herself, Mr. Peters , Mr. Connolly , Mr. Fitzpatrick , Ms. Norton , and Ms. Schakowsky ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require certain institutions of higher education to provide notice of tuition levels for students.\n#### 1. Short title\nThis Act may be cited as the Truth in Tuition Act of 2025 .\n#### 2. Notice of tuition levels\n##### (a) Amendment\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following new paragraph:\n(30) (A) The institution will provide to each student admitted to an undergraduate or graduate program\u2014 (i) a multi-year tuition and fee schedule; or (ii) a single-year tuition and fee schedule, and a nonbinding, multi-year estimate of net costs after all financial aid is awarded, assuming constant family and student income, assets, and relevant circumstances. (B) Multi-year schedules and estimates required by subparagraph (A) \u2014 (i) may include a percentage or dollar increase or decrease of any size the institution determines to be appropriate from one year to the next; and (ii) shall indicate, on a year-by-year basis, costs for the normal duration of such student's undergraduate or graduate program. (C) Institutions that elect a single-year tuition and fee schedule under subparagraph (A)(ii) shall include with each multi-year estimate provided under such subparagraph the average deviation, in percentage terms, between previous year estimates and actual net costs for students at their institution. (D) The Secretary shall waive the requirements of subparagraph (A) if the institution demonstrates to the Secretary that the requirements of subparagraph (A) are not practicable because of the occurrence of one or more events causing the institution severe economic distress, dramatic reduction of State or Federal aid, or any other circumstance determined to be appropriate by the Secretary. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall be effective on the date that is 120 days after the date of enactment of this Act.",
      "versionDate": "2025-02-06",
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
            "name": "Consumer affairs",
            "updateDate": "2025-04-16T13:29:36Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-16T13:29:36Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-04-16T13:29:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-11T15:09:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1090",
          "measure-number": "1090",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1090v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Truth in Tuition Act of </strong><strong>2025</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student\u00a0aid programs to provide admitted students with information related to tuition and fees. Specifically, the bill requires an IHE to provide to a student (1) a multi-year tuition and fee schedule; or (2) a single-year tuition and fee schedule and a nonbinding, multi-year estimate of net costs after financial aid is awarded. The Department of Education may waive this requirement under certain circumstances.</p>"
        },
        "title": "Truth in Tuition Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1090.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truth in Tuition Act of </strong><strong>2025</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student\u00a0aid programs to provide admitted students with information related to tuition and fees. Specifically, the bill requires an IHE to provide to a student (1) a multi-year tuition and fee schedule; or (2) a single-year tuition and fee schedule and a nonbinding, multi-year estimate of net costs after financial aid is awarded. The Department of Education may waive this requirement under certain circumstances.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr1090"
    },
    "title": "Truth in Tuition Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truth in Tuition Act of </strong><strong>2025</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student\u00a0aid programs to provide admitted students with information related to tuition and fees. Specifically, the bill requires an IHE to provide to a student (1) a multi-year tuition and fee schedule; or (2) a single-year tuition and fee schedule and a nonbinding, multi-year estimate of net costs after financial aid is awarded. The Department of Education may waive this requirement under certain circumstances.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr1090"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1090ih.xml"
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
      "title": "Truth in Tuition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Truth in Tuition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require certain institutions of higher education to provide notice of tuition levels for students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:35Z"
    }
  ]
}
```
