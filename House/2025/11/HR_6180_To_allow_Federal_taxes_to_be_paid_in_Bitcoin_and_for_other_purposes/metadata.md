# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6180?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6180
- Title: Bitcoin for America Act
- Congress: 119
- Bill type: HR
- Bill number: 6180
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2025-12-04T21:33:01Z
- Update date including text: 2025-12-04T21:33:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6180",
    "number": "6180",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Bitcoin for America Act",
    "type": "HR",
    "updateDate": "2025-12-04T21:33:01Z",
    "updateDateIncludingText": "2025-12-04T21:33:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6180ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6180\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo allow Federal taxes to be paid in Bitcoin, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the Bitcoin for America Act .\n##### (b) Findings\nCongress finds the following:\n**(1)**\nBitcoin operates on a decentralized, open-source protocol with a fixed supply cap of 21 million coins, creating inherent scarcity that contrasts sharply with fiat currencies; historical data shows that Bitcoin\u2019s value has increased dramatically since its 2009 inception, exceeding the compound annual growth rates of traditional assets as a direct result of its deflationary design.\n**(2)**\nBy authorizing the acceptance of Federal income taxes in Bitcoin and the deposit of such funds into the Strategic Bitcoin Reserve, the United States will diversify its national wealth into a non-inflationary asset that serves as a long-term store of value, thereby strengthening the Nation\u2019s financial resilience against currency devaluation, economic instability, and global market volatility.\n**(3)**\nOther nations\u2014including but not limited to China, Russia, and emerging economies\u2014actively acquire Bitcoin to diversify their reserves and hedge against global financial instability, such that the United States risks falling behind in this strategic race; authorizing the incorporation of Bitcoin into the United States Strategic Bitcoin Reserve through tax revenues would bolster the Nation\u2019s global competitiveness and safeguard national security by securing a stake in a decentralized, geopolitically neutral asset immune to sanctions or external interference.\n**(4)**\nBitcoin\u2019s permissionless nature enables individuals to participate in the global economy without reliance on traditional banking systems, which often exclude underserved populations; by enabling the payment of Federal income taxes in Bitcoin, the United States promotes financial inclusion, empowering citizens to engage in a modern, decentralized economy.\n**(5)**\nThe value of the United States dollar is influenced by monetary policies, including quantitative easing and interest rate adjustments, which have historically led to inflation and reduced purchasing power; Bitcoin, being free from such interventions, offers a stable alternative for preserving wealth, and the establishment and maintenance of the Strategic Bitcoin Reserve would mitigate risks associated with fiat currency devaluation, ensuring the United States maintains economic strength in an increasingly digital and decentralized global economy.\n**(6)**\nBitcoin\u2019s value is expected to appreciate due to its scarcity and growing adoption, such that revenues deposited into the United States Bitcoin Strategic Reserve would increase in real value over time, creating a self-sustaining fiscal mechanism that reduces reliance on debt-based financing, enhances the Nation\u2019s balance sheet, and provides a robust financial foundation for future generations.\n#### 2. Payment of Federal taxes with bitcoin\n##### (a) In general\nSubchapter B of chapter 64 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6318. Payment with bitcoin (a) Authority The Secretary shall allow taxpayers to pay the taxes (and any penalty, addition to tax, or other amount) imposed under this title with Bitcoin. (b) Manner of payment For purposes of this title, a payment of any amount with Bitcoin shall be deemed made\u2014 (1) if the taxpayer irrevocably transfers Bitcoin\u2014 (A) to a Bitcoin network address designated by the Secretary, or (B) to an address or account of an entity designated by the Secretary to act as a financial agent under subsection (e), in accordance with procedures prescribed by the Secretary, and (2) at the time that the transfer described in paragraph (1) has obtained the level of network confirmations specified by the Secretary. The Secretary may prescribe rules regarding required network confirmations and proof of transfer. (c) Valuation The amount of any payment made with Bitcoin shall be the fair market value of the Bitcoin at the time the payment is deemed made under subsection (b). The Secretary shall prescribe regulations that establish and publish one or more reference rates for determining such fair market value, similar to the foreign currency exchange rates published for Federal tax purposes. (d) Nonrecognition No gain or loss shall be recognized by a taxpayer on the transfer of Bitcoin to the United States (including to a financial agent of the United States acting pursuant to subsection (e)) in satisfaction of any liability imposed by this title. A transfer described in the preceding sentence shall not be treated as a sale or exchange for purposes of section 1001. Nonrecognition under this subsection shall apply only to the portion of any transfer not exceeding the amount of the liability satisfied thereby, determined using the fair market value under subsection (c). Any amount transferred in excess of such liability shall be treated as a disposition for purposes of section 1001. (e) Third-Party financial agents The Secretary may enter into contracts or other arrangements with regulated financial institutions chartered or licensed under United States law and subject to the Bank Secrecy Act and applicable Office of Foreign Assets Control (OFAC) requirements to act as the Secretary\u2019s financial agents to receive custody, convert (if and as directed by the Secretary), and remit Bitcoin tendered under this section. Agents shall comply with applicable Treasury, Internal Revenue Service, and financial regulatory standards. (f) Information reporting and guidance The Secretary may prescribe such regulations or other guidance as are necessary or appropriate to carry out the purposes of this section, including rules for documentation, receipts, timing and source of valuation, acceptable exchanges and price feeds, required network confirmations, and information reporting by payors and agents. (g) Basis and lot selection (1) In general In the case of a taxpayer that holds more than one lot of Bitcoin, the taxpayer may designate which lot or lots of Bitcoin are treated as transferred in a transaction described in subsection (d), in such form and manner and at such time as the Secretary may prescribe. (2) Permissible methods The Secretary shall prescribe regulations that allow taxpayers to determine which lot or lots are treated as transferred using one or more permissible methods including specific identification, first-in first-out, last-in first-out, highest cost in first-out, or other methods similar to those allowed under section 1012 and the regulations thereunder. The regulations shall provide rules for elections, changes in method, and default ordering when a taxpayer does not make a designation. (3) Basis The adjusted basis of the lots of Bitcoin treated as transferred under this section shall be removed from the taxpayer\u2019s aggregate basis in Bitcoin held, and the basis and holding period of any remaining Bitcoin shall be determined without regard to any gain or loss not recognized under subsection (d). .\n##### (b) Clerical amendment\nThe table of sections for subchapter B of chapter 64 of such Code is amended by adding at the end the following new item:\nSec. 6318. Payment with Bitcoin. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments made after the date of the enactment of this Act.\n#### 3. Strategic bitcoin reserve and custody authority\n##### (a) Establishment\nAny Bitcoin received by the Secretary as a payment under the Internal Revenue Code of 1986 shall be deposited by the Secretary in a Strategic Bitcoin Reserve (referred to in this Act as the Reserve ).\n##### (b) Custody and management\nThe Secretary is authorized to\u2014\n**(1)**\naccept, hold, and aggregate Bitcoin received under Federal law or acquired through lawful means on behalf of the United States,\n**(2)**\nestablish such custody, storage, and security arrangements for the Reserve as the Secretary determines appropriate, including cold storage, multi-signature arrangements, and geographically distributed storage facilities, and\n**(3)**\nmanage such holdings with discretion, subject to applicable law, to ensure long-term safekeeping and security.\n##### (c) Long-Term retention\nBitcoin deposited in the Reserve shall be held for the long-term benefit of the United States. The Secretary may not sell, swap, or otherwise dispose of Bitcoin held in the Reserve except\u2014\n**(1)**\nin accordance with a schedule providing that no more than one-twentieth of the total holdings may be disposed of in any one-year period, and\n**(2)**\nonly after the 20-year period beginning on the date such Bitcoin was received or acquired by the United States.\n##### (d) Reporting and oversight\nThe Secretary shall publish an annual public report describing\u2014\n**(1)**\nthe total Bitcoin holdings of the United States, and\n**(2)**\nthe custody and security arrangements of the Reserve.\n##### (e) Secretary\nFor purposes of this section, the term Secretary means the Secretary of the Treasury or the Secretary\u2019s delegate.",
      "versionDate": "2025-11-20",
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
        "name": "Taxation",
        "updateDate": "2025-12-04T21:33:01Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6180ih.xml"
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
      "title": "Bitcoin for America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bitcoin for America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow Federal taxes to be paid in Bitcoin, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T07:48:28Z"
    }
  ]
}
```
