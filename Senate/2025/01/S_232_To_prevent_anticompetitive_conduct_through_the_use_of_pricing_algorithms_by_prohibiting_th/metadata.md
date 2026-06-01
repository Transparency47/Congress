# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/232?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/232
- Title: Preventing Algorithmic Collusion Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 232
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/232",
    "number": "232",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Preventing Algorithmic Collusion Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T21:14:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "HI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NH"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s232is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 232\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Ms. Klobuchar (for herself, Mr. Wyden , Mr. Durbin , Mr. Welch , Ms. Hirono , Mr. Luj\u00e1n , Mrs. Shaheen , Mr. Murphy , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prevent anticompetitive conduct through the use of pricing algorithms by prohibiting the use of pricing algorithms that can facilitate collusion through the use of nonpublic competitor data, creating an antitrust law enforcement audit tool, increasing transparency, and enforcing violations through the Sherman Act and Federal Trade Commission Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Algorithmic Collusion Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Antitrust laws**\nThe term antitrust laws \u2014\n**(A)**\nhas the meaning given that term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ); and\n**(B)**\nincludes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ).\n**(2) Commercial terms**\nThe term commercial terms means\u2014\n**(A)**\nlevel of service;\n**(B)**\navailability;\n**(C)**\noutput, including quantities of products produced or distributed or the amount or level of service provided; or\n**(D)**\nrebates or discounts made available.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Distribute; distribution; distributing**\nThe terms distribute , distribution , and distributing include selling, licensing, providing access to, or otherwise making available by any means, including through a subscription or the sale of a service.\n**(5) Nonpublic competitor data**\nThe term nonpublic competitor data \u2014\n**(A)**\nmeans nonpublic data that is derived from or otherwise provided by another person that competes in the same market as a person, or a related market; and\n**(B)**\ndoes not include information distributed, reported, or otherwise communicated in a way that does not reveal any underlying data from a competitor, such as narrative industry reports, news reports, business commentaries, or generalized industry survey results.\n**(6) Nonpublic data**\nThe term nonpublic data means information that is not widely available or easily accessible to the public, including information about price, commercial terms, and related products or services, regardless of whether the data is attributable to a specific competitor or anonymized.\n**(7) Person**\nThe term person has the meaning given that term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ).\n**(8) Price**\nThe term price means the amount of money or other thing of value, whether tangible or not, expected, required, or given in payment for any product or service, including compensation paid to an employee or independent contractor for services provided.\n**(9) Pricing algorithm**\nThe term pricing algorithm means any computational process, including a computational process derived from machine learning or other artificial intelligence techniques, that processes data to recommend or set a price or commercial term that is in or affecting interstate or foreign commerce.\n#### 3. Competition law enforcement audit\n##### (a) In general\nA person using or distributing a pricing algorithm, upon a written request by the Attorney General or the Commission, shall, not later than 30 days after the date of the written request, or any later date approved by the Attorney General or the Commission, respectively, provide to the Attorney General or the Commission, respectively, a written report on each pricing algorithm identified in the request.\n##### (b) Report contents\nEach report under subsection (a) shall include\u2014\n**(1)**\ninformation on whether the person is responsible for the development or distribution of the pricing algorithm, or whether a third party is responsible for the development or distribution of the pricing algorithm, including the identity and contact information of any other person responsible for the development or distribution of the pricing algorithm;\n**(2)**\ninformation on whether the pricing algorithm autonomously sets prices or commercial terms and whether there is human review of any recommendation or decision of the pricing algorithm;\n**(3)**\nan explanation of the rules or processes that the pricing algorithm uses to set or recommend prices or commercial terms;\n**(4)**\na description of all data the pricing algorithm uses to set or recommend prices or commercial terms, including data used to train the algorithm;\n**(5)**\nall sources and collection processes, including the frequency of collection, of any data that the pricing algorithm uses to set or recommend prices or commercial terms;\n**(6)**\nwhether the pricing algorithm engages in price discrimination by setting or recommending different prices or commercial terms for\u2014\n**(A)**\ndifferent customers seeking identical or nearly identical products or services, and if so, the factors used in differentiating among such customers; or\n**(B)**\ndifferent employees or independent contractors providing substantially similar services, and if so, the factors used in differentiating among such employees or independent contractors; and\n**(7)**\nany changes made to the pricing algorithm between the date of receipt of the request under subsection (a) and the date of certification under subsection (c).\n##### (c) Certification of report\nThe Chief Executive Officer, Chief Economist, Chief Technology Officer, or a corporate officer of similar authority of a person shall certify, under penalty of perjury, the accuracy of a report under subsection (a) submitted by the person.\n##### (d) Confidentiality\nAll information submitted in a report under subsection (a) shall be treated as confidential and shall be considered to be privileged and confidential trade secrets and commercial or financial information exempt under subsection (b)(4) of section 552 of title 5, United States Code, from being made available to the public under subsection (a) of that section.\n##### (e) Information sharing\n**(1) In general**\nA report under subsection (a) may be shared\u2014\n**(A)**\nbetween the Department of Justice and the Commission; and\n**(B)**\nwith the National Institute of Standards and Technology for technical assistance in understanding the report.\n**(2) Limitation**\nThe National Institute of Standards and Technology shall not disclose the contents of a report shared under paragraph (1) or the analysis of the report by the National Institute of Standards and Technology to any person, except the Department of Justice or Commission, whichever sought the technical assistance.\n##### (f) Rules of construction\nNothing in this section shall\u2014\n**(1)**\nlimit the ability of the Commission or the Attorney General to issue a civil investigative demand, to issue a subpoena, to seek discovery in the course of litigation, or otherwise obtain information through other means available to the Commission or the Attorney General; or\n**(2)**\nrestrict the use of information submitted in a report under subsection (a) in the course of a formal investigation, enforcement action, litigation, trial, or other proceeding, in accordance with the confidentiality procedures applicable to such proceeding.\n#### 4. Preventing collusive activity in pricing algorithms\n##### (a) In general\nIt shall be unlawful for a person to use or distribute any pricing algorithm that uses, incorporates, or was trained with nonpublic competitor data.\n##### (b) Civil action\nIf the Commission or the Attorney General has reason to believe that a person has violated subsection (a), the Commission, in its own name by any of its attorneys designated by it for such purpose, or the Attorney General may bring a civil action against the person in an appropriate district court of the United States to seek to recover\u2014\n**(1)**\na civil penalty of\u2014\n**(A)**\nnot less than $10,000, adjusted for inflation on the basis of the Consumer Price Index, for each day during which the violation occurs or continues to occur; or\n**(B)**\nthe sum of the price of each product or service sold using the pricing algorithm in violation of subsection (a); and\n**(2)**\nother appropriate relief, including an injunction or other equitable relief.\n##### (c) Effective Date\nSubsection (a) shall take effect on the date that is 90 days after the date of enactment of this Act.\n#### 5. Algorithmic price fixing\n##### (a) Presumption of agreement\nWith respect to the use of a pricing algorithm that would violate section 4 of this Act, there shall be a presumption for purposes of section 1 of the Sherman Act ( 15 U.S.C. 1 ) that the defendant entered into an agreement, contract, combination, or conspiracy in restraint of trade and for purposes of section 5(a) of the Federal Trade Commission Act ( 15 U.S.C. 45(a) ) that the defendant has engaged in an unfair method of competition if the plaintiff establishes that\u2014\n**(1)**\nthe defendant distributed the pricing algorithm to 2 or more persons\u2014\n**(A)**\nwith the intent that the pricing algorithm be used to set or recommend a price or commercial term of a product or service in the same market or a related market; or\n**(B)**\nand 2 or more persons used the pricing algorithm to set or recommend a price or commercial term of a product or service in the same market or a related market; or\n**(2)**\n**(A)**\nthe defendant used the pricing algorithm to set or recommend a price or commercial term of a product or service; and\n**(B)**\nthe pricing algorithm was used by another person to set or recommend a price or commercial term of a product or service in the same market or a related market.\n##### (b) Rebuttal\nThe presumption under subsection (a) shall not apply to a defendant if the defendant did not develop or distribute the pricing algorithm and the defendant demonstrates by clear and convincing evidence that the defendant did not have actual knowledge or could not have reasonably known that the pricing algorithm used nonpublic competitor data.\n##### (c) Joint and several liability\nIn a civil case in which the presumption under subsection (a) is applicable, any persons that distributed the pricing algorithm and knew, or could reasonably have known, that the pricing algorithm would use, incorporate, or be trained with nonpublic competitor data shall be jointly and severally liable for any violation of section 1 of the Sherman Act ( 15 U.S.C. 1 ) or section 5(a) of the Federal Trade Commission Act ( 15 U.S.C. 45(a) ).\n##### (d) Relation to antitrust laws\nNothing in this section shall impair or limit the applicability of the antitrust laws.\n##### (e) Effective date\nSubsection (a) shall take effect on the date that is 90 days after the date of enactment of this Act.\n#### 6. Transparency in pricing algorithms\n##### (a) In general\nAny person that has $5,000,000 or more in annual revenue that uses a pricing algorithm to recommend or set a price or commercial term shall clearly disclose, as applicable\u2014\n**(1)**\nto a customer, before the customer purchases the relevant product or service, that the price or a commercial term, as applicable, is set or recommended by a pricing algorithm; and\n**(2)**\nto a current or prospective employee or independent contractor that the price or a commercial term for services rendered as an employee or independent contractor is set or recommended by a pricing algorithm.\n##### (b) Additional disclosures\n**(1) Price discrimination**\nIf applicable, a disclosure under subsection (a) shall state that the pricing algorithm sets or recommends different prices or commercial terms for\u2014\n**(A)**\ndifferent customers seeking identical or nearly identical products or services; or\n**(B)**\nemployees or independent contractors providing substantially similar services.\n**(2) Third-party algorithm**\nIf applicable, a disclosure under subsection (a) shall\u2014\n**(A)**\nstate that the pricing algorithm was developed or distributed by a person other than the person making the disclosure; and\n**(B)**\nprovide the identity of the person that developed or distributed the pricing algorithm.\n##### (c) Enforcement\nFailure to provide a disclosure under subsection (a), including the information required under subsection (b), shall constitute an unfair or deceptive act or practice under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ).\n##### (d) Civil action\nIf the Commission has reason to believe that a person has violated subsection (a) or (b), the Commission, in its own name by any of its attorneys designated by it for such purpose, may bring a civil action in an appropriate district court of the United States to recover\u2014\n**(1)**\na civil penalty of not less than $5,000, adjusted for inflation on the basis of the Consumer Price Index, for each day during which the violation occurs or continues to occur; and\n**(2)**\nother appropriate relief, including an injunction or other equitable relief.\n##### (e) Relation to antitrust laws\nNothing in this section shall impair or limit the applicability of the antitrust laws.\n#### 7. FTC study\nNot later than 2 years after the date of enactment of this Act, the Commission shall publish the results of a study of the use of pricing algorithms, including information on\u2014\n**(1)**\nthe prevalence of pricing algorithms;\n**(2)**\nthe frequency of the use of pricing algorithms to engage in price or wage discrimination;\n**(3)**\nthe potential for persons to use pricing algorithms to engage in behavior that increases prices, lowers wages, reduces output, lowers quality, deters innovation, or otherwise harms the competitive process outside of the price fixing context;\n**(4)**\nthe potential benefits or efficiencies of pricing algorithms;\n**(5)**\nany industries, sectors, or markets in which pricing algorithms may warrant additional oversight or regulation to protect competition and consumers; and\n**(6)**\nrecommendations for additional legislation, regulation, or rulemaking relating to competition and consumer protection issues arising from the use of pricing algorithms.",
      "versionDate": "2025-01-23",
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
        "name": "Commerce",
        "updateDate": "2025-02-25T12:47:28Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s232is.xml"
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
      "title": "Preventing Algorithmic Collusion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:48Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Algorithmic Collusion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent anticompetitive conduct through the use of pricing algorithms by prohibiting the use of pricing algorithms that can facilitate collusion through the use of nonpublic competitor data, creating an antitrust law enforcement tool, increasing transparency, and enforcing violations through the Sherman Act and Federal Trade Commission Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:34Z"
    }
  ]
}
```
