# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1599
- Title: Dismantling Investments in Violation of Ethical Standards through Trusts Act
- Congress: 119
- Bill type: HR
- Bill number: 1599
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-01-29T14:52:09Z
- Update date including text: 2026-01-29T14:52:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1599",
    "number": "1599",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Dismantling Investments in Violation of Ethical Standards through Trusts Act",
    "type": "HR",
    "updateDate": "2026-01-29T14:52:09Z",
    "updateDateIncludingText": "2026-01-29T14:52:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:03:30Z",
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
          "date": "2025-02-26T15:03:25Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "ME"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "OK"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1599ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1599\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Cloud (for himself, Mr. Golden of Maine , Mr. Self , Mr. Brecheen , and Mrs. Cammack ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 5, United States Code, to prohibit transactions involving certain financial instruments by senior Federal employees, their spouses, or dependent children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dismantling Investments in Violation of Ethical Standards through Trusts Act .\n#### 2. Prohibiting transactions and ownership of certain financial instruments by senior Federal employees, their spouses, or dependent children\n##### (a) In general\nChapter 13 of title 5, United States Code, is amended by adding after subchapter III the following:\nIV Restrictions Regarding Financial Instruments 13151. Definitions In this subchapter: (1) Covered financial instrument (A) In general The term covered financial instrument means\u2014 (i) any investment in\u2014 (I) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (II) a security future (as defined in that section); or (III) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (ii) any economic interest comparable to an interest described in clause (i) that is acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means. (B) Exclusions The term covered financial instrument does not include\u2014 (i) a diversified mutual fund; (ii) a diversified exchange-traded fund; (iii) a United States Treasury bill, note, or bond; or (iv) compensation from the primary occupation of a spouse or dependent child of a senior Federal employee. (2) Qualified blind trust The term qualified blind trust has the meaning given the term in section 13104. (3) Senior Federal employee The term senior Federal employee means any individual occupying a Senior Executive Service position (as that term is defined in section 3132). (4) Supervising ethics office The term supervising ethics office has the meaning given the term in section 13101. 13152. Prohibition on certain transactions and holdings involving covered financial instruments (a) Prohibition Except as provided in subsection (b), a senior Federal employee, their spouse, or their dependent children may not, during the term of service of the employee, hold, purchase, or sell any covered financial instrument. (b) Exceptions The prohibition under subsection (a) does not apply to\u2014 (1) a sale by a senior Federal employee, their spouse, or their dependent child that is completed by the date that is\u2014 (A) for an employee serving on the date of enactment of this title, 180 days after that date of enactment; and (B) for any employee who commences service as an employee after the date of enactment of this title, 180 days after the first date of the initial term of service; (2) a covered financial instrument held in a qualified blind trust operated on behalf of, or for the benefit of, a senior Federal employee, their spouse, or their dependent child; or (3) a covered financial instrument exempted from coverage under section 208 of title 18 pursuant to section 2640.202 of title 5, Code of Federal Regulations (or any successor regulation). (c) Application of certificate of divestiture program For purposes of section 1043 of the Internal Revenue Code of 1986\u2014 (1) this section shall be treated as a Federal conflict of interest statute; and (2) any person required to dispose of any property by reason of this section shall be treated as an eligible person. (d) Penalties (1) Disgorgement A senior Federal employee, their spouse, or their dependent child shall disgorge to the general fund of the Treasury any profit from a transaction or holding involving a covered financial instrument that is conducted in violation of this section. (2) Income tax A loss from a transaction or holding involving a covered financial instrument that is conducted in violation of this section may not be deducted from the amount of income tax owed by the applicable senior Federal employee, their spouse, or their dependent child. (3) Fines A senior Federal employee who holds or conducts a transaction involving a covered financial instrument in violation of this section may be subject to a civil fine assessed by the supervising ethics office under section 13153. 13153. Certification of compliance (a) In general Not less frequently than annually, each senior Federal employee shall submit to the supervising ethics office a written certification that the employee, their spouse, or their dependent child has achieved compliance with the requirements of this title. (b) Publication The supervising ethics office shall publish each certification submitted under subsection (a) on a publicly available website. 13154. Authority of supervising ethics office (a) In general The supervising ethics office may implement and enforce the requirements of this subchapter, including by\u2014 (1) issuing\u2014 (A) for applicable senior Federal employees\u2014 (i) rules governing that implementation; and (ii) 1 or more reasonable extensions to achieve compliance with this subchapter, if the supervising ethics office determines that an employee is making a good faith effort to divest any covered financial instruments; and (B) guidance relating to covered financial instruments; (2) publishing on the internet certifications submitted by senior Federal employees under section 13153(a); and (3) assessing civil fines against any senior Federal employee who is in violation of this subchapter, subject to subsection (b). (b) Requirements for civil fines (1) Amount A fine imposed under this section against a senior Federal employee shall be equal to the greater of\u2014 (A) $1,000, or (B) an amount equal to 10 percent of the greatest dollar value of the applicable covered financial instrument during any period that such instrument was held by the applicable senior Federal employee or their spouse or dependent child (as the case may be). (2) In general Before imposing a fine pursuant to this section, the supervising ethics office shall provide to the applicable senior Federal employee\u2014 (A) a written notice describing each covered financial instrument transaction for which a fine will be assessed; and (B) an opportunity, with respect to each such covered financial instrument transaction\u2014 (i) for a hearing; and (ii) to achieve compliance with the requirements of this subchapter. (3) Publication The supervising ethics office shall publish on a publicly available website a description of\u2014 (A) each fine assessed pursuant to this section; (B) the reasons why each such fine was assessed; and (C) the result of each assessment, including any hearing under paragraph (2)(B)(i) relating to the assessment. (4) Appeal A senior Federal employee may appeal to the supervising ethics office a fine assessed under this section during the 30-day period beginning on the date the fine is so assessed. 13155. Audit by Government Accountability Office Not later than 2 years after the date of enactment of this subchapter, the Comptroller General of the United States shall\u2014 (1) conduct an audit of the compliance by senior Federal employees with the requirements of this subchapter; and (2) submit to each supervising ethics office a report describing the results of the audit conducted under paragraph (1). .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to individuals described in section 13152(a) of title 5, United States Code, (as added by subsection (a)) beginning on the date that is 12 months following the date of enactment of this Act.\n##### (c) Additional employees\nSection 13121(c)(1) of title 5, United States Code, is amended by inserting up to 100 after appoint .\n##### (d) Funding\nThe Director of the Office of Management and Budget may transfer such funds as the Director considers appropriate, to be derived from unobligated amounts available for executive branch programs identified by the Director to be duplicative, to the Office of Government Ethics for the purpose of carrying out this Act, to remain available until the date that is 5 years following the date of the enactment of this Act.",
      "versionDate": "2025-02-26",
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
            "name": "Commodities markets",
            "updateDate": "2025-07-24T14:37:57Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-07-24T14:37:36Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-07-24T14:37:27Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-07-24T14:37:42Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-24T14:37:32Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-07-24T14:37:49Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-07-24T14:37:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T14:05:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1599",
          "measure-number": "1599",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2026-01-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1599v00",
            "update-date": "2026-01-29"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dismantling Investments in Violation of Ethical Standards through Trusts Act</strong></p><p>This bill prohibits a senior federal employee or an employee's spouse or dependent children from holding, purchasing, or selling certain financial instruments during the employee's term of service.\u00a0(A senior federal employee is defined as any individual occupying a Senior Executive Service position.)</p><p>Financial instruments covered by this prohibition include any investments in securities, security futures, commodities, or comparable economic interests acquired through synthetic means such as the use of derivatives.\u00a0The prohibition does not apply to\u00a0such instruments if they are held in a qualified blind trust or fall below certain<em>\u00a0</em>value thresholds. Additionally, the prohibition does not apply to diversified mutual funds, diversified exchange-traded funds, specified Treasury debt securities, or compensation from the primary occupation of a spouse or child. The bill provides a 180-day window for individuals affected by the bill to sell any prohibited financial instruments.</p><p>Any profit made in violation of the prohibition must be disgorged (given)\u00a0to the Treasury and may subject the individual to a civil fine\u00a0assessed by the supervising ethics office.\u00a0A loss from a transaction or holding conducted in violation of this bill may not be deducted from the amount of income tax owed by the applicable senior federal employee, spouse, or dependent child.</p><p>The bill requires each senior federal employee to annually certify compliance, including the compliance of the employee's spouse and dependent children. The Government Accountability Office must conduct a\u00a0compliance audit.</p>"
        },
        "title": "Dismantling Investments in Violation of Ethical Standards through Trusts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1599.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dismantling Investments in Violation of Ethical Standards through Trusts Act</strong></p><p>This bill prohibits a senior federal employee or an employee's spouse or dependent children from holding, purchasing, or selling certain financial instruments during the employee's term of service.\u00a0(A senior federal employee is defined as any individual occupying a Senior Executive Service position.)</p><p>Financial instruments covered by this prohibition include any investments in securities, security futures, commodities, or comparable economic interests acquired through synthetic means such as the use of derivatives.\u00a0The prohibition does not apply to\u00a0such instruments if they are held in a qualified blind trust or fall below certain<em>\u00a0</em>value thresholds. Additionally, the prohibition does not apply to diversified mutual funds, diversified exchange-traded funds, specified Treasury debt securities, or compensation from the primary occupation of a spouse or child. The bill provides a 180-day window for individuals affected by the bill to sell any prohibited financial instruments.</p><p>Any profit made in violation of the prohibition must be disgorged (given)\u00a0to the Treasury and may subject the individual to a civil fine\u00a0assessed by the supervising ethics office.\u00a0A loss from a transaction or holding conducted in violation of this bill may not be deducted from the amount of income tax owed by the applicable senior federal employee, spouse, or dependent child.</p><p>The bill requires each senior federal employee to annually certify compliance, including the compliance of the employee's spouse and dependent children. The Government Accountability Office must conduct a\u00a0compliance audit.</p>",
      "updateDate": "2026-01-29",
      "versionCode": "id119hr1599"
    },
    "title": "Dismantling Investments in Violation of Ethical Standards through Trusts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dismantling Investments in Violation of Ethical Standards through Trusts Act</strong></p><p>This bill prohibits a senior federal employee or an employee's spouse or dependent children from holding, purchasing, or selling certain financial instruments during the employee's term of service.\u00a0(A senior federal employee is defined as any individual occupying a Senior Executive Service position.)</p><p>Financial instruments covered by this prohibition include any investments in securities, security futures, commodities, or comparable economic interests acquired through synthetic means such as the use of derivatives.\u00a0The prohibition does not apply to\u00a0such instruments if they are held in a qualified blind trust or fall below certain<em>\u00a0</em>value thresholds. Additionally, the prohibition does not apply to diversified mutual funds, diversified exchange-traded funds, specified Treasury debt securities, or compensation from the primary occupation of a spouse or child. The bill provides a 180-day window for individuals affected by the bill to sell any prohibited financial instruments.</p><p>Any profit made in violation of the prohibition must be disgorged (given)\u00a0to the Treasury and may subject the individual to a civil fine\u00a0assessed by the supervising ethics office.\u00a0A loss from a transaction or holding conducted in violation of this bill may not be deducted from the amount of income tax owed by the applicable senior federal employee, spouse, or dependent child.</p><p>The bill requires each senior federal employee to annually certify compliance, including the compliance of the employee's spouse and dependent children. The Government Accountability Office must conduct a\u00a0compliance audit.</p>",
      "updateDate": "2026-01-29",
      "versionCode": "id119hr1599"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1599ih.xml"
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
      "title": "Dismantling Investments in Violation of Ethical Standards through Trusts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dismantling Investments in Violation of Ethical Standards through Trusts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to prohibit transactions involving certain financial instruments by senior Federal employees, their spouses, or dependent children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:30Z"
    }
  ]
}
```
