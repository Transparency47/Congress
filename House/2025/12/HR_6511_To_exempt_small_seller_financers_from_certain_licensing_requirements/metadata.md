# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6511
- Title: Affordable Homeownership Access Act
- Congress: 119
- Bill type: HR
- Bill number: 6511
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-02-11T09:06:12Z
- Update date including text: 2026-02-11T09:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6511",
    "number": "6511",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Affordable Homeownership Access Act",
    "type": "HR",
    "updateDate": "2026-02-11T09:06:12Z",
    "updateDateIncludingText": "2026-02-11T09:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:02:10Z",
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
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "MO"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6511\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Barr (for himself and Mr. Vicente Gonzalez of Texas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo exempt small seller financers from certain licensing requirements.\n#### 1. Short title\nThis Act may be cited as the Affordable Homeownership Access Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nReal-estate owner financing is a transaction in which the owner of a real estate property provides financing for the buyer of that property and the buyer makes some form of a down payment to the owner, receives the deed or title to the home and then makes installment payments to the owner over a defined period of time.\n**(2)**\nOwner financers provide financing in lieu of the buyer choosing to obtain a loan from a bank.\n**(3)**\nThe owner finance industry consists of small business owners who own real estate and provide financing on those properties to underserved buyers who cannot or would prefer not to obtain traditional bank or loan based financing.\n**(4)**\nOwner financers are governed by real estate and consumer protection laws (including, but not limited to, ability to repay, deceptive trade practices, and usury laws) of each State, as well as State and Federal fair housing and equal opportunity laws.\n**(5)**\nUsing owner financing will benefit home values, increase neighborhood stabilization, and assist with family wealth creation through increased homeownership as more homes are sold with owner financing.\n**(6)**\nNone of the amendments made by this Act, are applicable to transactions known as Contracts for Deed or Land Installment Contracts that are not lawfully recorded, Lease Options, Lease with Option to buy and Rent to Own.\n#### 3. Exception for owner financers with respect to loan originator license or registration requirements\nSection 1504 of the S.A.F.E. Mortgage Licensing Act of 2008 ( 12 U.S.C. 5103 ) is amended by adding at the end the following:\n(c) Exception for owner financers The requirements of this title shall not apply to any person (other than a depository institution) who\u2014 (1) extend credit with respect to not more than 24 residential mortgage loans in a 12-month period; and (2) only extend credit with respect to residential mortgage loans that are with respect to property that is owned by such person. .\n#### 4. Exception for owner financers in the definition of mortgage originator\nSubparagraph (E) of section 103(dd)(2) of the Truth in Lending Act ( 15 U.S.C. 1602(dd)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (F) and (G) as subparagraphs (G) and (H), respectively;\n**(2)**\nby amending subparagraph (E) to read as follows:\n(E) does not include, with respect to a residential mortgage sale, a person or entity (including a corporation, partnership, proprietorship, association, cooperative, estate, or trust) if\u2014 (i) such a person or entity provides owner financing, in a 12-month period, for the sale of 24 properties; and (ii) each piece of real property described under clause (i) is owned by such a person or entity and serves as security for the loan or extension of credit, provided that such loan or extension of credit\u2014 (I) is not made by a person or entity that has constructed, or acted as a general contractor for the construction of, a residence on the property in the ordinary course of business of such person, corporation, association, estate, or trust; (II) is fully amortizing; (III) is with respect to a sale for which the owner determines in good faith and documents that the buyer has a reasonable ability to pay the owner; (IV) has a fixed rate or an adjustable rate that is adjustable after 5 or more years, subject to reasonable annual and lifetime limitations on interest rate increases; and (V) meets any other criteria the Bureau may prescribe by rule; ; and\n**(3)**\nby inserting after subparagraph (E) the following:\n(F) does not include, with respect to a residential mortgage loan or extension of credit, a person or entity (including a corporation, partnership, proprietorship, association, cooperative, estate, or trust) if\u2014 (i) the loan or extension of credit is owner financed and is a consumer loan or extension of credit secured by a security interest on a manufactured home (as defined under section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974); and (ii) each home described under clause (i) is owned by such a person or entity and serves as security for the loan or extension of credit, provided that such loan or extension of credit\u2014 (I) is not made by a person or entity that has manufactured the manufactured home; (II) is fully amortizing; (III) is with respect to a sale for which the owner determines in good faith and documents that the buyer has a reasonable ability to pay the owner; (IV) has a fixed rate or an adjustable rate that is adjustable after 5 or more years, subject to reasonable annual and lifetime limitations on interest rate increases; and (V) meets any other criteria the Bureau may prescribe by rule; .\n#### 5. Report on owner financing\n##### (a) Study\nThe Secretary of Housing and Urban Development and the Secretary of the Treasury shall jointly carry out a study on\u2014\n**(1)**\nthe number of homes bought for under $150,000 or 60 percent of the median home value in a given community, whichever is lower, in the United States by utilizing owner financing;\n**(2)**\nthe number of homes described under paragraph (1) financed by licensed mortgage brokers;\n**(3)**\nthe potential number of homes described under paragraph (1) which could be sold but aren\u2019t, because owner financiers are unwilling, or from a practical standpoint unable, to comply with mortgage broker rules; and\n**(4)**\nthe potential benefit to home values and wealth creation if more homes were to be sold utilizing owner finance.\n##### (b) Report\nNot later than the end of the 1-year period beginning on the date of the enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of the Treasury shall jointly issue a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing\u2014\n**(1)**\nall findings and determinations made in carrying out the study required under subsection (a); and\n**(2)**\ndata on the number of transactions utilizing owner financing 20 years, 15 years, 10 years, and 5 years prior to the date of the enactment of this Act.",
      "versionDate": "2025-12-09",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-07T17:23:10Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6511ih.xml"
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
      "title": "Affordable Homeownership Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Homeownership Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt small seller financers from certain licensing requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:23Z"
    }
  ]
}
```
