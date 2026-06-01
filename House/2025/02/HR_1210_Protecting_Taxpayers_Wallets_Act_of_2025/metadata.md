# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1210?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1210
- Title: Protecting Taxpayers’ Wallets Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1210
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-07-10T18:05:16Z
- Update date including text: 2025-07-10T18:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1210",
    "number": "1210",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Protecting Taxpayers\u2019 Wallets Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-10T18:05:16Z",
    "updateDateIncludingText": "2025-07-10T18:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
            "date": "2025-03-25T15:17:09Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-11T15:01:35Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1210ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1210\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Perry introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend chapter 71 of title 5, United States Code, to charge labor organizations for the agency resources and employee time used by such labor organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Taxpayers\u2019 Wallets Act of 2025 .\n#### 2. Charging labor organizations for use of Federal resources\n##### (a) In general\nChapter 71 of title 5, United States Code, is amended by adding at the end the following new section:\n7136. Charging labor organizations for use of Federal resources (a) Fees for use of agency resources (1) In general Notwithstanding any other provision of this chapter, the head of each agency shall charge each labor organization recognized as an exclusive representative of employees of such agency a fee each calendar quarter for the use of the resources of such agency during such quarter. (2) Fee calculation The amount of the fee the head of an agency charges a labor organization under paragraph (1) with respect to a calendar quarter shall be equal to the amount that is the sum of\u2014 (A) the value of the union time of each labor representative for such labor organization while employed by such agency in such quarter; and (B) the value of agency resources provided for union use to such labor organization by such agency in such quarter. (3) Timing (A) Notice Not later than 30 days after the end of each calendar quarter, the head of each agency shall submit to each labor organization charged a fee by such head under paragraph (1) with respect to such calendar quarter a notice stating the amount of such fee. (B) Due date Payment of a fee charged under paragraph (1) is due not later than 60 days after the date on which the labor organization charged such fee receives a notice under paragraph (A) with respect to such fee. (4) Payment (A) In general Payment of a fee charged under paragraph (1) shall be made to the head of the agency that charged such fee. (B) Transfer to general fund The head of an agency shall transfer each payment of a fee charged under paragraph (1) that such head receives to the general fund of the Treasury. (b) Value determinations (1) In general The head of an agency charging a labor organization a fee under subsection (a) shall determine the value of union time used by labor representatives and the value of agency resources provided for union use for the purposes of paragraph (2) of such subsection in accordance with this subsection. (2) Values For the purposes of paragraph (2) of subsection (a), with respect to a fee charged to a labor organization by the head of an agency under paragraph (1) of such subsection\u2014 (A) the value of the union time of a labor representative during a calendar quarter is equal to amount that is the product of the hourly rate of pay of such labor representative paid by such agency and the number of hours of union time of such labor representative during such calendar quarter during which such labor representative was on duty as an employee of such agency; and (B) such head of such agency shall determine the value of agency resources provided for union use during a calendar quarter using rates established by the General Services Administration, where applicable, or to the extent that such rates are inapplicable to such the use of such resources, the market rate for the use of such resources, except that with respect to resources used for both agency business and for purposes pertaining to matters covered by this chapter, only the value of the portion of the use of such resources for the business of such labor organization shall be included. (3) Determinations not subject to review No determination of the head of an agency described in paragraph (1) may be determined to be an unfair labor practice or subject to collective bargaining or grievance procedures under this chapter, or otherwise contested or appealed. (c) Enforcement and penalties (1) Penalties (A) In general If a labor organization does not pay a fee charged to such labor organization under subsection (a)(1) on or before the date on which payment for such fee becomes due, during the period beginning on the date on which such payment becomes due and ending on the date on which every fee charged to such labor organization under such subsection is fully paid\u2014 (i) the amount of such fee shall be increased at a rate equal to the interest rate; (ii) the head of each agency shall\u2014 (I) beginning on the date that is 90 days after the date on which such period begins\u2014 (aa) deny such labor organization and the labor representatives for such labor organization any further union time; (bb) cease providing and the deny further use of agency resources provided for union use by such labor representatives for the business of such labor organization; and (cc) not be subject to\u2014 (AA) any grievance procedures or binding arbitration invoked by such labor organization under section 7121; or (BB) any unfair labor practice complaints or proceedings under this chapter pertaining to such labor organization or employees represented by such labor organization; and (II) beginning on the date that is 180 days after the date on which such period begins\u2014 (aa) terminate all allotments made by or on behalf of the agency with respect to such labor organization under section 7115; and (bb) not authorize any such allotments with respect to such labor organization; and (III) on the date that is 365 days after the date on which such period begins, inform the Authority and such labor organization that such period has reached a duration of 365 days; and (iii) on the date that is 380 days after the date on which such period begins, the Authority shall terminate the certification of such labor organization as the exclusive representative of employees of such agency. (B) Exclusive representative prohibition A labor organization for which the Authority terminates a certification as the exclusive representatives of employees of an agency under subparagraph (A)(iii) may not be certified as the exclusive representative of any employee of such agency unless such labor organization pays all fees charged to such labor organization by the head of such agency under subsection (a)(1), including any increases to such fees under subparagraph (A)(i). (C) Rule of construction Subparagraph (A)(ii)(I)(cc) may not be construed as\u2014 (i) tolling any statutory or contractual deadline for the filing of a grievance, complaint of an unfair labor practice, or proceeding to binding arbitration; or (ii) preventing or limiting an agency from filing any grievance against a labor organization or advancing such grievances to binding arbitration. (2) Time tracking (A) In general Each agency shall track the use of union time by labor representatives using the applicable time and attendance tracking system of such agency. (B) Failure to record (i) In general A labor representative who uses union time and fails to record such use in the applicable time and attendance tracking system shall be considered absent without leave and subject to appropriate adverse action. (ii) Willful or repeated failures A failure of a labor representative described in clause (i) shall constitute an impairment to the efficient of the service if such failure is willful or occurs in the same fiscal year as another such failure by such labor representative. (iii) Limited review Adverse action take against an employee under clause (i)\u2014 (I) may not be determined to be an unfair labor practice or subject to grievance procedures or binding arbitration under section 7121; and (II) notwithstanding any other provision of law, shall be sustained on appeal if the determination of the agency to take such adverse action against such employee is supported by substantial evidence. (3) Payment required The head of an agency may not forgive, reimburse, waive, or in any other manner reduce any fee charged under this section. (4) Compliance Not later than two years after the date of the enactment of this section, and every two years thereafter, the Inspector General of each agency shall\u2014 (A) conduct an evaluation of the compliance of such agency and each relevant labor organization with the requirements of this section, including the accuracy with which labor representatives recorded the use of union time, the promptness with which fees under subsection (a) were charged and paid, and the valuation of agency resources provided for union use by such agency pursuant to subsection (b)(2)(B); and (B) submit to the head of such agency, the Committee on Oversight and Government Reform of the House of Representatives, and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the findings of the evaluation required by subparagraph (A). (d) Definitions In this section: (1) Agency business The term agency business means work performed by employees on behalf of an agency, or under the direction and control of the agency. (2) Agency resources provided for union use The term agency resources provided for union use means the resources of an agency, other than the time of employees in a duty status, that such agency provides to labor representatives for purposes pertaining to matters covered by this chapter, including agency office space, parking space, equipment, and reimbursement for expenses incurred while on union time or otherwise performing non-agency business, except that this term does not include any resource to the extent that such resource is used for agency business. (3) Labor organization The term labor organization means a labor organization recognized as an exclusive representative of employees of an agency under this chapter or as a representative of agency employees under any system established by the Transportation Security Administration Administrator pursuant to section 111(d) of the Aviation and Transportation Security Act ( 49 U.S.C. 44935 note). (4) Hourly rate of pay The term hourly rate of pay means the total cost to an agency of employing an employee in a pay period or pay periods, including wages, salary, and other cash payments, agency contributions to employee health and retirement benefits, employer payroll tax payments, paid leave accruals, and the cost to the agency for other benefits, divided by the number of hours such employee worked in such pay period or pay periods. (5) Interest rate The term interest rate means the average market yield of outstanding marketable obligations of the United States having maturities of 30 years plus one percentage point. (6) Labor representative The term labor representative means an employee of an agency serving in any official or other representative capacity for a labor organization (including as any officer or steward of a labor organization) that is the exclusive representative of employees of such agency under this chapter or is the representative of employees under any system established by the Transportation Security Administration Administrator pursuant to section 111(d) of the Aviation and Transportation Security Act ( 49 U.S.C. 44935 note). (7) Union time The term union time means the time an employee of an agency who is a labor representative for a labor organization spends performing non-agency business while on duty, either in service of such labor organization or otherwise acting in the capacity as an employee representative, including official time authorized under section 7131. .\n##### (b) Clerical amendment\nThe table of sections for chapter 71 of title 5, United States Code, is amended by adding at the end the following new item:\n7136. Charging labor organizations for use of Federal resources. .",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "511",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Taxpayers\u2019 Wallets Act of 2025",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-05-12T19:19:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-12T19:19:56Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-05-12T19:19:56Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-05-12T19:19:56Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-05-12T19:19:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T14:47:28Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1210ih.xml"
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
      "title": "Protecting Taxpayers\u2019 Wallets Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Taxpayers\u2019 Wallets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 71 of title 5, United States Code, to charge labor organizations for the agency resources and employee time used by such labor organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T04:18:57Z"
    }
  ]
}
```
