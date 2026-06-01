# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1998?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1998
- Title: Small Business Tax Fairness and Compliance Simplification Act
- Congress: 119
- Bill type: S
- Bill number: 1998
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-05T21:43:51Z
- Update date including text: 2025-12-05T21:43:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1998",
    "number": "1998",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Small Business Tax Fairness and Compliance Simplification Act",
    "type": "S",
    "updateDate": "2025-12-05T21:43:51Z",
    "updateDateIncludingText": "2025-12-05T21:43:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T22:33:50Z",
          "name": "Referred To"
        }
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MD"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1998is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1998\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mr. Scott of South Carolina (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to simplify reporting requirements, promote tax compliance, and reduce tip reporting compliance burdens in the beauty service industry.\n#### 1. Short title\nThis Act may be cited as the Small Business Tax Fairness and Compliance Simplification Act .\n#### 2. Extension of credit for portion of employer social security taxes paid with respect to employee tips to beauty service establishments\n##### (a) Extension of tip credit to beauty service business\n**(1) In general**\nSection 45B(b) of the Internal Revenue Code of 1986 is amended by striking paragraph (2) and inserting the following new paragraphs:\n(2) Application only to certain lines of business In applying paragraph (1) there shall be taken into account only tips received from customers or clients in connection with the following services: (A) The providing, delivering, or serving of food or beverages for consumption, if the tipping of employees delivering or serving food or beverages by customers is customary. (B) The providing of beauty services to a customer or client if the tipping of employees providing such services is customary. (3) Limitation on application to beauty services Paragraph (2)(B) shall not apply for purposes of determining the credit allowed under subsection (a) with respect to any taxpayer for any taxable year unless\u2014 (A) the aggregate amount of tips taken into account by such taxpayer as an employer for such taxable year under paragraph (1)(A) with respect to services described in paragraph (2)(B), exceeds (B) 15 percent of the taxpayer\u2019s gross receipts with respect to the services described in paragraph (2)(B) for such taxable year. .\n**(2) Beauty service defined**\nSection 45B of such Code is amended by adding at the end the following new subsection:\n(e) Beauty service For purposes of this section, the term beauty service means any of the following: (1) Barbering and hair care. (2) Nail care. (3) Esthetics. (4) Body and spa treatments. .\n##### (b) Credit determined with respect to minimum wage in effect\nSection 45B(b)(1)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking as in effect on January 1, 2007, and ; and\n**(2)**\nby inserting , and in the case of food or beverage establishments, as in effect on January 1, 2007 after without regard to section 3(m) of such Act .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Employer tip reporting safe harbor\n##### (a) In general\nSection 3121(q) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking so much as precedes of this chapter and inserting the following:\n(q) Tips included for both employee and employer taxes (1) In general For purposes ; and\n**(2)**\nby adding at the end the following new paragraph:\n(2) Tip program safe harbor In the case of an employer who employs one or more employees who receive tips in the course of such employment which are attributable to the performance of beauty services (as such term is defined in section 45B) are considered remuneration for such employment under this section, no IRS tip examination with respect to such employer shall be initiated (except in the case of a tip examination of a current or former employee) if the employer\u2014 (A) establishes an educational program regarding applicable laws relating to proper reporting of tips received by employees for\u2014 (i) new employees, which shall include both verbal explanation and written materials, and (ii) existing employees, which shall be conducted quarterly, (B) establishes procedures for tipped employees to provide monthly reporting of cash and charged services and related tip income of at least $20 under section 6053(a), (C) complies with all applicable Federal tax law requirements applicable to employers for purposes of filing returns, and collection and payment of taxes imposed, with respect to tip income received by employees, and (D) maintains employee records related to\u2014 (i) contact information for such employees, and (ii) gross receipts from any services subject to tipping, and charge receipts for such services, for a period of not less than 4 calendar years after the calendar year to which the records relate. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 4. Information reporting of income from space rentals in the beauty service industry\n##### (a) In general\nSubpart B of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986, as amended by section 334(d) of Public Law 117\u2013328 , is amended by adding at the end the following new section:\n6050AA. Returns relating to income from certain rentals of space in the beauty service industry (a) Requirement of reporting Any person who, in the course of a trade or business and for any calendar year, receives rental payments from two or more individuals providing beauty services (as defined in section 45B(e)) aggregating $600 or more each for the lease of space to provide such services to third-party patrons shall make the return described in subsection (b) with respect to each person from whom such rent was so received at such time as the Secretary may by regulations prescribe. (b) Return A return is described in this subsection if such return\u2014 (1) is in such form as the Secretary may prescribe, and (2) contains\u2014 (A) the name, address, and TIN of each person from whom a rental payment described in subsection (a) was received during the calendar year, (B) the aggregate amount of such payments received by such person during such calendar year and the date and amount of each such payment, and (C) such other information as the Secretary may require. (c) Statement To be furnished to persons with respect to whom information is required (1) In general Every person required to make a return under subsection (a) shall furnish to each person whose name is required to be set forth in such return a written statement showing\u2014 (A) the name, address, and phone number of the information contact of the person required to make such a return, and (B) the aggregate amount of payments to the person required to be shown on the return. (2) Furnishing of information The written statement required under paragraph (1) shall be furnished to the person on or before January 31 of the year following the calendar year for which the return under subsection (a) is required to be made. (d) Regulations and guidance The Secretary may prescribe such regulations and other guidance as may be appropriate or necessary to carry out the purpose of this subsection, including rules to prevent duplicative reporting of transactions. .\n##### (b) Clerical amendment\nThe table of sections for subchapter A of chapter 61 of such Code is amended by adding at the end the following new item:\nSec. 6050AA. Returns relating to income from certain rentals of space in the beauty service industry. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments made after December 31, 2025.",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-04-02",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2603",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Business Tax Fairness and Compliance Simplification Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-06-30T15:56:07Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1998is.xml"
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
      "title": "Small Business Tax Fairness and Compliance Simplification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Tax Fairness and Compliance Simplification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to simplify reporting requirements, promote tax compliance, and reduce tip reporting compliance burdens in the beauty service industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:24Z"
    }
  ]
}
```
