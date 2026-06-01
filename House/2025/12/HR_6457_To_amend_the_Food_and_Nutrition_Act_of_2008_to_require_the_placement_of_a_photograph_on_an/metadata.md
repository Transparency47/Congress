# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6457
- Title: FAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 6457
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:07:58Z
- Update date including text: 2026-05-16T08:07:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6457",
    "number": "6457",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "FAIR Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:58Z",
    "updateDateIncludingText": "2026-05-16T08:07:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
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
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:04:00Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AL"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6457ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6457\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Mace (for herself, Mr. Moore of Alabama , and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to require the placement of a photograph on an electronic benefit transfer card used by a household to purchase food with supplemental nutrition assistance program benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Assistance Integrity and Responsibility Act or the FAIR Act .\n#### 2. Amendments to the Food and Nutrition act of 2008\n##### (a) Establishment of photographic identification requirement\nSection 7(h)(9) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h)(9) ) is amended to read as follows:\n(9) Photo identification on electronic benefit transfer cards (A) Requirement Each Electronic Benefit Transfer card issued to a household or individual under this chapter shall include on the face of the card a photographic image taken within the previous ten years, or in the case of a minor taken within the previous five years, of the authorized cardholder to whom the card is issued. (B) Limitation on use of electronic benefit transfer cards An individual authorized to utilize or redeem benefits through an Electronic Benefit Transfer card under this chapter shall redeem such benefits only through an Electronic Benefit Transfer card bearing the name and photograph of such individual cardholder. (C) Issuance of additional electronic benefit transfer cards For households in which benefits are accessed by more than one household member, a State agency may issue individual cards to each household member who is authorized to access benefits, including the name and photograph of an individual authorized to access benefits. (D) Exception for caregivers The Secretary shall establish procedures for reasonable accommodations to allow caregivers of a minor, individual with disabilities, or an elderly individual to access benefits on behalf of a recipient in their care. .\n##### (b) Requirement for retailers To verify identity\nSection 9(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2018(a) ) is amended by\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nredesignating clauses (iv) and (v) as clauses (v) and (vi); and\n**(B)**\ninserting after clause (iii) the following new clause:\n(iv) information related to the ability of a retailer to verify the identity of the holder of an electronic benefit transfer card to prevent fraudulent purchases; ; and\n**(2)**\nadding at the end the following new paragraph:\n(5) As a condition of authorization to accept or redeem benefits under this chapter, a retail food store or wholesale food concern, before making a sale, shall demand to see, and shall inspect, the photograph located on an Electronic Benefit Transfer card for every customer using an Electronic Benefit Transfer card to ensure the purchaser is entitled to utilize or redeem benefits under this chapter. .\n##### (c) Conforming amendment\nSection 7(h)(2)(C)(i) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h)(2)(C)(i) ) is amended by striking photographic identification on electronic benefit transfer cards, .\n##### (d) Rulemaking authority\nWithin 18 months of the enactment of this Act, the Secretary shall make such conforming changes to the Code of Federal Regulations as are necessary to implement the amendments made by this Act.\n##### (e) Effective date\nThis Act, and amendments made by this Act, shall take effect 18 months after the date of the enactment of this Act.",
      "versionDate": "2025-12-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:02:17Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6457ih.xml"
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
      "title": "FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Assistance Integrity and Responsibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to require the placement of a photograph on an electronic benefit transfer card used by a household to purchase food with supplemental nutrition assistance program benefits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:21Z"
    }
  ]
}
```
