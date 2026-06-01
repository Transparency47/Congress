# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8395?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8395
- Title: PACE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8395
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-04T15:47:41Z
- Update date including text: 2026-05-04T15:47:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8395",
    "number": "8395",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "PACE Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-04T15:47:41Z",
    "updateDateIncludingText": "2026-05-04T15:47:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:00:15Z",
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
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8395ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8395\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mrs. Kim (for herself and Mr. Liccardo ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide for the regulation of registered covered providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Payments Access and Consumer Efficiency Act of 2026 or the PACE Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Board**\nThe term Board of Governors means the Board of Governors of the Federal Reserve System.\n**(2) Comptroller**\nThe term Comptroller means the Comptroller of the Currency.\n**(3) Covered provider**\nThe term covered provider means a person that provides payment services and\u2014\n**(A)**\nholds at least 40 active money transmitter licenses issued in accordance with the laws of each applicable State in which the applicant seeks to offer such payment services;\n**(B)**\nholds a depository institution (as defined in section 3(c) of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(c) )) charter from the State in which the applicant seeks to offer such payment services; or\n**(C)**\nholds a State credit union (as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 )) charter from the State in which the applicant seeks to offer such payment services.\n**(4) Covered State regulator**\nThe term covered State regulator means a State agency that has issued a charter or license to a registered covered provider.\n**(5) Deposit**\nThe term deposit has the meaning given in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n**(6) Insured depository institution**\nThe term insured depository institution has the meaning given in section 2 of the GENIUS Act ( 12 U.S.C. 5901 ).\n**(7) Monetary value**\nThe term monetary value means a medium of exchange.\n**(8) Outstanding payment obligations**\nThe term outstanding payment obligations means the amount of payment service obligations incurred by a registered covered provider but not yet paid.\n**(9) Payment instrument**\nThe term payment instrument means a physical or electronic check, draft, money order, traveler\u2019s check, or card or other means of access to an account or other instrument for the transmission or payment of monetary value. The term does not include stored value.\n**(10) Payment service**\nThe term payment service \u2014\n**(A)**\nmeans\u2014\n**(i)**\nreceiving monetary value for transmission or transmitting monetary value;\n**(ii)**\nreceiving monetary value from a payor on behalf of a payee for goods or services provided by the payee;\n**(iii)**\nselling or issuing stored value;\n**(iv)**\nselling or issuing payment instruments; and\n**(v)**\nproviding access or custody services with respect to monetary value; and\n**(B)**\ndoes not include the provision solely of online or telecommunications services or network access.\n**(11) Payments reserve account**\nThe term payments reserve account means an account held at a Federal reserve bank that includes access to Fedwire Funds Service, FedNow Service, and FedACH Services (including access to necessary relevant contingent services, as determined by the Board of Governors of the Federal Reserve System).\n**(12) Registered covered provider**\nThe term registered covered provider means a covered provider that has registered with the Comptroller in accordance with the requirements of this Act.\n**(13) State**\nThe term State means each State of the United States, the District of Columbia, and each territory or possession of the United States.\n**(14) Stored value**\nThe term stored value has the meaning given in section 1002(28) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481(28) ).\n#### 3. Federal registration of eligible state payment service providers\n##### (a) Registration of payment service providers\n**(1) Registration**\nA covered provider may submit an application to register with the Comptroller to become a registered covered provider.\n**(2) Evaluation**\nThe Comptroller shall evaluate an application received under paragraph (1) using only the factors specified under paragraph (3).\n**(3) Factors**\nThe factors specified in this paragraph are the following:\n**(A)**\nThe applicant is limited to engaging in activities that directly support or are incidental to the provision of payment services.\n**(B)**\nThe applicant is able to meet the requirements of sections 4 and 5.\n**(C)**\nThe applicant has adequate financial resources, managerial or technical expertise, and a governance system tailored to the business model and risk profile of the covered provider.\n**(D)**\nThe applicant is able to comply with the requirements of the Bank Secrecy Act (as defined in section 2 of the GENIUS Act ( 12 U.S.C. 5901 )).\n**(E)**\nThe applicant demonstrates benefit to the public, including with respect to innovation, competition, and enabling widespread access and use of payment services.\n**(F)**\nThe applicant is not a designated financial market utility (as defined in section 803(4) of the Payment, Clearing, and Settlement Supervision Act of 2010 ( 12 U.S.C. 5462(4) )).\n**(4) Holders of money transmitter licenses**\nA covered provider described in section 2(3)(A) that becomes a registered covered provider under this Act may provide payment services in any State.\n##### (b) Timing for decision; grounds for denial\n**(1) Initial applications**\nWith respect to an application under subsection (a) received during the 180-day period beginning on the date of the enactment of this Act, the Comptroller shall notify each applicant, not later than 180 days after the receipt of such application\u2014\n**(A)**\nthat the application is complete; or\n**(B)**\nthat the application is incomplete and the specific information required for the application to be considered complete.\n**(2) Extension**\nThe Comptroller may extend the period described in paragraph (1) by an additional 60 days.\n**(3) Subsequent applications**\nWith respect to an application received after the end of the period described in paragraph (1) (including any extension made under paragraph (2)), the Comptroller shall provide the notification required under such paragraph to each applicant not later than 30 days after receiving such application.\n**(4) Decision**\nNot later than 180 days after notifying the applicant that an application is complete, the Comptroller shall notify the applicant of whether the Comptroller approved or denied such application. If the Comptroller fails to submit a notification with such 180-day period, such application shall be deemed to be approved.\n**(5) Denial**\n**(A) Grounds for denial**\nThe Comptroller may deny a complete application received under subsection (a) only if the Comptroller determines the factors described in subsection (a)(3) are not satisfied.\n**(B) Explanation required**\nThe Comptroller shall provide each applicant of a complete application that was denied a written notice explaining such denial, including all findings made by the Comptroller with respect to the factors described in subsection (a)(3).\n##### (c) Revocation\nThe Comptroller shall establish, by rule, a process by which the Comptroller may review and revoke a registration granted under this section to a covered provider if the Comptroller determines the factors described in subsection (a)(3) are not satisfied. Such process shall include a process for providing notice to the covered provider and a process for review of the decision to revoke a registration.\n#### 4. Customer protection standards\n##### (a) Reserve standards\n**(1) In general**\nA registered covered provider shall maintain identifiable reserves backing outstanding payment obligations on at least a 1 to 1 basis, with reserves comprising\u2014\n**(A)**\nUnited States coins and currency (including Federal Reserve notes) or money standing to the credit of an account with a Federal Reserve Bank;\n**(B)**\nfunds held as demand deposits (or other deposits that may be withdrawn upon request at any time) or insured shares at an insured depository institution (including any foreign branches or agents, including correspondent banks, of an insured depository institution), subject to limitations established by the Corporation and the National Credit Union Administration, as applicable, to address safety and soundness risks of such insured depository institution;\n**(C)**\nfunds in transit to the registered covered provider that are owed by an insured depository institution or another registered covered provider, including funds from the automated clearinghouse system or funds receivable from a payment instrument;\n**(D)**\nTreasury bills, notes, or bonds\u2014\n**(i)**\nwith a remaining maturity of 93 days or less; or\n**(ii)**\nissued with a maturity of 93 days or less;\n**(E)**\nmoney received under repurchase agreements, with the registered covered provider acting as a seller of securities and with an overnight maturity, that are backed by Treasury bills with a maturity of 93 days or less;\n**(F)**\nreverse repurchase agreements, with the registered covered provider acting as a purchaser of securities and with an overnight maturity, that are collateralized by Treasury notes, bills, or bonds on an overnight basis, subject to overcollateralization in line with standard market terms, that are\u2014\n**(i)**\ntri-party;\n**(ii)**\ncentrally cleared through a clearing agency registered with the Securities and Exchange Commission; or\n**(iii)**\nbilateral with a counterparty that the issuer has determined to be adequately creditworthy even in the event of severe market stress;\n**(G)**\nsecurities issued by an investment company registered under section 8(a) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20138(a) ), or other registered Government money market fund, and that are invested solely in underlying assets described in subparagraphs (A) through (F);\n**(H)**\nany other similarly liquid Federal Government-issued asset approved by the Comptroller; or\n**(I)**\nany reserve described in subparagraphs (A) through (D) or subparagraphs (G) through (H) in tokenized form, provided that such reserves comply with all applicable laws and regulations.\n**(2) Prohibition on rehypothecation**\nReserves described under paragraph (1) may not be pledged, rehypothecated, or reused, except for the purposes described in section 4(a)(2) of the GENIUS Act ( 12 U.S.C. 5903(a)(2) ).\n**(3) Segregation requirement for access or custody services**\nA registered covered provider providing access or custody services for monetary value shall segregate and separately account for such monetary value and may not commingle such monetary value with the assets of such provider.\n##### (b) Recordkeeping standards\n**(1) In general**\nA registered covered provider shall maintain records of\u2014\n**(A)**\noutstanding payment obligations of the provider with respect to each customer of the provider; and\n**(B)**\nreserves held pursuant to subsection (a).\n**(2) Access or custody services**\nA registered covered provider that provides access or custody services for monetary value shall maintain beneficial ownership records with respect to each applicable account and customer.\n#### 5. Risk management standards and fair access\n##### (a) In general\nThe Comptroller shall ensure that a registered covered provider shall be subject to the capital, liquidity, and risk management regulations issued pursuant to section 4(a)(4) of the GENIUS Act ( 12 U.S.C. 5903(a)(4) ) in a similar manner that such regulations apply to a permitted payment stablecoin issuer (as defined in section 2 of such Act ( 12 U.S.C. 5901 )), where such regulations are tailored to the business model and risk profile of the registered covered provider.\n##### (b) Fair access obligation\nA registered covered provider\u2014\n**(1)**\nshall be subject to the requirements of the Equal Credit Opportunity Act ( 15 U.S.C. 1691 et seq. ) in the same manner as a creditor under such Act;\n**(2)**\nmay not deny access to payment services to an individual because of the individual\u2019s constitutionally or statutorily protected beliefs, affiliations, or political views;\n**(3)**\nmay not cancel a payment services account of an individual as a tool to inhibit such beliefs, affiliations, or political views; and\n**(4)**\nshall make all business decisions with respect to the provision of payment services on the basis of individualized, objective, and risk-based analyses.\n#### 6. Examinations, contracted services, and enforcement\n##### (a) In general\nThe Comptroller may make examinations of a registered covered provider with respect to the following:\n**(1)**\nThe nature of the operations and financial condition of the registered covered provider.\n**(2)**\nThe financial, operational, and other risks that may pose a threat to\u2014\n**(A)**\nthe safety and soundness of the registered covered provider; or\n**(B)**\nthe stability of the financial system of the United States.\n**(3)**\nThe systems of the registered covered provider for monitoring and controlling the risks described in paragraph (2).\n**(4)**\nThe compliance of the registered covered provider with the requirements of Federal consumer financial law (as defined in section 1002 of Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 )), including by\u2014\n**(A)**\nobtaining information about the activities and compliance systems or procedures of such provider; and\n**(B)**\ndetecting and assessing risks to consumers and to markets for consumer financial products and services (as defined in such section 1002).\n##### (b) Contracted services\n**(1) In general**\nWhenever a registered covered provider relies on or contracts for any services or activities that are directly related to and are critical to the provision of payment services by the registered covered provider\u2014\n**(A)**\nthe person that performs such services or activities shall be subject to regulation and supervision by the Comptroller to the same extent as if such services were being performed by the registered covered provider; and\n**(B)**\nthe registered covered provider shall notify the Comptroller of any relationship between the provider and the person that performs such services or activities not later than 30 days after the date which is the earlier of the date on which\u2014\n**(i)**\nsuch provider and such person enter into a contract for provision of such services or activities; or\n**(ii)**\nsuch person begins performance of such service or activity.\n##### (c) Enforcement\nThe Comptroller may enforce the requirements of sections 4 and 5 of this Act against a registered covered provider and take such actions against such provider as permitted under section 8 of the Federal Deposit Insurance Act ( 12 U.S.C. 1818 ), as if such provider was an insured depository institution.\n#### 7. Reports\n##### (a) Submission of reports\nAt the frequency established by the Comptroller, a registered provider shall submit to the Comptroller a report relating to\u2014\n**(1)**\nthe financial condition of the registered covered provider;\n**(2)**\ncompliance by the registered covered provider with the requirements of this Act and other applicable laws relating to the provision of payment services; and\n**(3)**\nany other information the Comptroller may reasonably require with respect to the registered covered provider and the scope of the provision of payment services of such provider.\n##### (b) Existing reports\nTo comply with the requirements of this section, the Comptroller shall, to the maximum extent practicable, use existing reports and other supervisory information and avoid duplication of examination activities, reporting requirements, and requests for information.\n#### 8. Priority for customers of registered covered providers\n##### (a) Nonbank provider defined\nIn this section, the term nonbank provider means a registered covered provider that is not an insured depository institution (as defined in section 2 of the GENIUS Act ( 12 U.S.C. 5901 )).\n##### (b) Exclusion from bankruptcy\nA nonbank provider shall not be treated as a debtor for purposes of chapter 7 or chapter 11 of title 11, United States Code.\n##### (c) Insolvency standards\n**(1) In general**\nA nonbank provider shall be eligible to be subject to an insolvency proceeding administered by a covered State regulator.\n**(2) Appointment**\nNotwithstanding any other provision of Federal law or the law of any State, the Comptroller may be appointed by the covered State regulator to act as conservator or receiver for such a nonbank provider, pursuant to such rules issued by the Comptroller.\n**(3) Backup authority**\nIf, with respect to an insolvent nonbank provider, a State does not promptly initiate an insolvency proceeding beginning on the date the nonbank provider becomes insolvent, the Comptroller shall initiate such insolvency proceeding. For purposes of this paragraph, the Comptroller shall issue such rules as necessary to define promptly .\n##### (d) Priority\nTo the extent that a customer may hold balances with a nonbank provider, amounts realized from the liquidation or other resolution of the nonbank provider by the covered State regulator or the Comptroller (whichever is acting as a conservator or receiver under this section) shall be distributed to pay claims (other than secured claims to the extent of any such security) in the following order of priority:\n**(1)**\nAdministrative expenses of the conservator or receiver.\n**(2)**\nOutstanding payment obligations to customers.\n**(3)**\nAny other general or senior liability of the nonbank provider.\n**(4)**\nAny obligation subordinated to liabilities described in paragraphs (2) and (3) not described in paragraph (5).\n**(5)**\nAny obligation to shareholders or members of the nonbank provider arising as a result of their status as shareholders or members.\n##### (e) Custodial assets\nMonetary value maintained in connection with access or custody services, properly segregated from the nonbank provider\u2019s proprietary assets, are not general assets of the nonbank provider subject to the priority set forth in subsection (d). Any shortfall in custodial assets shall have the same priority as outstanding payment obligations to customers under subsection (d)(2).\n##### (f) Additional powers\nIn addition to and not in derogation of the powers conferred and the duties imposed by this Act on the Comptroller or a State as conservator or receiver of a nonbank provider, the Comptroller or State, as applicable, shall have such additional powers and duties with respect to the nonbank provider as imposed on a conservator or receiver of an insured depository institution under any other provision of law.\n#### 9. Access to payments reserve accounts\n##### (a) Access\nTo obtain access to a payments reserve account in the same manner and to the same extent as such access would be granted to an insured depository institution, a registered covered provider may submit a request to the Board of Governors for such access.\n##### (b) Approval\nThe Board of Governors shall approve or deny such a request not later than 120 days after receipt of such request, which period may be extended by an additional 60 days. If the Board of Governors fails to act on such a request within such period, the request shall be deemed to be approved.\n##### (c) Enforcement authority in unusual and exigent circumstances\n**(1) In general**\nIn unusual and exigent circumstances, the Board of Governors may issue a directive that has the effect of a cease and desist order against a registered covered provider that uses a payments reserve account for purposes of noncompliance with requirements of sections 4 and 5 of this Act, if the Board of Governors submits a written notice to the covered State regulator and the Comptroller not less than 48 hours before issuing such directive.\n**(2) Unusual and exigent circumstances defined**\nNot later than 180 days after the date of the enactment of this Act and in consultation with the Conference of State Bank Supervisors, the Board of Governors shall issue rules to define the term unusual and exigent circumstances for purposes of paragraph (1).\n**(3) Review**\n**(A) Administrative review**\n**(i) In general**\nAfter a directive described in paragraph (1) has been issued with respect to a registered covered provider, such registered covered provider may object and present to the Board of Governors, in writing, the reasons why the directive should be modified or rescinded.\n**(ii) Automatic lapse of directive**\nIf, not later than 10 days after the receipt of a response described in clause (i), the Board of Governors does not affirm, modify, or rescind the directive, the directive shall automatically lapse.\n**(B) Judicial review**\n**(i) In general**\nIf the Board of Governors affirms or modifies a directive pursuant to subparagraph (A), any affected party may immediately thereafter petition the United States district court for the district in which the main office of the affected party is located, or in the United States District Court for the District of Columbia, to stay, modify, terminate, or set aside the directive.\n**(ii) Relief for extraordinary cause**\nUpon a showing of extraordinary cause, an affected party may petition for relief under clause (i) without first pursuing or exhausting the administrative review under subparagraph (A).\n#### 10. Effect on securities laws\n##### (a) Investment advisors act of 1940\nSection 202(a)(18) of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20132(a)(18) ) is amended by adding at the end the following: The term security does not include a balance with a registered covered provider, as such term is defined in section 2 of the PACE Act of 2026. .\n##### (b) Investment company act of 1940\nSection 2(a)(36) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a)(36) ) is amended by adding at the end the following: The term security does not include a balance with a registered covered provider, as such term is defined in section 2 of the PACE Act of 2026. .\n##### (c) Securities act of 1933\nSection 2(a)(1) of the Securities Act of 1933 ( 15 U.S.C. 77b(a)(1) ) is amended by adding at the end the following: The term security does not include a balance with a registered covered provider, as such term is defined in section 2 of the PACE Act of 2026. .\n##### (d) Securities exchange act of 1934\nSection 3(a)(10) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a)(10) ) is amended by adding at the end the following: The term security does not include a balance with a registered covered provider, as such term is defined in section 2 of the PACE Act of 2026. .\n##### (e) Securities investor protection act of 1970\nSection 16(14) of the Securities Investor Protection Act of 1970 ( 15 U.S.C. 78lll(14) ) is amended by adding at the end the following: The term security does not include a balance with a registered covered provider, as such term is defined in section 2 of the PACE Act of 2026. .",
      "versionDate": "2026-04-21",
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
        "updateDate": "2026-05-04T15:47:41Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8395ih.xml"
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
      "title": "PACE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-27T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PACE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-27T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Payments Access and Consumer Efficiency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-27T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the regulation of registered covered providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-27T11:48:26Z"
    }
  ]
}
```
