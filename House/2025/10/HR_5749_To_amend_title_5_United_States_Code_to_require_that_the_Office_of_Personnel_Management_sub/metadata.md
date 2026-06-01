# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5749
- Title: Official Time Reporting Act
- Congress: 119
- Bill type: HR
- Bill number: 5749
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2026-01-09T16:41:29Z
- Update date including text: 2026-01-09T16:41:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5749",
    "number": "5749",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Official Time Reporting Act",
    "type": "HR",
    "updateDate": "2026-01-09T16:41:29Z",
    "updateDateIncludingText": "2026-01-09T16:41:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
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
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
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
        "item": [
          {
            "date": "2025-12-02T17:42:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-14T18:02:40Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "KY"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "AL"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5749ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5749\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Ms. Foxx (for herself, Mr. Comer , and Mr. Palmer ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to require that the Office of Personnel Management submit an annual report to Congress relating to the use of official time by Federal employees.\n#### 1. Short title\nThis Act may be cited as the Official Time Reporting Act .\n#### 2. Reporting requirement\n##### (a) In general\nSection 7131 of title 5, United States Code, is amended by adding at the end the following new subsection:\n(e) (1) (A) Not later than March 31 of each calendar year, the Director of the Office of Personnel Management, in consultation with the Director of the Office of Management and Budget, shall submit to the Committee on Oversight and Government Reform of the House of Representatives and Committee on Homeland Security and Governmental Affairs of the Senate, and make publicly available on a website of the Office of Personnel Management, a report covering the activities under this section during the most recently completed fiscal year prior to such calendar year, including each explanation submitted to the Director under subparagraph (C) and summarizing information received under subparagraph (B). (B) Not later than December 31 of each calendar year, the head of each agency shall submit to the Director of the Office of Personnel Management the information which the Director requires, with respect to such agency, for purposes of the report which is next due under subparagraph (A) in accordance with the guidance issued by the Director, including any standardized format for the submission of such information included in such guidance. (C) If the average aggregate official time rate of an agency for a fiscal year is greater than the average aggregate official time rate for such agency for the previous fiscal year, the head of such agency shall include an explanation for such increase in the information submitted to the Director of the Office of Personnel Management under subparagraph (B) for the purposes of the report required under subparagraph (A) covering such fiscal year. (2) Each report submitted by the Director of the Office of Personnel Management under paragraph (1)(A) shall include, with respect to the fiscal year covered by the report, the following information: (A) The total amount of official time granted to employees. (B) The average amount of official time expended per employee in a bargaining unit and the total number of employees in a bargaining unit. (C) For each agency, the average aggregate official time rate. (D) The agency or subdivision of an agency in which employees in a bargaining unit are employed. (E) The total amount withheld from the pay of employees in a bargaining unit using the payroll systems of agencies for the payment of the regular and periodic dues of the exclusive representative of the unit, and the total number of such employees that paid such dues through such payroll systems. (F) The specific types of activities or purposes for which official time was granted, and the effects on agency operations of such grants of official time for such activities or purposes. (G) The total number of employees to whom official time was granted and the number of such employees who as an employee, engaged in only activities or purposes involving the use of official time. (H) The amount paid by the Federal Government to employees granted official time with respect to the activities or purposes for which such employees were granted such official time, disaggregated by the costs of the compensation and fringe benefits of such employees and any travel, per diem, or other expense. (I) For each agency, a description of any room or space designated at the agency (or its subcomponent) as a room or space where employees of the agency conducted activities for which official time was granted, including the square footage of any such room or space, and, if the agency allowed a labor organization or individuals on official time the free or discounted use of property of the Government, the total fair market value of such free or discounted use and the amount, if any, paid by the labor organization to the agency for the use of such property. (3) The Director of the Office of Personnel Management shall\u2014 (A) provide the information required under paragraph (2) to be included in a report submitted by the Director under paragraph (1)(A) in the aggregate for all agencies and disaggregated by agency; and (B) include in each such report, other than the first such report submitted by the Director under paragraph (1)(A), comparisons of the information for the fiscal year covered by the report with the corresponding information for the previous fiscal year contained in the report submitted by the Director under paragraph (1)(A) covering such previous fiscal year, including such analysis of such comparisons as determined appropriate by the Director. (4) For the purposes of this subsection\u2014 (A) the term agency bargaining unit means a group of employees of an agency represented by an exclusive representative in an appropriate unit for collective bargaining under subchapter II of this chapter; (B) the term average aggregate official time rate , with respect to an agency, means the average of the official time rates for each agency bargaining unit of such agency for a fiscal year, weighted by the number of employees in each such agency bargaining unit as of the end of such fiscal year; (C) the term bargaining unit means a group of employees represented by an exclusive representative in an appropriate unit for collective bargaining under subchapter II of this chapter; (D) the term official time means the time an employee of an agency who is a labor representative for a labor organization spends performing non-agency business while on duty, either in service of such labor organization or otherwise acting in the capacity as an employee representative, including official time authorized under this section; and (E) the term official time rate means the total number of duty hours during a fiscal year that employees in an agency bargaining unit used for official time, divided by the number of employees in such agency bargaining unit as of the end of such fiscal year. .\n##### (b) Guidance\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Personnel Management shall\u2014\n**(1)**\nissue guidance to agencies (as defined in section 7103(a) of title 5, United States Code) regarding the submission of information under subparagraphs (B) and (C) of section 7131(e)(1) of title 5, United States Code, as added by subsection (a), which may include a standardized format for the submission of such information; and\n**(2)**\nin consultation with the Chief Human Capital Officers designated under chapter 14 of such title, promulgate any additional guidance that may be necessary or appropriate to assist the heads of such agencies in complying with the requirements of this Act and the amendments made by this Act.\n##### (c) Applicability\nThe amendment made by subsection (a) take effect on the first April 1 that is not less than six months after the date of the enactment of this Act.",
      "versionDate": "2025-10-14",
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
            "updateDate": "2026-01-09T16:41:16Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-01-09T16:41:25Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-09T16:41:21Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2026-01-09T16:41:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-09T21:22:43Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5749ih.xml"
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
      "title": "Official Time Reporting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Official Time Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to require that the Office of Personnel Management submit an annual report to Congress relating to the use of official time by Federal employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:15Z"
    }
  ]
}
```
