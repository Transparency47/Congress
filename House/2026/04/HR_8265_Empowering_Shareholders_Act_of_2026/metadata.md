# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8265
- Title: Empowering Shareholders Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8265
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-21T16:05:44Z
- Update date including text: 2026-04-21T16:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8265",
    "number": "8265",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Empowering Shareholders Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T16:05:44Z",
    "updateDateIncludingText": "2026-04-21T16:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:04:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8265ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8265\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Huizenga introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Investment Advisers Act of 1940 to establish requirements for proxy voting of passively managed funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering Shareholders Act of 2026 .\n#### 2. Proxy voting of passively managed funds\n##### (a) In general\nThe Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20131 et seq. ) is amended by inserting after section 208 ( 15 U.S.C. 80b\u20138 ) the following:\n208A. Proxy voting of passively managed funds (a) Investment adviser proxy voting (1) In general An investment adviser that holds authority to vote a proxy solicited by an issuer pursuant to section 14 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78n ) in connection with any vote of covered securities held by a passively managed fund shall\u2014 (A) vote in accordance with the instructions (which may include the selection of a published voting policy) of the beneficial owner (or fiduciary or other designee with proxy voting authority on their behalf) of a voting security of the passively managed fund; (B) vote in accordance with the voting recommendations of the board of directors (or similar governing body) of such issuer; (C) abstain from voting such securities but make reasonable efforts to be considered present for purposed of establishing a quorum; or (D) pursuant to rules issued by the Commission, instruct vote tabulators to make a reasonable effort to mirror vote shares to reflect the elections of the other shareholders in the covered security. (2) Exception Paragraph (1) shall not apply with respect to a vote on a routine matter. (b) Safe harbor With respect to a routine or non-routine vote, voted in the manner required by subsection (a)(1), an investment adviser shall not be liable to any person under any law or regulation of the United States, any constitution, law, or regulation of any State or political subdivision thereof, or under any contract or other legally enforceable agreement (including any arbitration agreement), for any of the following: (1) Voting in accordance with the instructions of the beneficial owner (or that beneficial owner\u2019s designee with proxy voting authority) of a voting security of the passively managed fund. (2) Not soliciting voting instructions from any person. (3) Voting in accordance with the voting recommendations of an issuer under subsection (a)(1)(B) with respect to such vote. (4) Abstaining from voting in accordance with subsection (a)(1)(C) with respect to such vote. (5) Instructing vote tabulators to make a reasonable effort to mirror vote shares to reflect the elections of the other shareholders in a covered security, pursuant to rules issued by the Commission described in subsection (a)(1)(D). (c) Foreign private issuers exemption Subsection (a) shall not apply with respect to a foreign private issuer if the published voting policy of the investment advisor with respect to such foreign private issuer is fully and fairly disclosed to beneficial owners, including the extent to which such policy differs from the published voting policy for non-exempt issuers. (d) Dissemination of information (1) In general Any investment adviser subject to the requirements of subsection (a)(1) shall, with respect to the dissemination of information and other material to a voting person, comply with the following requirements, unless the voting person affirmatively declines to receive that information and other material: (A) Provide the voting person (or the relevant intermediary with whom the investment adviser has access) with a form to select a published voting policy. (B) Provide the voting person with not less than 5 business days after the date on which the voting person receives the form described under subparagraph (A) to return that form to the investment adviser. (2) Electronic delivery All, or any portion, of the materials that an investment adviser is required to provide under paragraph (1)(A) may be provided electronically, including through\u2014 (A) an internet website; (B) another digital, internet, or electronic-based information repository; or (C) a mobile application. (e) Definitions In this section: (1) Covered security The term covered security \u2014 (A) means a voting security, as that term is defined in section 2(a) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a) ), in which a qualified fund is invested; and (B) does not include any voting security (as defined in subparagraph (A)) of an issuer registered with the Commission as an investment company under section 8 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20138 ). (2) Passively managed fund The term passively managed fund means a qualified fund\u2014 (A) that\u2014 (i) is designed to track, or is derived from, an index of securities or a portion of such an index; (ii) discloses that the qualified fund is a passive index fund; or (iii) allocates not less than 60 percent of the total assets of the qualified fund to an investment strategy that is designed to track, or is derived from, an index of securities or a portion of such an index fund; and (B) that commits to refrain from exercising control over an issuer through voting or investment authority. (3) Published voting policy The term published voting policy means\u2014 (A) a policy that\u2014 (i) articulates how proportionate shares would be expected to be voted in anticipated proxy voting matters; and (ii) is made available to investors, including via website or other electronic means; and (B) in the case of a policy of a passively managed fund or an investment adviser, a policy that does not\u2014 (i) seek to set the strategy or day-to-day management decisions of the issuer; (ii) involve submitting shareholder proposals; (iii) seek to nominate directors; and (iv) coordinate votes with other index managers. (4) Qualified fund The term qualified fund means\u2014 (A) an investment company; (B) a private fund; (C) an eligible deferred compensation plan, as that term is defined in section 457(b) of the Internal Revenue Code of 1986; (D) a trust, plan, account, or other entity described in section 3(c)(11) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133(c)(11) ); (E) a plan maintained by an employer described in clause (i), (ii), or (iii) of section 403(b)(1)(A) of the Internal Revenue Code of 1986 to provide annuity contracts described in section 403(b) of such Code; (F) a common trust fund, or similar fund, maintained by a bank; (G) any fund established under section 8438(b)(1) of title 5, United States Code; or (H) any separate managed account of a client of an investment adviser. (5) Routine matter The term routine matter \u2014 (A) includes a proposal that relates to\u2014 (i) an election with respect to the board of directors of a registrant; (ii) the compensation of management or the board of directors of a registrant; (iii) the selection of auditors; or (iv) declassification; and (B) does not include\u2014 (i) a proposal that is not submitted to a holder of covered securities by means of a proxy statement comparable to that described in section 240.14a\u2013101 of title 17, Code of Federal Regulations, or any successor regulation; or (ii) a proposal that is\u2014 (I) the subject of a counter-solicitation; or (II) part of a proposal made by a person other than the applicable registrant. .\n##### (b) Effective date\nThe amendment made by this section shall take effect 1 year after the date of enactment of this Act.",
      "versionDate": "2026-04-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-15",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "8286",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Americans\u2019 Retirement Savings From Politics Act",
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
        "updateDate": "2026-04-21T16:05:14Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8265ih.xml"
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
      "title": "Empowering Shareholders Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering Shareholders Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Investment Advisers Act of 1940 to establish requirements for proxy voting of passively managed funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:45Z"
    }
  ]
}
```
