# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/490
- Title: Protecting Americans’ Privacy Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 490
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-05-13T15:24:59Z
- Update date including text: 2025-05-13T15:24:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S796-797)
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S796-797)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/490",
    "number": "490",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protecting Americans\u2019 Privacy Act of 2025",
    "type": "S",
    "updateDate": "2025-05-13T15:24:59Z",
    "updateDateIncludingText": "2025-05-13T15:24:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S796-797)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-07T00:48:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s490is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 490\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Schumer (for himself, Mr. Wyden , Ms. Warren , Mr. Peters , Mrs. Murray , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide that unauthorized access to the central payment systems of the Bureau of the Fiscal Service is unlawful.\n#### 1. Short title\nThis Act may be cited as the Protecting Americans\u2019 Privacy Act of 2025 .\n#### 2. Unauthorized access to the central payment systems of the Bureau of the Fiscal Service\n##### (a) Prohibitions\n**(1) In general**\nIt shall be unlawful for an individual to knowingly access or exercise administrative control over any public money receipt or payment system of the Department of the Treasury (including any payment system of the Bureau of the Fiscal Service (or any successor thereof)) if the individual\u2014\n**(A)**\nis not\u2014\n**(i)**\na Federal employee; or\n**(ii)**\na Federal contractor whose current continuous service in a position on an agency's contract, as of the date of such access, is for a period of at least 1 year;\n**(B)**\nis a Federal employee\u2014\n**(i)**\nwho is employed as the chief executive officer, chief financial officer, chief operating officer, or a position of similar stature at a covered entity;\n**(ii)**\nwho serves on the Board of Directors of a covered entity;\n**(iii)**\nwho has control over a covered entity; or\n**(iv)**\nwhose current continuous service in a position in the civil service (as that term is defined in section 2101 of title 5, United States Code), as of the date of such access, is for a period of less than 1 year; or\n**(C)**\nis a covered employee who\u2014\n**(i)**\nhas a conflict of interest as described in section 208 of title 18, United States Code, with respect to such central payment system, or\n**(ii)**\nhas not signed a written ethics agreement with either the covered employee's respective agency or the Office of Government Ethics.\n**(2) Facilitation of access**\nIt shall be unlawful for an individual to facilitate access to or the exercise of administrative control over any such public money receipt or payment system, or to knowingly permit such access or exercise of control, which such individual knows or should know is in violation of paragraph (1).\n##### (b) Enforcement by individuals\n**(1) In general**\nAny persons harmed by a violation of subsection (a) may file a civil action in any district court of the United States or State court of general jurisdiction to recover from the individual who engaged in the violation appropriate relief described in paragraph (2).\n**(2) Relief**\nIn an action under this subsection, appropriate relief includes\u2014\n**(A)**\npreliminary and other equitable or declaratory relief, as appropriate;\n**(B)**\ndamages as described in paragraph (3);\n**(C)**\npunitive damages, as appropriate; and\n**(D)**\nreasonable attorney\u2019s fees and other reasonable litigation costs.\n**(3) Damages**\nIn an action under this subsection, a court may assess as damages an amount equal to the greater of\u2014\n**(A)**\nthe sum of the actual damages suffered by the plaintiff; or\n**(B)**\n$250,000 for each unauthorized access relating to the plaintiff.\n**(4) Joint and several liability**\nAny individual who violates subsection (a)(1) and any individual who violates subsection (a)(2) shall be jointly and severally liable to the extent such violations relate to the same access.\n##### (c) Definitions\nIn this section:\n**(1) Agency**\nThe term agency \u2014\n**(A)**\nhas the meaning given the term Executive agency in section 105 of title 5, United States Code; and\n**(B)**\nincludes each component of the Executive Office of the President, including each such component established under title 3, United States Code.\n**(2) Control**\nThe term control means, with respect to an entity\u2014\n**(A)**\nownership of, or the power to vote, more than 50 percent of the outstanding shares of any class of voting security of the entity;\n**(B)**\ncontrol over the election of a majority of the directors of the entity (or of individuals exercising similar functions); or\n**(C)**\nthe power to exercise a controlling influence over the management of the entity.\n**(3) Covered employee**\nThe term covered employee includes the following individuals:\n**(A)**\nEach individual who is\u2014\n**(i)**\na noncareer employee; and\n**(ii)**\ndescribed in any of paragraphs (3) through (8) of section 13103(f) of title 5, United States Code.\n**(B)**\nEach individual serving in a position with respect to which a determination has been made under section 7511(b)(2) of title 5, United States Code.\n**(C)**\nEach special Government employee, as defined in section 202(a) of title 18, United States Code.\n**(4) Covered entity**\nThe term covered entity means a corporation (and the subsidiaries it controls), company, association, firm, partnership, society, joint stock company, or any other organization or institution, including an organization described in section 501(c) of the Internal Revenue Code.\n**(5) Federal contractor**\nThe term Federal contractor means an individual, other than a Federal employee, working under a contract with an agency.\n**(6) Federal employee**\nThe term Federal employee means an individual employed by or holding office in an agency.\n**(7) Noncareer employee**\nThe term noncareer employee means an individual who is\u2014\n**(A)**\nserving in a position to which the President appointed the individual (without regard to whether the advice and consent of the Senate was required with respect to that appointment), other than an individual who is\u2014\n**(i)**\na member of a uniformed service, as that term is defined in section 210(m) of the Social Security Act ( 42 U.S.C. 410(m) ); or\n**(ii)**\na member of the Foreign Service serving under a career appointment, as described in section 301 of the Foreign Service Act of 1980 ( 22 U.S.C. 3941 );\n**(B)**\na noncareer appointee, as that term is defined in section 3132(a) of title 5, United States Code;\n**(C)**\nserving in a position in a Federal executive system (other than the Senior Executive Service established under subchapter II of chapter 31 of title 5, United States Code), if appointment to the position is not made through merit-based procedures; or\n**(D)**\nserving in a position with respect to which a determination has been made under section 7511(b)(2) of title 5, United States Code.\n##### (d) No inference\nNothing in this section shall be construed as creating any inference as to whether any act which occurred prior to the enactment of this Act was lawful or otherwise permitted.\n#### 3. Confidentiality of returns and return information under Internal Revenue Code of 1986\n##### (a) In general\nSection 6103 of the Internal Revenue Code of 1986 is amended by redesignating subsection (q) as subsection (r) and by inserting after subsection (p) the following new subsection:\n(q) Prohibition on disclosure to certain employees Notwithstanding any other provision of this section, no return or return information shall be disclosed by means of access to any public money receipt or payment system of the Department of the Treasury (including any payment system of the Bureau of the Fiscal Service (or any successor thereof)) to any individual described in subparagraph (B) or (C) of section 2(a)(1) of the Protecting Americans\u2019 Privacy Act of 2025 . .\n##### (b) Civil damages for unauthorized inspection or disclosure\n**(1) In general**\nSubsection (a) of section 7431 of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Inspection or disclosure by certain employees If any individual described in subparagraph (B) or (C) of section 2(a)(1) of the Protecting Americans\u2019 Privacy Act of 2025 knowingly, or by reason of negligence, inspects or discloses any return or return information with respect to a taxpayer in violation of section 6103(q), such taxpayer may bring a civil action for damages against such person in a district court of the United States. In any action brought under this paragraph, subsection (c)(1)(A) shall be applied by substituting $250,000 for $1,000 . .\n**(2) Conforming amendment**\nParagraph (1) of section 7431(a) of such Code is amended by striking If any in paragraph (1) and inserting Except as provided in paragraph (3), if any .\n##### (c) No inference\nNothing in the amendments made by this section shall be construed as creating any inference as to whether any disclosure or inspection prior to the enactment of this Act was lawful or permitted by section 6103 of the Internal Revenue Code of 1986.",
      "versionDate": "2025-02-06",
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
        "name": "Taxation",
        "updateDate": "2025-05-02T15:03:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s490",
          "measure-number": "490",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s490v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Americans\u2019 Privacy Act of 2025</strong></p><p>This bill makes it unlawful for certain individuals to access or exercise administrative control over any Department of the Treasury public money receipt or payment system. The bill also makes it unlawful to disclose return or return information to certain individuals by means of access to such Treasury system.</p><p>Under the bill, it is unlawful for an individual to knowingly access or exercise administrative control over any Treasury (including the Bureau of Fiscal Service) public money receipt or payment system if the individual is</p><ul><li>not a federal employee or federal contractor (with at least one year of continuous service);</li><li>a federal employee who holds a certain position within or is the board member of a business, organization, or institution;</li><li>in a civil service position for less than one year (continuously); or</li><li>an employee who meets certain other requirements and who has a conflict of interest or has not signed a written ethics agreement.</li></ul><p>The bill also makes it unlawful to (1) facilitate access to or administrative control over any Treasury public money receipt or payment system to such individuals, or (2) disclose return or return information to such individuals by means of access to such Treasury system.</p><p>Finally, the bill provides that persons harmed by the unlawful access to such Treasury system may file a civil action for</p><ul><li>preliminary and other equitable or declaratory relief,</li><li>damages (the greater of $250,000\u00a0or actual damages),</li><li>punitive damages, and</li><li>attorney\u2019s fees and litigation costs.</li></ul>"
        },
        "title": "Protecting Americans\u2019 Privacy Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s490.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Americans\u2019 Privacy Act of 2025</strong></p><p>This bill makes it unlawful for certain individuals to access or exercise administrative control over any Department of the Treasury public money receipt or payment system. The bill also makes it unlawful to disclose return or return information to certain individuals by means of access to such Treasury system.</p><p>Under the bill, it is unlawful for an individual to knowingly access or exercise administrative control over any Treasury (including the Bureau of Fiscal Service) public money receipt or payment system if the individual is</p><ul><li>not a federal employee or federal contractor (with at least one year of continuous service);</li><li>a federal employee who holds a certain position within or is the board member of a business, organization, or institution;</li><li>in a civil service position for less than one year (continuously); or</li><li>an employee who meets certain other requirements and who has a conflict of interest or has not signed a written ethics agreement.</li></ul><p>The bill also makes it unlawful to (1) facilitate access to or administrative control over any Treasury public money receipt or payment system to such individuals, or (2) disclose return or return information to such individuals by means of access to such Treasury system.</p><p>Finally, the bill provides that persons harmed by the unlawful access to such Treasury system may file a civil action for</p><ul><li>preliminary and other equitable or declaratory relief,</li><li>damages (the greater of $250,000\u00a0or actual damages),</li><li>punitive damages, and</li><li>attorney\u2019s fees and litigation costs.</li></ul>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s490"
    },
    "title": "Protecting Americans\u2019 Privacy Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Americans\u2019 Privacy Act of 2025</strong></p><p>This bill makes it unlawful for certain individuals to access or exercise administrative control over any Department of the Treasury public money receipt or payment system. The bill also makes it unlawful to disclose return or return information to certain individuals by means of access to such Treasury system.</p><p>Under the bill, it is unlawful for an individual to knowingly access or exercise administrative control over any Treasury (including the Bureau of Fiscal Service) public money receipt or payment system if the individual is</p><ul><li>not a federal employee or federal contractor (with at least one year of continuous service);</li><li>a federal employee who holds a certain position within or is the board member of a business, organization, or institution;</li><li>in a civil service position for less than one year (continuously); or</li><li>an employee who meets certain other requirements and who has a conflict of interest or has not signed a written ethics agreement.</li></ul><p>The bill also makes it unlawful to (1) facilitate access to or administrative control over any Treasury public money receipt or payment system to such individuals, or (2) disclose return or return information to such individuals by means of access to such Treasury system.</p><p>Finally, the bill provides that persons harmed by the unlawful access to such Treasury system may file a civil action for</p><ul><li>preliminary and other equitable or declaratory relief,</li><li>damages (the greater of $250,000\u00a0or actual damages),</li><li>punitive damages, and</li><li>attorney\u2019s fees and litigation costs.</li></ul>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s490"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s490is.xml"
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
      "title": "Protecting Americans\u2019 Privacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Americans\u2019 Privacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that unauthorized access to the central payment systems of the Bureau of the Fiscal Service is unlawful.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:39Z"
    }
  ]
}
```
