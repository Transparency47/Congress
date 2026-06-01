# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4252
- Title: Extreme Risk Protection Order Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4252
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2026-03-24T18:26:23Z
- Update date including text: 2026-03-24T18:26:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4252",
    "number": "4252",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Extreme Risk Protection Order Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-24T18:26:23Z",
    "updateDateIncludingText": "2026-03-24T18:26:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:02:40Z",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "VA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4252ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4252\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Mr. Carbajal (for himself, Ms. Brownley , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo support State, Tribal, and local efforts to remove access to firearms from individuals who are a danger to themselves or others pursuant to court orders for this purpose.\n#### 1. Short title\nThis Act may be cited as the Extreme Risk Protection Order Expansion Act of 2025 .\n#### 2. Extreme risk protection order grant program\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State or Indian Tribe\u2014\n**(i)**\nthat enacts legislation described in subsection (c);\n**(ii)**\nwith respect to which the Attorney General determines that the legislation described in clause (i) complies with the requirements under subsection (c)(1); and\n**(iii)**\nthat certifies to the Attorney General that the State or Indian Tribe will, with respect to a grant received under subsection (b)\u2014\n**(I)**\nuse the grant for the purposes described in subsection (b)(2); and\n**(II)**\nallocate not less than 25 percent and not more than 70 percent of the amount received under the grant for the development and dissemination of training for law enforcement officers in accordance with subsection (b)(4); or\n**(B)**\na unit of local government or other public or private entity that\u2014\n**(i)**\nis located in a State or in the territory under the jurisdiction of an Indian Tribe that meets the requirements described in clauses (i) and (ii) of subparagraph (A); and\n**(ii)**\ncertifies to the Attorney General that the unit of local government or entity will, with respect to a grant received under subsection (b)\u2014\n**(I)**\nuse the grant for the purposes described in subsection (b)(2); and\n**(II)**\nallocate not less than 25 percent and not more than 70 percent of the amount received under the grant for the development and dissemination of training for law enforcement officers in accordance with subsection (b)(4).\n**(2) Extreme risk protection order**\nThe term extreme risk protection order means a written order or warrant, issued by a State or Tribal court or signed by a magistrate (or other comparable judicial officer), the primary purpose of which is to reduce the risk of firearm-related death or injury by doing 1 or more of the following:\n**(A)**\nProhibiting a named individual from having under the custody or control of the individual, owning, purchasing, possessing, or receiving a firearm.\n**(B)**\nHaving a firearm removed or requiring the surrender of firearms from a named individual.\n**(3) Firearm**\nThe term firearm has the meaning given the term in section 921 of title 18, United States Code.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term Indian tribe in section 1709 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 ).\n**(5) Law enforcement officer**\nThe term law enforcement officer means a public servant authorized by Federal, State, local, or Tribal law or by an agency of the Federal Government or of a State, local, or Tribal government to\u2014\n**(A)**\nengage in or supervise the prevention, detection, investigation, or prosecution of an offense; or\n**(B)**\nsupervise sentenced criminal offenders.\n**(6) Petitioner**\nThe term petitioner means an individual authorized under State or Tribal law to petition for an extreme risk protection order.\n**(7) Respondent**\nThe term respondent means an individual named in the petition for an extreme risk protection order or subject to an extreme risk protection order.\n**(8) State**\nThe term State means\u2014\n**(A)**\na State;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico; and\n**(D)**\nany other territory or possession of the United States.\n**(9) Unit of local government**\nThe term unit of local government has the meaning given the term in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n##### (b) Grant program established\n**(1) In general**\nThe Attorney General shall establish a program under which, from amounts made available to carry out this section, the Attorney General may make grants to eligible entities to assist in carrying out the provisions of the legislation described in subsection (c).\n**(2) Use of funds**\nFunds awarded under this subsection may be used by an applicant to\u2014\n**(A)**\nenhance the capacity of law enforcement agencies and the courts of a State, unit of local government, or Indian Tribe by providing personnel, training, technical assistance, data collection, and other resources to carry out enacted legislation described in subsection (c);\n**(B)**\ntrain judges, court personnel, health care and legal professionals, and law enforcement officers to more accurately identify individuals whose access to firearms poses a danger of causing harm to themselves or others by increasing the risk of firearms suicide or interpersonal violence;\n**(C)**\ndevelop and implement law enforcement and court protocols, forms, and orders so that law enforcement agencies and the courts may carry out the provisions of the enacted legislation described in subsection (c) in a safe, equitable, and effective manner, including through the removal and storage of firearms pursuant to extreme risk protection orders under the enacted legislation; and\n**(D)**\nraise public awareness and understanding of the enacted legislation described in subsection (c), including through subgrants to community-based organizations for the training of community members, so that extreme risk protection orders may be issued in appropriate situations to reduce the risk of firearms-related death and injury.\n**(3) Application**\nAn eligible entity desiring a grant under this subsection shall submit to the Attorney General an application at such time, in such manner, and containing or accompanied by such information as the Attorney General may reasonably require.\n**(4) Training**\n**(A) In general**\nA recipient of a grant under this subsection shall provide training to law enforcement officers, including officers of relevant Federal, State, local, and Tribal law enforcement agencies, in the safe, impartial, effective, and equitable use and administration of extreme risk protection orders, including training to address\u2014\n**(i)**\nbias based on race and racism, ethnicity, gender, sexual orientation, gender identity, religion, language proficiency, mental health condition, disability, and classism in the use and administration of extreme risk protection orders;\n**(ii)**\nthe appropriate use of extreme risk protection orders in cases of domestic violence, including the applicability of other policies and protocols to address domestic violence in situations that may also involve extreme risk protection orders and the necessity of safety planning with the victim before a law enforcement officer petitions for and executes an extreme risk protection order, if applicable;\n**(iii)**\ninteracting with persons with a mental illness or emotional distress, including de-escalation and crisis intervention; and\n**(iv)**\nbest practices for referring persons subject to extreme risk protection orders and associated victims of violence to social service providers that may be available in the jurisdiction and appropriate for those individuals, including health care, mental health, substance abuse, and legal services, employment and vocational services, housing assistance, case management, and veterans and disability benefits.\n**(B) Consultation with experts**\nA recipient of a grant under this subsection, in developing law enforcement training required under subparagraph (A), shall seek advice from domestic violence service providers (including culturally specific (as defined in section 40002 of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291 )) organizations), social service providers, suicide prevention advocates, violence intervention specialists, law enforcement agencies, mental health disability experts, and other community groups working to reduce suicides and violence, including domestic violence, within the State or the territory under the jurisdiction of the Indian Tribe, as applicable, that enacted the legislation described in subsection (c) that enabled the grant recipient to be an eligible entity.\n**(5) Authorization of appropriations**\nThere are authorized to be appropriated such sums as are necessary to carry out this subsection.\n##### (c) Eligibility for extreme risk protection order grant program\n**(1) Requirements**\nLegislation described in this subsection is legislation that establishes requirements that are substantially similar to the following:\n**(A) Petition for extreme risk protection order**\nA petitioner, including a law enforcement officer, may submit a petition to a State or Tribal court, on a form designed by the court or a State or Tribal agency, that\u2014\n**(i)**\ndescribes the facts and circumstances justifying that an extreme risk protection order be issued against the named individual; and\n**(ii)**\nis signed by the applicant, under oath.\n**(B) Notice and due process**\nThe individual named in a petition for an extreme risk protection order as described in subparagraph (A) shall be given written notice of the petition and an opportunity to be heard on the matter in accordance with this paragraph.\n**(C) Issuance of extreme risk protection orders**\n**(i) Hearing**\n**(I) In general**\nUpon receipt of a petition described in subparagraph (A) or request of an individual named in such a petition, the court shall order a hearing to be held within a reasonable time, and not later than 30 days after the date of the petition or request.\n**(II) Determination**\nIf the court finds at the hearing ordered under subclause (I), by a preponderance of the evidence or according to a higher evidentiary standard established by the State or Indian Tribe, that the respondent poses a danger of causing harm to self or others by having access to a firearm, the court may issue an extreme risk protection order.\n**(ii) Duration of extreme risk protection order**\nAn extreme risk protection order shall be in effect\u2014\n**(I)**\nuntil an order terminating or superseding the extreme risk protection order is issued; or\n**(II)**\nfor a set period of time.\n**(D) Ex parte extreme risk protection orders**\n**(i) In general**\nUpon receipt of a petition described in subparagraph (A), the court may issue an ex parte extreme risk protection order, if\u2014\n**(I)**\nthe petition for an extreme risk protection order alleges that the respondent poses a danger of causing harm to self or others by having access to a firearm; and\n**(II)**\nthe court finds there is probable cause to believe, or makes a finding according to a higher evidentiary standard established by the State or Indian Tribe, that the respondent poses a danger of causing harm to self or others by having access to a firearm.\n**(ii) Duration of ex parte extreme risk protection order**\nAn ex parte extreme risk protection order shall remain in effect only until the hearing required under subparagraph (C)(i).\n**(E) Storage of removed firearms**\n**(i) Availability for return**\nAll firearms removed or surrendered pursuant to an extreme risk protection order shall only be available for return to the named individual when the individual has regained eligibility under Federal and State law and, where applicable, Tribal law to possess firearms.\n**(ii) Consent required for disposal or destruction**\nFirearms owned by a named individual may not be disposed of or destroyed during the period of the extreme risk protection order without the consent of the named individual.\n**(F) Notification**\n**(i) In general**\n**(I) Requirement**\nA State or Tribal court that issues an extreme risk protection order shall notify the Attorney General or the comparable State or Tribal agency, as applicable, of the order as soon as practicable or within a designated period of time.\n**(II) Form and manner**\nA State or Tribal court shall submit a notification under subclause (I) in an electronic format, in a manner prescribed by the Attorney General or the comparable State or Tribal agency.\n**(ii) Update of databases by State or Tribal agency**\nAs soon as practicable or within the time period designated by State or Tribal law after receiving a notification under clause (i), the comparable State or Tribal agency shall ensure that the extreme risk protection order is reflected in the National Instant Criminal Background Check System.\n**(2) Additional provisions**\nLegislation described in this subsection may\u2014\n**(A)**\nprovide procedures for the termination of an extreme risk protection order;\n**(B)**\nprovide procedures for the renewal of an extreme risk protection order;\n**(C)**\nestablish burdens and standards of proof for issuance of orders described in paragraph (1) that are substantially similar to or higher than the burdens and standards of proof set forth in that paragraph;\n**(D)**\nlimit the individuals who may submit a petition described in paragraph (1), provided that, at a minimum, 1 or more law enforcement officers are authorized to do so; and\n**(E)**\ninclude any other authorizations or requirements that the State or Tribal authorities determine appropriate.\n**(3) Attorney General responsibilities**\n**(A) Manner of submitting notification to Attorney General**\nThe Attorney General shall prescribe the manner in which a State or Tribal court shall submit a notification to the Attorney General under a provision of State or Tribal law that is substantially similar to paragraph (1)(F)(i).\n**(B) Update of databases**\nAs soon as practicable, and in any event not later than 30 days, after receiving a notification under a provision of State or Tribal law that is substantially similar to paragraph (1)(F)(i), the Attorney General shall ensure that the extreme risk protection order is reflected in the National Instant Criminal Background Check System.\n**(4) Annual report**\nNot later than 1 year after the date on which an eligible entity receives a grant under subsection (b), and annually thereafter for the duration of the grant period, the entity shall submit to the Attorney General a report that includes, with respect to the preceding year\u2014\n**(A)**\nthe number of petitions for ex parte extreme risk protection orders filed, as well as the number of such orders issued and the number denied, disaggregated by\u2014\n**(i)**\nthe jurisdiction;\n**(ii)**\nthe individual authorized under State or Tribal law to petition for an extreme risk protection order, including the relationship of the individual to the respondent; and\n**(iii)**\nthe alleged danger posed by the respondent, including whether the danger involved a risk of suicide, unintentional injury, domestic violence, or other interpersonal violence;\n**(B)**\nthe number of petitions for extreme risk protection orders filed, as well as the number of such orders issued and the number denied, disaggregated by\u2014\n**(i)**\nthe jurisdiction;\n**(ii)**\nthe individual authorized under State or Tribal law to petition for an extreme risk protection order, including the relationship of the individual to the respondent; and\n**(iii)**\nthe alleged danger posed by the respondent, including whether the danger involved a risk of suicide, unintentional injury, domestic violence, or other interpersonal violence;\n**(C)**\nthe number of petitions for renewals of extreme risk protection orders filed, as well as the number of such orders issued and the number denied;\n**(D)**\nthe number of cases in which a court imposed a penalty for false reporting or frivolous petitions;\n**(E)**\ndemographic data of petitioners, including race, ethnicity, national origin, sex, gender, age, disability, and English language proficiency, if available;\n**(F)**\ndemographic data of respondents, including race, ethnicity, national origin, sex, gender, age, disability, and English language proficiency, if available; and\n**(G)**\nthe number of firearms removed, if available.\n#### 3. Federal firearms prohibition\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (10) and (11) as paragraphs (11) and (12), respectively;\n**(B)**\nby inserting after paragraph (9) the following:\n(10) is subject to a court order that\u2014 (A) was issued after a hearing of which such person received actual notice, and at which such person had an opportunity to participate; (B) prevents such person from possessing or receiving firearms; and (C) includes a finding that such person poses a danger of harm to self or others. ; and\n**(C)**\nin paragraph (12), as so redesignated, by striking (10) and inserting (11) ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (8)(C)(ii), by striking or at the end;\n**(B)**\nin paragraph (9), by striking the comma at the end and inserting ; or ; and\n**(C)**\nby inserting after paragraph (9) the following:\n(10) is subject to a court order that\u2014 (A) was issued after a hearing of which such person received actual notice, and at which such person had an opportunity to participate; (B) prevents such person from possessing or receiving firearms; and (C) includes a finding that such person poses a danger of harm to self or others. .\n#### 4. Identification records\nSection 534 of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (4) and (5) as paragraphs (5) and (6), respectively; and\n**(B)**\nby inserting after paragraph (3) the following:\n(4) acquire, collect, classify, and preserve records from Federal, Tribal, and State courts and other agencies identifying individuals subject to extreme risk protection orders, as defined in section 2(a) of the Extreme Risk Protection Order Expansion Act of 2025 ; ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking (a)(5) and inserting (a)(6) ; and\n**(B)**\nby striking (a)(4) and inserting (a)(5) ; and\n**(3)**\nby adding at the end the following:\n(g) Extreme risk protection orders in national crime information databases A Federal, Tribal, or State criminal justice agency or criminal or civil court may\u2014 (1) include extreme risk protection orders, as defined in section 2(a) of the Extreme Risk Protection Order Expansion Act of 2025 , in national crime information databases, as that term is defined in subsection (f)(3) of this section; and (2) have access to information regarding extreme risk protection orders through the national crime information databases. .\n#### 5. Conforming amendment\nSection 3(1) of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40903(1) ) is amended by striking section 922(g)(8) and inserting paragraph (8) or (10) of section 922(g) .\n#### 6. Full faith and credit\n##### (a) Definitions\nIn this section, the terms extreme risk protection order , Indian Tribe , and State have the meanings given those terms in section 2(a).\n##### (b) Full faith and credit required\nAny extreme risk protection order issued under a State or Tribal law enacted in accordance with this Act shall be accorded the same full faith and credit by the court of another State or Indian Tribe (referred to in this subsection as the enforcing State or Indian Tribe ) and enforced by the court and law enforcement personnel of the other State or Tribal government as if it were the order of the enforcing State or Indian Tribe.\n##### (c) Applicability to extreme risk protection orders\n**(1) In general**\nSubsection (b) shall apply to an extreme risk protection order issued by a State or Tribal court if\u2014\n**(A)**\nthe court has jurisdiction over the parties and matter under the law of the State or Indian Tribe; and\n**(B)**\nreasonable notice and opportunity to be heard is given to the person against whom the order is sought sufficient to protect that person\u2019s right to due process.\n**(2) Ex parte extreme risk protection orders**\nFor purposes of paragraph (1)(B), in the case of an ex parte extreme risk protection order, notice and opportunity to be heard shall be provided within the time required by State or Tribal law, and in any event within a reasonable time after the order is issued, sufficient to protect the due process rights of the respondent.\n##### (d) Tribal court jurisdiction\nFor purposes of this section, a court of an Indian Tribe shall have full civil jurisdiction to issue and enforce an extreme risk protection order involving any person, including the authority to enforce any order through civil contempt proceedings, to exclude violators from Indian land, and to use other appropriate mechanisms, in matters arising anywhere in the Indian country (as defined in section 1151 of title 18, United States Code) of the Indian Tribe or otherwise within the authority of the Indian Tribe.\n#### 7. Severability\nIf any provision of this Act or amendment made by this Act, or the application of such provision or amendment to any person or circumstance, is held to be invalid, the remaining provisions of this Act and amendments made by this Act, or the application of such provision or amendment to other persons or circumstances, shall not be affected.\n#### 8. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-06-30",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "889",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Extreme Risk Protection Order Expansion Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-24T12:42:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-30",
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
          "measure-id": "id119hr4252",
          "measure-number": "4252",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4252v00",
            "update-date": "2026-03-24"
          },
          "action-date": "2025-06-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Extreme Risk Protection Order Expansion Act of 2025</strong></p><p>This bill establishes grants to support the implementation of extreme risk protection order laws at the state and local levels, extends federal firearms restrictions to individuals who are subject to extreme risk protection orders, and expands related data collection. Extreme risk protection order laws, or red flag laws, generally allow certain individuals (e.g., law enforcement officers or family members) to petition a court for a temporary order that prohibits an at-risk individual from purchasing and possessing firearms.</p><p>Among its provisions, the bill</p><ul><li>directs the Department of Justice to establish a grant program to help states, local governments, Indian tribes, and other entities implement extreme risk protection order laws;</li><li>extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to individuals who are subject to extreme risk protection orders; and</li><li>requires the Federal Bureau of Investigation to compile records from federal, tribal, and state courts and other agencies that identify individuals who are subject to extreme risk protection orders.</li></ul>"
        },
        "title": "Extreme Risk Protection Order Expansion Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4252.xml",
    "summary": {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Extreme Risk Protection Order Expansion Act of 2025</strong></p><p>This bill establishes grants to support the implementation of extreme risk protection order laws at the state and local levels, extends federal firearms restrictions to individuals who are subject to extreme risk protection orders, and expands related data collection. Extreme risk protection order laws, or red flag laws, generally allow certain individuals (e.g., law enforcement officers or family members) to petition a court for a temporary order that prohibits an at-risk individual from purchasing and possessing firearms.</p><p>Among its provisions, the bill</p><ul><li>directs the Department of Justice to establish a grant program to help states, local governments, Indian tribes, and other entities implement extreme risk protection order laws;</li><li>extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to individuals who are subject to extreme risk protection orders; and</li><li>requires the Federal Bureau of Investigation to compile records from federal, tribal, and state courts and other agencies that identify individuals who are subject to extreme risk protection orders.</li></ul>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr4252"
    },
    "title": "Extreme Risk Protection Order Expansion Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Extreme Risk Protection Order Expansion Act of 2025</strong></p><p>This bill establishes grants to support the implementation of extreme risk protection order laws at the state and local levels, extends federal firearms restrictions to individuals who are subject to extreme risk protection orders, and expands related data collection. Extreme risk protection order laws, or red flag laws, generally allow certain individuals (e.g., law enforcement officers or family members) to petition a court for a temporary order that prohibits an at-risk individual from purchasing and possessing firearms.</p><p>Among its provisions, the bill</p><ul><li>directs the Department of Justice to establish a grant program to help states, local governments, Indian tribes, and other entities implement extreme risk protection order laws;</li><li>extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to individuals who are subject to extreme risk protection orders; and</li><li>requires the Federal Bureau of Investigation to compile records from federal, tribal, and state courts and other agencies that identify individuals who are subject to extreme risk protection orders.</li></ul>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr4252"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4252ih.xml"
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
      "title": "Extreme Risk Protection Order Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Extreme Risk Protection Order Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To support State, Tribal, and local efforts to remove access to firearms from individuals who are a danger to themselves or others pursuant to court orders for this purpose.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:29Z"
    }
  ]
}
```
