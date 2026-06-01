# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/129
- Title: No Tax on Tips Act
- Congress: 119
- Bill type: S
- Bill number: 129
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-05-27T08:05:17Z
- Update date including text: 2025-05-27T08:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2025-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2993-2995; text: CR S2993-2994)
- 2025-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-05-20 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2025-05-20 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2025-05-23 - Floor: Message on Senate action sent to the House.
- 2025-05-26 09:02:36 - Floor: Received in the House.
- 2025-05-26 09:16:09 - Floor: Held at the desk.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2025-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2993-2995; text: CR S2993-2994)
- 2025-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-05-20 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2025-05-20 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2025-05-23 - Floor: Message on Senate action sent to the House.
- 2025-05-26 09:02:36 - Floor: Received in the House.
- 2025-05-26 09:16:09 - Floor: Held at the desk.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/129",
    "number": "129",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Tax on Tips Act",
    "type": "S",
    "updateDate": "2025-05-27T08:05:17Z",
    "updateDateIncludingText": "2025-05-27T08:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-05-26",
      "actionTime": "09:16:09",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-05-26",
      "actionTime": "09:02:36",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2993-2995; text: CR S2993-2994)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
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
        "item": [
          {
            "date": "2025-05-20T20:13:07Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-16T20:23:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s129is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 129\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Cruz (for himself, Mr. Daines , Ms. Rosen , Mr. Ricketts , Ms. Cortez Masto , Mr. Hawley , Mr. Scott of Florida , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate the application of the income tax on qualified tips through a deduction allowed to all individual taxpayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Tax on Tips Act .\n#### 2. Deduction for qualified tips\n##### (a) In general\n**(1) Deduction allowed**\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Qualified tips (a) In general There shall be allowed as a deduction an amount equal to the qualified tips received during the taxable year that are included on statements furnished to the employer pursuant to section 6053(a). (b) Maximum deduction The deduction allowed by subsection (a) for any taxpayer for the taxable year shall not exceed $25,000. (c) Qualified tips For purposes of this section\u2014 (1) In general The term qualified tip means any cash tip received by an individual in the course of such individual's employment in an occupation which traditionally and customarily received tips on or before December 31, 2023, as provided by the Secretary. (2) Exclusion for certain employees Such term shall not include any amount received by an individual in the course of employment by an employer if such individual had, for the preceding taxable year, compensation (within the meaning of section 414(q))(4) from such employer in excess of the amount in effect under section 414(q)(1)(B)(i). .\n**(2) Published list of occupations traditionally receiving tips**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall publish a list of occupations which traditionally and customarily received tips on or before December 31, 2023, for purposes of section 224(c)(1) of the Internal Revenue Code of 1986 (as added by paragraph (1)).\n**(3) Conforming amendment**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Qualified tips. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (3), by striking the period at the end of paragraph (4) and inserting and , and by adding at the end the following new paragraph:\n(5) the deduction provided in section 224. .\n##### (c) Non-Application of certain limitations for itemizers\n**(1) Deduction not treated as a miscellaneous itemized deduction**\nSection 67(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (11), by striking the period at the end of paragraph (12) and inserting , and , and by adding at the end the following new paragraph:\n(13) the deduction under section 224 (relating to qualified tips). .\n**(2) Deduction not taken into account under overall limitation**\nSection 68(c) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) the deduction under section 224 (relating to qualified tips). .\n##### (d) Withholding\nThe Secretary of the Treasury (or the Secretary's delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account the deduction allowed under section 224 of such Code (as added by this Act).\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Extension of credit for portion of employer social security taxes paid with respect to employee tips to beauty service establishments\n##### (a) Extension of tip credit to beauty service business\n**(1) In general**\nSection 45B(b)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Application only to certain lines of business In applying paragraph (1) there shall be taken into account only tips received from customers or clients in connection with the following services: (A) The providing, delivering, or serving of food or beverages for consumption, if the tipping of employees delivering or serving food or beverages by customers is customary. (B) The providing of beauty services to a customer or client if the tipping of employees providing such services is customary. .\n**(2) Beauty service defined**\nSection 45B of such Code is amended by adding at the end the following new subsection:\n(e) Beauty service For purposes of this section, the term beauty service means any of the following: (1) Barbering and hair care. (2) Nail care. (3) Esthetics. (4) Body and spa treatments. .\n##### (b) Credit determined with respect to minimum wage in effect\nSection 45B(b)(1)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking as in effect on January 1, 2007, and ; and\n**(2)**\nby inserting , and in the case of food or beverage establishments, as in effect on January 1, 2007 after without regard to section 3(m) of such Act .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s129es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 129\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Internal Revenue Code of 1986 to eliminate the application of the income tax on qualified tips through a deduction allowed to all individual taxpayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Tax on Tips Act .\n#### 2. Deduction for qualified tips\n##### (a) In general\n**(1) Deduction allowed**\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Qualified tips (a) In general There shall be allowed as a deduction an amount equal to the qualified tips received during the taxable year that are included on statements furnished to the employer pursuant to section 6053(a). (b) Maximum deduction The deduction allowed by subsection (a) for any taxpayer for the taxable year shall not exceed $25,000. (c) Qualified tips For purposes of this section\u2014 (1) In general The term qualified tip means any cash tip received by an individual in the course of such individual's employment in an occupation which traditionally and customarily received tips on or before December 31, 2023, as provided by the Secretary. (2) Exclusion for certain employees Such term shall not include any amount received by an individual in the course of employment by an employer if such individual had, for the preceding taxable year, compensation (within the meaning of section 414(q))(4) from such employer in excess of the amount in effect under section 414(q)(1)(B)(i). .\n**(2) Published list of occupations traditionally receiving tips**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall publish a list of occupations which traditionally and customarily received tips on or before December 31, 2023, for purposes of section 224(c)(1) of the Internal Revenue Code of 1986 (as added by paragraph (1)).\n**(3) Conforming amendment**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Qualified tips. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (3), by striking the period at the end of paragraph (4) and inserting and , and by adding at the end the following new paragraph:\n(5) the deduction provided in section 224. .\n##### (c) Non-Application of certain limitations for itemizers\n**(1) Deduction not treated as a miscellaneous itemized deduction**\nSection 67(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (11), by striking the period at the end of paragraph (12) and inserting , and , and by adding at the end the following new paragraph:\n(13) the deduction under section 224 (relating to qualified tips). .\n**(2) Deduction not taken into account under overall limitation**\nSection 68(c) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) the deduction under section 224 (relating to qualified tips). .\n##### (d) Withholding\nThe Secretary of the Treasury (or the Secretary's delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account the deduction allowed under section 224 of such Code (as added by this Act).\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Extension of credit for portion of employer social security taxes paid with respect to employee tips to beauty service establishments\n##### (a) Extension of tip credit to beauty service business\n**(1) In general**\nSection 45B(b)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Application only to certain lines of business In applying paragraph (1) there shall be taken into account only tips received from customers or clients in connection with the following services: (A) The providing, delivering, or serving of food or beverages for consumption, if the tipping of employees delivering or serving food or beverages by customers is customary. (B) The providing of beauty services to a customer or client if the tipping of employees providing such services is customary. .\n**(2) Beauty service defined**\nSection 45B of such Code is amended by adding at the end the following new subsection:\n(e) Beauty service For purposes of this section, the term beauty service means any of the following: (1) Barbering and hair care. (2) Nail care. (3) Esthetics. (4) Body and spa treatments. .\n##### (b) Credit determined with respect to minimum wage in effect\nSection 45B(b)(1)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking as in effect on January 1, 2007, and ; and\n**(2)**\nby inserting , and in the case of food or beverage establishments, as in effect on January 1, 2007 after without regard to section 3(m) of such Act .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "482",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Tax on Tips Act",
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
            "updateDate": "2025-05-22T15:26:23Z"
          },
          {
            "name": "Food industry and services",
            "updateDate": "2025-05-22T15:26:37Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-05-22T15:26:16Z"
          },
          {
            "name": "Service industries",
            "updateDate": "2025-05-22T15:26:45Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-05-22T15:26:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-25T19:50:13Z"
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
          "measure-id": "id119s129",
          "measure-number": "129",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s129v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>"
        },
        "title": "No Tax on Tips Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s129.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s129"
    },
    "title": "No Tax on Tips Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s129"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s129is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s129es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No Tax on Tips Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-24T11:03:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "No Tax on Tips Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-05-21T04:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax on Tips Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to eliminate the application of the income tax on qualified tips through a deduction allowed to all individual taxpayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:19Z"
    }
  ]
}
```
