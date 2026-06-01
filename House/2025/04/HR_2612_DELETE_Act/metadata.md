# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2612?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2612
- Title: DELETE Act
- Congress: 119
- Bill type: HR
- Bill number: 2612
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-01-21T05:06:17Z
- Update date including text: 2026-01-21T05:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2612",
    "number": "2612",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000482",
        "district": "3",
        "firstName": "Lori",
        "fullName": "Rep. Trahan, Lori [D-MA-3]",
        "lastName": "Trahan",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "DELETE Act",
    "type": "HR",
    "updateDate": "2026-01-21T05:06:17Z",
    "updateDateIncludingText": "2026-01-21T05:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:03:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2612ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2612\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mrs. Trahan introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a centralized system to allow individuals to request the simultaneous deletion of their personal information across all data brokers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Data Elimination and Limiting Extensive Tracking and Exchange Act or the DELETE Act .\n#### 2. Data deletion requirements\n##### (a) Data broker annual registration\n**(1) In general**\n**(A) Regulations**\nNot later than 1 year after the date of enactment of this section, the Commission shall promulgate regulations to require any data broker to\u2014\n**(i)**\nnot later than 18 months after the date of enactment of this section, and annually thereafter, register with the Commission; and\n**(ii)**\nsubject to subparagraph (B), provide with such registration certain information, including\u2014\n**(I)**\nthe name and primary physical, email, and uniform resource locator (URL) addresses of the data broker;\n**(II)**\nif the data broker permits an individual to opt out of the data broker\u2019s collection or use of personal information, certain sales of such information, or its databases\u2014\n**(aa)**\nthe method for requesting an opt-out;\n**(bb)**\nany limitations on the type of data collection, uses, or sales for which an individual may opt-out; and\n**(cc)**\nwhether the data broker permits an individual to authorize a third party to perform the opt-out on the individual\u2019s behalf;\n**(III)**\na response to a standardized form (as issued by the Commission) specifying the types of information the data broker collects or obtains and the sources from which the data broker obtains data;\n**(IV)**\na statement as to whether the data broker implements a credentialing process and, if so, a description of that process;\n**(V)**\nany additional information or explanation the data broker chooses to provide concerning its data collection practices; and\n**(VI)**\nany other information determined appropriate by the Commission.\n**(B) Construction**\nNothing in this paragraph shall be construed as requiring a data broker to disclose any information that is a trade secret or other kind of confidential information described in section 552(b)(4) of title 5, United States Code.\n**(2) Public availability**\n**(A) In general**\nThe Commission shall make the information provided pursuant to paragraph (1)(A)(ii) publicly available in a downloadable and machine-readable format, except in the event that the Commission\u2014\n**(i)**\ndetermines that the risk of making such information available is not in the interest of public safety or welfare; and\n**(ii)**\nprovides a justification for such determination.\n**(B) Disclaimer**\nThe Commission shall include on the website of the Commission a disclaimer that\u2014\n**(i)**\nthe Commission cannot confirm the accuracy of the information provided pursuant to paragraph (1)(A)(ii); and\n**(ii)**\nindividuals may contact a data broker who provided such information at their own risk.\n##### (b) Centralized data deletion system\n**(1) Establishment**\n**(A) In general**\nNot later than 1 year after the date of enactment of this section, the Commission shall promulgate regulations to establish a centralized system that\u2014\n**(i)**\nimplements and maintains reasonable security procedures and practices (including administrative, physical, and technical safeguards) appropriate to the nature of the information and the purposes for which the personal information will be used, to protect individuals\u2019 personal information from unauthorized use, disclosure, access, destruction, or modification;\n**(ii)**\nallows an individual, through a single submission, to request that every data broker who is registered under subsection (a) and who maintains any persistent identifiers (as described in subparagraph (B)(iii))\u2014\n**(I)**\ndelete any personal information related to such individual held by such data broker or affiliated legal entity of the data broker; and\n**(II)**\nunless otherwise specified by the individual, discontinue any present or future collection of personal information related to such individual; and\n**(iii)**\nallows a registered data broker, prior to the collection of any personal information that is tied to a persistent identifier for which a registry exists, to submit a query to the centralized system to confirm that the persistent identifier is not subject to a deletion request described in clause (ii).\n**(B) Requirements**\nThe centralized system established in subparagraph (A) shall meet the following requirements:\n**(i)**\nThe centralized system shall allow an individual to request the deletion of all personal information related to such individual and the discontinuation of any collection of such personal information related to such individual through a single deletion request.\n**(ii)**\nThe centralized system shall provide a standardized form to allow an individual to make such request.\n**(iii)**\nSuch standardized form shall include the individual's email, phone number, physical address, and any other persistent identifier determined by the Commission to aid in the deletion request.\n**(iv)**\nThe centralized system shall automatically salt and hash all submitted information and allow the Commission to maintain independent hashed registries of each type of information obtained through such form.\n**(v)**\nThe centralized system shall only permit data brokers who are registered with the Commission to submit hashed queries to the independent hashed registries described in clause (iv).\n**(vi)**\nWith respect to the independent hashed registries described in clause (iv), the salt shall be different for each such registry and shall be made available to all registered data brokers for the purposes of submitting hashed queries, as described in clause (v).\n**(vii)**\nThe centralized system shall allow an individual to make such request using an internet website operated by the Commission.\n**(viii)**\nThe centralized system shall not charge the individual to make such request.\n**(C) Transition**\n**(i) In general**\nNot later than 8 months after the effective date of the regulations promulgated under subparagraph (A), each data broker shall\u2014\n**(I)**\nnot less than once every 31 days, access the hashed registries maintained by the Commission as described in subparagraph (B)(iv); and\n**(II)**\nprocess any deletion request associated with a match between such hashed registries and the records of the data broker.\n**(ii) FTC guidance**\nNot later than 6 months after the effective date of the regulations promulgated under subparagraph (A), the Commission shall publish guidance on the process and standards to which a data broker must adhere in carrying out clause (i).\n**(2) Deletion**\n**(A) Information deletion**\n**(i) In general**\nSubject to clause (ii), not later than 31 days after accessing the hashed registries described in paragraph (1)(B)(iv), a data broker and any associated legal entity shall delete all personal information in its possession related to the individual making the request and discontinue the collection of personal information related to such individual. Immediately following the deletion, the data broker shall send an affirmative representation to the Commission with the number of records deleted pursuant to each match with a value in the hashed registries.\n**(ii) Exclusions**\nIn carrying out clause (i), a data broker may retain, where required, the following information:\n**(I)**\nAny personal information that is processed or maintained solely as part of human subjects research conducted in compliance with any legal requirements for the protection of human subjects.\n**(II)**\nAny personal information necessary to comply with a warrant, subpoena, court order, rule, or other applicable law.\n**(III)**\nAny information necessary for an activity described in subsection (f)(3)(B), provided that the retained information is used solely for any such activity.\n**(iii) Use of information**\nAny personal information excluded under clause (ii) may only be used for the purpose described in the applicable subclause of clause (ii), and may not be used for any other purpose, including marketing purposes.\n**(B) Annual report**\nEach data broker registered under subsection (a) shall submit to the Commission, on an annual basis, a report on the completion rate with respect to the completion of deletion requests under subparagraph (A).\n**(C) Audit**\n**(i) In general**\nNot later than 3 years after the date of enactment of this section, and every 3 years thereafter, each data broker registered under subsection (a) shall undergo an independent third party audit to determine compliance with this subsection.\n**(ii) Audit report**\nNot later than 6 months after the completion of any audit under clause (i), each such data broker shall submit to the Commission any report produced as a result of the audit, along with any related materials.\n**(iii) Maintain records**\nEach such data broker shall maintain the materials described in clause (ii) for a period of not less than 6 years.\n**(3) Annual fee**\n**(A) In general**\nSubject to subparagraph (B), each data broker registered under subsection (a) and who maintains any persistent identifiers (as described in paragraph (1)(B)(iii)) shall pay to the Commission, on an annual basis, a subscription fee determined by the Commission to access the database.\n**(B) Limit**\nThe amount of the subscription fee under subparagraph (A) may not exceed 1 percent of the expected annual cost of operating the centralized system and hashed registries described in paragraph (1), as determined by the Commission.\n**(C) Availability**\nAny amounts collected by the Commission pursuant to this paragraph shall be available without further appropriation to the Commission for the exclusive purpose of enforcing and administering this section, including the implementation and maintenance of such centralized system and hashed registries and the promotion of public awareness of the centralized system.\n##### (c) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) or (b) or a regulation promulgated under this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates subsection (a) or (b) or a regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Rulemaking**\nThe Commission shall promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this section.\n##### (d) Study and report\n**(1) Study**\nThe Commission shall conduct a study on the implementation and enforcement of this section. Such study shall include\u2014\n**(A)**\nan analysis of the effectiveness of the centralized system established in subsection (b)(1)(A);\n**(B)**\nthe number deletion requests submitted annually using such centralized system;\n**(C)**\nan analysis of the progress of coordinating the operation and enforcement of such requests with similar systems established and maintained by the various States; and\n**(D)**\nany other area determined appropriate by the Commission.\n**(2) Report**\nNot later than 3 years after the date of enactment of this section, and annually thereafter for each of the next 4 years, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report containing\u2014\n**(A)**\nthe results of the study conducted pursuant to paragraph (1);\n**(B)**\na summary of any enforcement actions taken pursuant to this Act; and\n**(C)**\nrecommendations for any legislation and administrative action as the Commission determines appropriate.\n##### (e) Preemption\n**(1) In general**\nThe provisions of this Act shall preempt any State privacy law only to the extent that such State law is inconsistent with the provisions of this Act.\n**(2) Greater protection under State law**\nFor purposes of paragraph (1), a State privacy law is not inconsistent with the provisions of this Act if the protection such law affords any person is greater than the protection provided under this Act, as determined by the Commission.\n##### (f) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Credentialing process**\nThe term credentialing process means the practice of taking reasonable steps to confirm\u2014\n**(A)**\nthe identity of the entity with whom the data broker has a direct relationship;\n**(B)**\nthat any data disclosed to the entity by such data broker will be used for the described purpose of such disclosure; and\n**(C)**\nthat such data will not be used for unlawful purposes.\n**(3) Data broker**\n**(A) In general**\nThe term data broker means an entity that knowingly collects or obtains the personal information of an individual with whom the entity does not have a direct relationship and then\u2014\n**(i)**\nuses the personal information to perform a service for a third party; or\n**(ii)**\nsells, licenses, trades, provides for consideration, or is otherwise compensated for disclosing personal information to a third party.\n**(B) Exclusion**\nThe term data broker does not include an entity who solely uses, sells, licenses, trades, provides for consideration, or is otherwise compensated for disclosing personal information for 1 or more of the following activities:\n**(i)**\nProviding 411 directory assistance or directory information services, including name, address, and telephone number, on behalf of or as a function of a telecommunications carrier.\n**(ii)**\nProviding an individual's publicly available information if the information is being used by the recipient as it relates to that individual's business or profession.\n**(iii)**\nProviding personal information to a third party at the express direction of the individual for a clearly disclosed single-use purpose.\n**(iv)**\nProviding or using personal information for assessing, verifying, or authenticating an individual's identity, or for investigating or preventing actual or potential fraud.\n**(v)**\nGathering, preparing, collecting, photographing, recording, writing, editing, reporting, or publishing news or information that concerns local, national, or international events or other matters of public interest (as determined by the Commission) for dissemination to the public.\n**(vi)**\nActing as a consumer reporting agency (as defined in section 603(f) of the Fair Credit Reporting Act ( 15 U.S.C. 1681a(f) )).\n**(C) Exclusion from sale**\n**(i) In general**\nFor purposes of this paragraph, the term sells does not include a one-time or occasional sale of assets of an entity as part of a transfer of control of those assets that is not part of the ordinary conduct of the entity.\n**(ii) Notice required**\nTo meet the exclusion criteria described in clause (i), an entity must provide notice to the Commission, in the manner determined appropriate by the Commission, of any such one-time or occasional sale of assets.\n**(4) Delete**\nThe term delete means to remove or destroy information such that the information is not maintained in human- or machine-readable form and cannot be retrieved or utilized in such form in the normal course of business.\n**(5) Direct relationship**\n**(A) In general**\nThe term direct relationship means a relationship between an individual and an entity where the individual\u2014\n**(i)**\nis a current customer;\n**(ii)**\nhas obtained a good or service from the entity within the prior 18 months; or\n**(iii)**\nhas made an inquiry about the products or services of the entity within the prior 90 days.\n**(B) Exclusion**\nThe term direct relationship does not include a relationship\u2014\n**(i)**\nbetween an individual and a data broker where the individual's only connection to the data broker is based on the individual's request\u2014\n**(I)**\nfor the data broker to delete the personal information of the individual; or\n**(II)**\nto opt-out of the data broker\u2019s collection or use of personal information, certain sales of such information, or its databases; or\n**(ii)**\nrequired under any State or Federal law related to the use of personal information.\n**(6) Hash**\nThe term hash means to input data to a cryptographic, one-way, collision resistant function that maps a bit string of arbitrary length to a fixed-length bit string to produce a cryptographically secure value.\n**(7) Hashed**\nThe term hashed means the type of value produced by hashing data.\n**(8) Human subjects research**\nThe term human subjects research means research that\u2014\n**(A)**\nan investigator (whether professional or student) conducts on a living individual; and\n**(B)**\neither\u2014\n**(i)**\nobtains information or biospecimens through intervention or interaction with the individual, and uses, studies, or analyzes the information or biospecimens; or\n**(ii)**\nobtains, uses, studies, analyzes, or generates personal information or identifiable biospecimens.\n**(9) Personal information**\n**(A) In general**\nThe term personal information means any information held by a data broker, regardless of how the information is collected, inferred, created, or obtained, that is linked or reasonably linkable by the data broker to a particular individual or consumer device, including the following:\n**(i)**\nFinancial information, including any bank account number, credit card number, debit card number, or insurance policy number.\n**(ii)**\nA name, alias, home or other physical address, online identifier, Internet Protocol address, email address, phone number, account name, State identification card number, driver's license number, passport number, or an identifying number on a government-issued identification.\n**(iii)**\nGeolocation information.\n**(iv)**\nBiometric information.\n**(v)**\nThe contents of, attachments to, or parties to information, including with respect to email, text messages, picture messages, voicemails, audio conversations, or video conversations.\n**(vi)**\nWeb browsing history, including any search query.\n**(vii)**\nGenetic sequencing information.\n**(viii)**\nA device identifier, online identifier, persistent identifier, or digital fingerprinting information.\n**(ix)**\nAny inference drawn from any of the information described in this paragraph that is used to create a profile about an individual that reflects such individual's preferences, characteristics, psychological trends, predispositions, behavior, attitudes, intelligence, abilities, or aptitudes.\n**(x)**\nAny other information determined appropriate by the Commission.\n**(B) Linked or reasonably linkable**\nFor purposes of subparagraph (A), information is linked or reasonably linkable to a particular individual or consumer device if the information can be used on its own or in combination with other information held by or readily accessible to a data broker to identify a particular individual or consumer device.\n**(10) Process**\nThe term process means to perform or direct the performance of an operation on personal information, including the collection, transmission, use, disclosure, analysis, prediction, or modification of such personal information, whether or not by automated means.\n**(11) Salt**\nThe term salt means to add a random string of data to the input of a hash function.\n**(12) Uniform resource locator; URL**\nThe term uniform resource locator or URL means a short string containing an address that refers to an object on the web.",
      "versionDate": "2025-04-02",
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
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1287",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DELETE Act",
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
        "name": "Commerce",
        "updateDate": "2025-05-14T14:38:26Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2612ih.xml"
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
      "title": "DELETE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DELETE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Elimination and Limiting Extensive Tracking and Exchange Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a centralized system to allow individuals to request the simultaneous deletion of their personal information across all data brokers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:19Z"
    }
  ]
}
```
