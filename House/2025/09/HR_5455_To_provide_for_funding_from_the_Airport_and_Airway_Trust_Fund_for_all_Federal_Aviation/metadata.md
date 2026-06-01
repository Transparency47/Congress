# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5455
- Title: Aviation Funding Stability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5455
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-05T21:31:21Z
- Update date including text: 2025-12-05T21:31:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-19 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-19 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5455",
    "number": "5455",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Aviation Funding Stability Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:31:21Z",
    "updateDateIncludingText": "2025-12-05T21:31:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-18",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-19T21:46:49Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-18T14:08:40Z",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "MI"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "OH"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NE"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "KS"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "AZ"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "UT"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "GU"
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
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5455ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5455\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Bean of Florida introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for funding from the Airport and Airway Trust Fund for all Federal Aviation.\n#### 1. Short title\nThis Act may be cited as the Aviation Funding Stability Act of 2025 .\n#### 2. Funding for the Federal Aviation Administration in the event of a lapse in appropriation\n##### (a) In general\nIf, with respect to the Federal Aviation Administration, an appropriation measure for a fiscal year is not enacted before the beginning of such fiscal year or a joint resolution making continuing appropriations is not in effect, amounts in the Airport and Airway Trust Fund not otherwise appropriated shall be available to the Administrator for continuing programs, projects, or activities (including the costs of direct loans and loan guarantees) that were conducted with amounts made available for the Federal Aviation Administration, including for the accounts Federal Aviation Administration\u2014Operations , Federal Aviation Administration\u2014Facilities and Equipment , Federal Aviation Administration\u2014Research, Engineering, and Development , and Federal Aviation Administration\u2014Grants-in-Aid for Airports in the preceding fiscal year\u2014\n**(1)**\nin the corresponding appropriation Act for such preceding fiscal year; or\n**(2)**\nif the corresponding appropriation bill for such preceding fiscal year did not become law, then in a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (b) Rate for operations\nAppropriations and funds made available, and authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be at a rate for operations not greater than\u2014\n**(1)**\nthe rate for operations provided for in the regular appropriation Act providing for such program, project, or activity for the preceding fiscal year; or\n**(2)**\nin the absence of such an Act, the rate for operations provided for such program, project, or activity pursuant to a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (c) Availability\nAppropriations and funds made available, and authority granted, for any fiscal year pursuant to this section for a program, project, or activity shall be available for the period beginning with the first day of a lapse in appropriations and ending with the earlier of\u2014\n**(1)**\nthe date on which\u2014\n**(A)**\nthe applicable regular appropriation bill for such fiscal year becomes law (whether or not such law provides for such program, project, or activity); or\n**(B)**\na joint resolution making continuing appropriations becomes law; or\n**(2)**\nthe date that is 30 days after the first day of a lapse in appropriations.\n##### (d) Terms and conditions\nAn appropriation or funds made available, or authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be subject to the terms and conditions imposed with respect to the appropriation made or funds made available for the preceding fiscal year, or authority granted for such program, project, or activity under applicable law on the first day of the applicable lapse in appropriations.\n##### (e) End of fiscal year\nIf this section is in effect at the end of a fiscal year, funding levels shall continue as provided in this section for the next fiscal year.\n##### (f) Expenditures and obligations\nExpenditures and obligations made for a program, project, or activity for any fiscal year pursuant to this section shall be charged to the applicable appropriation, fund, or authorization whenever a regular appropriation bill or a joint resolution making continuing appropriations until the end of a fiscal year providing for such program, project, or activity for such period becomes law.\n##### (g) Expenditure authority\nSection 9502(d)(1)(A) of the Internal Revenue Code of 1986 is amended by striking the semicolon at the end and inserting or Aviation Funding Stability Act of 2025 ; .\n##### (h) Termination\nThis section shall not apply to a program, project, or activity during any portion of a fiscal year if any other provision of law (other than an authorization of appropriations)\u2014\n**(1)**\nmakes an appropriation, makes funds available, or grants authority for such program, project, or activity to continue for such period; or\n**(2)**\nspecifically provides that no appropriation shall be made, no funds shall be made available, or no authority shall be granted for such program, project, or activity to continue for such period.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1045",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Aviation Funding Stability Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-19",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "5451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Aviation Funding Stability Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-10-03T14:24:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119hr5455",
          "measure-number": "5455",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-18",
          "originChamber": "HOUSE",
          "update-date": "2025-10-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5455v00",
            "update-date": "2025-10-03"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Aviation Funding Stability Act of 2025</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p><p>The bill provides the appropriations until the earlier of (1) the date on which the applicable regular appropriations bill for the fiscal year or a joint resolution making continuing appropriations becomes law, or (2) the date that is 30 days after the first day of a lapse in appropriations.\u00a0</p>"
        },
        "title": "Aviation Funding Stability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5455.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Funding Stability Act of 2025</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p><p>The bill provides the appropriations until the earlier of (1) the date on which the applicable regular appropriations bill for the fiscal year or a joint resolution making continuing appropriations becomes law, or (2) the date that is 30 days after the first day of a lapse in appropriations.\u00a0</p>",
      "updateDate": "2025-10-03",
      "versionCode": "id119hr5455"
    },
    "title": "Aviation Funding Stability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Funding Stability Act of 2025</strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities that were funded in the preceding fiscal year.</p><p>The bill provides the appropriations until the earlier of (1) the date on which the applicable regular appropriations bill for the fiscal year or a joint resolution making continuing appropriations becomes law, or (2) the date that is 30 days after the first day of a lapse in appropriations.\u00a0</p>",
      "updateDate": "2025-10-03",
      "versionCode": "id119hr5455"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5455ih.xml"
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
      "title": "Aviation Funding Stability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Funding Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for funding from the Airport and Airway Trust Fund for all Federal Aviation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:24Z"
    }
  ]
}
```
