# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/840?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/840
- Title: Digital Integrity in Democracy Act
- Congress: 119
- Bill type: S
- Bill number: 840
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-02-02T17:33:37Z
- Update date including text: 2026-02-02T17:33:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/840",
    "number": "840",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Digital Integrity in Democracy Act",
    "type": "S",
    "updateDate": "2026-02-02T17:33:37Z",
    "updateDateIncludingText": "2026-02-02T17:33:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T20:55:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s840is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 840\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Welch (for himself, Ms. Hirono , Ms. Klobuchar , Mr. Merkley , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo hold accountable operators of social media platforms that intentionally or knowingly host false election administration information.\n#### 1. Short title\nThis Act may be cited as the Digital Integrity in Democracy Act .\n#### 2. Exception to section 230 immunity for social media platform operators hosting false election administration information\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) is amended\u2014\n**(1)**\nin subsection (c)(1)\u2014\n**(A)**\nby striking No provider and inserting the following:\n(A) In general Except as provided in subparagraph (B), no provider ; and\n**(B)**\nby adding at the end the following:\n(B) Exception Subparagraph (A) shall not apply with respect to false election administration information that the operator of a social media platform intentionally or knowingly hosts on the social media platform. ; and\n**(2)**\nin subsection (f), by adding at the end the following:\n(5) Covered election The term covered election has the meaning given the term election under section 301(1) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(1) ). (6) False election administration information (A) In general The term false election administration information , with respect to a social media platform, means objectively incorrect information that\u2014 (i) relates to\u2014 (I) the time, place, or manner of holding any covered election; or (II) the qualifications for or restrictions on voter eligibility for any covered election, including\u2014 (aa) any criminal, civil, or other legal penalties associated with voting in any covered election; or (bb) information regarding the registration status or eligibility of a voter; and (ii) is publicly accessible on the social media platform. (B) Political speech excluded The term false election administration information does not include any content that relates to political speech in favor of or against\u2014 (i) a candidate (as defined in section 301(2) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(2) )); (ii) an individual who holds a Federal office (as defined in section 301(3) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(3) )); or (iii) a political party. (7) Social media platform The term social media platform means a social media platform, as defined in section 124(a)(2) of the Trafficking Victims Prevention and Protection Reauthorization Act of 2022 ( 42 U.S.C. 1862w(a)(2) ), that had not fewer than 25,000,000 unique monthly users in the United States for a majority of the months during the most recent 12-month period, except that such section 124(a)(2) shall be applied by substituting an interactive computer service for a website or internet medium . .\n#### 3. False election administration information removal process\n##### (a) Definitions\nIn this section:\n**(1) Election day**\nThe term election day means, with respect to any covered election (as defined in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ), as amended by section 2)\u2014\n**(A)**\nthe date on which the covered election is held; and\n**(B)**\nany day during the period\u2014\n**(i)**\nbeginning on the earlier of\u2014\n**(I)**\nthe first day during which early voting for such election is allowed; or\n**(II)**\nthe first day on which the State distributes absentee ballots for such election; and\n**(ii)**\nending on the date of such election.\n**(2) False election administration information**\nThe term false election administration information has the meaning given the term in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ), as amended by section 2.\n**(3) Social media platform**\nThe term social media platform has the meaning given the term in section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ), as amended by section 2.\n**(4) Written**\nThe term written , with respect to a communication, includes a written electronic communication.\n##### (b) Removal process\n**(1) Removal required**\nIf an operator of a social media platform receives a complete notification, in accordance with paragraph (2), that false election administration information is being hosted on the social media platform, the operator shall\u2014\n**(A)**\ndetermine whether the alleged false election administration information is objectively incorrect;\n**(B)**\nif the determination under subparagraph (A) is that the alleged false election administration information is objectively incorrect, remove the false election administration information\u2014\n**(i)**\nnot later than 48 hours after receiving the complete notification, if received on a day other than an election day; or\n**(ii)**\nnot later than 24 hours after receiving the complete notification, if received on an election day; and\n**(C)**\nnot later than 12 hours after removing false election administration information, provide a written response to the complainant stating that the operator removed the false election administration information.\n**(2) Notification requirements**\nA notification described in paragraph (1) shall\u2014\n**(A)**\nbe a written notification submitted to the operator of the social media platform;\n**(B)**\ncontain a description of the false election administration information being hosted on the social media platform that is reasonably sufficient for the operator to locate the false election administration information; and\n**(C)**\ncontain the name and contact information of the complainant, including mailing address, telephone number, and email address.\n##### (c) Enforcement\n**(1) Attorney General civil action**\nThe Attorney General may bring a civil action in an appropriate district court of the United States against an operator of a social media platform that violates subsection (b)(1) for\u2014\n**(A)**\ndamages of $50,000 for each item of false election administration information that was not removed by the operator in accordance with that subsection; and\n**(B)**\ninjunctive relief relating to the removal of false election administration information that is the subject of the civil action.\n**(2) State civil action**\nThe attorney general or secretary of state of a State may bring a civil action in an appropriate district court of the United States against an operator of a social media platform that violates subsection (b)(1) with respect to a covered election being held in that State for\u2014\n**(A)**\ndamages of $50,000 for each item of false election administration information that was not removed by the operator in accordance with that subsection; and\n**(B)**\ninjunctive relief relating to the removal of false election administration information that is the subject of the civil action.\n**(3) Private right of action**\nA candidate, as defined in section 301 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 ), aggrieved by a violation of subsection (b)(1) may, after notifying the chief election official of the State involved, bring a civil action in an appropriate district court of the United States against the operator of a social media platform that committed the violation for\u2014\n**(A)**\ndamages of $50,000 for each item of false election administration information that was not removed by the operator in accordance with that subsection; and\n**(B)**\ninjunctive relief relating to the removal of false election administration information that is the subject of the civil action.\n##### (d) Safe harbor relating to section 230 immunity exception\nSubparagraph (B) of section 230(c)(1) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(1) ), as added by section 2, shall not apply with respect to false election administration information hosted on a social media platform if the operator of the social media platform\u2014\n**(1)**\nbecomes aware of the information due to a notification described in paragraph (2) of subsection (b) of this section and removes the information in accordance with paragraph (1) of that subsection; or\n**(2)**\nbecomes aware of the information through means other than a notification described in subsection (b)(2) of this section and removes the information\u2014\n**(A)**\nnot later than 48 hours after becoming aware of the information, if it becomes so aware on a day other than an election day; or\n**(B)**\nnot later than 24 hours after becoming aware of the information, if it becomes so aware on an election day.\n#### 4. Effective date\nThis Act, and the amendments made by this Act, shall apply with respect to any false election administration information alleged to be hosted on a social media platform on or after the date of enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-06T18:34:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119s840",
          "measure-number": "840",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2026-02-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s840v00",
            "update-date": "2026-02-02"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Digital Integrity in Democracy Act</strong></p><p>This bill requires large social media platforms to promptly remove from their sites false information about election logistics and voter eligibility.</p><p>Specifically, platforms notified of potential false election information must investigate the veracity of the flagged information and, if it is false, remove it. Covered information includes false information about the time and place of, or voter eligibility for, an election. Platforms must generally remove false information within 48 hours of receipt of notification of its existence. If notification is received on the day of an election, including during an early or absentee voting period, the information must be removed within 24 hours.\u00a0</p><p>The Department of Justice may bring a civil suit against a social media platform that violates the timely removal requirement. States may bring suit against a platform if the false information at issue related to an election in the state, and candidates may bring suit against a platform if the candidate was aggrieved by the false information. Such suits may seek money damages and injunctive relief.\u00a0</p><p>The bill also specifies that Section 230 protection does not apply to false election information that is knowingly hosted on a social media platform. (Section 230 generally precludes providers and users of an interactive computer service (e.g., a social media platform) from being held legally responsible under federal law for content provided by a third party.) However, platforms that comply with the timely removal requirements with respect to false election information retain Section 230 protection.\u00a0</p>"
        },
        "title": "Digital Integrity in Democracy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s840.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Digital Integrity in Democracy Act</strong></p><p>This bill requires large social media platforms to promptly remove from their sites false information about election logistics and voter eligibility.</p><p>Specifically, platforms notified of potential false election information must investigate the veracity of the flagged information and, if it is false, remove it. Covered information includes false information about the time and place of, or voter eligibility for, an election. Platforms must generally remove false information within 48 hours of receipt of notification of its existence. If notification is received on the day of an election, including during an early or absentee voting period, the information must be removed within 24 hours.\u00a0</p><p>The Department of Justice may bring a civil suit against a social media platform that violates the timely removal requirement. States may bring suit against a platform if the false information at issue related to an election in the state, and candidates may bring suit against a platform if the candidate was aggrieved by the false information. Such suits may seek money damages and injunctive relief.\u00a0</p><p>The bill also specifies that Section 230 protection does not apply to false election information that is knowingly hosted on a social media platform. (Section 230 generally precludes providers and users of an interactive computer service (e.g., a social media platform) from being held legally responsible under federal law for content provided by a third party.) However, platforms that comply with the timely removal requirements with respect to false election information retain Section 230 protection.\u00a0</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119s840"
    },
    "title": "Digital Integrity in Democracy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Digital Integrity in Democracy Act</strong></p><p>This bill requires large social media platforms to promptly remove from their sites false information about election logistics and voter eligibility.</p><p>Specifically, platforms notified of potential false election information must investigate the veracity of the flagged information and, if it is false, remove it. Covered information includes false information about the time and place of, or voter eligibility for, an election. Platforms must generally remove false information within 48 hours of receipt of notification of its existence. If notification is received on the day of an election, including during an early or absentee voting period, the information must be removed within 24 hours.\u00a0</p><p>The Department of Justice may bring a civil suit against a social media platform that violates the timely removal requirement. States may bring suit against a platform if the false information at issue related to an election in the state, and candidates may bring suit against a platform if the candidate was aggrieved by the false information. Such suits may seek money damages and injunctive relief.\u00a0</p><p>The bill also specifies that Section 230 protection does not apply to false election information that is knowingly hosted on a social media platform. (Section 230 generally precludes providers and users of an interactive computer service (e.g., a social media platform) from being held legally responsible under federal law for content provided by a third party.) However, platforms that comply with the timely removal requirements with respect to false election information retain Section 230 protection.\u00a0</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119s840"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s840is.xml"
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
      "title": "Digital Integrity in Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Digital Integrity in Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to hold accountable operators of social media platforms that intentionally or knowingly host false election administration information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:21Z"
    }
  ]
}
```
