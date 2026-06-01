# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2889
- Title: Online Consumer Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2889
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-14T14:53:54Z
- Update date including text: 2026-05-14T14:53:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2889",
    "number": "2889",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Online Consumer Protection Act",
    "type": "HR",
    "updateDate": "2026-05-14T14:53:54Z",
    "updateDateIncludingText": "2026-05-14T14:53:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:10:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2889ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2889\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. Schakowsky (for herself and Ms. Castor of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo clarify that a violation of certain terms of service and related materials is an unfair or deceptive act or practice and subject to enforcement by the Federal Trade Commission.\n#### 1. Short title\nThis Act may be cited as the Online Consumer Protection Act .\n#### 2. Terms of service required for social media platforms and online marketplaces\n##### (a) In general\nEach social media platform or online marketplace shall establish, maintain, and make publicly available at all times and in a machine-readable format, terms of service in a manner that is clear, easily understood, and written in plain and concise language. The terms of service shall meet the following requirements:\n**(1)**\nThe terms of service shall include\u2014\n**(A)**\nany terms or conditions of use of any service provided by such person to a consumer;\n**(B)**\nany policies of such person with regard to such service or use of such service by a consumer; and\n**(C)**\nthe consumer protection policy consistent with subsection (b).\n**(2)**\nThe terms of service shall cover issues related to the behavior of a service or a user of such service, and shall at a minimum include terms of use related to\u2014\n**(A)**\npayment methods;\n**(B)**\ncontent ownership, including content generated by a user;\n**(C)**\npolicies related to sharing user content with third parties;\n**(D)**\nany disclaimers, limitations, notices of nonliability, or the consequences of not agreeing to or complying with the terms of service; and\n**(E)**\nany other topic the Commission deems appropriate.\n##### (b) Required consumer protection policy\n**(1) For social media platforms**\nFor social media platforms, the consumer protection policy required by subsection (a) shall include\u2014\n**(A)**\na description of the content and behavior permitted or prohibited on its service both by the platform and by users;\n**(B)**\nwhether content may be blocked, removed, or modified, or if service to users may be terminated and the grounds upon which such actions will be taken;\n**(C)**\nwhether a person can request that content be blocked, removed, or modified, or that a user\u2019s service be terminated, and how to make such a request;\n**(D)**\na description of how a user will be notified of and can respond to a request that his or her content be blocked, removed, or modified, or service be terminated, if such actions are taken;\n**(E)**\nwhether a user who requested content be blocked, removed, or modified will be notified of whether action was taken as a result of the request, the action that was taken, the reason why action was taken or not taken, and how the user will be notified;\n**(F)**\nhow a person can appeal a decision to block, remove, or modify content, allow content to remain, or terminate or not terminate service to a user, if such actions are taken;\n**(G)**\na description of how a user will be notified of the result of the appeal;\n**(H)**\na description of the tools and support available to users who have experienced cyber harassment; and\n**(I)**\nany other topic the Commission deems appropriate.\n**(2) For online marketplaces**\nFor online marketplaces, the consumer protection policy required by subsection (a) shall include\u2014\n**(A)**\na description of the products, product descriptions, and marketing material, allowed or disallowed on the marketplace;\n**(B)**\nwhether a product, product descriptions, and marketing material may be blocked, removed, or modified, or if service to a user may be terminated and the grounds upon which such actions will be taken;\n**(C)**\nwhether users will be notified of products that have been recalled or are dangerous, and how they will be notified;\n**(D)**\nfor users\u2014\n**(i)**\nwhether a user can report suspected fraud, deception, dangerous products, or violations of the online marketplace\u2019s terms of service, and how to make such report;\n**(ii)**\nwhether a user who submitted a report will be notified of whether action was taken as a result of the report, the action that was taken and the reason why action was taken or not taken, and how the user will be notified;\n**(iii)**\nhow to appeal the result of a report;\n**(iv)**\nwhether a user who appealed the result of a report will be notified of whether action was taken as a result of the appeal, the action that was taken, the reason why action was taken or not taken, and how the user will be notified; and\n**(v)**\nunder what circumstances a user is entitled to refund, repair, or other remedy and the remedy to which the user may be entitled, how the user will be notified of such entitlement, and how the user may claim such remedy; and\n**(E)**\nfor sellers\u2014\n**(i)**\nhow sellers are notified of a report by a user or a violation of the terms of service or consumer protection policy;\n**(ii)**\nhow to contest a report by a user;\n**(iii)**\nhow a seller who is the subject of a report will be notified of what action will be or must be taken as a result of the report and the justification for such action;\n**(iv)**\nhow to appeal a decision of the online marketplace to take an action in response to a user report or for a violation of the terms of service or consumer protection policy; and\n**(v)**\nthe policy regarding refunds, repairs, replacements, or other remedies as a result of a user report or a violation of the terms of service or consumer protection policy.\n##### (c) Standard short-Form statements and graphic icons for consumer protection practices\n**(1) Study and report**\nNot later than 180 days after the date of the enactment of this Act, the Commission shall conduct a study to determine the most effective method of communicating common consumer protection practices in short-form consumer disclosure statements or graphic icons that disclose the consumer protection and content moderation practices of social media platforms and online marketplaces. The Commission shall submit a report to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate with the results of the study. The report shall also be made publicly available on the website of the Commission.\n**(2) Regulations**\nExcept as provided in paragraph (3), after completion of the study and not later than 1 year after the date of the enactment of this Act, the Commission shall finalize regulations based on the results of such study that require social media platforms and online marketplaces to communicate their consumer protection and content moderation practices, and any other information as the Commission may determine, in a clear and conspicuous manner.\n**(3) Exception**\nIf the Commission determines, by a majority vote of the Commissioners, that short-form consumer disclosure statements or graphic icons will not advance consumer understanding of consumer protection and content moderation practices of social media platforms and online marketplaces, the Commission shall include its reasoning for making that determination in the report to Congress required by paragraph (1) and shall not finalize the rulemaking until it determines such rules would advance consumer understanding of consumer protection and content moderation practices of social media platforms and online marketplaces.\n#### 3. Consumer protection program\n##### (a) In general\nEach social media platform and online marketplace shall establish and implement a consumer protection program that includes policies, practices, and procedures regarding consumer protection and content moderation\u2014\n**(1)**\nto\u2014\n**(A)**\nensure compliance with applicable Federal, State, and local consumer protection laws;\n**(B)**\ndevelop, implement, and ensure compliance with the terms of service required by section 2;\n**(C)**\ndevelop and implement policies regarding the content and behavior permitted on its service both by the platform and users, and ensure compliance with such policies, practices and procedures;\n**(D)**\nmitigate risks that could be harmful to consumers\u2019 safety, well-being, and reasonable expectations of users of the social media platform or online marketplace, including cyber harassment;\n**(E)**\nimplement reasonable safeguards within, and training and education of employees and contractors of, the social media platform or online marketplace to promote compliance with all consumer protection laws and the consumer protection program; and\n**(F)**\ndisclose any other requirement the Commission deems appropriate; and\n**(2)**\ntaking into consideration\u2014\n**(A)**\nthe size of, and the nature, scope, and complexity of the activities engaged in by the social media platform and online marketplace;\n**(B)**\nthe activities engaged in by users on the social media platform or online marketplace; and\n**(C)**\nthe cost of implementing the program.\n##### (b) Additional requirements\nAs part of the consumer protection program, a social media platform or online marketplace shall\u2014\n**(1)**\nestablish processes to monitor, manage, and enforce the social media platform\u2019s or online marketplace\u2019s consumer protection program, and demonstrate the covered entity\u2019s compliance with Federal, State, and local consumer protection laws;\n**(2)**\nestablish processes to assess and mitigate the risks to individuals resulting from the social media platform\u2019s or online marketplace\u2019s amplification of content or products not in compliance with its terms of service;\n**(3)**\nestablish a process to periodically review and update the consumer protection program;\n**(4)**\nappoint a consumer protection officer, who reports directly to the chief executive officer; and\n**(5)**\nestablish and implement controls to monitor and mitigate known or reasonably foreseeable risks to consumers resulting from hosting content or products.\n##### (c) Annual filings to the FTC\n**(1) Filing requirements**\nEach social media platform or online marketplace that either has annual revenue in excess of $250,000 in the prior year or that has more than 10,000 monthly active users on average in the prior year, shall be required to submit to the Commission, on an annual basis, a filing that includes\u2014\n**(A)**\na detailed and granular description of each of the requirements in section 2 and this section;\n**(B)**\nthe name and contact information of the consumer protection officer required under subsection (b)(4); and\n**(C)**\na description of any material changes in the consumer protection program or the terms of service since the most recent prior disclosure to the Commission.\n**(2) Officer certification**\nFor each entity that submits an annual filing under paragraph (1), the entity\u2019s principal executive officer and the consumer protection officer required under subsection (b)(4), shall be required to certify in each such annual filing that\u2014\n**(A)**\nthe signing officer has reviewed the filing;\n**(B)**\nbased on such officer\u2019s knowledge, the filing does not contain any untrue statement of a material fact or omit to state a material fact necessary to make the statements, in light of the circumstances under which such statements were made, not misleading;\n**(C)**\nbased on such officer\u2019s knowledge, the filing fairly presents in all material respects the consumer protection practices of the social media platform or online marketplace; and\n**(D)**\nthe signing consumer protection officer\u2014\n**(i)**\nis responsible for establishing and maintaining safeguards and controls to protect consumers and administer the consumer protection program; and\n**(ii)**\nhas provided all material conclusions about the effectiveness of such safeguards and controls.\n**(3) Public availability**\nThe Commission shall make publicly available on the website of the Commission the filings submitted under paragraph (1). The Commission may withhold information included in such a filing if the Commission determines such information should not be public. If the Commission withholds any information, the Commission shall make publicly available on the website the category of information withheld and the reasons for withholding it.\n#### 4. Enforcement\n##### (a) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nAny violation of this Act shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (b) Regulations\nThe Commission shall promulgate regulations under section 553 of title 5, United States Code, to carry out the purposes of this Act.\n##### (c) Private right of action\n**(1) Enforcement by individuals**\n**(A) In general**\nAn individual alleging damages as a result of a violation of this Act may bring a civil action in any court of competent jurisdiction, State or Federal.\n**(B) Relief**\nIn a civil action brought under subparagraph (A) in which the plaintiff prevails, the court may award\u2014\n**(i)**\ndamages as provided in subparagraph (C);\n**(ii)**\nreasonable attorney\u2019s fees and litigation costs; and\n**(iii)**\nany other relief, including equitable or declaratory relief, that the court determines appropriate.\n**(C) Damages**\nA prevailing plaintiff is entitled to actual damages as a result of the violation of this Act.\n**(2) Invalidity of pre-dispute arbitration agreements and pre-dispute joint-action waivers**\n**(A) In general**\nNotwithstanding any other provision of law, no pre-dispute arbitration agreement or pre-dispute joint-action waiver shall be valid or enforceable with respect to a dispute arising under this Act.\n**(B) Applicability**\nAny determination as to whether or how this paragraph applies to any dispute shall be made by a court, rather than an arbitrator, without regard to whether such agreement purports to delegate such determination to an arbitrator.\n**(C) Definitions**\nIn this paragraph:\n**(i) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means any agreement to arbitrate a dispute that has not arisen at the time of making the agreement.\n**(ii) Pre-dispute joint-action waiver**\nThe term pre-dispute joint-action waiver means an agreement, whether or not part of a pre-dispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administration, or other forum, concerning a dispute that has not yet arisen at the time of making the agreement.\n**(iii) Dispute**\nThe term dispute means any claim related to an alleged violation of this Act and between an individual and a covered organization.\n##### (d) Enforcement by State attorneys general\n**(1) In general**\nIf the chief law enforcement officer of a State, or an official or agency designated by a State, has reason to believe that any person has violated or is violating this Act, the attorney general, official, or agency of the State, in addition to any authority it may have to bring an action in State court under its consumer protection law, may bring a civil action in any appropriate United States district court or in any other court of competent jurisdiction, including a State court, to\u2014\n**(A)**\nenjoin further such violation by such person;\n**(B)**\nenforce compliance with this Act;\n**(C)**\nobtain civil penalties; and\n**(D)**\nobtain damages, restitution, or other compensation on behalf of residents of the State.\n**(2) Notice and intervention by the FTC**\nThe attorney general of a State shall provide prior written notice of any action under paragraph (1) to the Commission and provide the Commission with a copy of the complaint in the action, except in any case in which such prior notice is not feasible, in which case the attorney general shall serve such notice immediately upon instituting such action. The Commission shall have the right\u2014\n**(A)**\nto intervene in the action;\n**(B)**\nupon so intervening, to be heard on all matters arising therein; and\n**(C)**\nto file petitions for appeal.\n**(3) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for violation of this Act, no State attorney general, or official or agency of a State, may bring an action under this subsection during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this Act alleged in the complaint.\n**(4) Relationship with State-law claims**\nIf the attorney general of a State has authority to bring an action under State law directed at acts or practices that also violate this Act, the attorney general may assert the State-law claim and a claim under this Act in the same civil action.\n#### 5. Relationship to other laws\n##### (a) Effect of other laws\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) shall not apply to any violation of this Act.\n##### (b) Effect on State laws\nNothing in this Act or any regulation promulgated under this Act shall preempt or otherwise affect any State or local law.\n##### (c) Severability\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act and the application of such provision to other persons not similarly situated or to other circumstances shall not be affected by the invalidation.\n#### 6. FTC enforcement authority\n##### (a) In general\nSection 230(e) of the Communications Act of 1934 ( 47 U.S.C. 230(e) ) is amended by adding at the end the following:\n(6) No effect on FTC enforcement Nothing in this section shall be construed to impair the enforcement by the Federal Trade Commission of any provision of law enforced by the Federal Trade Commission. .\n##### (b) Applicability\nThe amendment made by this section shall apply with respect to any action or proceeding that is commenced on or after the date of the enactment of this Act.\n#### 7. Definitions\nAs used in this Act, the following definitions apply:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Consumer product**\nThe term consumer product has the meaning given such term in section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ).\n**(3) Cyber harassment**\nThe term cyber harassment means electronic communication that harasses, torments, threatens, or terrorizes a target.\n**(4) Online marketplace**\nThe term online marketplace means a website or web application, that\u2014\n**(A)**\nincludes features that allow for, facilitate, or enable third-party sellers to engage in the sale, purchase, payment, storage, shipping, or delivery of a consumer product in the United States; and\n**(B)**\nhosts one or more third-party sellers.\n**(5) Seller**\nThe term seller means a person or entity that sells, offers to sell, or contracts to sell a consumer product through an online marketplace\u2019s platform.\n**(6) Social media platform**\nThe term social media platform means a website or mobile web application that\u2014\n**(A)**\npermits a person to become a registered user, establish an account, or create a profile for the purpose of allowing the user to create, share, and view user-generated content through such an account or profile;\n**(B)**\nenables one or more users to generate content that can be viewed by other users of the platform; and\n**(C)**\nprimarily serves as a medium for users to interact with content generated by other users of the medium and for the platform to deliver ads to users.\n**(7) User**\nThe term user means a person or entity that uses a social media platform or online marketplace for any purpose, including advertisers and sellers, regardless of whether that person has an account or is otherwise registered with the platform.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-27T15:41:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2889",
          "measure-number": "2889",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2889v00",
            "update-date": "2026-05-14"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Online Consumer Protection Act</strong></p><p>This bill requires social media platforms and online marketplaces to establish, maintain, and disclose\u00a0terms of service that include a consumer protection policy.</p><p>The terms must\u00a0cover issues such as payment methods, content ownership, and policies related to sharing user content with third parties.</p><p>Further, the consumer protection policy must address what content or products are permitted on the platform or marketplace and how content or products may be blocked, removed, or modified.\u00a0The policy for social media platforms\u00a0also must describe the tools and support available to users who have experienced cyber harassment.</p><p>Social media platforms and online marketplaces must develop and implement a consumer protection program to maintain compliance with the terms of service, consumer protection policies,\u00a0and consumer protection laws. Platforms and marketplaces\u00a0with annual revenues\u00a0that\u00a0exceeded $250,000 in the prior year\u00a0or more than 10,000 active monthly\u00a0users on average in the prior year also must submit to the Federal Trade Commission annual filings with respect to the requirements of this bill.</p><p>The bill provides for enforcement by the commission, state attorneys general, and private civil action.</p>"
        },
        "title": "Online Consumer Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2889.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Online Consumer Protection Act</strong></p><p>This bill requires social media platforms and online marketplaces to establish, maintain, and disclose\u00a0terms of service that include a consumer protection policy.</p><p>The terms must\u00a0cover issues such as payment methods, content ownership, and policies related to sharing user content with third parties.</p><p>Further, the consumer protection policy must address what content or products are permitted on the platform or marketplace and how content or products may be blocked, removed, or modified.\u00a0The policy for social media platforms\u00a0also must describe the tools and support available to users who have experienced cyber harassment.</p><p>Social media platforms and online marketplaces must develop and implement a consumer protection program to maintain compliance with the terms of service, consumer protection policies,\u00a0and consumer protection laws. Platforms and marketplaces\u00a0with annual revenues\u00a0that\u00a0exceeded $250,000 in the prior year\u00a0or more than 10,000 active monthly\u00a0users on average in the prior year also must submit to the Federal Trade Commission annual filings with respect to the requirements of this bill.</p><p>The bill provides for enforcement by the commission, state attorneys general, and private civil action.</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119hr2889"
    },
    "title": "Online Consumer Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Online Consumer Protection Act</strong></p><p>This bill requires social media platforms and online marketplaces to establish, maintain, and disclose\u00a0terms of service that include a consumer protection policy.</p><p>The terms must\u00a0cover issues such as payment methods, content ownership, and policies related to sharing user content with third parties.</p><p>Further, the consumer protection policy must address what content or products are permitted on the platform or marketplace and how content or products may be blocked, removed, or modified.\u00a0The policy for social media platforms\u00a0also must describe the tools and support available to users who have experienced cyber harassment.</p><p>Social media platforms and online marketplaces must develop and implement a consumer protection program to maintain compliance with the terms of service, consumer protection policies,\u00a0and consumer protection laws. Platforms and marketplaces\u00a0with annual revenues\u00a0that\u00a0exceeded $250,000 in the prior year\u00a0or more than 10,000 active monthly\u00a0users on average in the prior year also must submit to the Federal Trade Commission annual filings with respect to the requirements of this bill.</p><p>The bill provides for enforcement by the commission, state attorneys general, and private civil action.</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119hr2889"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2889ih.xml"
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
      "title": "Online Consumer Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-30T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Online Consumer Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify that a violation of certain terms of service and related materials is an unfair or deceptive act or practice and subject to enforcement by the Federal Trade Commission.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T03:48:19Z"
    }
  ]
}
```
