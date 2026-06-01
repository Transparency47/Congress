# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7040
- Title: SAFE KIDS Act
- Congress: 119
- Bill type: HR
- Bill number: 7040
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-02-11T09:06:10Z
- Update date including text: 2026-02-11T09:06:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H1161-1162)
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H1161-1162)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7040",
    "number": "7040",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SAFE KIDS Act",
    "type": "HR",
    "updateDate": "2026-02-11T09:06:10Z",
    "updateDateIncludingText": "2026-02-11T09:06:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1161-1162)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
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
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2026-01-13T15:02:10Z",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "MI"
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
      "sponsorshipDate": "2026-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AL"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TN"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "UT"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
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
      "sponsorshipDate": "2026-01-13",
      "state": "TN"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "UT"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "VA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "WY"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MD"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7040ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7040\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Moore of Utah (for himself, Mr. Moolenaar , Mrs. Kiggans of Virginia , Mr. Aderholt , Mr. Dunn of Florida , Mr. Moran , Mr. Gosar , Mrs. Harshbarger , Mr. McCormick , Mr. Rulli , Mr. McDowell , Mr. Kennedy of Utah , Mr. McGuire , Mr. Sessions , Mr. Shreve , Mr. Rose , and Mr. Owens ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prevent citizens of foreign adversarial nations from entering into or enforcing surrogacy contracts in the United States.\n#### 1. Short title\nThis Act may be cited as the Stopping Adversarial Foreign Exploitation of Kids In Domestic Surrogacy Act or the SAFE KIDS Act .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nCitizens of foreign entities of concern are exploiting commercial surrogacy laws in the United States.\n**(2)**\nMany developed countries ban international commercial surrogacy altogether. The United States, however, presently allows even citizens of foreign entities of concern to solicit and pay financially distressed Americans to give birth to their children in the United States and then send these infants abroad.\n**(3)**\nThis presents an acute national security threat, and recent events in Arcadia, California reveal that surrogacy is even being used to facilitate human trafficking.\n##### (b) Purposes\nThis Act\u2014\n**(1)**\nacknowledges that foreign persons (including nationals of foreign entities of concern) are abusing surrogacy agreements to exploit women in the United States and to obtain United States citizenship for their children;\n**(2)**\ninvalidates surrogate parentage contracts between prospective parents from foreign entities of concern and a surrogate mother in the United States; and\n**(3)**\nimposes criminal penalties on surrogacy brokers who commercially facilitate such invalid agreements.\n#### 3. Definitions\nIn this Act:\n**(1) Foreign entity of concern**\nThe term foreign entity of concern means any foreign nation listed under section 4872(f)(2) of title 10, United States Code.\n**(2) Prospective parent**\nThe term prospective parent means an individual who, directly or indirectly, enters into a surrogacy agreement to become the legal or custodial parent of a child birthed by a surrogate parent.\n**(3) Surrogacy agreement**\n**(A) In general**\nThe term surrogacy agreement means a contract, agreement, or arrangement, without regard to whether it is oral or written or is direct or brokered, between 1 or more prospective parents and a surrogate parent, under which the surrogate parent agrees to become pregnant and give birth to a child, and, subject to subparagraph (B), to relinquish all parental rights and responsibilities to the prospective parent or parents.\n**(B) Presumption**\nWith respect to a contract, agreement, or arrangement, without regard to whether it is oral or written or is direct or brokered, under which a surrogate parent agrees to become pregnant and give birth to a child that does not expressly addressing parental or custodial rights, there shall be a presumption that the surrogate parent has agreed to relinquish her parental or custodial rights, and that the contract, agreement, or arrangement is a surrogacy agreement, if the contract, agreement, or arrangement is with a prospective parent who is a citizen or permanent resident of a foreign entity of concern.\n**(4) Surrogacy broker**\nThe term surrogacy broker means any individual or entity that induces, arranges, procures, facilitates, or otherwise assists in the formation or execution of a surrogacy agreement.\n**(5) Surrogate parent**\nThe term surrogate parent means a person who agrees to become pregnant and give birth to a child, and to relinquish all parental rights and responsibilities to another person under the terms of a surrogacy agreement.\n#### 4. Certain international surrogate parentage contracts void and unenforceable\n##### (a) In general\nSubject to subsection (b), a surrogacy agreement shall be void and unenforceable if the agreement is between a surrogate parent who is in the United States at the time of birth or who is a citizen or lawful permanent resident of the United States and\u2014\n**(1)**\na prospective parent who is a citizen or permanent resident of a foreign entity of concern; or\n**(2)**\na surrogacy broker who arranges a surrogacy agreement with a prospective parent who is a citizen or permanent resident of a foreign entity of concern.\n##### (b) Exception\nSubsection (a) shall not invalidate a surrogacy agreement between a surrogate parent and 2 prospective parents, if\u2014\n**(1)**\nthe 2 prospective parents are legally married; and\n**(2)**\nat least 1 prospective parent is a citizen or lawful permanent resident of the United States.\n#### 5. Commercial facilitation of foreign surrogacy prohibited; penalty\nA surrogacy broker who knowingly or recklessly induces, arranges, procures, facilitates, or otherwise assists in the formation or execution of a surrogacy agreement that is void and unenforceable under section 4 shall be fined under title 18, United States Code, imprisoned for not more than 1 year, or both.\n#### 6. Custody of child when international surrogate parentage contracts are void and unenforceable\nLegal custody of a child born pursuant to a surrogacy agreement that is void and unenforceable under section 4 shall be decided based on a determination of the best interests of the child under the law of the State where the surrogate parent resides, with no effect given to the surrogacy agreement or any other purported agreement, contract, or understanding concerning the custody of the child.",
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
        "actionDate": "2025-11-04",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3101",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE KIDS Act",
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
        "name": "Immigration",
        "updateDate": "2026-02-02T14:48:23Z"
      }
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7040ih.xml"
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
      "title": "SAFE KIDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE KIDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Adversarial Foreign Exploitation of Kids In Domestic Surrogacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent citizens of foreign adversarial nations from entering into or enforcing surrogacy contracts in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:20Z"
    }
  ]
}
```
