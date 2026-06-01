# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5835
- Title: REPO Implementation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5835
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-04-22T08:06:47Z
- Update date including text: 2026-04-22T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5835",
    "number": "5835",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "REPO Implementation Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:06:47Z",
    "updateDateIncludingText": "2026-04-22T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TN"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
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
      "sponsorshipDate": "2025-11-04",
      "state": "DC"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NH"
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
      "sponsorshipDate": "2025-11-07",
      "state": "UT"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MA"
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
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MD"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-10",
      "state": "OH"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "WA"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "PA"
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
      "sponsorshipDate": "2026-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5835ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5835\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Wilson of South Carolina (for himself, Ms. Kaptur , Mr. Kean , Mr. Cohen , and Mr. Doggett ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act to improve the implementation of the seizure of Russian sovereign assets for the benefit of Ukraine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the REPO for Ukrainians Implementation Act of 2025 or the REPO Implementation Act of 2025 .\n#### 2. Recognition of Porto Declaration of Organization for Security and Co-operation in Europe\nSection 101(a) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(10) Every member of the European Union, including Belgium, and all but one member of the G7, are also participating states of the Organization for Security and Co-operation in Europe. (11) On July 3, 2025, the Parliamentary Assembly of the Organization for Security and Co-operation in Europe adopted unanimously in plenary session the Porto Declaration, which [c]alls on OSCE participating States to unlock the full value of an estimated US$300 billion in Russian sovereign assets frozen across the region by repurposing the underlying principal, in sizeable increments and on a regular and timely schedule, for Ukraine until the Russian Federation ends its aggression and agrees to compensate Ukraine for damages directly resulting from the war . .\n#### 3. Transfer of assets to Ukraine Support Fund\nSection 104(b)(2) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin the heading, by striking Vesting and inserting Status of assets ;\n**(2)**\nby striking For funds confiscated and inserting the following:\n(A) Vesting of confiscated funds For funds confiscated ; and\n**(3)**\nby adding at the end the following:\n(B) Transfer of funds not confiscated For the purpose of placing Russian aggressor state sovereign assets into an interest-bearing account, the President may transfer such funds into the Ukraine Support Fund without confiscating such funds. .\n#### 4. Investment of amounts in Ukraine Support Fund\n##### (a) In general\nSection 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking of any funds and inserting the following: \u201cof\u2014\n(A) any funds ;\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(B) any amounts that may be credited to the account under paragraph (3). ; and\n**(2)**\nby adding at the end the following:\n(3) Investment of amounts (A) Investment of amounts The Secretary of the Treasury shall invest such portion of the account established under paragraph (1) as is not required to meet current withdrawals in interest-bearing obligations of the United States or in obligations guaranteed as to both principal and interest by the United States. (B) Interest and proceeds The interest on, and the proceeds from the sale or redemption of, any obligations held in the account established under paragraph (1) shall be credited to and form a part of the account. .\n##### (b) Implementation\nThe President shall ensure that funds in the Ukraine Support Fund established under section 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act are invested as required by paragraph (3) of that section, as added by subsection (a), by not later than the date that is 45 days after the date of the enactment of this Act.\n#### 5. Quarterly obligation of funds in Ukraine Support Fund to benefit Ukraine\n##### (a) In general\nSection 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(4) Quarterly obligations (A) In general Not less frequently than every 90 days while funds remain in the Ukraine Support Fund, the Secretary of State may obligate and expend, from the Fund, an amount that is not less than $250,000,000 (except as provided by subparagraph (B)) for the purpose of providing assistance to Ukraine under this subsection. (B) Final amounts in Fund When less than $250,000,000 remains in the Fund, the Secretary of State may obligate and expend the remaining amount for the purpose of providing assistance to Ukraine under this subsection. .\n##### (b) Implementation\nIt is the sense of Congress that the President should ensure that the first obligation of amounts pursuant to paragraph (4) of section 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act, as added by subsection (a), occurs not later than the date that is 60 days after the date on which Russian sovereign assets are deposited in the Ukraine Support Fund.\n#### 6. Engagement with certain foreign countries\n##### (a) In general\nTitle II of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n109. Engagement with foreign countries (a) Reports required (1) Covered country report Not later than 90 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (2) Report on non-covered countries Not later than 270 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the foreign countries that are not covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (3) Form The reports required by paragraphs (1) and (2) shall be submitted in unclassified form but may include a classified annex. (b) Sense of Congress on engagement Not later than 30 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the Secretary of State, in coordination with the Secretary of the Treasury, should commence a robust, sustained, diplomatic effort to persuade the government of each covered country to begin repurposing, on a quarterly basis, an amount that is not less than 5 percent of the Russian sovereign assets located in that country for the benefit of Ukraine. (c) Covered country defined In this section, the term covered country means Australia and any country that is a member of the G7 or the European Union, other than the United States. .\n##### (b) Clerical amendment\nThe table of contents in section 1 of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by inserting after the item relating to section 108 the following:\nSec. 109. Engagement with foreign countries. .\n#### 7. Modification of judicial review provision\nSection 104(k) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by striking this section each place it appears and inserting this division .\n#### 8. Technical corrections\nThe Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin section 2(2), by striking paragraph (7) and inserting paragraph (6) ;\n**(2)**\nin section 101(a)\u2014\n**(A)**\nin paragraph (4), by striking deplore[d] and inserting [d]eplore[d] ; and\n**(B)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking a resolution and inserting Resolution ES\u201311/5 ;\n**(3)**\nin section 102(6), by striking the period at the end and inserting a semicolon;\n**(4)**\nin section 103(a), in the matter preceding paragraph (1), by striking section 104(j) and inserting section 104(l) ;\n**(5)**\nin section 104\u2014\n**(A)**\nin subsection (a), by striking section 501.603(b)(ii) and inserting section 501.603(b)(1)(ii) ;\n**(B)**\nin subsection (d)(2), by striking accounts and inserting account ; and\n**(C)**\nin subsection (f)(1), by striking Funds and inserting funds ; and\n**(6)**\nin section 105\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by striking section 104(c) and inserting section 104(d) ;\n**(B)**\nin subsection (b), by striking section 104(f) and inserting section 104(g) ; and\n**(C)**\nin subsection (f), by striking subsection (c)(2) and inserting subsection (c) .",
      "versionDate": "2025-10-24",
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
        "actionDate": "2025-10-30",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 243."
      },
      "number": "2918",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REPO Implementation Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T19:45:13Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5835ih.xml"
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
      "title": "REPO Implementation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPO Implementation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPO for Ukrainians Implementation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act to improve the implementation of the seizure of Russian sovereign assets for the benefit of Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T10:03:13Z"
    }
  ]
}
```
