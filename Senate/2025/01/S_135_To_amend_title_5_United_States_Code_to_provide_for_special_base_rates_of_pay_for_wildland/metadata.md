# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/135?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/135
- Title: Wildland Firefighter Paycheck Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 135
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:45:34Z
- Update date including text: 2025-12-05T21:45:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/135",
    "number": "135",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Wildland Firefighter Paycheck Protection Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:45:34Z",
    "updateDateIncludingText": "2025-12-05T21:45:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-16T21:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NM"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WY"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "MI"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s135is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 135\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Padilla (for himself, Mr. Daines , Mr. Barrasso , Mr. Schiff , Mr. Sheehy , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to provide for special base rates of pay for wildland firefighters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildland Firefighter Paycheck Protection Act of 2025 .\n#### 2. Special base rates of pay for wildland firefighters\n##### (a) In general\nSubchapter III of chapter 53 of title 5, United States Code, is amended by inserting after section 5332 the following:\n5332a. Special base rates of pay for wildland firefighters (a) Definitions In this section\u2014 (1) the term firefighter means an employee who\u2014 (A) is a firefighter within the meaning of section 8331(21) or section 8401(14); (B) in the case of an employee who holds a supervisory or administrative position and is subject to subchapter III of chapter 83, but who does not qualify to be considered a firefighter within the meaning of section 8331(21), would otherwise qualify if the employee had transferred directly to that position after serving as a firefighter within the meaning of that section; (C) in the case of an employee who holds a supervisory or administrative position and is subject to chapter 84, but who does not qualify to be considered a firefighter within the meaning of section 8401(14), would otherwise qualify if the employee had transferred directly to that position after performing duties described in section 8401(14)(A) for at least 3 years; or (D) in the case of an employee who is not subject to subchapter III of chapter 83 or chapter 84, holds a position that the Office of Personnel Management determines would satisfy subparagraph (A), (B), or (C) if the employee were subject to subchapter III of chapter 83 or chapter 84; (2) the term General Schedule base rate means an annual rate of basic pay established under section 5332 before any additions, such as a locality-based comparability payment under section 5304 or 5304a or a special rate supplement under section 5305; (3) the term special base rate means an annual rate of basic pay payable to a wildland firefighter, before any additions or reductions, that replaces the General Schedule base rate otherwise applicable to the wildland firefighter and that is administered in the same manner as a General Schedule base rate; and (4) the term wildland firefighter means a firefighter\u2014 (A) who is employed by the Forest Service or the Department of the Interior; and (B) the duties of the position of whom relate primarily to wildland fires, as opposed to structure fires. (b) Special base rates of pay (1) Entitlement to special rate Notwithstanding section 5332, a wildland firefighter is entitled to a special base rate at grades 1 through 15, which shall\u2014 (A) replace the otherwise applicable General Schedule base rate for the wildland firefighter; (B) be basic pay for all purposes, including the purpose of computing a locality-based comparability payment under section 5304 or 5304a; and (C) be computed as described in paragraph (2) and adjusted at the time of adjustments in the General Schedule. (2) Computation (A) In general The special base rate for a wildland firefighter shall be derived by increasing the otherwise applicable General Schedule base rate for the wildland firefighter by the following applicable percentage for the grade of the wildland firefighter and rounding the result to the nearest whole dollar: (i) For GS\u20131, 42 percent. (ii) For GS\u20132, 39 percent. (iii) For GS\u20133, 36 percent. (iv) For GS\u20134, 33 percent. (v) For GS\u20135, 30 percent. (vi) For GS\u20136, 27 percent. (vii) For GS\u20137, 24 percent. (viii) For GS\u20138, 21 percent. (ix) For GS\u20139, 18 percent. (x) For GS\u201310, 15 percent. (xi) For GS\u201311, 12 percent. (xii) For GS\u201312, 9 percent. (xiii) For GS\u201313, 6 percent. (xiv) For GS\u201314, 3 percent. (xv) For GS\u201315, 1.5 percent. (B) Hourly, daily, weekly, or biweekly rates When the special base rate with respect to a wildland firefighter is expressed as an hourly, daily, weekly, or biweekly rate, the special base rate shall be computed from the appropriate annual rate of basic pay derived under subparagraph (A) in accordance with the rules under section 5504(b). .\n##### (b) Clerical amendment\nThe table of sections for subchapter III of chapter 53 of title 5, United States Code, is amended by inserting after the item relating to section 5332 the following:\n5332a. Special base rates of pay for wildland firefighters. .\n##### (c) Prevailing rate employees\nSection 5343 of title 5, United States Code, is amended by adding at the end the following:\n(g) (1) For a prevailing rate employee described in section 5342(a)(2)(A) who is a wildland firefighter, as defined in section 5332a(a), the Secretary of Agriculture or the Secretary of the Interior (as applicable) shall increase the wage rates of that employee by an amount (determined at the sole and exclusive discretion of the applicable Secretary after consultation with the other Secretary) that is generally consistent with the percentage increases given to wildland firefighters in the General Schedule under section 5332a. (2) An increased wage rate under paragraph (1) shall be basic pay for the same purposes as the wage rate otherwise established under this section. (3) An increase under this subsection may not cause the wage rate of an employee to increase to a rate that would produce an annualized rate in excess of the annual rate for level IV of the Executive Schedule. .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the first day of the first applicable pay period beginning after the last day of the last pay period for which Federal wildland firefighter temporary salary increases were in effect, as originally authorized under section 40803(d)(4)(B) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(d)(4)(B) ) and as extended under the Consolidated Appropriations Act, 2024 ( Public Law 118\u201342 ; 138 Stat. 25), the Continuing Appropriations Act, 2025 (division A of Public Law 118\u201383 ; 138 Stat. 1524), and the Further Continuing Appropriations Act, 2025 (division A of Public Law 118\u2013158 ).\n#### 3. Wildland fire incident response premium pay\n##### (a) In general\nSubchapter V of chapter 55 of title 5, United Sates Code, is amended by inserting after section 5545b the following:\n5545c. Incident response premium pay for employees engaged in wildland firefighting (a) Definitions In this section\u2014 (1) the term appropriate committees of Congress means\u2014 (A) the Committee on Homeland Security and Governmental Affairs of the Senate; (B) the Committee on Energy and Natural Resources of the Senate; (C) the Committee on Agriculture, Nutrition, and Forestry of the Senate; (D) the Committee on Appropriations of the Senate; (E) the Committee on Oversight and Accountability of the House of Representatives; (F) the Committee on Agriculture of the House of Representatives; (G) the Committee on Natural Resources of the House of Representatives; and (H) the Committee on Appropriations of the House of Representatives; (2) the term covered employee means an employee of the Forest Service or the Department of the Interior who is\u2014 (A) a wildland firefighter, as defined in section 5332a(a); or (B) certified by the applicable agency to perform wildland fire incident-related duties during the period that employee is deployed to respond to a qualifying incident; (3) the term incident response premium pay means pay to which a covered employee is entitled under subsection (c); (4) the term prescribed fire incident means a wildland fire originating from a planned ignition in accordance with applicable laws, policies, and regulations to meet specific objectives; (5) the term qualifying incident \u2014 (A) means\u2014 (i) a wildfire incident, a prescribed fire incident, or a severity incident; or (ii) an incident that the Secretary of Agriculture or the Secretary of the Interior determines is similar in nature to an incident described in clause (i); and (B) does not include an initial response (including an initial attack fire) in which a wildfire is contained within 36 hours; and (6) the term severity incident means an incident in which a covered employee is pre-positioned in an area in which conditions indicate there is a high risk of wildfires. (b) Eligibility A covered employee is eligible for incident response premium pay under this section if\u2014 (1) the covered employee is deployed to respond to a qualifying incident; and (2) the deployment described in paragraph (1) is\u2014 (A) outside of the official duty station of the covered employee; or (B) within the official duty station of the covered employee and the covered employee is assigned to an incident-adjacent fire camp or other designated field location. (c) Entitlement to incident response premium pay (1) In general A covered employee who satisfies the conditions under subsection (b) is entitled to premium pay for the period in which the covered employee is deployed to respond to the applicable qualifying incident. (2) Computation (A) Formula Subject to subparagraphs (B) and (C), premium pay under paragraph (1) shall be paid to a covered employee at a daily rate of 450 percent of the hourly rate of basic pay of the covered employee for each day that the covered employee satisfies the requirements under subsection (b), rounded to the nearest whole cent. (B) Limitation Premium pay under this subsection\u2014 (i) with respect to a covered employee for whom the annual rate of basic pay is greater than that for step 10 of GS\u201310, shall be paid at the daily rate established under subparagraph (A) for the applicable rate for step 10 of GS\u201310 (where the applicable rate is the rate in effect in the same locality that is the basis for a locality-based comparability payment payable to the covered employee under section 5304); and (ii) may not be paid to a covered employee in a total amount that exceeds $9,000 in any calendar year. (C) Adjustments (i) Assessment The Secretary of Agriculture and the Secretary of the Interior shall assess the difference between the average total amount of compensation that was paid to covered employees, by grade, in fiscal years 2023 and 2024. (ii) Report Not later than 180 days after the date that is 1 year after the effective date of this section, the Secretary of Agriculture and the Secretary of the Interior shall jointly publish a report on the results of the assessment conducted under clause (i). (iii) Administrative actions After publishing the report required under clause (ii), the Secretary of Agriculture and the Secretary of the Interior, in consultation with the Director of the Office of Personnel Management, may, in the sole and exclusive discretion of the Secretaries acting jointly, administratively adjust the amount of premium pay paid under this subsection (or take other administrative action) to ensure that the average annual amount of total compensation paid to covered employees, by grade, is more consistent with such amount that was paid to those employees in fiscal year 2023. (iv) Congressional notification Not later than 3 days after an adjustment made, or other administrative action taken, under clause (iii) becomes final, the Secretary of Agriculture and the Secretary of the Interior shall jointly submit to the appropriate committees of Congress a notification regarding that adjustment or other administrative action, as applicable. (d) Treatment of incident response premium pay Incident response premium pay under this section\u2014 (1) is not considered part of the basic pay of a covered employee for any purpose; (2) may not be considered in determining the lump-sum payment of a covered employee for accumulated and accrued annual leave under section 5551 or section 5552; (3) may not be used in determining pay under section 8114; (4) may not be considered in determining pay for hours of paid leave or other paid time off during which the premium pay is not payable; and (5) shall be disregarded in determining the minimum wage and overtime pay to which a covered employee is entitled under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ). .\n##### (b) Additional premium pay amendments\nSubchapter V of chapter 55 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 5544\u2014\n**(A)**\nby amending the section heading to read as follows: Wage-board overtime, Sunday rates, and other premium pay ; and\n**(B)**\nby adding at the end the following:\n(d) A prevailing rate employee described in section 5342(a)(2)(A) shall receive incident response premium pay under the same terms and conditions that apply to a covered employee under section 5545c if that employee\u2014 (1) is employed by the Forest Service or the Department of the Interior; and (2) (A) is a wildland firefighter, as defined in section 5332a(a); or (B) is certified by the applicable agency to perform wildland fire incident-related duties during the period the employee is deployed to respond to a qualifying incident (as defined in section 5545c(a)). ; and\n**(2)**\nin section 5547(a), in the matter preceding paragraph (1), by inserting 5545c, after 5545a, .\n##### (c) Clerical amendments\nThe table of sections for subchapter V of chapter 55 of title 5, United States Code, is amended\u2014\n**(1)**\nby amending the item relating to section 5544 to read as follows:\n5544. Wage-board overtime, Sunday rates, and other premium pay. ;\nand\n**(2)**\nby inserting after the item relating to section 5545b the following:\n5545c. Incident response premium pay for employees engaged in wildland firefighting. .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the first day of the first applicable pay period beginning after the last day of the last pay period for which Federal wildland firefighter temporary salary increases were in effect, as originally authorized under section 40803(d)(4)(B) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(d)(4)(B) ) and as extended under the Consolidated Appropriations Act, 2024 ( Public Law 118\u201342 ; 138 Stat. 25), the Continuing Appropriations Act, 2025 (division A of Public Law 118\u201383 ; 138 Stat. 1524), and the Further Continuing Appropriations Act, 2025 (division A of Public Law 118\u2013158 ).\n#### 4. Rest and recuperation leave for employees engaged in wildland firefighting\n##### (a) In general\nSubchapter II of chapter 63 of title 5, United States Code, is amended by adding at the end the following:\n6329e. Rest and recuperation leave for employees engaged in wildland firefighting (a) Definitions In this section\u2014 (1) the term applicable Secretary means the Secretary of Agriculture or the Secretary of the Interior, as applicable to a covered employee; (2) the term covered employee means an employee of the Forest Service or the Department of the Interior who\u2014 (A) qualifies as a wildland firefighter based on the definitions of the terms firefighter and wildland firefighter in section 5332a(a) (applying the definition of employee in section 6301(2) in lieu of the definition of employee in section 5331(a)); or (B) is certified by the applicable Secretary to perform wildland fire incident-related duties during the period the employee is deployed to respond to a qualifying incident; and (3) the term qualifying incident has the meaning given the term in section 5545c(a). (b) Rest and recuperation leave (1) In general A covered employee may receive paid rest and recuperation leave following the completion of service in which the covered employee is deployed to respond to a qualifying incident, subject to the policies prescribed under this subsection. (2) Prescription of policies The Secretary of Agriculture and the Secretary of the Interior shall, in the sole and exclusive discretion of the Secretaries acting jointly, prescribe uniform policies described in paragraph (1) after consulting with the other applicable Secretary. (3) Content of policies The policies prescribed under paragraph (2) may include\u2014 (A) a maximum period of days in which a covered employee is deployed to respond to a qualifying incident, which shall\u2014 (i) begin on the date on which the covered employee departs from the official duty station of the covered employee and end on the date on which the covered employee returns to the official duty station of the covered employee; and (ii) be followed by a minimum number of days of rest and recuperation for the covered employee; or (B) a requirement that prohibits a covered employee from working more than 16 hours per day on average over a 14-day period during which the covered employee is deployed to respond to a qualifying incident. (c) Use of leave (1) In general Rest and recuperation leave granted under this section\u2014 (A) shall be used during scheduled hours within the tour of duty of the applicable covered employee established for leave-charging purposes; (B) shall be paid in the same manner as annual leave; (C) shall be used immediately after a qualifying incident; and (D) may not be set aside for later use. (2) No payment A covered employee may not receive any payment for unused rest and recuperation leave granted under this section. (d) Intermittent work schedule A covered employee with an intermittent work schedule\u2014 (1) shall be excused from duty during the same period of time that other covered employees in the same circumstances are entitled to rest and recuperation leave; and (2) shall receive a payment as if the covered employee were entitled to rest and recuperation leave under subsection (b). .\n##### (b) Technical and conforming amendment\nThe table of sections for subchapter II of chapter 63 of title 5, United States Code, is amended by inserting after the item relating to section 6329d the following:\n6329e. Rest and recuperation leave for employees engaged in wildland firefighting. .\n#### 5. Transfer authority\nNotwithstanding section 40803(c)(2) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(2) ), not more than $5,000,000 of the unobligated balances of amounts made available under the heading Wildland Fire Management under the heading Forest Service under the heading Department of Agriculture in title VI of division J of that Act ( Public Law 117\u201358 ; 135 Stat. 1410) pursuant to section 40803(c)(2)(B) of that Act ( 16 U.S.C. 6592(c)(2)(B) ) may, as necessary to continue uninterrupted the Federal wildland firefighter base salary increase described in section 40803(d)(4)(B) of that Act ( 16 U.S.C. 6592(d)(4)(B) ), be transferred to and merged with the amounts made available under the heading Wildland Fire Management under the heading Department-wide programs under the heading Department of the Interior in title VI of division J of that Act ( Public Law 117\u201358 ; 135 Stat. 1393).",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "1943",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Wildland Firefighter Paycheck Protection Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Employee leave",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T15:58:59Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-03-13T15:58:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:11:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s135",
          "measure-number": "135",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s135v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Wildland Firefighter Paycheck Protection Act of 2025</strong></p><p>This bill establishes specialized pay for federal wildland firefighters.</p><p>Specifically, the bill provides for a specialized pay schedule for wildland firefighters in the Forest Service and the Department of the Interior. The specialized pay schedule is based on the General Schedule, increased by a specified percentage depending on the position grade (the higher the grade, the lower the percentage adjustment).</p><p>The bill also provides for specialized premium pay for wildland firefighters who respond to certain prolonged fire incidents (i.e., those that are not contained within 36 hours). It\u00a0also provides for paid rest and recuperation leave in conjunction with such responses.\u00a0</p>"
        },
        "title": "Wildland Firefighter Paycheck Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s135.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wildland Firefighter Paycheck Protection Act of 2025</strong></p><p>This bill establishes specialized pay for federal wildland firefighters.</p><p>Specifically, the bill provides for a specialized pay schedule for wildland firefighters in the Forest Service and the Department of the Interior. The specialized pay schedule is based on the General Schedule, increased by a specified percentage depending on the position grade (the higher the grade, the lower the percentage adjustment).</p><p>The bill also provides for specialized premium pay for wildland firefighters who respond to certain prolonged fire incidents (i.e., those that are not contained within 36 hours). It\u00a0also provides for paid rest and recuperation leave in conjunction with such responses.\u00a0</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s135"
    },
    "title": "Wildland Firefighter Paycheck Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wildland Firefighter Paycheck Protection Act of 2025</strong></p><p>This bill establishes specialized pay for federal wildland firefighters.</p><p>Specifically, the bill provides for a specialized pay schedule for wildland firefighters in the Forest Service and the Department of the Interior. The specialized pay schedule is based on the General Schedule, increased by a specified percentage depending on the position grade (the higher the grade, the lower the percentage adjustment).</p><p>The bill also provides for specialized premium pay for wildland firefighters who respond to certain prolonged fire incidents (i.e., those that are not contained within 36 hours). It\u00a0also provides for paid rest and recuperation leave in conjunction with such responses.\u00a0</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s135"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s135is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Wildland Firefighter Paycheck Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildland Firefighter Paycheck Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to provide for special base rates of pay for wildland firefighters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:24Z"
    }
  ]
}
```
