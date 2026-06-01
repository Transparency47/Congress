# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1149
- Title: SEC Whistleblower Reform Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1149
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-01-30T22:18:26Z
- Update date including text: 2026-01-30T22:18:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1149",
    "number": "1149",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SEC Whistleblower Reform Act of 2025",
    "type": "S",
    "updateDate": "2026-01-30T22:18:26Z",
    "updateDateIncludingText": "2026-01-30T22:18:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T18:21:43Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "ME"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1149is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1149\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Grassley (for himself, Ms. Warren , Ms. Collins , Mr. Warnock , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Securities Exchange Act of 1934 to further enhance anti-retaliation protections for whistleblowers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SEC Whistleblower Reform Act of 2025 .\n#### 2. Whistleblower protections for internal disclosures\n##### (a) In general\nSection 21F of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136 ) is amended\u2014\n**(1)**\nin subsection (a)(6)\u2014\n**(A)**\nby striking The term and inserting the following:\n(A) In general The term ; and\n**(B)**\nby adding at the end the following:\n(B) Special rule Solely for the purposes of subsection (h)(1), the term whistleblower includes any individual who takes, or 2 or more individuals acting jointly who take, an action described in subsection (h)(1)(A), that the individual or 2 or more individuals reasonably believe relates to a violation of any law, rule, or regulation subject to the jurisdiction of the Commission, the Public Company Accounting Oversight Board, the Municipal Securities Rulemaking Board, or a self-regulatory organization. ; and\n**(2)**\nin subsection (h)(1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting or post-employment after of employment ;\n**(ii)**\nin clause (i), by inserting , in writing or orally if the oral report is documented, after to the Commission ;\n**(iii)**\nin clause (ii), by striking or at the end;\n**(iv)**\nin clause (iii), by striking the period at the end and inserting ; or ; and\n**(v)**\nby adding at the end the following:\n(iv) in providing information regarding any conduct that the whistleblower reasonably believes constitutes a violation of any law, rule, or regulation subject to the jurisdiction of the Commission to\u2014 (I) a person with supervisory authority over the whistleblower at the employer of the whistleblower, if that employer is an entity registered with, or required to be registered with, or otherwise subject to the jurisdiction of, the Commission, the Public Company Accounting Oversight Board, a self-regulatory organization, or a State securities commission or office performing like functions; or (II) another individual working for the employer described in subclause (I) who the whistleblower reasonably believes has the authority to\u2014 (aa) investigate, discover, or terminate the misconduct; or (bb) take any other action to address the misconduct. ; and\n**(B)**\nin subparagraph (B), by adding at the end the following:\n(iv) Jury trial A person against which an action is brought under this subsection shall be entitled to a jury trial. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply to any claim involving a violation of section 21F(h)(1) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136(h)(1) ), including a claim in an enforcement action or proceeding brought by the Securities and Exchange Commission, that is\u2014\n**(1)**\npending in any appropriate judicial or administrative forum, as of the date of enactment of this Act; or\n**(2)**\nfiled after the date of enactment of this Act.\n#### 3. Prompt payment of awards\nSection 21F(b) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136(b) ) is amended by adding at the end the following:\n(3) Timely processing of claims (A) Initial disposition (i) In general Except as provided in subparagraph (B), the Commission shall make an initial disposition with respect to a claim submitted by a whistleblower for an award under this section (referred to in this paragraph as an award claim ) not later than the later of\u2014 (I) the date that is 1 year after the deadline established by the Commission, by rule, for the whistleblower to file the award claim; or (II) the date that is 1 year after the final resolution of all litigation, including any appeals, concerning the covered action or related action. (ii) Multiple actions If an award claim involves 1 or more related actions, the requirement under clause (i) shall apply with respect to the latest deadline with respect to the actions. (B) Exceptions (i) Initial extension If the Director of the Division of Enforcement of the Commission (referred to in this paragraph as the Director ), or the designee of the Director, determines that an award claim is sufficiently complex or involves more than 1 whistleblower, or if other good cause exists such that the Commission cannot reasonably satisfy the requirements under subparagraph (A), as determined by the Director or the designee, as applicable, the Director or the designee, after providing notice to the Chairman of the Commission (referred to in this paragraph as the Chairman ), may extend the deadline with respect to the satisfaction of those requirements by not more than 180 days. (ii) Additional extensions If, after providing an extension under clause (i), the Director, or the designee of the Director, determines that good cause exists such that the Commission cannot reasonably satisfy the requirement under subparagraph (A), the Director or the designee of the Director, may extend the deadline described in clause (i) as needed for 1 or more additional successive 180-day periods only after providing notice to and receiving approval from the Commission. (iii) Notice to whistleblower required If the Director, or the designee of the Director, exercises authority under clause (i) or (ii), the Director or the designee, as applicable, shall submit to the whistleblower who filed the award claim that is subject to that action by the Director or the designee a written notification of that action. (C) Applicability This paragraph shall apply only to an award claim that the Director of the designee of the Director determines is timely submitted under a deadline established by the Commission after the date of enactment of this paragraph. .\n#### 4. Nonenforceability of certain provisions\n##### (a) In general\nSection 21F of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136 ) is amended by adding at the end the following:\n(k) Nonenforceability of certain provisions waiving rights and remedies or requiring arbitration (1) Waiver of rights and remedies The rights and remedies provided in this section may not be waived by any agreement, policy form, or condition of employment, including by a predispute arbitration agreement. (2) Predispute arbitration agreement No predispute arbitration agreement shall be valid or enforceable if the agreement requires the arbitration of a dispute arising under this section. .\n##### (b) Applicability\nSubsection (k) of section 21F of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136 ), as added by subsection (a), shall apply with respect to any action that is filed on or after, or that is pending as of, the date of enactment of this Act.\n#### 5. Rulemaking authority\nThe Securities and Exchange Commission may issue any rules that are necessary or appropriate to carry out this Act consistent with the purposes of section 21F of the Securities Exchange Act of 1934 ( 15 U.S.C. 78u\u20136 ), as amended by this Act.",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-04-10T12:38:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119s1149",
          "measure-number": "1149",
          "measure-type": "s",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1149v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>SEC Whistleblower Reform Act of 2025</strong></p><p>This bill expands and revises whistleblower protections applicable to individuals who provide information to the Securities and Exchange Commission (SEC) relating to a violation of securities laws.</p><p>Under current law, an employer is prohibited from retaliating against these whistleblowers. Under the bill, this prohibition is expanded to include (1) individuals who provide information regarding potential violations to supervisors or other employees in positions of authority; and (2) information relating to violations subject to the jurisdiction of the Public Company Accounting Oversight Board, the Municipal Securities Rulemaking Board, or a self-regulatory organization.</p><p>Additionally, the bill establishes the right to a jury trial for a person accused of violating whistleblower protection laws.</p><p>The bill also requires the SEC to make an initial disposition of a whistleblower award claim within the later of (1) one year of the deadline to submit such a claim, or (2) one year after the final resolution of any litigation in the matter.</p><p>Finally, the bill deems as unenforceable a predispute arbitration agreement regarding a whistleblower action.</p>"
        },
        "title": "SEC Whistleblower Reform Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1149.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>SEC Whistleblower Reform Act of 2025</strong></p><p>This bill expands and revises whistleblower protections applicable to individuals who provide information to the Securities and Exchange Commission (SEC) relating to a violation of securities laws.</p><p>Under current law, an employer is prohibited from retaliating against these whistleblowers. Under the bill, this prohibition is expanded to include (1) individuals who provide information regarding potential violations to supervisors or other employees in positions of authority; and (2) information relating to violations subject to the jurisdiction of the Public Company Accounting Oversight Board, the Municipal Securities Rulemaking Board, or a self-regulatory organization.</p><p>Additionally, the bill establishes the right to a jury trial for a person accused of violating whistleblower protection laws.</p><p>The bill also requires the SEC to make an initial disposition of a whistleblower award claim within the later of (1) one year of the deadline to submit such a claim, or (2) one year after the final resolution of any litigation in the matter.</p><p>Finally, the bill deems as unenforceable a predispute arbitration agreement regarding a whistleblower action.</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1149"
    },
    "title": "SEC Whistleblower Reform Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>SEC Whistleblower Reform Act of 2025</strong></p><p>This bill expands and revises whistleblower protections applicable to individuals who provide information to the Securities and Exchange Commission (SEC) relating to a violation of securities laws.</p><p>Under current law, an employer is prohibited from retaliating against these whistleblowers. Under the bill, this prohibition is expanded to include (1) individuals who provide information regarding potential violations to supervisors or other employees in positions of authority; and (2) information relating to violations subject to the jurisdiction of the Public Company Accounting Oversight Board, the Municipal Securities Rulemaking Board, or a self-regulatory organization.</p><p>Additionally, the bill establishes the right to a jury trial for a person accused of violating whistleblower protection laws.</p><p>The bill also requires the SEC to make an initial disposition of a whistleblower award claim within the later of (1) one year of the deadline to submit such a claim, or (2) one year after the final resolution of any litigation in the matter.</p><p>Finally, the bill deems as unenforceable a predispute arbitration agreement regarding a whistleblower action.</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1149"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1149is.xml"
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
      "title": "SEC Whistleblower Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEC Whistleblower Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Securities Exchange Act of 1934 to further enhance anti-retaliation protections for whistleblowers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T02:33:35Z"
    }
  ]
}
```
