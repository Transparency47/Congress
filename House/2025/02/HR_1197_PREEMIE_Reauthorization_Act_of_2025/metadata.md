# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1197
- Title: PREEMIE Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1197
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-03-25T08:06:03Z
- Update date including text: 2026-03-25T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1197",
    "number": "1197",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "PREEMIE Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:03Z",
    "updateDateIncludingText": "2026-03-25T08:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-11",
      "state": "GA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "VA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MD"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "DC"
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
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "VA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "OH"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "DE"
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
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "TN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "OH"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "ME"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "VA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "FL"
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
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MI"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1197ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1197\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Ms. Kelly of Illinois (for herself, Mrs. Miller-Meeks , Mrs. Fletcher , Mr. Carter of Georgia , Ms. Brown , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo reauthorize the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act.\n#### 1. Short title\nThis Act may be cited as the PREEMIE Reauthorization Act of 2025 .\n#### 2. PREEMIE\n##### (a) Research relating to preterm labor and delivery and the care, treatment, and outcomes of preterm and low birthweight infants\n**(1) In general**\nSection 3(e) of the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act (42 U.S.C. 247b\u20134f(e)) is amended by striking fiscal years 2019 through 2023 and inserting fiscal years 2025 through 2029 .\n**(2) Technical correction**\nEffective as if included in the enactment of the PREEMIE Reauthorization Act of 2018 ( Public Law 115\u2013328 ), section 2 of such Act is amended, in the matter preceding paragraph (1), by striking Section 2 and inserting Section 3 .\n##### (b) Interagency working group\nSection 5(a) of the PREEMIE Reauthorization Act of 2018 ( Public Law 115\u2013328 ) is amended by striking The Secretary of Health and Human Services, in collaboration with other departments, as appropriate, may establish and inserting Not later than 18 months after the date of the enactment of the PREEMIE Reauthorization Act of 2025 , the Secretary of Health and Human Services, in collaboration with other departments, as appropriate, shall establish .\n##### (c) Study on preterm births\n**(1) In general**\nThe Secretary of Health and Human Services shall enter into appropriate arrangements with the National Academies of Sciences, Engineering, and Medicine under which the National Academies shall\u2014\n**(A)**\nnot later than 30 days after the date of enactment of this Act, convene a committee of experts in maternal health to study premature births in the United States; and\n**(B)**\nupon completion of the study under subparagraph (A)\u2014\n**(i)**\napprove by consensus a report on the results of such study;\n**(ii)**\ninclude in such report\u2014\n**(I)**\nan assessment of each of the topics listed in paragraph (2);\n**(II)**\nthe analysis required by paragraph (3); and\n**(III)**\nthe raw data used to develop such report; and\n**(iii)**\nnot later than 24 months after the date of enactment of this Act, transmit such report to\u2014\n**(I)**\nthe Secretary of Health and Human Services;\n**(II)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(III)**\nthe Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate.\n**(2) Assessment topics**\nThe topics listed in this subsection are each of the following:\n**(A)**\nThe financial costs of premature birth to society, including\u2014\n**(i)**\nan analysis of stays in neonatal intensive care units and the cost of such stays;\n**(ii)**\nlong-term costs of stays in such units to society and the family involved post-discharge; and\n**(iii)**\nhealth care costs for families post-discharge from such units (such as medications, therapeutic services, co-payments for visits, and specialty equipment).\n**(B)**\nThe factors that impact preterm birth rates.\n**(C)**\nOpportunities for earlier detection of premature birth risk factors, including\u2014\n**(i)**\nopportunities to improve maternal and infant health; and\n**(ii)**\nopportunities for public health programs to provide support and resources for parents in-hospital, in non-hospital settings, and post-discharge.\n**(3) Analysis**\nThe analysis required by this subsection is an analysis of\u2014\n**(A)**\ntargeted research strategies to develop effective drugs, treatments, or interventions to bring at-risk pregnancies to term;\n**(B)**\nState and other programs\u2019 best practices with respect to reducing premature birth rates; and\n**(C)**\nprecision medicine and preventative care approaches starting early in the life course (including during pregnancy) with a focus on behavioral and biological influences on premature birth, child health, and the trajectory of such approaches into adulthood.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Child health",
            "updateDate": "2025-05-02T14:51:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-02T14:52:12Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-02T14:52:06Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-05-02T14:51:57Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-05-02T14:51:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:18:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1197",
          "measure-number": "1197",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1197v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>PREEMIE Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and establishes\u00a0actions by the Department of Health and Human Services (HHS) to address preterm birth (i.e., babies born before 37 weeks of pregnancy).</p><p>Specifically, the bill reauthorizes\u00a0epidemiological\u00a0studies, data tracking, and prevention efforts conducted by the Centers for Disease Control and Prevention related to preterm birth.</p><p>Also, the bill requires HHS to establish an interagency working group to improve federal coordination and provide recommendations on preventing preterm birth, infant mortality, and related adverse birth outcomes.</p><p>Additionally, HHS must arrange for the National Academies of Sciences, Engineering, and Medicine to study preterm birth in the United States and report to HHS and Congress on certain aspects, including the financial costs and strategies to reduce the rate of preterm birth.</p>"
        },
        "title": "PREEMIE Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1197.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PREEMIE Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and establishes\u00a0actions by the Department of Health and Human Services (HHS) to address preterm birth (i.e., babies born before 37 weeks of pregnancy).</p><p>Specifically, the bill reauthorizes\u00a0epidemiological\u00a0studies, data tracking, and prevention efforts conducted by the Centers for Disease Control and Prevention related to preterm birth.</p><p>Also, the bill requires HHS to establish an interagency working group to improve federal coordination and provide recommendations on preventing preterm birth, infant mortality, and related adverse birth outcomes.</p><p>Additionally, HHS must arrange for the National Academies of Sciences, Engineering, and Medicine to study preterm birth in the United States and report to HHS and Congress on certain aspects, including the financial costs and strategies to reduce the rate of preterm birth.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1197"
    },
    "title": "PREEMIE Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PREEMIE Reauthorization Act of 2025</strong></p><p>This bill reauthorizes through FY2029 and establishes\u00a0actions by the Department of Health and Human Services (HHS) to address preterm birth (i.e., babies born before 37 weeks of pregnancy).</p><p>Specifically, the bill reauthorizes\u00a0epidemiological\u00a0studies, data tracking, and prevention efforts conducted by the Centers for Disease Control and Prevention related to preterm birth.</p><p>Also, the bill requires HHS to establish an interagency working group to improve federal coordination and provide recommendations on preventing preterm birth, infant mortality, and related adverse birth outcomes.</p><p>Additionally, HHS must arrange for the National Academies of Sciences, Engineering, and Medicine to study preterm birth in the United States and report to HHS and Congress on certain aspects, including the financial costs and strategies to reduce the rate of preterm birth.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1197"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1197ih.xml"
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
      "title": "PREEMIE Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:49Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PREEMIE Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:56Z"
    }
  ]
}
```
