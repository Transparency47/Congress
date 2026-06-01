# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3545
- Title: Lowering American Energy Costs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3545
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-26T14:58:11Z
- Update date including text: 2026-01-26T14:58:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3545",
    "number": "3545",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Lowering American Energy Costs Act of 2025",
    "type": "S",
    "updateDate": "2026-01-26T14:58:11Z",
    "updateDateIncludingText": "2026-01-26T14:58:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T21:45:59Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3545is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3545\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Markey (for himself, Ms. Warren , Mr. Wyden , Mr. Merkley , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Energy Policy and Conservation Act to ban the export of natural gas produced in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering American Energy Costs Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Federal Government has repeatedly found that natural gas exports lead to increased domestic gas and electricity prices, as evidenced by\u2014\n**(A)**\na November 2025 analysis by the Energy Information Administration, which predicts that natural gas prices in 2026 will be 16 percent higher than in 2025 due to increased liquefied natural gas (referred to in this section as LNG ) exports;\n**(B)**\na December 2024 study by the Department of Energy, which determined that\u2014\n**(i)**\nunconstrained exports of United States LNG are projected to increase wholesale domestic natural gas prices by 31 percent by 2050, not accounting for the additional price impact of LNG exports on natural gas price volatility;\n**(ii)**\nvolatility in the global natural gas market will further increase costs on domestic consumers and industry as United States natural gas exports increase;\n**(iii)**\nUnited States households will pay up to an additional $122 per year on average in higher natural gas and electricity costs by 2050; and\n**(iv)**\nthe United States industrial sector will pay an additional $125,000,000,000 in higher energy costs by 2050 as a result of rising United States LNG exports;\n**(C)**\na January 2024 report from the Energy Information Administration, which found that, in the United States, the price of natural gas is the most important driver of wholesale electricity prices because natural gas is often the highest-cost fuel for electricity generation;\n**(D)**\na 2018 study by the Department of Energy, which found that producing incremental natural gas volumes to support natural gas exports will increase the marginal cost of supplying natural gas and therefore raise domestic natural gas prices. ; and\n**(E)**\na 2012 study by the Energy Information Administration, which found that increased natural gas exports lead to increased natural gas prices. and that larger export levels lead to larger domestic price increases, while rapid increases in export levels lead to large initial price increases. ;\n**(2)**\naccording to research by Public Citizen, from January 2025 through September 2025, households in the United States paid $12,000,000,000 more for natural gas than from the same period in 2024, a 22 percent price increase that translates to a roughly $124 price hike for the average household;\n**(3)**\naccording to the Institute for Energy Economics and Financial Analysis, surging United States LNG exports from September 2021 to December 2022 led to the sharpest rise of wholesale gas prices in over a decade, costing domestic consumers $111,000,000,000 in higher energy bills;\n**(4)**\nthe United States is already the largest producer of natural gas and largest exporter of LNG in the world, and continues to set records for LNG exports, including that\u2014\n**(A)**\nin 2025, the United States had multiple record-setting months for LNG exports; and\n**(B)**\nin October 2025, the United States became the first country in the world to surpass 10,000,000 metric tons worth of LNG exports in a single month;\n**(5)**\nnatural gas is primarily composed of methane, which is a dangerous greenhouse gas and the second-largest contributor to atmospheric warming; and\n**(6)**\nnatural gas infrastructure, including pipelines and LNG terminals, lead to significant negative health outcomes for communities surrounding the pipelines and terminals, which is compounded by the fact that new natural gas infrastructure is disproportionately sited in communities that already have polluting infrastructure.\n#### 3. Domestic use of energy supplies and related materials and equipment\n##### (a) In general\nThe Energy Policy and Conservation Act ( 42 U.S.C. 6201 et seq. ) is amended by inserting after section 101 the following:\n102. Domestic use of energy supplies and related materials and equipment (a) Export restrictions The President, by rule, under such terms and conditions as the President determines to be appropriate and necessary to carry out the purposes of this Act, shall restrict exports of natural gas for the purpose of keeping domestic energy costs low. (b) Prohibition of export of natural gas (1) Rule Subject to paragraph (2), the President shall exercise the authority provided under subsection (a) to promulgate a rule prohibiting the export of natural gas produced in the United States. (2) Exemptions (A) In general In accordance with subparagraph (A), the President may exempt from a prohibition on the export natural gas under paragraph (1) any natural gas exports that the President determines\u2014 (i) to be consistent with the national interest and will not unreasonably raise costs for residential consumers; or (ii) to be critical for the national security of\u2014 (I) the United States; or (II) a country that is a strategic international partner or ally of the United States. (B) Congressional approval Before any exemption issued by the President may go into effect, the exemption must be approved by a joint resolution of Congress. .\n##### (b) Clerical and conforming amendments\n**(1) Clerical amendment**\nThe table of contents for the Energy Policy and Conservation Act (42 U.S.C. prec. 6201) is amended by inserting after the item relating to section 101 the following:\n102. Domestic use of energy supplies and related materials and equipment. .\n**(2) Conforming amendment**\nSection 101 of division O of the Consolidated Appropriations Act, 2016 ( 42 U.S.C. 6212a ), is amended by striking subsections (b) through (d).",
      "versionDate": "2025-12-17",
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6851",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lowering American Energy Costs Act of 2025",
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
        "name": "Energy",
        "updateDate": "2026-01-20T15:08:44Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3545is.xml"
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
      "title": "Lowering American Energy Costs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lowering American Energy Costs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Policy and Conservation Act to ban the export of natural gas produced in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:29Z"
    }
  ]
}
```
