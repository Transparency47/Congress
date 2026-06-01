# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/780
- Title: SAFE Lending Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 780
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-01-15T17:58:21Z
- Update date including text: 2026-01-15T17:58:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/780",
    "number": "780",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
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
    "title": "SAFE Lending Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T17:58:21Z",
    "updateDateIncludingText": "2026-01-15T17:58:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T17:45:29Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-27",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s780is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 780\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Merkley (for himself, Mr. Sanders , Mr. Wyden , Mr. Van Hollen , Mr. Durbin , Mr. Blumenthal , Ms. Smith , Mr. Markey , Mr. Booker , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Truth in Lending Act to address certain issues relating to the extension of consumer credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Abuse and Fraud in Electronic Lending Act of 2025 or the SAFE Lending Act of 2025 .\n#### 2. Consumer control over bank accounts\n##### (a) Prohibiting unauthorized remotely created checks\nSection 905 of the Electronic Fund Transfer Act ( 15 U.S.C. 1693c ) is amended by adding at the end the following:\n(d) Limitations on remotely created checks (1) Definition In this subsection\u2014 (A) the term Federal consumer financial law has the meaning given the term in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 ); and (B) the term remotely created check means a check, including a paper or electronic check and any other payment order that the Bureau, by rule, determines is appropriately covered under this subsection, that\u2014 (i) is not created by the financial institution that holds the customer account from which the check is to be paid; and (ii) does not bear a signature applied, or purported to be applied, by the person from whose account the check is to be paid. (2) Limitations Subject to the limitations in paragraph (3) and any additional limitations that the Bureau may establish, by rule, a remotely created check may only be issued by a person designated in writing by a consumer, with that written designation specifically provided by the consumer to the insured depository institution at which the consumer maintains the account from which the check is to be drawn. (3) Additional limitations (A) In general A designation provided by a consumer under paragraph (2) may be revoked at any time by the consumer. (B) Consumer financial protection laws No payment order, including a remotely created check, may be issued by any person in response to the exercise of, or attempt to exercise, any right by a consumer under\u2014 (i) any Federal consumer financial law; or (ii) any other provision of any law or regulation within the jurisdiction of the Bureau. .\n##### (b) Consumer protections for certain one-Time electronic fund transfers\nSection 913 of the Electronic Fund Transfer Act ( 15 U.S.C. 1693k ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by inserting (a) In general.\u2014 before No person ;\n**(2)**\nin subsection (a)(1), as so designated, by striking preauthorized electronic fund transfers and inserting an electronic fund transfer ; and\n**(3)**\nby adding at the end the following:\n(b) Treatment for electronic fund transfers in credit extensions If a consumer voluntarily agrees to repay an extension of a small-dollar consumer credit transaction, as defined in section 110(a) of the Truth in Lending Act, by means of an electronic fund transfer, the electronic fund transfer shall be treated as a preauthorized electronic fund transfer subject to the protections of this title. .\n#### 3. Transparency and consumer empowerment in small-dollar lending\n##### (a) Small-Dollar consumer credit transactions\n**(1) In general**\nThe Truth in Lending Act ( 15 U.S.C. 1601 et seq. ) is amended\u2014\n**(A)**\nby inserting after section 109 ( 15 U.S.C. 1608 ) the following:\n110. Registration requirement for small-dollar lenders (a) Definition In this section, the term small-dollar consumer credit transaction \u2014 (1) means any transaction that extends credit that is\u2014 (A) made to a consumer in an amount that is not more than\u2014 (i) $5,000; or (ii) such greater amount as the Bureau may, by rule, determine to reflect changes in the Consumer Price Index for all urban consumers published by the Department of Labor; and (B) extended pursuant to an agreement that is\u2014 (i) (I) other than an open end credit plan; and (II) payable in 1 or more installments of less than 12 months; (ii) an open end credit plan in which each advance is fully repayable within a defined time or in connection with a defined event, or both; or (iii) any other plan as the Bureau determines, by rule; and (2) includes any action that facilitates, brokers, arranges, or gathers applications for a transaction described in paragraph (1). (b) Registration requirement A person shall register with the Bureau before issuing credit in a small-dollar consumer credit transaction. ; and\n**(B)**\nin section 173 ( 15 U.S.C. 1666j ), by adding at the end the following:\n(d) Notwithstanding any other provision of this title, any small-dollar consumer credit transaction, as defined in section 110(a), shall comply with the laws of the State in which the consumer to which credit in the transaction is extended resides with respect to annual percentage rates, interest, fees, charges, and such other similar or related matters as the Bureau may, by rule, determine if the small-dollar consumer credit transaction is\u2014 (1) made\u2014 (A) over the internet; (B) by telephone; (C) by facsimile; (D) by mail; (E) by electronic mail; or (F) through another electronic communication; or (2) conducted by a national bank. .\n**(2) Technical and conforming amendment**\nThe table of sections for chapter 1 of the Truth in Lending Act ( 15 U.S.C. 1601 et seq. ) is amended by inserting after the item relating to section 109 the following:\n110. Registration requirement for small-dollar lenders. .\n##### (b) Prohibition on certain fees\nSection 915 of the Electronic Fund Transfer Act ( 15 U.S.C. 1693l\u20131 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Additional fees prohibited (1) Definition In this subsection, the term prepaid account has the meaning given the term in section 1005.2 of title 12, Code of Federal Regulations, or any successor regulation. (2) Prohibition With respect to the use of a prepaid account by a consumer\u2014 (A) it shall be unlawful for any person to charge the consumer a fee for an overdraft with respect to the prepaid account; (B) any transaction for an amount that exceeds the account balance of the prepaid account may be declined by the financial institution holding the prepaid account; and (C) the Bureau may, by rule, prohibit any person from charging a fee with respect to the prepaid account (other than a fee described in subparagraph (A)) so that the Bureau may\u2014 (i) prevent unfair, deceptive, or abusive practices; and (ii) promote the ability of the consumer to understand and compare the costs of prepaid accounts. .\n#### 4. Restrictions on lead generation in small-dollar consumer credit transactions\n##### (a) In general\nChapter 2 of the Truth in Lending Act ( 15 U.S.C. 1631 et seq. ) is amended by adding at the end the following:\n140B. Restrictions on lead generation in small-dollar consumer credit transactions (a) Definitions In this section\u2014 (1) the terms Internet access service and Internet information location tool have the meanings given those terms in section 231(e) of the Communications Act of 1934 ( 47 U.S.C. 231(e) ); (2) the term sensitive personal financial information means a social security number, financial account number, bank routing number, bank account number, or security or access code that is immediately necessary to permit access to the financial account of an individual; and (3) the term small-dollar consumer credit transaction has the meaning given the term in section 110(a). (b) Identification information Any person facilitating, brokering, arranging for, or gathering applications for the distribution of sensitive personal financial information in connection with a small-dollar consumer credit transaction shall prominently disclose information by which the person may be contacted or identified, including for service of process and for identification of the registrant of any domain name registered or used. (c) Prohibition on lead generation in small-Dollar consumer credit transactions No person may facilitate, broker, arrange for, or gather applications for the distribution of sensitive personal financial information in connection with a small-dollar consumer credit transaction unless the person is directly providing the small-dollar consumer credit to a consumer. (d) Rule of construction (1) In general Nothing in this section may be construed to limit the authority of the Bureau to further restrict activities covered by this section. (2) Clarification For the purposes of this section, it shall not be considered facilitating, brokering, arranging for, or gathering applications for the distribution of sensitive personal financial information in connection with a small-dollar consumer credit transaction to be engaged solely in one of the following activities: (A) The provision of a telecommunications service, an Internet access service, or an Internet information location tool. (B) The transmission, storage, retrieval, hosting, formatting, or translation (or any combination thereof) of a communication, without selection or alteration of the content of the communication, except the deletion of a particular communication or material made by another person in a manner that is consistent with section 230(c) of the Communications Act of 1934 ( 47 U.S.C. 230(c) ). .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 2 of the Truth in Lending Act ( 15 U.S.C. 1631 et seq. ) is amended by adding at the end the following:\n140B. Restrictions on lead generation in small-dollar consumer credit transactions. .\n#### 5. Studies\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(B)**\nthe Committee on Indian Affairs of the Senate;\n**(C)**\nthe Committee on Financial Services of the House of Representatives; and\n**(D)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(2)**\nthe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n##### (b) Study required\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study regarding\u2014\n**(1)**\nthe availability of capital on reservations of Indian Tribes; and\n**(2)**\nthe impact that small-dollar consumer credit extended through internet and non-internet means to members of Indian Tribes has had on economic opportunity and wealth for members of Indian Tribes.\n##### (c) Consultation\nIn conducting the study required under subsection (b), the Comptroller General of the United States shall consult, as appropriate, with\u2014\n**(1)**\nthe Bureau of Consumer Financial Protection;\n**(2)**\nthe Board of Governors of the Federal Reserve System;\n**(3)**\nthe Director of the Bureau of Indian Affairs;\n**(4)**\nfederally recognized Indian Tribes; and\n**(5)**\ncommunity development financial institutions operating in Indian lands.\n##### (d) Congressional consideration\nThe Comptroller General of the United States shall submit to the appropriate committees of Congress the study required under subsection (b).\n#### 6. Rulemaking\nNot later than 1 year after the date of enactment of this Act, the Bureau of Consumer Financial Protection shall adopt any final rules that are necessary to implement the provisions of this Act and the amendments made by this Act.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "1658",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE Lending Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-21T18:39:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s780",
          "measure-number": "780",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s780v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stopping Abuse and Fraud in Electronic Lending Act of 2025 or the SAFE Lending Act of 2025</strong></p><p>This bill creates additional consumer protections applicable to certain credit and\u00a0banking transactions, including matters concerning remotely created checks, electronic fund transfers, registration of small-dollar lenders, overdraft fees, and the collection of personal information.</p><p>Under the bill, remotely created checks may only be issued by a person specifically designated in writing by a consumer.\u00a0The consumer must\u00a0provide the designation to the consumer's depository institution. (A remotely created check is a check not issued by the bank and not signed by the account owner.)</p><p>A voluntary agreement to repay a small-dollar consumer credit transaction by an electronic fund transfer is subject to certain protections, including the right of the consumer to stop payment.</p><p>Small-dollar consumer credit providers must register with the Consumer Financial Protection Bureau. Any small-dollar consumer credit transaction is subject to the laws of the state in which the consumer resides.</p><p>The bill also prohibits overdraft fees on prepaid accounts.</p>"
        },
        "title": "SAFE Lending Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s780.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stopping Abuse and Fraud in Electronic Lending Act of 2025 or the SAFE Lending Act of 2025</strong></p><p>This bill creates additional consumer protections applicable to certain credit and\u00a0banking transactions, including matters concerning remotely created checks, electronic fund transfers, registration of small-dollar lenders, overdraft fees, and the collection of personal information.</p><p>Under the bill, remotely created checks may only be issued by a person specifically designated in writing by a consumer.\u00a0The consumer must\u00a0provide the designation to the consumer's depository institution. (A remotely created check is a check not issued by the bank and not signed by the account owner.)</p><p>A voluntary agreement to repay a small-dollar consumer credit transaction by an electronic fund transfer is subject to certain protections, including the right of the consumer to stop payment.</p><p>Small-dollar consumer credit providers must register with the Consumer Financial Protection Bureau. Any small-dollar consumer credit transaction is subject to the laws of the state in which the consumer resides.</p><p>The bill also prohibits overdraft fees on prepaid accounts.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s780"
    },
    "title": "SAFE Lending Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stopping Abuse and Fraud in Electronic Lending Act of 2025 or the SAFE Lending Act of 2025</strong></p><p>This bill creates additional consumer protections applicable to certain credit and\u00a0banking transactions, including matters concerning remotely created checks, electronic fund transfers, registration of small-dollar lenders, overdraft fees, and the collection of personal information.</p><p>Under the bill, remotely created checks may only be issued by a person specifically designated in writing by a consumer.\u00a0The consumer must\u00a0provide the designation to the consumer's depository institution. (A remotely created check is a check not issued by the bank and not signed by the account owner.)</p><p>A voluntary agreement to repay a small-dollar consumer credit transaction by an electronic fund transfer is subject to certain protections, including the right of the consumer to stop payment.</p><p>Small-dollar consumer credit providers must register with the Consumer Financial Protection Bureau. Any small-dollar consumer credit transaction is subject to the laws of the state in which the consumer resides.</p><p>The bill also prohibits overdraft fees on prepaid accounts.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s780"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s780is.xml"
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
      "title": "SAFE Lending Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T13:18:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Lending Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stopping Abuse and Fraud in Electronic Lending Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Truth in Lending Act to address certain issues relating to the extension of consumer credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:10Z"
    }
  ]
}
```
