# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6086?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6086
- Title: Aviation Funding Solvency Act
- Congress: 119
- Bill type: HR
- Bill number: 6086
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-05-14T08:07:34Z
- Update date including text: 2026-05-14T08:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Aviation.
- 2025-12-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-18 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-12-18 - Committee: Subcommittee on Aviation Discharged
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-19 - Committee: Referred to the Subcommittee on Aviation.
- 2025-12-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-18 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-12-18 - Committee: Subcommittee on Aviation Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6086",
    "number": "6086",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000546",
        "district": "6",
        "firstName": "Sam",
        "fullName": "Rep. Graves, Sam [R-MO-6]",
        "lastName": "Graves",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Aviation Funding Solvency Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:34Z",
    "updateDateIncludingText": "2026-05-14T08:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
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
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Aviation Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
            "date": "2025-12-18T18:50:35Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-18T18:50:29Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-11-18T15:06:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-19T17:37:40Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IN"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "KS"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IN"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "IL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NV"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "CO"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "UT"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NE"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "TN"
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
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6086ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6086\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Graves (for himself, Mr. Larsen of Washington , Mr. Nehls , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo provide for funding from the Aviation Insurance Revolving Fund to continue certain Federal Aviation Administration activities in the event of a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Funding Solvency Act .\n#### 2. Temporary funding for Federal Aviation Administration in event of lapse in appropriation\n##### (a) In general\nSubject to subsection (c) and notwithstanding section 44307 of title 49, United States Code, if, with respect to the Federal Aviation Administration, an appropriation measure for a fiscal year is not enacted before the beginning of such fiscal year or a law making continuing appropriations is not in effect, covered amounts in the Aviation Insurance Revolving Fund shall be available to the Administrator for continuing programs, projects, or activities (including the costs of direct loans and loan guarantees) that were conducted with amounts made available for the Federal Aviation Administration, including for the accounts Federal Aviation Administration\u2014Operations and Federal Aviation Administration\u2014Facilities and Equipment in the preceding fiscal year\u2014\n**(1)**\nin the corresponding appropriation Act for such preceding fiscal year; or\n**(2)**\nif the corresponding appropriation bill for such preceding fiscal year did not become law, in a law making continuing appropriations for such preceding fiscal year.\n##### (b) Rate for operations\nAppropriations and funds made available, and authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be at a rate for operations not greater than\u2014\n**(1)**\nthe rate for operations provided for in the regular appropriation Act providing for such program, project, or activity for the preceding fiscal year; or\n**(2)**\nin the absence of such an Act, the rate for operations provided for such program, project, or activity pursuant to an Act making continuing appropriations for such preceding fiscal year.\n##### (c) Availability\nAppropriations and funds made available, and authority granted, for any fiscal year pursuant to this section for a program, project, or activity shall be available for the period beginning with the first day of a lapse in appropriations in any fiscal year and ending with the date on which either\u2014\n**(1)**\nthe applicable regular appropriation bill for such fiscal year becomes law (whether or not such law provides for such program, project, or activity); or\n**(2)**\nan Act making continuing appropriations becomes law.\n##### (d) Terms and conditions\nAn appropriation or funds made available, or authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be subject to the terms and conditions imposed with respect to the appropriation made or funds made available for the preceding fiscal year, or authority granted for such program, project, or activity under current law.\n##### (e) End of fiscal year\nIf this section is in effect at the end of a fiscal year, funding levels shall continue as provided in this section for the next fiscal year.\n##### (f) Expenditures and obligations\nExpenditures and obligations made for a program, project, or activity for any fiscal year pursuant to this section shall be charged to the applicable appropriation, fund, or authorization whenever a regular appropriation bill or a law making continuing appropriations until the end of a fiscal year providing for such program, project, or activity for such period becomes law.\n##### (g) Prioritization\nIf the Administrator determines that covered amounts are insufficient to continue all programs, projects, or activities described in subsection (a), the Administrator shall prioritize continuing the payment of compensation for employees of the Air Traffic Organization of the Administration using covered amounts.\n##### (h) Termination\nThis section shall not apply to a program, project, or activity during any portion of a fiscal year\u2014\n**(1)**\nif any other provision of law (other than an authorization of appropriations)\u2014\n**(A)**\nmakes an appropriation, makes funds available, or grants authority for such program, project, or activity to continue for such period; or\n**(B)**\nspecifically provides that no appropriation shall be made, no funds shall be made available, or no authority shall be granted for such program, project, or activity to continue for such period; or\n**(2)**\nif continuing such program, project, or activity under this section would cause the balance of the Aviation Insurance Revolving Fund to decrease to less than $1,000,000,000.\n##### (i) Covered amounts defined\nIn this section, the term covered amounts means the balance of the amounts in the Aviation Insurance Revolving Fund minus $1,000,000,000.\n#### 3. Extension of non-premium war risk insurance\nSection 44310 of title 49, United States Code, is amended\u2014\n**(1)**\nby striking (a) In general.\u2014 The and inserting The ; and\n**(2)**\nby striking subsection (b).",
      "versionDate": "2025-11-18",
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
            "name": "Appropriations",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2026-03-18T14:46:37Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-03-18T14:47:12Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2026-03-18T14:46:01Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-03-18T14:46:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-01T16:58:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-18",
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
          "measure-id": "id119hr6086",
          "measure-number": "6086",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2025-12-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6086v00",
            "update-date": "2025-12-18"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Aviation Funding Solvency Act</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a law making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Aviation Insurance Revolving Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.\u00a0The FAA may use the balance of the fund, minus $1 billion.\u00a0If the FAA\u00a0determines that the amounts from the fund\u00a0are insufficient to continue all programs, projects, or\u00a0activities, then the\u00a0FAA must prioritize compensation payments for employees of the Air Traffic Organization (e.g., air traffic controllers).</p><p>The bill provides the appropriations until the date on which either (1) specified appropriations legislation for the fiscal year becomes law, or (2) a bill making continuing appropriations\u00a0becomes law.</p><p>Finally, the bill permanently extends the FAA Non-premium War Risk Insurance Program. This program provides aviation insurance without a premium to eligible air carriers at the request of the Department of Defense or another federal agency, provided that the agency agrees to indemnify the FAA from all losses covered under the insurance. Eligible air carriers include those whose operations are under a federal contract and are necessary for national security or to carry out U.S. foreign policy.</p>"
        },
        "title": "Aviation Funding Solvency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6086.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Funding Solvency Act</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a law making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Aviation Insurance Revolving Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.\u00a0The FAA may use the balance of the fund, minus $1 billion.\u00a0If the FAA\u00a0determines that the amounts from the fund\u00a0are insufficient to continue all programs, projects, or\u00a0activities, then the\u00a0FAA must prioritize compensation payments for employees of the Air Traffic Organization (e.g., air traffic controllers).</p><p>The bill provides the appropriations until the date on which either (1) specified appropriations legislation for the fiscal year becomes law, or (2) a bill making continuing appropriations\u00a0becomes law.</p><p>Finally, the bill permanently extends the FAA Non-premium War Risk Insurance Program. This program provides aviation insurance without a premium to eligible air carriers at the request of the Department of Defense or another federal agency, provided that the agency agrees to indemnify the FAA from all losses covered under the insurance. Eligible air carriers include those whose operations are under a federal contract and are necessary for national security or to carry out U.S. foreign policy.</p>",
      "updateDate": "2025-12-18",
      "versionCode": "id119hr6086"
    },
    "title": "Aviation Funding Solvency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Funding Solvency Act</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a law making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Aviation Insurance Revolving Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.\u00a0The FAA may use the balance of the fund, minus $1 billion.\u00a0If the FAA\u00a0determines that the amounts from the fund\u00a0are insufficient to continue all programs, projects, or\u00a0activities, then the\u00a0FAA must prioritize compensation payments for employees of the Air Traffic Organization (e.g., air traffic controllers).</p><p>The bill provides the appropriations until the date on which either (1) specified appropriations legislation for the fiscal year becomes law, or (2) a bill making continuing appropriations\u00a0becomes law.</p><p>Finally, the bill permanently extends the FAA Non-premium War Risk Insurance Program. This program provides aviation insurance without a premium to eligible air carriers at the request of the Department of Defense or another federal agency, provided that the agency agrees to indemnify the FAA from all losses covered under the insurance. Eligible air carriers include those whose operations are under a federal contract and are necessary for national security or to carry out U.S. foreign policy.</p>",
      "updateDate": "2025-12-18",
      "versionCode": "id119hr6086"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6086ih.xml"
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
      "title": "Aviation Funding Solvency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Funding Solvency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for funding from the Aviation Insurance Revolving Fund to continue certain Federal Aviation Administration activities in the event of a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:19Z"
    }
  ]
}
```
