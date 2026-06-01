# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3660
- Title: Credit Card Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 3660
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-02-26T12:03:17Z
- Update date including text: 2026-02-26T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3660",
    "number": "3660",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Credit Card Fairness Act",
    "type": "S",
    "updateDate": "2026-02-26T12:03:17Z",
    "updateDateIncludingText": "2026-02-26T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T17:13:44Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "WI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3660is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3660\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Fetterman (for himself, Mr. Booker , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Truth in Lending Act to reduce excessive credit card late fees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Credit Card Fairness Act .\n#### 2. Purpose\nCongress believes the late fees rule of the Consumer Financial Protection Bureau under part 1026 of title 12, Code of Federal Regulations (commonly known as Regulation Z ), was appropriately promulgated as an extension of the Bureau's authority, in existence at the time the rule was promulgated, and this Act is intended only to codify that appropriately promulgated rule and thereby limit late fees to an amount that is reasonable and proportional with respect to the costs of credit card issuers.\n#### 3. Reasonable credit card late fees\nSection 149 of the Truth in Lending Act ( 15 U.S.C. 1665d ) is amended\u2014\n**(1)**\nin subsection (c), by striking shall consider and all that follows through the period, and inserting shall consider the cost incurred by the creditor from such omission or violation. ; and\n**(2)**\nby adding at the end the following:\n(f) Cap on credit card late fees (1) Definitions In this subsection: (A) Large credit card issuer The term large credit card issuer means credit card issuer that had 1,000,000 or more open accounts during the preceding calendar year. (B) Open account The term open account has the meaning given that term in section 1026.58(b)(6) of title 12, Code of Federal Regulations, as in effect on the date of enactment of this subsection (or successor regulation that is consistent with the purposes of the Credit Card Fairness Act ). (2) Fee limitation (A) In general Subject to subparagraph (B), a fee imposed by a large credit card issuer associated with a late payment on an account\u2014 (i) may not exceed $8; and (ii) shall not be, in the determination of the Bureau, in excess of the total costs described in subclause (I), thereby contributing to profits of the credit card issuer. (B) Updates to cap The Bureau may increase the cap on late fees for all large credit card issuers under subparagraph (A)(i) by a rate that is not more than the change in the Consumer Price Index for All Urban Consumers, as published by the Bureau of Labor Statistics of the Department of Labor, for the period beginning on the date of enactment of this Act and ending on the date of proposed implementation of such increase to the cap. (3) Venue for challenge Any action brought to challenge any provision in this subsection, or any decision of the Bureau made pursuant to this subsection, shall be filed in the United States District Court for the District of Columbia. (4) Rulemaking The Bureau shall promulgate any rules under this subsection in accordance with section 553 of title 5, United States Code, and prior to the notice and comment period, the Bureau shall publicly release the research used to inform and develop the proposed rule. .",
      "versionDate": "2026-01-15",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-10T18:35:01Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3660is.xml"
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
      "title": "Credit Card Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Credit Card Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Truth in Lending Act to reduce excessive credit card late fees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:38Z"
    }
  ]
}
```
