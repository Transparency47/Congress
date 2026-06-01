# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4159?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4159
- Title: Sammy’s Law
- Congress: 119
- Bill type: S
- Bill number: 4159
- Origin chamber: Senate
- Introduced date: 2026-03-20
- Update date: 2026-04-01T14:01:30Z
- Update date including text: 2026-04-01T14:01:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-20: Introduced in Senate
- 2026-03-20 - IntroReferral: Introduced in Senate
- 2026-03-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-20: Introduced in Senate

## Actions

- 2026-03-20 - IntroReferral: Introduced in Senate
- 2026-03-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-20",
    "latestAction": {
      "actionDate": "2026-03-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4159",
    "number": "4159",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Sammy\u2019s Law",
    "type": "S",
    "updateDate": "2026-04-01T14:01:30Z",
    "updateDateIncludingText": "2026-04-01T14:01:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-20",
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
      "actionDate": "2026-03-20",
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
          "date": "2026-03-20T18:54:18Z",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
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
      "sponsorshipDate": "2026-03-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4159is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4159\nIN THE SENATE OF THE UNITED STATES\nMarch 20, 2026 Mr. Husted (for himself, Mrs. Britt , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces, through which a child or a parent may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on the large social media platform in the same manner as is available to the child, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Sammy\u2019s Law .\n#### 2. Definitions\nIn this Act:\n**(1) Child**\nThe term child means any individual who\u2014\n**(A)**\nhas not attained 17 years of age; and\n**(B)**\nhas registered an account with a large social media platform.\n**(2) Commerce**\nThe term commerce has the meaning given such term in section 4 of the Federal Trade Commission Act ( 15 U.S.C. 44 ).\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Covered nation**\nThe term covered nation has the meaning given such term in section 4872(f) of title 10, United States Code.\n**(5) Large social media platform**\nThe term large social media platform \u2014\n**(A)**\nmeans a service\u2014\n**(i)**\nprovided through an internet website or a mobile application;\n**(ii)**\nthe terms of service of which do not prohibit the use of the service by a child;\n**(iii)**\nwith any feature that enables a child to share images, text, or video through the internet with other users of the service whom such child has met, identified, or become aware of solely through the use of the service; and\n**(iv)**\nthat has more than 100,000,000 monthly global active users or generates more than $1,000,000,000 in gross revenue per year, adjusted yearly for inflation; and\n**(B)**\ndoes not include\u2014\n**(i)**\na service that primarily serves\u2014\n**(I)**\nto facilitate\u2014\n**(aa)**\nthe sale or provision of a professional service; or\n**(bb)**\nthe sale of a commercial product; or\n**(II)**\nto provide news or information in a manner in which a user of the service may not send any content directly to a child through such service; or\n**(ii)**\na service that\u2014\n**(I)**\nhas a feature that enables a user who communicates directly with a child through a message (including images, text, audio, or video messages) to add to such message other users that such child may have met, identified, or become aware of solely through the use of the service; and\n**(II)**\ndoes not have any feature described in subparagraph (A)(iii).\n**(6) Large social media platform provider**\nThe term large social media platform provider means any person who, for commercial purposes in or affecting commerce, provides, manages, operates, owns, or controls a large social media platform.\n**(7) Parent**\nThe term parent means, with respect to a child, the parent or legal guardian of such child.\n**(8) Sale**\nThe term sale , with respect to user data\u2014\n**(A)**\nmeans the exchange of user data for monetary consideration; and\n**(B)**\ndoes not include the disclosure of user data by a third-party safety software provider to a processor or service provider that processes user data on behalf of the third-party safety software provider.\n**(9) State**\nThe term State means each of the 50 States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(10) Third-party safety software provider**\nThe term third-party safety software provider means any person who, for commercial purposes in or affecting commerce\u2014\n**(A)**\nis authorized to interact with a relevant large social media platform to manage the online interactions, content, or account settings of a child for the sole purpose of protecting the child from harm, including physical or emotional harm; and\n**(B)**\nhas received such authorization from the child, or in the case of a child who has not attained 13 years of age, the parent of such child.\n**(11) User data**\nThe term user data means any information reasonably necessary for a user to have a profile or submit content on a large social media platform (including any image, text, audio, or video) that is created by or sent to a child through the account of the child on such platform, but only\u2014\n**(A)**\nif the information or content is created by or sent to the child while a delegation under section 3(a)(1)(A) is in effect with respect to the account; and\n**(B)**\nduring a 30-day period beginning on the date on which the information or content is created by or sent to such child.\n#### 3. Providing access to third-party safety software providers\n##### (a) Obligations of large social media platform providers\n**(1) Availability of application programming interfaces**\n**(A) In general**\nNot later than the date described in subparagraph (B), a large social media platform provider shall create, maintain, and make available to a third-party safety software provider registered with the Commission under subsection (b)(3) a set of third-party-accessible real-time application programming interfaces, including any information necessary to use such interfaces, by which a child (or, in the case of a child who has not attained 13 years of age, a parent of the child) may delegate permission to the third-party safety software provider to\u2014\n**(i)**\nmanage any online interaction with or content created by or sent to the child, as well as the account settings of the child on the large social media platform in the same manner as is available to the child; and\n**(ii)**\ninitiate a secure transfer of user data from the large social media platform in a commonly used and machine-readable format to the third-party safety software provider, where the frequency of such transfers may not be limited by the large social media platform provider to less than once per hour.\n**(B) Date described**\nFor purposes of subparagraph (A), the date described in this subparagraph is\u2014\n**(i)**\nin the case of a service that is a large social media platform on the date of enactment of this Act, 180 days after such date; or\n**(ii)**\nin the case of a service that becomes a large social media platform after such date of enactment, not later than 30 days after the date on which such service becomes a large social media platform.\n**(2) Revocation**\nOnce a child or parent makes a delegation under paragraph (1)(A), the large social media platform provider shall make the application programming interfaces and information described in such paragraph available to the relevant third-party safety software provider on an ongoing basis until\u2014\n**(A)**\nthe child or a parent, as applicable, revokes the delegation;\n**(B)**\nthe child or a parent, as applicable, revokes or disables the registration of the account of such child with the large social media platform;\n**(C)**\nthe third-party safety software provider\u2014\n**(i)**\nrejects the delegation;\n**(ii)**\nreceives notice that\u2014\n**(I)**\nthe parent of such child who made the delegation no longer has legal parental rights over such child; or\n**(II)**\na temporary arrangement has been put in place by a court or legal authority regarding the custody of such child; or\n**(iii)**\nis deregistered by the Commission; or\n**(D)**\nthe child attains the age of 17 years old.\n**(3) Data security**\n**(A) In general**\nA large social media platform provider shall establish, implement, and maintain reasonable policies, practices, and procedures to protect\u2014\n**(i)**\nthe confidentiality, integrity, and accessibility of user data transferred from the large social media platform provider to a third-party safety software provider pursuant to a delegation under paragraph (1)(A); and\n**(ii)**\nany such user data against unauthorized access.\n**(B) Scope**\nThe policies, practices, and procedures required by subparagraph (A) shall be\u2014\n**(i)**\nconsistent with state-of-the-art administrative, technical, and physical safeguards for protecting transferred user data; and\n**(ii)**\nappropriate to the nature, scope, and volume of such user data.\n**(4) Disclosure**\nIn the case of a delegation made by a child or a parent, as applicable, under paragraph (1)(A), with respect to the account of such child with a large social media platform, the large social media platform provider shall\u2014\n**(A)**\ndisclose to such child or parent, as applicable, such delegation;\n**(B)**\nprovide to such child or parent, as applicable, a summary of any user data transferred to a third-party safety software provider; and\n**(C)**\nupdate such summary as necessary to reflect any change to such user data.\n**(5) Limitation**\nAny management by a third-party safety software provider pursuant to paragraph (1)(A)(i) shall be limited to such management that protects a child from harm, including any such management related to the optimization of any privacy setting on an account of the child, stated user age, and marketing settings for the account.\n**(6) User control**\n**(A) In general**\nIf a large social media platform uses a messaging feature or service that provides security features that give a user control over access to the content of any communication of the user in a manner that renders the access of the large social media platform to such content technically infeasible without overriding such control, then the following shall apply:\n**(i)**\nThe large social media platform may not be required to grant a third-party safety software provider access to such content through a set of third-party-accessible real-time application programming interfaces under paragraph (1)(A).\n**(ii)**\nThe large social media platform, upon a delegation under paragraph (1)(A), shall\u2014\n**(I)**\nmake available and maintain a technical interface that enables contemporaneous transmission of such communication to a third-party safety software provider\u2014\n**(aa)**\nregistered under subsection (b)(3); and\n**(bb)**\nselected by the child or parent, as applicable, as a user-designated recipient;\n**(II)**\nmaintain such security features without altering, bypassing, or overriding such features;\n**(III)**\npermit the communicating users (and any user-designated recipient) to access the content through such interface; and\n**(IV)**\nnot gain access to the content of such communication.\n**(B) Rule of construction**\nNothing in this paragraph may be construed to limit the obligations of a large social media platform under this Act with respect to user data other than the content of communications described in this paragraph.\n##### (b) Third-Party safety software providers\n**(1) Protection of user data**\nA third-party safety software provider shall\u2014\n**(A)**\nlimit any collection, maintenance, and processing of user data the third-party safety software provider obtains pursuant to this Act to what is adequate, relevant, and reasonably necessary for the purposes for which the user data is collected, maintained, or processed, or disclosed to a parent under subsection (d)(1)(C);\n**(B)**\nestablish, implement, and maintain reasonable policies, practices, and procedures (that are consistent with state-of-the-art administrative, technical, and physical safeguards related to protecting transferred user data and appropriate to the nature, scope, and volume of such user data) to protect\u2014\n**(i)**\nthe confidentiality, integrity, and accessibility of the user data received from a large social media platform pursuant to this Act; and\n**(ii)**\nthe user data received from a large social media platform pursuant to this Act against unauthorized access; and\n**(C)**\nupon any revocation described in subsection (a)(2), delete the user data of the child within 5 days.\n**(2) Prohibition on sale**\nA third-party safety software provider may not sell any user data collected, maintained, or processed pursuant to this Act.\n**(3) Registration with the Commission**\nA third-party safety software provider shall register with the Commission as a condition of accessing an application programming interface and any information under subsection (a). In order to complete such registration, the third-party safety software provider shall demonstrate the following to the satisfaction of the Commission:\n**(A)**\nThe third-party safety software provider is not operated, directly or indirectly (including through a parent company, subsidiary, or affiliate), by a company operated or controlled by a covered nation.\n**(B)**\nSuch software provider will collect, process, maintain, or otherwise use any user data obtained under subsection (a) for the sole purpose of protecting a child from harm in accordance with any applicable terms of service and the provisions of this Act.\n**(C)**\nSuch software provider will only disclose user data obtained under subsection (a) as permitted by subsection (d).\n**(D)**\nSuch software provider will not sell, disclose, process, store, transfer, or otherwise make available user data obtained under this Act to a government of a covered nation or to a company operated or controlled by a covered nation.\n**(E)**\n**(i)**\nSuch software provider will delete any user data obtained under this Act as soon as possible\u2014\n**(I)**\nbut not later than 5 days after receiving such data from a large social media platform; and\n**(II)**\nnot including any data the software provider discloses under subsection (d).\n**(ii)**\nFor any data disclosed under subsection (d)(1)(C), such software provider will maintain such data until\u2014\n**(I)**\nthe child or parent who made a delegation under subsection (a)(1)(A), and whose data is at issue, requests that the third-party safety software provider delete such data;\n**(II)**\nthe child attains 17 years of age; or\n**(III)**\nthe third-party safety software provider is deregistered by the Commission.\n**(iii)**\nIn the event that the child or parent who made a delegation under subsection (a)(1)(A) revokes the delegation, such software provider will delete all applicable user data not later than 15 days after the date of such revocation.\n**(F)**\nSuch software provider will disclose, in an easy-to-understand, human-readable format, to each child with respect to whose account with a large social media platform the service of the third-party safety software provider is operating and (if a parent made the delegation under subsection (a)(1)(A) with respect to the account) to the parent, sufficient information detailing the operation of the service and what information the software provider is collecting to enable such child or parent, as applicable, to make informed decisions regarding the use of the service.\n**(G)**\nSuch software provider will disclose, in an easy-to-understand format to each child or parent who made a delegation under subsection (a)(1)(A) notice of any material changes in how the third-party safety software provider provides services.\n**(H)**\nSuch software provider is able to provide services in accordance with any applicable terms of service and any relevant disclosures made to any consumer, including by ensuring such terms and disclosures are clear and conspicuous and are written in plain and easy-to-understand English.\n**(I)**\nSuch software provider has established, implemented, and maintained reasonable policies, practices, and procedures to protect the confidentiality, integrity, and accessibility of any user data collected or processed pursuant to this Act and that the policies, practices, and procedures are appropriate to ensure a level of security appropriate to the risk to such user data, the cost of implementing such policies, practices, and procedures, and the nature, scope, and volume of such user data.\n**(J)**\nSuch software provider assesses compliance with applicable Federal law, including the requirements of this Act.\n**(K)**\nSuch software provider is in compliance with the requirements of this Act.\n**(4) Annual audit**\n**(A) Audit process; audit report**\nFor each year or partial year during which a third-party safety software provider is registered with the Commission under paragraph (3), the third-party safety software provider shall retain the services of a qualified independent auditing firm to complete an annual audit and write an audit report (which shall be exempt from disclosure under section 552(b)(3) of title 5, United States Code) that includes\u2014\n**(i)**\na review and assessment of such registration and any subsequent written reports, including whether the third-party safety software provider has remained in compliance with the conditions described in paragraph (3); and\n**(ii)**\nan identification of whether the third-party safety software provider has made any material changes in how the third-party safety software provider provides services, and in the event of any such material changes\u2014\n**(I)**\nan explanation as to how such changes have impacted users; and\n**(II)**\nany information relating to whether such users were notified of the material change at the time the material change was implemented.\n**(B) Submission to the Commission**\nNot later than 30 days after the date on which an audit report is written under subparagraph (A), a third-party safety software provider shall submit to the Commission\u2014\n**(i)**\na full copy of such audit report; and\n**(ii)**\na summary of such audit report that may contain redactions to protect the confidential business information and trade secrets of the third-party safety software provider.\n**(C) Audit review by the Commission**\nThe Commission shall\u2014\n**(i)**\nreview each audit report submitted by a third-party safety software provider under subparagraph (B)(i) to verify compliance with the requirements of this Act;\n**(ii)**\nmake a copy of the summary of such audit report submitted under subparagraph (B)(ii) available to the public; and\n**(iii)**\nin the event an audit required under subparagraph (A) detects an unusual finding, and prior to any adverse action taken by the Commission under paragraph (5), direct a third-party safety software provider to promptly investigate and resolve the matter.\n**(5) Additional oversight of third-party safety software providers**\nIn addition to the jurisdiction, powers, and duties of the Commission otherwise provided under this Act and any other provision of law, the Commission may take an adverse action against a third-party safety software provider, including by\u2014\n**(A)**\ndenying registration of the third-party safety software provider under paragraph (3);\n**(B)**\npermanently deregistering the third-party safety software provider; and\n**(C)**\nsuspending the registration of the third-party safety software provider due to a finding by the Commission of a material risk to the security of the data or safety of the public, including for\u2014\n**(i)**\nwillful misconduct or gross negligence by the third-party safety software provider;\n**(ii)**\na material misrepresentation made by a third-party safety software provider to the Commission or to any consumer;\n**(iii)**\nfailure by the third-party safety software provider to comply with any requirements of this Act or failure to operate in accordance with the affirmations, assertions, representations, or terms of any security review, audit, terms of services, or consumer disclosures; or\n**(iv)**\nfailure by the third-party safety software provider to respond to an unusual finding in an annual audit completed under paragraph (4).\n**(6) Rights of third-party safety software providers**\n**(A) In general**\nIn the event the Commission takes an adverse action against a third-party safety software provider under paragraph (5), the Commission shall give the third-party safety software provider the opportunity to\u2014\n**(i)**\nappeal such adverse action; and\n**(ii)**\nremediate any deficiency described in an annual audit completed under paragraph (4) within 45 days (if the third-party safety software provider demonstrates the third-party safety software provider has remediated any such deficiency and has taken satisfactory action to ensure such deficiency shall not reoccur), except in the case of a finding of\u2014\n**(I)**\nwillful misconduct;\n**(II)**\ngross negligence; or\n**(III)**\na demonstrated history of multiple failures in relation to the types of material risk described in paragraph (5)(C).\n**(B) Exception**\nThe rights described in subparagraph (A) shall not prevent the Commission from suspending the registration of a third-party safety software provider to protect the public from ongoing material risk for the period during which the third-party safety software provider is in the process of exercising such rights.\n##### (c) Indemnification\nIn any civil action in Federal or State court (other than an action brought by the Commission), a large social media platform provider may not be held liable for damages arising from transferring user data to a third-party safety software provider under subsection (a) if the large social media platform provider has complied with the requirements of this Act in good faith.\n##### (d) User data disclosure\n**(1) Permitted disclosures**\nA third-party safety software provider may not disclose any user data obtained under subsection (a) to any other person, except\u2014\n**(A)**\npursuant to a lawful request from a government body, including for law enforcement purposes or for judicial or administrative proceedings, by means of a court order or a court-ordered warrant, a subpoena or summons issued by a judicial officer, or a grand jury subpoena;\n**(B)**\nto the extent that such disclosure is required by law and such disclosure complies with and is limited to the relevant requirements of such law;\n**(C)**\nto a child who made a delegation under subsection (a)(1)(A) and whose data is at issue, the parent of such child, or to a parent who made such a delegation and whose child's data is at issue, with such third-party safety software provider making a good faith effort to ensure that such disclosure includes only the user data necessary for a reasonable parent to understand that such child is experiencing (or is at foreseeable risk to experience)\u2014\n**(i)**\nsuicide;\n**(ii)**\nanxiety;\n**(iii)**\ndepression;\n**(iv)**\nan eating disorder;\n**(v)**\nviolence, including being the victim of or planning to commit or facilitate assault;\n**(vi)**\nsubstance abuse;\n**(vii)**\nfraud;\n**(viii)**\nsevere forms of trafficking in persons (as defined in section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ));\n**(ix)**\nsexual abuse;\n**(x)**\nphysical injury;\n**(xi)**\nharassment;\n**(xii)**\nsexually explicit conduct or child pornography (as such terms are defined in section 2256 of title 18, United States Code);\n**(xiii)**\nterrorism (as defined in section 140(d) of the Foreign Relations Authorization Act, Fiscal Years 1988 and 1989 ( 22 U.S.C. 2656f(d) )), including communications with or in support of a foreign terrorist organization (as designated by the Secretary of State under section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) )); or\n**(xiv)**\nthe sharing of personal information, limited to\u2014\n**(I)**\nhome address;\n**(II)**\nphone number;\n**(III)**\nsocial security number; and\n**(IV)**\npersonal banking information;\n**(D)**\nin the case of a good faith determination that disclosure is necessary to prevent or lessen a reasonably foreseeable serious and imminent threat to the health or safety of any individual, if the disclosure is made to a person reasonably able to prevent or lessen the threat; or\n**(E)**\nto a public health authority or other appropriate government authority authorized by law to receive reports of child abuse or neglect.\n**(2) Disclosure reporting**\nA third-party safety software provider that makes a disclosure permitted by subparagraphs (A), (B), (D), or (E) of paragraph (1) shall promptly inform the child or parent who made a delegation under subsection (a)(1)(A) that such a disclosure has been or will be made, except if the third-party safety software provider\u2014\n**(A)**\nin the exercise of professional judgment, determines informing such child or parent would place such child at risk of serious harm; or\n**(B)**\nis prohibited by law (including through a valid order by a court or administrative body) from informing such child or parent.\n**(3) Child exploitation**\nNothing in this Act shall be construed to relieve a third-party safety software provider or a large social media platform from their duty to report pursuant to section 2258A of title 18, United States Code.\n#### 4. Implementation and enforcement\n##### (a) Enforcement\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Preservation of authority**\nNothing in this Act may be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Compliance assessment\nThe Commission, on a biannual basis, shall assess compliance by large social media platform providers with the provisions of this Act.\n##### (c) Complaints\nNot later than 180 days after the date of enactment of this Act, the Commission shall establish procedures under which a child (or the parent of such child), a large social media platform provider, or a third-party safety software provider may file a complaint alleging that a large social media platform provider or a third-party safety software provider has violated this Act.\n#### 5. One national standard\n##### (a) In general\nNo State or political subdivision of a State may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of a State, related to requiring large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces for the purposes of child online safety, through which a child or a parent of a child may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on a large social media platform in the same manner as is available to the child.\n##### (b) Rule of construction\nThis section may not be construed to\u2014\n**(1)**\nlimit the enforcement of any consumer protection law of general applicability of a State or political subdivision of a State;\n**(2)**\npreempt the applicability of State trespass, contract, or tort law; or\n**(3)**\npreempt the applicability of any State law to the extent that the law relates to acts of fraud, unauthorized access to personal information, or notification of unauthorized access to personal information.",
      "versionDate": "2026-03-20",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-01T14:01:30Z"
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
      "date": "2026-03-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4159is.xml"
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
      "title": "Sammy\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sammy\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require large social media platform providers to create, maintain, and make available to third-party safety software providers a set of real-time application programming interfaces, through which a child or a parent may delegate permission to a third-party safety software provider to manage the online interactions, content, and account settings of such child on the large scale social media platform in the same manner as is available to the child, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:32Z"
    }
  ]
}
```
