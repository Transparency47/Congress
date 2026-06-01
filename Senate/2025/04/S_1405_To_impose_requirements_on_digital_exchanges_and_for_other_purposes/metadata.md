# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1405?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1405
- Title: PROOF Act
- Congress: 119
- Bill type: S
- Bill number: 1405
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-05T20:22:24Z
- Update date including text: 2026-03-05T20:22:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1405",
    "number": "1405",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "PROOF Act",
    "type": "S",
    "updateDate": "2026-03-05T20:22:24Z",
    "updateDateIncludingText": "2026-03-05T20:22:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T15:25:27Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1405is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1405\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Tillis (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo impose requirements on digital exchanges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Proving Reserves Of Others\u2019 Funds Act or the PROOF Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered asset**\n**(A) In general**\nThe term covered asset means, with respect to a customer of a digital exchange, money, an asset, or property of the customer.\n**(B) Exceptions**\n**(i) Proprietary funds**\nThe term covered asset does not include proprietary funds of a digital exchange.\n**(ii) Margin accounts**\nIf a customer of a digital exchange has opened a margin account for the purposes of borrowing cash or digital assets, or other related activity, the assets in that margin account are not covered assets.\n**(2) Digital asset**\nThe term digital asset means any digital representation of value that is recorded on a cryptographically secured digital ledger.\n**(3) Digital commodity**\nThe term digital commodity means any form of fungible and intangible personal property that\u2014\n**(A)**\ncan be\u2014\n**(i)**\nexclusively possessed; and\n**(ii)**\ntransferred from a person to another person without necessary reliance on an intermediary; and\n**(B)**\nis not an investment contract.\n**(4) Digital custodian**\n**(A) In general**\nThe term digital custodian means an entity that holds, maintains, or safeguards digital commodities, digital assets, and other assets on behalf of a customer.\n**(B) Exception**\nAny entity facilitating clearing or settling services of a covered asset on behalf of a customer shall not be considered to be a digital custodian of that covered asset for the duration of the clearing or settling process.\n**(5) Digital exchange**\nThe term digital exchange means a trading facility that lists for trading not less than 1 digital commodity or digital asset.\n**(6) Digital wallet**\nThe term digital wallet means any device, physical medium, program, or service that stores a digital asset or digital commodity.\n**(7) Investment contract**\n**(A) In general**\nThe term investment contract means a contract\u2014\n**(i)**\nthat provides for an investment of money in an enterprise with a sponsor; and\n**(ii)**\nthe objective of the performance of which is primarily profit (rather than consumption), which is derived primarily from the managerial or entrepreneurial efforts of the sponsor described in clause (i).\n**(B) Use of certain terms**\nFor the purposes of subparagraph (A)\u2014\n**(i)**\nthe term money means\u2014\n**(I)**\nany medium of exchange recognized as legal tender anywhere in the world; or\n**(II)**\nany convertible virtual currency, as defined by the Financial Crimes Enforcement Network of the Department of the Treasury; and\n**(ii)**\nthe term sponsor means a manager or entrepreneur that has solicited investment in a contract described in that subparagraph.\n**(C) Effect of membership in certain organizations**\nA member of a formal or informal decentralized autonomous organization is not, solely by reason of that membership, or through participation in such an organization, the holder of an investment contract.\n**(D) Exclusions**\nA contract that would otherwise be an investment contract under this paragraph is not an investment contract if the obligee of that contract\u2014\n**(i)**\nas of the date on which the contract became effective, primarily expected profit from performance of the contract; and\n**(ii)**\n**(I)**\nat a date after the date described in clause (i)\u2014\n**(aa)**\nprimarily expects to consume goods or services associated with the contract; or\n**(bb)**\nno longer expects profit primarily from the managerial or entrepreneurial efforts of the sponsor described in subparagraph (A)(i) with respect to the contract.\n**(8) Office**\nThe term Office means the Office of Domestic Finance of the Department of the Treasury.\n**(9) Under Secretary**\nThe term Under Secretary means the Under Secretary of the Treasury for Domestic Finance.\n#### 3. Requirements for digital exchanges regarding treatment of customer assets\n##### (a) Required standards and procedures\nEach digital exchange shall establish baseline accounting standards and procedures that are designed to protect and ensure the safety of covered assets of customers of the exchange.\n##### (b) Holding of customer assets\n**(1) In general**\nEach digital exchange shall hold the covered assets of each customer of the exchange in a manner that minimizes\u2014\n**(A)**\nthe risk of loss by the customer of any such covered asset; and\n**(B)**\nany delay in the customer accessing any such covered asset.\n**(2) Segregation of funds**\n**(A) In general**\nEach digital exchange shall treat and deal with all covered assets of a customer of the exchange that are received by the exchange as belonging to the customer.\n**(B) Co-mingling prohibited**\nExcept as provided in subparagraph (C), with respect to any covered asset of a customer of a digital exchange, the exchange may not\u2014\n**(i)**\nco-mingle that covered asset with assets that are not covered assets; or\n**(ii)**\nuse that covered asset to margin, secure, or guarantee any trade or account of any person other than the customer for which that item is held.\n**(C) Exceptions**\n**(i) In general**\nA digital exchange may, for convenience, co-mingle and deposit a covered asset of a customer of the exchange in the same account as funds of the exchange with any bank, trust company, or qualified digital custodian.\n**(ii) Withdrawal**\nA digital exchange may withdraw from a bank, trust, or digital wallet account such share of a covered asset of a customer of the exchange as may be necessary in the ordinary course of business to margin, guarantee, secure, transfer, adjust, or settle a transaction regarding a digital asset or digital commodity with another digital exchange, including for the payment of a commission, a brokerage fee, interest, taxes, storage costs, or any other charge that lawfully accrues in connection with a digital commodity transaction.\n**(iii) Substitution**\nA customer may explicitly consent to a digital exchange substituting covered assets of the customer with certain other assets.\n##### (c) Enforcement\n**(1) In general**\nIf, in the process of reviewing a report submitted to the Under Secretary under section 4(b) with respect to a digital exchange, the Under Secretary discovers that the digital exchange has violated a provision of this section, the Under Secretary, through the Office, shall impose a civil penalty on the digital exchange in the manner described in clauses (i), (ii), and (iii) of section 4(c)(1)(A) (subject to paragraph (2) of this subsection).\n**(2) Rule of construction**\nFor the purposes of a civil penalty imposed under paragraph (1)\u2014\n**(A)**\nan entity that is subject to the requirements of section 4(a), as described in section 4(c)(1)(A), shall be deemed to be an entity that is subject to the requirements of this section; and\n**(B)**\nthe failure of an entity to satisfy the requirements of section 4(a), as described in section 4(c)(1)(A), shall be deemed to be a failure to satisfy the requirements of this section.\n#### 4. Attestation requirements\n##### (a) Attestation\n**(1) In general**\nNot later than 30 days after the effective date of this section, and monthly thereafter, each digital exchange and each digital custodian shall obtain from an independent auditing firm an attestation that the applicable entity has proof of reserves, which shall be accompanied by appropriate evidence demonstrating proof of those reserves, as described further in subsection (b).\n**(2) Inability to obtain services of auditing firm**\n**(A) In general**\nA digital exchange or digital custodian may contract with, or otherwise obtain the services of, a disinterested third party to carry out the responsibilities of an independent auditing firm under paragraph (1) only if the digital exchange or digital custodian is unable to contract with, or otherwise obtain the services of, an independent auditing firm to carry out those responsibilities.\n**(B) Applicability**\nIf a digital exchange or digital custodian contracts with, or otherwise obtains the services of, a disinterested third party as described in subparagraph (A), that third party shall be subject to the requirements of this section to the same extent as an independent auditing firm carrying out the responsibilities described in paragraph (1).\n**(3) Industry standard**\n**(A) Solicitation of standard**\nNot later than 90 days after the date of enactment of this Act, the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants shall jointly issue a request for public comment soliciting proposals from the digital asset industry regarding a standard for the attestations required under this section.\n**(B) Establishment of advisory committee**\nAfter the expiration of the 90-day period described in subparagraph (A), the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants shall establish an advisory committee that shall be comprised of the entities that submit proposals under that subparagraph.\n**(C) Creation of standard**\nThe advisory committee established under subparagraph (B) shall\u2014\n**(i)**\ncreate a proposed standard for the purposes described in subparagraph (A); and\n**(ii)**\nsubmit to the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants the proposed standard described in clause (i) for approval of the proposed standard by those entities.\n**(D) Approval of standard**\n**(i) In general**\nNot later than 18 months after the date of enactment of this Act, the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants shall jointly approve a proposed standard submitted to those entities under subparagraph (C).\n**(ii) Extension of deadline**\nIf, as of the date that is 18 months after the date of enactment of this Act, the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants have not issued a joint approval described in clause (i), the 18-month deadline described in that clause with respect to that approval shall be extended by consecutive 180-day periods until the date on which those entities issue such an approval.\n##### (b) Reports\n**(1) In general**\nAn auditing firm that prepares an attestation under subsection (a) with respect to an entity shall, after making the attestation, submit to the Under Secretary a report that addresses the following with respect to the entity:\n**(A)**\nCryptographic proof of possession or control over keys that are capable of effectuating the transfer, change of control, or movement of a chain of assets that are owned by a person other than that entity, such as a customer of the entity.\n**(B)**\nVerification of cryptographic proof of reserves of the entity.\n**(C)**\n**(i)**\nVerification of cryptographic proof of the liabilities of the entity.\n**(ii)**\nFor the purposes of clause (i), cryptographic proof means a cryptographically verifiable attestation using a Merkle tree structure, a zero-knowledge proof, or another similar mechanism that can prove\u2014\n**(I)**\nthe existence of the applicable liabilities; and\n**(II)**\nthat the applicable liabilities are the legal responsibility of the entity that is the subject of the report.\n**(2) Public availability**\nThe Under Secretary, through the Office, shall make each report received under paragraph (1) available to the public, which shall include, in addition to the material described in subparagraphs (A), (B), and (C) of that paragraph\u2014\n**(A)**\nthe name of the entity for which the attestation that is the subject of the report was performed; and\n**(B)**\nthe name of the auditing firm that made the attestation described in subparagraph (A) of this paragraph.\n##### (c) Enforcement\n**(1) Civil penalties**\n**(A) In general**\nWith respect to an entity that is subject to the requirements under subsection (a) and fails to satisfy those requirements, the Under Secretary, through the Office, shall, subject to subparagraph (B), impose a civil penalty on the entity as follows:\n**(i)**\nIf that failure is the only such failure by the entity during the most recent 24-month period, the amount of the penalty shall be the greater of the following:\n**(I)**\n25 cents per user or customer of the entity (as applicable), as of the date on which the penalty is imposed.\n**(II)**\n2.5 basis points of the total assets under management by the entity, as of the date on which the penalty is imposed.\n**(ii)**\nIf the entity has 1 additional such failure during the most recent 24-month period, the amount of the penalty shall be the greater of the following:\n**(I)**\n55 cents per user or customer of the entity (as applicable), as of the date on which the penalty is imposed.\n**(II)**\n5.5 basis points of the total assets under management by the entity, as of the date on which the penalty is imposed.\n**(iii)**\nIf the entity has more than 1 additional such failure during the most recent 24-month period, the amount of the penalty shall be the greater of the following:\n**(I)**\n90 cents per user or customer of the entity (as applicable), as of the date on which the penalty is imposed.\n**(II)**\n9 basis points of the total assets under management by the entity, as of the date on which the penalty is imposed.\n**(B) Limitation**\nThe Under Secretary, through the Office, may not impose a penalty on an entity under subparagraph (A) if the imposition of that penalty would cause the total amount of penalties imposed on that entity under that subparagraph for the year in which the penalty would be imposed to exceed the lesser of the following:\n**(i)**\n$1 per user or customer of the entity (as applicable), as of the date on which the penalty would be imposed.\n**(ii)**\n10 basis points of the total assets under management by the entity, as of the date on which the penalty would be imposed.\n**(2) Publication**\nThe Under Secretary, through the Office, shall make publicly available, with respect to the most recent 24-month period, the name of each entity that is subject to the requirements under subsection (a) and has failed to satisfy those requirements.\n**(3) Appeals**\n**(A) In general**\nThe Under Secretary shall establish a process through which an entity on which a penalty is imposed under paragraph (1) may appeal that penalty.\n**(B) Waiver of penalty**\nThe Under Secretary shall waive a penalty imposed under paragraph (1) if the Under Secretary determines in an appeal brought under subparagraph (A) of this paragraph that the reason that the Under Secretary did not receive a report under subsection (b)(1) is because of an action or omission by an auditing firm and not the entity on which the Under Secretary imposed the penalty.\n**(C) Pause in payment**\nAn entity on which the Under Secretary imposes a penalty under paragraph (1) shall not be required to pay that penalty during the period in which an appeal brought by the entity under this paragraph is pending.\n##### (d) Effective date\nThis section shall take effect on the date on which the Public Company Accounting Oversight Board and the American Institute of Certified Public Accountants jointly approve, under subsection (a)(3), an industry standard for the attestations required under this section.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-09T12:37:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1405",
          "measure-number": "1405",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1405v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Proving Reserves Of Others\u2019 Funds Act or the PROOF Act</strong></p><p>This bill requires digital exchanges to protect customer funds and provide proof of reserves.</p><p>Specifically, digital exchanges must minimize (1) customer risk of asset loss, and (2) delays experienced by a customer when accessing assets. With some exceptions, a customer\u2019s assets must be separated from any other assets and may not be used to margin, secure, or guarantee a trade or account of a person other than the customer.</p><p>Further, digital exchanges and digital custodians must report on their proof of reserves through an attestation from an independent auditing firm or a disinterested third party. The Office of Domestic Finance in the Department of the Treasury must make these attestations publicly available.</p><p>The bill also provides for the creation of an industry standard for the attestations.</p><p>Violations are subject to civil penalties.</p>"
        },
        "title": "PROOF Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1405.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Proving Reserves Of Others\u2019 Funds Act or the PROOF Act</strong></p><p>This bill requires digital exchanges to protect customer funds and provide proof of reserves.</p><p>Specifically, digital exchanges must minimize (1) customer risk of asset loss, and (2) delays experienced by a customer when accessing assets. With some exceptions, a customer\u2019s assets must be separated from any other assets and may not be used to margin, secure, or guarantee a trade or account of a person other than the customer.</p><p>Further, digital exchanges and digital custodians must report on their proof of reserves through an attestation from an independent auditing firm or a disinterested third party. The Office of Domestic Finance in the Department of the Treasury must make these attestations publicly available.</p><p>The bill also provides for the creation of an industry standard for the attestations.</p><p>Violations are subject to civil penalties.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119s1405"
    },
    "title": "PROOF Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Proving Reserves Of Others\u2019 Funds Act or the PROOF Act</strong></p><p>This bill requires digital exchanges to protect customer funds and provide proof of reserves.</p><p>Specifically, digital exchanges must minimize (1) customer risk of asset loss, and (2) delays experienced by a customer when accessing assets. With some exceptions, a customer\u2019s assets must be separated from any other assets and may not be used to margin, secure, or guarantee a trade or account of a person other than the customer.</p><p>Further, digital exchanges and digital custodians must report on their proof of reserves through an attestation from an independent auditing firm or a disinterested third party. The Office of Domestic Finance in the Department of the Treasury must make these attestations publicly available.</p><p>The bill also provides for the creation of an industry standard for the attestations.</p><p>Violations are subject to civil penalties.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119s1405"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1405is.xml"
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
      "title": "PROOF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROOF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-01T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Proving Reserves Of Others\u2019 Funds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-01T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose requirements on digital exchanges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-01T02:18:22Z"
    }
  ]
}
```
