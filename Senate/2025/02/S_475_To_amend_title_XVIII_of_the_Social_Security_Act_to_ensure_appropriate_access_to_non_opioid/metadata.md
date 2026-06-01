# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/475?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/475
- Title: Alternatives to PAIN Act
- Congress: 119
- Bill type: S
- Bill number: 475
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/475",
    "number": "475",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Alternatives to PAIN Act",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
            "date": "2025-02-06T22:08:04Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T22:08:04Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MS"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "AR"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "GA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "WV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "LA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-10",
      "state": "ME"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "GA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "OR"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "MT"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NE"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CT"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "OH"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "KS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s475is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 475\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Tillis (for himself, Mr. Kelly , Mrs. Capito , Mr. Kaine , Mrs. Britt , Mrs. Shaheen , Mr. Budd , Mr. Coons , Mr. Cornyn , Mr. Booker , Mr. Moran , Mr. Bennet , Mr. Banks , Mr. Padilla , Mr. Daines , Mr. Warner , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to ensure appropriate access to non-opioid pain management drugs under part D of the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Alternatives to Prevent Addiction In the Nation Act or the Alternatives to PAIN Act .\n#### 2. Appropriate cost-sharing for qualifying non-opioid pain management drugs under Medicare part D\n##### (a) Medicare part D\nSection 1860D\u20132 of the Social Security Act ( 42 U.S.C. 1395w\u2013102 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), in the matter preceding clause (i), by striking paragraphs (8) and (9) and inserting paragraphs (8), (9), and (10) ;\n**(B)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking paragraphs (8) and (9) and inserting paragraphs (8), (9), and (10) ; and\n**(C)**\nby adding at the end the following new paragraph:\n(10) Treatment of cost-sharing for qualifying non-opioid pain management drugs (A) In general For plan years beginning on or after January 1, 2026, with respect to a covered part D drug that is a qualifying non-opioid pain management drug (as defined in subparagraph (B))\u2014 (i) the deductible under paragraph (1) shall not apply; and (ii) such drug shall be placed on the lowest cost-sharing tier, if any, for purposes of determining the maximum co-insurance or other cost-sharing for such drug. (B) Qualifying non-opioid pain management drugs In this paragraph, the term qualifying non-opioid pain management drug means a drug or biological product\u2014 (i) that has a label indication approved by the Food and Drug Administration to reduce postoperative pain or any other form of acute pain; (ii) that does not act upon the body\u2019s opioid receptors; (iii) for which there is no other drug or product that is\u2014 (I) rated as therapeutically equivalent (under the Food and Drug Administration\u2019s most recent publication of Approved Drug Products with Therapeutic Equivalence Evaluations ); and (II) sold or marketed in the United States; and (iv) for which the wholesale acquisition cost (as defined in section 1847A(c)(6)(B)), for a monthly supply does not exceed the monthly specialty-tier cost threshold as determined by the Secretary from time to time. ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(7) Treatment of cost-sharing for qualifying non-opioid pain management drugs The coverage is provided in accordance with subsection (b)(10). .\n##### (b) Conforming amendments to cost-Sharing for low-Income individuals\nSection 1860D\u201314(a) of the Social Security Act ( 42 U.S.C. 1395w\u2013114(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(D), in each of the clauses (ii) and (iii), by striking Subject to paragraph (6) and inserting Subject to paragraphs (6) and (7) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(7) Treatment of cost-sharing or deductible for qualifying non-opioid pain management drugs For plan years beginning on or after January 1, 2026, with respect to a covered part D drug that is a qualifying non-opioid pain management drug (as defined in section 1860D\u20132(b)(10)(B))\u2014 (A) the deductible under section 1860D\u20132(b)(1) shall not apply; and (B) such drug shall be placed on the lowest cost-sharing tier, if any, for purposes of determining the maximum co-insurance or other cost-sharing for such drug. .\n#### 3. Prohibition on the use of step therapy and prior authorization for qualifying non-opioid pain management drugs under medicare part D\nSection 1860D\u20134(c) of the Social Security Act ( 42 U.S.C. 1395w\u2013104 ) is amended\u2014\n**(1)**\nby redesignating paragraph (6), as added by section 50354 of division E of the Bipartisan Budget Act of 2018 ( Public Law 115\u2013123 ), as paragraph (7); and\n**(2)**\nby adding at the end the following paragraph:\n(8) Prohibition on use of step therapy and prior authorization for qualifying non-opioid pain management drugs (A) In general For plan years beginning on or after January 1, 2026, a prescription drug plan or an MA\u2013PD plan may not, with respect to a qualifying non-opioid pain management drug (as defined in section 1860D\u20132(b)(10)(B)) for which coverage is provided under such plan, impose any\u2014 (i) step therapy requirement under which an individual enrolled under such plan is required to use an opioid prior to receiving such drug; or (ii) prior authorization requirement. (B) Step therapy In this paragraph, the term step therapy means a drug therapy utilization management protocol or program that requires use of an alternative, preferred prescription drug or drugs before the plan approves coverage for the non-preferred drug therapy prescribed. (C) Prior authorization In this paragraph, the term prior authorization means any requirement to obtain approval from a plan prior to the furnishing of a drug. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1227",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Alternatives to PAIN Act",
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
            "name": "Drug therapy",
            "updateDate": "2025-06-13T18:47:14Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-13T18:47:09Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-06-13T18:46:58Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-06-13T18:47:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-06T13:20:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s475",
          "measure-number": "475",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s475v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Alternatives to Prevent Addiction In the Nation Act or the Alternatives to PAIN Act</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid pain management drugs.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>"
        },
        "title": "Alternatives to PAIN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s475.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Alternatives to Prevent Addiction In the Nation Act or the Alternatives to PAIN Act</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid pain management drugs.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s475"
    },
    "title": "Alternatives to PAIN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Alternatives to Prevent Addiction In the Nation Act or the Alternatives to PAIN Act</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid pain management drugs.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s475"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s475is.xml"
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
      "title": "Alternatives to PAIN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Alternatives to PAIN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Alternatives to Prevent Addiction In the Nation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to ensure appropriate access to non-opioid pain management drugs under part D of the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:05Z"
    }
  ]
}
```
