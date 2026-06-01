# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/236
- Title: Federal Employee Return to Work Act
- Congress: 119
- Bill type: HR
- Bill number: 236
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-03-18T15:43:54Z
- Update date including text: 2025-03-18T15:43:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/236",
    "number": "236",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Federal Employee Return to Work Act",
    "type": "HR",
    "updateDate": "2025-03-18T15:43:54Z",
    "updateDateIncludingText": "2025-03-18T15:43:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:03:10Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "CO"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "SC"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "MN"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KY"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MD"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NC"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr236ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 236\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Newhouse (for himself, Mr. Nunn of Iowa , Mr. Meuser , Mr. Weber of Texas , Ms. Boebert , Mr. Timmons , Mr. Ellzey , Mrs. Hinson , Mr. Collins , Ms. Malliotakis , Mr. Carter of Georgia , Mr. Finstad , and Mr. Fleischmann ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit certain telework employees from receiving certain annual adjustments to pay schedules, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Employee Return to Work Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered employee**\nThe term covered employee \u2014\n**(A)**\nmeans an employee who teleworks not fewer than 1 day, or in the case of an alternative work schedule, not less than 20 percent, a week; and\n**(B)**\ndoes not include an employee who\u2014\n**(i)**\nteleworks not fewer than 1 day a week; and\n**(ii)**\nis\u2014\n**(I)**\nis disabled and receives reasonable accommodations;\n**(II)**\na member of the Foreign Service of the United States;\n**(III)**\na Federal law enforcement officer;\n**(IV)**\na member of the Armed Forces on active duty; or\n**(V)**\nany other employee, the official worksite of whom is not described in section 531.605(a)(1) of title 5, Code of Federal Regulations (or any corresponding similar regulation or ruling).\n**(2) Employee**\nThe term employee has the meaning given the term in section 2105 of title 5, United States Code.\n**(3) Telework**\nThe term telework has the meaning given the term in section 6501 of title 5, United States Code.\n#### 3. Annual adjustments to pay schedules\nNo covered employee may receive an annual adjustment under section 5303 of title 5, United States Code.\n#### 4. Pay localities\nEach covered employee shall be paid at the rate of basic pay under the applicable grade and step for that employee under the locality pay area designated as Rest of U.S. \u2014\n**(1)**\nas of the date on which the employee becomes a covered employee; and\n**(2)**\nwhich shall not be adjusted under section 5304 of title 5, United States Code.\n#### 5. Effective date\nThis Act shall take effect on the first day of the first full fiscal year beginning after the date of enactment of this Act.",
      "versionDate": "2025-01-07",
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
        "actionDate": "2025-01-07",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "27",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Employee Return to Work Act",
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
            "name": "Commuting",
            "updateDate": "2025-03-05T16:06:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-05T16:07:01Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T16:06:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:04:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr236",
          "measure-number": "236",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr236v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p><p>\u00a0</p>"
        },
        "title": "Federal Employee Return to Work Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr236.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr236"
    },
    "title": "Federal Employee Return to Work Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr236"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr236ih.xml"
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
      "title": "Federal Employee Return to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Employee Return to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit certain telework employees from receiving certain annual adjustments to pay schedules, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:18:26Z"
    }
  ]
}
```
