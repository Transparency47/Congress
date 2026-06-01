# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3074
- Title: Common Cents Act
- Congress: 119
- Bill type: HR
- Bill number: 3074
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2026-02-04T04:26:30Z
- Update date including text: 2026-02-04T04:26:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 35 - 13.
- 2025-09-04 - Calendars: Placed on the Union Calendar, Calendar No. 192.
- 2025-09-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.
- 2025-09-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 35 - 13.
- 2025-09-04 - Calendars: Placed on the Union Calendar, Calendar No. 192.
- 2025-09-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.
- 2025-09-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3074",
    "number": "3074",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001136",
        "district": "9",
        "firstName": "Lisa",
        "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
        "lastName": "McClain",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Common Cents Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:30Z",
    "updateDateIncludingText": "2026-02-04T04:26:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-09-04",
      "calendarNumber": {
        "calendar": "U00192"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 192.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-04",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-235.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 35 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
        "item": [
          {
            "date": "2025-09-04T18:14:27Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-23T16:54:39Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-22T16:54:25Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-29T14:04:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3074ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3074\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mrs. McClain (for herself and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Secretary of the Treasury to stop minting the penny, to require cash transactions to be rounded up or down to the nearest five cents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Common Cents Act .\n#### 2. Elimination of production of one-cent coin\n##### (a) Elimination\nNot later than 1 year after the date of enactment of this Act, except as provided in subsection (b) and notwithstanding any other provision of law (including section 5112(a)(6) of title 31, United States Code), the Secretary of the Treasury shall cease production of one-cent coins.\n##### (b) Exception\n**(1) In General**\nThe Secretary of the Treasury shall continue to produce one-cent coins as appropriate solely to meet the needs of numismatic collectors of the one-cent coin.\n**(2) Sale**\nAny one-cent coin produced under this subsection shall be sold in accordance with section 5132(a) of title 31 United States Code, and any other provisions of law governing numismatic coins.\n**(3) Net Receipts**\nThe net receipts from the sale of any one-cent coin produced under this subsection shall equal or exceed the total cost of production, including variable costs and the appropriate share of fixed costs of production, as determined by the Secretary of the Treasury.\n##### (c) No effect on legal tender\nAll coins and currencies of the United States, regardless of when coined, printed, or issued, and including one-cent coins, shall continue to be legal tender for all debts, public and private, public charges, taxes, duties, and dues, in accordance with law.\n#### 3. Cash transaction rounding\n##### (a) In general\nNotwithstanding any other provision of law, any person selling goods or services in a cash transaction, entering into any other transaction that results in a payment or transfer of cash between the parties to the transaction, or paying cash wages to an employee as compensation, shall round the payment in the following manner:\n**(1) Rounding down**\nIn any case in which the total transaction amount, including any taxes, ends with 1 cent, 2 cents, 6 cents, or 7 cents as the final digit, the amount of cents in the sum shall be rounded down to the nearest amount divisible by 5 for any person seeking to make payment with legal tender.\n**(2) Rounding up**\nIn any case in which the total transaction amount, including any taxes, ends with 3 cents, 4 cents, 8 cents, or 9 cents as the final digit, the amount of cents in the sum shall be rounded up to the nearest amount divisible by 5 for any person seeking to make payment with legal tender.\n##### (b) Exception\nSubsection (a) shall not apply to\u2014\n**(1)**\ntransactions in which the total transaction amount, including any taxes, totals $0.01 or $0.02, where such transactions shall be rounded up to $.05 for any person seeking to make payment with legal tender; or\n**(2)**\nany transaction for which payment is made by any demand or negotiable instrument, electronic fund transfer, check, gift card, money order, credit card, or other like instrument or method.\n##### (c) Effective date\nThis section shall take effect 1 year after the date of enactment of this Act.",
      "versionDate": "2025-04-29",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3074rh.xml",
      "text": "IB\nUnion Calendar No. 192\n119th CONGRESS\n1st Session\nH. R. 3074\n[Report No. 119\u2013235]\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mrs. McClain (for herself and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on Financial Services\nSeptember 4, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on April 29, 2025\nA BILL\nTo direct the Secretary of the Treasury to stop minting the penny, to require cash transactions to be rounded up or down to the nearest five cents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Common Cents Act .\n#### 2. Specifications of 5-cent coins and elimination of one-cent coins\nSection 5112 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (5), by striking weighs 5 grams. and inserting the following:\nweighs\u2014 (A) 5 grams, with respect to such coin that is an alloy of copper and nickel; or (B) between 4 and 6 grams, with respect to such coin as described in subsection (c). ; and\n**(B)**\nin paragraph (6)\u2014\n**(i)**\nby striking except as provided under subsection (c) of this section, ; and\n**(ii)**\nby striking and weighs 3.11 grams ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the sixth sentence\u2014\n**(i)**\nby inserting either before an alloy ; and\n**(ii)**\nby inserting or a composition described in subsection (c) before the period;\n**(B)**\nby inserting with respect to such coins that are an alloy of copper and nickel after nickel required ; and\n**(C)**\nby striking Except through zinc and inserting The one-cent coin is composed of copper and zinc ;\n**(3)**\nby amending subsection (c) to read as follows:\n(c) 5-cent coin (1) In general The 5-cent coin may be a coin with an inner layer of zinc and an outer layer of nickel. (2) Composition The Secretary may prescribe the composition of zinc and nickel in the 5-cent coin, subject to testing and evaluation that such composition reduces the cost incurred to produce such coin. ; and\n**(4)**\nby adding at the end the following:\n(bb) Elimination of one-cent coin (1) In general Notwithstanding any other provision of law, the Secretary shall cease production of one-cent coins for general circulation, but may continue to produce and issue one-cent coins for sale as numismatic items. (2) No effect on legal tender Any one-cent coin that is minted and issued on any date before the date of the enactment of this subsection shall remain legal tender for all debts, public charges, taxes, and dues. .",
      "versionDate": "2025-09-04",
      "versionType": "Reported in House"
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
        "actionDate": "2025-07-16",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4459",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MINT Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-30",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1525",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Common Cents Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Consumer affairs",
            "updateDate": "2025-08-25T15:33:58Z"
          },
          {
            "name": "Currency",
            "updateDate": "2025-08-25T15:33:42Z"
          },
          {
            "name": "Monetary policy",
            "updateDate": "2025-08-25T15:33:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:07:45Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3074ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3074rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Common Cents Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-05T04:23:20Z"
    },
    {
      "title": "Common Cents Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Common Cents Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Treasury to stop minting the penny, to require cash transactions to be rounded up or down to the nearest five cents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:33Z"
    }
  ]
}
```
