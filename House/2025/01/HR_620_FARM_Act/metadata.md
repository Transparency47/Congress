# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/620
- Title: FARM Act
- Congress: 119
- Bill type: HR
- Bill number: 620
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-04-09T15:17:13Z
- Update date including text: 2026-04-09T15:17:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/620",
    "number": "620",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FARM Act",
    "type": "HR",
    "updateDate": "2026-04-09T15:17:13Z",
    "updateDateIncludingText": "2026-04-09T15:17:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:13:09Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "GU"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "KS"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "IA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "IN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
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
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "SD"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "AR"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MS"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "UT"
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
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OH"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NH"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-06",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr620ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 620\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Jackson of Texas (for himself, Mr. Sessions , Mr. Panetta , Mr. Vicente Gonzalez of Texas , Mr. Moylan , Mr. Zinke , Mr. Estes , Mr. Finstad , Mrs. Hinson , Mrs. Miller of Illinois , Mr. Costa , Mr. Fallon , Mr. Messmer , Mr. Rose , Mr. Weber of Texas , Mr. Johnson of South Dakota , Mr. Newhouse , and Mr. Crawford ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Defense Production Act of 1950 to prevent harm and disruption to the United States agriculture industry by protecting against foreign influence over agriculture production and supply chains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Adversary Risk Management Act or the FARM Act .\n#### 2. United States agriculture included in Committee on Foreign Investment in the United States\n##### (a) Agriculture representative\nSection 721(k)(2) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(k)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (H), (I), and (J) as subparagraphs (I), (J), and (K), respectively; and\n**(2)**\nby inserting after subparagraph (G) the following:\n(H) The Secretary of Agriculture. .\n##### (b) Review of agriculture investments by foreign entities\nSection 721(a)(4) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) any transaction described in subparagraph (B)(vi) that is proposed, pending, or completed on or after the date of the enactment of the Foreign Adversary Risk Management Act . ; and\n**(2)**\nin subparagraph (B), by adding at the end the following:\n(vi) Any transaction, merger, acquisition, transfer, agreement, takeover, or other arrangement that could result in foreign control of any United States business that is engaged in agriculture and uses agricultural products (as defined in the first section of the Act of July 2, 1926 (44 Stat. 802, chapter 725; 7 U.S.C. 451 )). .\n##### (c) Agricultural supply chains included in critical infrastructure\nSection 721(a)(5) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(5) ) is amended\u2014\n**(1)**\nby striking critical infrastructure means and inserting the following:\ncritical infrastructure \u2014 (i) means ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(ii) includes, subject to regulations prescribed by the Committee, agricultural systems and supply chains. .\n##### (d) Agricultural supply chains included as critical technologies\nSection 721(a)(6)(A) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(6)(A) ) is amended by adding at the end the following:\n(vii) Agricultural supply chains used for agricultural products (as defined in the first section of the Act of July 2, 1926 (44 Stat. 802, chapter 725; 7 U.S.C. 451 )). .\n#### 3. Reports on investments by foreign countries in United States agriculture industry\nNot later than one year after the date of the enactment of this Act and annually thereafter, the Secretary of Agriculture and the Comptroller General of the United States shall each\u2014\n**(1)**\nconduct an analysis of foreign influence in the United States agriculture industry; and\n**(2)**\nsubmit to Congress a report that includes a summary of\u2014\n**(A)**\nforeign investments in the United States agriculture industry;\n**(B)**\nthe potential for foreign investment to undermine United States agriculture production and agricultural supply chains;\n**(C)**\nthe largest international threats for increased foreign control of, and investment in, the United States agriculture sector; and\n**(D)**\nagriculture-related espionage and theft techniques used by foreign governments, including any attempts to target United States agricultural intellectual property, innovation, research and development, cost or pricing data, or internal strategy documents.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-01-22",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "179",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FARM Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T15:37:00Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-03-13T15:37:00Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-13T15:37:00Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T15:17:13Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-03-13T15:37:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-02-27T16:50:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr620",
          "measure-number": "620",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr620v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each annually analyze and report on foreign influence in the U.S. agricultural industry.</p>"
        },
        "title": "FARM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr620.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each annually analyze and report on foreign influence in the U.S. agricultural industry.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr620"
    },
    "title": "FARM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each annually analyze and report on foreign influence in the U.S. agricultural industry.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr620"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr620ih.xml"
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
      "title": "FARM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FARM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Adversary Risk Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Defense Production Act of 1950 to prevent harm and disruption to the United States agriculture industry by protecting against foreign influence over agriculture production and supply chains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:33Z"
    }
  ]
}
```
