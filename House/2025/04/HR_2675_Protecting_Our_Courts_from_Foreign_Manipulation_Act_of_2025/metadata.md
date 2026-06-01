# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2675
- Title: Protecting Our Courts from Foreign Manipulation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2675
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-04-29T08:06:52Z
- Update date including text: 2026-04-29T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-11-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-11-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2675",
    "number": "2675",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:52Z",
    "updateDateIncludingText": "2026-04-29T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
            "date": "2025-11-20T18:26:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-18T19:59:44Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-07T16:03:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "MN"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NE"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "IL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MO"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "WA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "NC"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "KY"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "MO"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "IA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "KS"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "WI"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2675ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2675\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Cline introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 111 of title 28, United States Code, to increase transparency and oversight of third-party funding by foreign persons, to prohibit third-party funding by foreign states and sovereign wealth funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Courts from Foreign Manipulation Act of 2025 .\n#### 2. Transparency and limitations on foreign third-party litigation funding\n##### (a) In general\nChapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Transparency and limitations on foreign third-party litigation funding (a) Definitions In this section\u2014 (1) the term foreign person \u2014 (A) means any person or entity that is not a United States person, as defined in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ); and (B) does not include a foreign state or a sovereign wealth fund; (2) the term foreign state has the meaning given that term in section 1603; and (3) the term sovereign wealth fund means an investment fund owned or controlled by a foreign state, an agency or instrumentality of a foreign state (as defined in section 1603), or an agent of a foreign principal (as defined in section 1 of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 )). (b) Disclosure of third-Party litigation funding and foreign source certification by foreign persons, foreign states, and sovereign wealth funds (1) In general In any civil action, each party or the counsel of record for the party shall\u2014 (A) disclose in writing to the court, to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security\u2014 (i) the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of any foreign person, foreign state, or sovereign wealth fund, other than the named parties or counsel of record, that has a right to receive any payment that is contingent in any respect on the outcome of the civil action by settlement, judgment, or otherwise; (ii) the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of any foreign person, foreign state, or sovereign wealth fund, other than the named parties or counsel of record, that has a right to receive any payment that is contingent in any respect on the outcome of any matter within a portfolio that includes the civil action and involves the same counsel of record or affiliated counsel; and (iii) if the party or the counsel of record for the party submits a certification described in subparagraph (C)(i), the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of the foreign person, foreign state, or sovereign wealth fund that is the source of the money; (B) produce to the court, to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security, except as otherwise stipulated or ordered by the court, a copy of any agreement creating a contingent right described in subparagraph (A); and (C) for a civil action involving an agreement creating a right to receive any payment by anyone, other than the named parties or counsel of record, that is contingent in any respect on the outcome of the civil action by settlement, judgment, or otherwise, or on the outcome of any matter within a portfolio that includes the civil action and involves the same counsel or affiliated counsel, submit to the court a certification that\u2014 (i) the money that has been or will be used to satisfy any term of the agreement has been or will be directly or indirectly sourced, in whole or in part, from a foreign person, foreign state, or sovereign wealth fund, including the monetary amounts that have been or will be used to satisfy the agreement; or (ii) that the disclosure and certification criteria set forth in subparagraph (A)(iii) and clause (i) of this subparagraph do not apply to the civil action. (2) Timing (A) In general The disclosure and certification required by paragraph (1) shall be made not later than the later of\u2014 (i) 30 days after execution of any agreement described in paragraph (1); or (ii) the date on which the civil action is filed. (B) Parties served or joined later A party that enters into an agreement described in paragraph (1) that is first served or joined after the date on which the civil action is filed shall make the disclosure and certification required by paragraph (1) not later than 30 days after being served or joined, unless a different time is set by stipulation or court order. (3) Foreign source disclosure and certification format (A) In general A disclosure required under paragraph (1)(A) and a certification required under paragraph (1)(C) shall\u2014 (i) be made in the form of a declaration under penalty of perjury pursuant to section 1746 and shall be made to the best knowledge, information, and belief of the declarant formed after reasonable inquiry; and (ii) be provided to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security by the party or counsel of record for the party making the disclosure and certification, except as otherwise stipulated or ordered by the court. (B) Supplementation and correction Not later than 30 days after the date on which a party or counsel of record for the party knew or should have known that the disclosure required under paragraph (1)(A) or a certification required under paragraph (1)(C) is incomplete or inaccurate in any material respect, the party or counsel of record shall supplement or correct the disclosure or certification. (c) Prohibition on third-Party funding litigation by foreign states and sovereign wealth funds (1) In general It shall be unlawful for any party to or counsel of record for a civil action to enter into an agreement creating a right for anyone, other than the named parties or counsel of record, to receive any payment that is contingent in any respect on the outcome of a civil action or any matter within a portfolio that includes the civil action and involves the same counsel of record or affiliated counsel, the terms of which are to be satisfied by money that has been or will be directly or indirectly sourced, in whole or in part, from a foreign state or a sovereign wealth fund. (2) Enforcement Any agreement entered in violation of paragraph (1) shall be null and void. (d) Failure To disclose, To supplement; sanctions A disclosure, production, or certification under subsection (b) is deemed to be information required by rule 26(a) of the Federal Rules of Civil Procedure and subject to the sanctions provisions of rule 37 of the Federal Rules of Civil Procedure. .\n##### (b) Technical and conforming amendment\nThe table of sections chapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Transparency and limitations on foreign third-party litigation funding. .\n#### 3. Report to Congress\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on the activities involving foreign third-party litigation funding in Federal courts, including, if applicable\u2014\n**(1)**\nthe identities of foreign third-party litigation funders in Federal courts, including names, addresses, and citizenship or country of incorporation or registration;\n**(2)**\nthe identities of foreign persons, foreign states, or sovereign wealth funds (as such terms are defined in section 1660 of title 28, United States Code, as added by section 2 of this Act) that have been the sources of money for third-party litigation funding in Federal courts;\n**(3)**\nthe judicial districts in which foreign third-party litigation funding has occurred;\n**(4)**\nan estimate of the total amount of foreign-sourced money used for third-party litigation funding in Federal courts, including an estimate of the amount of such money sourced from each country; and\n**(5)**\na summary of the subject matters of the civil actions in Federal courts for which foreign sourced money has been used for third-party litigation funding.\n#### 4. Applicability\nThe amendments made by this Act shall apply to any civil action pending on or commenced on or after the date of enactment of this Act.",
      "versionDate": "2025-04-07",
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3180",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-12-11T17:17:46Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T17:17:59Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-12-11T17:18:05Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-12-11T17:17:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-05-05T12:12:41Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2675ih.xml"
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
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 111 of title 28, United States Code, to increase transparency and oversight of third-party funding by foreign persons, to prohibit third-party funding by foreign states and sovereign wealth funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:26Z"
    }
  ]
}
```
