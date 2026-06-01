# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3958?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3958
- Title: Puerto Rico Nutrition Assistance Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 3958
- Origin chamber: Senate
- Introduced date: 2026-03-02
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in Senate
- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-02: Introduced in Senate

## Actions

- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3958",
    "number": "3958",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Puerto Rico Nutrition Assistance Fairness Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-02",
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
        "item": {
          "date": "2026-03-02T22:54:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "PA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NM"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NY"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "GA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "VA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "VT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "NJ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3958is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3958\nIN THE SENATE OF THE UNITED STATES\nMarch 2, 2026 Mrs. Gillibrand (for herself, Mr. Fetterman , Mr. Luj\u00e1n , Mr. Padilla , Mr. Schumer , Mr. Warnock , Mr. Murphy , Mr. Kaine , Mr. Booker , Mr. Welch , Mr. Blumenthal , Mr. Markey , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to transition Puerto Rico to the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Puerto Rico Nutrition Assistance Fairness Act .\n#### 2. Amendments to the Food and Nutrition Act of 2008\n##### (a) Definitions\nSection 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ) is amended\u2014\n**(1)**\nin subsection (r), by inserting Puerto Rico, after Guam, ; and\n**(2)**\nin subsection (u)(3), by striking subparagraph (A) and inserting the following:\n(A) make cost adjustments in the thrifty food plan for Hawaii, the urban and rural parts of Alaska, and Puerto Rico to reflect the cost of food in Hawaii, the urban and rural parts of Alaska, and Puerto Rico, respectively; .\n##### (b) Eligible households\nSection 5 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014 ) is amended\u2014\n**(1)**\nin subsection (b), in the first sentence, by inserting Puerto Rico, after Guam, ;\n**(2)**\nin subsection (c)(1), by striking and Guam and inserting Guam, and Puerto Rico ; and\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)(A), by inserting Puerto Rico, after Hawaii, each place it appears; and\n**(B)**\nin paragraph (6)(B), in the matter preceding clause (i), by inserting Puerto Rico, after Guam, .\n#### 3. Submission of plan of operation; technical assistance; determination and certification by Secretary of Agriculture\n##### (a) Submission of plan of operation\nOn designating an agency of the kind described in section 3(s)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(s)(1) ), Puerto Rico shall have 180 days to submit to the Secretary of Agriculture (in this Act referred to as the Secretary ) its plan of operation, including a plan to transition to the supplemental nutrition assistance program under section 4(a) of such Act ( 7 U.S.C. 2013(a) ) as a request to participate in the supplemental nutrition assistance program under such Act.\n##### (b) Technical assistance\nWithin the 180-day period specified in subsection (a) and upon request from Puerto Rico, the Secretary shall provide appropriate training and technical assistance to enable Puerto Rico to formulate a plan of operation described in subsection (a).\n##### (c) Determination by the Secretary of Agriculture\nNot later than 180 days after receiving a plan of operation described in subsection (a), the Secretary shall approve the plan of operation if such plan satisfies the requirements for a supplemental nutrition assistance program State plan in accordance with subsections (d) and (e) of section 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ). If the Secretary does not approve such plan, the Secretary shall provide, not later than 30 days after disapproval, a statement that specifies each of the requirements that were not satisfied by such plan.\n##### (d) Certification by the Secretary of Agriculture\nIf the Secretary approves the plan submitted by Puerto Rico under subsection (a), the Secretary shall submit to the Congress, not later than 90 days thereafter, a certification that Puerto Rico qualifies to participate in the supplemental nutrition assistance program as a State as defined in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n#### 4. Transition from the consolidated block grant for Puerto Rico\n##### (a) Covered period\nThe Secretary may continue to implement the then most recent approved consolidated block grant specified in section 19(b)(1)(A) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2028(b)(1)(A) ) for an implementation period ending 5 years after the effective date of the amendments made by this Act, or on the date the Secretary determines that Puerto Rico no longer needs to operate the consolidated block grant to complete the transition described in section 3(a), whichever occurs first.\n##### (b) Report\nFor each year a plan is continued under subsection (a), the Secretary shall submit to the Congress an annual report on the operation of such plan. The Secretary shall include in such report information related to increases in funding that are required to accommodate the transition of Puerto Rico from the receipt of block grant payments to the implementation of supplemental nutrition assistance program.\n#### 5. Consolidated block grant for Puerto Rico and American Samoa\nSection 19 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2028 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A), by inserting until the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , before the Commonwealth ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by striking and at the end, and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby inserting ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter ;\n**(bb)**\nby striking the period at the end and inserting ; and ; and\n**(cc)**\nby adding at the end the following:\n(iii) subject to the availability of appropriations under section 18(a), for each fiscal year beginning after the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , 0.4 percent of the aggregate amount specified in clause (i) and adjusted under clause (ii), as further adjusted by the percentage by which the thrifty food plan has been adjusted under section 3(u)(3) between June 30 of the penultimate fiscal year preceding such effective date and June 30 of the fiscal year for which the adjustment is made under this clause. ;\n**(ii)**\nin subparagraph (B)(i), in the matter preceding subclause (I), by inserting ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter ; and\n**(iii)**\nin subparagraph (C)\u2014\n**(I)**\nby striking For and inserting the following:\n(i) In general For ;\n**(II)**\nin clause (i) (as so designated), by inserting ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter ; and\n**(III)**\nby adding at the end the following:\n(ii) Full use of funds For each fiscal year beginning after the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , the Secretary shall use 100 percent of the funds made available under subparagraph (A) for payment to American Samoa to pay 100 percent of the expenditures by American Samoa for a nutrition assistance program extended under section 601(c) of Public Law 96\u2013597 ( 48 U.S.C. 1469d(c) ). ; and\n**(C)**\nin paragraph (3), by inserting until the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , before pay to ; and\n**(2)**\nin subsection (b)(1)(A), in the first sentence, by striking In order to receive payments under this Act for any fiscal year and inserting Until the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , to receive payments under this Act for a fiscal year .\n#### 6. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary until the end of the period described in section 4(a).\n#### 7. Effective dates\n##### (a) In general\nExcept as provided in subsection (b), this Act shall take effect on the date of the enactment of this Act.\n##### (b) Effective date of amendments\nThe amendments made by this Act shall take effect on the date that is 10 years after the date of the enactment of this Act.",
      "versionDate": "2026-03-02",
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
        "actionDate": "2025-09-08",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "5168",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
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
        "updateDate": "2026-03-19T19:42:26Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3958is.xml"
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
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to transition Puerto Rico to the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T03:48:24Z"
    }
  ]
}
```
