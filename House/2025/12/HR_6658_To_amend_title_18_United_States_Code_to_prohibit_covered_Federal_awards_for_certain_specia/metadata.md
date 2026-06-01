# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6658
- Title: BASIC Act
- Congress: 119
- Bill type: HR
- Bill number: 6658
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-02T15:50:10Z
- Update date including text: 2026-04-02T15:50:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6658",
    "number": "6658",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BASIC Act",
    "type": "HR",
    "updateDate": "2026-04-02T15:50:10Z",
    "updateDateIncludingText": "2026-04-02T15:50:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T16:02:35Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "DC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IN"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6658ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6658\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Min (for himself, Ms. Norton , Ms. Ansari , Mr. Garcia of California , Ms. Tlaib , Mr. Johnson of Georgia , Mr. Carson , and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 18, United States Code, to prohibit covered Federal awards for certain special Government employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ban on Self-Interested Contracting Act or the BASIC Act .\n#### 2. Prohibition on covered Federal awards for special Government employees\n##### (a) Prohibition\nChapter 11 of title 18, United States Code, is amended by inserting after section 220 the following (and conforming the table of sections of such chapter accordingly):\n221. Prohibition on covered Federal awards for special Government employees (a) Except as provided in subsection (c), any special Government employee who knowingly demands, seeks, receives, accepts, or agrees to receive or accept, directly or indirectly, any covered Federal award offered or issued by their employing agency shall be subject to the penalties set forth in section 216 of this title. (b) For purposes of subsection (a), a special Government employee indirectly demands, seeks, receives, accepts, or agrees to receive or accept a covered Federal award if\u2014 (1) such award is given, with the employee\u2019s knowledge and acquiescence to the employee's parent, sibling, spouse, child, dependent relative, or a member of the employee's household because of that person's relationship to the employee or the employee\u2019s spouse, minor child, or general partner; or (2) such award is given to any organization with whom the employee is an officer, director, trustee, general partner, or employee, or is negotiating for, or otherwise has an arrangement for employment, if\u2014 (A) the employee will aid or assist the organization in seeking, negotiating, or performing any part of the work under the covered Federal award; or (B) the employee will receive any compensation traceable to the covered Federal award. (c) Subsection (a) does not apply to a special Government employee who\u2014 (1) only serves as a member of an advisory committee; (2) has duties comparable to the duties of an individual in a position at GS\u201310 of the General Schedule or lower; or (3) has a position designated exclusively for students. (d) In this section: (1) The term advisory committee has the meaning given that term in section 1001 of title 5. (2) The term covered Federal award means a contract, grant, cooperative agreement, or other contract-like instrument, including an agreement entered into pursuant to other transaction authority, that awards to the recipient on an annual basis an amount that is more than $1,000,000. .\n##### (b) Revisions required\nNot later than 60 days after the date of the enactment of this section, part 3 of the Federal Acquisition Regulation and part 200, Code of Federal Regulations, shall be revised to prohibit any officer or employee of an executive branch agency or department from awarding a covered Federal award if to do so would violate section 2(a) of this Act in accordance with this section.\n##### (c) Guidance\nThe Office of Government Ethics shall issue regulatory guidance on this section and the amendment made by this section.\n#### 3. Publication of certain information relating to special Government employees\n##### (a) Position data\nSection 3330f(a)(5) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (A);\n**(2)**\nby striking the period at the end of subparagraph (B) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) includes any special Government employee (as that term is defined in section 202(a) of title 18), but not including any such employee who\u2014 (i) only serves as a member of an advisory committee; (ii) has duties comparable to the duties of an individual in a position at GS\u201310 of the General Schedule or lower; or (iii) has a position designated exclusively for students. .\n##### (b) Financial disclosure reports\nNotwithstanding chapter 131 of title 5, United States Code, including section 13109, each Executive agency shall make publicly available any financial disclosure report filed by a special Government employee with the Executive agency after the date of the enactment of this Act, using the procedures established under section 13107 of such title, except that this subsection shall not apply to any financial disclosure report that is filed by\u2014\n**(1)**\nan individual described in paragraph (1) or (2) of section 13107(a) of such title; or\n**(2)**\na special Government employee described in subsection (c) of section 221 of title 18, United States Code (as added by section 2(a) of this Act).\n#### 4. Database of special Government employees\nSection 1103 of title 5, United States Code, is amended by adding at the end the following:\n(d) (1) In this subsection, the term covered individual \u2014 (A) means an individual who is a special Government employee who is not serving on an advisory committee; and (B) does not include an individual described in paragraph (1) or (2) of section 13107(a). (2) The Director, in coordination with the Office of Government Ethics, shall maintain to the extent technically practicable, keep current, and make available to the public over the internet, without a fee or other access charge, in a searchable, sortable, and downloadable manner, an electronic database that contains the name of each covered individual, a rolling tally of the number of days the person has served as a special Government employee, and a description of why the individual was designated as a special Government employee rather than a regular employee. .",
      "versionDate": "2025-12-11",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-02T15:50:10Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6658ih.xml"
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
      "title": "BASIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BASIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ban on Self-Interested Contracting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit covered Federal awards for certain special Government employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:23Z"
    }
  ]
}
```
