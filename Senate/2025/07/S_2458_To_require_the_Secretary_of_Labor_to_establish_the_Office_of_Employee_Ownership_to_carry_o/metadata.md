# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2458
- Title: Employee Ownership Financing Act
- Congress: 119
- Bill type: S
- Bill number: 2458
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-09-17T17:00:11Z
- Update date including text: 2025-09-17T17:00:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2458",
    "number": "2458",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Employee Ownership Financing Act",
    "type": "S",
    "updateDate": "2025-09-17T17:00:11Z",
    "updateDateIncludingText": "2025-09-17T17:00:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T18:21:49Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2458is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2458\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Sanders (for himself, Mrs. Shaheen , Mr. Blumenthal , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Labor to establish the Office of Employee Ownership to carry out the Employee Ownership Initiative and establish and carry out the Employee Ownership Loan Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Employee Ownership Financing Act .\n#### 2. Definitions\nIn this Act:\n**(1) Director**\nThe term Director means the Director of the Office of Employee Ownership appointed under section 3(a)(2).\n**(2) Eligible worker-owned cooperative**\nThe term eligible worker-owned cooperative has the meaning given the term in section 1042(c)(2) of the Internal Revenue Code of 1986.\n**(3) Employee stock ownership plan**\nThe term employee stock ownership plan has the meaning given the term in section 4975(e)(7) of the Internal Revenue Code of 1986.\n**(4) Office**\nThe term Office means the Office of Employee Ownership established under section 3(a).\n**(5) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 3. Office of Employee Ownership\n##### (a) Establishment of the Office of Employee Ownership\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish the Office of Employee Ownership in the Department of Labor, outside of the Employee Benefits Security Administration.\n**(2) Director**\nThe Secretary shall appoint the Director of the Office of Employee Ownership to serve as the head of the Office at the pleasure of the Secretary.\n**(3) Staff**\nThe Director may select, appoint, and employ such employees as are necessary to carry out the functions of the Office.\n##### (b) Functions\nThe Director shall be responsible for\u2014\n**(1)**\ncarrying out the Employee Ownership Initiative established under section 346 of the SECURE 2.0 Act of 2022 ( 29 U.S.C. 3228 ); and\n**(2)**\ncarrying out the Employee Ownership Loan Program under section 4.\n#### 4. Employee Ownership Loan Program\n##### (a) Definition of eligible entity\nIn this section, the term eligible entity \u2014\n**(1)**\nmeans\u2014\n**(A)**\nan employee stock ownership plan;\n**(B)**\nan eligible worker-owned cooperative; or\n**(C)**\na qualified trust under section 401(a) of the Internal Revenue Code of 1986, or another entity, on behalf of an employee stock ownership plan or eligible worker-owned cooperative, which other entity may include a company that sponsors an employee stock ownership plan; and\n**(2)**\nexcludes any entity primarily owned by a private equity firm, as defined by the Director.\n##### (b) Loan program\n**(1) In general**\nThe Director shall establish and carry out an Employee Ownership Loan Program to make loans, or loan guarantees, to eligible entities satisfying the requirements under subsection (c) in order to foster increased employee ownership of United States companies and greater employee participation in company decision making throughout the United States.\n**(2) Loans**\n**(A) In general**\nEach loan or loan guarantee made by the Secretary to an eligible entity under this section shall be\u2014\n**(i)**\nto enable the eligible entity to purchase the equity of a company\u2014\n**(I)**\nthat is not less than 51 percent employee-owned; or\n**(II)**\nthat will become not less than 51 percent employee-owned through support from the loan or loan guarantee;\n**(ii)**\nto allow a company that is less than 51 percent employee-owned to become not less than 51 percent employee-owned;\n**(iii)**\nto allow a company that is not less than 51 percent employee-owned to increase the level of employee ownership at the company; or\n**(iv)**\nto allow a company that is not less than 51 percent employee-owned to expand operations and increase or preserve employment.\n**(B) Terms and conditions for loans and loan guarantees**\nNotwithstanding any other provision of law, a loan that is made or guaranteed under this section shall\u2014\n**(i)**\nbear interest at an annual rate that is the lesser of\u2014\n**(I)**\na rate that is sufficient to cover an appropriate amount of the cost of borrowing and losses to the Department of Labor for obligations of comparable maturity, as determined by the Secretary in consultation with the Director; or\n**(II)**\na rate that is equal to the current applicable market rate for a loan of comparable maturity, as determined by the Secretary in consultation with the Director;\n**(ii)**\nhave a repayment period not to exceed 15 years; and\n**(iii)**\nsatisfy applicable requirements of the Internal Revenue Code of 1986 and the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ).\n**(C) Subordination**\nA loan or loan guarantee made under this section may be subordinated to the interests of current and former participants in the employee stock ownership plan or eligible worker-owned cooperative if an eligible entity files for bankruptcy, if determined appropriate by the Director.\n##### (c) Preconditions\nAn eligible entity seeking a loan or loan guarantee under this section shall submit to the Director, at such time, in such manner, and containing such information as the Director may reasonably require, a business plan (and follow-up reporting on the business plan, as determined by the Director) that\u2014\n**(1)**\nin the case of an eligible entity that is an employee stock ownership plan or that is receiving the loan or loan guarantee on behalf of such a plan, demonstrates that\u2014\n**(A)**\nnot less than 51 percent of the equity of the company to be supported by the loan or loan guarantee is or will be owned by an employee stock ownership plan;\n**(B)**\nthe trustee of the plan has full voting rights for the shares and, under the plan, such shares are voted in accordance with section 409(e) of the Internal Revenue Code of 1986;\n**(C)**\nnot fewer than 2 of the members of the board of directors of such company are directors who are not employed by the company, have no other business relationship with the company, and are otherwise independent from the company;\n**(D)**\nthe company will establish a committee, of which not less than 50 percent of the members are employees (but not officers) of the company, that will, not later than 1 year after receipt of the loan or loan guarantee, submit to the Director a plan to establish a system of meaningful employee involvement in any work-related decisions of the company, including decisions with respect to\u2014\n**(i)**\nincreasing workplace democracy;\n**(ii)**\nopen-book management; and\n**(iii)**\nother forms of meaningful employee engagement;\n**(E)**\nthe company offers a diversified investment option for retirement for employees; and\n**(F)**\nall employees of the company will receive basic information about company progress on a quarterly basis as determined by the Director through regulations;\n**(2)**\nin the case of an eligible entity that is an eligible worker-owned cooperative or that is receiving the loan or loan guarantee on behalf of such a cooperative, demonstrates that the board of directors of the company is or will be elected, by members of the eligible worker-owned cooperative on a 1 member to 1 vote basis; and\n**(3)**\ncontains a study from an independent third party with\u2014\n**(A)**\na fair market valuation of the company; and\n**(B)**\na positive determination that the eligible entity should generate enough cash flow to pay back the loan or loan guarantee within the repayment period required under subsection (b)(2)(B)(ii).\n##### (d) Loan portfolio\n**(1) Employee ownership loan program fund**\n**(A) Establishment**\nThere is established in the Treasury of the United States a fund to be known as the Employee Ownership Loan Program Fund .\n**(B) Deposits**\nNotwithstanding section 3302 of title 31, there shall be deposited in the Employee Ownership Loan Program Fund any amount repaid or otherwise received with respect to loans or loan guarantees made under this section, including from any collection effort.\n**(C) Availability of amounts**\nAll amounts deposited in the Employee Ownership Loan Program Fund under subparagraph (B) shall\u2014\n**(i)**\nbe deposited as offsetting collections into the Employee Ownership Loan Program Fund;\n**(ii)**\nbe available to the Director, without further appropriation, to make loans or loan guarantees under this section and for the administrative costs of such loans and loan guarantees; and\n**(iii)**\nremain available to the Director until expended.\n**(2) Limitation of loan portfolio**\nThe principal amount of outstanding loans and loan guarantees made under this section (including using amounts from the Employee Ownership Loan Program Fund) shall not exceed, in the aggregate, $500,000,000 at any one time.\n#### 5. Employee right of first refusal before plant closing\n##### (a) In general\nSection 3 of the Worker Adjustment and Retraining Notification Act ( 29 U.S.C. 2102 ) is amended by adding at the end the following:\n(e) Employee stock ownership plans and eligible worker-Owned cooperatives (1) Opportunity to purchase If an employer orders a plant closing that is a permanent shutdown of an entire facility, the employer shall include in the notice required under subsection (a) an offer for the affected employees of the employer to purchase that plant or facility, or the company of the plant or facility, through either of the following: (A) An employee stock ownership plan, as defined in section 4975(e)(7) of the Internal Revenue Code of 1986, sponsored by a company that is not less than 51 percent employee-owned. (B) An eligible worker-owned cooperative, as defined in section 1042(c)(2) of such Code. (2) Determination of value (A) In general The value of the plant, facility, or company that is the subject of the offer described in paragraph (1) shall be the fair market value of the plant, facility, or company, respectively, as determined by an appraisal that is\u2014 (i) conducted by an independent third party selected in accordance with subparagraph (B); and (ii) paid for by the employer described in paragraph (1). (B) Independent third party The independent third party described in subparagraph (A)(i) shall be\u2014 (i) in the case of a plant, facility, or company to be purchased through an employee stock ownership plan, selected by the trustee of the plan; and (ii) in the case of an eligible worker-owned cooperative, selected jointly by the employer described in paragraph (1) and the affected employees of that employer (or the designated representative of such employees). (C) Disclosures For purposes of determining the value of a plant, facility, or company that is the subject of an employee stock ownership plan or eligible worker-owned cooperative described in paragraph (1), the offer required under such paragraph shall include, with respect to the plant, facility, or company, a disclosure of\u2014 (i) any outstanding liabilities, including any outstanding claims by creditors; (ii) copies of all recent financial statements; (iii) securities filings or related disclosures; (iv) any legal claims filed against the company; (v) any bankruptcy filings; and (vi) any other similar information necessary to determine the full value and financial viability of the plant, facility, or company (and in the case of a plant or company, any facilities of the plant or company). (3) Limitation In the event that the affected employees and employer described in paragraph (1) (or the designated representatives of such employees and employer) enter, in good faith and during the 60-day period after the employer serves the notice required under subsection (a), into negotiations for the purchase of the plant, facility, or company, the plant (and all facilities or operating units at the plant), facility (and all operating units at such facility), or company (and all facilities or operating units at the company), as applicable, shall remain open during such negotiations and for at least the 30-day period following the closing date for such purchase. .\n##### (b) Exemption from prohibited transactions for purchase due to plant closing\n**(1) In general**\nSection 408 of Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1108 ) is amended by adding at the end the following:\n(i) Purchase and operation of employer company, plant, or facility due to plant closing Sections 406 and 407 shall not apply to the purchase and operation of a company, plant, or facility through an employee stock ownership plan (as that term is defined in section 4975(e)(7) of the Internal Revenue Code of 1986) pursuant to section 3(e) of the Worker Adjustment and Retraining Notification Act ( 29 U.S.C. 2102(e) ). .\n**(2) Conforming amendments to the Internal Revenue Code of 1986**\n**(A) In general**\nSubsection (d) of section 4975 of the Internal Revenue Code of 1986 is amended by striking or at the end of paragraph (24), by striking the period at the end of paragraph (25) and inserting , or , and by adding at the end the following new paragraph:\n(26) the purchase and operation of a company, plant, or facility through an employee stock ownership plan pursuant to section 3(e) of the Worker Adjustment and Retraining Notification Act ( 29 U.S.C. 2102(e) ). .\n**(B) Exemption from owner-employee rules**\nSubparagraph (A) of section 4975(f)(6) of such Code is amended by striking (9) and (12) and inserting (9), (12), and (26) .\n#### 6. Advisory Council on Employee Ownership\n##### (a) In general\n**(1) Establishment**\nThere is hereby established an Advisory Council on Employee Ownership (hereinafter in this section referred to as the Council ) consisting of 7 members appointed by the Secretary.\n**(2) Membership**\n**(A) In general**\nOf the 7 members of the Council\u2014\n**(i)**\n4 shall be appointed to represent employees;\n**(ii)**\n1 shall be appointed to represent companies that have established an employee stock ownership plan or eligible worker-owned cooperative;\n**(iii)**\n1 shall be appointed to represent employee stock ownership plan providers; and\n**(iv)**\n1 shall be appointed to represent associations or other membership organizations for employee stock ownership plans or eligible worker-owned cooperatives.\n**(B) Political affiliation**\nNot more than 4 members of the Council shall be members of the same political party.\n**(3) Terms**\nMembers of the Council shall serve for terms of 2 years.\n**(4) Appointment; reappointment**\nA member of the Council may be reappointed to serve additional terms.\n**(5) Vacancies**\nA member of the Council appointed to fill a vacancy shall be appointed only for the remainder of such term.\n**(6) Quorum**\nA majority of members of the Council shall constitute a quorum and action shall be taken only by a majority vote of those present and voting.\n##### (b) Duties and functions\n**(1) In general**\nIt shall be the duty of the Council to advise the Secretary with respect to the carrying out of the functions of the Secretary under this Act and to submit to the Secretary recommendations with respect to carrying out such duties.\n**(2) Meetings**\nThe Council shall meet at least 4 times each year and at such other times as the Secretary requests.\n**(3) Report**\nThe Council shall annually submit a report to the Secretary on the recommendations described in paragraph (1).\n##### (c) Executive Secretary; Secretarial and clerical services\nThe Secretary shall furnish to the Council an Executive Secretary and such secretarial, clerical, and other services as are determined necessary to conduct the business of the Council. The Secretary may call upon other agencies of the Federal Government for statistical data, reports, and other information which will assist the Council in the performance of its duties.\n##### (d) Compensation\n**(1) In general**\nMembers of the Council shall each be entitled to receive the daily equivalent of the annual rate of basic pay in effect for level IV of the Executive Schedule under section 5315 of title 5, United States Code for each day (including travel time) during which they are engaged in the actual performance of duties vested in the Council.\n**(2) Travel expenses**\nWhile away from their homes or regular places of business in the performance of services for the Council, members of the Council shall be allowed travel expenses, including per diem in lieu of subsistence, in the same manner as persons employed intermittently in the Government service are allowed expenses under section 5703 of title 5, United States Code.\n##### (e) Termination\nSection 1013 of title 5, United States Code, relating to termination, shall not apply to the Council.\n#### 7. Regulations or guidance\nNot later than 1 year after the date of enactment of this Act, the Secretary shall prescribe such regulations or guidance as are necessary to implement sections 3, 4, and 6.\n#### 8. Authorization of appropriations\n##### (a) Loan program\nThere are authorized to be appropriated to the Employee Ownership Loan Program Fund established under section 4\u2014\n**(1)**\n$500,000,000 for fiscal year 2026, to remain available until expended, to make loans or loan guarantees under such section during such fiscal year and subsequent fiscal years;\n**(2)**\n$5,000,000 for fiscal year 2026, to remain available until September 30, 2026, for administrative costs in establishing the program under such section; and\n**(3)**\nsuch sums as may be necessary for fiscal year 2027, and each subsequent fiscal year, for administrative costs in carrying out the program during such fiscal years.\n##### (b) Additional authorizations\nThere are authorized to be appropriated to the Secretary to carry out this Act, other than section 4, such sums as may be necessary for each fiscal year.",
      "versionDate": "2025-07-24",
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
        "updateDate": "2025-09-17T17:00:11Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2458is.xml"
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
      "title": "Employee Ownership Financing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Employee Ownership Financing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Labor to establish the Office of Employee Ownership to carry out the Employee Ownership Initiative and establish and carry out the Employee Ownership Loan Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:23Z"
    }
  ]
}
```
