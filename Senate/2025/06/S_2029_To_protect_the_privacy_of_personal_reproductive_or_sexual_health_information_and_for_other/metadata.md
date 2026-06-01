# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2029?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2029
- Title: My Body, My Data Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2029
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2026-04-21T11:03:28Z
- Update date including text: 2026-04-21T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2029",
    "number": "2029",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "My Body, My Data Act of 2025",
    "type": "S",
    "updateDate": "2026-04-21T11:03:28Z",
    "updateDateIncludingText": "2026-04-21T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
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
            "date": "2025-06-11T17:34:54Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-11T17:34:54Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "DE"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NM"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "RI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MD"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2029is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2029\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Ms. Hirono (for herself, Mr. Wyden , Mr. Blumenthal , Ms. Blunt Rochester , Ms. Cantwell , Ms. Duckworth , Mr. Gallego , Mrs. Gillibrand , Mr. Heinrich , Mr. Kaine , Ms. Klobuchar , Mr. Merkley , Mrs. Murray , Mr. Schiff , Mrs. Shaheen , Ms. Smith , Mr. Welch , Mr. Whitehouse , Ms. Baldwin , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo protect the privacy of personal reproductive or sexual health information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the My Body, My Data Act of 2025 .\n#### 2. Minimization\n##### (a) Minimization of collecting, retaining, using, and disclosing\nA regulated entity may not collect, retain, use, or disclose personal reproductive or sexual health information, except as is strictly necessary to provide a product or service that the individual to whom such information relates has requested from such regulated entity.\n##### (b) Minimization of employee access\nA regulated entity shall restrict access to personal reproductive or sexual health information by the employees or service providers of such regulated entity to such employees or service providers for which access is necessary to provide a product or service that the individual to whom such information relates has requested from such regulated entity.\n#### 3. Right of access, correction, and deletion\n##### (a) Right of access\n**(1) In general**\nA regulated entity shall make available a reasonable mechanism by which an individual, upon a verified request, may access\u2014\n**(A)**\nany personal reproductive or sexual health information relating to such individual that is retained by such regulated entity, including\u2014\n**(i)**\nin the case of such information that such regulated entity collected from third parties, how and from which specific third parties such regulated entity collected such information; and\n**(ii)**\nsuch information that such regulated entity inferred about such individual; and\n**(B)**\na list of the specific third parties to which such regulated entity has disclosed any personal reproductive or sexual health information relating to such individual.\n**(2) Format**\nA regulated entity shall make the information described in paragraph (1) available in both a human-readable format and a structured, interoperable, and machine-readable format.\n##### (b) Right of correction\nA regulated entity shall make available a reasonable mechanism by which an individual, upon a verified request, may direct the correction of any inaccurate personal reproductive or sexual health information relating to such individual that is retained by such regulated entity or the service providers of such regulated entity, including any such information that such regulated entity collected from a third party or inferred from other information retained by such regulated entity.\n##### (c) Right of deletion\nA regulated entity shall make available a reasonable mechanism by which an individual, upon a verified request, may direct the deletion of any personal reproductive or sexual health information relating to such individual that is retained by such regulated entity and the service providers of such regulated entity, including any such information that such regulated entity collected from a third party or inferred from other information retained by such regulated entity.\n##### (d) General provisions\n**(1) Reasonable mechanism defined**\nIn this section, the term reasonable mechanism means, with respect to a regulated entity and a right under this section, a mechanism that\u2014\n**(A)**\nis provided in the primary manner through which such regulated entity provides the goods or services of such regulated entity;\n**(B)**\nis easy to use and prominently available; and\n**(C)**\nincludes an online means of exercising such right.\n**(2) Timeline for complying with requests**\nA regulated entity shall comply with a verified request received under this section without undue delay and not later than 15 days after the date on which the requesting individual submits the verified request.\n**(3) Fees prohibited**\nA regulated entity may not charge a fee to an individual for a request made under this section.\n**(4) Rules of construction**\nNothing in this section shall be construed to require a regulated entity to\u2014\n**(A)**\ntake an action that would convert information that is not personal information into personal information;\n**(B)**\ncollect or retain personal information that such regulated entity would otherwise not collect or retain; or\n**(C)**\nretain personal information longer than such regulated entity would otherwise retain such information.\n#### 4. Privacy policy\n##### (a) Policy required\nA regulated entity shall maintain a privacy policy relating to the practices of such regulated entity regarding the collecting, retaining, using, and disclosing of personal reproductive or sexual health information.\n##### (b) Publication required\nA regulated entity shall prominently publish the privacy policy required by subsection (a) on the website of such regulated entity.\n##### (c) Contents\nThe privacy policy required by subsection (a) shall be clear and conspicuous and shall contain, at a minimum, the following:\n**(1)**\nA description of the practices of the regulated entity regarding the collecting, retaining, using, and disclosing of personal reproductive or sexual health information.\n**(2)**\nA concise statement of the categories of such information collected, retained, used, or disclosed by the regulated entity.\n**(3)**\nA concise statement, for each such category, of the purposes of such regulated entity for the collecting, retaining, using, or disclosing of such information.\n**(4)**\nA list of the specific third parties to which such regulated entity discloses such information, and a concise statement of the purposes for which such regulated entity discloses such information, including how such information may be used by each such third party.\n**(5)**\nA list of the specific third parties from which such regulated entity has collected such information, and a concise statement of the purposes for which such regulated entity collects such information.\n**(6)**\nA concise statement describing the extent to which individuals may exercise control over the collecting, retaining, using, and disclosing of personal reproductive or sexual health information by such regulated entity, the steps an individual is required to take to implement such controls, and direct links to such controls.\n**(7)**\nA concise statement describing the efforts of the regulated entity to protect personal reproductive or sexual health information from unauthorized disclosure.\n#### 5. Prohibition against retaliation\nA regulated entity may not retaliate against an individual because the individual exercises a right of the individual under this Act, including by\u2014\n**(1)**\ndenying goods or services to the individual;\n**(2)**\ncharging the individual different prices or rates for goods or services, including by using discounts or other benefits or imposing penalties;\n**(3)**\nproviding a different level or quality of goods or services to the individual; or\n**(4)**\nsuggesting that the individual will receive a different price or rate for goods or services or a different level or quality of goods or services.\n#### 6. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\n**(A) In general**\nExcept as provided in section 7(6)(A)(ii), the Commission shall enforce this Act and the regulations promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny regulated entity that violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Rulemaking authority**\nThe Commission may promulgate, in accordance with section 553 of title 5, United States Code, such regulations as may be necessary to carry out this Act.\n##### (b) Enforcement by individuals\n**(1) In general**\nAny individual alleging a violation of this Act or a regulation promulgated under this Act may bring a civil action in any court of competent jurisdiction.\n**(2) Relief**\nIn a civil action brought under paragraph (1) in which the plaintiff prevails, the court may award\u2014\n**(A)**\nan amount not less than $100 and not greater than $1,000 per violation per day, or actual damages, whichever is greater;\n**(B)**\npunitive damages;\n**(C)**\nreasonable attorney\u2019s fees and litigation costs; and\n**(D)**\nany other relief, including equitable or declaratory relief, that the court determines appropriate.\n**(3) Injury in fact**\nA violation of this Act, or a regulation promulgated under this Act, with respect to personal reproductive or sexual health information constitutes a concrete and particularized injury in fact to the individual to whom such information relates.\n**(4) Invalidity of pre-dispute arbitration agreements and pre-dispute joint action waivers**\n**(A) In general**\nNotwithstanding any other provision of law, no pre-dispute arbitration agreement or pre-dispute joint-action waiver shall be valid or enforceable with respect to a dispute arising under this Act.\n**(B) Applicability**\nAny determination as to whether or how this paragraph applies to any dispute shall be made by a court, rather than an arbitrator, without regard to whether such agreement purports to delegate such determination to an arbitrator.\n**(C) Definitions**\nFor purposes of this paragraph:\n**(i) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means any agreement to arbitrate a dispute that has not arisen at the time of the making of the agreement.\n**(ii) Pre-dispute joint-action waiver**\nThe term pre-dispute joint-action waiver means an agreement that would prohibit a party from participating in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not arisen at the time of the making of the agreement.\n#### 7. Definitions\nIn this Act:\n**(1) Collect**\nThe term collect means, with respect to personal reproductive or sexual health information, for a regulated entity to obtain such information in any manner.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Disclose**\nThe term disclose means, with respect to personal reproductive or sexual health information, for a regulated entity to release, transfer, sell, provide access to, license, or divulge such information in any manner to a third party or government entity.\n**(4) Personal information**\nThe term personal information means information that identifies, relates to, describes, is reasonably capable of being associated with, or could reasonably be linked, directly or indirectly, with a particular individual, household, or device.\n**(5) Personal reproductive or sexual health information**\nThe term personal reproductive or sexual health information means personal information relating to the past, present, or future reproductive or sexual health of an individual, including\u2014\n**(A)**\nefforts to research or obtain reproductive or sexual health information, services, or supplies, including location information that might indicate an attempt to acquire or receive such information, services, or supplies;\n**(B)**\nreproductive or sexual health conditions, status, diseases, or diagnoses, including pregnancy and pregnancy-related conditions, menstruation, ovulation, ability to conceive a pregnancy, whether such individual is sexually active, and whether such individual is engaging in unprotected sex;\n**(C)**\nreproductive- and sexual-health-related surgeries or procedures, including abortion;\n**(D)**\nuse or purchase of contraceptives, medication abortion, or any other drug, device, or materials related to reproductive health;\n**(E)**\nbodily functions, vital signs, measurement, or symptoms related to menstruation or pregnancy, such as basal temperature, cramps, bodily discharge, or hormone levels;\n**(F)**\nany information about diagnoses or diagnostic testing, treatment, medications, or the purchase or use of any product or service relating to the matters described in subparagraphs (A) through (E); and\n**(G)**\nany information described in subparagraphs (A) through (F) that is derived or extrapolated from non-health information, including proxy, derivative, inferred, emergent, and algorithmic data.\n**(6) Regulated entity**\n**(A) In general**\nThe term regulated entity means any entity (to the extent such entity is engaged in activities in or affecting commerce (as defined in section 4 of the Federal Trade Commission Act ( 15 U.S.C. 44 ))) that is\u2014\n**(i)**\na person, partnership, or corporation subject to the jurisdiction of the Commission under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ); or\n**(ii)**\nnotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 ; 45(a)(2); 46) or any jurisdictional limitation of the Commission\u2014\n**(I)**\na common carrier subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto; or\n**(II)**\nan organization not organized to carry on business for its own profit or that of its members.\n**(B) Exclusions**\nThe term regulated entity does not include\u2014\n**(i)**\nan entity that is a covered entity, as defined in section 160.103 of title 45, Code of Federal Regulations (or any successor to such regulation), to the extent such entity is acting as a covered entity under the HIPAA privacy regulations (as defined in section 1180(b)(3) of the Social Security Act ( 42 U.S.C. 1320d\u20139(b)(3) ));\n**(ii)**\nan entity that is a business associate, as defined in section 160.103 of title 45, Code of Federal Regulations (or any successor to such regulation), to the extent such entity is acting as a business associate under the HIPAA privacy regulations (as defined in such section 1180(b)(3)); or\n**(iii)**\nan entity that is subject to restrictions on disclosure of records under section 543 of the Public Health Service Act ( 42 U.S.C. 290dd\u20132 ), to the extent such entity is acting in a capacity subject to such restrictions.\n**(7) Service provider**\n**(A) In general**\nThe term service provider means a person who\u2014\n**(i)**\ncollects, retains, uses, or discloses personal reproductive or sexual health information for the sole purpose of, and only to the extent that such person is, conducting business activities on behalf of, for the benefit of, under instruction of, and under contractual agreement with a regulated entity and not any other individual or entity; and\n**(ii)**\ndoes not divulge personal reproductive or sexual health information to any individual or entity other than such regulated entity or a contractor to such service provider bound to information processing terms no less restrictive than terms to which such service provider is bound.\n**(B) Limitation of application**\nSuch person shall only be considered a service provider in the course of activities described in subparagraph (A)(i).\n**(C) Minimization by service providers**\nFor purposes of compliance with section 2 by a service provider of a regulated entity, a request from an individual to such regulated entity for a product or service shall be treated as having also been provided to such service provider.\n**(8) Third party**\nThe term third party means, with respect to the disclosing or collecting of personal reproductive or sexual health information, any person who is not\u2014\n**(A)**\nthe regulated entity that is disclosing or collecting such information;\n**(B)**\nthe individual to whom such information relates; or\n**(C)**\na service provider.\n#### 8. Rule of construction\nNothing in this Act shall be construed to limit or diminish First Amendment freedoms guaranteed under the Constitution.\n#### 9. Relationship to Federal and State laws\n##### (a) Federal law preservation\nNothing in this Act, or a regulation promulgated under this Act, shall be construed to limit any other provision of Federal law, except as specifically provided in this Act.\n##### (b) State law preservation\n**(1) In general**\nNothing in this Act, or a regulation promulgated under this Act, shall be construed to preempt, displace, or supplant any State law, except to the extent that a provision of State law conflicts with a provision of this Act, or a regulation promulgated under this Act, and then only to the extent of the conflict.\n**(2) Greater protection under State law**\nFor purposes of this subsection, a provision of State law does not conflict with a provision of this Act, or a regulation promulgated under this Act, if such provision of State law provides greater privacy protection than the privacy protection provided by such provision of this Act or such regulation.\n#### 10. Savings clause\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law. Nothing in this Act, or a regulation promulgated under this Act, shall be construed to prohibit a regulated entity from disclosing personal reproductive or sexual health information to the Commission as required by law, in compliance with a court order, or in compliance with a civil investigative demand or similar process authorized under law.\n#### 11. Severability clause\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons not similarly situated or to other circumstances, shall not be affected by the invalidation.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-06-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3916",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "My Body, My Data Act of 2025",
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
        "updateDate": "2025-07-01T13:30:46Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2029is.xml"
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
      "title": "My Body, My Data Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "My Body, My Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the privacy of personal reproductive or sexual health information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:32Z"
    }
  ]
}
```
