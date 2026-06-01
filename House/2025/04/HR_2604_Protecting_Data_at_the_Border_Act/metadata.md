# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2604?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2604
- Title: Protecting Data at the Border Act
- Congress: 119
- Bill type: HR
- Bill number: 2604
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-01-22T17:38:41Z
- Update date including text: 2026-01-22T17:38:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2604",
    "number": "2604",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Protecting Data at the Border Act",
    "type": "HR",
    "updateDate": "2026-01-22T17:38:41Z",
    "updateDateIncludingText": "2026-01-22T17:38:41Z"
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
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
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
          "date": "2025-04-02T22:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-02T21:01:12Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-02T22:02:30Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "DC"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2604ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2604\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Lieu (for himself, Mr. Beyer , Ms. Norton , and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure the digital contents of electronic equipment and online accounts belonging to or in the possession of United States persons entering or exiting the United States are adequately protected at the border, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Data at the Border Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUnited States persons have a reasonable expectation of privacy in the digital contents of their electronic equipment, the digital contents of their online accounts, and the nature of their online presence.\n**(2)**\nThe Supreme Court of the United States recognized in Riley v. California, 134 S. Ct. 2473 (2014), the extraordinary privacy interests in electronic equipment like cell phones.\n**(3)**\nThe privacy interest of United States persons in the digital contents of their electronic equipment, the digital contents of their online accounts, and the nature of their online presence differs in both degree and kind from their privacy interest in closed containers.\n**(4)**\nAccessing the digital contents of electronic equipment, accessing the digital contents of an online account, or obtaining information regarding the nature of the online presence of a United States person entering or exiting the United States, without a lawful warrant based on probable cause, is unreasonable under the Fourth Amendment to the Constitution of the United States.\n#### 3. Definitions\nAs used in this Act\u2014\n**(1)**\nthe term access credential includes a username, password, PIN number, fingerprint, or biometric indicator;\n**(2)**\nthe term border means the international border of the United States and the functional equivalent of such border;\n**(3)**\nthe term digital contents means any signs, signals, writing, images, sounds, data, or intelligence of any nature transmitted in whole or in part by electronic equipment, or stored in electronic equipment or an online account;\n**(4)**\nthe term electronic communication service has the meaning given that term in section 2510 of title 18, United States Code;\n**(5)**\nthe term electronic equipment has the meaning given the term computer in section 1030(e) of title 18, United States Code;\n**(6)**\nthe term Governmental entity means a department or agency of the United States (including any officer, employee, or contractor or other agent thereof);\n**(7)**\nthe term online account means an online account with an electronic communication service or remote computing service;\n**(8)**\nthe term online account information means the screen name or other identifier or information that would allow a Governmental entity to identify the online presence of an individual;\n**(9)**\nthe term remote computing service has the meaning given that term in section 2711 of title 18, United States Code; and\n**(10)**\nthe term United States person means an individual who is a United States person, as defined in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ).\n#### 4. Procedures for lawful access to digital data at the border\n##### (a) Standard\nSubject to subsection (b), a Governmental entity may not\u2014\n**(1)**\naccess the digital contents of any electronic equipment belonging to or in the possession of a United States person at the border without a valid warrant supported by probable cause issued using the procedures described in the Federal Rules of Criminal Procedure by a court of competent jurisdiction;\n**(2)**\ndeny entry into or exit from the United States by a United States person based on a refusal by the United States person to\u2014\n**(A)**\ndisclose an access credential that would enable access to the digital contents of electronic equipment or the digital contents of an online account;\n**(B)**\nprovide access to the digital contents of electronic equipment or the digital contents of an online account; or\n**(C)**\nprovide online account information; or\n**(3)**\ndelay entry into or exit from the United States by a United States person for longer than the period of time, which may not exceed 4 hours, necessary to determine whether the United States person will, in a manner in accordance with subsection (c), consensually provide an access credential, access, or online account information, as described in subparagraphs (A), (B), and (C) of paragraph (2).\n##### (b) Emergency exceptions\n**(1) Emergency situations generally**\n**(A) In general**\nAn investigative or law enforcement officer of a Governmental entity who is designated by the Secretary of Homeland Security for purposes of this paragraph may access the digital contents of electronic equipment belonging to or in possession of a United States person at the border without a warrant described in subsection (a)(1) if the investigative or law enforcement officer\u2014\n**(i)**\nreasonably determines that\u2014\n**(I)**\nan emergency situation exists that involves\u2014\n**(aa)**\nimmediate danger of death or serious physical injury to any person;\n**(bb)**\nconspiratorial activities threatening the national security interest of the United States; or\n**(cc)**\nconspiratorial activities characteristic of organized crime;\n**(II)**\nthe emergency situation described in subclause (I) requires access to the digital contents of the electronic equipment before a warrant described in subsection (a)(1) authorizing such access can, with due diligence, be obtained; and\n**(III)**\nthere are grounds upon which a warrant described in subsection (a)(1) could be issued authorizing such access; and\n**(ii)**\nmakes an application in accordance with this section for a warrant described in subsection (a)(1) as soon as practicable, but not later than 7 days after the investigative or law enforcement officer accesses the digital contents under the authority under this subparagraph.\n**(B) Warrant not obtained**\nIf an application for a warrant described in subparagraph (A)(ii) is denied, or in any other case in which an investigative or law enforcement officer accesses the digital contents of electronic equipment belonging to or in possession of a United States person at the border without a warrant under the emergency authority under subparagraph (A) and a warrant authorizing the access is not obtained\u2014\n**(i)**\nany copy of the digital contents in the custody or control of a Governmental entity shall immediately be destroyed;\n**(ii)**\nthe digital contents, and any information derived from the digital contents, may not be disclosed to any Governmental entity or a State or local government; and\n**(iii)**\nthe Governmental entity employing the investigative or law enforcement officer that accessed the digital contents shall notify the United States person that any copy of the digital contents has been destroyed.\n**(2) Protection of public safety and health**\nA Governmental entity may access the digital contents of electronic equipment belonging to or in possession of a United States person at the border without a warrant described in subsection (a)(1) if the access is\u2014\n**(A)**\nnecessary for the provision of fire, medical, public safety, or other emergency services; and\n**(B)**\nunrelated to the investigation of a possible crime or other violation of the law.\n##### (c) Informed consent in writing\n**(1) Notice**\n**(A) In general**\nA Governmental entity shall provide the notice described in subparagraph (B) before requesting that a United States person at the border\u2014\n**(i)**\nprovide consent to access the digital contents of any electronic equipment belonging to or in the possession of or the digital contents of an online account of the United States person;\n**(ii)**\ndisclose an access credential that would enable access to the digital contents of electronic equipment or the digital contents of an online account of the United States person;\n**(iii)**\nprovide access to the digital contents of electronic equipment or the digital contents of an online account of the United States person; or\n**(iv)**\nprovide online account information of the United States person.\n**(B) Contents**\nThe notice described in this subparagraph is written notice in a language understood by the United States person that the Governmental entity\u2014\n**(i)**\nmay not\u2014\n**(I)**\ncompel access to the digital contents of electronic equipment belonging to or in the possession of, the digital contents of an online account of, or the online account information of a United States person without a valid warrant;\n**(II)**\ndeny entry into or exit from the United States by the United States person based on a refusal by the United States person to\u2014\n**(aa)**\ndisclose an access credential that would enable access to the digital contents of electronic equipment or the digital contents of an online account;\n**(bb)**\nprovide access to the digital contents of electronic equipment or the digital contents of an online account; or\n**(cc)**\nprovide online account information; or\n**(III)**\ndelay entry into or exit from the United States by the United States person for longer than the period of time, which may not exceed 4 hours, necessary to determine whether the United States person will consensually provide an access credential, access, or online account information, as described in items (aa), (bb), and (cc) of subclause (II); and\n**(ii)**\nif the Governmental entity has probable cause that the electronic equipment contains information that is relevant to an allegation that the United States person has committed a felony, may seize electronic equipment belonging to or in the possession of the United States person for a period of time if the United States person refuses to consensually provide access to the digital contents of the electronic equipment.\n**(2) Consent**\n**(A) In general**\nA Governmental entity shall obtain written consent described in subparagraph (B) before\u2014\n**(i)**\naccessing, pursuant to the consent of a United States person at the border the digital contents of electronic equipment belonging to or in the possession of or the digital contents of an online account of the United States person;\n**(ii)**\nobtaining, pursuant to the consent of a United States person at the border, an access credential of the United States person that would enable access to the digital contents of electronic equipment or the digital contents of an online account; or\n**(iii)**\nobtaining, pursuant to the consent of a United States person at the border, online account information for an online account of the United States person.\n**(B) Contents of written consent**\nWritten consent described in this subparagraph is written consent that\u2014\n**(i)**\nindicates the United States person understands the protections and limitations described in paragraph (1)(B);\n**(ii)**\nstates the United States person is\u2014\n**(I)**\nproviding consent to the Governmental entity to access certain digital contents or consensually disclosing an access credential; or\n**(II)**\nconsensually providing online account information; and\n**(iii)**\nspecifies the digital contents, access credential, or online account information with respect to which the United States person is providing consent.\n##### (d) Retention of digital contents\n**(1) Lawful access**\nA Governmental entity that obtains access to the digital contents of electronic equipment, the digital contents of an online account, or online account information in accordance with this section may not make or retain a copy of the digital contents or online account information, or any information directly or indirectly derived from the digital contents or online account information, unless there is probable cause to believe the digital contents or online account information contains evidence of, or constitutes the fruits of, a crime.\n**(2) Unlawful access**\nIf a Governmental entity obtains access to the digital contents of electronic equipment, digital contents of an online account, or online account information in a manner that is not in accordance with this section, the Governmental entity\u2014\n**(A)**\nshall immediately destroy any copy of the digital contents or online account information, and any information directly or indirectly derived from the digital contents or online account information, in the custody or control of the Governmental entity;\n**(B)**\nmay not disclose the digital contents or online account information, or any information directly or indirectly derived from the digital contents or online account information, to any other Governmental entity or a State or local government; and\n**(C)**\nshall notify the United States person that any copy of the digital contents or online account information, and any information directly or indirectly derived from the digital contents or online account information, has been destroyed.\n##### (e) Recordkeeping\nA Governmental entity shall keep a record of each instance in which the Governmental entity obtains access to the digital contents of electronic equipment belonging to or in the possession of an individual at the border, the digital contents of an online account of an individual who is at the border, or online account information of an individual who is at the border, which shall include\u2014\n**(1)**\nthe reason for the access;\n**(2)**\nthe nationality, immigration status, and admission category of the individual;\n**(3)**\nthe nature and extent of the access;\n**(4)**\nif the access was consensual, how and to what the individual consented, and what the individual provided by consent;\n**(5)**\nwhether electronic equipment of the individual was seized;\n**(6)**\nwhether the Governmental entity made a copy of all or a portion of the digital contents or online account information, or any information directly or indirectly derived from the digital contents or online account information; and\n**(7)**\nwhether the digital contents or online account information, or any information directly or indirectly derived from the digital contents or online account information, was shared with another Governmental entity or a State or local government.\n#### 5. Limits on use of digital contents as evidence\n##### (a) In general\nWhenever any digital contents or online account information have been obtained in violation of this Act, no part of the digital contents or online account information and no evidence derived therefrom may be received in evidence in any trial, hearing, or other proceeding (including any proceeding relating to the immigration laws, as defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )) in or before any court, grand jury, department, officer, agency, regulatory body, legislative committee, or other authority of the United States, a State, or a political subdivision thereof.\n##### (b) Application\nTo the maximum extent practicable, the limitations under subsection (a) shall be applied in the same manner as the limitations under section 2515 of title 18, United States Code.\n#### 6. Limits on seizure of electronic equipment\nA Governmental entity may not seize any electronic equipment belonging to or in the possession of a United States person at the border unless there is probable cause to believe that the electronic equipment contains information that is relevant to an allegation that the United States person has committed a felony.\n#### 7. Audit and reporting requirements\nIn March of each year, the Secretary of Homeland Security shall submit to Congress and make publicly available on the website of the Department of Homeland Security a report that includes the following:\n**(1)**\nThe number of times during the previous year that an officer or employee of the Department of Homeland Security did each of the following:\n**(A)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of or the digital contents of an online account of a United States person at the border pursuant to a warrant supported by probable cause issued using the procedures described in the Federal Rules of Criminal Procedure by a court of competent jurisdiction.\n**(B)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of a United States person at the border pursuant to the emergency authority under section 5(b).\n**(C)**\nRequested consent to access the digital contents of any electronic equipment belonging to or in the possession of, the digital contents of an online account of, or online account information of a United States person at the border.\n**(D)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of, the digital contents of an online account of, or online account information of a United States person at the border pursuant to written consent provided in accordance with section 5(c).\n**(E)**\nRequested a United States person at the border consensually disclose an access credential that would enable access to the digital contents of electronic equipment or the digital contents of an online account of the United States person.\n**(F)**\nAccessed the digital contents of electronic equipment or the digital contents of an online account of a United States person at the border using an access credential pursuant to written consent provided in accordance with section 5(c).\n**(G)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of, the digital contents of an online account of, or online account information of a United States person at the border in a manner that was not in accordance with section 5.\n**(H)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of, the digital contents of an online account of, or online account information of an individual who is not a United States person at the border.\n**(I)**\nAccessed the digital contents of any electronic equipment belonging to or in the possession of an individual at the border, the digital contents of an online account of an individual at the border, or online account information of an individual at the border (regardless of whether the individual is a United States person) at the request of a Governmental entity (including another component of the Department of Homeland Security) that is not the Governmental entity employing the individual accessing the digital contents or online account information.\n**(2)**\nAggregate data on\u2014\n**(A)**\nthe number of United States persons for which a Governmental entity obtains access to\u2014\n**(i)**\nthe digital contents of electronic equipment belonging to or in the possession of the United States person at the border;\n**(ii)**\nthe digital contents of an online account of the United States person while at the border; or\n**(iii)**\nonline account information of the United States person while at the border;\n**(B)**\nthe country from which United States persons departed most recently before arriving in the United States for the United States persons for which a Governmental entity obtains access to\u2014\n**(i)**\nthe digital contents of electronic equipment belonging to or in the possession of the United States person at the border;\n**(ii)**\nthe digital contents of an online account of the United States person while at the border; or\n**(iii)**\nonline account information of the United States person while at the border;\n**(C)**\nthe number and nationality of individuals who are not United States persons for which a Governmental entity obtains access to\u2014\n**(i)**\nthe digital contents of electronic equipment belonging to or in the possession of the individuals at the border;\n**(ii)**\nthe digital contents of an online account of the individuals while at the border; or\n**(iii)**\nonline account information of the individuals while at the border; and\n**(D)**\nthe country from which individuals who are not United States persons departed most recently before arriving in the United States for the individuals for which a Governmental entity obtains access to\u2014\n**(i)**\nthe digital contents of electronic equipment belonging to or in the possession of the individuals at the border;\n**(ii)**\nthe digital contents of an online account of the individuals while at the border; or\n**(iii)**\nonline account information of the individuals while at the border.\n**(3)**\nAggregate data regarding the perceived race and ethnicity of individuals for whom a Governmental entity obtains access to\u2014\n**(A)**\nthe digital contents of electronic equipment belonging to or in the possession of the individuals at the border;\n**(B)**\nthe digital contents of an online account of the individuals while at the border; or\n**(C)**\nonline account information of the individuals while at the border.\n#### 8. Savings provisions\nNothing in this Act shall be construed to\u2014\n**(1)**\nprohibit a Governmental entity from conducting an inspection of the external physical components of the electronic equipment to determine the presence or absence of weapons or contraband without a warrant, including activating or attempting to activate an object that appears to be electronic equipment to verify that the object is electronic equipment; or\n**(2)**\nlimit the authority of a Governmental entity under the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 et seq. ).",
      "versionDate": "2025-04-02",
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
        "name": "Immigration",
        "updateDate": "2025-04-09T14:22:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2604",
          "measure-number": "2604",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-02",
          "originChamber": "HOUSE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2604v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Data at the Border Act</strong></p><p>This bill limits government access to digital information at the border.</p><p>A governmental entity may not (1) access the digital contents of electronic equipment of a U.S. person at the border without a warrant, (2) deny such a person's entry into or exit from the United States because the person refused to provide access to digital content on electronic equipment or online account information, (3) delay such a person's entry or exit for more than four hours to determine whether the person will consent to providing access to online information, or (4) seize electronic equipment from a U.S. person without probable cause to believe that such equipment contains information relevant to a felony.</p><p>A governmental entity may access the contents of electronic equipment of a U.S. person without a warrant in an emergency. The entity must subsequently apply for a warrant within seven days, and if a warrant is not granted, the seized information must be destroyed and may not be disclosed.</p><p>A governmental entity may not make or retain a copy of information accessed under this bill without probable cause to believe that such information relates to a crime.</p><p>Information seized in violation of this bill (1) must be destroyed, (2) may not be disclosed, and (3) may not be received in evidence in any trial or government proceeding.</p><p>A governmental entity shall keep a record of each instance in which it obtains access to an individual's digital information at the border.</p>"
        },
        "title": "Protecting Data at the Border Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2604.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Data at the Border Act</strong></p><p>This bill limits government access to digital information at the border.</p><p>A governmental entity may not (1) access the digital contents of electronic equipment of a U.S. person at the border without a warrant, (2) deny such a person's entry into or exit from the United States because the person refused to provide access to digital content on electronic equipment or online account information, (3) delay such a person's entry or exit for more than four hours to determine whether the person will consent to providing access to online information, or (4) seize electronic equipment from a U.S. person without probable cause to believe that such equipment contains information relevant to a felony.</p><p>A governmental entity may access the contents of electronic equipment of a U.S. person without a warrant in an emergency. The entity must subsequently apply for a warrant within seven days, and if a warrant is not granted, the seized information must be destroyed and may not be disclosed.</p><p>A governmental entity may not make or retain a copy of information accessed under this bill without probable cause to believe that such information relates to a crime.</p><p>Information seized in violation of this bill (1) must be destroyed, (2) may not be disclosed, and (3) may not be received in evidence in any trial or government proceeding.</p><p>A governmental entity shall keep a record of each instance in which it obtains access to an individual's digital information at the border.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr2604"
    },
    "title": "Protecting Data at the Border Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Data at the Border Act</strong></p><p>This bill limits government access to digital information at the border.</p><p>A governmental entity may not (1) access the digital contents of electronic equipment of a U.S. person at the border without a warrant, (2) deny such a person's entry into or exit from the United States because the person refused to provide access to digital content on electronic equipment or online account information, (3) delay such a person's entry or exit for more than four hours to determine whether the person will consent to providing access to online information, or (4) seize electronic equipment from a U.S. person without probable cause to believe that such equipment contains information relevant to a felony.</p><p>A governmental entity may access the contents of electronic equipment of a U.S. person without a warrant in an emergency. The entity must subsequently apply for a warrant within seven days, and if a warrant is not granted, the seized information must be destroyed and may not be disclosed.</p><p>A governmental entity may not make or retain a copy of information accessed under this bill without probable cause to believe that such information relates to a crime.</p><p>Information seized in violation of this bill (1) must be destroyed, (2) may not be disclosed, and (3) may not be received in evidence in any trial or government proceeding.</p><p>A governmental entity shall keep a record of each instance in which it obtains access to an individual's digital information at the border.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr2604"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2604ih.xml"
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
      "title": "Protecting Data at the Border Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Data at the Border Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the digital contents of electronic equipment and online accounts belonging to or in the possession of United States persons entering or exiting the United States are adequately protected at the border, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:24Z"
    }
  ]
}
```
