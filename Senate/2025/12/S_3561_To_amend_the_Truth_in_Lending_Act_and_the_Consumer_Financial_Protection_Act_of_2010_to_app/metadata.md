# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3561
- Title: Buy Now, Pay Later Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3561
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-02-10T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S8923)
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S8923)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3561",
    "number": "3561",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Buy Now, Pay Later Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-02-10T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S8923)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-18",
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
            "date": "2025-12-18T17:35:23Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-18T17:35:23Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3561is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3561\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Reed (for himself, Mr. Van Hollen , Mr. Blumenthal , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Truth in Lending Act and the Consumer Financial Protection Act of 2010 to apply certain protections and oversight to buy now, pay later loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Buy Now, Pay Later Protection Act of 2025 .\n#### 2. Application of the Truth in Lending Act to buy now pay later loans\n##### (a) In general\nThe Truth in Lending Act ( 15 U.S.C. 1601 et seq. ) is amended\u2014\n**(1)**\nin section 103 ( 15 U.S.C. 1602 ), by adding at the end the following:\n(ff) Buy now, pay later loan The term buy now, pay later loan means a closed-end consumer loan for a retail transaction that\u2014 (1) is repaid in not more than 4 interest-free installments; and (2) does not impose a finance charge. ;\n**(2)**\nin section 127 ( 15 U.S.C. 1637 )\u2014\n**(A)**\nin subsection (a), by striking under an open end consumer credit plan and inserting under an open end consumer credit plan or a buy now, pay later loan each place it occurs; and\n**(B)**\nin subsection (b), by striking under an open end consumer credit plan and inserting under an open end consumer credit plan or a buy now, pay later loan each place it occurs;\n**(3)**\nin section 170 ( 15 U.S.C. 1666i )\u2014\n**(A)**\nin the section heading, by striking Rights of credit card customers. and inserting Rights of credit card customers and buy now, pay later loan customers. ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nby striking a card issuer who has issued a credit card to a cardholder pursuant to an open end consumer credit plan and inserting a card issuer who has issued a credit card to a cardholder pursuant to an open end consumer credit plan or a creditor who has provided a buy now, pay later loan to a consumer ;\n**(ii)**\nby striking in which the credit card and inserting in which the credit card or buy now, pay later loan ;\n**(iii)**\nby striking honoring the credit card and inserting honoring the credit card or buy now, pay later loan each place it occurs;\n**(iv)**\nby striking provided by the cardholder and inserting provided by the cardholder or consumer ;\n**(v)**\nby striking defenses against a card issuer and inserting defenses against a card issuer or creditor ;\n**(vi)**\nby striking is the same person as the card issuer and inserting is the same person as the card issuer or creditor ;\n**(vii)**\nby striking is controlled by the card issuer, and inserting is controlled by the card issuer or creditor, ;\n**(viii)**\nby striking common control with the card issuer and inserting common control with the card issuer or creditor ;\n**(ix)**\nby striking in the card issuer's products and inserting in the card issuer's or creditor\u2019s products ;\n**(x)**\nby striking by the card issuer in which and inserting by the card issuer or creditor in which ; and\n**(xi)**\nby striking using the credit card issued by the card issuer and inserting using the credit card issued by the card issuer or the buy now, pay later loan provided by the creditor ; and\n**(C)**\nin subsection (b)\u2014\n**(i)**\nby striking asserted by the cardholder and inserting asserted by the cardholder or consumer ;\n**(ii)**\nby striking at the time the cardholder first notifies the card issuer or the person honoring the credit card of such claim or defense and inserting at the time the cardholder or consumer first notifies the card issuer or creditor or the person honoring the credit card or buy now, pay later loan of such claim or defense ; and\n**(iii)**\nby striking the cardholder's account and inserting the cardholder's account or the consumer's buy now, pay later loan account ;\n**(4)**\nin section 161 ( 15 U.S.C. 1666 )\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by striking in connection with an extension of consumer credit, and inserting in connection with an extension of consumer credit, including a buy now, pay later loan, ; and\n**(B)**\nin subsection (d), by striking an open end consumer credit plan and inserting an open end consumer credit plan or a buy now, pay later loan ; and\n**(5)**\nin section 171(a) ( 15 U.S.C. 1666i\u20131 ), by striking In the case of any credit card account under an open end consumer credit plan and inserting In the case of any credit card account under an open end consumer credit plan or buy now, pay later loan .\n##### (b) Rulemaking\nNot later than 1 year after the date of enactment of this Act, the Consumer Financial Protection Bureau shall issue such rules as the Bureau determines necessary to carry out the amendments made by subsection (a).\n#### 3. Federal supervision of buy now, pay later loan lenders\nSection 1024(a)(1) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5514(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking ; or and inserting a semicolon;\n**(2)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end:\n(F) offers or provides to a consumer a buy now, pay later loan, as defined in section 103 of the Truth in Lending Act ( 15 U.S.C. 1602 ). .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "6891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Buy Now, Pay Later Protection Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-20T15:16:43Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3561is.xml"
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
      "title": "Buy Now, Pay Later Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Truth in Lending Act and the Consumer Financial Protection Act of 2010 to apply certain protections and oversight to buy now, pay later loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T08:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Buy Now, Pay Later Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T07:58:16Z"
    }
  ]
}
```
