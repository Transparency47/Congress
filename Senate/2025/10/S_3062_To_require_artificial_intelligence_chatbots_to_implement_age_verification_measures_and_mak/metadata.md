# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3062?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3062
- Title: GUARD Act
- Congress: 119
- Bill type: S
- Bill number: 3062
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2026-05-15T19:12:53Z
- Update date including text: 2026-05-15T19:12:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-04-30 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 406.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-04-30 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 406.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3062",
    "number": "3062",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "GUARD Act",
    "type": "S",
    "updateDate": "2026-05-15T19:12:53Z",
    "updateDateIncludingText": "2026-05-15T19:12:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 406.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
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
            "date": "2026-05-11T20:30:49Z",
            "name": "Reported By"
          },
          {
            "date": "2026-04-30T14:15:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-28T19:35:34Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-28T19:35:34Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "AZ"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "UT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VT"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "TN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "RI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3062is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3062\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Hawley (for himself, Mr. Blumenthal , Mrs. Britt , Mr. Warner , Mr. Murphy , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require artificial intelligence chatbots to implement age verification measures and make certain disclosures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guidelines for User Age-verification and Responsible Dialogue Act of 2025 or the GUARD Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence chatbots are increasingly being deployed on social media platforms and in consumer applications used by minors.\n**(2)**\nThese chatbots can generate and disseminate harmful or sexually explicit content to children.\n**(3)**\nThese chatbots can manipulate emotions and influence behavior in ways that exploit the developmental vulnerabilities of minors.\n**(4)**\nThe widespread availability of such chatbots exposes children to physical and psychological safety risks, including grooming, addiction, self-harm, and harm to others.\n**(5)**\nProtecting children from artificial intelligence chatbots that simulate human interaction without accountability is a compelling governmental interest.\n#### 3. Definitions\nIn this Act:\n**(1) AI companion**\nThe term AI companion means an artificial intelligence chatbot that\u2014\n**(A)**\nprovides adaptive, human-like responses to user inputs; and\n**(B)**\nis designed to encourage or facilitate the simulation of interpersonal or emotional interaction, friendship, companionship, or therapeutic communication.\n**(2) Artificial intelligence chatbot**\nThe term artificial intelligence chatbot \u2014\n**(A)**\nmeans any interactive computer service or software application that\u2014\n**(i)**\nproduces new expressive content or responses not fully predetermined by the developer or operator of the service or application; and\n**(ii)**\naccepts open-ended natural-language or multimodal user input and produces adaptive or context-responsive output; and\n**(B)**\ndoes not include an interactive computer service or software application\u2014\n**(i)**\nthe responses of which are limited to contextualized replies; and\n**(ii)**\nthat is unable to respond on a range of topics outside of a narrow specified purpose.\n**(3) Covered entity**\nThe term covered entity means any person who owns, operates, or otherwise makes available an artificial intelligence chatbot to individuals in the United States.\n**(4) Minor**\nThe term minor means any individual who has not attained 18 years of age.\n**(5) Reasonable age verification measure**\nThe term reasonable age verification measure means a method that is authenticated to relate to a user of an artificial intelligence chatbot, such as\u2014\n**(A)**\na government-issued identification; or\n**(B)**\nany other commercially reasonable method that can reliably and accurately\u2014\n**(i)**\ndetermine whether a user is an adult; and\n**(ii)**\nprevent access by minors to AI companions, as required by section 6.\n**(6) Reasonable age verification process**\nThe term reasonable age verification process means an age verification process employed by a covered entity that\u2014\n**(A)**\nuses one or more reasonable age verification measures in order to verify the age of a user of an artificial intelligence chatbot owned, operated, or otherwise made available by the covered entity;\n**(B)**\nprovides that requiring a user to confirm that the user is not a minor, or to insert the user's birth date, is not sufficient to constitute a reasonable age verification measure;\n**(C)**\nensures that each user is subjected to each reasonable age verification measure used by the covered entity as part of the age verification process; and\n**(D)**\ndoes not base verification of a user's age on factors such as whether the user shares an Internet Protocol address, hardware identifier, or other technical indicator with another user determined to not be a minor.\n#### 4. Criminal prohibitions\n##### (a) In general\nPart I of title 18, United States Code, is amended by inserting after chapter 5 the following:\n6 Artificial intelligence Sec. 91. Artificial intelligence chatbots. 91. Artificial intelligence chatbots (a) Definitions In this section: (1) Artificial intelligence chatbot The term artificial intelligence chatbot \u2014 (A) means any interactive computer service or software application that\u2014 (i) produces new expressive content or responses not fully predetermined by the developer or operator of the service or application; and (ii) accepts open-ended natural-language or multimodal user input and produces adaptive or context-responsive output; and (B) does not include an interactive computer service or software application\u2014 (i) the responses of which are limited to contextualized replies; and (ii) that is unable to respond on a range of topics outside of a narrow specified purpose. (2) Minor The term minor means any individual who has not attained 18 years of age. (3) Sexually explicit conduct The term sexually explicit conduct has the meaning given the term in section 2256. (b) Solicitation of minors (1) Offense It shall be unlawful to design, develop, or make available an artificial intelligence chatbot, knowing or with reckless disregard for the fact that the artificial intelligence chatbot poses a risk of soliciting, encouraging, or inducing minors to\u2014 (A) engage in, describe, or simulate sexually explicit conduct; or (B) create or transmit any visual depiction of sexually explicit conduct, including any visual depiction described in section 1466A(a). (2) Penalty Any person who violates paragraph (1) shall be fined not more than $100,000 per offense. (c) Promotion of physical violence (1) Offense It shall be unlawful to design, develop, or make available an artificial intelligence chatbot, knowing or with reckless disregard for the fact that the artificial intelligence chatbot encourages, promotes, or coerces suicide, non-suicidal self-injury, or imminent physical or sexual violence. (2) Penalty Any person who violates paragraph (1) shall be fined not more than $100,000 per offense. .\n##### (b) Technical and conforming amendment\nThe table of chapters for part I of title 18, United States Code, is amended by inserting after the item relating to chapter 5 the following:\n6. Artificial intelligence 91 .\n#### 5. Covered entity obligations\n##### (a) Creation of user accounts\nA covered entity shall require each individual accessing an artificial intelligence chatbot to make a user account in order to use or otherwise interact with such chatbot.\n##### (b) Age verification\n**(1) Age verification of existing accounts**\nWith respect to each user account of an artificial intelligence chatbot that exists as of the effective date of this Act, a covered entity shall\u2014\n**(A)**\non such date, freeze any such account;\n**(B)**\nin order to restore the functionality of such account, require that the user provide age data that is verifiable using a reasonable age verification process, subject to paragraph (4); and\n**(C)**\nusing such age data, classify each user as a minor or an adult.\n**(2) Age verification of new accounts**\nAt the time an individual creates a new user account to use or interact with an artificial intelligence chatbot, a covered entity shall\u2014\n**(A)**\nrequest age data from the individual;\n**(B)**\nverify the individual\u2019s age using a reasonable age verification process, subject to paragraph (4); and\n**(C)**\nusing such age data, classify each user as a minor or an adult.\n**(3) Periodic age verification**\nA covered entity shall periodically review previously verified user accounts using a reasonable age verification process, subject to paragraph (4), to ensure compliance with this Act.\n**(4) Use of third parties**\nFor purposes of paragraphs (1)(B), (2)(B), and (3), a covered entity may contract with a third party to employ reasonable age verification measures as part of the covered entity's reasonable age verification process, but the use of such a third party shall not relieve the covered entity of its obligations under this Act or from liability under this Act.\n**(5) Age verification measure data security**\nA covered entity\u2014\n**(A)**\nshall establish, implement, and maintain reasonable data security to\u2014\n**(i)**\nlimit collection of personal data to that which is minimally necessary to verify a user\u2019s age or maintain compliance with this Act; and\n**(ii)**\nprotect such age verification data against unauthorized access;\n**(B)**\nshall protect such age verification data against unauthorized access;\n**(C)**\nshall protect the integrity and confidentiality of such data by only transmitting such data using industry-standard encryption protocols;\n**(D)**\nshall retain such data for no longer than is reasonably necessary to verify a user\u2019s age or maintain compliance with this Act; and\n**(E)**\nmay not share with, transfer to, or sell to, any other entity such data.\n##### (c) Required disclosures for artificial intelligence chatbots\n**(1) Disclosure of non-human status**\nEach artificial intelligence chatbot made available to users shall\u2014\n**(A)**\nat the initiation of each conversation with a user and at 30-minute intervals, clearly and conspicuously disclose to the user that the chatbot is an artificial intelligence system and not a human being; and\n**(B)**\nbe programmed to ensure that the chatbot does not claim to be a human being or otherwise respond deceptively when asked by a user if the chatbot is a human being.\n**(2) Disclosure regarding non-professional status**\n**(A) In general**\nAn artificial intelligence chatbot may not represent, directly or indirectly, that the chatbot is a licensed professional, including a therapist, physician, lawyer, financial advisor, or other professional.\n**(B) Other limitations**\nEach artificial intelligence chatbot made available to users shall, at the initiation of each conversation with a user and at reasonably regular intervals, clearly and conspicuously disclose to the user that\u2014\n**(i)**\nthe chatbot does not provide medical, legal, financial, or psychological services; and\n**(ii)**\nusers of the chatbot should consult a licensed professional for such advice.\n#### 6. Prohibition on minor use of AI companions\nIf the age verification process described in section 5(b) determines that an individual is a minor, a covered entity shall prohibit the minor from accessing or using any AI companion owned, operated, or otherwise made available by the covered entity.\n#### 7. Enforcement\n##### (a) In general\nIn the case of a violation of section 5 or 6, or a regulation promulgated thereunder, the Attorney General may bring a civil action in an appropriate district court of the United States to\u2014\n**(1)**\nenjoin the violation;\n**(2)**\nenforce compliance with section 5 or 6, or the regulation promulgated thereunder; or\n**(3)**\nobtain civil penalties under subsection (c) of this section, restitution, and other appropriate relief.\n##### (b) Attorney General powers\n**(1) Investigatory powers**\nFor the purpose of conducting investigations or bringing enforcement actions under this section, the Attorney General may issue subpoenas, administer oaths, and compel the production of documents or testimony.\n**(2) Rulemaking**\nThe Attorney General may promulgate any regulations necessary to carry out this Act.\n##### (c) Civil penalties\n**(1) In general**\nAny person who violates section 5 or 6, or a regulation promulgated thereunder, shall be subject to a civil penalty not to exceed $100,000 for each violation.\n**(2) Separate violations**\nEach violation described in paragraph (1) shall be considered a separate violation.\n##### (d) State enforcement\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by the engagement of any covered entity in a violation of this Act or a regulation promulgated thereunder, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States or a State court of appropriate jurisdiction to obtain injunctive relief.\n##### (e) Relationship to State laws\nNothing in this Act or an amendment made by this Act, or any regulation promulgated thereunder, shall be construed to prohibit or otherwise affect the enforcement of any State law or regulation that is at least as protective of users of artificial intelligence chatbots as this Act and the amendments made by this Act, and the regulations promulgated thereunder.\n#### 8. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-10-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3062rs.xml",
      "text": "II\nCalendar No. 406\n119th CONGRESS\n2d Session\nS. 3062\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Hawley (for himself, Mr. Blumenthal , Mrs. Britt , Mr. Warner , Mr. Murphy , Mr. Kelly , Mr. Gallego , Mr. Lee , Mr. Lankford , Mr. Cotton , Mr. Welch , Ms. Hassan , Ms. Cortez Masto , Mr. Kaine , Mrs. Gillibrand , Mr. Ricketts , Mrs. Blackburn , Mr. Whitehouse , Mr. Durbin , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 11, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require artificial intelligence chatbots to implement age verification measures and make certain disclosures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guidelines for User Age-verification and Responsible Dialogue Act of 2025 or the GUARD Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence chatbots are increasingly being deployed on social media platforms and in consumer applications used by minors.\n**(2)**\nThese chatbots can generate and disseminate harmful or sexually explicit content to children.\n**(3)**\nThese chatbots can manipulate emotions and influence behavior in ways that exploit the developmental vulnerabilities of minors.\n**(4)**\nThe widespread availability of such chatbots exposes children to physical and psychological safety risks, including grooming, addiction, self-harm, and harm to others.\n**(5)**\nProtecting children from artificial intelligence chatbots that simulate human interaction without accountability is a compelling governmental interest.\n#### 3. Definitions\nIn this Act:\n**(1) AI companion**\nThe term AI companion means an artificial intelligence chatbot that\u2014\n**(A)**\nprovides adaptive, human-like responses to user inputs; and\n**(B)**\nis designed to encourage or facilitate the simulation of interpersonal or emotional interaction, friendship, companionship, or therapeutic communication.\n**(2) Artificial intelligence chatbot**\nThe term artificial intelligence chatbot \u2014\n**(A)**\nmeans any interactive computer service or software application that\u2014\n**(i)**\nproduces new expressive content or responses not fully predetermined by the developer or operator of the service or application; and\n**(ii)**\naccepts open-ended natural-language or multimodal user input and produces adaptive or context-responsive output; and\n**(B)**\ndoes not include an interactive computer service or software application\u2014\n**(i)**\nthe responses of which are limited to contextualized replies; and\n**(ii)**\nthat is unable to respond on a range of topics outside of a narrow specified purpose.\n**(3) Covered entity**\nThe term covered entity means any person who owns, operates, or otherwise makes available an artificial intelligence chatbot to individuals in the United States.\n**(4) Minor**\nThe term minor means any individual who has not attained 18 years of age.\n**(5) Reasonable age verification measure**\nThe term reasonable age verification measure means a method that is authenticated to relate to a user of an artificial intelligence chatbot, such as\u2014\n**(A)**\na government-issued identification; or\n**(B)**\nany other commercially reasonable method that can reliably and accurately\u2014\n**(i)**\ndetermine whether a user is an adult; and\n**(ii)**\nprevent access by minors to AI companions, as required by section 6.\n**(6) Reasonable age verification process**\nThe term reasonable age verification process means an age verification process employed by a covered entity that\u2014\n**(A)**\nuses one or more reasonable age verification measures in order to verify the age of a user of an artificial intelligence chatbot owned, operated, or otherwise made available by the covered entity;\n**(B)**\nprovides that requiring a user to confirm that the user is not a minor, or to insert the user's birth date, is not sufficient to constitute a reasonable age verification measure;\n**(C)**\nensures that each user is subjected to each reasonable age verification measure used by the covered entity as part of the age verification process; and\n**(D)**\ndoes not base verification of a user's age on factors such as whether the user shares an Internet Protocol address, hardware identifier, or other technical indicator with another user determined to not be a minor.\n#### 4. Criminal prohibitions\n##### (a) In general\nPart I of title 18, United States Code, is amended by inserting after chapter 5 the following:\n6 Artificial intelligence Sec. 91. Artificial intelligence chatbots. 91. Artificial intelligence chatbots (a) Definitions In this section: (1) Artificial intelligence chatbot The term artificial intelligence chatbot \u2014 (A) means any interactive computer service or software application that\u2014 (i) produces new expressive content or responses not fully predetermined by the developer or operator of the service or application; and (ii) accepts open-ended natural-language or multimodal user input and produces adaptive or context-responsive output; and (B) does not include an interactive computer service or software application\u2014 (i) the responses of which are limited to contextualized replies; and (ii) that is unable to respond on a range of topics outside of a narrow specified purpose. (2) Minor The term minor means any individual who has not attained 18 years of age. (3) Sexually explicit conduct The term sexually explicit conduct has the meaning given the term in section 2256. (b) Solicitation of minors (1) Offense It shall be unlawful to design, develop, or make available an artificial intelligence chatbot, knowing or with reckless disregard for the fact that the artificial intelligence chatbot poses a risk of soliciting, encouraging, or inducing minors to\u2014 (A) engage in, describe, or simulate sexually explicit conduct; or (B) create or transmit any visual depiction of sexually explicit conduct, including any visual depiction described in section 1466A(a). (2) Penalty Any person who violates paragraph (1) shall be fined not more than $100,000 per offense. (c) Promotion of physical violence (1) Offense It shall be unlawful to design, develop, or make available an artificial intelligence chatbot, knowing or with reckless disregard for the fact that the artificial intelligence chatbot encourages, promotes, or coerces suicide, non-suicidal self-injury, or imminent physical or sexual violence. (2) Penalty Any person who violates paragraph (1) shall be fined not more than $100,000 per offense. .\n##### (b) Technical and conforming amendment\nThe table of chapters for part I of title 18, United States Code, is amended by inserting after the item relating to chapter 5 the following:\n6. Artificial intelligence 91 .\n#### 5. Covered entity obligations\n##### (a) Creation of user accounts\nA covered entity shall require each individual accessing an artificial intelligence chatbot to make a user account in order to use or otherwise interact with such chatbot.\n##### (b) Age verification\n**(1) Age verification of existing accounts**\nWith respect to each user account of an artificial intelligence chatbot that exists as of the effective date of this Act, a covered entity shall\u2014\n**(A)**\non such date, freeze any such account;\n**(B)**\nin order to restore the functionality of such account, require that the user provide age data that is verifiable using a reasonable age verification process, subject to paragraph (4); and\n**(C)**\nusing such age data, classify each user as a minor or an adult.\n**(2) Age verification of new accounts**\nAt the time an individual creates a new user account to use or interact with an artificial intelligence chatbot, a covered entity shall\u2014\n**(A)**\nrequest age data from the individual;\n**(B)**\nverify the individual\u2019s age using a reasonable age verification process, subject to paragraph (4); and\n**(C)**\nusing such age data, classify each user as a minor or an adult.\n**(3) Periodic age verification**\nA covered entity shall periodically review previously verified user accounts using a reasonable age verification process, subject to paragraph (4), to ensure compliance with this Act.\n**(4) Use of third parties**\nFor purposes of paragraphs (1)(B), (2)(B), and (3), a covered entity may contract with a third party to employ reasonable age verification measures as part of the covered entity's reasonable age verification process, but the use of such a third party shall not relieve the covered entity of its obligations under this Act or from liability under this Act.\n**(5) Age verification measure data security**\nA covered entity\u2014\n**(A)**\nshall establish, implement, and maintain reasonable data security to\u2014\n**(i)**\nlimit collection of personal data to that which is minimally necessary to verify a user\u2019s age or maintain compliance with this Act; and\n**(ii)**\nprotect such age verification data against unauthorized access;\n**(B)**\nshall protect such age verification data against unauthorized access;\n**(C)**\nshall protect the integrity and confidentiality of such data by only transmitting such data using industry-standard encryption protocols;\n**(D)**\nshall retain such data for no longer than is reasonably necessary to verify a user\u2019s age or maintain compliance with this Act; and\n**(E)**\nmay not share with, transfer to, or sell to, any other entity such data.\n##### (c) Required disclosures for artificial intelligence chatbots\n**(1) Disclosure of non-human status**\nEach artificial intelligence chatbot made available to users shall\u2014\n**(A)**\nat the initiation of each conversation with a user and at 30-minute intervals, clearly and conspicuously disclose to the user that the chatbot is an artificial intelligence system and not a human being; and\n**(B)**\nbe programmed to ensure that the chatbot does not claim to be a human being or otherwise respond deceptively when asked by a user if the chatbot is a human being.\n**(2) Disclosure regarding non-professional status**\n**(A) In general**\nAn artificial intelligence chatbot may not represent, directly or indirectly, that the chatbot is a licensed professional, including a therapist, physician, lawyer, financial advisor, or other professional.\n**(B) Other limitations**\nEach artificial intelligence chatbot made available to users shall, at the initiation of each conversation with a user and at reasonably regular intervals, clearly and conspicuously disclose to the user that\u2014\n**(i)**\nthe chatbot does not provide medical, legal, financial, or psychological services; and\n**(ii)**\nusers of the chatbot should consult a licensed professional for such advice.\n#### 6. Prohibition on minor use of AI companions\nIf the age verification process described in section 5(b) determines that an individual is a minor, a covered entity shall prohibit the minor from accessing or using any AI companion owned, operated, or otherwise made available by the covered entity.\n#### 7. Enforcement\n##### (a) In general\nIn the case of a violation of section 5 or 6, or a regulation promulgated thereunder, the Attorney General may bring a civil action in an appropriate district court of the United States to\u2014\n**(1)**\nenjoin the violation;\n**(2)**\nenforce compliance with section 5 or 6, or the regulation promulgated thereunder; or\n**(3)**\nobtain civil penalties under subsection (c) of this section, restitution, and other appropriate relief.\n##### (b) Attorney General powers\n**(1) Investigatory powers**\nFor the purpose of conducting investigations or bringing enforcement actions under this section, the Attorney General may issue subpoenas, administer oaths, and compel the production of documents or testimony.\n**(2) Rulemaking**\nThe Attorney General may promulgate any regulations necessary to carry out this Act.\n##### (c) Civil penalties\n**(1) In general**\nAny person who violates section 5 or 6, or a regulation promulgated thereunder, shall be subject to a civil penalty not to exceed $100,000 for each violation.\n**(2) Separate violations**\nEach violation described in paragraph (1) shall be considered a separate violation.\n##### (d) State enforcement\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by the engagement of any covered entity in a violation of this Act or a regulation promulgated thereunder, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States or a State court of appropriate jurisdiction to obtain injunctive relief.\n##### (e) Relationship to State laws\nNothing in this Act or an amendment made by this Act, or any regulation promulgated thereunder, shall be construed to prohibit or otherwise affect the enforcement of any State law or regulation that is at least as protective of users of artificial intelligence chatbots as this Act and the amendments made by this Act, and the regulations promulgated thereunder.\n#### 8. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-05-11",
      "versionType": "Reported in Senate"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-15T19:12:53Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3062is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3062rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Guidelines for User Age-verification and Responsible Dialogue Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guidelines for User Age-verification and Responsible Dialogue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require artificial intelligence chatbots to implement age verification measures and make certain disclosures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T06:18:18Z"
    }
  ]
}
```
