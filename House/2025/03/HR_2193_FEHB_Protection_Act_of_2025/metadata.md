# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2193
- Title: FEHB Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2193
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-06-07T16:29:56Z
- Update date including text: 2025-06-07T16:29:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 15.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 15.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2193",
    "number": "2193",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "FEHB Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-07T16:29:56Z",
    "updateDateIncludingText": "2025-06-07T16:29:56Z"
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 15.",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
            "date": "2025-03-25T15:18:07Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-18T16:03:30Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2193ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2193\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Grothman introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Director of the Office of Personnel Management to take certain actions with respect to the health insurance program carried out under chapter 89 of title 5, United States Code, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FEHB Protection Act of 2025 .\n#### 2. FEHB improvements\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of the Office of Personnel Management.\n**(2) Employing office**\nThe term employing office has the meaning given the term in section 890.101(a) of title 5, Code of Federal Regulations, or any successor regulation.\n**(3) Health benefits plan; member of family**\nThe terms health benefits plan and member of family have the meanings given those terms in section 8901 of title 5, United States Code.\n**(4) Open season**\nThe term open season means an open season described in section 890.301(f) of title 5, Code of Federal Regulations, or any successor regulation.\n**(5) Program**\nThe term Program means the health insurance programs carried out under chapter 89 of title 5, United States Code, including the program carried out under section 8903c of that title.\n**(6) Qualifying life event**\nThe term qualifying life event has the meaning given the term in section 892.101 of title 5, Code of Federal Regulations, or any successor regulation.\n##### (b) Verification requirements\nNot later than 1 year after the date of the enactment of this Act, the Director shall issue regulations and implement a process to verify\u2014\n**(1)**\nthe veracity of any qualifying life event through which an enrollee in the Program seeks to add a member of family with respect to the enrollee to a health benefits plan under the Program; and\n**(2)**\nthat, when an enrollee in the Program seeks to add a member of family with respect to the enrollee to the health benefits plan of the enrollee under the Program, including during any open season, the individual so added is a qualifying member of family with respect to the enrollee.\n##### (c) Fraud risk assessment\nIn any fraud risk assessment conducted with respect to the Program on or after the date of the enactment of this Act, the Director shall include an assessment of individuals who are enrolled in, or covered under, a health benefits plan under the Program even though those individuals are not eligible to be so enrolled or covered.\n##### (d) Family member eligibility verification audit\n**(1) In general**\nDuring the 3-year period beginning 1 year after the date of the enactment of this Act, the Director, in coordination with the head of each employing office, shall conduct a comprehensive audit regarding members of family who are covered under an enrollment in a health benefits plan under the Program.\n**(2) Contents**\nIn conducting an audit required under paragraph (1), the Director, in coordination with the head of each employing office, shall review marriage certificates, birth certificates, and other appropriate documents that are necessary to determine eligibility to enroll in a health benefits plan under the Program.\n##### (e) Disenrollment or removal\nNot later than 6 months after the date of the enactment of this Act, the Director shall develop a process by which any individual enrolled in, or covered under, a health benefits plan under the Program who is not eligible to be so enrolled or covered shall be disenrolled or removed from enrollment in a health benefits plan under the Program.\n#### 3. Earned benefits and healthcare administrative services associated oversight and audit funding\n##### (a) In general\nSection 8909(a)(2) of title 5, United States Code, is amended by striking Congress. and inserting Congress, except that the amounts authorized under subsection (b)(2) for the Office shall not be subject to the limitations that may be specified annually by Congress. .\n##### (b) Oversight\nSection 8909(b) of title 5, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (5); and\n**(2)**\nby inserting after paragraph (1) the following:\n(2) In addition to the funds provided under paragraph (1), amounts of all contributions shall be available for the Office to develop, maintain, and conduct oversight over the enrollment and eligibility systems with respect to benefits under this chapter, including the Postal Service Health Benefits Program under section 8903c. Amounts for the Office under this paragraph shall not be available in excess of the following amounts in the following fiscal years: (A) In fiscal year 2026, $36,792,000. (B) In fiscal year 2027, $44,733,161. (C) In fiscal year 2028, $50,930,778. (D) In fiscal year 2029, $54,198,238. (E) In fiscal year 2030, $54,855,425. (F) In fiscal year 2031, $56,062,244. (G) In fiscal year 2032, $57,295,613. (H) In fiscal year 2033, $58,556,117. (I) In fiscal year 2034, $59,844,351. (J) In fiscal year 2035 and each fiscal year thereafter, the amount equal to the dollar limit for the immediately preceding fiscal year, increased by 2.2. percent. (3) In fiscal year 2026, $80,000,000, to be derived from all contributions and to remain available until expended, shall be available for the Office to conduct the audit required under section 2(d) of the FEHB Protection Act of 2025. Of such amount, the Office may transfer funds as the Director of the Office determines necessary to an employing office (as that term is defined in section 890.101(a) of title 5, Code of Federal Regulations, or any successor regulation) in order to conduct the required audit. (4) Amounts of all contributions shall be available for the Office of Personnel Management Office of the Inspector General to conduct oversight associated with activities under this chapter (including the Postal Service Health Benefits Program under section 8903c), including activities associated with enrollment and eligibility in these programs and any associated audit activities as required under the FEHB Protection Act of 2025. Amounts for the Office of the Inspector General under this paragraph shall not be available in excess of the following amounts in the following fiscal years: (A) In fiscal year 2026, $5,090,278. (B) In fiscal year 2027 and each fiscal year thereafter, the amount equal to the dollar limit for the immediately preceding fiscal year, increased by 2.2 percent. .",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-05-22",
        "actionTime": "06:56:39",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-06-02T20:32:52Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-02T20:32:58Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-02T20:32:19Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-02T20:32:10Z"
          },
          {
            "name": "Office of Personnel Management (OPM)",
            "updateDate": "2025-06-02T20:33:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-19T15:30:53Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2193ih.xml"
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
      "title": "FEHB Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEHB Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the Office of Personnel Management to take certain actions with respect to the health insurance program carried out under chapter 89 of title 5, United States Code, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:04Z"
    }
  ]
}
```
