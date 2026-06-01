# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/188
- Title: Free Speech Protection Act
- Congress: 119
- Bill type: S
- Bill number: 188
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-02-26T20:12:44Z
- Update date including text: 2025-02-26T20:12:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/188",
    "number": "188",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Free Speech Protection Act",
    "type": "S",
    "updateDate": "2025-02-26T20:12:44Z",
    "updateDateIncludingText": "2025-02-26T20:12:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T19:30:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "UT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s188is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 188\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Paul (for himself, Mr. Lee , Mr. Schmitt , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit Federal employees and contractors from directing online platforms to censor any speech that is protected by the First Amendment to the Constitution of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Free Speech Protection Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered information**\nThe term covered information means information relating to\u2014\n**(A)**\na phone call;\n**(B)**\nany type of digital communication, including a post on a covered platform, an e-mail, a text, and a direct message;\n**(C)**\na photo;\n**(D)**\nshopping and commerce history;\n**(E)**\nlocation data, including a driving route and ride hailing information;\n**(F)**\nan IP address;\n**(G)**\nmetadata;\n**(H)**\nsearch history;\n**(I)**\nthe name, age, or demographic information of a user of a covered platform; and\n**(J)**\na calendar item.\n**(2) Covered platform**\nThe term covered platform means\u2014\n**(A)**\nan interactive computer service, as that term is defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ); and\n**(B)**\nany platform through which a media organization disseminates information, without regard to whether the organization disseminates that information\u2014\n**(i)**\nthrough broadcast or print;\n**(ii)**\nonline; or\n**(iii)**\nthrough any other channel.\n**(3) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(4) Employee**\n**(A) In general**\nExcept where otherwise expressly provided, the term employee \u2014\n**(i)**\nmeans an employee of an Executive agency; and\n**(ii)**\nincludes\u2014\n**(I)**\nan individual, other than an employee of an Executive agency, working under a contract with an Executive agency; and\n**(II)**\nthe President and the Vice President.\n**(B) Rule of construction**\nWith respect to an individual described in subparagraph (A)(ii)(I), solely for the purposes of this Act, the Executive agency that has entered into the contract under which the employee is working shall be construed to be the Executive agency employing the employee.\n**(5) Executive agency**\nThe term Executive agency \u2014\n**(A)**\nhas the meaning given the term in section 105 of title 5, United States Code; and\n**(B)**\nincludes the Executive Office of the President.\n**(6) Provider**\nThe term provider means a provider of a covered platform.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nThe First Amendment to the Constitution of the United States guarantees\u2014\n**(A)**\nfreedoms concerning religion, expression, assembly, and petition of the government;\n**(B)**\nthe freedom of expression by prohibiting the government from restricting the press or the right of an individual to speak freely; and\n**(C)**\nthe right of an individual to assemble peaceably and to petition the government.\n**(2)**\nFreedom of speech is an essential element of liberty that restrains tyranny and empowers individuals.\n**(3)**\nWriting in support of a Bill of Rights, Thomas Jefferson stated that [t]here are rights which it is useless to surrender to the government, and which yet, governments have always been fond to invade. These are the rights of thinking and publishing our thoughts by speaking or writing.\n**(4)**\nThe Supreme Court of the United States (referred to in this section as the Court ) has upheld the right to speak free from governmental interference as a fundamental right.\n**(5)**\nThe Court, in Palko v. Connecticut, 302 U.S. 319 (1937), wrote that freedom of thought and speech is the matrix, the indispensable condition, of nearly every other form of freedom .\n**(6)**\nIn Turner Broadcasting System, Inc. v. Federal Communications Commission, 512 U.S. 622 (1994), the Court stated the following: At the heart of the First Amendment lies the principle that each person should decide for himself or herself the ideas and beliefs deserving of expression, consideration, and adherence. Our political system and cultural life rest upon this ideal. Government action that stifles speech on account of its message, or that requires the utterance of a particular message favored by the Government, contravenes this essential right . . . [and poses] the inherent risk that Government seeks not to advance a legitimate regulatory goal, but to suppress unpopular ideas or manipulate the public debate through coercion rather than persuasion. These restrictions \u2018rais[e] the specter that the Government may effectively drive certain ideas or viewpoints from the marketplace.\u2019 For these reasons, the First Amendment, subject only to narrow and well-understood exceptions, does not countenance government control over the content of messages expressed by private individuals.\n**(7)**\nIn R.A.V. v. City of St. Paul, 505 U.S. 377 (1992), the Court explained that the First Amendment to the Constitution of the United States generally prevents government from proscribing speech, or even expressive conduct, because of disapproval of the ideas expressed. Content-based restrictions are presumptively invalid.\n**(8)**\nThe case of Brandenburg v. Ohio, 395 U.S. 444 (1969), stands for the proposition that speech can be suppressed only if the speech is intended, and is likely to produce, imminent lawless action.\n**(9)**\nJustice William Brennan, in his majority opinion for the Court in Texas v. Johnson, 491 U.S. 397 (1989), asserted that [i]f there is a bedrock principle underlying the First Amendment, it is that the government may not prohibit the expression of an idea simply because society finds the idea itself offensive or disagreeable.\n**(10)**\nJustice Neil Gorsuch, in his majority opinion for the Court in 303 Creative LLC v. Elenis, 600 U.S. 570 (2023), stated, The First Amendment envisions the United States as a rich and complex place where all persons are free to think and speak as they wish, not as the government demands.\n**(11)**\nAs evidenced in disclosures from various social media companies, Federal officials in recent years have sought to censor legal speech on platforms operated by those companies by using the power of their offices to influence what opinions, views, and other content that users of those platforms may disseminate.\n**(12)**\nWhite House officials and officials of Executive agencies sought to silence narratives on social media platforms on issues relating to the COVID\u201319 pandemic.\n**(13)**\nThe Centers for Disease Control and Prevention engaged with officials at Facebook and Twitter to request that certain posts be flagged as disinformation and held regular meetings with those companies to share instances of what government officials determined to be misinformation about the COVID\u201319 pandemic that had been spread on the platforms operated by those companies.\n**(14)**\nIn the midst of the 2020 election cycle, the Federal Bureau of Investigation communicated with high-level technology company executives and suggested that a New York Post story regarding the contents of Hunter Biden\u2019s laptop were part of a hack and leak operation.\n**(15)**\nOn April 27, 2022, the Department of Homeland Security announced the creation of a Disinformation Governance Board (referred to in this paragraph as the Board ). The Director of the Board, Nina Jankowicz, sought to establish an analytic exchange with industry partners . In congressional testimony, Secretary of Homeland Security Alejandro Mayorkas provided misleading testimony about the actions of the Board.\n**(16)**\nSince 2020, 2 nonprofit organizations affiliated with the Global Disinformation Index (referred to in this paragraph as GDI ) have received a total of $330,000 in grants from Federal agencies. GDI maintains a list of global news publications rated high risk for disinformation . Major advertising companies seek guidance from this purported nonpartisan group to determine where advertising money should be spent. Despite the self-proclaimed nonpartisan nature of the list, GDI includes a host of reputable media outlets, such as Reason, RealClearPolitics, and the New York Post.\n#### 4. Employee prohibitions\n##### (a) Prohibitions\n**(1) In general**\nAn employee acting under official authority or influence may not\u2014\n**(A)**\nuse any form of communication (without regard to whether the communication is visible to members of the public) to direct, coerce, compel, or encourage a provider to take, suggest or imply that a provider should take, or request that a provider take any action to censor speech that is protected by the Constitution of the United States, including by\u2014\n**(i)**\nremoving that speech from the applicable covered platform;\n**(ii)**\nsuppressing that speech on the applicable covered platform;\n**(iii)**\nremoving or suspending a particular user (or a class of users) from the applicable covered platform or otherwise limiting the access of a particular user (or a class of users) to the covered platform;\n**(iv)**\nlabeling that speech as disinformation, misinformation, or false, or by making any similar characterization with respect to the speech; or\n**(v)**\notherwise blocking, banning, deleting, deprioritizing, demonetizing, deboosting, limiting the reach of, or restricting access to the speech;\n**(B)**\ndirect or encourage a provider to share with an Executive agency covered information containing data or information regarding a particular topic, or a user or group of users on the applicable covered platform, including any covered information shared or stored by users on the covered platform;\n**(C)**\nwork, directly or indirectly, with any private or public entity or person to take an action that is prohibited under subparagraph (A) or (B); or\n**(D)**\non behalf of the Executive agency employing the employee\u2014\n**(i)**\nenter into a partnership with a provider to monitor any content disseminated on the applicable covered platform; or\n**(ii)**\nsolicit, accept, or enter into a contract or other agreement (including a no-cost agreement) for free advertising or another promotion on a covered platform.\n**(2) Exception**\nNotwithstanding subparagraph (B) of paragraph (1), the prohibition under that subparagraph shall not apply with respect to an action by an Executive agency or employee pursuant to a warrant that is issued by\u2014\n**(A)**\na court of the United States of competent jurisdiction in accordance with the procedures described in rule 41 of the Federal Rules of Criminal Procedure; or\n**(B)**\na State court of competent jurisdiction.\n**(3) Employee discipline**\n**(A) In general**\nNotwithstanding any provision of title 5, United States Code, and subject to subparagraph (B), the head of an Executive agency employing an employee who violates any provision of paragraph (1) (or, in the case of the head of an Executive agency who violates any provision of paragraph (1), the President) shall impose on that employee\u2014\n**(i)**\ndisciplinary action consisting of removal, reduction in grade, suspension, or debarment from employment with the United States;\n**(ii)**\na civil penalty in an amount that is not less than $10,000;\n**(iii)**\nineligibility for any annuity under chapter 83 or 84 of title 5, United States Code; and\n**(iv)**\npermanent revocation of any applicable security clearance held by the employee.\n**(B) Specific contractor discipline**\nIn the case of an employee described in section 2(4)(A)(ii)(I) who violates any provision of paragraph (1), in addition to any discipline that may be applicable under subparagraph (A) of this paragraph, that employee shall be barred from working under any contract with the Federal Government.\n##### (b) Private right of action\n**(1) In general**\nA person, the account, content, speech, or other information of which has been affected in violation of this section, may bring a civil action in the United States District Court for the District of Columbia for reasonable attorneys\u2019 fees, injunctive relief, and actual damages against\u2014\n**(A)**\nthe applicable Executive agency; and\n**(B)**\nthe employee of the applicable Executive agency who committed the violation.\n**(2) Presumption of liability**\nIn a civil action brought under paragraph (1), there shall be a rebuttable presumption against the applicable Executive agency or employee if the person bringing the action demonstrates that the applicable employee communicated with a provider on a matter relating to\u2014\n**(A)**\ncovered information with respect to that person; or\n**(B)**\na statement made by that person on the applicable covered platform.\n#### 5. Reporting requirements\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, and not less frequently than once every 90 days thereafter, the head of each Executive agency shall submit to the Director and the chair and ranking member of the Committee on Homeland Security and Governmental Affairs of the Senate, the Committee on the Judiciary of the Senate, the Committee on Oversight and Government Reform of the House of Representatives, and the Committee on the Judiciary of the House of Representatives a report that discloses, for the period covered by the report, each communication between a representative of a provider and an employee of that Executive agency\u2014\n**(1)**\nincluding any such communication that constitutes a violation of section 4(a)(1); and\n**(2)**\nnot including any such communication that relates to combating child pornography or exploitation, human trafficking, or the illegal transporting or transacting in controlled substances.\n##### (b) Contents\nEach report submitted under subsection (a) shall include, with respect to a communication described in that subsection\u2014\n**(1)**\nthe name and professional title of each employee and each representative of a provider engaged in the communication; and\n**(2)**\nif the communication constitutes a violation of section 4(a)(1)\u2014\n**(A)**\na detailed explanation of the nature of the violation; and\n**(B)**\nthe date of the violation.\n##### (c) Publication\n**(1) In general**\nNot later than 5 days after the date on which the Director receives a report under subsection (a), the Director shall\u2014\n**(A)**\ncollect the report and assign the report a unique tracking number; and\n**(B)**\npublish on a publicly accessible and searchable website the contents of the report and the tracking number for the report.\n**(2) Subject of report**\nWith respect to a report submitted pursuant to subsection (a) of which an individual is a subject, not later than the end of the business day following the business day on which the report is submitted, the Director shall make a reasonable effort to contact any person or entity directly affected by a violation of this Act described in the report to inform that person of the report.\n#### 6. Cybersecurity infrastructure and security agency report\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security shall submit to the Director and the chair and ranking member of the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report that discloses any action of an employee of the Cybersecurity and Infrastructure Security Agency that\u2014\n**(1)**\noccurred between November 16, 2018, and the date of enactment of this Act; and\n**(2)**\nwould have been in violation of section 4(a)(1).\n#### 7. Termination of Disinformation Governance Board\n##### (a) Termination\nThe Disinformation Governance Board established by the Department of Homeland Security, if in existence on the date of enactment of this Act, is terminated.\n##### (b) Prohibition against Federal funding\nNo Federal funds may be used to establish or support the activities of any other entity that is substantially similar to the Disinformation Governance Board terminated pursuant to subsection (a).\n#### 8. Prohibition on misinformation and disinformation grants\nThe head of an Executive agency may not award a grant relating to programming on misinformation or disinformation.\n#### 9. Grant terms\n##### (a) Certification\nThe recipient of a grant awarded by an Executive agency on or after the date of enactment of this Act shall certify to the head of the Executive agency that the recipient or a subgrantee of the recipient, during the term of the grant, will not designate any creator of news content, regardless of medium, as a source of misinformation or disinformation.\n##### (b) Publication\nNot later than 10 days after the date on which an Executive agency awards a grant, the head of the Executive agency shall publish the certification received under subsection (a) with respect to the grant on Grants.gov, or any successor website.\n##### (c) Penalty\nUpon a determination by the head of an Executive agency that a recipient or subgrantee of a recipient has violated the certification of the recipient under subsection (a), the recipient or subgrantee, respectively, shall\u2014\n**(1)**\nrepay the grant associated with the certification; and\n**(2)**\nbe ineligible to receive a grant from the Executive agency.\n#### 10. Presidential war powers under the Communications Act of 1934\n##### (a) In general\nSection 706 of the Communications Act of 1934 ( 47 U.S.C. 606 ) is amended\u2014\n**(1)**\nby striking subsections (c) through (g); and\n**(2)**\nby redesignating subsection (h) as subsection (c).\n##### (b) Technical and conforming amendments\nSection 309(h) of the Communications Act of 1934 ( 47 U.S.C. 309(h) ) is amended\u2014\n**(1)**\nby inserting and before (2) ; and\n**(2)**\nby striking Act; and all that follows through the period at the end and inserting the following: Act. .\n#### 11. Applicability of FOIA\n##### (a) Definition\nIn this section, the term agency has the meaning given the term in section 551 of title 5, United States Code.\n##### (b) Applicability\nNotwithstanding any provision of section 552 of title 5, United States Code, any request made to an agency pursuant to that section for records relating to communication between an employee and a representative of a provider\u2014\n**(1)**\nshall be granted by the agency without regard to any exemption under subsection (b) of that section, except the agency may not release any identifying information of a user of a covered platform without express written consent granted by the user to the agency; and\n**(2)**\nmay not be granted by the agency if the communication occurred pursuant to a warrant described in section 4(a)(2).",
      "versionDate": "2025-01-22",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:12:44Z"
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
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s188is.xml"
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
      "title": "Free Speech Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Free Speech Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit Federal employees and contractors from directing online platforms to censor any speech that is protected by the First Amendment to the Constitution of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:27Z"
    }
  ]
}
```
