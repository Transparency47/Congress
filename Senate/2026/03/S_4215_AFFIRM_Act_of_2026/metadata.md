# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4215?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4215
- Title: AFFIRM Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4215
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-09T14:23:31Z
- Update date including text: 2026-04-09T14:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4215",
    "number": "4215",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "AFFIRM Act of 2026",
    "type": "S",
    "updateDate": "2026-04-09T14:23:31Z",
    "updateDateIncludingText": "2026-04-09T14:23:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T16:26:04Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4215is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4215\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mrs. Shaheen introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to reduce Federal spending on crop insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Assisting Family Farmers through Insurance Reform Measures Act of 2026 or the AFFIRM Act of 2026 .\n#### 2. Crop insurance premium subsidies disclosure in the public interest\nSection 502(c)(2) of the Federal Crop Insurance Act ( 7 U.S.C. 1502(c)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as subparagraphs (C) and (D), respectively; and\n**(2)**\nby inserting before subparagraph (C) (as so redesignated) the following:\n(A) Disclosure in the public interest Notwithstanding paragraph (1) or any other provision of law, except as provided in subparagraph (B), the Secretary shall on an annual basis make available to the public\u2014 (i) (I) the name of each individual or entity that obtained a federally subsidized crop insurance, livestock, or forage policy or plan of insurance during the previous reinsurance year; (II) the amount of premium subsidy received by the individual or entity from the Corporation; and (III) the amount of any Federal portion of indemnities paid in the event of a loss for that reinsurance year for each policy associated with that individual or entity; and (ii) for each private insurance provider, a description by the name of the private insurance provider of\u2014 (I) the underwriting gains earned through participation in the federally subsidized crop insurance program; and (II) the amount paid under this subtitle for\u2014 (aa) administrative and operating expenses; (bb) any Federal portion of indemnities and reinsurance; and (cc) any other purpose. (B) Limitation The Secretary shall not disclose under subparagraph (A) information relating to individuals and entities covered by a catastrophic risk protection plan offered under section 508(b). .\n#### 3. Adjusted gross income and per person limitations on share of insurance premiums paid by Corporation\nSection 508(e)(1) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e)(1) ) is amended\u2014\n**(1)**\nby striking For the purpose and inserting the following:\n(A) Payment authority Subject to subparagraphs (B) and (C), for the purpose ; and\n**(2)**\nby adding at the end the following:\n(B) Adjusted gross income limitation The Corporation shall not pay a part of the premium for additional coverage for any person or legal entity that has an average adjusted gross income (as defined in section 1001D(a) of the Food Security Act of 1985 (7 U.S.C. 1308\u20133a(a))) that is greater than $250,000. (C) Per person limitation The Corporation shall not pay more than $40,000 for any reinsurance year to any person or legal entity for premiums under this section. .\n#### 4. Prohibition on premium subsidy for harvest price policies\nSection 508(e) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(e) ) is amended by adding at the end the following:\n(10) Prohibition on premium subsidy for harvest price policies Notwithstanding any other provision of law, beginning with the 2027 reinsurance year, the Corporation shall not pay any amount of premium subsidy in the case of a policy or plan of insurance that is based on the actual market price of an agricultural commodity on the date of harvest. .\n#### 5. Cap on overall rate of return for crop insurance providers\nSection 508(k)(3) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(k)(3) ) is amended\u2014\n**(1)**\nby striking the paragraph designation and heading and all that follows through The and inserting the following:\n(3) Risk (A) Share of risk The ; and\n**(2)**\nby adding at the end the following:\n(B) Limitation on average rate of return The target average rate of return for reinsured companies for the 2027 reinsurance year and each subsequent reinsurance year shall be 8.9 percent of retained premiums. .\n#### 6. Cap on reimbursements for administrative and operating expenses of crop insurance providers\nSection 508(k)(4) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(k)(4) ) is amended by adding at the end the following:\n(G) Additional cap on reimbursements (i) In general Notwithstanding subparagraphs (A) through (F), the total amount of reimbursements for administrative and operating costs for the 2027 reinsurance year for all types of policies and plans of insurance shall not exceed $900,000,000. (ii) Adjustment For the 2028 reinsurance year and each subsequent reinsurance year, the dollar amount in effect pursuant to clause (i) shall be increased by the inflation factor established for the administrative and operating costs limitation in the 2011 Standard Reinsurance Agreement. .\n#### 7. Renegotiation of Standard Reinsurance Agreement\nSection 508(k)(8) of the Federal Crop Insurance Act ( 7 U.S.C. 1508(k)(8) ) is amended by striking subparagraph (F).",
      "versionDate": "2026-03-26",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-09T14:23:31Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4215is.xml"
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
      "title": "AFFIRM Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AFFIRM Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Assisting Family Farmers through Insurance Reform Measures Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to reduce Federal spending on crop insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:38Z"
    }
  ]
}
```
