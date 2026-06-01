# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2528
- Title: Unleashing AI Innovation in Financial Services Act
- Congress: 119
- Bill type: S
- Bill number: 2528
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2528",
    "number": "2528",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Unleashing AI Innovation in Financial Services Act",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
        "item": [
          {
            "date": "2025-07-30T01:03:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-30T01:03:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NM"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NC"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2528is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2528\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Rounds (for himself, Mr. Heinrich , Mr. Tillis , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish AI Innovation Labs that permit certain persons to experiment with artificial intelligence without expectation of enforcement actions.\n#### 1. Short title\nThis Act may be cited as the Unleashing AI Innovation in Financial Services Act .\n#### 2. Definitions\n**(1) AI test project**\nThe term AI test project means a financial product or service that\u2014\n**(A)**\nfalls under the jurisdiction of a financial regulatory agency;\n**(B)**\nmakes substantial use of artificial intelligence; and\n**(C)**\nis, or may be, subject to a Federal regulation or Federal statute.\n**(2) Appropriate financial regulatory agency**\nThe term appropriate financial regulatory agency means\u2014\n**(A)**\nthe appropriate Federal banking agency, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ), with respect to an institution described in subsection (q) of that section;\n**(B)**\nthe Securities and Exchange Commission, with respect to an institution not described in subparagraph (A) that is\u2014\n**(i)**\nany broker or dealer that is registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(ii)**\nany investment company that is registered with the Commission under the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20131 et seq. );\n**(iii)**\nany investment adviser that is registered with the Commission under the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20131 et seq. );\n**(iv)**\nany clearing agency registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(v)**\nany nationally recognized statistical rating organization registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(vi)**\nany transfer agent registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(vii)**\nany exchange registered as a national securities exchange with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(viii)**\nany national securities association registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(ix)**\nany securities information processor registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(x)**\nthe Municipal Securities Rulemaking Board established under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(xi)**\nthe Public Company Accounting Oversight Board established under the Sarbanes-Oxley Act of 2002 ( 15 U.S.C. 7211 et seq. );\n**(xii)**\nthe Securities Investor Protection Corporation established under the Securities Investor Protection Act of 1970 ( 15 U.S.C. 78aaa et seq. ); and\n**(xiii)**\nany security-based swap execution facility, security-based swap data repository, security-based swap dealer, or major security-based swap participant registered with the Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ), with respect to the security-based swap activities of the person that require such person to be registered under such Act;\n**(C)**\nthe Bureau of Consumer Financial Protection, with respect to a covered person, as defined in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 ), that does not have an appropriate financial regulatory agency under subparagraph (A), (B), (D), or (E) of this paragraph;\n**(D)**\nthe National Credit Union Administration, with respect to an insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ); and\n**(E)**\nthe Federal Housing Finance Agency, with respect to\u2014\n**(i)**\na Federal Home Loan Bank;\n**(ii)**\nthe Federal Home Loan Bank System;\n**(iii)**\nthe Federal National Mortgage Association; and\n**(iv)**\nthe Federal Home Loan Mortgage Corporation.\n**(3) Artificial intelligence; ai**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(4) Commission**\nThe term Commission means the Securities and Exchange Commission.\n**(5) Federal securities laws**\nThe term Federal securities laws means\u2014\n**(A)**\nthe Securities Act of 1933 ( 15 U.S.C. 77a et seq. );\n**(B)**\nthe Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. );\n**(C)**\nthe Sarbanes-Oxley Act of 2002 ( 15 U.S.C. 7201 et seq. );\n**(D)**\nthe Trust Indenture Act of 1939 ( 15 U.S.C. 77aaa et seq. );\n**(E)**\nthe Investment Company Act of 1940 ( 15 U.S.C. 80a\u20131 et seq. );\n**(F)**\nthe Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20131 et seq. );\n**(G)**\nthe Jumpstart Our Business Startup Act ( Public Law 112\u2013106 ; 126 Stat. 306); and\n**(H)**\nthe Dodd-Frank Wall Street Reform and Consumer Protection Act ( Public Law 111\u2013203 ; 124 Stat. 1376).\n**(6) Financial product or service**\nThe term financial product or service \u2014\n**(A)**\nhas the meaning given the term in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 );\n**(B)**\nincludes\u2014\n**(i)**\nactivities that are financial in nature, as defined in section 4(k)(4) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843(k)(4) );\n**(ii)**\nany financial product or service provided by a person regulated by the Commission, as defined in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 ); and\n**(iii)**\nincludes the offer or sale of any security subject to the Federal securities laws; and\n**(C)**\ndoes not include the business of insurance.\n**(7) Financial regulatory agency**\nThe term financial regulatory agency means\u2014\n**(A)**\nthe Board of Governors of the Federal Reserve System;\n**(B)**\nthe Federal Deposit Insurance Corporation;\n**(C)**\nthe Office of the Comptroller of the Currency;\n**(D)**\nthe Securities and Exchange Commission;\n**(E)**\nthe Bureau of Consumer Financial Protection;\n**(F)**\nthe National Credit Union Administration; and\n**(G)**\nthe Federal Housing Finance Agency.\n**(8) Regulated entity**\nThe term regulated entity means an entity regulated by any financial regulatory agency.\n#### 3. Use of artificial intelligence by regulated financial entities\n##### (a) AI innovation labs\n**(1) Establishment**\nEach financial regulatory agency shall establish, or identify an office, division, or department of the agency that shall serve as, an AI Innovation Lab to enable regulated entities to experiment with AI test projects without unnecessary or unduly burdensome regulation or expectation of enforcement actions, pursuant to the approval of an application under paragraph (2).\n**(2) Applications**\n**(A) Submission**\n**(i) In general**\nA regulated entity may submit to the appropriate financial regulatory agency an application, on a form determined by the appropriate financial regulatory agency, to engage in an AI test project through the AI Innovation Lab established or identified under paragraph (1).\n**(ii) Contents**\nAn application submitted under clause (i) shall include\u2014\n**(I)**\na description of the AI test project proposed to be carried out by the regulated entity;\n**(II)**\nan alternative compliance strategy that\u2014\n**(aa)**\nidentifies a regulation issued by the appropriate financial regulatory agency that the regulated entity requests to be waived or modified; and\n**(bb)**\nproposes an alternative method for the regulated entity to comply with the regulation, including an explanation as to why the alternative method is essential to the operation of the entity and how the regulated entity would effectively manage risks associated with the AI test project;\n**(III)**\nan explanation of how under the strategy described in subclause (II), the AI test project\u2014\n**(aa)**\nwould serve the public interest, improve consumer or investor access to a financial product or service, or promote consumer or investor protection;\n**(bb)**\nwould enhance efficiency or operations, foster innovation or competitiveness, improve risk management and security, or enhance regulatory compliance;\n**(cc)**\nwould not present a systemic risk to the financial system of the United States;\n**(dd)**\nis consistent with the purposes of the anti-money laundering and countering the financing of terrorism obligations under subchapter II of chapter 53 of title 31, United States Code; and\n**(ee)**\nwould not present a national security risk to the United States;\n**(IV)**\na proposed date on which the AI test project would terminate and an explanation why such termination date would be appropriate;\n**(V)**\nproposed limitations on the size, scope, and growth of the AI test project;\n**(VI)**\na detailed business plan; and\n**(VII)**\nan estimate of the economic impact of the AI test project if approved.\n**(iii) Joint applications**\nTwo or more regulated entities may submit a joint application to the same financial regulatory agency under clause (i).\n**(iv) Regulations of other agencies**\n**(I) In general**\nA regulated entity may submit an application under this subparagraph that includes an alternative compliance strategy for a regulation issued or enforced by a financial regulatory agency that is not the appropriate financial regulatory agency for the regulated entity.\n**(II) Requirements**\nAn application described in subclause (I) shall be subject to the same requirements as an application described in clause (ii), except that\u2014\n**(aa)**\nthe regulated entity shall submit the application to the appropriate financial regulatory agency and the financial regulatory agency that issued or enforces the regulation that is the subject of the alternative compliance strategy; and\n**(bb)**\nthe AI test project may not take effect unless the appropriate financial regulatory agency and any other financial regulatory agency that issued or enforces the regulation that is the subject of the alternative compliance strategy jointly approve the application using the process described in subparagraph (B).\n**(v) Notice**\nA regulated entity that is regulated or supervised by more than 1 financial regulatory agency shall provide notice of any application submitted to the appropriate financial regulatory agency under this section to each financial regulatory agency by which it is regulated or supervised not later than 5 business days after the entity submits the application to the appropriate financial regulatory agency.\n**(B) Agency review**\n**(i) In general**\nExcept as provided in clause (iv), not later than 120 days after the date on which an application is submitted to the appropriate financial regulatory agency under subparagraph (A), the appropriate financial regulatory agency shall\u2014\n**(I)**\nreview the application; and\n**(II)**\nsubmit to the applicant in writing a determination of the agency.\n**(ii) Approval**\n**(I) In general**\nIf the applicant shows that it is more likely than not that the application meets the requirements for establishing an alternative compliance strategy and satisfies the standards described in subclauses (II) and (III) of subparagraph (A)(ii), the agency shall approve the application and notify the applicant in writing of\u2014\n**(aa)**\nthe regulation that is the subject of the alternative compliance strategy;\n**(bb)**\nthe terms of the alternative compliance strategy for the AI test project;\n**(cc)**\nthe date on which the AI test project will terminate;\n**(dd)**\nany limitations on the size, scope, or growth of the AI test project; and\n**(ee)**\nany additional limitations or conditions on the AI test project, as determined by the appropriate financial regulatory agency.\n**(II) Effect of approval**\nWith respect to an AI test project, except as provided in subclause (III), beginning on the date on which an application submitted under subparagraph (A) is approved and ending on the date described in subclause (I)(cc)\u2014\n**(aa)**\nthe appropriate financial regulatory agency may enforce a regulation described in subclause (I)(aa) only in the manner set out in the alternative compliance strategy described in subclause (I)(bb); and\n**(bb)**\na financial regulatory agency that is not the appropriate financial regulatory agency may not enforce a regulation described in subclause (I)(aa).\n**(III) Enforcement by another financial regulatory agency**\nWith respect to an AI test project, a financial regulatory agency other than the appropriate financial regulatory agency that approves an application under subparagraph (A)(iv) may enforce a regulation described in subclause (I)(aa) if the alternative compliance strategy described in subclause (I)(bb) provides for enforcement by such financial regulatory agency.\n**(IV) Rule of construction**\nNothing in this clause may be construed to limit the authority of a financial regulatory agency to take an enforcement action against a regulated entity with respect to fraud or for engaging in an unsafe or unsound practice relating to an AI test project.\n**(iii) Denial**\n**(I) In general**\nIf an agency denies an application submitted under subparagraph (A), the agency\u2014\n**(aa)**\nshall submit to the applicant a written notice explaining the reason for denial; and\n**(bb)**\nmay not take an enforcement action related to the proposed AI test project against the applicant earlier than the date that is 30 days after the date on which the agency submits the written notice described in item (aa).\n**(II) Resubmittals**\nEach time an application submitted under subparagraph (A) is denied, the regulated entity\u2014\n**(aa)**\nmay submit an amended application after receiving feedback from the agency making such denial; and\n**(bb)**\nmay not resubmit more than 2 applications that are substantially similar to the denied application.\n**(III) Injunctive relief**\nA financial regulatory agency, by and through its own attorneys, may file a civil action in an appropriate United States district court to enjoin an AI test project if the agency determines that the AI test project\u2014\n**(aa)**\npresents an immediate danger to consumers or investors; or\n**(bb)**\npresents a risk\u2014\n(AA)\nto financial markets;\n(BB)\nin the case of an AI test project engaged in by an insured depository institution or an insured credit union, of loss to a Federal deposit or share insurance fund;\n(CC)\nof a violation of anti-money laundering and countering the financing of terrorism obligations under subchapter II of chapter 53 of title 31, United States Code; or\n(DD)\nto the national security of the United States.\n**(iv) Extension**\nIf the financial regulatory agency needs additional time, the agency may extend the approval deadline by 120 days. After the expiration of the 120-day extension period, if the agency has not made a determination on the application, the application will automatically be deemed approved and effective.\n**(C) Data security**\nAll data supplied by sponsors of AI test projects to a financial regulatory agency submitted under this section shall be stored and maintained in a secure manner by the financial regulatory agency, consistent with applicable data security standards.\n**(D) Regulations**\nNot later than 180 days after the date of enactment of this Act, each financial regulatory agency shall promulgate regulations that\u2014\n**(i)**\nshall be published in the Federal Register and provide a 60-day period for public notice and comment; and\n**(ii)**\ninclude\u2014\n**(I)**\nprocedures for modifying the AI test projects that are approved by the agency;\n**(II)**\nconsequences for failure to comply with the terms of an alternative compliance strategy;\n**(III)**\na requirement that an AI test project will terminate not earlier than 1 year after the AI test project is approved;\n**(IV)**\nprocedures to extend the termination date described in subclause (III);\n**(V)**\nprocedures for confidentiality; and\n**(VI)**\nprocedures for coordinating decisions relating to applications submitted jointly by multiple regulated entities or applications submitted to more than one financial regulatory agency.\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, and each year for 7 years thereafter, each financial regulatory agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives an annual report on the outcomes of AI test projects. A report under this subsection may not include the names of participating entities or any proprietary or confidential business information. A report under this subsection shall include aggregated findings, trends, and lessons learned from the AI test projects.\n##### (c) Rule of construction\nNothing in this section may be construed to limit the authority of a financial regulatory agency to take an enforcement action against a regulated entity with respect to fraud relating to an AI test project.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4801",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Unleashing AI Innovation in Financial Services Act",
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
        "updateDate": "2025-09-16T14:32:07Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2528is.xml"
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
      "title": "Unleashing AI Innovation in Financial Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unleashing AI Innovation in Financial Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish AI Innovation Labs that permit certain persons to experiment with artificial intelligence without expectation of enforcement actions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:20Z"
    }
  ]
}
```
