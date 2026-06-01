# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/636?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/636
- Title: Public Safety Employer-Employee Cooperation Act
- Congress: 119
- Bill type: S
- Bill number: 636
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2026-05-13T11:03:31Z
- Update date including text: 2026-05-13T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/636",
    "number": "636",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Public Safety Employer-Employee Cooperation Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:31Z",
    "updateDateIncludingText": "2026-05-13T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-19",
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
            "date": "2025-02-19T21:06:51Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-19T21:06:51Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s636is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 636\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Mr. Hickenlooper (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide collective bargaining rights for public safety officers employed by States or their political subdivisions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Safety Employer-Employee Cooperation Act .\n#### 2. Purpose and policy\nCongress declares that the following is the policy of the United States:\n**(1)**\nLabor-management relationships and partnerships are based on trust, mutual respect, open communication, bilateral consensual problem solving, and shared accountability. Labor-management cooperation fully uses the strengths of both parties to best serve the interests of the public: operating as a team to carry out the public safety mission in a quality work environment. In many public safety agencies, it is the labor organization that provides the institutional stability as elected leaders and appointees come and go.\n**(2)**\nState and local public safety officers play an essential role in the efforts of the United States to detect, prevent, and respond to terrorist attacks and to respond to natural disasters, hazardous materials, and other mass casualty incidents. State and local public safety officers, as first responders, are a component of the National Incident Management System, developed by the Department of Homeland Security to coordinate response to and recovery from terrorism, major natural disasters, and other major emergencies. Public safety employer-employee cooperation is essential in meeting these needs and is, therefore, in the national interest.\n**(3)**\nThe Federal Government needs to encourage conciliation, mediation, and arbitration to aid and encourage public safety employers and the representatives of their employees to reach and maintain agreements concerning rates of pay, hours, and working conditions and to make all reasonable efforts through negotiations to settle their differences by mutual agreement reached through collective bargaining or by such methods as may be provided for in any applicable agreement for the settlement of disputes.\n**(4)**\nThe absence of adequate cooperation between public safety employers and employees has implications for the security of employees and can affect interstate and intrastate commerce. The lack of such labor-management cooperation can detrimentally impact the upgrading of law enforcement, fire, and emergency medical services of local communities, the health and well-being of public safety officers, and the morale of law enforcement, fire, and emergency medical service departments. Additionally, these factors could have significant commercial repercussions. Moreover, providing minimal standards for collective bargaining negotiations in the public safety sector can prevent industrial strife between labor and management that interferes with the normal flow of commerce.\n**(5)**\nMany States and localities already provide public safety officers with collective bargaining rights comparable to or greater than the rights and responsibilities set forth in this Act, and such State and local laws should be respected.\n#### 3. Definitions\nIn this Act:\n**(1) Authority**\nThe term Authority means the Federal Labor Relations Authority.\n**(2) Confidential employee**\nThe term confidential employee , with respect to the application of this Act in a State\u2014\n**(A)**\nhas the meaning given such term (or a substantially equivalent term) under any applicable State law of such State on the date of enactment of this Act; or\n**(B)**\nif no such applicable State law is in effect in such State, means an individual, employed by a public safety employer, who\u2014\n**(i)**\nis designated as confidential; and\n**(ii)**\nis an individual who routinely assists, in a confidential capacity, any supervisory employee or management employee.\n**(3) Emergency medical services employee**\nThe term emergency medical services employee means an individual who provides out-of-hospital emergency medical care, including an emergency medical technician, paramedic, or first responder.\n**(4) Employ**\nThe term employ has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(5) Firefighter**\nThe term firefighter has the meaning given the term employee in fire protection activities in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(6) Labor organization**\nThe term labor organization means an organization of any kind, in which public safety officers participate and which exists for the purpose, in whole or in part, of dealing with a public safety employer concerning grievances, conditions of employment, and related matters.\n**(7) Law enforcement officer**\nThe term law enforcement officer has the meaning given such term in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ).\n**(8) Management employee**\nThe term management employee , with respect to the application of this Act in a State\u2014\n**(A)**\nhas the meaning given such term (or a substantially equivalent term) under any applicable State law of such State on the date of enactment of this Act; or\n**(B)**\nif no such applicable State law is in effect in such State, means an individual employed by a public safety employer in a position that requires or authorizes the individual to formulate, determine, or influence the policies of the public safety employer.\n**(9) Person**\nThe term person means an individual or a labor organization.\n**(10) Public safety employer**\n**(A) In general**\nThe term public safety employer means any State, or political subdivision of a State, that employs a public safety officer.\n**(B) Applicability**\nFor purposes of this Act, a public safety employer shall be considered to be engaged in commerce or in an industry or activity affecting commerce.\n**(11) Public safety officer**\nThe term public safety officer \u2014\n**(A)**\nmeans an individual employed by a public safety employer who is a law enforcement officer, a firefighter, or an emergency medical services employee;\n**(B)**\nincludes an individual who is temporarily transferred to a supervisory or management position; and\n**(C)**\nexcept as provided in subparagraph (B), does not include\u2014\n**(i)**\na supervisory employee;\n**(ii)**\na management employee; or\n**(iii)**\na confidential employee.\n**(12) State**\nThe term State means each of the several States of the United States, the District of Columbia, and any territory or possession of the United States.\n**(13) Substantially provides**\nThe term substantially provides , when used with respect to the rights and responsibilities described in section 4(b), means providing rights and responsibilities that are comparable to or greater than each right and responsibility described in such section.\n**(14) Supervisory employee**\nThe term supervisory employee , with respect to the application of this Act in a State\u2014\n**(A)**\nhas the meaning given such term (or a substantially equivalent term) under any applicable State law of such State on the date of enactment of this Act; or\n**(B)**\nif no such applicable State law is in effect in such State, an individual, employed by a public safety employer, who\u2014\n**(i)**\nhas the authority in the interest of the public safety employer, if the exercise of such authority is not merely routine or clerical in nature but requires the consistent exercise of independent judgment, to\u2014\n**(I)**\nhire, direct, assign, promote, reward, transfer, furlough, lay off, recall, suspend, discipline, or remove public safety officers;\n**(II)**\nadjust the grievances of public safety officers; or\n**(III)**\neffectively recommend any action described in subclause (I) or (II); and\n**(ii)**\ndevotes a majority of time at work to exercising such authority.\n**(15) Unfair labor practice**\nThe term unfair labor practice means a practice described in section 7116 of title 5, United States Code, except that, in applying such section\u2014\n**(A)**\npublic safety officer shall be substituted for employee ;\n**(B)**\npublic safety employer shall be substituted for agency ; and\n**(C)**\nthis Act shall be substituted for this chapter .\n#### 4. Determination of rights and responsibilities\n##### (a) Determination\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act (except as provided in paragraph (4)(B)), the Authority shall make a determination for each State as to whether a State substantially provides for each of the rights and responsibilities described in subsection (b).\n**(2) Consideration of additional opinions**\nIn making the determination described in paragraph (1), the Authority shall consider the opinions of affected public safety employers and labor organizations. In the case where the Authority is notified by an affected public safety employer and labor organization that both parties agree that the law applicable to such public safety employer and labor organization substantially provides for the rights and responsibilities described in subsection (b), the Authority shall give such agreement weight to the maximum extent practicable in making the Authority\u2019s determination under paragraph (1).\n**(3) Limited criteria**\nIn making the determination described in paragraph (1), the Authority shall be limited to the application of the criteria described in subsection (b).\n**(4) Subsequent determinations**\n**(A) In general**\nA determination made pursuant to paragraph (1) shall remain in effect unless and until the Authority issues a subsequent determination, in accordance with the procedures set forth in subparagraph (B).\n**(B) Procedures for subsequent determinations**\nA public safety employer or a labor organization may submit to the Authority a written request for a subsequent determination with respect to whether a material change of State law (or an interpretation of such law) has occurred.\n**(C) Issuance of subsequent determination**\nIf satisfied that a material change in State law or its interpretation has occurred, the Authority shall issue a subsequent determination under paragraph (1) not later than 30 days after receipt of such request.\n**(5) Exception**\nThe Authority shall not make a determination under paragraph (1) that the laws of a State do not substantially provide for each of the rights and responsibilities described in subsection (b) on the basis that relevant State laws\u2014\n**(A)**\npermit an employee to appear on the employee\u2019s own behalf with respect to the employee\u2019s employment relations with the public safety employer involved;\n**(B)**\ndo not apply to a political subdivision of the State if such political subdivision\u2014\n**(i)**\nhas a population of fewer than 5,000 individuals; or\n**(ii)**\nemploys fewer than 25 full-time employees (excluding any individual elected by popular vote or appointed to serve on a board or commission); or\n**(C)**\ndo not require bargaining with respect to pension, retirement, or health benefits.\n**(6) Judicial review**\nAny person or public safety employer aggrieved by a determination of the Authority under paragraph (1) may, during the 60-day period beginning on the date on which the determination was made, petition any United States Court of Appeals in the circuit in which the person or public safety employer resides or transacts business or in the Court of Appeals for the District of Columbia Circuit, for judicial review.\n##### (b) Rights and responsibilities\nThe rights and responsibilities described under this subsection are the following:\n**(1)**\nA right of public safety officers to form and join a labor organization\u2014\n**(A)**\nwhich may exclude any management employee, supervisory employee, or confidential employee, and\n**(B)**\nthat is, or seeks to be, recognized as the exclusive bargaining representative of such public safety officers.\n**(2)**\nA requirement that any public safety employer\u2014\n**(A)**\nrecognize the labor organization of its public safety officers (freely chosen by a majority of the public safety officers);\n**(B)**\nagree to bargain with such labor organization; and\n**(C)**\ncommit any agreements with such labor organization to writing in a contract or memorandum of understanding.\n**(3)**\nA right of public safety officers to bargain with respect to hours, wages, and terms and conditions of employment.\n**(4)**\nA right to binding interest arbitration as a mechanism to resolve an impasse in collective bargaining negotiations.\n**(5)**\nA right to enforcement of all rights, responsibilities, and protections enumerated in this subsection, and of any written contract or memorandum of understanding between a labor organization and a public safety employer, through\u2014\n**(A)**\na State administrative agency, if the State so chooses; or\n**(B)**\nany court of competent jurisdiction.\n##### (c) Compliance with requirements\nIf the Authority determines under subsection (a)(1) that a State substantially provides each of the rights and responsibilities described in subsection (b), then subsection (d) shall not apply and this Act shall not preempt the laws of such State.\n##### (d) Failure To meet requirements\n**(1) In general**\nIf the Authority determines under subsection (a)(1) that a State does not substantially provide for the rights and responsibilities described in subsection (b), then such State shall be subject to the regulations and procedures described in section 5 beginning on the later of\u2014\n**(A)**\nthe date that is 2 years after the date of enactment of this Act;\n**(B)**\nthe date that is the last day of the first regular session of the legislature of the State that begins after the date the Authority makes a determination under subsection (a)(1); or\n**(C)**\nin the case of a State receiving a subsequent determination under subsection (a)(4), the date that is the last day of the first regular session of the legislature of the State that begins after the date the Authority made the determination.\n**(2) Partial failure**\nIf the Authority determines under subsection (a)(1) that a State does not substantially provide for the rights and responsibilities described in subsection (b) because the State law substantially provides for such rights and responsibilities for certain categories of public safety officers covered by this Act but not others, the Authority shall identify those categories of public safety officers that shall be subject to the regulations and procedures described in section 5, pursuant to section 8(b)(3) and beginning on the appropriate date described in paragraph (1), and those categories of public safety officers that shall remain solely subject to State law with respect to the rights and responsibilities described in subsection (b).\n#### 5. Role of Federal Labor Relations Authority\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Authority shall issue regulations, in accordance with the rights and responsibilities described in section 4(b), establishing collective bargaining procedures for public safety employers and public safety officers that substantially provide for the minimum standards described in section 4(b) for States described in section 4(d).\n##### (b) Role of the Federal Labor Relations Authority\nIn carrying out subsection (a), the Authority shall\u2014\n**(1)**\ndetermine the appropriateness of units for labor organization representation;\n**(2)**\nsupervise or conduct elections to determine whether a labor organization has been chosen as an exclusive representative by a voting majority of the public safety officers in an appropriate unit;\n**(3)**\nresolve issues relating to the duty to bargain in good faith;\n**(4)**\nconduct hearings and resolve complaints of unfair labor practices;\n**(5)**\nresolve exceptions to the awards of arbitrators;\n**(6)**\nprotect the right of each employee to form, join, or assist any labor organization or to refrain from any such activity, freely and without fear of penalty or reprisal, and protect each employee in the exercise of such right; and\n**(7)**\ntake such other actions as are necessary and appropriate to effectively administer this Act, including issuing subpoenas requiring the attendance and testimony of witnesses and the production of documentary or other evidence from any place in the United States, and administering oaths, taking or ordering the taking of depositions, ordering responses to written interrogatories, and receiving and examining witnesses.\n##### (c) Enforcement\n**(1) Authority to petition court**\nThe Authority may petition any United States Court of Appeals with jurisdiction over the parties, or the United States Court of Appeals for the District of Columbia Circuit, to enforce any final orders under this section, and for appropriate temporary relief or a restraining order.\n**(2) Private right of action**\nUnless the Authority has filed a petition for enforcement as provided in paragraph (1) and except as provided in section 8(b)(4) with respect to States, any party may file suit in any appropriate district court of the United States to enforce compliance with the regulations issued by the Authority pursuant to this section, or to enforce compliance with any order issued by the Authority pursuant to this section.\n#### 6. Strikes and lockouts prohibited\n##### (a) In general\nSubject to subsection (b), a public safety employer, public safety officer, or labor organization may not engage in a lockout, sickout, work slowdown, strike, or any other organized job action that will measurably disrupt the delivery of emergency services and is designed to compel a public safety employer, public safety officer, or labor organization to agree to the terms of a proposed contract.\n##### (b) No preemption\nNothing in this section shall be construed to preempt any law of any State or political subdivision of any State with respect to strikes by public safety officers.\n#### 7. Existing collective bargaining units and agreements\nThe enactment of this Act shall not invalidate any certification, recognition, result of an election, collective bargaining agreement, or memorandum of understanding that has been issued, approved, or ratified by any public employee relations board or commission or by any State or political subdivision or its agents and is in effect on the day before the date of enactment of this Act.\n#### 8. Construction and compliance\n##### (a) Construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto preempt or limit the remedies, rights, and procedures of any law of any State or political subdivision of any State that provides comparable or greater rights and responsibilities than the rights and responsibilities described in section 4(b); or\n**(2)**\nto prevent a State from enforcing any law that prohibits public safety employers and labor organizations from negotiating provisions in a labor agreement that require labor organization membership or payment of labor organization fees as a condition of employment.\n##### (b) Compliance\n**(1) Actions of states**\nNothing in this Act or the regulations promulgated under this Act shall be construed to require a State to rescind or preempt the laws or ordinances of any of the State\u2019s political subdivisions if such laws provide rights and responsibilities for public safety officers that are comparable to or greater than the rights and responsibilities described in section 4(b).\n**(2) Actions of the authority**\nNothing in this Act or the regulations promulgated under this Act shall be construed to preempt\u2014\n**(A)**\nthe laws or ordinances of any State or political subdivision of a State, if such laws provide collective bargaining rights for public safety officers that are comparable to or greater than the rights enumerated in section 4(b);\n**(B)**\nthe laws or ordinances of any State or political subdivision of a State that provide for the rights and responsibilities described in section 4(b) with respect to certain categories of public safety officers covered by this Act solely because such rights and responsibilities have not been extended to other categories of public safety officers covered by this Act; or\n**(C)**\nthe laws or ordinances of any State or political subdivision of a State that provide for the rights and responsibilities described in section 4(b), solely because such laws or ordinances provide that a contract or memorandum of understanding between a public safety employer and a labor organization must be presented to a legislative body as part of the process for approving such contract or memorandum of understanding.\n**(3) Limited enforcement power**\nIn the case of a law described in paragraph (2)(B), the Authority shall only exercise the powers provided in section 5 with respect to those categories of public safety officers who have not been afforded the rights and responsibilities described in section 4(b).\n**(4) Exclusive enforcement provision**\nNotwithstanding any other provision of the Act, and in the absence of a waiver of a State\u2019s sovereign immunity, the Authority shall have the exclusive power to enforce the provisions of this Act with respect to employees of a State.\n#### 9. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act.",
      "versionDate": "2025-02-19",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-10T14:35:26Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-07-10T14:35:04Z"
          },
          {
            "name": "Federal appellate courts",
            "updateDate": "2025-07-10T14:35:19Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-07-10T14:35:31Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-10T14:34:33Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-07-10T14:34:49Z"
          },
          {
            "name": "Labor standards",
            "updateDate": "2025-07-10T14:35:09Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-07-10T14:34:44Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-10T14:34:28Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-10T14:34:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-13T14:54:39Z"
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
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s636is.xml"
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
      "title": "Public Safety Employer-Employee Cooperation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Safety Employer-Employee Cooperation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide collective bargaining rights for public safety officers employed by States or their political subdivisions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:29Z"
    }
  ]
}
```
