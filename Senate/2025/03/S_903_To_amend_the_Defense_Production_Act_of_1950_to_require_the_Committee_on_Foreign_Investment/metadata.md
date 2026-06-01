# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/903
- Title: PASS Act
- Congress: 119
- Bill type: S
- Bill number: 903
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-02-19T20:32:08Z
- Update date including text: 2026-02-19T20:32:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/903",
    "number": "903",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "PASS Act",
    "type": "S",
    "updateDate": "2026-02-19T20:32:08Z",
    "updateDateIncludingText": "2026-02-19T20:32:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T20:41:48Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WY"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "SD"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "ND"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ND"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s903is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 903\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Rounds (for himself, Ms. Cortez Masto , Ms. Lummis , Mr. Thune , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Defense Production Act of 1950 to require the Committee on Foreign Investment in the United States to review and prohibit certain transactions relating to agriculture.\n#### 1. Short title\nThis Act may be cited as the Promoting Agriculture Safeguards and Security Act or the PASS Act .\n#### 2. Review and prohibitions by Committee on Foreign Investment in the United States of certain transactions relating to agriculture\n##### (a) In general\nSection 721 of the Defense Production Act of 1950 ( 50 U.S.C. 4565 ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(14) Agriculture The term agriculture has the meaning given that term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ). ;\n**(2)**\nin subsection (b)(1), by adding at the end the following:\n(I) Consideration of certain agricultural land transactions (i) In general Not later than 30 days after receiving notification from the Secretary of Agriculture of a reportable agricultural land transaction, the Committee shall determine\u2014 (I) whether the transaction is a covered transaction; and (II) if the Committee determines that the transaction is a covered transaction, whether to\u2014 (aa) request the submission of a notice under clause (i) of subparagraph (C) or a declaration under clause (v) of such subparagraph pursuant to the process established under subparagraph (H); or (bb) initiate a review pursuant to subparagraph (D). (ii) Reportable agricultural land transaction defined In this subparagraph, the term reportable agricultural land transaction means a transaction\u2014 (I) that the Secretary of Agriculture has reason to believe is a covered transaction; (II) that involves the acquisition of an interest in agricultural land by a foreign person, other than an excepted investor or an excepted real estate investor, as such terms are defined in regulations prescribed by the Committee; and (III) with respect to which a person is required to submit a report to the Secretary of Agriculture under section 2(a) of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501(a) ). ;\n**(3)**\nin subsection (k)(2)\u2014\n**(A)**\nby redesignating subparagraphs (H), (I), and (J) as subparagraphs (I), (J), and (K), respectively; and\n**(B)**\nby inserting after subparagraph (G) the following:\n(H) The Secretary of Agriculture, with respect to any covered transaction related to the purchase of agricultural land or agricultural biotechnology or otherwise related to the agriculture industry in the United States. ; and\n**(4)**\nby adding at the end the following:\n(r) Prohibitions relating to purchases of agricultural land and agricultural businesses (1) In general If the Committee, in conducting a review under this section, determines that a transaction described in clause (i), (ii), or (iv) of subsection (a)(4)(B) would result in the purchase or lease by a covered foreign person of real estate described in paragraph (2) or would result in control by a covered foreign person of a United States business engaged in agriculture, the President shall prohibit the transaction unless a party to the transaction voluntarily chooses to abandon the transaction. (2) Real estate described Subject to regulations prescribed by the Committee, real estate described in this paragraph is agricultural land (as defined in section 9 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508 )) in the United States that is in close proximity (subject to subsection (a)(4)(C)(ii)) to a United States military installation or another facility or property of the United States Government that is\u2014 (A) sensitive for reasons relating to national security for purposes of subsection (a)(4)(B)(ii)(II)(bb); and (B) identified in regulations prescribed by the Committee. (3) Waiver The President may waive, on a case-by-case basis, the requirement to prohibit a transaction under paragraph (1) after the President determines and reports to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives that the waiver is in the national interest of the United States. (4) Covered foreign person defined (A) In general In this subsection, subject to regulations prescribed by the Committee, the term covered foreign person \u2014 (i) means any foreign person (including a foreign entity) that acts as an agent, representative, or employee of, or acts at the direction or control of, the government of a covered country; and (ii) does not include a United States citizen or an alien lawfully admitted for permanent residence to the United States. (B) Covered country defined For purposes of subparagraph (A), the term covered country means any of the following countries, if the country is determined to be a foreign adversary pursuant to section 791.4 of title 15, Code of Federal Regulations (or a successor regulation): (i) The People\u2019s Republic of China. (ii) The Russian Federation. (iii) The Islamic Republic of Iran. (iv) The Democratic People\u2019s Republic of Korea. .\n##### (b) Spending plans\nNot later than 60 days after the date of the enactment of this Act, each department or agency represented on the Committee on Foreign Investment in the United States shall submit to the chairperson of the Committee a copy of the most recent spending plan required under section 1721(b) of the Foreign Investment Risk Review Modernization Act of 2018 ( 50 U.S.C. 4565 note).\n##### (c) Regulations\n**(1) In general**\nThe President shall direct, subject to section 553 of title 5, United States Code, the issuance of regulations to carry out the amendments made by this section.\n**(2) Effective date**\nThe regulations prescribed under paragraph (1) shall take effect not later than one year after the date of the enactment of this Act.\n##### (d) Effective date; applicability\nThe amendments made by this section shall\u2014\n**(1)**\ntake effect on the date that is 30 days after the effective date of the regulations under subsection (c)(2); and\n**(2)**\napply with respect to a covered transaction (as defined in section 721 of the Defense Production Act of 1950 ( 50 U.S.C. 4565 )) that is proposed, pending, or completed on or after the date described in paragraph (1).",
      "versionDate": "2025-03-06",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-14T12:49:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119s903",
          "measure-number": "903",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s903v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Promoting Agriculture Safeguards and Security Act or the</strong> <strong>PASS Act</strong></p><p>This bill establishes requirements to address the national security risk to the U.S. agricultural sector.</p><p>Specifically, the bill prohibits foreign persons (i.e., individuals or entities)\u00a0who are acting on behalf of China, Russia, Iran, or North Korea from engaging in certain transactions that would result in the person (1) purchasing or leasing\u00a0U.S. agricultural land near a military installation or another facility or property that is sensitive for national security reasons, or (2) controlling a U.S. agricultural company.\u00a0The prohibition does not apply if a party to the transaction voluntarily chooses to abandon the transaction. The President may waive this prohibition, on a case-by-case basis, if the waiver is in the national interest. </p><p>The bill also places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS)\u00a0with respect to transactions (1) related to the purchase of agricultural land or agricultural biotechnology, or (2) otherwise related to the U.S. agricultural industry. The bill also requires\u00a0CFIUS to review certain transactions involving investments by foreign persons in U.S. agricultural land.</p><p>The\u00a0President must direct the issuance of regulations to implement these changes. The regulations must take effect not later than one year after\u00a0the bill's enactment.</p><p>Further,\u00a0the prohibitions and requirements in\u00a0this bill (1)\u00a0take effect 30 days after the effective date of the regulations; and (2)\u00a0apply to any covered transactions that are proposed, pending, or completed on or after the effective date.</p>"
        },
        "title": "PASS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s903.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Agriculture Safeguards and Security Act or the</strong> <strong>PASS Act</strong></p><p>This bill establishes requirements to address the national security risk to the U.S. agricultural sector.</p><p>Specifically, the bill prohibits foreign persons (i.e., individuals or entities)\u00a0who are acting on behalf of China, Russia, Iran, or North Korea from engaging in certain transactions that would result in the person (1) purchasing or leasing\u00a0U.S. agricultural land near a military installation or another facility or property that is sensitive for national security reasons, or (2) controlling a U.S. agricultural company.\u00a0The prohibition does not apply if a party to the transaction voluntarily chooses to abandon the transaction. The President may waive this prohibition, on a case-by-case basis, if the waiver is in the national interest. </p><p>The bill also places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS)\u00a0with respect to transactions (1) related to the purchase of agricultural land or agricultural biotechnology, or (2) otherwise related to the U.S. agricultural industry. The bill also requires\u00a0CFIUS to review certain transactions involving investments by foreign persons in U.S. agricultural land.</p><p>The\u00a0President must direct the issuance of regulations to implement these changes. The regulations must take effect not later than one year after\u00a0the bill's enactment.</p><p>Further,\u00a0the prohibitions and requirements in\u00a0this bill (1)\u00a0take effect 30 days after the effective date of the regulations; and (2)\u00a0apply to any covered transactions that are proposed, pending, or completed on or after the effective date.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s903"
    },
    "title": "PASS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Promoting Agriculture Safeguards and Security Act or the</strong> <strong>PASS Act</strong></p><p>This bill establishes requirements to address the national security risk to the U.S. agricultural sector.</p><p>Specifically, the bill prohibits foreign persons (i.e., individuals or entities)\u00a0who are acting on behalf of China, Russia, Iran, or North Korea from engaging in certain transactions that would result in the person (1) purchasing or leasing\u00a0U.S. agricultural land near a military installation or another facility or property that is sensitive for national security reasons, or (2) controlling a U.S. agricultural company.\u00a0The prohibition does not apply if a party to the transaction voluntarily chooses to abandon the transaction. The President may waive this prohibition, on a case-by-case basis, if the waiver is in the national interest. </p><p>The bill also places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS)\u00a0with respect to transactions (1) related to the purchase of agricultural land or agricultural biotechnology, or (2) otherwise related to the U.S. agricultural industry. The bill also requires\u00a0CFIUS to review certain transactions involving investments by foreign persons in U.S. agricultural land.</p><p>The\u00a0President must direct the issuance of regulations to implement these changes. The regulations must take effect not later than one year after\u00a0the bill's enactment.</p><p>Further,\u00a0the prohibitions and requirements in\u00a0this bill (1)\u00a0take effect 30 days after the effective date of the regulations; and (2)\u00a0apply to any covered transactions that are proposed, pending, or completed on or after the effective date.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s903"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s903is.xml"
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
      "title": "PASS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PASS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Agriculture Safeguards and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Defense Production Act of 1950 to require the Committee on Foreign Investment in the United States to review and prohibit certain transactions relating to agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:03:19Z"
    }
  ]
}
```
