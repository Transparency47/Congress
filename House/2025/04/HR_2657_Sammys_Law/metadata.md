# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2657
- Title: Sammy’s Law
- Congress: 119
- Bill type: HR
- Bill number: 2657
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-05-30T08:05:49Z
- Update date including text: 2026-05-30T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-03 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-03 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2657",
    "number": "2657",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000797",
        "district": "25",
        "firstName": "Debbie",
        "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
        "lastName": "Wasserman Schultz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Sammy\u2019s Law",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:49Z",
    "updateDateIncludingText": "2026-05-30T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:35:11Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:34:24Z",
                "name": "Markup by"
              },
              {
                "date": "2025-04-03T20:34:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "GA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "WA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IL"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2657ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2657\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Ms. Wasserman Schultz (for herself, Mr. Carter of Georgia , Ms. Schrier , Mrs. Miller-Meeks , Mr. Suozzi , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces, through which a child or a parent or legal guardian of a child may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on the large social media platform on the same terms as such child, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sammy\u2019s Law .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nparents and legal guardians should be empowered to use the services of third-party safety software providers to protect the children of such parents and legal guardians from certain harms on large social media platforms; and\n**(2)**\ndangers like cyberbullying, human trafficking, illegal drug distribution, sexual harassment, and violence perpetrated, facilitated, or exacerbated through the use of certain large social media platforms have harmed children on such platforms.\n#### 3. Definitions\nIn this Act:\n**(1) Child**\nThe term child means any individual under the age of 17 years who has registered an account with a large social media platform.\n**(2) Commerce**\nThe term commerce has the meaning given such term in section 4 of the Federal Trade Commission Act ( 15 U.S.C. 44 ).\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Large social media platform**\nThe term large social media platform \u2014\n**(A)**\nmeans a service\u2014\n**(i)**\nprovided through an internet website or a mobile application (or both);\n**(ii)**\nthe terms of service of which do not prohibit the use of the service by a child;\n**(iii)**\nwith any feature or features that enable a child to share images, text, or video through the internet with other users of the service whom such child has met, identified, or become aware of solely through the use of the service; and\n**(iv)**\nthat has more than 100,000,000 monthly global active users or generates more than $1,000,000,000 in gross revenue per year, adjusted yearly for inflation; and\n**(B)**\ndoes not include\u2014\n**(i)**\na service that primarily serves\u2014\n**(I)**\nto facilitate\u2014\n**(aa)**\nthe sale or provision of professional services; or\n**(bb)**\nthe sale of commercial products; or\n**(II)**\nto provide news or information, where the service does not offer the ability for content to be sent by a user directly to a child; or\n**(ii)**\na service that\u2014\n**(I)**\nhas a feature that enables a user who communicates directly with a child through a message (including a text, audio, or video message) not otherwise available to other users of the service to add other users to that message that such child may not have otherwise met, identified, or become aware of solely through the use of the service; and\n**(II)**\ndoes not have any feature or features described in subparagraph (A)(iii).\n**(5) Large social media platform provider**\nThe term large social media platform provider means any person who, for commercial purposes in or affecting commerce, provides, manages, operates, or controls a large social media platform.\n**(6) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(7) Third-party safety software provider**\nThe term third-party safety software provider means any person who, for commercial purposes in or affecting commerce, is authorized by a child (if the child is 13 years of age or older) or a parent or legal guardian of a child to interact with a large social media platform to manage the online interactions, content, or account settings of such child for the sole purpose of protecting such child from harm, including physical or emotional harm.\n**(8) User data**\nThe term user data means any information needed to have a profile on a large social media platform or content on a large social media platform, including images, video, audio, or text, that is created by or sent to a child on or through the account of such child with such platform, but only\u2014\n**(A)**\nif the information or content is created by or sent to such child while a delegation under section 4(a) is in effect with respect to the account; and\n**(B)**\nduring a 30-day period beginning on the date on which the information or content is created by or sent to such child.\n#### 4. Providing access to third-party safety software\n##### (a) Duty of large social media platform providers\n**(1) In general**\nNot later than 30 days after the effective date of this Act (in the case of a service that is a large social media platform on such effective date) or not later than 30 days after a service becomes a large social media platform (in the case of a service that becomes a large social media platform after such effective date), the large social media platform provider shall create, maintain, and make available to any third-party safety software provider registered with the Commission under subsection (b)(1) a set of third-party-accessible real-time application programming interfaces, including any information necessary to use such interfaces, by which a child (if the child is 13 years of age or older) or a parent or legal guardian of a child may delegate permission to the third-party safety software provider to\u2014\n**(A)**\nmanage the online interactions, content, and account settings of such child on the large social media platform on the same terms as such child; and\n**(B)**\ninitiate secure transfers of user data from the large social media platform in a commonly-used and machine-readable format to the third-party safety software provider, where the frequency of such transfers may not be limited by the large social media platform provider to less than once per hour.\n**(2) Revocation**\nOnce a child or a parent or legal guardian of a child makes a delegation under paragraph (1), the large social media platform provider shall make the application programming interfaces and information described in such paragraph available to the third-party safety software provider on an ongoing basis until\u2014\n**(A)**\nthe child (if the child made the delegation) or the parent or legal guardian of such child revokes the delegation;\n**(B)**\nthe child or a parent or legal guardian of such child revokes or disables the registration of the account of such child with the large social media platform;\n**(C)**\nthe third-party safety software provider rejects the delegation; or\n**(D)**\none or more of the affirmations made by the third-party safety software provider under subsection (b)(1)(A) is no longer true.\n**(3) Secure transfer of user data**\nA large social media platform provider shall establish and implement reasonable policies, practices, and procedures regarding the secure transfer of user data pursuant to a delegation under paragraph (1) from the large social media platform to a third-party safety software provider in order to mitigate any risks related to user data.\n**(4) Disclosure**\nIn the case of a delegation made by a child or a parent or legal guardian of a child under paragraph (1) with respect to the account of such child with a large social media platform, the large social media platform provider shall\u2014\n**(A)**\ndisclose to such child and (if the parent or legal guardian made the delegation) the parent or legal guardian the fact that the delegation has been made;\n**(B)**\nprovide to such child and (if such parent or legal guardian made the delegation) such parent or legal guardian a summary of the user data that is transferred to the third-party safety software provider; and\n**(C)**\nupdate the summary provided under subparagraph (B) as necessary to reflect any change to the user data that is transferred to the third-party safety software provider.\n**(5) Limitation**\nAny management by a third-party safety software provider of online interactions, content, and account settings of a child under this subsection shall be limited to such management that protects such child from harm, including the optimization of the privacy settings of the account, stated user age, and marketing settings of the child.\n##### (b) Third-Party safety software providers\n**(1) Registration with Commission**\nA third-party safety software provider shall register with the Commission as a condition of accessing an application programming interface and any information under subsection (a). As a condition of such registration, the third-party safety software provider shall\u2014\n**(A)**\nsatisfactorily demonstrate to the Commission that the third-party safety software provider\u2014\n**(i)**\nis a company based in the United States;\n**(ii)**\nis not a subsidiary of any foreign-owned company or otherwise controlled by a foreign person or persons;\n**(iii)**\nwill solely use any user data obtained under subsection (a) for the purpose of protecting a child from harm in accordance with any applicable terms of service and the provisions of this Act;\n**(iv)**\nwill only disclose user data obtained under subsection (a) as permitted by subsection (f);\n**(v)**\nwill process and maintain all user data obtained under subsection (a) and copies of any communications generated in relation thereto exclusively on hardware and devices located within the territorial boundaries of the United States;\n**(vi)**\n**(I)**\nwill delete any user data obtained under this section as soon as possible but not later than 14 days after receiving such data from the large social media platform, not including any data the third-party safety software provider discloses under subsection (f);\n**(II)**\nfor any data disclosed under subsection (f)(1)(C), will maintain such data until the child or a parent or legal guardian of the child who made a delegation under subsection (a) and whose data is at issue requests that the third-party safety software provider delete such data; and\n**(III)**\nin the event that the child or a parent or legal guardian of the child who made a delegation under subsection (a) cancels their account with the third-party safety software provider, will delete all applicable user data no later than 30 days after the request for account cancellation has been made; and\n**(vii)**\nwill disclose, in an easy-to-understand, human-readable format, to each child with respect to whose account with a large social media platform the service of the third-party safety software provider is operating and (if a parent or legal guardian of the child made the delegation under subsection (a) with respect to the account) to the parent or legal guardian, sufficient information detailing the operation of the service and what information the third-party safety software provider is collecting to enable such child and (if applicable) such parent or legal guardian to make informed decisions regarding the use of the service; and\n**(B)**\nas part of the registration process, undergo a security review in such form as the Commission may proscribe but which may include requiring that a qualified independent auditing firm conduct such a review to independently verify and confirm via a written report (which shall be exempt from disclosure under section 552(b)(3) of title 5, United States Code) that the third-party safety software provider\u2014\n**(i)**\nis in compliance, or has the ability to comply, with the requirements of subparagraph (A);\n**(ii)**\nis able to provide services in accordance with any applicable terms of service and any relevant disclosures made to any consumer, including whether such terms and disclosures are clear and conspicuous and are written in plain and easy-to-understand English;\n**(iii)**\nhas taken appropriate steps to assess potential risks and to protect the confidentiality, integrity, and security of any user data, including a determination of the adequacy of business and technology-related controls, policies, procedures, and other safeguards employed by the third-party safety software provider based on guidance issued by the Commission and other industry standards and best practices; and\n**(iv)**\nassesses compliance with applicable Federal law, including the requirements of this Act.\n**(2) Annual audit**\n**(A) Audit process; audit report**\nFor each year or partial year during which a third-party safety software provider is registered with the Commission under paragraph (1), the third-party safety software provider shall retain the services of a qualified independent auditing firm to complete an annual audit and write an audit report (which shall be exempt from disclosure under section 552(b)(3) of title 5, United States Code), and such audit report shall\u2014\n**(i)**\ninclude a review and assessment of the third-party safety software provider\u2019s initial security review and any subsequent written reports, including whether the third-party safety software provider has remained in compliance with the requirements described in paragraph (1)(B); and\n**(ii)**\nidentify whether the third-party safety software provider has made any material changes in how the third-party safety software provider provides services, and in the event of any such material changes, provide an explanation as to how such changes have impacted users.\n**(B) Submission to Commission**\nNot later than 30 days after the date on which an audit report is written under subparagraph (A), a third-party safety software provider shall submit to the Commission\u2014\n**(i)**\na full copy of such audit report; and\n**(ii)**\na summary of such audit report that may contain redactions to protect the proprietary information and trade secrets of the third-party safety software provider.\n**(C) Audit review by Commission**\nThe Commission shall\u2014\n**(i)**\nreview each audit report submitted by a third-party safety software provider under subparagraph (B)(i) to verify compliance;\n**(ii)**\nmake a copy of the summary of such audit report submitted by a third-party safety software provider under subparagraph (B)(ii) available to the public; and\n**(iii)**\nin the event an audit required under subparagraph (A) detects an unusual finding, direct a third-party safety software provider to promptly investigate and resolve the matter.\n**(3) Additional authority of Commission**\nIn addition to the jurisdiction, powers, and duties of the Commission otherwise provided under this Act and any other provision of law, the Commission may take an adverse action against a third-party safety software provider, including by\u2014\n**(A)**\ndenying an initial registration for the third-party safety software provider under paragraph (1);\n**(B)**\npermanently de-registering the third-party safety software provider; and\n**(C)**\nsuspending the registration of the third-party safety software provider due to an audit finding of a material risk to the security of the data or safety of the public, including for\u2014\n**(i)**\nwillful misconduct or gross negligence by the third-party safety software provider;\n**(ii)**\na material misrepresentation made by a third-party safety software provider to the Commission or to any consumer;\n**(iii)**\nfailure by the third-party safety software provider to comply with any requirements of this Act or failure to operate in accordance with the affirmations, assertions, representations, or terms of any security review, audit, terms of services, or consumer disclosures;\n**(iv)**\nfailure by the third-party safety software provider to respond to an unusual finding in an annual audit completed under paragraph (2)(A); and\n**(v)**\nfailure by the third-party safety software provider to adhere to or implement guidance issued by the Commission.\n**(4) Rights of third-party safety software providers**\n**(A) In general**\nIn the event the Commission takes an adverse action against a third-party safety software provider under paragraph (3), the Commission shall give the third-party safety software provider\u2014\n**(i)**\nthe opportunity to appeal the findings of the auditor or such action of the Commission; and\n**(ii)**\nthe opportunity to remediate any deficiencies, except in the case of a finding of\u2014\n**(I)**\nwillful misconduct;\n**(II)**\ngross negligence; or\n**(III)**\na demonstrated history of multiple failures in relation to the types of material risk described in paragraph (3)(C)(ii) through (3)(C)(v).\n**(B) Exception**\nThe rights described in subparagraph (A) shall not prevent the Commission from suspending the registration of a third-party safety software provider to protect the public from ongoing material risk for the period during which the third-party safety software provider is in the process of exercising the rights described in paragraph (4).\n##### (c) Authentication\nNot later than 180 days after the date of the enactment of this Act, the Commission shall issue guidance to facilitate the ability of a third-party safety software provider to obtain user data or access under subsection (a) in a manner that ensures that a request for user data or access on behalf of a child is a verifiable request.\n##### (d) Guidance and consumer education\nThe Commission shall\u2014\n**(1)**\nnot later than 180 days after the date of the enactment of this Act, issue guidance for large social media platform providers and third-party safety software providers regarding the maintenance of reasonable safety standards to protect user data; and\n**(2)**\neducate consumers regarding the rights of consumers under this Act.\n##### (e) Indemnification\nIn any civil action in Federal or State court (other than an action brought by the Commission), a large social media platform provider may not be held liable for damages arising out of the transfer of user data to a third-party safety software provider under subsection (a), if the large social media platform provider has in good faith complied with the requirements of this Act and the guidance issued by the Commission under this Act.\n##### (f) User data disclosure\n**(1) Permitted disclosures**\nA third-party safety software provider may not disclose any user data obtained under subsection (a) to any other person except\u2014\n**(A)**\npursuant to a lawful request from a government body, including for law enforcement purposes or for judicial or administrative proceedings by means of a court order or a court-ordered warrant, a subpoena or summons issued by a judicial officer, or a grand jury subpoena;\n**(B)**\nto the extent that such disclosure is required by law and such disclosure complies with and is limited to the relevant requirements of such law;\n**(C)**\nto the child or a parent or legal guardian of the child who made a delegation under such subsection and whose data is at issue, with such third-party safety software provider making a good faith effort to ensure that such disclosure includes only the user data necessary for a reasonable parent or caregiver to understand that such child is experiencing (or is at foreseeable risk to experience) the following harms\u2014\n**(i)**\nsuicide;\n**(ii)**\nanxiety;\n**(iii)**\ndepression;\n**(iv)**\neating disorders;\n**(v)**\nviolence, including being the victim of or planning to commit or facilitate assault;\n**(vi)**\nsubstance abuse;\n**(vii)**\nfraud;\n**(viii)**\nsevere forms of trafficking in persons (as defined in section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ));\n**(ix)**\nsexual abuse;\n**(x)**\nphysical injury;\n**(xi)**\nharassment;\n**(xii)**\nsexually explicit conduct or child pornography (as defined in section 2256 of title 18, United States Code);\n**(xiii)**\nterrorism (as defined in section 140(d) of the Foreign Relations Authorization Act, Fiscal Years 1988 and 1989 ( 22 U.S.C. 2656f(d) )), including communications with or in support of a foreign terrorist organization (as designated by the Secretary of State under section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ));\n**(xiv)**\nacademic dishonesty, including cheating, plagiarism, and other forms of academic dishonesty that are intended to gain an unfair academic advantage; and\n**(xv)**\nsharing personal information, limited to\u2014\n**(I)**\nhome address;\n**(II)**\nphone number;\n**(III)**\nsocial security number; and\n**(IV)**\npersonal banking information;\n**(D)**\nin the case of a reasonably foreseeable serious and imminent threat to the health or safety of any individual, if the disclosure is made to a person or persons reasonably able to prevent or lessen the threat; or\n**(E)**\nto a public health authority or other appropriate government authority authorized by law to receive reports of child abuse or neglect.\n**(2) Disclosure reporting**\nA third-party safety software provider that makes a disclosure permitted by paragraph (1)(A), (1)(B), (1)(D), or (1)(E) shall promptly inform the child with respect to whose account with a large social media platform the delegation was made under subsection (a) and (if a parent or legal guardian of the child made the delegation) the parent or legal guardian that such a disclosure has been or will be made, except if\u2014\n**(A)**\nthe third-party safety software provider, in the exercise of professional judgment, believes informing such child or parent or legal guardian would place such child at risk of serious harm; or\n**(B)**\nthe third-party safety software provider is prohibited by law (including a valid order by a court or administrative body) from informing such child or parent or legal guardian.\n#### 5. Implementation and enforcement\n##### (a) Enforcement\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Preservation of authority**\nNothing in this Act may be construed to limit the authority of the Commission under any other provision of law.\n##### (b) FTC guidance\nNot later than 180 days after the date of the enactment of this Act, the Commission shall issue guidance to assist large social media platform providers and third-party safety software providers in complying with this Act.\n##### (c) Compliance assessment\nThe Commission, on a biannual basis, shall assess compliance by large social media platform providers and third-party safety software providers with the provisions of this Act.\n##### (d) Complaints\nThe Commission shall establish procedures under which a child, or the parent or legal guardian of such child, a large social media platform provider, or a third-party safety software provider may file a complaint alleging that a large social media platform provider or a third-party safety software provider has violated this Act.\n#### 6. One national standard\n##### (a) In general\nNo State or political subdivision of a State may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of a State, related to requiring large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces, through which a child or a parent or legal guardian of a child may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on a large social media platform on the same terms as such child.\n##### (b) Rule of construction\nThis section may not be construed to\u2014\n**(1)**\nlimit the enforcement of any consumer protection law of a State or political subdivision of a State;\n**(2)**\npreempt the applicability of State trespass, contract, or tort law; or\n**(3)**\npreempt the applicability of any State law to the extent that the law relates to acts of fraud, unauthorized access to personal information, or notification of unauthorized access to personal information.\n#### 7. Effective date\nThis Act shall take effect on the date on which the Commission issues guidance under section 5(b).",
      "versionDate": "2025-04-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Business records",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-01-02T15:41:27Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-01-02T15:41:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-01T14:59:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2657",
          "measure-number": "2657",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2657v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sammy\u2019s Law</strong></p><p>This bill requires large social media platforms to permit certain providers of safety software to monitor and manage the activity of children under the age of 17 on such platforms.</p><p>Specifically, large social media platforms must make available a mechanism by which a child or their parent or guardian may permit a provider of safety software to (1) manage the child\u2019s interactions, content, and account settings on the platform; and (2) regularly access the child\u2019s user data.</p><p>A software provider may only disclose a child\u2019s data under limited circumstances, including to the child\u2019s parent or guardian if the child is experiencing or is at foreseeable risk of experiencing specified harms. Such harms include suicide, eating disorders, sexual abuse, harassment, and academic dishonesty. The provider may only share data necessary for a reasonable parent or caregiver to understand that the child is experiencing or is at risk of harm.</p><p>To participate, a software provider must register with the Federal Trade Commission, undergo a security review, and demonstrate that, among other requirements, the provider is based in the United States and will use a child's data solely to protect them from harm.</p><p>Under the bill, a <em>large social media platform</em> is generally a service that enables a child to share content through the internet with other users that the child has become aware of solely through the platform, and which has more than 100 million monthly global active users or generates more than $1 billion in gross annual revenue.</p>"
        },
        "title": "Sammy\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2657.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sammy\u2019s Law</strong></p><p>This bill requires large social media platforms to permit certain providers of safety software to monitor and manage the activity of children under the age of 17 on such platforms.</p><p>Specifically, large social media platforms must make available a mechanism by which a child or their parent or guardian may permit a provider of safety software to (1) manage the child\u2019s interactions, content, and account settings on the platform; and (2) regularly access the child\u2019s user data.</p><p>A software provider may only disclose a child\u2019s data under limited circumstances, including to the child\u2019s parent or guardian if the child is experiencing or is at foreseeable risk of experiencing specified harms. Such harms include suicide, eating disorders, sexual abuse, harassment, and academic dishonesty. The provider may only share data necessary for a reasonable parent or caregiver to understand that the child is experiencing or is at risk of harm.</p><p>To participate, a software provider must register with the Federal Trade Commission, undergo a security review, and demonstrate that, among other requirements, the provider is based in the United States and will use a child's data solely to protect them from harm.</p><p>Under the bill, a <em>large social media platform</em> is generally a service that enables a child to share content through the internet with other users that the child has become aware of solely through the platform, and which has more than 100 million monthly global active users or generates more than $1 billion in gross annual revenue.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr2657"
    },
    "title": "Sammy\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sammy\u2019s Law</strong></p><p>This bill requires large social media platforms to permit certain providers of safety software to monitor and manage the activity of children under the age of 17 on such platforms.</p><p>Specifically, large social media platforms must make available a mechanism by which a child or their parent or guardian may permit a provider of safety software to (1) manage the child\u2019s interactions, content, and account settings on the platform; and (2) regularly access the child\u2019s user data.</p><p>A software provider may only disclose a child\u2019s data under limited circumstances, including to the child\u2019s parent or guardian if the child is experiencing or is at foreseeable risk of experiencing specified harms. Such harms include suicide, eating disorders, sexual abuse, harassment, and academic dishonesty. The provider may only share data necessary for a reasonable parent or caregiver to understand that the child is experiencing or is at risk of harm.</p><p>To participate, a software provider must register with the Federal Trade Commission, undergo a security review, and demonstrate that, among other requirements, the provider is based in the United States and will use a child's data solely to protect them from harm.</p><p>Under the bill, a <em>large social media platform</em> is generally a service that enables a child to share content through the internet with other users that the child has become aware of solely through the platform, and which has more than 100 million monthly global active users or generates more than $1 billion in gross annual revenue.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr2657"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2657ih.xml"
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
      "title": "Sammy\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sammy\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces, through which a child or a parent or legal guardian of a child may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on the large social media platform on the same terms as such child, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:18:30Z"
    }
  ]
}
```
