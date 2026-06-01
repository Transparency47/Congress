# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/482?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/482
- Title: No Tax on Tips Act
- Congress: 119
- Bill type: HR
- Bill number: 482
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-10-07T08:05:33Z
- Update date including text: 2025-10-07T08:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/482",
    "number": "482",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No Tax on Tips Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:33Z",
    "updateDateIncludingText": "2025-10-07T08:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "TX"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NV"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "FL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "LA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NC"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr482ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 482\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Buchanan (for himself, Mr. Donalds , Mr. Van Orden , and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate the application of the income tax on qualified tips through a deduction allowed to all individual taxpayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Tax on Tips Act .\n#### 2. Deduction for qualified tips\n##### (a) In general\n**(1) Deduction allowed**\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Qualified tips (a) In general There shall be allowed as a deduction an amount equal to the qualified tips received during the taxable year that are included on statements furnished to the employer pursuant to section 6053(a). (b) Maximum deduction The deduction allowed by subsection (a) for any taxpayer for the taxable year shall not exceed $25,000. (c) Qualified tips For purposes of this section\u2014 (1) In general The term qualified tip means any cash tip received by an individual in the course of such individual's employment in an occupation which traditionally and customarily received tips on or before December 31, 2023, as provided by the Secretary. (2) Exclusion for certain employees Such term shall not include any amount received by an individual in the course of employment by an employer if such individual had, for the preceding taxable year, compensation (within the meaning of section 414(q))(4) from such employer in excess of the amount in effect under section 414(q)(1)(B)(i). .\n**(2) Published list of occupations traditionally receiving tips**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall publish a list of occupations which traditionally and customarily received tips on or before December 31, 2023, for purposes of section 224(c)(1) of the Internal Revenue Code of 1986 (as added by paragraph (1)).\n**(3) Conforming amendment**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Qualified tips. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (3), by striking the period at the end of paragraph (4) and inserting and , and by adding at the end the following new paragraph:\n(5) the deduction provided in section 224. .\n##### (c) Non-Application of certain limitations for itemizers\n**(1) Deduction not treated as a miscellaneous itemized deduction**\nSection 67(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (11), by striking the period at the end of paragraph (12) and inserting , and , and by adding at the end the following new paragraph:\n(13) the deduction under section 224 (relating to qualified tips). .\n**(2) Deduction not taken into account under overall limitation**\nSection 68(c) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) the deduction under section 224 (relating to qualified tips). .\n##### (d) Withholding\nThe Secretary of the Treasury (or the Secretary's delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account the deduction allowed under section 224 of such Code (as added by this Act).\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Extension of credit for portion of employer social security taxes paid with respect to employee tips to beauty service establishments\n##### (a) Extension of tip credit to beauty service business\n**(1) In general**\nSection 45B(b)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Application only to certain lines of business In applying paragraph (1) there shall be taken into account only tips received from customers or clients in connection with the following services: (A) The providing, delivering, or serving of food or beverages for consumption, if the tipping of employees delivering or serving food or beverages by customers is customary. (B) The providing of beauty services to a customer or client if the tipping of employees providing such services is customary. .\n**(2) Beauty service defined**\nSection 45B of such Code is amended by adding at the end the following new subsection:\n(e) Beauty service For purposes of this section, the term beauty service means any of the following: (1) Barbering and hair care. (2) Nail care. (3) Esthetics. (4) Body and spa treatments. .\n##### (b) Credit determined with respect to minimum wage in effect\nSection 45B(b)(1)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking as in effect on January 1, 2007, and ; and\n**(2)**\nby inserting , and in the case of food or beverage establishments, as in effect on January 1, 2007 after without regard to section 3(m) of such Act .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-16",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-05-22T15:27:34Z"
          },
          {
            "name": "Food industry and services",
            "updateDate": "2025-05-22T15:27:34Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-05-22T15:27:34Z"
          },
          {
            "name": "Service industries",
            "updateDate": "2025-05-22T15:27:34Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-05-22T15:27:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-19T20:26:15Z"
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
          "measure-id": "id119hr482",
          "measure-number": "482",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr482v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>"
        },
        "title": "No Tax on Tips Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr482.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr482"
    },
    "title": "No Tax on Tips Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax on Tips Act</strong></p><p>This bill establishes a new tax deduction of up to $25,000 for tips, subject to limitations. The bill also expands the business tax credit for the portion of payroll taxes an employer pays on certain tips to include payroll taxes paid on tips received in connection with certain beauty services.</p><p>Under the bill, the new tax deduction for tips is limited to cash tips (1) received by an employee during the course of employment in an occupation that customarily receives tips, and (2) reported by the employee to the employer for purposes of withholding payroll taxes. (Under current law, an employee is required to report tips exceeding $20 per month to their employer.)</p><p>Further, an employee with compensation exceeding a specified threshold ($160,000\u00a0in 2025 and adjusted annually for inflation) in the prior tax year may not claim the new tax deduction for tips.</p><p>Finally, the bill expands the business tax credit for the portion of payroll taxes that an employer pays on certain tips to include payroll taxes paid on tips received in connection with barbering and hair care, nail care, esthetics, and body and spa treatments. (Under current law, an employer is allowed a business tax credit for the amount of payroll taxes paid on certain tips received by an employee in connection with providing, delivering, or serving food or beverages.)\u00a0\u00a0</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr482"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr482ih.xml"
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
      "title": "No Tax on Tips Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax on Tips Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the application of the income tax on qualified tips through a deduction allowed to all individual taxpayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T11:03:30Z"
    }
  ]
}
```
