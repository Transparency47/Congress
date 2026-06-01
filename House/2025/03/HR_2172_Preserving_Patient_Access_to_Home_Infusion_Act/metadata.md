# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2172
- Title: Preserving Patient Access to Home Infusion Act
- Congress: 119
- Bill type: HR
- Bill number: 2172
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-05-20T08:07:08Z
- Update date including text: 2026-05-20T08:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2172",
    "number": "2172",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "Preserving Patient Access to Home Infusion Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:08Z",
    "updateDateIncludingText": "2026-05-20T08:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:01:00Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "AL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IA"
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
      "sponsorshipDate": "2025-04-24",
      "state": "WA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
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
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WV"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "UT"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "UT"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "IL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NE"
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
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2172ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2172\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Buchanan (for himself, Mrs. Dingell , Mrs. Harshbarger , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to clarify congressional intent and preserve patient access to home infusion therapy under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preserving Patient Access to Home Infusion Act .\n#### 2. Preservation of patient access to home infusion therapy under Medicare program\n##### (a) Inclusion of pharmacy services\nSection 1861(iii)(2) of the Social Security Act ( 42 U.S.C. 1395x(iii)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting and pharmacy services after nursing services ; and\n**(2)**\nin subparagraph (B), by inserting , assessments, drug preparation and compounding, coordination and documentation of infusion therapy services in the plan of care after subsection (n)) .\n##### (b) Payment\nSection 1834(u)(1)(A) of the Social Security Act ( 42 U.S.C. 1395m(u)(1)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking clause (iii) and inserting clauses (iii) and (iv) ;\n**(2)**\nin clause (ii) by inserting after the first sentence the following new sentence: For purposes of the previous sentence, a reference to payment to a qualified home infusion therapy supplier for an infusion drug administration calendar day in the home of such individual shall refer to payment for each day on which such a drug was administered to the individual (regardless of whether a qualified home infusion therapy supplier was physically present in the home of such individual on such date). ;\n**(3)**\nin clause (iii)\u2014\n**(A)**\nby striking The single payment amount and inserting the following:\n(I) In general Subject to subclause (II), the single payment amount ; and\n**(B)**\nby adding at the end the following new subclause:\n(II) Transitional rule For home infusion therapy furnished on or after January 1, 2026, and before January 1, 2030, the Secretary shall ensure that the single payment amount determined under this subparagraph reflects 5 hours of infusion for a particular therapy in a calendar day. ; and\n**(4)**\nby adding at the end the following new clause:\n(iv) Special rule when a qualified home infusion therapy supplier not physically present in the individual's home In the case where a qualified home infusion therapy supplier is not physically present in the individual's home on the day the home infusion drug is administered to the individual, the single payment amount under this subsection for items and services described in clause (i) furnished on such day to such individual shall be an amount equal to 50 percent of the amount that would have applied under this subsection for such items and services if such a supplier had been physically present. .\n##### (c) Permitting nurse practitioners and physician assistants To establish and review a home infusion plan of care\nSection 1861(iii)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(iii)(1)(B) ) is amended by striking physician (as defined in subsection (r)(1)) and is periodically reviewed by a physician and inserting physician (as defined in subsection (r)(1)) or a nurse practitioner or physician assistant (as those terms are defined in subsection (aa)(5)) and is periodically reviewed by a physician, nurse practitioner, or physician assistant .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n#### 3. Access to home infusion for non-pump drugs and biologicals\n##### (a) Modification of definition of home infusion drug\nSection 1861(iii)(3) of the Social Security Act ( 42 U.S.C. 1395x(iii)(3) ) is amended\u2014\n**(1)**\nin subparagraph (C), by inserting and, in the case of a drug or biological other than a specified non-pump drug or biological (as defined in subparagraph (E)), before through ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) The term specified non-pump drug or biological means a drug or biological that\u2014 (i) is administered intravenously but not through a pump that is an item of durable medical equipment (as defined in subsection (n)); and (ii) is an antibacterial, antifungal, or antiviral (as categorized by the United States Pharmacopeia). .\n##### (b) Clarification on billing\nSection 1834(u) of the Social Security Act ( 42 U.S.C. 1395m(u) ) is amended by adding at the end the following new paragraph:\n(8) Clarification on billing for a specified non-pump drug or biological In the case of a qualified home infusion supplier (as defined in section 1861(iii)(3)(D)) that furnishes items and services described in subparagraphs (A) and (B) of section 1861(iii)(2) in coordination with the furnishing of a home infusion drug (as defined in section 1861(iii)(3)(C)) that is a specified non-pump drug or biological (as defined in section 1861(iii)(3)(E)) where the method of infusion utilized in furnishing such drug or biological does not involve a pump that is an item of durable medical equipment, payment under this subsection for the items and services described in subparagraphs (A) and (B) of section 1861(iii)(2) shall be made with respect to such drug or biological regardless of whether such drug or biological so furnished is payable under this part. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n#### 4. Modification of payment for home infusion supplies\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ) is amended by adding at the end the following new paragraph:\n(22) Special payment rule for items and supplies furnished in conjunction with home infusion therapy (A) In general Notwithstanding the preceding provisions of this subsection, no payment may be made under this subsection with respect to applicable items and services (as defined in subparagraph (B)) that are furnished on or after January 1, 2026, in conjunction home infusion therapy (as defined in section 1861(iii)(1)) for which payment is made under subsection (u) and which are so furnished on the same day as such home infusion therapy and with respect to the same home infusion drug (as defined in section 1861(iii)(3)(C)) for which such payment was so made. (B) Applicable items and services defined For purposes of subparagraph (A), the term applicable items and services means tubing, catheters, dressings, needles, syringes, and other supplies identified by HCPCS code A4221, A4222, or K0552 (or any successor code). .",
      "versionDate": "2025-03-18",
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
      "number": "1058",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preserving Patient Access to Home Infusion Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-01T11:30:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2172",
          "measure-number": "2172",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2172v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>"
        },
        "title": "Preserving Patient Access to Home Infusion Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2172.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr2172"
    },
    "title": "Preserving Patient Access to Home Infusion Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preserving Patient Access to Home Infusion Act\u00a0</strong></p><p>This bill specifically includes pharmacy services and home infusion drugs that are administered\u00a0without a pump as part of covered home infusion therapy under Medicare. The bill also allows nurses and physician assistants to establish and review the plan of care for home infusion therapy, and it specifies that payment may be made regardless of whether a practitioner is physically present in the home at the time the drug is administered.\u00a0</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr2172"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2172ih.xml"
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
      "title": "Preserving Patient Access to Home Infusion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preserving Patient Access to Home Infusion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to clarify congressional intent and preserve patient access to home infusion therapy under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T06:18:31Z"
    }
  ]
}
```
