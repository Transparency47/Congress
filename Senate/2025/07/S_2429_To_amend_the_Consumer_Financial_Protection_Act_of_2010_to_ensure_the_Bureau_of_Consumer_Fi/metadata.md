# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2429
- Title: Stop the Scammers Act
- Congress: 119
- Bill type: S
- Bill number: 2429
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-12-04T12:03:25Z
- Update date including text: 2025-12-04T12:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2429",
    "number": "2429",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Stop the Scammers Act",
    "type": "S",
    "updateDate": "2025-12-04T12:03:25Z",
    "updateDateIncludingText": "2025-12-04T12:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T15:17:57Z",
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
      "sponsorshipDate": "2025-07-24",
      "state": "MA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NY"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "RI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MD"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "PA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NJ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NV"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CO"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "GA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "VA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "DE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2429is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2429\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Ms. Cortez Masto (for herself, Ms. Warren , Mr. Schumer , Mr. Reed , Ms. Smith , Mr. Van Hollen , Mr. Kim , Mr. Gallego , Ms. Alsobrooks , Mr. Durbin , Mr. Blumenthal , Ms. Klobuchar , Mr. Merkley , Mr. Whitehouse , Mr. Sanders , Mrs. Gillibrand , Mr. Fetterman , Mr. Booker , Ms. Rosen , Mr. Welch , Mr. Luj\u00e1n , Mr. Hickenlooper , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Consumer Financial Protection Act of 2010 to ensure the Bureau of Consumer Financial Protection retains adequate resources to ensure fair, transparent, and competitive markets for financial products and services for consumers and to provide for whistleblower incentives and protection.\n#### 1. Short title\nThis Act may be cited as the Stop the Scammers Act .\n#### 2. Bureau whistleblower incentives and protection\n##### (a) In general\nThe Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 et seq. ) is amended by inserting after section 1017 the following:\n1017A. Whistleblower incentives and protection (a) Definitions In this section: (1) Administrative proceeding or court action The term administrative proceeding or court action means any judicial or administrative action brought by the Bureau that results in monetary sanctions exceeding $1,000,000. (2) Fund The term Fund means the Consumer Financial Civil Penalty Fund established under section 1017(d)(1). (3) Monetary sanctions The term monetary sanctions means, with respect to any administrative proceeding or court action, any monies, including penalties, disgorgement, restitution, interest, ordered to be paid or other amounts of relief obtained under section 1055(a)(2). (4) Original information The term original information means information that\u2014 (A) is derived from the independent knowledge or analysis of a whistleblower; (B) is not known to the Bureau from any other source, unless the whistleblower is the original source of the information; (C) is not exclusively derived from an allegation made in a judicial or administrative hearing, in a governmental report, hearing, or from the news media, unless the whistleblower is a source of the information; and (D) is not exclusively derived from an allegation made in an audit, examination, or investigation. (5) Successful enforcement The term successful enforcement includes, with respect to any administrative proceeding or court action brought by the Bureau, any settlement of such proceeding or action. (6) Whistleblower The term whistleblower means any individual who provides, or 2 or more individuals acting jointly who provide, original information relating to a violation of Federal consumer financial law, consistent with any rule or regulation issued by the Bureau under this section. (b) Awards (1) In general In any administrative proceeding or court action the Bureau, subject to regulations prescribed by the Bureau and subject to subsection (c), shall pay an award or awards to 1 or more whistleblowers who voluntarily provided original information that led to the successful enforcement of the covered administrative proceeding or court action in an aggregate amount equal to\u2014 (A) not less than 10 percent, in total, of the civil money penalties collected by the Bureau in the action; and (B) not more than 30 percent, in total, of the civil money penalties collected by the Bureau in the action. (2) Payment of awards Any amount paid under paragraph (1) shall be paid from the Fund. (3) Award minimum If the Bureau collects less than $1,000,000 in civil money penalties in the action, the Bureau shall provide for an award to any single whistleblower equal to the greater of\u2014 (A) 10 percent of the civil money penalties collected; or (B) $50,000. (c) Determination of amount of award; denial of award (1) Determination of amount of award (A) Discretion The determination of the percentage amount of an award made under subsection (b) shall be in the discretion of the Bureau. (B) Criteria In determining the percentage amount of an award made under subsection (b), the Bureau shall take into consideration\u2014 (i) the significance of the information provided by the whistleblower to the successful enforcement of the administrative proceeding or court action; (ii) the degree of assistance provided by the whistleblower and any legal representative of the whistleblower in an administrative proceeding or court action; (iii) the programmatic interest of the Bureau in deterring violations of Federal consumer financial law (including applicable regulations) by making awards to whistleblowers who provide information that leads to the successful enforcement of such laws; and (iv) such additional relevant factors as the Bureau may establish by rule or regulation, including the amount available in the Fund. (2) Denial of award No award under subsection (b) shall be made\u2014 (A) to any whistleblower who is, or was at the time the whistleblower acquired the original information submitted to the Bureau, a member, officer, or employee of an entity described in subclauses (I) through (V) of subsection (h)(1)(C)(i); (B) to any whistleblower who is convicted of a criminal violation related to the administrative proceeding or court action for which the whistleblower otherwise could receive an award under this section; (C) to any whistleblower who is found to be liable for the conduct in the administrative proceeding or court action, or a related action, for which the whistleblower otherwise could receive an award under this section; (D) to any whistleblower who planned and initiated the conduct at issue in the administrative proceeding or court action for which the whistleblower otherwise could receive an award under this section; (E) to any whistleblower who submits information to the Bureau that is based on the facts underlying the administrative proceeding or court action previously submitted by another whistleblower; and (F) to any whistleblower who fails to submit information to the Bureau in such form as the Bureau may, by rule or regulation, require. (d) Representation (1) Permitted representation Any whistleblower who makes a claim for an award under subsection (b) may be represented by counsel. (2) Required representation (A) In general Any whistleblower who anonymously makes a claim for an award under subsection (b) shall be represented by counsel if the whistleblower submits the information upon which the claim is based. (B) Disclosure of identity Prior to the payment of an award, a whistleblower shall disclose the identity of the whistleblower and provide such other information as the Bureau may require, directly or through counsel of the whistleblower. (e) No contract necessary No contract or other agreement with the Bureau is necessary for any whistleblower to receive an award under subsection (b), unless otherwise required by the Bureau by rule or regulation. (f) Appeals (1) In general Any determination made under this section, including whether, to whom, or in what amount to make awards, shall be in the discretion of the Bureau. Any such determination, except the determination of the amount of an award if the award was made in accordance with subsection (b), may be appealed to the appropriate court of appeals of the United States not more than 30 days after the determination is issued by the Bureau. (2) Scope of review The court shall review the determination made by the Bureau in accordance with section 706 of title 5, United States Code. (g) Reports to Congress Not later than December 31 of each year, the Bureau shall transmit to the House Committee on Financial Services and the Senate Committee on Banking, Housing, and Urban Affairs a report on the Bureau\u2019s whistleblower award program under this section, including a description of the number of awards granted and the types of cases in which awards were granted during the preceding fiscal year. (h) Protection of whistleblowers (1) Confidentiality (A) In general Except as provided in subparagraphs (B) and (C), the Bureau and any officer or employee of the Bureau, shall not disclose any information, including information provided by a whistleblower to the Bureau, which could reasonably be expected to reveal the identity of a whistleblower, except in accordance with the provisions of section 552a of title 5, United States Code, unless and until required to be disclosed to a defendant or respondent in connection with a public proceeding instituted by the Bureau or any entity described in subparagraph (C). For purposes of section 552 of title 5, United States Code, this paragraph shall be considered a statute described in subsection (b)(3)(B) of such section 552. (B) Effect Nothing in this paragraph is intended to limit the ability of the Attorney General to present such evidence to a grand jury or to share such evidence with potential witnesses or defendants in the course of an ongoing criminal investigation. (C) Availability to government agencies (i) In general Without the loss of its status as confidential in the hands of the Bureau, all information referred to in subparagraph (A) may, in the discretion of the Bureau, when determined by the Bureau to be necessary or appropriate, be made available to\u2014 (I) the Department of Justice; (II) an appropriate department or agency of the Federal Government, acting within the scope of its jurisdiction; (III) a State attorney general in connection with any criminal investigation; (IV) an appropriate department or agency of any State, acting within the scope of its jurisdiction; and (V) a foreign regulatory authority. (ii) Maintenance of information Each of the entities, agencies, or persons described in clause (i) shall maintain information described in that clause as confidential, in accordance with the requirements in subparagraph (A). (2) Rights retained Nothing in this section shall be deemed to diminish the rights, privileges, or remedies of any whistleblower under section 1057, any other Federal or State law, or under any collective bargaining agreement. (i) Rulemaking authority The Bureau shall have the authority to issue such rules and regulations as may be necessary or appropriate to implement the provisions of this section consistent with the purposes of this section. (j) Original information Information submitted to the Bureau by a whistleblower in accordance with rules or regulations implementing this section shall not lose its status as original information solely because the whistleblower submitted such information prior to the effective date of such rules or regulations, provided such information was submitted after the date of enactment of this section. (k) Provision of false information A whistleblower who knowingly and willfully makes any false, fictitious, or fraudulent statement or representation, or who makes or uses any false writing or document knowing the same to contain any false, fictitious, or fraudulent statement or entry, shall not be entitled to an award under this section and shall be subject to prosecution under section 1001 of title 18, United States Code. (l) Unenforceability of certain agreements (1) No waiver of rights and remedies Except as provided under paragraph (3), and notwithstanding any other provision of law, the rights and remedies provided for in this section may not be waived by any agreement, policy, form, or condition of employment, including by any predispute arbitration agreement. (2) No predispute arbitration agreements Except as provided under paragraph (3), and notwithstanding any other provision of law, no predispute arbitration agreement shall be valid or enforceable to the extent that the agreement requires arbitration of a dispute arising under this section. (3) Exception Notwithstanding paragraphs (1) and (2), an arbitration provision in a collective bargaining agreement shall be enforceable as to disputes arising under this section, unless the Bureau determines, by rule, that such provision is inconsistent with the purposes of this title. .\n##### (b) Consumer Financial Civil Penalty Fund\nSection 1017(d)(2) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5497(d)(2) ) is amended, in the first sentence, by inserting and for awards authorized under section 1017A before the period at the end.\n#### 3. Funding cap for the Bureau of Consumer Financial Protection\nSection 1017(a)(2)(A)(iii) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5497(a)(2)(A)(iii) ) is amended by striking 6.5 and inserting 12 .",
      "versionDate": "2025-07-24",
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
        "updateDate": "2025-09-12T14:42:28Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2429is.xml"
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
      "title": "Stop the Scammers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the Scammers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consumer Financial Protection Act of 2010 to ensure the Bureau of Consumer Financial Protection retains adequate resources to ensure fair, transparent, and competitive markets for financial products and services for consumers and to provide for whistleblower incentives and protection.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:23Z"
    }
  ]
}
```
