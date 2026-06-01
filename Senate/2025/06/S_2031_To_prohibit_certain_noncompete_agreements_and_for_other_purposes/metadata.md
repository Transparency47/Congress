# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2031?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2031
- Title: Workforce Mobility Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2031
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-07-22T12:43:08Z
- Update date including text: 2025-07-22T12:43:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2031",
    "number": "2031",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Workforce Mobility Act of 2025",
    "type": "S",
    "updateDate": "2025-07-22T12:43:08Z",
    "updateDateIncludingText": "2025-07-22T12:43:08Z"
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
        "item": {
          "date": "2025-06-11T17:38:18Z",
          "name": "Referred To"
        }
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "IN"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2031is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2031\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Murphy (for himself, Mr. Young , Mr. Cramer , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit certain noncompete agreements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Workforce Mobility Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe proliferation of noncompete agreements throughout sectors, occupational categories, and income brackets is contrary to the commitment of Congress to foster stronger wage growth for workers in the United States. Economists now estimate that 1 in 5 workers is covered by a noncompete agreement.\n**(2)**\nNoncompete agreements are blunt instruments that crudely protect employer interests and place a drag on national productivity by forcing covered workers to either idle for long periods of time or leave the industries in which the workers have honed their skills altogether.\n**(3)**\nEnforceable noncompete agreements also reduce wages, restrict worker mobility, impinge on the freedom of a worker to maximize labor market potential, and slow the pace of innovation in the United States.\n**(4)**\nEmployers have access to legal recourses to protect their legitimate interests and property, including trade secret protections, intellectual property protections, and nondisclosure agreements that do not inflict broad collateral harm on the labor market prospects for workers.\n**(5)**\nEmployers that rely on a list or lists of vendors, customers, or clients that are not easily obtained by an individual through means other than the work relationship have adequate legal protection through the use of trade secret protections and nondisclosure agreements.\n**(6)**\nNoncompete agreements broadly restrict employment options for workers in the United States when more narrowly targeted remedies are readily available to employers.\n**(7)**\nFostering an environment where employers can flourish is necessary to promote vitality and prosperity in the economy.\n**(8)**\nEmployers may retain critical skilled employees while ensuring that disincentives affecting mobility, including noncompete agreements, do not negatively impact the workforce in the United States.\n#### 3. Prohibiting noncompete agreements\n##### (a) Prohibition\n**(1) In general**\nExcept as provided in subsection (b), no person shall enter into, enforce, or attempt to enforce a noncompete agreement with any individual who is employed by, or performs work under contract with, such person with respect to the activities of such person in or affecting commerce.\n**(2) Effect of agreements**\nExcept as provided in subsection (b), a noncompete agreement described in paragraph (1) shall have no force or effect.\n##### (b) Exceptions\n**(1) Sale of goodwill or ownership interest**\n**(A) In general**\nA seller of a business entity may enter into an agreement with the buyer to refrain from carrying on a like business within a specified geographic area described in subparagraph (C), if the buyer, or any person deriving title to the goodwill of the business entity or an ownership interest in the business entity from the buyer, carries on a like business in such specified geographic area.\n**(B) Senior executive officials with severance agreements**\n**(i) In general**\nSubject to clause (ii), a buyer or seller of a business entity may enter into a noncompete agreement with a senior executive official who has a severance agreement described in clause (iii) that restricts the senior executive official from performing, within a specified geographic area described in subparagraph (C), any work that is similar to the work that the senior executive official performed for the buyer or seller, if the buyer, or any person deriving title to the goodwill of the business entity or an ownership interest in the business entity from the buyer, carries on a like business in such specified geographic area.\n**(ii) Time-limited agreement**\nA noncompete agreement described in clause (i) may not restrict the senior executive official as described in such clause for a period that is more than one year.\n**(iii) Severance agreement**\nA severance agreement described in this clause is an agreement between the buyer or seller of a business entity and a senior executive official that\u2014\n**(I)**\nis part of the terms and conditions of the sale; and\n**(II)**\nrequires monetary compensation for the senior executive official in the event of termination of the employment of the senior executive official at an amount that is not less than the compensation that the senior executive official is or would be reasonably expected to receive from the buyer during the 1-year period following the sale.\n**(C) Specified geographic area**\nA specified geographic area described in this subparagraph is a geographic area\u2014\n**(i)**\nthat is specified in an agreement described in subparagraph (A), or a noncompete agreement described in subparagraph (B), regarding a business entity; and\n**(ii)**\nin which such business entity, including any division or subsidiary of such business entity, conducted business prior to the agreement or noncompete agreement.\n**(2) Partnership dissolution or disassociation**\n**(A) In general**\nAny partner of a partnership may enter into an agreement with any other member of the partnership that, upon the dissolution of the partnership or dissociation of the partner from such partnership, the partner will refrain from carrying on a like business within a specified geographic area described in subparagraph (B), if any other member of the partnership, or any person deriving title to the partnership or the goodwill of the partnership from any other member of the partnership, carries on a like business in such specified geographic area.\n**(B) Specified geographic area**\nA specified geographic area described in this subparagraph is a geographic area\u2014\n**(i)**\nthat is specified in an agreement described in subparagraph (A); and\n**(ii)**\nin which any business of the partnership has been transacted prior to the agreement.\n#### 4. Trade secrets\nNothing in this Act shall preclude a person from entering into an agreement with an individual who is employed by, or performs work under contract with, such person with respect to the activities of such person in or affecting commerce to not disclose any information (including after the individual is no longer employed or performing work for the person) regarding the person, or the work performed by the individual for the person, that is a trade secret.\n#### 5. Notice; public awareness campaign\n##### (a) Notice\nAny person who engages an individual who is employed by, or performs work under contract with, such person with respect to the activities of such person in or affecting commerce shall post and maintain notice of the provisions of this Act\u2014\n**(1)**\nin a conspicuous place on the premises of such person; or\n**(2)**\nin a conspicuous place where notices to employees and applicants for employment are customarily posted physically or electronically by such person.\n##### (b) Public awareness campaign\nThe Secretary of Labor may carry out activities to make the public aware of the provisions of this Act.\n#### 6. Enforcement\n##### (a) Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 3 or 5(a) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nThe Federal Trade Commission shall enforce sections 3 and 5(a) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates section 3 or 5(a) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n##### (b) Department of Labor\n**(1) In general**\nThe Secretary of Labor\u2014\n**(A)**\nshall investigate as the Secretary determines necessary to determine violations of section 3 or 5(a) by an employer; and\n**(B)**\nmay, subject to paragraph (2), bring an action in any court of competent jurisdiction to obtain the legal or equitable relief against an employer on behalf of an individual aggrieved by the violation as may be appropriate to effectuate the purposes of such sections.\n**(2) Statute of limitations**\nAn action described in paragraph (1)(B) may not be commenced later than 4 years after the date on which the violation occurred.\n**(3) Regulations**\nNot later than 18 months after the date of enactment of this Act, the Secretary of Labor, in consultation with the Chair of the Federal Trade Commission, shall issue regulations as necessary to carry out this Act, including with respect to the authority of the Secretary of Labor to enforce violations of section 3 or 5(a) in accordance with paragraph (1).\n##### (c) Standards for dual enforcement\nNot later than 1 year after the date of enactment of this Act, the Federal Trade Commission and the Secretary of Labor shall, for the purposes of enforcing this Act\u2014\n**(1)**\ndevelop shared standards for consistent enforcement; and\n**(2)**\nidentify the scope of responsibility of the Federal Trade Commission and such scope of the Secretary of Labor to ensure complementary enforcement of this Act.\n##### (d) Reporting violations\n**(1) In general**\nThe Federal Trade Commission and the Secretary of Labor shall each establish a system to receive complaints by individuals regarding alleged violations of section 3.\n**(2) Confidentiality**\nExcept as otherwise required by law, the Federal Trade Commission and the Secretary of Labor may not disclose the identity or identifying information of any individual providing a complaint under paragraph (1), without explicit consent from the individual.\n##### (e) Private right of action\n**(1) In general**\nAn individual who is aggrieved by a violation of this Act may bring a civil action in any appropriate district court of the United States.\n**(2) Relief**\nIn a civil action under paragraph (1), a court may award\u2014\n**(A)**\nany actual damages sustained by the individual as a result of the violation; and\n**(B)**\nin the case of any successful action, the costs of the action and reasonable attorney\u2019s fees, as determined by the court.\n##### (f) Enforcement by States\n**(1) In general**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by any person who violates any provision of section 3 or 5(a) or any rule promulgated under this Act to carry out such section, the attorney general of the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin any further such violation by the person;\n**(B)**\ncompel compliance with section 3 or 5(a) or any such rule;\n**(C)**\nobtain a permanent, temporary, or preliminary injunction;\n**(D)**\nobtain damages, restitution, or other compensation on behalf of the residents of the State; or\n**(E)**\nobtain any other appropriate equitable relief.\n**(2) Preservation of state powers**\nNothing in this subsection shall be construed as altering, limiting, or affecting the authority of the attorney general of a State to\u2014\n**(A)**\nbring an action or other regulatory proceeding arising solely under the laws in effect in that State; or\n**(B)**\nexercise the powers conferred on the attorney general by the laws of the State, including the ability to conduct investigations, administer oaths or affirmations, or compel the attendance of witnesses or the production of documentary or other evidence.\n##### (g) Arbitration and class action\nNotwithstanding any other provision of law, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to any alleged violation of section 3 or 5(a).\n#### 7. Reports\nNot later than 1 year after the date on which the Secretary of Labor issues any regulations under section 6(b)(3), the Federal Trade Commission and the Secretary of Labor shall each submit to Congress a report on any actions taken by the Federal Trade Commission or Secretary, respectively, to enforce the provisions of this Act.\n#### 8. Definitions\nFor purposes of this Act:\n**(1) Business entity**\nThe term business entity means any partnership (including a limited partnership or a limited liability partnership), limited liability company (including a series of a limited liability company formed under the laws of a jurisdiction that recognizes such a series), or corporation.\n**(2) Buyer**\nThe term buyer , with respect to a business entity, means any person who buys the goodwill of the business entity, buys or otherwise acquires ownership interest in the business entity, or buys a qualified asset or interest with regard to the business entity.\n**(3) Class action**\nThe term class action means a lawsuit in which 1 or more parties seek or obtain class treatment pursuant to rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law.\n**(4) Commerce**\nThe term commerce has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(5) Employ; Employee; employer**\nThe terms employ , employee , and employer have the meanings given such terms in section 3 of such Act ( 29 U.S.C. 203 ).\n**(6) Noncompete agreement**\nThe term noncompete agreement means an agreement, entered into after the date of enactment of this Act between a person and an individual performing work for the person, that restricts such individual, after the working relationship between the person and individual terminates, from performing\u2014\n**(A)**\nany work for another person for a specified period of time;\n**(B)**\nany work in a specified geographical area; or\n**(C)**\nany work for another person that is similar to such individual\u2019s work for the person that is a party to such agreement.\n**(7) Owner of a business entity**\nThe term owner of a business entity means\u2014\n**(A)**\nin the case of a business entity that is a partnership (including a limited partnership or a limited liability partnership), any partner;\n**(B)**\nin the case of a business entity that is a limited liability company (including a series of a limited liability company formed under the laws of a jurisdiction that recognizes such a series), any member of such company; or\n**(C)**\nin the case of a business entity that is a corporation, a capital stockholder of the business entity who owns not less than 5 percent of the capital stock.\n**(8) Ownership interest**\nThe term ownership interest means\u2014\n**(A)**\nin the case of a business entity that is a partnership (including a limited partnership or a limited liability partnership), a partnership interest;\n**(B)**\nin the case of a business entity that is a limited liability company (including a series of a limited liability company formed under the laws of a jurisdiction that recognizes such a series), a membership interest; or\n**(C)**\nin the case of a business entity that is a corporation, not less than 5 percent of the capital stock of the business entity or, as applicable, a subsidiary of the business entity.\n**(9) Person**\nThe term person has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(10) Predispute arbitration agreement**\nThe term predispute arbitration agreement means an agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement.\n**(11) Predispute joint-action waiver**\nThe term predispute joint-action waiver means an agreement, whether or not part of a predispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement.\n**(12) Qualified asset or interest**\nThe term qualified asset or interest , with respect to a business entity, means an asset or interest that is\u2014\n**(A)**\nall or substantially all of the operating assets and the goodwill of the business entity;\n**(B)**\nall or substantially all of the operating assets of a division, or a subsidiary, of the business entity and the goodwill of that division or subsidiary; or\n**(C)**\nall of the ownership interest of any subsidiary of the business entity.\n**(13) Sale**\nThe term sale , with respect to a business entity, means the sale of the goodwill of the business entity, the sale or other disposal of all of the ownership interest of a seller in the business entity, or the sale of a qualified asset or interest with regard to the business entity.\n**(14) Seller**\nThe term seller , with respect to a business entity, means any person who sells the goodwill of the business entity, any owner of the business entity selling or otherwise disposing of all of his or her ownership interest in the business entity, or any owner of the business entity that sells a qualified asset or interest with regard to the business entity.\n**(15) Senior executive official**\nThe term senior executive official , with respect to a sale, means an official who was acquired as an employee of the buyer in such sale through the terms and conditions of the sale, and, on the day before the date of such sale\u2014\n**(A)**\nwho was employed by the seller in such sale;\n**(B)**\nwho was responsible for making or directing major decisions of the seller; and\n**(C)**\nwhose rate of compensation was in the highest 10 percent of the compensation rates for all employees of the seller.\n**(16) Trade secret**\nThe term trade secret has the meaning given the term in section 1839 of title 18, United States Code.",
      "versionDate": "2025-06-11",
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
        "name": "Labor and Employment",
        "updateDate": "2025-07-22T12:43:08Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2031is.xml"
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
      "title": "Workforce Mobility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Workforce Mobility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain noncompete agreements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:40Z"
    }
  ]
}
```
