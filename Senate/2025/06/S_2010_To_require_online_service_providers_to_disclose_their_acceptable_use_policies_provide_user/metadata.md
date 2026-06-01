# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2010
- Title: TERMS Act
- Congress: 119
- Bill type: S
- Bill number: 2010
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-12-05T22:49:30Z
- Update date including text: 2025-12-05T22:49:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2010",
    "number": "2010",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "TERMS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:30Z",
    "updateDateIncludingText": "2025-12-05T22:49:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T18:43:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "AL"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "AR"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "WY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "ID"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MO"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2010is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2010\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Cruz (for himself, Mrs. Blackburn , Mrs. Britt , Mr. Cotton , Mr. Crapo , Ms. Lummis , Mr. Marshall , Mr. Risch , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require online service providers to disclose their acceptable use policies, provide users with written notice before the termination of a user\u2019s account, and publish an annual report detailing actions taken to enforce their acceptable use policies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency in Enforcement, Restricting, and Monitoring of Services Act or the TERMS Act .\n#### 2. Purpose\nThe purpose of this Act is to ensure that consumers, businesses, and organizations seeking to use the products or services of an online service provider have sufficient information regarding the online service provider\u2019s commercial business standards, processes, and policies with respect to the unilateral termination, suspension, or cancellation of user accounts or ability to use the online service provider\u2019s products or services. Such information allows consumers to make informed choices regarding their decision to use or purchase the services or products of an online service provider and promotes a competitive marketplace for such products or services.\n#### 3. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Nonprofit organization**\nThe term nonprofit organization has the meaning given such term in section 201(i) of title 35, United States Code.\n**(3) Online service provider**\nThe term online service provider \u2014\n**(A)**\nmeans the provider of a public-facing website, online service, or online application directed to a consumer or organization that\u2014\n**(i)**\nrequires any person who wishes to use the website, online service, or online application to create a unique account or profile for such website, service, or application;\n**(ii)**\nprovides an internet-based product or service that is accessible through the website, online service, or online application; and\n**(iii)**\nis engaged in interstate or foreign commerce; and\n**(B)**\nincludes any entity described in subparagraph (A), regardless of whether\u2014\n**(i)**\noffering a product or service to the general public is the sole source of income or principal business of such entity; or\n**(ii)**\nthe entity earns a profit on a product or service.\n**(4) Restrict**\nThe term restrict , with respect to a user, means an online service provider\u2019s termination or suspension of a user\u2019s account or profile on the online service provider\u2019s website, online service, or online application, or limitation of the user\u2019s access thereto based on a determination that the user violated the online service provider\u2019s acceptable use policy.\n**(5) User**\nThe term user means, with respect to an online service provider, a person who registers an account or creates a profile on the website, online service, or online application of the online service provider.\n#### 4. Disclosure of acceptable use policies\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act and subject to subsection (b), an online service provider shall publicly disclose in an easily accessible manner, such as within terms of service available on the online service provider\u2019s website, an acceptable use policy that concisely and accurately describes, in clear language, information regarding the standards, processes, and policies of the online service provider with respect to any decision by the online service provider to restrict a user.\n##### (b) Required information\nFor purposes of subsection (a), an online service provider shall include the following information in an acceptable use policy:\n**(1)**\nAn explanation of what specific acts or practices are prohibited by the online service provider that could lead to a decision by the online service provider to restrict a user.\n**(2)**\nAn explanation of how the online service provider enforces the acceptable use policy, including any third party the online service provider relies upon, in whole or in part, to assist in the enforcement of the acceptable use policy by the online service provider.\n**(3)**\nEither\u2014\n**(A)**\nan explanation of how a user can appeal, if applicable, a decision by an online service provider to restrict a user; or\n**(B)**\nif the online service provider does not permit an appeal or reconsideration of a decision to restrict a user, a statement that such decision is not appealable or subject to reconsideration.\n**(4)**\nAn explanation of whether acts or practices a user commits entirely outside of the website, online service, or online application of the online service provider, such as social media posts, public statements, media publications, and third-party resources, may be a sufficient basis alone or in combination with other information to restrict a user.\n**(5)**\nAn explanation of the online service provider\u2019s standards, processes, and policies with respect to the notice requirement described in section 5.\n##### (c) Changes to acceptable use policies\nIf an online service provider makes a material change to its acceptable use policy that would result in a material change to any information described in subsection (b), the online service provider shall, taking into account available technology, provide advance notice to each user.\n#### 5. Advance written notice prior to termination or suspension\n##### (a) Notice requirement\n**(1) In general**\nExcept as described in subsection (b), an online service provider shall provide advance written notice to a user in violation of the online service provider\u2019s acceptable use policy prior to restricting the user.\n**(2) Required information**\nThe advance written notice required under paragraph (1) shall include the following information:\n**(A)**\nThe specific act or practice of the user that led to the decision to restrict the user.\n**(B)**\nA description of how the act or practice identified in subparagraph (A) violated the acceptable use policy.\n**(C)**\nWhether the user has an option to appeal the decision, and, if so, a description of the process for how the user can appeal the online service provider\u2019s decision, consistent with the acceptable use policy.\n**(D)**\nA description of the option for the user to elect that the online service provider publicly disclose such written notice as described in paragraph (4).\n**(3) Advance written notice**\n**(A) In general**\nFor the purposes of this section, an online service provider will be deemed to have provided an advance written notice to a user if such provider makes a good faith effort to notify the user not later than 7 days prior to restricting the user.\n**(B) Good faith effort**\nFor the purposes of subparagraph (A), a good faith effort may include\u2014\n**(i)**\na notification to the most recent email address or other contact information the user provided to the online service provider; or\n**(ii)**\nif the online service provider does not have any contact information for the user, a prominent notice that is displayed to the user on the online service provider\u2019s website, service, or application when the user next accesses the user\u2019s account or profile on such website, service, or application.\n**(4) Public disclosure**\nAn online service provider shall\u2014\n**(A)**\nprovide to any user issued a written notice under paragraph (1) an option for the online service provider to publicly disclose such notice; and\n**(B)**\nif such user chooses to have such notice publicly disclosed, publish such notice on the website of the online service provider.\n##### (b) Exceptions for court action or imminent risk of harm\nAn online service provider may restrict a user without advance written notice if\u2014\n**(1)**\nsuch restriction was done to\u2014\n**(A)**\ncomply with a lawful order of a court of competent jurisdiction;\n**(B)**\ncomply with Federal law; or\n**(C)**\nprotect against an imminent risk of\u2014\n**(i)**\ndeath;\n**(ii)**\na serious physical injury; or\n**(iii)**\na serious health risk; and\n**(2)**\nthe online service provider provides the user the information required by subsection (a)(2) and publicly discloses the written notice at the same time that the provider restricts the user or as soon as practicable thereafter.\n##### (c) Effective date\nThe requirements of this section shall take effect on the date that is 180 days after the date of enactment of this Act.\n#### 6. Reporting requirements\n##### (a) Annual report\nNot later than 1 year after the date of enactment of this Act and annually thereafter on a date to be determined by each online service provider, an online service provider shall publish, with an open license, in both a format easily read by humans and a machine-readable format, in a location on its public website that is easily accessible to users and visitors of such website, and consistent with the requirements described in subsections (b) and (c), a report detailing actions taken to enforce the online service provider\u2019s acceptable use policy.\n##### (b) Report requirements\nThe report required under subsection (a) shall include the following information with respect to the applicable reporting period:\n**(1)**\nThe total number of instances in which the online service provider was alerted of a potential violation of the acceptable use policy by\u2014\n**(A)**\na user complaint;\n**(B)**\nan employee of, or a person contracting with, the online service provider;\n**(C)**\nan internal automated detection tool of the online service provider;\n**(D)**\na government entity, including the specific office or entity that alerted the online service provider;\n**(E)**\na nonprofit organization; or\n**(F)**\nany other person.\n**(2)**\nSubject to subsection (c), the number of instances in which the online service provider took steps to restrict a user, including the number of instances in which the online service provider\u2014\n**(A)**\nterminated a user\u2019s account or profile on the online service provider\u2019s website, online service, or online application or otherwise permanently limited access to or use of the product or service of the online service provider;\n**(B)**\nsuspended a user\u2019s account or profile on the online service provider\u2019s website, online service, or online application;\n**(C)**\nlimited a user\u2019s access to the online service provider\u2019s website, online service, or online application; or\n**(D)**\ntook any other action, such as issuing a warning, in response to a violation of the acceptable use policy.\n**(3)**\nThe number of instances in which a user appealed the online service provider\u2019s decision.\n**(4)**\nThe number of appeals that resulted in a reversal of the online service provider\u2019s decision.\n##### (c) Categorization of actions taken\nThe information described in subsection (b)(2) shall be categorized by\u2014\n**(1)**\nthe exact provision of the acceptable use policy that was violated by a user; and\n**(2)**\nthe source of the alert of the potential violation of the acceptable use policy as described in subsection (b)(1).\n#### 7. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nExcept as provided in subparagraph (C), any online service provider who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Nonprofit organizations**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2), 46) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraphs (A) and (B), with respect to organizations not organized to carry on business for their own profit or that of their members.\n**(D) Authority preserved**\nNothing in this subsection shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Commission guidance\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Commission shall issue guidance to assist online service providers in complying with the requirements of this Act, which shall include the provision of best practices and examples.\n**(2) Limitation on guidance**\nNo guidance issued by the Commission with respect to this Act shall\u2014\n**(A)**\nconfer any rights on any person, State, or locality; or\n**(B)**\noperate to bind the Commission or any person to the approach recommended in such guidance.\n**(3) Use in enforcement actions**\nIn any enforcement action brought pursuant to this Act\u2014\n**(A)**\nthe Commission\u2014\n**(i)**\nshall allege a specific violation of a provision of this Act; and\n**(ii)**\nmay not base such enforcement on, or execute a consent order based on, practices that are alleged to be inconsistent with any guidance issued by the Commission with respect to this Act, unless the practices are alleged to violate a provision of this Act; and\n**(B)**\na person may use compliance with any such guidance as evidence of compliance with this Act.",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-06-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3875",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TERMS Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-07-18T14:47:21Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2010is.xml"
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
      "title": "TERMS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TERMS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transparency in Enforcement, Restricting, and Monitoring of Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require online service providers to disclose their acceptable use policies, provide users with written notice before the termination of a user's account, and publish an annual report detailing actions taken to enforce their acceptable use policies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:20Z"
    }
  ]
}
```
