# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5732?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5732
- Title: Keep Air Travel Safe Act
- Congress: 119
- Bill type: HR
- Bill number: 5732
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2026-05-16T08:07:41Z
- Update date including text: 2026-05-16T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-13 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-13 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5732",
    "number": "5732",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Keep Air Travel Safe Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:41Z",
    "updateDateIncludingText": "2026-05-16T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-13",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:30:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-13T20:15:39Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-10T16:30:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "LA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "OH"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "HI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NV"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TN"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OR"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "RI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "AL"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MO"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MN"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MI"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NJ"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CO"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "DE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MD"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5732ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5732\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mrs. Dingell (for herself and Ms. Brownley ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for funding for all Transportation Security Administration activities for a certain period in the event of a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep Air Travel Safe Act .\n#### 2. Funding for the Transportation Security Administration in the event of a lapse in appropriation\n##### (a) In general\nDuring any period in which there is a lapse in appropriations for the Transportation Security Administration, the Administrator of the Transportation Security Administration shall continue, using amounts described in subsection (g), all programs, projects, or activities (including the costs of direct loans and loan guarantees) of the Administration that were conducted with amounts made available for any account of the Administration in the preceding fiscal year\u2014\n**(1)**\nin the corresponding appropriation Act for such preceding fiscal year; or\n**(2)**\nif the corresponding appropriation bill for such preceding fiscal year did not become law, then in a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (b) Rate for operations\nAppropriations and funds made available, and authority granted, to continue a program, project, or activity for any fiscal year pursuant to this section shall be at a rate for operations not greater than\u2014\n**(1)**\nthe rate for operations provided for in the regular appropriation Act providing for such program, project, or activity for the preceding fiscal year; or\n**(2)**\nin the absence of such an Act, the rate for operations provided for such program, project, or activity pursuant to a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (c) Availability\nAppropriations and funds made available, and authority granted, for any fiscal year pursuant to this section for a program, project, or activity shall be available for the period beginning with the first day of a lapse in appropriations and ending with the earlier of\u2014\n**(1)**\nthe date on which\u2014\n**(A)**\nthe applicable regular appropriation bill for such fiscal year becomes law (whether or not such law provides for such program, project, or activity); or\n**(B)**\na joint resolution making continuing appropriations becomes law; or\n**(2)**\nthe date that is 180 days after the first day of a lapse in appropriations.\n##### (d) Terms and conditions\nAn appropriation or funds made available, or authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be subject to the terms and conditions imposed with respect to the appropriation made or funds made available for the preceding fiscal year, or authority granted for such program, project, or activity under applicable law on the first day of the applicable lapse in appropriations.\n##### (e) End of fiscal year\nIf this section is in effect at the end of a fiscal year, funding levels shall continue as provided in this section for the next fiscal year.\n##### (f) Amounts described\nThe amounts described in this subsection are the unobligated balances, as of the date of the enactment of this Act, of amounts made available under section 90003 of Public Law 119\u201321 (commonly referred to as the One Big Beautiful Bill Act ; 139 Stat. 358).",
      "versionDate": "2025-10-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-03T19:21:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-10",
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
          "measure-id": "id119hr5732",
          "measure-number": "5732",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-10",
          "originChamber": "HOUSE",
          "update-date": "2025-11-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5732v00",
            "update-date": "2025-11-03"
          },
          "action-date": "2025-10-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep Air Travel Safe Act</strong></p><p>This bill provides continuing appropriations for the Transportation Security Administration (TSA) during any period in which there is a lapse in appropriations for TSA.\u00a0It also requires the continuing appropriations to be funded using\u00a0certain unobligated funds that were provided to U.S. Immigration and Customs Enforcement by the One Big Beautiful Bill Act.\u00a0\u00a0</p><p>The bill provides the appropriations for TSA to continue all programs, projects, or activities (including the costs of direct loans and loan guarantees) that were funded in the preceding fiscal year.</p><p>The appropriations provided by this bill are available from the first day of a lapse in appropriations for\u00a0TSA until the earlier of</p><ul><li>the date on which the applicable regular appropriations bill for the fiscal year becomes law or a joint resolution making continuing appropriations becomes law, or\u00a0</li><li>the date that is 180 days after the first day of a lapse in appropriations.</li></ul>"
        },
        "title": "Keep Air Travel Safe Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5732.xml",
    "summary": {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Air Travel Safe Act</strong></p><p>This bill provides continuing appropriations for the Transportation Security Administration (TSA) during any period in which there is a lapse in appropriations for TSA.\u00a0It also requires the continuing appropriations to be funded using\u00a0certain unobligated funds that were provided to U.S. Immigration and Customs Enforcement by the One Big Beautiful Bill Act.\u00a0\u00a0</p><p>The bill provides the appropriations for TSA to continue all programs, projects, or activities (including the costs of direct loans and loan guarantees) that were funded in the preceding fiscal year.</p><p>The appropriations provided by this bill are available from the first day of a lapse in appropriations for\u00a0TSA until the earlier of</p><ul><li>the date on which the applicable regular appropriations bill for the fiscal year becomes law or a joint resolution making continuing appropriations becomes law, or\u00a0</li><li>the date that is 180 days after the first day of a lapse in appropriations.</li></ul>",
      "updateDate": "2025-11-03",
      "versionCode": "id119hr5732"
    },
    "title": "Keep Air Travel Safe Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Air Travel Safe Act</strong></p><p>This bill provides continuing appropriations for the Transportation Security Administration (TSA) during any period in which there is a lapse in appropriations for TSA.\u00a0It also requires the continuing appropriations to be funded using\u00a0certain unobligated funds that were provided to U.S. Immigration and Customs Enforcement by the One Big Beautiful Bill Act.\u00a0\u00a0</p><p>The bill provides the appropriations for TSA to continue all programs, projects, or activities (including the costs of direct loans and loan guarantees) that were funded in the preceding fiscal year.</p><p>The appropriations provided by this bill are available from the first day of a lapse in appropriations for\u00a0TSA until the earlier of</p><ul><li>the date on which the applicable regular appropriations bill for the fiscal year becomes law or a joint resolution making continuing appropriations becomes law, or\u00a0</li><li>the date that is 180 days after the first day of a lapse in appropriations.</li></ul>",
      "updateDate": "2025-11-03",
      "versionCode": "id119hr5732"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5732ih.xml"
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
      "title": "Keep Air Travel Safe Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Air Travel Safe Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for funding for all Transportation Security Administration activities for a certain period in the event of a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:11Z"
    }
  ]
}
```
