# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3793
- Title: Predatory Lending Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 3793
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-02-26T16:42:03Z
- Update date including text: 2026-02-26T16:42:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S511-512)
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S511-512)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3793",
    "number": "3793",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Predatory Lending Elimination Act",
    "type": "S",
    "updateDate": "2026-02-26T16:42:03Z",
    "updateDateIncludingText": "2026-02-26T16:42:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S511-512)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T19:08:33Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "HI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "RI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3793is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3793\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Reed (for himself, Mr. Blumenthal , Ms. Duckworth , Mr. Fetterman , Mr. Heinrich , Mr. Luj\u00e1n , Mr. Merkley , Mr. Padilla , Mr. Schatz , Ms. Smith , Mr. Van Hollen , Mr. Whitehouse , Mr. Warnock , Mr. Welch , Mr. Wyden , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Truth in Lending Act to extend the consumer credit protections provided to members of the Armed Forces and their dependents under title 10, United States Code, to all consumers.\n#### 1. Short title\nThis Act may be cited as the Predatory Lending Elimination Act .\n#### 2. Limitations on consumer credit and maximum rates of interest\n##### (a) In general\nChapter 2 of the Truth in Lending Act ( 15 U.S.C. 1631 et seq. ) is amended by adding at the end the following:\n140B. Limitations on consumer credit and maximum rates of interest (a) Application of the Military Lending Act (1) In general Except as provided in paragraph (2), section 987(b) of title 10, United States Code, shall apply to a creditor who extends consumer credit to a consumer to the same extent as that section applies to a creditor who extends consumer credit to a covered member or a dependent, as those terms are defined in such section 987. (2) Exceptions Paragraph (1) shall not apply to\u2014 (A) a residential mortgage; (B) a loan procured in the course of purchasing a car if the loan is offered\u2014 (i) for the express purpose of financing the purchase; and (ii) is secured by the car; or (C) a loan made by a Federal credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ), subject to the rate of interest limit provided under section 107(5)(A)(vi) of that Act, as implemented by the National Credit Union Administration Board. (b) No exemptions permitted The exemption authority of the Bureau under section 105(f) shall not apply with respect to this section. (c) Calculation of the annual percentage rate for open-End credit (1) In general For purposes of this section, the annual percentage rate applicable to an open-end credit plan shall be calculated under section 107(a)(2), subject to adjustments to the amount considered a finance charge, as provided in the rules issued by the Secretary of Defense on July 22, 2015, to carry out section 987 of title 10, United States Code. (2) Exception to finance charge calculation (A) In general Notwithstanding paragraph (1), for consumer credit extended in a credit card account under an open-end (not home-secured) consumer credit plan, a bona fide fee other than a periodic rate is not a charge required to be included in the finance charge for purposes of this section if the fee is assessed in compliance with section 127(n). (B) Limitation Subparagraph (A) shall not apply to\u2014 (i) any credit insurance premium or fee, including any charge for single premium credit insurance, any fee for a debt cancellation contract, or any fee for a debt suspension agreement; or (ii) any fee for a credit-related ancillary product sold in connection with the credit card account under an open-end (not home-secured) consumer credit plan. (d) Relation to State law Nothing in this section may be construed to preempt any provision of State law that provides greater protection to consumers than is provided under this section. (e) Penalties and remedies Section 987(f) of title 10, United States Code, shall apply to a creditor who extends consumer credit to a consumer in violation of this section to the same extent as such section 987(f) applies to a creditor who extends consumer credit to a covered member or a dependent, as those terms are defined in such section 987. (f) Preservation of State enforcement (1) State attorneys general Not later than 3 years after the date on which a violation of this section occurs, the attorney general of a State (or an equivalent official) may bring a civil action in the name of that State\u2014 (A) in any district court of the United States that is located in that State or in a State court that is located in that State and that has jurisdiction over the defendant; and (B) to\u2014 (i) enforce provisions of this section or rules issued under this section; and (ii) secure remedies under provisions of this section or remedies otherwise provided under other law. (2) State regulators Not later than 3 years after the date on which a violation of this section occurs, a State regulator may bring a civil action or initiate another appropriate proceeding to\u2014 (A) enforce the provisions of this section or regulations issued under this section with respect to any entity that is, or is required to be, State-chartered, incorporated, licensed, or otherwise authorized to do business under State law; and (B) secure remedies under provisions of this section or remedies otherwise provided under other provisions of law with respect to an entity described in subparagraph (A). (3) Notice requirement; additional regulations Subsections (b), (c), and (d) of section 1042 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5552 ), shall apply to a civil action or other appropriate proceeding brought or initiated under paragraph (1) or (2) to the same extent as those subsections apply to actions and other administrative and regulatory proceedings described in subsection (a) of that section. (g) Regulations (1) In general Notwithstanding section 1027(o) of the Consumer Financial Protection Act ( 12 U.S.C. 5517(o) ), not later than 1 year after the date of enactment of this section, the Bureau, in consultation with the Secretary of Defense, shall\u2014 (A) issue rules carrying out this section; and (B) notify Congress and the public, including on the website of the Bureau, regarding the issuance of the rules required under subparagraph (A). (2) Consistency The rules issued by the Bureau under paragraph (1)\u2014 (A) shall be consistent with rules issued by the Secretary of Defense to carry out section 987 of title 10, United States Code; and (B) may not provide lesser protection to consumers than the protection afforded covered members, as defined in section 987 of title 10, United States Code, in applicable provisions in the rules issued by the Secretary of Defense on July 22, 2015, to carry out that section. .\n##### (b) Technical and conforming amendment\nThe table of contents for chapter 2 of the Truth in Lending Act is amended by adding at the end the following:\n140B. Limitations on consumer credit and maximum rates of interest. .\n##### (c) Applicability\nThe amendments made by subsection (a) shall apply to an extension of credit made after the earlier of\u2014\n**(1)**\nthe date on which the rules issued by the Bureau of Consumer Financial Protection under subsection (g) of section 140B of the Truth in Lending Act, as added by subsection (a) of this section, require compliance; and\n**(2)**\nthe date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2026-02-05",
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
        "updateDate": "2026-02-26T16:42:03Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3793is.xml"
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
      "title": "Predatory Lending Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Predatory Lending Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Truth in Lending Act to extend the consumer credit protections provided to members of the Armed Forces and their dependents under title 10, United States Code, to all consumers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:22Z"
    }
  ]
}
```
