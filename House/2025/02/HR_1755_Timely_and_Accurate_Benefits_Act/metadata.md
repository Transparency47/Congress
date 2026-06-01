# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1755?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1755
- Title: Timely and Accurate Benefits Act
- Congress: 119
- Bill type: HR
- Bill number: 1755
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-22T19:05:13Z
- Update date including text: 2026-05-22T19:05:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1755",
    "number": "1755",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000480",
        "district": "4",
        "firstName": "William",
        "fullName": "Rep. Timmons, William R. [R-SC-4]",
        "lastName": "Timmons",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Timely and Accurate Benefits Act",
    "type": "HR",
    "updateDate": "2026-05-22T19:05:13Z",
    "updateDateIncludingText": "2026-05-22T19:05:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
            "date": "2026-04-29T13:07:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T14:05:45Z",
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
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
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
      "sponsorshipDate": "2025-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1755ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1755\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Timmons (for himself, Ms. Greene of Georgia , and Mr. Fallon ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require an income verification platform for certain Federal benefit funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Timely and Accurate Benefits Act .\n#### 2. Requirements of States; Enhanced Income Verification Platform Required\nTo be eligible to receive Federal funds for a covered Federal benefit program, a State, not later than 1 year after the date of the enactment of this Act, shall procure, contract, and use an Enhanced Income Verification Platform.\n#### 3. Definitions\nIn this Act:\n**(1) Covered Federal benefit program**\nThe term covered Federal benefit program means any program administered by the Federal government, or by a State or local government using Federal funds, in which eligibility for benefits, or the amount of benefits, is determined, in whole or in part, based on the income of an individual or household.\n**(2) Enhanced Gross Income**\nThe term enhanced gross income means\u2014\n**(A)**\nwages, salaries, tips included and not included on pay stubs, and other compensation from all forms of employment, including traditional W\u20132 employment not provided by existing data sources, contract work, self-employment, and participation in the gig economy;\n**(B)**\nunemployment compensation;\n**(C)**\nSocial Security benefits, including retirement, disability, and survivor benefits;\n**(D)**\nSupplemental Security Income (SSI) payments;\n**(E)**\ninterest and dividends;\n**(F)**\nshort-term and long-term rental income;\n**(G)**\nroyalties;\n**(H)**\nchild support and alimony payments received;\n**(I)**\ncash assistance from government programs;\n**(J)**\nregular or recurring gifts or contributions from individuals or organizations;\n**(K)**\ndistributions from trusts or estates;\n**(L)**\nany other source of income, whether taxable or non-taxable, that is available to the individual or household to meet their needs, as determined by the Secretary; and\n**(M)**\nother income identified and verified through consumer-permissioned direct access to deposit account transaction data.\n**(3) Enhanced Income Verification Platform**\nThe term Enhanced Income Verification Platform means\u2014\n**(A)**\nservices incorporating automated, real-time data matching and analytics to proactively identify and verify potential instances of unreported or underreported enhanced gross income, inconsistent income reporting, or other indicators of potential ineligibility or improper payments;\n**(B)**\nreceiving and analyzing applicant-permissioned deposit account transactional data that identifies and verifies sources of enhanced gross income not currently obtained through existing data sources that provide for payroll, new-hire and latent State and Federal tax data, with the option for the claimant to review and attest to the accuracy of the data; and\n**(C)**\nthe ability to identify and consolidate overlapping data to avoid double-counting of financial records.\n**(4) State**\nThe term State means each of the several States, the District of Columbia, and each territory and possession of the United States.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-05-19",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1807",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Timely and Accurate Benefits Act",
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
            "name": "Intergovernmental relations",
            "updateDate": "2026-05-22T19:05:13Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-05-22T19:05:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-21T13:59:01Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1755ih.xml"
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
      "title": "Timely and Accurate Benefits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Timely and Accurate Benefits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require an income verification platform for certain Federal benefit funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:23Z"
    }
  ]
}
```
