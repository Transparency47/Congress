# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3180?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3180
- Title: Protecting Our Courts from Foreign Manipulation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3180
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3180",
    "number": "3180",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-18",
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
        "item": [
          {
            "date": "2025-11-18T21:35:07Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-18T21:35:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3180is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3180\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 111 of title 28, United States Code, to increase transparency and oversight of third-party funding by foreign persons, to prohibit third-party funding by foreign states and sovereign wealth funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Courts from Foreign Manipulation Act of 2025 .\n#### 2. Transparency and limitations on foreign third-party litigation funding\n##### (a) In general\nChapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Transparency and limitations on foreign third-party litigation funding (a) Definitions In this section\u2014 (1) the term foreign person \u2014 (A) means any person or entity that is not a United States person, as defined in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ); and (B) does not include a foreign state or a sovereign wealth fund; (2) the term foreign state has the meaning given that term in section 1603; and (3) the term sovereign wealth fund means an investment fund owned or controlled by\u2014 (A) a foreign state, an agency or instrumentality of a foreign state (as defined in section 1603); or (B) (i) an entity, a majority of whose shares or other ownership interest is owned or controlled by an investment fund owned or controlled by a foreign state, or by an agency or instrumentality of a foreign state (as defined in section 1603); or (ii) any subsidiary of an entity described in clause (i). (b) Disclosure of third-Party litigation funding and foreign source certification by foreign persons, foreign states, and sovereign wealth funds (1) In general In any civil action, each party or the counsel of record for the party shall\u2014 (A) disclose in writing to the court, to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security\u2014 (i) the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of any foreign person, foreign state, or sovereign wealth fund, other than the named parties or counsel of record, that has a right to receive any payment that is contingent in any respect on the outcome of the civil action by settlement, judgment, or otherwise; (ii) the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of any foreign person, foreign state, or sovereign wealth fund, other than the named parties or counsel of record, that has a right to receive any payment that is contingent in any respect on the outcome of any matter within a portfolio that includes the civil action and involves the same counsel of record or affiliated counsel; and (iii) if the party or the counsel of record for the party submits a certification described in subparagraph (C)(i), the name, the address, and, if applicable, the citizenship or the country of incorporation or registration of the foreign person, foreign state, or sovereign wealth fund that is the source of the money; (B) produce to the court, to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security, except as otherwise stipulated or ordered by the court, a copy of any agreement creating a contingent right described in subparagraph (A); and (C) for a civil action involving an agreement creating a right to receive any payment by anyone, other than the named parties or counsel of record, that is contingent in any respect on the outcome of the civil action by settlement, judgment, or otherwise, or on the outcome of any matter within a portfolio that includes the civil action and involves the same counsel or affiliated counsel, submit to the court a certification that\u2014 (i) the money that has been or will be used to satisfy any term of the agreement has been or will be directly or indirectly sourced, in whole or in part, from a foreign person, foreign state, or sovereign wealth fund, including the monetary amounts that have been or will be used to satisfy the agreement; or (ii) that the disclosure and certification criteria set forth in subparagraph (A)(iii) and clause (i) of this subparagraph do not apply to the civil action. (2) Timing (A) In general The disclosure and certification required by paragraph (1) shall be made not later than the later of\u2014 (i) 30 days after execution of any agreement described in paragraph (1); or (ii) the date on which the civil action is filed. (B) Parties served or joined later A party that enters into an agreement described in paragraph (1) that is first served or joined after the date on which the civil action is filed shall make the disclosure and certification required by paragraph (1) not later than 30 days after being served or joined, unless a different time is set by stipulation or court order. (3) Foreign source disclosure and certification format (A) In general A disclosure required under paragraph (1)(A) and a certification required under paragraph (1)(C) shall\u2014 (i) be made in the form of a declaration under penalty of perjury pursuant to section 1746 and shall be made to the best knowledge, information, and belief of the declarant formed after reasonable inquiry; and (ii) be provided to all other named parties to the civil action, to the Attorney General, and to the Principal Deputy Assistant Attorney General for National Security by the party or counsel of record for the party making the disclosure and certification, except as otherwise stipulated or ordered by the court. (B) Supplementation and correction Not later than 30 days after the date on which a party or counsel of record for the party knew or should have known that the disclosure required under paragraph (1)(A) or a certification required under paragraph (1)(C) is incomplete or inaccurate in any material respect, the party or counsel of record shall supplement or correct the disclosure or certification. (c) Prohibition on third-Party funding litigation by foreign states and sovereign wealth funds (1) In general It shall be unlawful for any party to, or counsel of record in a civil action to, enter into an agreement creating a right for anyone, other than the named parties or counsel of record, to receive any payment that is contingent in any respect on the outcome of a civil action, or any matter within a portfolio that includes the civil action, and involves the same counsel of record or affiliated counsel, the terms of which are to be satisfied by money that has been or will be directly or indirectly sourced, in whole or in part, from a foreign state or a sovereign wealth fund. (2) Enforcement Any agreement entered in violation of paragraph (1) shall be null and void. (d) Failure To disclose, To supplement; sanctions A disclosure, production, or certification under subsection (b) is deemed to be information required by rule 26(a) of the Federal Rules of Civil Procedure and subject to the sanctions provisions of rule 37 of the Federal Rules of Civil Procedure. .\n##### (b) Technical and conforming amendment\nThe table of sections chapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Transparency and limitations on foreign third-party litigation funding. .\n#### 3. Report to Congress\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on the activities involving foreign third-party litigation funding in Federal courts, including, if applicable\u2014\n**(1)**\nthe identities of foreign third-party litigation funders in Federal courts, including names, addresses, and citizenship or country of incorporation or registration;\n**(2)**\nthe identities of foreign persons, foreign states, or sovereign wealth funds (as such terms are defined in section 1660 of title 28, United States Code, as added by section 2 of this Act) that have been the sources of money for third-party litigation funding in Federal courts;\n**(3)**\nthe judicial districts in which foreign third-party litigation funding has occurred;\n**(4)**\nan estimate of the total amount of foreign-sourced money used for third-party litigation funding in Federal courts, including an estimate of the amount of such money sourced from each country; and\n**(5)**\na summary of the subject matters of the civil actions in Federal courts for which foreign sourced money has been used for third-party litigation funding.\n#### 4. Applicability\nThe amendments made by this Act shall apply to any civil action pending on or commenced on or after the date of enactment of this Act.",
      "versionDate": "2025-11-18",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-20",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11."
      },
      "number": "2675",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-12-11T17:18:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T17:18:30Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-12-11T17:18:30Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-12-11T17:18:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-12-02T14:52:11Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3180is.xml"
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
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Our Courts from Foreign Manipulation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-25T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 111 of title 28, United States Code, to increase transparency and oversight of third-party funding by foreign persons, to prohibit third-party funding by foreign states and sovereign wealth funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-25T05:18:19Z"
    }
  ]
}
```
