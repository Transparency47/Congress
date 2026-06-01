# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8721?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8721
- Title: Preventing Foreign Interference in American Elections Act
- Congress: 119
- Bill type: HR
- Bill number: 8721
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-19T08:05:44Z
- Update date including text: 2026-05-19T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-11 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-11 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8721",
    "number": "8721",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Preventing Foreign Interference in American Elections Act",
    "type": "HR",
    "updateDate": "2026-05-19T08:05:44Z",
    "updateDateIncludingText": "2026-05-19T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
        "item": [
          {
            "date": "2026-05-14T17:15:05Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-11T14:30:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-11T14:30:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8721ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8721\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Steil introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prevent foreign interference in United States elections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Foreign Interference in American Elections Act .\n#### 2. Modifications to foreign money ban\n##### (a) Additional restrictions\n**(1) In general**\nSection 319(a)(1) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(a)(1) ) is amended\u2014\n**(A)**\nby striking or at the end of subparagraph (B); and\n**(B)**\nby adding at the end the following new subparagraph:\n(D) a donation for the purpose of\u2014 (i) voter registration activity; (ii) ballot collection; (iii) voter identification; (iv) get-out-the-vote activity; (v) any public communication that refers to a clearly identified Federal, State, or local political party; or (vi) the administration of a Federal, State, or local election; or .\n**(2) Conforming amendment**\nSection 319(a)(2) of such Act ( 52 U.S.C. 30121(a)(2) ) is amended by striking subparagraph (A) or (B) of paragraph (1) and inserting subparagraph (A), (B), or (D) of paragraph (1) .\n##### (b) Prohibition on aiding or facilitating violations\nSection 319(a) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(a) ), as amended by subsection (a) , is amended\u2014\n**(1)**\nin paragraph (1)(D), by striking or at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) a person to knowingly aid or facilitate a violation of paragraph (1) or (2). .\n##### (c) Indirect contributions\nSection 319 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121 ) is amended by adding at the end the following new subsection:\n(c) Indirect contributions For purposes of this section, a person shall be treated as having indirectly made a contribution, donation, expenditure, or disbursement described in subparagraphs (A), (B), (C), or (D) of subsection (a)(1) if such person has made a contribution or donation to a person with a designation, instruction, or encumbrance (whether direct or indirect, express or implied, oral or written, or involving intermediaries or conduits) which results in any part of such contribution, donation, expenditure, or disbursement being used for an activity described in subparagraphs (A), (B), (C), or (D) of subsection (a)(1). .\n##### (d) Enforcement provisions\nSection 319 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121 ), as amended by subsection (c), is amended by adding at the end the following new subsection:\n(d) Enforcement (1) Use of certification as a defense (A) In general In the case of any allegation that a person has violated subsection (a), any person alleged in the complaint may, in connection with a response to such allegation under section 309(a)(1), submit, under penalty of perjury, a certification that no such violation has occurred. (B) Effect of submission The Commission shall take into consideration any certification submitted under subparagraph (A) in making a determination under section 309(a)(2) whether there is reason to believe such violation has occurred. (2) Limitation on investigations (A) In general If the Commission makes a determination under section 309(a)(2) that there is reason to believe a violation of subsection (a) has occurred or is about to occur, any investigation of such alleged violation shall be limited in scope to the factual matter necessary to determine whether such alleged violation occurred. (B) Petition to quash subpoena or order on basis not limited in scope to necessary factual matter (i) In general A person subject to an investigation by the Commission following a determination of the Commission that there is reason to believe a violation of subsection (a) has occurred or is about to occur may file a petition in any United States district court with jurisdiction to quash any subpoena or order of the Commission issued under paragraph (3) or (4), respectively, of section 307(a) on the basis that the subpoena or order is not limited in scope to the factual matter necessary to determine whether such alleged violation occurred as required under subparagraph (A). (ii) Clarification Nothing in clause (i) shall be construed to alter the right of any person to otherwise challenge the power of the Commission to issue a subpoena under section 307(a)(3) or an order under section 307(a)(4). .\n##### (e) Reporting\n**(1) Contributions and expenditures of political committees and political parties**\nSection 304(b) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30104(b) ) is amended\u2014\n**(A)**\nby striking and at the end of paragraph (7);\n**(B)**\nby striking the period at the end of paragraph (8) and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(9) under penalty of perjury, a certification that the committee has complied with the requirements of section 319(a). .\n**(2) Independent expenditures**\n**(A) Committee reports**\nSection 304(b)(6)(B)(iii) of such Act ( 52 U.S.C. 30104(b)(6)(B)(iii) ) is amended\u2014\n**(i)**\nby striking and a certification and inserting a certification ; and\n**(ii)**\nby inserting , and a certification, under penalty of perjury, that the independent expenditure does not violate section 319(a) before the semicolon at the end.\n**(B) Other persons**\nSection 304(c)(2) of such Act ( 52 U.S.C. 30104(c)(2) ) is amended\u2014\n**(i)**\nby striking and at the end of subparagraph (B);\n**(ii)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(iii)**\nby inserting after subparagraph (B) the following new subparagraph:\n(C) under penalty of perjury, a certification that the independent expenditure does not violate section 319(a); and .\n**(3) Electioneering communications**\nSection 304(f)(2) of such Act ( 52 U.S.C. 30104(f)(2) ) is amended by adding at the end the following new subparagraph:\n(G) A certification, under penalty of perjury, that the disbursement does not violate section 319(a). .\n#### 3. Protecting privacy of donors to tax-exempt organizations\n##### (a) Restrictions on collection of donor information\n**(1) Restrictions**\nAn entity of the Federal Government may not collect or require the submission of information on the identification of any donor to a tax-exempt organization.\n**(2) Exceptions**\nParagraph (1) does not apply to the following:\n**(A)**\nThe Internal Revenue Service, acting lawfully pursuant to section 6033 of the Internal Revenue Code of 1986 or any successor provision.\n**(B)**\nThe Secretary of the Senate and the Clerk of the House of Representatives, acting lawfully pursuant to section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1604 ).\n**(C)**\nThe Federal Election Commission, acting lawfully pursuant to\u2014\n**(i)**\nsection 510 of title 36, United States Code; or\n**(ii)**\nany provision of title III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ).\n**(D)**\nAn entity acting pursuant to a lawful order of a court or administrative body which has the authority under law to direct the entity to collect or require the submission of the information, but only to the extent permitted by the lawful order of such court or administrative body.\n##### (b) Restrictions on release of donor information\n**(1) Restrictions**\nAn entity of the Federal Government may not disclose to the public information revealing the identification of any donor to a tax-exempt organization.\n**(2) Exceptions**\nParagraph (1) does not apply to the following:\n**(A)**\nThe Internal Revenue Service, acting lawfully pursuant to section 6104 of the Internal Revenue Code of 1986 or any successor provision.\n**(B)**\nThe Secretary of the Senate and the Clerk of the House of Representatives, acting lawfully pursuant to section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1604 ).\n**(C)**\nThe Federal Election Commission, acting lawfully pursuant to\u2014\n**(i)**\nsection 510 of title 36, United States Code; or\n**(ii)**\nany provision of title III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ).\n**(D)**\nAn entity acting pursuant to a lawful order of a court or administrative body which has the authority under law to direct the entity to disclose the information, but only to the extent permitted by the lawful order of such court or administrative body.\n**(E)**\nAn entity which discloses the information as authorized by the organization.\n##### (c) Tax-Exempt organization defined\nIn this section, a tax-exempt organization means an organization which is described in section 501(c) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code. Nothing in this section may be construed to treat a political organization under section 527 of such Code as a tax-exempt organization for purposes of this section.\n##### (d) Penalties\nIt shall be unlawful for any officer or employee of the United States, or any former officer or employee, willfully to disclose to any person, except as authorized in this section, any information revealing the identification of any donor to a tax-exempt organization. Any violation of this section shall be a felony punishable upon conviction by a fine in any amount not exceeding $250,000, or imprisonment of not more than 5 years, or both, together with the costs of prosecution, and if such offense is committed by any officer or employee of the United States, he shall, in addition to any other punishment, be dismissed from office or discharged from employment upon conviction for such offense.\n#### 4. Effective date\n##### (a) Modifications to foreign money ban\n**(1) In general**\nExcept as provided in paragraph (2), section 2 and the amendments made by section 2 shall apply with respect to donations or other amounts provided on or after the date of the enactment of this Act.\n**(2) Reporting requirements**\nSubsection (e) of section 2 and the amendments made by such subsection shall apply with respect to reports filed under the Federal Election Campaign Act of 1971 on or after the date of the enactment of this Act.\n##### (b) Protecting privacy of donors\nSection 3 shall apply with respect to donations made on or after the date of the enactment of this Act.",
      "versionDate": "2026-05-11",
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
        "actionDate": "2025-11-06",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "3129",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Foreign Interference in American Elections Act",
      "type": "S"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-13T21:05:58Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8721ih.xml"
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
      "title": "Preventing Foreign Interference in American Elections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Foreign Interference in American Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prevent foreign interference in United States elections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T08:18:40Z"
    }
  ]
}
```
