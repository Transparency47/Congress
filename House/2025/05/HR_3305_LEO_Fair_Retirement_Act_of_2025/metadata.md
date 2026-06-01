# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3305
- Title: LEO Fair Retirement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3305
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-21T08:08:24Z
- Update date including text: 2026-05-21T08:08:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3305",
    "number": "3305",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000621",
        "district": "9",
        "firstName": "Nellie",
        "fullName": "Rep. Pou, Nellie [D-NJ-9]",
        "lastName": "Pou",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "LEO Fair Retirement Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:24Z",
    "updateDateIncludingText": "2026-05-21T08:08:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-08T13:02:05Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
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
      "sponsorshipDate": "2025-05-08",
      "state": "PA"
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
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3305ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3305\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Pou (for herself, Mr. Bacon , Mr. Fitzpatrick , and Mr. Connolly ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 5, United States Code, to provide that for purposes of computing the annuity of certain law enforcement officers, any hours worked in excess of the limitation applicable to law enforcement premium pay shall be included in such computation, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the LEO Fair Retirement Act of 2025 .\n##### (b) Findings\nCongress finds the following:\n**(1)**\nFederal law enforcement officers are never off-duty . They are counted on to respond at any time of the day or night, regardless of their official duty status, to protect the public safety. Outside of our Nation\u2019s Armed Forces, theirs is the only profession comprised of individuals who are routinely called upon to put their lives on the line to keep America safe.\n**(2)**\nThough the Federal Government may house the largest variety of occupations of any U.S. employer across its panoply of agencies and entities, Federal law enforcement is absolutely unique among them, and the Federal law enforcement officer has no counterpart in the private sector. It is one of the most stressful, most dangerous, and most rewarding careers for those who meet the rigorous requirements of the job.\n**(3)**\nIt was in recognition of the unique nature of the occupation, and the demanding schedules required of those who fill its ranks, that Congress established distinct pay and benefit systems for Federal law enforcement positions. This includes basic pay, retirement, and even overtime compensation.\n**(4)**\nUnder current law, however, the payment of overtime compensation is limited, and is only payable to the extent that the payments do not cause the aggregate of the law enforcement officer\u2019s biweekly or annual pay to exceed the pay caps established under section 5547 of title 5, United States Code. This often results in a law enforcement officer working significant amounts of overtime hours year after year for which the officer is never compensated.\n**(5)**\nIn light of the continuing homeland and national security threats facing our Nation, it is in the interest of the Federal Government to ensure that it can continue to recruit and retain the highest caliber personnel by allowing Federal law enforcement officers the opportunity to reclaim full credit in retirement for overtime hours worked but never paid.\n#### 2. Computation of annuity for hours worked in excess of law enforcement premium pay limitations\n##### (a) CSRS\n**(1) In general**\nSection 8339 of title 5, United States Code, is amended by adding at the end the following:\n(v) (1) Notwithstanding any other provision of this title, including sections 5545a and 5547, and consistent with the requirements of paragraph (2), any premium pay described in section 5547(a) that would have been received by a law enforcement officer but for the limitation provided in such section shall be included in the average pay of such officer for purposes of computing the annuity of such officer under this section. (2) (A) Paragraph (1) shall not apply unless the law enforcement officer makes a lump-sum payment to the Office in the manner prescribed under this paragraph. (B) The officer may\u2014 (i) not later than 180 days before the date that the officer\u2019s annuity will commence, request from the Office an estimate (expressed as a dollar figure) of\u2014 (I) the lump-sum payment described under subparagraph (C); (II) the amount of the officer\u2019s monthly annuity payment if the officer elects to make the lump-sum payment and receive an amended annuity that includes the application of paragraph (1); and (III) the amount of such officer\u2019s monthly annuity payment if the officer does not make such an election; and (ii) consistent with the requirements of subparagraph (D), not later than 90 days after receipt of the estimate under clause (i), irrevocably elect to make the lump-sum payment to the Office. (C) If a law enforcement officer makes an election pursuant to subparagraph (B)(ii), such officer shall make a lump-sum payment to the Office equal to the difference between\u2014 (i) the amount that would have been contributed by the officer and the employer under section 8334 during the 3 consecutive years used to determine average pay (as described under section 8331(4)) if the rate of basic pay of the officer during such period of years included any premium pay described in section 5547(a) that would have been received by a law enforcement officer but for the limitation provided in such section; and (ii) the amount that was so contributed during such period of years. (D) The officer may elect an actuarial annuity reduction, consistent with regulations prescribed by the Office, in lieu of the lump-sum payment required under subparagraphs (B) and (C). (3) In this subsection, the term law enforcement officer has the meaning given the term qualified public safety employee in section 72(t)(10) of the Internal Revenue Code of 1986. .\n**(2) Clarification with respect to annuity limit**\nThe limitation provided in section 8339(f) of title 5, United States Code, shall apply to any annuity calculated pursuant to subsection (v) of such section (as added by paragraph (1)).\n##### (b) FERS\nSection 8415 of title 5, United States Code, is amended by adding at the end the following:\n(o) (1) Notwithstanding any other provision of this title, including sections 5545a and 5547, and consistent with the requirements of paragraph (2), any premium pay described in section 5547(a) that would have been received by a law enforcement officer but for the limitation provided in such section shall be included in the average pay of such officer for purposes of computing the annuity of such officer under this section. (2) Paragraph (1) shall not apply unless the law enforcement officer makes a lump-sum payment to the Office in the same manner as prescribed under section 8339(v)(2). (3) In this subsection, the term law enforcement officer has the meaning given the term qualified public safety employee in section 72(t)(10) of the Internal Revenue Code of 1986. .\n##### (c) Application\nThe amendments made by subsections (a) and (b) shall apply to any applicable annuity calculated on or after the date that is one year after the date of enactment of this Act.\n##### (d) Regulations\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Director of the Office of Personnel Management shall promulgate regulations to carry out sections 8339(v) and 8415(o) of title 5, United States Code, as added by subsections (a) and (b).\n**(2) Lump-sum payment**\nSuch regulations shall include\u2014\n**(A)**\nprocedures under which any law enforcement officer covered by such sections may make the lump-sum payment as described under sections 8339(v)(2) and 8415(o)(2) of title 5, United States Code, as added by subsections (a) and (b), from amounts within the officer\u2019s Thrift Savings Fund account; and\n**(B)**\nprocedures, promulgated in consultation with the Thrift Savings Board, under which a transfer may be made from such account to the Office of Personnel Management.\n**(3) Solicitation of payroll information**\nSuch regulations shall include\u2014\n**(A)**\nguidance for agencies employing law enforcement officers for proper retention of payroll information required to carry out the amendments made by subsections (a) and (b), including, for each creditable year of service, the difference between the amount the law enforcement officer received in gross compensation and the amount that would have been received as gross compensation but for the application of the premium pay caps in section 5547 of title 5, United States Code; and\n**(B)**\nprocedures for the Director to solicit sufficient payroll information from the head of each applicable agency to provide for the computations required by the amendments made by this Act.\n#### 3. Eligibility for availability pay\n##### (a) In general\nSection 5545a of title 5, United States Code, is amended by adding at the end the following:\n(l) (1) The provisions of subsections (a)\u2013(h) providing for availability pay shall apply to a covered employee. For the purpose of this section, section 5542(d) of this title, and section 13(a)(16) and (b)(30) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 213(a)(16) and (b)(30)), a covered employee shall be deemed to be a criminal investigator as defined in this section. (2) In this subsection, the term covered employee means\u2014 (A) a Postal Inspector (referred to in section 1003(c) of title 39); (B) a criminal investigator classified under the GS\u20131811 series (or any successor series); (C) a Federal air marshal; (D) a special agent in the Diplomatic Security Service; (E) a probation officer (referred to in section 3672 of title 18); and (F) a pretrial services officer (referred to in section 3153 of title 18). .\n##### (b) Conforming amendment\nSection 410(b)(11) of title 39, United States Code, is amended by striking section 5520a and inserting sections 5520a and 5545a .\n#### 4. Credit for certain lump-sum payments of uncompensated law enforcement premium pay\n##### (a) In general\nIn the case of an individual, there shall be allowed as a credit against the tax imposed by chapter 1 of the Internal Revenue Code of 1986 for the taxable year an amount equal to the sum of the lump-sum payments made by the individual during such taxable year pursuant to section 8339(v)(2) or 8415(o)(2) of title 5, United States Code, with respect to an annuity of such individual.\n##### (b) Treated as non-Refundable personal credit\nFor purposes of the Internal Revenue Code of 1986, the credit allowed under subsection (a) shall be treated as a credit allowed under subpart A of part IV of subchapter A of chapter 1 of such Code.",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-06-06T18:20:44Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3305ih.xml"
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
      "title": "LEO Fair Retirement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:06Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEO Fair Retirement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to provide that for purposes of computing the annuity of certain law enforcement officers, any hours worked in excess of the limitation applicable to law enforcement premium pay shall be included in such computation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:18:20Z"
    }
  ]
}
```
