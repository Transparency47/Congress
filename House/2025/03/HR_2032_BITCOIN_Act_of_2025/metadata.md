# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2032
- Title: BITCOIN Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2032
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-01-26T17:15:06Z
- Update date including text: 2026-01-26T17:15:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2032",
    "number": "2032",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "BITCOIN Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-26T17:15:06Z",
    "updateDateIncludingText": "2026-01-26T17:15:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:00:20Z",
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
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MP"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2032ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2032\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Begich (for himself, Mr. McDowell , Mr. Harrigan , Mr. Rulli , Mr. Nehls , Mr. Taylor , and Mr. Collins ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a Strategic Bitcoin Reserve and other programs to ensure the transparent management of Bitcoin holdings of the Federal Government, to offset costs utilizing certain resources of the Federal Reserve System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Boosting Innovation, Technology, and Competitiveness through Optimized Investment Nationwide Act of 2025 or the BITCOIN Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe global financial landscape is rapidly evolving, with digital assets playing an increasingly significant role in the world economy.\n**(2)**\nBitcoin has demonstrated resilience, widespread adoption, and served as a medium of exchange and a store of value for more than a decade.\n**(3)**\nJust as gold reserves have historically served as a cornerstone of national financial security, Bitcoin represents a digital-age asset capable of enhancing the financial leadership and security of the United States in the 21st century global economy.\n**(4)**\nThe acquisition and long-term storage of substantial quantities of Bitcoin by the United States can strengthen the financial condition of the United States, providing a hedge against economic uncertainty and monetary instability.\n**(5)**\nBitcoin, as a decentralized and finitely scarce digital asset, offers unique properties that complement existing national reserves, strengthening the position of the United States dollar in the global financial system.\n**(6)**\nDiversification of the national assets of the United States to include Bitcoin can enhance financial resilience and position the United States at the forefront of global financial innovation.\n#### 3. Definitions\nIn this Act:\n**(1) Airdrop**\nThe term airdrop means a gratuitous distribution of digital assets to holders of Bitcoin in a broad, equitable, and non-discretionary manner.\n**(2) Bitcoin Purchase Program**\nThe term Bitcoin Purchase Program means the program established under section 5(a).\n**(3) Cold storage**\nThe term cold storage means a method of storing private keys required to transact in Bitcoin, with a nexus to a secure physical location, protected from unauthorized access and isolated from any network connections.\n**(4) Fork**\nThe term fork means a change to the consensus mechanism of a distributed ledger that creates a separate ledger, resulting in a new digital asset that shares a common transaction history with Bitcoin up to the point of the change.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(6) Strategic Bitcoin Reserve**\nThe term Strategic Bitcoin Reserve means the decentralized network of secure Bitcoin storage facilities established pursuant to section 4(a).\n#### 4. Establishment of Strategic Bitcoin Reserve\n##### (a) Establishment\nThe Secretary shall establish a decentralized network of secure Bitcoin storage facilities distributed across the United States, collectively to be known as the Strategic Bitcoin Reserve for the cold storage of Government Bitcoin holdings.\n##### (b) Purpose\nThe Strategic Bitcoin Reserve shall be used for the generation, safekeeping, and management of Bitcoin private keys associated with Government Bitcoin holdings.\n##### (c) Oversight\nThe Secretary shall be responsible for the ongoing monitoring and auditing of the holdings of the Strategic Bitcoin Reserve.\n##### (d) Decentralization\n**(1) In general**\nThe Secretary shall ensure that the facilities of the Strategic Bitcoin Reserve are geographically dispersed throughout the United States, to minimize the risk of simultaneous compromise and to enhance the resilience of the Strategic Bitcoin Reserve.\n**(2) Location selection**\nThe Secretary shall select the locations for the facilities described in paragraph (1) based on a comprehensive risk assessment, prioritizing geographic diversity, security, and accessibility.\n##### (e) Security measures\n**(1) In general**\nThe Secretary shall implement state-of-the-art physical and digital security measures to protect the Strategic Bitcoin Reserve.\n**(2) Consultation**\nThe Secretary shall consult and collaborate with the Secretary of Defense, the Secretary of Homeland Security, and industry experts to ensure the highest level of physical and digital security for the Strategic Bitcoin Reserve.\n##### (f) Retention of forks and airdrops\n**(1) In general**\nThe Secretary shall ensure that, with respect to Bitcoins controlled by the Strategic Bitcoin Reserve, all digital assets resulting from forks of the Bitcoin distributed ledger and digital assets distributed via airdrops to Bitcoin addresses are accounted for and reasonably stored in the Strategic Bitcoin Reserve.\n**(2) Prohibition on immediate sale**\nNo digital asset stored in the Strategic Bitcoin Reserve that is the result of a fork or airdrop may be sold or otherwise disposed of during the 5-year period beginning on the date of the fork or airdrop, unless explicitly authorized by law.\n**(3) Evaluation and disposition after the holding period**\n**(A) Market capitalization assessment**\nUpon the expiration of the 5-year holding period described in paragraph (2), the Secretary shall conduct an assessment to determine which digital asset resulting from a fork has the highest publicly traded market capitalization.\n**(B) Retention of dominant asset**\nThe Secretary shall retain the digital asset with the highest publicly traded market capitalization that resulted from the fork.\n**(C) Disposition of non-dominant assets**\nThe Secretary may sell, auction, or otherwise dispose of any digital assets resulting from the fork other than the asset identified in subparagraph (B), with the proceeds from such disposition to be deposited in the general fund of the Treasury.\n**(D) Exception for novel utility**\nIf the Secretary, in consultation with the Secretary of Commerce and industry experts, determines that a non-dominant forked asset possesses novel technological utility or strategic value to the United States distinct from the dominant asset, the Secretary may recommend to Congress the retention of such asset, notwithstanding subparagraph (C).\n#### 5. Bitcoin Purchase Program\n##### (a) Establishment\n**(1) In general**\nThe Secretary shall establish a Bitcoin Purchase Program which shall\u2014\n**(A)**\npurchase 200,000 Bitcoins per year over a 5-year period, for a total acquisition of 1,000,000 Bitcoins;\n**(B)**\nconduct purchases in a transparent and strategic manner to minimize market disruption; and\n**(C)**\nhold Bitcoin acquired under this section in trust for the United States, as provided in this section.\n**(2) Flexibility relating to purchases**\nThe Secretary shall, by rule, establish a procedure to adjust the purchase schedule set forth under paragraph (1), if necessary, based on prevailing market conditions.\n**(3) Transfer offset**\nAny Bitcoin transferred to the Strategic Bitcoin Reserve under section 7 may offset the purchase requirements under paragraph (1).\n##### (b) Deposit\nAll Bitcoins purchased under the Bitcoin Purchase Program shall be placed in the Strategic Bitcoin Reserve.\n##### (c) Minimum Holding Period\n**(1) In general**\nTo ensure the long-term stability and security of the Strategic Bitcoin Reserve, the Secretary shall hold all Bitcoin acquired by the United States and deposited in the Strategic Bitcoin Reserve, regardless of acquisition method, for not less than 20 years from the date of acquisition.\n**(2) Retention of Bitcoin**\nDuring the minimum holding period under paragraph (1), no Bitcoin held in the Strategic Bitcoin Reserve may be sold, swapped, auctioned, encumbered, or otherwise disposed of for any purpose.\n**(3) Recommendations after holding period**\n**(A) In general**\nOn the date that is 2 years before the end of the minimum holding period under paragraph (1), the Secretary shall submit to Congress recommendations on whether to continue to voluntarily hold or to allow for the gradual and controlled release of a portion of the holdings of the Strategic Bitcoin Reserve for the sole purpose of reducing the national debt.\n**(B) Recommendation**\nUpon the expiration of the minimum holding period, the Secretary shall not recommend selling more than 10 percent of the assets of the Strategic Bitcoin Reserve during any 2-year period.\n##### (d) Public reports\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for a period of 20 years, the Secretary shall publish an annual public report on the status of the Bitcoin Purchase Program.\n##### (e) Additional Bitcoin Acquisitions\n**(1) In general**\nNotwithstanding the purchase limit established in subsection (a)(1)(A), the United States may acquire and hold Bitcoin in excess of 1,000,000 Bitcoins if such Bitcoin is acquired through\u2014\n**(A)**\ntransfers from Federal agencies pursuant to section 7;\n**(B)**\ncivil or criminal forfeitures;\n**(C)**\ngifts or bequests made to the United States; or\n**(D)**\nany other lawful means other than direct purchase under the Bitcoin Purchase Program.\n**(2) Treatment of additional holdings**\nAny Bitcoin acquired pursuant to paragraph (1) shall\u2014\n**(A)**\nbe placed in the Strategic Bitcoin Reserve;\n**(B)**\nbe subject to the same security, auditing, and reporting requirements as Bitcoin acquired through the Bitcoin Purchase Program; and\n**(C)**\nbe subject to the minimum holding period established in subsection (c)(1).\n**(3) Limitation**\nNothing in this subsection shall be construed to authorize the Secretary to purchase Bitcoin in excess of the limits established in subsection (a)(1)(A) through the Bitcoin Purchase Program.\n##### (f) Coordination with exchange stabilization fund\nThe Secretary shall coordinate Bitcoin purchases made through the Bitcoin Purchase Program with any Bitcoin purchases made through the Exchange Stabilization Fund under section 5302 of title 31, United States Code, as amended by section 11 of this Act.\n#### 6. Proof of Reserve System\nTo ensure transparency and accountability in the management of the Strategic Bitcoin Reserve, the Secretary shall establish an ongoing Proof of Reserve system of public cryptographic attestation under which\u2014\n**(1)**\nthe Secretary shall\u2014\n**(A)**\npublish quarterly reports on the Strategic Bitcoin Reserve that include detailed information on the total holdings, transactions, and demonstrated control of private keys relating to the Strategic Bitcoin Reserve, including a public cryptographic attestation;\n**(B)**\nmake the quarterly reports available to the public on an official website of the Department of Treasury; and\n**(C)**\nselect an independent, third-party auditor with expertise in cryptographic attestations to verify the accuracy and integrity of the quarterly reports; and\n**(2)**\nthe Comptroller General of the United States shall, to ensure compliance with this Act, conduct regular oversight of\u2014\n**(A)**\nthe Strategic Bitcoin Reserve;\n**(B)**\nthe quarterly reports under paragraph (1)(A); and\n**(C)**\nthe audits under paragraph (1)(C).\n#### 7. Consolidation of Government Bitcoin Holdings\nBeginning on the date of enactment of this Act, any Bitcoin under the control of any Federal agency, including the United States Marshal Service, shall\u2014\n**(1)**\nnot be sold, swapped, auctioned, or otherwise encumbered; and\n**(2)**\nupon the acquisition of legal title to such Bitcoin (including after a final, unappealable judgment is entered in a criminal or civil forfeiture action in favor of the Federal agency), be transferred by the head of such Federal agency to the Strategic Bitcoin Reserve.\n#### 8. Voluntary State Participation and Segregated Accounts\n##### (a) Voluntary State participation\nThe Secretary shall establish a program that allows a State to voluntarily participate in storing the Bitcoin holdings of the State in the Strategic Bitcoin Reserve in a segregated account.\n##### (b) Participation requirements\nA State choosing to participate in the program established under subsection (a) shall sign a contractual agreement outlining the terms and conditions of participation, which shall include\u2014\n**(1)**\nthe responsibilities of both the State and the Strategic Bitcoin Reserve in managing and securing the Bitcoin holdings of the State in the segregated account of the State;\n**(2)**\na requirement that the State, in coordination with the Secretary, develop and implement appropriate security protocols and access controls to ensure the integrity and confidentiality of the segregated account of the State; and\n**(3)**\nretention of title, and all attendant legal interests, by the State in the Bitcoin held in the segregated account, including title to any digital asset that is the result of a fork or airdrop relating to such Bitcoin.\n##### (c) Withdraw or transfer\nEach State participating in the program established under subsection (a) shall have the right to withdraw or transfer the contents of the segregated account of the State within the Strategic Bitcoin Reserve, subject to the terms and conditions in the signed contractual agreement under subsection (b) and any applicable Federal regulations.\n##### (d) Limitation of liability\n**(1) In general**\nNotwithstanding any other provision of law, the Federal Government shall not be liable for any loss, theft, destruction, or inaccessibility of Bitcoin or other digital assets held in the Strategic Bitcoin Reserve, except in cases of gross negligence or willful misconduct by the Secretary or officials responsible for the management of the Strategic Bitcoin Reserve.\n**(2) Acknowledgment of risk**\nAny agreement entered into under subsection (b) shall include an explicit acknowledgment by the State that digital asset custody carries inherent risks that cannot be eliminated completely, and that the State assumes all risks associated with the voluntary placement of its digital assets in the Strategic Bitcoin Reserve.\n#### 9. Offsetting the cost of the strategic Bitcoin reserve\n##### (a) Discretionary surplus funds of federal reserve banks\nSection 7(a)(3)(A) of the Federal Reserve Act ( 12 U.S.C. 289(a)(3)(A) ) is amended by striking $6,825,000,000 and inserting $2,400,000,000 .\n##### (b) Use of remittances to treasury\n**(1) In general**\nNotwithstanding the second subsection (b) of section 7 of the Federal Reserve Act ( 12 U.S.C. 290 ), for fiscal years 2025 through 2029, if the Federal reserve banks remit net earnings to the general fund of the Treasury during that period, the first $6,000,000,000 of these remittances (before repayment of any deferred asset) in a fiscal year shall be utilized by the Secretary for the implementation of the Bitcoin Purchase Program, pursuant to the purposes set forth under section 5.\n**(2) Exception**\nParagraph (1) shall not apply if the Federal Reserve banks do not remit net earnings in any given fiscal year during the period of fiscal years 2025 through 2029.\n##### (c) Federal reserve system gold certificates\nNot later than 180 days after the date of enactment of this Act, the Federal reserve banks shall tender all outstanding gold certificates in their custody to the Secretary. Not later than 90 days after the tender of the last such certificate, the Secretary shall issue new gold certificates to the Federal reserve banks that reflect the fair market value price of the gold held against such certificates by the Treasury, as of the date specified by the Secretary on each new gold certificate. Upon issue by the Secretary, each Federal reserve bank that receives a new gold certificate shall remit the difference in cash value between the old and new gold certificates to the Secretary for deposit in the general fund within 90 days.\n##### (d) Use of gold certificate remittances\n**(1) In general**\nFunds remitted to the Secretary under subsection (c) shall be allocated as follows:\n**(A)**\nAn amount necessary to fund the Bitcoin Purchase Program, as established in section 5, shall be reserved for that purpose, up to the full amount required to purchase 1,000,000 Bitcoins under the program.\n**(B)**\nAny funds in excess of the amount necessary to fully fund the Bitcoin Purchase Program shall be deposited in the general fund of the Treasury to reduce the public debt.\n**(2) Priority use**\nFunds allocated under paragraph (1)(A) shall be used for Bitcoin purchases under the Bitcoin Purchase Program before utilizing the remittances described in subsection (b) for such purchases.\n**(3) Annual report**\nThe Secretary shall include in the annual report required under section 5(d) an accounting of all funds received under subsection (c) and their allocation pursuant to this subsection.\n##### (e) Conforming amendment\nSection 5117(b) of title 31, United States Code, is amended by striking (for the purpose of issuing those certificates, of 42 and two-ninths dollars a fine troy ounce) .\n#### 10. Protection of Private Property Rights\n##### (a) Rules of construction\nNothing in this Act shall be construed to\u2014\n**(1)**\nauthorize the Federal Government to seize, confiscate, or otherwise impair any property right in the lawfully acquired Bitcoin holdings of any person; or\n**(2)**\ninfringe upon the rights of individuals, businesses, or organizations to purchase, hold, transfer, or dispose of Bitcoin in accordance with the law.\n##### (b) Affirmation of rights\nThis Act affirms and protects the rights of persons to maintain full lawful control over the Bitcoin and other digital assets of those individuals, recognizing that the ability to maintain self-custody of private keys is fundamental to the principles of financial sovereignty, privacy, and personal liberty in the digital age.\n#### 11. Modification of exchange stabilization fund\n##### (a) In general\nSection 5302 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1), by inserting after section 3 of the Special Drawing Rights Act ( 22 U.S.C.286 o ), the following: section 5 of the BITCOIN Act of 2025, ; and\n**(2)**\nin subsection (b), in the first sentence, by striking gold, foreign exchange, and other instruments of credit and securities and inserting gold, Bitcoin, foreign exchange, and other instruments of credit and securities .\n##### (b) Transparency and accountability\nSection 5302(c) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting after all projected liabilities the following: , including a detailed accounting of any Bitcoin transactions and holdings ; and\n**(2)**\nin paragraph (2), by inserting after on the operation of the fund the following: , including a specific accounting of any Bitcoin purchased, sold, or held by the fund during the preceding year .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "954",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BITCOIN Act of 2025",
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
        "updateDate": "2025-03-26T15:25:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
    "originChamber": "House",
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
          "measure-id": "id119hr2032",
          "measure-number": "2032",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2032v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Boosting Innovation, Technology, and Competitiveness through Optimized Investment Nationwide Act of 2025 or the BITCOIN Act of 2025</strong></p><p>This bill provides for the acquisition and storage of the cryptocurrency Bitcoin by the U.S. government.</p><p>The Department of the Treasury must purchase one million Bitcoins over a five-year period and hold the Bitcoins in trust for the United States. The bill also allows for additional acquisitions through specified transfers, forfeitures, and gifts.\u00a0All Bitcoins acquired by the United States and placed into the Strategic Bitcoin Reserve\u00a0must be held for at least 20 years.\u00a0At the end of this period and upon the recommendation of Treasury, a percentage of the holdings may be sold to reduce the national debt. The bill also establishes exceptions to this holding period for specified Bitcoin asset distributions and splits.</p><p>The bill directs Treasury to establish a Strategic Bitcoin Reserve for the secure storage of U.S. Bitcoins. The reserve must be a decentralized network of secure facilities across the United States. Existing U.S.\u00a0Bitcoin holdings must be transferred to the reserve.\u00a0States may voluntarily store Bitcoin holdings in the reserve in segregated accounts.</p><p>The bill also reduces the total amount of U.S. dollars Federal Reserve banks may hold in surplus and requires Federal Reserve banks to remit a certain amount of net earnings annually to the purchase of Bitcoins.</p><p>The bill also allows the use of Treasury\u2019s Exchange Stabilization Fund to carry out purchases made under this bill.</p>"
        },
        "title": "BITCOIN Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2032.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Boosting Innovation, Technology, and Competitiveness through Optimized Investment Nationwide Act of 2025 or the BITCOIN Act of 2025</strong></p><p>This bill provides for the acquisition and storage of the cryptocurrency Bitcoin by the U.S. government.</p><p>The Department of the Treasury must purchase one million Bitcoins over a five-year period and hold the Bitcoins in trust for the United States. The bill also allows for additional acquisitions through specified transfers, forfeitures, and gifts.\u00a0All Bitcoins acquired by the United States and placed into the Strategic Bitcoin Reserve\u00a0must be held for at least 20 years.\u00a0At the end of this period and upon the recommendation of Treasury, a percentage of the holdings may be sold to reduce the national debt. The bill also establishes exceptions to this holding period for specified Bitcoin asset distributions and splits.</p><p>The bill directs Treasury to establish a Strategic Bitcoin Reserve for the secure storage of U.S. Bitcoins. The reserve must be a decentralized network of secure facilities across the United States. Existing U.S.\u00a0Bitcoin holdings must be transferred to the reserve.\u00a0States may voluntarily store Bitcoin holdings in the reserve in segregated accounts.</p><p>The bill also reduces the total amount of U.S. dollars Federal Reserve banks may hold in surplus and requires Federal Reserve banks to remit a certain amount of net earnings annually to the purchase of Bitcoins.</p><p>The bill also allows the use of Treasury\u2019s Exchange Stabilization Fund to carry out purchases made under this bill.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr2032"
    },
    "title": "BITCOIN Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Boosting Innovation, Technology, and Competitiveness through Optimized Investment Nationwide Act of 2025 or the BITCOIN Act of 2025</strong></p><p>This bill provides for the acquisition and storage of the cryptocurrency Bitcoin by the U.S. government.</p><p>The Department of the Treasury must purchase one million Bitcoins over a five-year period and hold the Bitcoins in trust for the United States. The bill also allows for additional acquisitions through specified transfers, forfeitures, and gifts.\u00a0All Bitcoins acquired by the United States and placed into the Strategic Bitcoin Reserve\u00a0must be held for at least 20 years.\u00a0At the end of this period and upon the recommendation of Treasury, a percentage of the holdings may be sold to reduce the national debt. The bill also establishes exceptions to this holding period for specified Bitcoin asset distributions and splits.</p><p>The bill directs Treasury to establish a Strategic Bitcoin Reserve for the secure storage of U.S. Bitcoins. The reserve must be a decentralized network of secure facilities across the United States. Existing U.S.\u00a0Bitcoin holdings must be transferred to the reserve.\u00a0States may voluntarily store Bitcoin holdings in the reserve in segregated accounts.</p><p>The bill also reduces the total amount of U.S. dollars Federal Reserve banks may hold in surplus and requires Federal Reserve banks to remit a certain amount of net earnings annually to the purchase of Bitcoins.</p><p>The bill also allows the use of Treasury\u2019s Exchange Stabilization Fund to carry out purchases made under this bill.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr2032"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2032ih.xml"
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
      "title": "BITCOIN Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BITCOIN Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Boosting Innovation, Technology, and Competitiveness through Optimized Investment Nationwide Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Strategic Bitcoin Reserve and other programs to ensure the transparent management of Bitcoin holdings of the Federal Government, to offset costs utilizing certain resources of the Federal Reserve System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:04:05Z"
    }
  ]
}
```
