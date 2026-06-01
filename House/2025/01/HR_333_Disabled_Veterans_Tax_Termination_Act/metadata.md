# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/333
- Title: Disabled Veterans Tax Termination Act
- Congress: 119
- Bill type: HR
- Bill number: 333
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-06-27T08:06:18Z
- Update date including text: 2025-06-27T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/333",
    "number": "333",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B000490",
        "district": "2",
        "firstName": "Sanford",
        "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
        "lastName": "Bishop",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Disabled Veterans Tax Termination Act",
    "type": "HR",
    "updateDate": "2025-06-27T08:06:18Z",
    "updateDateIncludingText": "2025-06-27T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:36:50Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-13T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "RI"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 333\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Bishop introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to permit retired members of the Armed Forces who have a service-connected disability rated less than 50 percent to receive concurrent payment of both retired pay and veterans disability compensation, to extend eligibility for concurrent receipt to chapter 61 disability retirees with less than 20 years of service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disabled Veterans Tax Termination Act .\n#### 2. Concurrent receipt of both retired pay and veterans\u2019 disability compensation for military retirees with compensable service-connected disabilities\n##### (a) Inclusion of Retirees With Service-Connected Disabilities Rated Less Than 50 Percent\nSection 1414(a) of title 10, United States Code, is amended\u2014\n**(1)**\nby striking Compensation in the subsection heading and all that follows through Subject and inserting Compensation .\u2014Subject ;\n**(2)**\nby striking qualifying service-connected disability and inserting service-connected disability ; and\n**(3)**\nby striking paragraph (2).\n##### (b) Inclusion of disability retirees with less than 20 years of service\nSection 1414(b) of title 10, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking member retired and inserting qualified retiree who is retired ; and\n**(2)**\nby striking paragraph (2) and inserting the following new paragraph:\n(2) Disability retirees with less than 20 years of service The retired pay of a qualified retiree who is retired under chapter 61 of this title with fewer than 20 years of creditable service is subject to reduction under sections 5304 and 5305 of title 38, but only by the amount (if any) by which the amount of the member\u2019s retired pay under such chapter exceeds the amount equal to 2\u00bd percent of the member\u2019s years of creditable service multiplied by the member\u2019s retired pay base under section 1406(b)(1) or 1407 of this title, whichever is applicable to the member. .\n##### (c) Conforming amendments reflecting end of Concurrent Receipt phase-In period\nSection 1414 of title 10, United States Code, is further amended\u2014\n**(1)**\nin subsection (a), as amended by subsection (a) of this section, by striking the final sentence;\n**(2)**\nby striking subsection (c) and redesignating subsections (d) and (e) as subsections (c) and (d), respectively; and\n**(3)**\nin subsection (d), as so redesignated, by striking paragraphs (3) and (4).\n##### (d) Clerical Amendments\n**(1) Section heading**\nThe heading for section 1414 of title 10, United States Code, is amended to read as follows:\n1414. Members eligible for retired pay who are also eligible for veterans\u2019 disability compensation: concurrent payment of retired pay and disability compensation .\n**(2) Table of sections**\nThe item relating to such section in the table of sections at the beginning of chapter 71 of title 10, United States Code, is amended to read as follows:\n1414. Members eligible for retired pay who are also eligible for veterans\u2019 disability compensation: concurrent payment of retired pay and disability compensation. .\n##### (e) Conforming amendment reflecting subsection redesignation\nSection 1413a(f) of title 10, United States Code, is amended by striking Subsection (d) and inserting Subsection (c) .\n##### (f) Effective Date\nThe amendments made by this section shall take effect on the first day of the first month beginning after the date of the enactment of this Act and shall apply to payments for months beginning on or after that date.",
      "versionDate": "2025-01-13",
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
            "name": "Disability and paralysis",
            "updateDate": "2025-03-05T16:10:49Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-05T16:10:49Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-05T16:10:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:44:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr333",
          "measure-number": "333",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr333v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disabled Veterans Tax Termination Act</strong></p> <p>This bill modifies provisions related to military retired pay. Specifically, the bill authorizes veterans with a service-connected disability of less than 50% to concurrently receive both retired pay and disability compensation. The bill also makes qualified disability retirees with less than 20 years of retirement-creditable service eligible for concurrent receipt, subject to specified reductions in retired pay.</p>"
        },
        "title": "Disabled Veterans Tax Termination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr333.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disabled Veterans Tax Termination Act</strong></p> <p>This bill modifies provisions related to military retired pay. Specifically, the bill authorizes veterans with a service-connected disability of less than 50% to concurrently receive both retired pay and disability compensation. The bill also makes qualified disability retirees with less than 20 years of retirement-creditable service eligible for concurrent receipt, subject to specified reductions in retired pay.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr333"
    },
    "title": "Disabled Veterans Tax Termination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disabled Veterans Tax Termination Act</strong></p> <p>This bill modifies provisions related to military retired pay. Specifically, the bill authorizes veterans with a service-connected disability of less than 50% to concurrently receive both retired pay and disability compensation. The bill also makes qualified disability retirees with less than 20 years of retirement-creditable service eligible for concurrent receipt, subject to specified reductions in retired pay.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr333"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr333ih.xml"
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
      "title": "Disabled Veterans Tax Termination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disabled Veterans Tax Termination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to permit retired members of the Armed Forces who have a service-connected disability rated less than 50 percent to receive concurrent payment of both retired pay and veterans disability compensation, to extend eligibility for concurrent receipt to chapter 61 disability retirees with less than 20 years of service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T05:18:28Z"
    }
  ]
}
```
