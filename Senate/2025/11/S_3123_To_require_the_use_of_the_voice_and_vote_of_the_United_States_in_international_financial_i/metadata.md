# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3123
- Title: Sustainable International Financial Institutions Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3123
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-12-05T21:54:26Z
- Update date including text: 2025-12-05T21:54:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3123",
    "number": "3123",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Sustainable International Financial Institutions Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:54:26Z",
    "updateDateIncludingText": "2025-12-05T21:54:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T16:46:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-11-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3123is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3123\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Merkley (for himself and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the use of the voice and vote of the United States in international financial institutions to advance the cause of transitioning the global economy to a clean energy economy and to prohibit United States Government assistance to countries or entities to support fossil fuel activity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sustainable International Financial Institutions Act of 2025 .\n#### 2. Clean energy and climate justice at international financial institutions\nThe International Financial Institutions Act ( 22 U.S.C. 262c et seq. ) is amended by adding at the end the following:\nXX Clean energy and climate justice 2001. Clean energy and climate justice (a) In general The United States Executive Directors at the international financial institutions specified in subsection (c) shall use the voice and vote of the United States in those institutions\u2014 (1) to advance the cause of reducing greenhouse gas emissions and transitioning the global economy to a clean energy economy, including by seeking to channel assistance toward countries and entities that are building clean and sustainable energy systems; (2) to oppose any policy reform, investment, loan, or extension of financial or technical assistance to any country or entity, that is intended to create, or will have the effect of creating, new capacity for, or the expansion of, fossil fuel activity, including\u2014 (A) any such policy reform, investment, loan, or extension of assistance that would support the refurbishment or life extension of existing fossil fuel capacity; or (B) any such investment, loan, or extension of assistance to a country or entity that would necessitate, or is predicated upon, increased fossil fuel capacity outside of the country receiving the investment, loan, or extension of assistance or the country in which the entity operates, as applicable, without regard to whether the activity falls within the portfolio of the international financial institution providing the investment, loan, or extension of assistance; and (3) to support the phasing out of funding for internal combustion engines for passenger vehicles and buses by 2027 in a way that is sustainable and sensitive to communities in need of mobility. (b) Reduction of contributions; deposit in escrow account (1) Determination of expenditure on new fossil fuel capacity In each fiscal year, the Secretary of the Treasury shall\u2014 (A) determine the amount of investments, loans, and extensions of financial or technical assistance provided by each international financial institution specified in subsection (c) to any country or entity to create new capacity for fossil fuel activity during the preceding fiscal year; and (B) reduce the contribution of the United States to that institution by the amount determined under subparagraph (A). (2) Deposit in escrow account The Secretary shall deposit in an escrow account the amount by which the contribution of the United States to each international financial institution specified in subsection (c) is reduced under paragraph (1)(B). (3) Release from escrow account The Secretary shall release to each international financial institution specified in subsection (c) the amount in the escrow account under paragraph (2) attributable to contributions to that institution reduced under paragraph (1)(B) at such time as the Secretary determines and certifies to Congress that the institution is no longer providing investments, loans, or extensions of financial or technical assistance to any country or entity to create new capacity for fossil fuel activity. (4) Reports required Not later than 120 days after depositing amounts into the escrow account under paragraph (2) attributable to contributions to an international financial institution specified in subsection (c) reduced under paragraph (1)(B), and annually thereafter until amounts are released to that institution under paragraph (3), the Secretary shall submit to Congress a report that documents investments, loans, and extensions of financial or technical assistance provided by that institution to any country or entity to create new capacity for fossil fuel activity during the preceding fiscal year. (c) International financial institutions specified The international financial institutions specified in this subsection are the following: (1) The International Bank for Reconstruction and Development. (2) The International Development Association. (3) The International Finance Corporation. (4) The Multilateral Investment Guarantee Agency. (5) The African Development Fund. (6) The African Development Bank. (7) The Asian Development Fund. (8) The Asian Development Bank. (9) The European Bank for Reconstruction and Development. (10) The Inter-American Development Bank. (11) The Inter-American Development Bank Invest. (12) The North American Development Bank. (d) Definitions In this section: (1) Fossil fuel activity The term fossil fuel activity means the exploration, development, mining or production, processing, refining, transportation (including pipelines transporting gas, oil, or products thereof), combustion, distribution, or marketing of, or the construction or operation of plants for the processing or refining of, coal, petroleum, natural gas, or any derivative of coal, petroleum, or natural gas that is used for fuel. (2) Fossil fuel (A) In general The term fossil fuel means all forms of coal, oil, and gas. (B) Inclusions The term fossil fuel includes\u2014 (i) bitumen from oil sands; (ii) kerogen from oil shale; (iii) liquids manufactured from coal; (iv) coal bed methane; (v) methane hydrates; (vi) light oil derived from shale or other formations; (vii) natural gas liquids; and (viii) all conventionally and unconventionally produced hydrocarbons. (3) Policy reform The term policy reform means a process at an international financial institution that changes rules, regulations, or institutions and results in incentivizing fossil fuel investment, such as by lowering tax liability or increasing energy tariffs. .\n#### 3. Prohibition on foreign assistance that would support fossil fuel activity\nThe United States may not provide, directly or indirectly (such as through a financial intermediary), any loan, insurance, guarantee, or extension of financial or technical assistance, including policy guidance, to any country or entity for any fossil fuel activity (as defined in section 2001(d) of the International Financial Institutions Act, as added by section 2) or a related infrastructure project, including through the United States International Development Finance Corporation, the Export-Import Bank of the United States, the Trade and Development Agency, the United States Agency for International Development, or the Millennium Challenge Corporation.",
      "versionDate": "2025-11-06",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5952",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sustainable International Financial Institutions Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-11-20T17:28:48Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3123is.xml"
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
      "title": "Sustainable International Financial Institutions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T06:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sustainable International Financial Institutions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the use of the voice and vote of the United States in international financial institutions to advance the cause of transitioning the global economy to a clean energy economy and to prohibit United States Government assistance to countries or entities to support fossil fuel activity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:25Z"
    }
  ]
}
```
