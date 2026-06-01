# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1670
- Title: INDEX Act
- Congress: 119
- Bill type: S
- Bill number: 1670
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-04-30T18:36:00Z
- Update date including text: 2026-04-30T18:36:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1670",
    "number": "1670",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "INDEX Act",
    "type": "S",
    "updateDate": "2026-04-30T18:36:00Z",
    "updateDateIncludingText": "2026-04-30T18:36:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T15:30:22Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "LA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "LA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1670is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1670\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Sullivan (for himself, Mr. Daines , Mr. Cornyn , Mr. Cassidy , Mr. Tillis , Mr. Scott of Florida , Mr. Kennedy , Mr. Hagerty , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Investment Advisers Act of 1940 to require investment advisers for passively managed funds to arrange for pass-through voting of proxies for certain securities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the INvestor Democracy is EXpected Act or the INDEX Act .\n#### 2. Proxy voting of passively managed funds\n##### (a) In general\nThe Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20131 et seq. ) is amended by inserting after section 208 ( 15 U.S.C. 80b\u20138 ) the following:\n208A. Requirement with respect to proxy voting of passively managed funds (a) Definitions In this section\u2014 (1) the term covered security \u2014 (A) means a voting security, as that term is defined in section 2(a) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a) ), in which a qualified fund is invested; and (B) does not include any voting security (as defined in subparagraph (A)) of an issuer registered with the Commission as an investment company under section 8 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20138 ); (2) the term passively managed fund means a qualified fund that\u2014 (A) is designed to track, or is derived from, an index of securities or a portion of such an index; (B) discloses that the qualified fund is a passive fund or an index fund; (C) allocates not less than 40 percent of the total assets of the qualified fund to an investment strategy that is designed to track, or is derived from, an index of securities or a portion of such an index; or (D) discloses that an allocation described in subparagraph (C) follows an investment strategy that is passive or based on an index of securities; (3) the term qualified fund means\u2014 (A) an investment company, as that term is defined in section 3 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133 ); (B) a private fund; (C) an eligible deferred compensation plan, as that term is defined in section 457(b) of the Internal Revenue Code of 1986; (D) an entity described in section 3(c)(11) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(11) ); (E) a plan maintained by an employer described in clause (i), (ii), or (iii) of section 403(b)(1)(A) of the Internal Revenue Code of 1986 to provide annuity contracts described in section 403(b) of such Code; (F) a common trust fund, or similar fund, maintained by a bank; (G) any fund established under section 8438(b)(1) of title 5, United States Code; or (H) any separate managed account of a client of an investment adviser; (4) the term registrant means an issuer of covered securities; (5) the term routine matter does not include\u2014 (A) a proposal that is not submitted to a holder of covered securities by means of a proxy statement comparable to that described in section 240.14a\u2013101 of title 17, Code of Federal Regulations, or any successor regulation; (B) a proposal that is\u2014 (i) the subject of a counter-solicitation; or (ii) part of a proposal made by a person other than the applicable registrant; (C) a proposal that relates to a merger or consolidation, except when, with respect to a registrant\u2014 (i) the proposal is to merge with a wholly owned subsidiary of the registrant; and (ii) holders of covered securities issued by the registrant that dissent to the proposal do not have rights of appraisal; (D) a proposal that relates to the sale, lease, or exchange of all, or substantially all, of the property and assets of a registrant; (E) an election for directors (or comparable positions); or (F) any other matter determined by the Commission or an exchange registered under section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ) to be not routine; and (6) the term voting person means a person that provides voting instructions under subsection (b) or (c). (b) Requirement (1) In general Subject to subsection (g), if an investment adviser holds authority to vote a proxy solicited pursuant to section 14 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78n ) in connection with any vote of covered securities held by a passively managed fund, and the voting authority held by that investment adviser with respect to those covered securities (when combined with the voting authority of other persons controlled by, or under common control with, that investment adviser) is more than 1 percent of the voting authority of the outstanding securities of the registrant subject to the vote, the investment adviser shall vote proportionate amounts of those covered securities in accordance with the voting instructions of\u2014 (A) in the case of a passively managed fund that issues securities, persons holding securities in the passively managed fund, such that, solely for the purposes of that vote, the percentage of securities held by such a person shall be deemed to be the percentage of the covered securities beneficially owned by that person; and (B) in all cases other than a case described in subparagraph (A), persons holding economic interests in the passively managed fund, such that, solely for purposes of that vote, the percentage of economic interests held by such a person shall be deemed to be the percentage of the covered securities beneficially owned by that person. (2) Prohibition If paragraph (1) applies with respect to any vote of covered securities and the investment adviser to which that paragraph applies does not receiving voting instructions from all persons described in subparagraphs (A) and (B) of that paragraph, the investment adviser may not vote the proportion of the shares of the covered securities for which the investment adviser does not receive voting instructions. (c) Passively managed fund as security holder of another passively managed fund If a passively managed fund (referred to in this subsection as the holding fund ) holds securities of another passively managed fund (referred to in this subsection as the held fund ), and there is a vote with respect to covered securities held by the held fund, the investment adviser of the holding fund shall obtain voting instructions from persons holding securities in the holding fund, or to persons holding economic interests in the holding fund, as applicable, with respect to that vote in the manner described in subsection (b). (d) Prohibitions (1) Reimbursement No person may seek reimbursement from a registrant, or require any expenses incurred to be paid by a registrant, with respect to the obligations imposed under this section. (2) Partial compliance An investment adviser may not solicit voting instructions from some, but not all, voting persons under subsection (b)(1) or (c), as applicable. (e) Exceptions (1) Voting on routine matters Notwithstanding subsections (b)(1), (b)(2), and (d)(2), if an investment adviser chooses not to solicit voting instructions with respect to a vote described in subsection (b)(1) or (c), or, as of the date that is 10 days before such a vote, the investment adviser has not received voting instructions from a person described in subparagraph (A) or (B) of subsection (b)(1) or subsection (c), as applicable, the investment adviser may vote the covered securities for which the investment adviser has not received voting instructions with respect to a routine matter. (2) Mirror voting exception for matters requiring approval of a majority of outstanding securities Notwithstanding subsections (b)(1), (b)(2), and (d)(2), if a matter to be considered at a meeting of a registrant requires the approval of a majority of the outstanding securities of the registrant entitled to vote on the matter, an investment adviser to which any such provision applies may, with respect to any covered securities for which voting instructions have not been received, as of the date that is 10 days before that vote, vote the uninstructed covered securities in a manner that is proportionate to the votes submitted on the matter by all other security holders of the registrant. (f) Dissemination of information (1) In general Any investment adviser subject to the requirements of subsection (b) or (c) shall, with respect to the dissemination of information and other materials to a voting person, comply with the following requirements, unless the voting person affirmatively declines to receive that information and other materials: (A) Provide to the voting person\u2014 (i) a proxy statement, other proxy soliciting material, or an information statement; (ii) an annual report from the applicable registrant; (iii) a form of voting instruction to return to the investment adviser; and (iv) any control or identification number that the voting person needs to return to the investment adviser the voting instruction provided under subparagraph (B). (B) Provide the voting person with not less than 5 business days after the date on which the voting person receives the materials provided under paragraph (1) to return those materials to the investment adviser. (2) Electronic delivery All, or any portion, of the materials that an investment adviser is required to provide under paragraph (1)(A) may be provided electronically, including an internet website address provided by the applicable registrant or a third party. (3) Option for investment advisers An investment adviser may provide recommendations to voting persons with the material provided under paragraph (1)(A), or after providing the material under that paragraph, if the investment adviser permits voting recommendations to be provided to voting persons by third parties on a nondiscriminatory basis and on a wide range of views. (4) Satisfaction of requirements by passively managed fund With respect to any requirement applicable to an investment adviser under this subsection, the requirement may be satisfied by the applicable passively managed fund, which may cover any expenses, direct or indirect, incurred in carrying out that requirement. (g) Safe harbor and rule of construction regarding duties An investment adviser\u2014 (1) with respect to a matter that is not a routine matter, may choose not to solicit voting instructions from any person under subsection (b)(1) or (c), subject to subsections (d)(2) and (e); and (2) if the investment adviser chooses not to solicit voting instructions under subparagraph (A), shall not be considered to be in violation of any duty under any Federal or State law for failing to vote the applicable securities. .\n##### (b) Effective date\nSection 208A of the Investment Advisers Act of 1940, as added by subsection (a), shall take effect on the first August 1 that occurs after the date that is 2 years after the date of enactment of this Act.\n#### 3. Voting instructions from customers\nSection 14(b)(1) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78n(b)(1) ) is amended by inserting voting instruction, after consent, .",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-06-04T17:03:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119s1670",
          "measure-number": "1670",
          "measure-type": "s",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2026-04-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1670v00",
            "update-date": "2026-04-30"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>INvestor Democracy is EXpected Act or the INDEX Act </strong></p><p>This bill establishes guidelines for passively managed funds (e.g., index funds) that vote shares on behalf of fund investors in proxy shareholder votes. Under the bill, these funds generally must vote shares on a proportional basis according to instructions from fund investors.</p><p>The bill establishes an exemption for routine matters and matters requiring approval of a majority of outstanding securities. Additionally, the bill establishes a safe harbor from these requirements for investment advisers. \u00a0</p>"
        },
        "title": "INDEX Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1670.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>INvestor Democracy is EXpected Act or the INDEX Act </strong></p><p>This bill establishes guidelines for passively managed funds (e.g., index funds) that vote shares on behalf of fund investors in proxy shareholder votes. Under the bill, these funds generally must vote shares on a proportional basis according to instructions from fund investors.</p><p>The bill establishes an exemption for routine matters and matters requiring approval of a majority of outstanding securities. Additionally, the bill establishes a safe harbor from these requirements for investment advisers. \u00a0</p>",
      "updateDate": "2026-04-30",
      "versionCode": "id119s1670"
    },
    "title": "INDEX Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>INvestor Democracy is EXpected Act or the INDEX Act </strong></p><p>This bill establishes guidelines for passively managed funds (e.g., index funds) that vote shares on behalf of fund investors in proxy shareholder votes. Under the bill, these funds generally must vote shares on a proportional basis according to instructions from fund investors.</p><p>The bill establishes an exemption for routine matters and matters requiring approval of a majority of outstanding securities. Additionally, the bill establishes a safe harbor from these requirements for investment advisers. \u00a0</p>",
      "updateDate": "2026-04-30",
      "versionCode": "id119s1670"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1670is.xml"
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
      "title": "INDEX Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INDEX Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INvestor Democracy is EXpected Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Investment Advisers Act of 1940 to require investment advisers for passively managed funds to arrange for pass-through voting of proxies for certain securities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:15Z"
    }
  ]
}
```
