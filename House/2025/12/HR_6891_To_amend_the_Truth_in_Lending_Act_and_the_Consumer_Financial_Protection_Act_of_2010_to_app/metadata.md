# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6891
- Title: Buy Now, Pay Later Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6891
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-04-28T08:06:42Z
- Update date including text: 2026-04-28T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Financial Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6891",
    "number": "6891",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Buy Now, Pay Later Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:42Z",
    "updateDateIncludingText": "2026-04-28T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:01:25Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6891ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6891\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Ross introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Truth in Lending Act and the Consumer Financial Protection Act of 2010 to apply certain protections and oversight to buy now, pay later loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Buy Now, Pay Later Protection Act of 2025 .\n#### 2. Application of the Truth in Lending Act to buy now pay later loans\n##### (a) In general\nThe Truth in Lending Act ( 15 U.S.C. 1601 et seq. ) is amended\u2014\n**(1)**\nin section 103, by adding at the end the following:\n(ff) Buy now, pay later loan The term buy now, pay later loan means a closed-end consumer loan for a retail transaction that\u2014 (1) is repaid in not more than 4 interest-free installments; and (2) does not impose a finance charge. ;\n**(2)**\nin section 127(a), by striking under an open end consumer credit plan and inserting under an open end consumer credit plan or a buy now, pay later loan each place it occurs;\n**(3)**\nin section 127(b), by striking under an open end consumer credit plan and inserting under an open end consumer credit plan or a buy now, pay later loan each place it occurs;\n**(4)**\nin section 170\u2014\n**(A)**\nin the section heading, by striking Rights of credit card customers. and inserting Rights of credit card customers and buy now, pay later loan customers. ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nby striking a card issuer who has issued a credit card to a cardholder pursuant to an open end consumer credit plan and inserting a card issuer who has issued a credit card to a cardholder pursuant to an open end consumer credit plan or a creditor who has provided a buy now, pay later loan to a consumer ;\n**(ii)**\nby striking in which the credit card and inserting in which the credit card or buy now, pay later loan ;\n**(iii)**\nby striking honoring the credit card and inserting honoring the credit card or buy now, pay later loan each place it occurs;\n**(iv)**\nby striking provided by the cardholder and inserting provided by the cardholder or consumer ;\n**(v)**\nby striking defenses against a card issuer and inserting defenses against a card issuer or creditor ;\n**(vi)**\nby striking is the same person as the card issuer and inserting is the same person as the card issuer or creditor ;\n**(vii)**\nby striking is controlled by the card issuer, and inserting is controlled by the card issuer or creditor, ;\n**(viii)**\nby striking common control with the card issuer and inserting common control with the card issuer or creditor ;\n**(ix)**\nby striking in the card issuer's products and inserting in the card issuer's or creditor\u2019s products ;\n**(x)**\nby striking by the card issuer in which and inserting by the card issuer or creditor in which ; and\n**(xi)**\nby striking using the credit card issued by the card issuer and inserting using the credit card issued by the card issuer or the buy now, pay later loan provided by the creditor ; and\n**(C)**\nin subsection (b)\u2014\n**(i)**\nby striking asserted by the cardholder and inserting asserted by the cardholder or consumer ;\n**(ii)**\nby striking at the time the cardholder first notifies the card issuer or the person honoring the credit card of such claim or defense and inserting at the time the cardholder or consumer first notifies the card issuer or creditor or the person honoring the credit card or buy now, pay later loan of such claim or defense ; and\n**(iii)**\nby striking the cardholder's account and inserting the cardholder\u2019s account or the consumer\u2019s buy now, pay later loan account ;\n**(5)**\nin section 161\u2014\n**(A)**\nby striking in connection with an extension of consumer credit, and inserting in connection with an extension of consumer credit, including a buy now, pay later loan,\n**(B)**\nin subsection (d), by striking an open end consumer credit plan and inserting an open end consumer credit plan or a buy now, pay later loan ; and\n**(6)**\nin section 171(a), by striking In the case of any credit card account under an open end consumer credit plan and inserting In the case of any credit card account under an open end consumer credit plan or buy now, pay later loan .\n##### (b) Rulemaking\nThe Bureau of Consumer Financial Protection shall, not later than 1 year after the date of this section shall issue such rules as the Bureau of Consumer Financial Protection determines necessary to carry out the amendments made by subsection (a).\n#### 3. Federal supervision of buy now, pay later loan lenders\nSection 1024(a)(1) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5514(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (D) by striking ; or and inserting a semicolon;\n**(2)**\nin subparagraph (E) by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end:\n(F) offers or provides to a consumer a buy now, pay later loan as such term is defined in section 103 of the Truth in Lending Act. .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-18",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S8923)"
      },
      "number": "3561",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Buy Now, Pay Later Protection Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-05T16:02:43Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6891ih.xml"
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
      "title": "To amend the Truth in Lending Act and the Consumer Financial Protection Act of 2010 to apply certain protections and oversight to buy now, pay later loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:40:00Z"
    },
    {
      "title": "Buy Now, Pay Later Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Buy Now, Pay Later Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:19Z"
    }
  ]
}
```
