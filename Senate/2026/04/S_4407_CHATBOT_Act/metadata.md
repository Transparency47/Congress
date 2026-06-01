# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4407
- Title: CHATBOT Act
- Congress: 119
- Bill type: S
- Bill number: 4407
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-18T20:16:39Z
- Update date including text: 2026-05-18T20:16:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4407",
    "number": "4407",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "CHATBOT Act",
    "type": "S",
    "updateDate": "2026-05-18T20:16:39Z",
    "updateDateIncludingText": "2026-05-18T20:16:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T19:39:33Z",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "HI"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "UT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4407is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4407\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Cruz (for himself, Mr. Schatz , Mr. Curtis , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the creation of family accounts for children to be able to use artificial intelligence chatbots, to require verifiable parental consent for teens using artificial intelligence chatbots, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Children\u2019s Health, Advancement, Trust, Boundaries, and Oversight in Technology Act or the CHATBOT Act .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Artificial intelligence chatbot**\nThe term artificial intelligence chatbot means artificial intelligence that, in an open-ended natural-language or multimodal manner\u2014\n**(A)**\naccepts user input;\n**(B)**\nengages in interactive conversations with a user; and\n**(C)**\nprovides outputs that are not\u2014\n**(i)**\npre-determined or scripted;\n**(ii)**\nlimited to contextualized replies or to a narrow, specified purpose, such as\u2014\n**(I)**\ncustomer service;\n**(II)**\nany operational purpose of a business;\n**(III)**\nproductivity and analysis related to source information;\n**(IV)**\ninternal research; or\n**(V)**\ntechnical assistance; or\n**(iii)**\nlimited to an educational product or service that primarily provides information, experience, training, or instruction for the purpose of building any knowledge, skill, or craft.\n**(3) Child**\nThe term child means an individual who is under the age of 13.\n**(4) Commission**\nThe term Commission means the Federal Trade Commission.\n**(5) Covered entity**\nThe term covered entity means any public-facing website, online service, or software application that, as its primary function, provides an artificial intelligence chatbot to users.\n**(6) Know**\nThe term know means to have actual knowledge or knowledge fairly implied on the basis of objective circumstances.\n**(7) Parent**\nWith respect to a child or teen, the term parent includes a legal guardian of the child or teen.\n**(8) Personal data**\nThe term personal data has the meaning given the term personal information in section 1302 of the Children's Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ).\n**(9) Targeted advertising**\nThe term targeted advertising \u2014\n**(A)**\nmeans advertising or any other effort to market a product or service to a child or teen user based on any personal data collected from the child or teen; and\n**(B)**\ndoes not include\u2014\n**(i)**\nadvertising or marketing to a child or teen user in response to the most recent prompt input by the child or teen user;\n**(ii)**\ncontextual advertising, such as when an advertisement is displayed to a child based on the content of the website, online service, or software application of a covered entity in which the advertisement appears and does not vary based on the personal data of the child or teen user; or\n**(iii)**\nprocessing personal data solely for the purpose of measuring or reporting advertising or content performance, reach, or frequency, including independent measurement.\n**(10) Teen**\nThe term teen means an individual who has attained 13 years of age but has not attained 18 years of age.\n**(11) Transparency label**\nThe term transparency label means a notice that\u2014\n**(A)**\nis clearly and conspicuously displayed to a user;\n**(B)**\ndisappears only if the user\u2014\n**(i)**\nexits the artificial intelligence chatbot; or\n**(ii)**\naffirmatively dismisses the notice; and\n**(C)**\ndiscloses that\u2014\n**(i)**\nthe artificial intelligence chatbot is artificial intelligence and not a natural person; and\n**(ii)**\nany output of the artificial intelligence chatbot is generated using artificial intelligence.\n**(12) User**\nThe term user means, with respect to a covered entity, an individual who registers an account or creates a profile in order to access the artificial intelligence chatbot of the covered entity.\n#### 3. Family account requirement for children; termination of existing user accounts and profiles; deletion of personal data\n##### (a) Creation and maintenance of family accounts\nA covered entity shall require an individual to create and maintain a family account that meets the requirements described in section 5 to access an artificial intelligence chatbot of the covered entity if the covered entity knows such individual is a child.\n##### (b) Termination of existing user accounts and profiles of child and teen users\nA covered entity shall terminate any user account or profile of an artificial intelligence chatbot of the covered entity that exists as of the effective date of this Act if the covered entity knows such user is\u2014\n**(1)**\na child and such child has not created a family account; or\n**(2)**\na teen and the parent of such teen has not provided verifiable parental consent pursuant to section 4(a)(1).\n##### (c) Deletion of personal data of children and teens\n**(1) In general**\nSubject to paragraph (2), upon termination of a user account or profile pursuant to subsection (b), a covered entity shall immediately delete all personal data collected from the user or submitted by the user (including data of the user collected from or submitted by the parent of such user) to the artificial intelligence chatbot of such entity.\n**(2) Access of children and teens to personal data**\nDuring the 90-day period beginning on the date on which a covered entity terminates a user account or profile pursuant to subsection (b), to the extent technically feasible and not in violation of any licensing agreement, the covered entity shall make available to such user or parent of such user, upon request, a copy of the personal data collected from the user or submitted by the user to the artificial chatbot of such entity in\u2014\n**(A)**\na manner that is readable and able to be understood by a reasonable person; and\n**(B)**\na portable, structured, and machine-readable format.\n**(3) Rule of construction**\nNothing in this subsection shall be construed to prohibit a covered entity from retaining\u2014\n**(A)**\na record of the termination of a user account or profile; and\n**(B)**\nthe minimum information necessary for ensuring compliance with this section.\n#### 4. Verifiable parental consent and option for family accounts for teens\n##### (a) In general\n**(1) Notice and verifiable parental consent**\nPrior to an individual's creation of a user account or profile with an artificial intelligence chatbot of a covered entity, if the covered entity knows such individual is a teen, the covered entity shall\u2014\n**(A)**\nprovide direct notice to a parent of the teen of the attempt by such teen to create such user account or profile; and\n**(B)**\nobtain verifiable parental consent (as defined in section 1302(9) of the Children\u2019s Online Privacy Protection Act ( 15 U.S.C. 6501(9) )) from the parent of the teen in order for the teen to create such user account or profile.\n**(2) Option for family accounts**\nIn obtaining verifiable parental consent under paragraph (1), a covered entity shall provide a parent of a teen with the option to create a family account for the teen that meets the requirements described in section 5.\n**(3) Default features**\n**(A) In general**\nSubject to subparagraph (B), if the parent of a teen user does not create a family account for the teen as permitted in paragraph (2), a covered entity shall set and fix any feature or setting described in section (5)(a)(1) at the default setting required by section 5(b)(1) for the user account or profile of such teen.\n**(B) Later creation of a family account**\nIf a parent of a teen user creates a family account for the teen user after such teen user first creates a user account or profile, the covered entity shall permit such parent to adjust any default setting set and fixed under subparagraph (A).\n**(4) Reasonable efforts**\nA covered entity shall be deemed compliant with the requirements of this subsection if the covered entity is in compliance with the requirements of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) to use reasonable efforts (taking into consideration available technology) to provide a parent with direct notice and to obtain verifiable parental consent.\n##### (b) Revocation of consent\n**(1) In general**\nWith respect to a parent of a teen who has provided verifiable parental consent under subsection (a)(1), a covered entity shall provide such parent with the ability to revoke such consent.\n**(2) Effect of verifiable parental consent**\nIf a covered entity receives a revocation of verifiable parental consent under paragraph (1), the covered entity shall suspend, delete, or otherwise disable the user account or profile of the teen on the artificial intelligence chatbot that is subject to such revocation.\n##### (c) Rule of construction\nNothing in this section shall be construed to require a covered entity to require a teen or the parent of such teen to provide government-issued identification for\u2014\n**(1)**\nrelationship verification; or\n**(2)**\nthe provision of verifiable parental consent under subsection (a)(1).\n#### 5. Parental controls and settings for family accounts\n##### (a) Parental controls and settings\nAny family account provided by a covered entity to meet the requirements of section 3 or 4 shall permit the parent of a child or teen user, as applicable, to\u2014\n**(1)**\ndetermine the privacy and account settings for the user account or profile of such child or teen, including the ability to\u2014\n**(A)**\nlimit the amount of time the child or teen is able to spend using the artificial intelligence chatbot of the covered entity;\n**(B)**\ndisable rewards or incentives, including badges or other visual award symbols, based on frequency, time spent, or the activity of the child or teen using the artificial intelligence chatbot;\n**(C)**\ndisable notifications and push alerts;\n**(D)**\ndisable any financial transaction made available while using the artificial intelligence chatbot;\n**(E)**\ndisable the generation of an output from the artificial intelligence chatbot that is not in response to the input of a user; and\n**(F)**\nenable a requirement that the covered entity display a transparency label and set the intervals at which the transparency label should be displayed;\n**(2)**\nset the number of inputs that, or the period of time during which, an artificial intelligence chatbot may use the personal data of, or such inputs provided by, a child or teen user to generate outputs before such data and such inputs must be deleted from any memory used by the artificial intelligence chatbot to generate outputs;\n**(3)**\naccess\u2014\n**(A)**\na full record of the conversations and activity of the child or teen with such artificial intelligence chatbot; and\n**(B)**\nfeatures that allow the parent to monitor, analyze, and understand, at scale, the record of such conversations and activity; and\n**(4)**\nreceive customized notifications or other alerts when the child or teen attempts to bypass, disable, or violate any parental control or setting described in paragraph (1).\n##### (b) Default safeguards and parental control options\n**(1) Default safeguards**\nEach covered entity shall ensure that the default setting of any parental control or setting described in subsection (a) for a family account is the option, or pre-set option (for purposes of paragraph (2)), that provides the most protective level of control with respect to the use of the artificial intelligence chatbot by a child or teen user.\n**(2) Pre-set options for parents**\nEach covered entity shall provide a parent of a child or teen user with the option to select between several pre-set tiered options for governing the settings described in subsection (a)(2) that balance the tradeoffs between the protectiveness to the child or teen user and the effectiveness of the artificial intelligence chatbot.\n##### (c) Disclosure and transparency\n**(1) In general**\nEach covered entity shall ensure that the default setting of any parental control or setting described in subsection (a) within a family account is accompanied by a clear and conspicuous disclosure that defines the scope of the setting in a manner that is understandable by an ordinary consumer.\n**(2) Provision of information**\nPrior to the creation of a family account, a covered entity shall provide to the parent of a child or teen clear and conspicuous information, which may include a link to a web page of the covered entity, regarding\u2014\n**(A)**\nthe policies and practices of the covered entity with respect to each parental control or setting described in subsection (a), including an easy-to-understand explanation of the options described in such subsection, the pre-set options described in subsection (b)(2), and the effect of each option or pre-set option; and\n**(B)**\nhow to access and manage the family account for the child or teen user, including an easy-to-understand explanation of how to view, change, and determine each parental control or setting described in subsection (a).\n##### (d) Report\nA covered entity shall provide an easily accessible means for a child or teen user or the parent of such child or teen user to\u2014\n**(1)**\nreport violations of the parental controls or settings specified in subsection (a); and\n**(2)**\ncontact the covered entity with respect to any matter related to child or teen use of the artificial intelligence chatbot of the covered entity.\n#### 6. Prohibition on targeted advertising\n##### (a) In general\nA covered entity shall not use the personal data of a user that the covered entity knows is a child or teen for purposes of targeted advertising.\n##### (b) Rule of construction\nNothing in subsection (a) shall be construed to prohibit a covered entity that knows the age of the child or teen from delivering advertising or marketing that\u2014\n**(1)**\ncomplies with the prohibition described in subsection (a); and\n**(2)**\nis age-appropriate and intended for a child or teen audience, so long as the covered entity does not use any personal information other than the age of the child or teen to display such advertisement.\n#### 7. Determination of whether a covered entity knows that an individual is a child or teen\n##### (a) Rule of construction\nFor purposes of determining whether a covered entity knows that an individual is a child or teen, the Commission or attorney general of a State shall rely on competent and reliable evidence, taking into account the totality of circumstances, including whether a reasonable and prudent person under the circumstances would have known that the individual is a child or teen.\n##### (b) Protections for privacy\nNothing in this Act, including a determination described in subsection (a), shall be construed to require a covered entity to\u2014\n**(1)**\nimplement an age gating or age verification functionality; or\n**(2)**\naffirmatively collect any personal data with respect to the age of any individual that the covered entity is not already collecting in the normal course of business.\n##### (c) Restriction on use and retention of personal data\nIf a covered entity (or a third party acting on behalf of a covered entity) voluntarily collects personal data for the purpose of complying with this Act, the covered entity (or third party) shall not\u2014\n**(1)**\nuse any personal data collected for a purpose other than for sole compliance with the requirements of this Act; or\n**(2)**\nretain any personal data collected for longer than is necessary to comply with the requirements of this Act or than is minimally necessary to demonstrate such compliance.\n#### 8. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by States\n**(1) Authorization**\nSubject to paragraph (3), in any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of a covered entity in a practice that violates section 3 or 4, the attorney general of the State may, as parens patriae, bring a civil action against the covered entity on behalf of the residents of the State in an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such practice;\n**(B)**\nenforce compliance with this Act;\n**(C)**\non behalf of residents of the State, obtain damages, restitution, or other compensation, each of which shall be distributed in accordance with State law; or\n**(D)**\nobtain such other relief as the court may consider to be appropriate.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (ii), before initiating a civil action under paragraph (1), the attorney general of a State shall provide to the Commission a written notice of such action and a copy of the complaint for such action.\n**(ii) Exception**\nIf the attorney general determines that it is not feasible to provide the notice described in clause (i) before initiating a civil action under paragraph (1), the attorney general shall provide written notice of the action and a copy of the complaint to the Commission immediately upon initiating the civil action.\n**(B) Intervention by the Commission**\nUpon receiving the notice required under subparagraph (A), the Commission may\u2014\n**(i)**\nintervene in the civil action that is the subject of the notice; and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard with respect to any matter that arises in such action; and\n**(II)**\nfile a petition for appeal for any decision in such action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Preemptive action by the Commission**\nIn any case in which an action is instituted by or on behalf of the Commission for a violation of this Act, no State may, during the pendency of that action, institute a separate civil action under paragraph (1) against any defendant named in the complaint in the action instituted by or on behalf of the Commission for that violation.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n#### 9. Relationship to other laws\n##### (a) In general\nSubject to subsection (b), the provisions of this Act shall preempt any related State law, rule, or regulation only to the extent that such State law, rule, or regulation conflicts with a provision of this Act.\n##### (b) Rules of construction\nNothing in this Act shall be construed to\u2014\n**(1)**\nprohibit a State from enacting a law, rule, or regulation that provides greater protection to children than the protections provided in this Act; or\n**(2)**\naffect the application of\u2014\n**(A)**\nsection 444 of the General Education Provisions Act ( 20 U.S.C. 1232g , commonly known as the Family Educational Rights and Privacy Act of 1974 ) or other Federal or State laws governing student privacy; or\n**(B)**\nthe Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) or any rule or regulation promulgated under such Act.\n#### 10. Study on the impact of artificial intelligence chatbots on child and teen human relationships and social needs\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Director of the National Science Foundation shall conduct or commission a study on the effects of artificial intelligence chatbots on human relationships and the social needs of children and teens.\n##### (b) Scope\nThe study required under subsection (a) shall examine, with respect to children and teens\u2014\n**(1)**\nthe use of artificial intelligence chatbots by children and teens to meet companionship or social needs and the resulting effects on the real-world social engagement and mental health of children and teens;\n**(2)**\nthe prevalence and effects of sycophantic or excessively affirming behavior by artificial intelligence chatbots on children and teens; and\n**(3)**\nthe role of design features of artificial intelligence chatbots in shaping the results of paragraphs (1) and (2).\n##### (c) Methodology\nThe study required under subsection (a) shall draw on existing research, expert consultation, and, where feasible, observational, experimental, and survey-based data collection, consistent with applicable ethical standards and requirements for research involving children and teens.\n##### (d) Report\nNot later than 1 year after the date of enactment of this Act, the Director of the National Science Foundation shall submit to the Committee on Commerce, Science and Transportation of the Senate and the Committee on Energy and Commerce and the Committee on Science, Space, and Technology of the House of Representatives a report containing the findings of the study conducted under subsection (a).\n#### 11. GAO report on recommendations and best practices\n##### (a) In general\nNot later than 2 years after the date described in section 12, the Comptroller General of the United States (in this section referred to as the Comptroller General ) shall submit a report to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce and the Committee on Science, Space, and Technology of the House of Representatives that examines\u2014\n**(1)**\nthe effectiveness of this Act, including the overall effectiveness of the family account requirements described in sections 3, 4, and 5;\n**(2)**\nthe adoption rate of family accounts by parents of children and teens;\n**(3)**\nthe rate of compliance with the requirements of this Act by covered entities;\n**(4)**\nthe effectiveness of each parental control or setting required within a family account, including recommendations or best practices to provide the most protective or ideal level of control for children and teens, including analysis of the parental control described in section 5(a)(2), including\u2014\n**(A)**\nusing best available research or industry data; and\n**(B)**\nan analysis of model drift with specific consideration of the number of inputs or the duration of time that causes an artificial intelligence chatbot to generate outputs not consistent with its behavior parameters;\n**(5)**\nrecommendations for parents and covered entities to provide the most protective level of control for children and teens with respect to the use of the parental control described in section 5(a)(2), including recommended settings for limiting the number of inputs or the retention of personal data within the memory of the artificial intelligence chatbot, with reference to the data described in paragraph (4);\n**(6)**\nrecommendations for parents, based on available data, with respect to best practices for maximizing the protection of a child or teen within a family account while ensuring the effectiveness of an artificial intelligence chatbot;\n**(7)**\nrecommendations to the Commission for improving enforcement of this Act; and\n**(8)**\nrecommendations to Congress for potential legislative improvement to this Act.\n##### (b) Consultation requirement\nIn carrying out the report required under subsection (a), the Comptroller General shall consult with each of the following:\n**(1)**\nThe National Institute of Standards and Technology.\n**(2)**\nThe Commission.\n**(3)**\nRepresentatives of covered entities.\n**(4)**\nParents of children or teen users of artificial intelligence chatbots.\n**(5)**\nIndividuals with experience advocating for online child safety, consumer protection, or online privacy.\n**(6)**\nIndividuals with experience in artificial intelligence, computer science, and software engineering.\n**(7)**\nAcademic experts with expertise in prevention of online harms to children or teens.\n**(8)**\nOther relevant Federal agencies with expertise in child or teen online safety.\n#### 12. Effective date\nThis Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-04-28",
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
        "updateDate": "2026-05-18T20:16:39Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4407is.xml"
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
      "title": "CHATBOT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHATBOT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Children\u2019s Health, Advancement, Trust, Boundaries, and Oversight in Technology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the creation of family accounts for children to be able to use artificial intelligence chatbots, to require verifiable parental consent for teens using artificial intelligence chatbots, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:36Z"
    }
  ]
}
```
