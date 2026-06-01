# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7024?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7024
- Title: Hemp Planting Predictability Act
- Congress: 119
- Bill type: HR
- Bill number: 7024
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-05-22T08:07:46Z
- Update date including text: 2026-05-29T16:27:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7024",
    "number": "7024",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Hemp Planting Predictability Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:46Z",
    "updateDateIncludingText": "2026-05-29T16:27:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:42:14Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "KY"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "CO"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MN"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "KY"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "VA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "CO"
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
      "sponsorshipDate": "2026-01-14",
      "state": "GA"
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
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "WI"
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
      "sponsorshipDate": "2026-01-16",
      "state": "GA"
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
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "WI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "GA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "WI"
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
      "sponsorshipDate": "2026-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
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
      "sponsorshipDate": "2026-05-15",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7024ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7024\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Baird (for himself, Mr. Comer , Mr. Evans of Colorado , Mr. Moore of North Carolina , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.\n#### 1. Short title\nThis Act may be cited as the Hemp Planting Predictability Act .\n#### 2. Delayed implementation of amendments to hemp production provisions\nSection 781 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026 ( Public Law 119\u201337 ; 139 Stat. 558) is amended, in the matter preceding paragraph (1), by striking 365 days and inserting 3 years .",
      "versionDate": "2026-01-13",
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
        "actionDate": "2026-05-20",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "7010",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-15T22:41:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-13",
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
          "measure-id": "id119hr7024",
          "measure-number": "7024",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7024v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2026-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>"
        },
        "title": "Hemp Planting Predictability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7024.xml",
    "summary": {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr7024"
    },
    "title": "Hemp Planting Predictability Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr7024"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7024ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hemp Planting Predictability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T14:09:55Z"
    },
    {
      "title": "Hemp Planting Predictability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T14:09:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T14:03:15Z"
    }
  ]
}
```
