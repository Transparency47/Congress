# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8652
- Title: YODA
- Congress: 119
- Bill type: HR
- Bill number: 8652
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-18T18:52:37Z
- Update date including text: 2026-05-18T18:52:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8652",
    "number": "8652",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "YODA",
    "type": "HR",
    "updateDate": "2026-05-18T18:52:37Z",
    "updateDateIncludingText": "2026-05-18T18:52:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:32:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8652ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8652\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Cloud introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo affirm user ownership of their data, prohibit entities from requiring the transfer or monetization of private data in exchange for services, prohibit the collection of third-party contact information without written consent, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the You Own the Data Act or YODA .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nGovernments exist to protect individual rights to life, liberty, and property.\n**(2)**\nThe protection of civil liberties, including the rights to private property and privacy from unwarranted searches and seizures, is one of the hallmarks of a free society.\n**(3)**\nIt is appropriate for Congress to enact laws to protect individuals from data collection by third parties.\n**(4)**\nData is the property of the user, as the user creates the data.\n**(5)**\nA user maintains ownership of the data of such user, even when such data is sold or leased with the consent of such user.\n**(6)**\nTechnology should empower the individual and the productivity of the individual.\n**(7)**\nIndividuals should have reasonable access to and use of popularly available consumer technologies without abdicating the rights of such individuals to privacy and anonymity.\n#### 3. Prohibition on sharing user contacts without written consent and clarifying user access to data\n##### (a) Prohibition on access to user contacts\nIt shall be unlawful for a covered entity to ask a user to share the contacts or information about the contacts of the user unless the user and the contacts of the user consent to such use in writing.\n##### (b) Access to, and correction, deletion, and portability of, covered data\n**(1) In general**\nSubject to paragraphs (2) and (3), a covered entity shall provide a user, immediately or as quickly as possible and in no case later than 90 days after receiving a verified request from the user, with the ability to reasonably\u2014\n**(A)**\naccess\u2014\n**(i)**\nif applicable, a list of each third party and service provider to whom the covered entity has transferred or shared the covered data of the user;\n**(ii)**\nthe covered data of the user, or an accurate representation of the covered data of the user, including data aggregation that is a readable summary, that is held or has been processed by the covered entity or any service provider of the covered entity; and\n**(iii)**\nif a covered entity transfers covered data, a description of the covered data that was transferred and the purpose for which the third party requested the data;\n**(B)**\nrequest that the covered entity\u2014\n**(i)**\ncorrect material inaccuracies or materially incomplete information with respect to the covered data of the user that is maintained by the covered entity;\n**(ii)**\ndelete or de-identify covered data of the user that is or has been maintained by the covered entity;\n**(iii)**\nnotify any service provider or third party to which the covered entity transferred such covered data of the corrected information; and\n**(iv)**\nprovide contact information to the user of any service provider or third party that the covered data of the user was transferred to so that the user may make requests described in this subparagraph; and\n**(C)**\nto the extent that is technically feasible, provide covered data of the user that is or has been generated and submitted to the covered entity by the user and maintained by the covered entity in a portable, structured, and machine-readable format that is not subject to licensing restrictions.\n**(2) Frequency and cost of access**\nA covered entity shall\u2014\n**(A)**\nprovide a user with the opportunity to exercise the rights described in paragraph (1) not less than twice in any 12-month period; and\n**(B)**\nfulfill the responsibilities described in paragraph (1) free of charge.\n**(3) Prohibition on retaliation**\nA covered entity shall provide the same quality of goods or services, at the same price or rate, regardless of whether a user took an action described under paragraph (1).\n**(4) Retention of data**\nA covered entity that collects data on a user\u2019s browsing history or biometric data and information shall delete the data within 60 days after the date on which the data was collected.\n##### (c) Data minimization and contextuality\n**(1) Collection and use of information**\nA commercial data operator shall limit the collection and sharing of information by the operator with third parties to what is reasonably necessary to provide a service or conduct an activity that a consumer has requested or is reasonably necessary for fraud prevention.\n**(2) Retention of information**\nA commercial data operator that collects the personal information of a consumer shall limit the use and retention of that information to what is reasonably necessary to provide a service or conduct an activity that a consumer has requested or a related operational purpose. Any data collected or retained by a commercial data operator solely for security or fraud prevention may not be used for operational purposes.\n**(3) Monetization**\nMonetization of personal information shall not be considered reasonably necessary to provide a service or conduct an activity that a consumer has requested or reasonably necessary for security or fraud prevention.\n##### (d) Consumer choice and control\n**(1) Commercial data operator**\nA commercial data operator shall provide a prominently and conspicuously displayed icon a user may click to opt out of data collection on every unique website, mobile application, or computer application.\n**(2) Covered entities**\nWithin 2 years after the date of the enactment of this Act, a covered entity shall take reasonable steps, taking account of available technology, to provide users the ability to directly delete the covered data collected by the covered entity.\n##### (e) Default settings\nA covered entity may require, through terms of service or otherwise, that a user must consent to the transfer of covered data in order to use the service of the covered entity.\n##### (f) Policies regarding data from minors\nA covered entity may not collect, retain, or transfer the covered data of a user to a third party without affirmative consent from the parent or guardian of the user if the user is below the age of 18 years old, where technically feasible.\n##### (g) Prohibition on tracking cookies without user consent\nA commercial data operator\u2014\n**(1)**\nunless authorized by the user, may not track cookies, including on mobile applications; and\n**(2)**\nshall provide the same services to users who do not authorize tracking cookies.\n##### (h) Transparency\n**(1) Privacy notice**\nA covered entity shall provide users with a clear, comprehensible, accurate, and continuously available privacy notice that\u2014\n**(A)**\ndescribes in detail the information collected by the operator, how that information would be used, and whether the information would be sold or shared with any third party; and\n**(B)**\nis 1,000 words or less.\n**(2) Report on use of information required**\nIf a user allows a commercial data operator to sell the covered data of the user, the commercial data operator shall provide the user with an annual report regarding the types of third parties with whom data has been shared. The report shall include a description of what information has been shared, for what purpose information is shared, and a list of each third party that receives data.\n##### (i) Data security and breach notification\nA covered entity shall notify each user in a timely manner of any data breach with respect to the information of the user and provide any remedy to compensate the user for the breach of their information, including a credit protection service, fraud alert, and credit monitoring through credit reporting agencies.\n##### (j) Enforcement\n**(1) Enforcement by the Federal Trade Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(B) Powers of Commission**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(2) Effect on other laws**\nNothing in this section shall be construed in any way to limit the authority of the Commission under any other provision of law or to limit the application of any Federal or State law.\n**(3) Enforcement by State attorneys general**\n**(A) In general**\nIf the chief law enforcement officer of a State, or an official or agency designated by a State, has reason to believe that any person has violated or is violating this section, the attorney general, official, or agency of the State, in addition to any authority it may have to bring an action in State court under its consumer protection law, may bring a civil action in any appropriate United States district court or in any other court of competent jurisdiction, including a State court, to\u2014\n**(i)**\nenjoin further such violation by such person;\n**(ii)**\nenforce compliance with this section;\n**(iii)**\nobtain civil penalties; and\n**(iv)**\nobtain damages, restitution, or other compensation on behalf of residents of the State.\n**(B) Notice and intervention by the Federal Trade Commission**\nThe attorney general of a State shall provide prior written notice of any action under subparagraph (A) to the Commission and provide the Commission with a copy of the complaint in the action, except in any case in which such prior notice is not feasible, in which case the attorney general shall serve such notice immediately upon instituting such action. The Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(C) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for violation of this section, no State attorney general, or official or agency of a State, may bring an action under this paragraph during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this section alleged in the complaint.\n**(4) Private right of action**\n**(A) In general**\nAny individual alleging a violation of this section or a regulation promulgated under this section may bring a civil action in any Federal or State court of competent jurisdiction against a covered entity that has global annual gross revenues of at least $50,000,000.\n**(B) Relief**\nIn a civil action brought under subparagraph (A) in which the plaintiff prevails, the court may award\u2014\n**(i)**\n$100 to $750 per violation;\n**(ii)**\nreasonable attorney\u2019s fees and litigation costs; and\n**(iii)**\nany other relief, including equitable or declaratory relief, that the court determines appropriate.\n##### (k) Definitions\nIn this section:\n**(1) Commercial data operator**\nThe term commercial data operator means an entity acting in its capacity as a consumer online services provider or data broker that\u2014\n**(A)**\ngenerates a material amount of revenue from the use, collection, processing, sale, or sharing of data generated by a user; and\n**(B)**\nhas more than 100,000,000 unique monthly visitors or users in the United States for a majority of months during the previous 1-year period.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Consent**\nThe term consent means an affirmative act by an individual that clearly communicates the informed authorization of the individual for an act or practice.\n**(4) Core function**\nThe term core function does not mean targeted advertising or marketing.\n**(5) Covered data**\nThe term covered data means individually, identifiable information about a user collected online, including any of the following:\n**(A)**\nLocation information that would identify the physical address of an individual.\n**(B)**\nTelephone number.\n**(C)**\nEmail address.\n**(D)**\nSocial security number or other unique, government-issued identifiers.\n**(E)**\nNonpublic personal information (as defined in section 509 of the Gramm-Leach-Bliley Act ( 15 U.S.C. 6809 )).\n**(F)**\nContent of a personal wire communication, oral communication, or electronic communication such as email or direct messaging with respect to any entity that is not the intended recipient of the communication.\n**(G)**\nCall detail records.\n**(H)**\nWeb browsing history, application usage history, and the functional equivalent of either that is not aggregated data.\n**(I)**\nBiometric data and information, such as facial and voice recognition data.\n**(6) Covered entity**\nThe term covered entity means a commercial data broker or large online operator that collects covered data from a user through an online platform.\n**(7) Data broker**\nThe term data broker means a covered entity whose principal source of revenue is derived from processing or transferring the covered data of individuals with whom the entity does not have a direct relationship on behalf of a third party for use by the third party.\n**(8) De-identify**\nThe term de-identify means to separate information from the user or IP address the information is associated with.\n**(9) Delete**\nThe term delete means to remove or destroy information so that the information is not maintained in human or machine-readable form and cannot be retrieved or used in such form in the normal course of business.\n**(10) Large online operator**\nThe term large online operator means any person that\u2014\n**(A)**\nprovides an online service; and\n**(B)**\nhas more than 100,000,000 authenticated users of an online service in any 30-day period.\n**(11) Monetization**\nThe term monetization means the process of collecting, using, and storing data solely for economic benefit.\n**(12) User**\nThe term user means an individual residing in the United States who uses a website that collects data and information from the user.",
      "versionDate": "2026-05-04",
      "versionType": "Introduced in House"
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
        "name": "Commerce",
        "updateDate": "2026-05-18T18:52:37Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8652ih.xml"
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
      "title": "YODA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "YODA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "You Own the Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To affirm user ownership of their data, prohibit entities from requiring the transfer or monetization of private data in exchange for services, prohibit the collection of third-party contact information without written consent, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:18:35Z"
    }
  ]
}
```
