# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4394
- Title: the CODE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4394
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-07-31T12:04:50Z
- Update date including text: 2025-07-31T12:04:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4394",
    "number": "4394",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "the CODE Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-31T12:04:50Z",
    "updateDateIncludingText": "2025-07-31T12:04:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:01:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4394ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4394\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Casten introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of the Treasury to develop a public-private partnership program to examine innovative anti-money laundering solutions for decentralized finance services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Compliant Operations of Decentralized Entities Act of 2025 or the the CODE Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nIn 2019, under the Trump Administration, the Financial Crimes Enforcement Network issued guidance (FIN\u20132019\u2013G001) to clarify that decentralized finance applications may be required to register with the agency and comply with the Bank Secrecy Act, including anti-money laundering, recordkeeping, and reporting requirements.\n**(2)**\nIn 2019, under the Trump Administration, the Financial Crimes Enforcement Network published an advisory (FIN\u20132019\u2013A003) noting that the prevalence of unregistered cryptocurrency entities without sufficient anti-money laundering controls enables illicit activity that threatens national security.\n**(3)**\nIn 2022, under the Biden Administration, the Federal Bureau of Investigation published a public service announcement (I\u2013082922\u2013PSA) encouraging decentralized finance services to institute real-time analytics, monitoring, and rigorous testing of the computer code to more quickly identify vulnerabilities and respond to indicators of suspicious activity.\n**(4)**\nIn 2023, under the Biden Administration, the Commodity Futures Trading Commission issued a report ( Decentralized Finance ), advocating for building regulatory compliance into decentralized finance systems and noting that areas like illicit finance compliance and cybersecurity are ripe for this kind of near-term action by software developers.\n**(5)**\nDecentralized finance services may be subject to Bank Secrecy Act requirements, but there is a lack of standardization across decentralized finance services and compliance processes.\n**(6)**\nDecentralized finance services present unique cybersecurity risks and have been vulnerable to exploitation campaigns by North Korean threat actors.\n**(7)**\nDecentralized finance services and the broader cryptocurrency ecosystem could benefit from a set of technological controls that are coherent, consistent, and capable of satisfying Bank Secrecy Act requirements.\n#### 3. Public-private partnership program for decentralized finance services\n##### (a) In general\nNot later than 6 months after the date of enactment of this Act, the Secretary of the Treasury, in consultation with the Financial Crimes Enforcement Network, the Office of Foreign Assets Control, the Federal Bureau of Investigation, the United States Secret Service, the National Institute of Standards and Technology, the Cybersecurity and Infrastructure Security Agency, and such other relevant agencies as determined by the Secretary of the Treasury, shall develop a public-private partnership program with decentralized finance services and relevant risk management experts to\u2014\n**(1)**\nfocus on decentralized finance applications and front-end user interfaces;\n**(2)**\nconsider integrating anti-money laundering, identity verification, sanctions, and cybersecurity controls and other technological solutions into decentralized smart contracts prior to deployment on a public blockchain network;\n**(3)**\ntest the capabilities of such integrated controls in decentralized smart contracts;\n**(4)**\nconsider establishing a regulatory gateway to external, verifiable data inputs and outputs that are capable of upgrading smart contract behavior after it has been deployed; and\n**(5)**\nprovide legislative and regulatory recommendations related to integrated compliance mechanisms for decentralized finance services.\n##### (b) Prohibition on certain participants\nParticipants selected for the public-private partnership program required under subsection (a) shall not include a decentralized finance service owned or controlled, directly or indirectly, by a covered person.\n##### (c) Sunset\nThe public-private partnership program developed under subsection (a) shall terminate 18 months after the date of enactment of this Act.\n##### (d) Rule of construction\nNothing in subsection (a) shall be construed to limit, impair, or otherwise affect the supervisory, regulatory, or enforcement authority or the jurisdiction of the agencies described in subsection (a) under any applicable law.\n##### (e) Interagency coordination\nThe Secretary of the Treasury shall share the recommendations provided pursuant to subsection (a)(5) with other appropriate agencies, and such agencies shall take the recommendations into account when issuing rules or carrying out supervisory functions.\n#### 4. FinCEN advisory\nNot later than 18 months after the date of enactment of this Act, the Financial Crimes Enforcement Network shall publish an advisory related to the responsible development, deployment, and ongoing operation of decentralized finance services on a public blockchain network for the purposes of strengthening compliance with the Bank Secrecy Act.\n#### 5. Rulemaking to modernize and strengthen Bank Secrecy Act requirements for decentralized finance services\nNot later than 30 months after the date of enactment of this Act, the Secretary of the Treasury shall issue a rule to\u2014\n**(1)**\nfurther define the terms decentralized finance service and decentralized smart contract ; and\n**(2)**\nexpressly require that a decentralized finance service implements and maintains\u2014\n**(A)**\na risk-based anti-money laundering program that meets the requirements under the Bank Secrecy Act; and\n**(B)**\na risk-based sanctions compliance program.\n#### 6. Definitions\nIn this Act:\n**(1) Bank Secrecy Act**\nThe term Bank Secrecy Act means\u2014\n**(A)**\nsection 21 of the Federal Deposit Insurance Act ( 12 U.S.C. 1829b );\n**(B)**\nchapter 2 of title I of Public Law 91\u2013508 ( 12 U.S.C. 1951 et seq. ); and\n**(C)**\nsubchapter II of chapter 53 of title 31, United States Code.\n**(2) Covered person**\nThe term covered person means\u2014\n**(A)**\nthe President;\n**(B)**\nthe Vice President;\n**(C)**\na Member of Congress;\n**(D)**\na senior executive branch employee; or\n**(E)**\nthe spouse, child, son-in-law, or daughter-in-law, as determined under applicable common law, of any individual described in subparagraph (A), (B), (C), or (D).\n**(3) Decentralized finance service**\nThe term decentralized finance service means a protocol, application, or service that, through the use of decentralized smart contracts deployed on a public blockchain network, facilitates digital asset transactions or the exchange of digital assets for other digital assets or fiat currency and may include\u2014\n**(A)**\na peer-to-peer digital asset trading platform;\n**(B)**\na digital asset lending protocol;\n**(C)**\na digital asset staking or liquidity service;\n**(D)**\na digital asset mixing service;\n**(E)**\na cross-chain bridge service provider; or\n**(F)**\nany other decentralized finance service determined by the Secretary of the Treasury.\n**(4) Decentralized smart contract**\nThe term decentralized smart contract means a digital contract or collections of computer code on a public blockchain network that are automatically executed if specific conditions are met.\n**(5) Public blockchain network**\nThe term public blockchain network means an open source, decentralized, permissionless distributed ledger system that records digital asset transactions.\n**(6) Risk management expert**\nThe term risk management expert means a person or entity with specialized knowledge or expertise in identifying, preventing, and managing illicit finance, cybersecurity, or compliance risks associated with decentralized finance services, and may include\u2014\n**(A)**\nan identity verification software provider;\n**(B)**\na fraud detection service;\n**(C)**\na blockchain analytics firm;\n**(D)**\na smart contract auditor;\n**(E)**\na blockchain oracle service;\n**(F)**\na blockchain cybersecurity service; and\n**(G)**\nany other relevant risk management experts as determined by the Secretary of the Treasury.\n**(7) Senior executive branch employee**\nThe term senior executive branch employee means an executive branch employee\u2014\n**(A)**\nwho is employed in a position listed in section 5312 of title 5, United States Code, or for which the rate of pay is equal to the rate of pay payable for level I of the Executive Schedule;\n**(B)**\nwho is employed in a position\u2014\n**(i)**\nin the Executive Office of the President; and\n**(ii)**\nlisted in section 5313 of title 5, United States Code, or for which the rate of pay is equal to the rate of pay payable for level II of the Executive Schedule;\n**(C)**\nwho is appointed by the President pursuant to section 105(a)(2)(A) of title 3, United States Code; or\n**(D)**\nwho is appointed by the Vice President pursuant to section 106(a)(1)(A) of title 3, United States Code.",
      "versionDate": "2025-07-15",
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
        "updateDate": "2025-07-31T12:04:50Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4394ih.xml"
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
      "title": "the CODE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T10:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "the CODE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T10:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "the Compliant Operations of Decentralized Entities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T10:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Treasury to develop a public-private partnership program to examine innovative anti-money laundering solutions for decentralized finance services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T10:33:22Z"
    }
  ]
}
```
