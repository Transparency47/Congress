# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/66?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/66
- Title: Federal Employee Student Debt Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 66
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-03T16:08:25Z
- Update date including text: 2025-03-03T16:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/66",
    "number": "66",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Federal Employee Student Debt Transparency Act",
    "type": "HR",
    "updateDate": "2025-03-03T16:08:25Z",
    "updateDateIncludingText": "2025-03-03T16:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OK"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr66ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 66\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Brecheen ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend chapter 131 of title 5, United States Code, to require Senior Executive Service and schedule C employees to disclose Federal student loan debt, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Employee Student Debt Transparency Act .\n#### 2. Disclosure of Federal student loan debt by SES and schedule C employees\nSection 13104 of title 5, United States Code, is amended by adding at the end the following:\n(j) Disclosure of Federal student loan debt by SES and schedule C employees (1) Definition In this subsection, the term covered employee means an employee of the executive branch who occupies\u2014 (A) a Senior Executive Service position (as defined in section 3132(a)); or (B) a position of a confidential or policy-determining nature under schedule C of subpart C of part 213 of title 5, Code of Federal Regulations, or any successor regulation. (2) Reports by covered employees Not later than 60 days after the date of enactment of the Federal Employee Student Debt Transparency Act, and not later than February 28 of each year thereafter, each covered employee shall file a report containing a full and complete statement of the outstanding balance of principal and interest owed by the covered employee on\u2014 (A) each loan made under part D of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1087a et seq. ); and (B) any loan made, insured, or guaranteed under part B or E of such title ( 20 U.S.C. 1071 et seq. , 1087aa et seq.). (3) New covered employees Not later than 60 days after the date on which an individual assumes the position of a covered employee, the individual shall file a report containing the information required under paragraph (2). (4) Reports to Congress Not later than May 1 of each year, the Director of the Office of Government Ethics shall transmit to Congress a report containing\u2014 (A) the total amount owed by all covered employees as reported pursuant to paragraphs (2) and (3); and (B) the name of any covered employee who failed to file or report any information required to be reported pursuant to paragraph (2) or (3). .",
      "versionDate": "2025-01-03",
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
            "updateDate": "2025-03-03T16:08:25Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-03T16:06:38Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-03T16:08:19Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-03-03T16:08:14Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-03T16:08:00Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-03-03T16:08:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T13:12:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr66",
          "measure-number": "66",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr66v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Employee Student Debt Transparency Act</strong></p><p>This bill requires certain executive branch employees to disclose their federal student loan debt in an annual report.</p><p>The bill's requirement applies to an employee serving in a\u00a0Senior Executive Service position or a position of a confidential or policy-determining nature (i.e., a Schedule C position). Covered employees must file a report detailing the principal and interest owed on loans under the William D. Ford Federal Direct Loan Program, the Federal Family Education Loan Program, and the Federal Perkins Loan Program.\u00a0</p><p>The bill also requires the Office of Government Ethics to submit an annual report to Congress that contains (1) the total amount owed by all covered employees, and (2) the name of any covered employee who failed to report the required information.</p><p>\u00a0</p>"
        },
        "title": "Federal Employee Student Debt Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr66.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Employee Student Debt Transparency Act</strong></p><p>This bill requires certain executive branch employees to disclose their federal student loan debt in an annual report.</p><p>The bill's requirement applies to an employee serving in a\u00a0Senior Executive Service position or a position of a confidential or policy-determining nature (i.e., a Schedule C position). Covered employees must file a report detailing the principal and interest owed on loans under the William D. Ford Federal Direct Loan Program, the Federal Family Education Loan Program, and the Federal Perkins Loan Program.\u00a0</p><p>The bill also requires the Office of Government Ethics to submit an annual report to Congress that contains (1) the total amount owed by all covered employees, and (2) the name of any covered employee who failed to report the required information.</p><p>\u00a0</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr66"
    },
    "title": "Federal Employee Student Debt Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Employee Student Debt Transparency Act</strong></p><p>This bill requires certain executive branch employees to disclose their federal student loan debt in an annual report.</p><p>The bill's requirement applies to an employee serving in a\u00a0Senior Executive Service position or a position of a confidential or policy-determining nature (i.e., a Schedule C position). Covered employees must file a report detailing the principal and interest owed on loans under the William D. Ford Federal Direct Loan Program, the Federal Family Education Loan Program, and the Federal Perkins Loan Program.\u00a0</p><p>The bill also requires the Office of Government Ethics to submit an annual report to Congress that contains (1) the total amount owed by all covered employees, and (2) the name of any covered employee who failed to report the required information.</p><p>\u00a0</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr66"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr66ih.xml"
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
      "title": "Federal Employee Student Debt Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Employee Student Debt Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 131 of title 5, United States Code, to require Senior Executive Service and schedule C employees to disclose Federal student loan debt, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T03:33:36Z"
    }
  ]
}
```
