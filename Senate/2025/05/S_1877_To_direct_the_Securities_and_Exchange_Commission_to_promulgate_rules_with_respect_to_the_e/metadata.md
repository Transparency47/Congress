# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1877?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1877
- Title: Improving Disclosure for Investors Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1877
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1877",
    "number": "1877",
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
    "title": "Improving Disclosure for Investors Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T17:19:51Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T17:19:51Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "SD"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "NC"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "GA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "MT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "AZ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1877is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1877\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Tillis (for himself, Mr. Hickenlooper , Mrs. Shaheen , Mr. Rounds , Mr. Peters , Mr. Budd , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Securities and Exchange Commission to promulgate rules with respect to the electronic delivery of certain required disclosures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Disclosure for Investors Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Securities and Exchange Commission.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nan investment company, as defined in section 3(a)(1) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(a)(1) ), that is registered under such Act;\n**(B)**\na business development company, as defined in section 2(a) the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a) );\n**(C)**\na registered broker or dealer, as those terms are defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) );\n**(D)**\na registered municipal securities dealer, as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) );\n**(E)**\na registered government securities broker or government securities dealer, as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) );\n**(F)**\na registered investment adviser, as defined in section 202(a) of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20131(a) );\n**(G)**\na registered transfer agent, as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ); or\n**(H)**\na registered funding portal, as defined in section 3(a) of the Securities Exchange Act of 1934) ( 15 U.S.C. 78c(a) ).\n**(3) Electronic delivery**\nThe term electronic delivery , with respect to regulatory documents, includes\u2014\n**(A)**\nthe direct delivery of such regulatory document to an electronic address of an investor;\n**(B)**\nthe posting of such regulatory document to a website and direct electronic delivery of an appropriate notice of the availability of the regulatory document to the investor; and\n**(C)**\nan electronic method reasonably designed to ensure receipt of such regulatory document by the investor.\n**(4) Regulatory documents**\nThe term regulatory documents includes\u2014\n**(A)**\nprospectuses meeting the requirements of section 10(a) of the Securities Act of 1933 ( 15 U.S.C. 77j(a) );\n**(B)**\nsummary prospectuses meeting the requirements of section 230.498 or 230.498A of title 17, Code of Federal Regulations;\n**(C)**\nStatements of Additional Information, as defined in section 270.30e\u20133(h) of title 17, Code of Federal Regulations;\n**(D)**\nannual and semiannual reports to investors meeting the requirements of section 30(e) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u201329(e) );\n**(E)**\nnotices meeting the requirements of section 270.19a\u20131 of title 17, Code of Federal Regulations;\n**(F)**\nconfirmations and account statements meeting the requirements of section 240.10b\u201310 of title 17, Code of Federal Regulations;\n**(G)**\nproxy statements meeting the requirements of section 240.14a\u20133 of title 17, Code of Federal Regulations;\n**(H)**\nprivacy notices meeting the requirements of Regulation S\u2013P under subpart A of part 248 of title 17, Code of Federal Regulations;\n**(I)**\naffiliate marketing notices meeting the requirements of Regulation S\u2013AM under subpart B of part 248 of title 17, Code of Federal Regulations; and\n**(J)**\nall other regulatory documents required to be delivered by covered entities to investors under the securities laws and the rules and regulations of the Commission and the self-regulatory organizations.\n**(5) Securities laws**\nThe term securities laws has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ).\n**(6) Self-regulatory organization**\nThe term self-regulatory organization means a self-regulatory organization, as defined in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ).\n**(7) Website**\nThe term website means an internet website or other digital, internet, or electronic-based information repository, such as a mobile application, to which an investor of a covered entity has been provided reasonable access.\n#### 3. Electronic delivery\n##### (a) Promulgation of rules\nNot later than 180 days after the date of the enactment of this section, the Commission shall propose and, not later than 1 year after the date of the enactment of this section, the Commission shall finalize, rules, regulations, amendments, or interpretations, as appropriate, to allow a covered entity to satisfy the obligation of the entity to deliver regulatory documents required under the securities laws to investors using electronic delivery.\n##### (b) Required provisions\nRules, regulations, amendments, or interpretations the Commission promulgates pursuant to subsection (a) shall\u2014\n**(1)**\nwith respect to investors that do not receive all regulatory documents by electronic delivery, provide for\u2014\n**(A)**\ndelivery of an initial communication in paper form regarding electronic delivery;\n**(B)**\na transition period not to exceed 180 days until such regulatory documents are delivered to such investors by electronic delivery; and\n**(C)**\nduring a period not to exceed 2 years following the transition period set forth in subparagraph (B), delivery of an annual notice in paper form solely reminding such investors of the ability to opt out of electronic delivery at any time and receive paper versions of regulatory documents;\n**(2)**\nset forth requirements for the content of the initial communication described in paragraph (1)(A);\n**(3)**\nset forth requirements for the timing of delivery of a notice of website availability of regulatory documents and the content of the appropriate notice described in section 2(3)(B);\n**(4)**\nprovide a mechanism for investors to opt out of electronic delivery at any time and receive paper versions of regulatory documents;\n**(5)**\nrequire measures reasonably designed to identify and remediate failed electronic deliveries of regulatory documents;\n**(6)**\nset forth minimum requirements regarding readability and retainability for regulatory documents that are delivered electronically; and\n**(7)**\nfor covered entities other than brokers, dealers, investment advisers registered with the Commission, and investment companies, require measures reasonably designed to ensure the confidentiality of personal information in regulatory documents that are delivered to investors electronically.\n##### (c) Treatment of revisions not completed in a timely manner\nIf the Commission fails to finalize the rules, regulations, amendments, or interpretations required under subsection (a) before the date specified in such subsection\u2014\n**(1)**\na covered entity may deliver regulatory documents using electronic delivery in accordance with subsection (b); and\n**(2)**\nsuch electronic delivery shall be deemed to satisfy the obligation of the covered entity to deliver regulatory documents required under the securities laws.\n##### (d) Other required actions\n**(1) Review of rules**\nThe Commission shall\u2014\n**(A)**\nnot later than 180 days after the date of enactment of this Act, conduct a review of the rules and regulations of the Commission to determine whether any such rules or regulations require delivery of written documents to investors; and\n**(B)**\nnot later than 1 year after the date of enactment of this Act, promulgate amendments to such rules or regulations to provide that any requirement to deliver a regulatory document in writing may be satisfied by electronic delivery.\n**(2) Actions by self-regulatory organizations**\nEach self-regulatory organization shall adopt rules and regulations, or amend the rules and regulations of the self-regulatory organization, consistent with this Act and consistent with rules, regulations, amendments, or interpretations finalized by the Commission pursuant to subsection (a).\n**(3) Applicability**\nThis subsection shall not apply to a rule or regulation issued pursuant to a Federal statute if that Federal statute specifically requires delivery of written documents to investors.\n##### (e) Exemption from certain requirements\nSection 101(c) of the Electronic Signatures in Global and National Commerce Act ( 15 U.S.C. 7001(c) ) shall not apply with respect to a regulatory document delivered in accordance with this section.\n##### (f) Rule of construction\nNothing in this section shall be construed as altering the substance or timing of any regulatory document obligation under the securities laws or regulations of a self-regulatory organization.",
      "versionDate": "2025-05-22",
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
        "updateDate": "2025-06-03T17:59:30Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1877is.xml"
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
      "title": "Improving Disclosure for Investors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Disclosure for Investors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Securities and Exchange Commission to promulgate rules with respect to the electronic delivery of certain required disclosures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:18Z"
    }
  ]
}
```
