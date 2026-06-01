# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4212
- Title: Prioritizing the Warfighter in Defense Contracting Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4212
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4212",
    "number": "4212",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Prioritizing the Warfighter in Defense Contracting Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T22:30:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "MO"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4212is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4212\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Ms. Warren (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require contractors of the Department of Defense to prioritize meeting warfighter needs over the purchase of their own securities and executive compensation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Prioritizing the Warfighter in Defense Contracting Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Oversight and Government Reform of the House of Representatives.\n**(2) Covered employee**\nThe term covered employee means an employee, executive, or officer.\n**(3) Equity security**\nThe term equity security has the meaning given such term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ).\n**(4) Covered compensation**\nThe term covered compensation \u2014\n**(A)**\nmeans\u2014\n**(i)**\nsalary;\n**(ii)**\nbonuses;\n**(iii)**\nany compensation that is granted, earned, or vested based wholly or in part upon the attainment of any financial reporting measure or other performance metric;\n**(iv)**\nequity-based compensation;\n**(v)**\ntime- or service-based awards;\n**(vi)**\nawards based on nonfinancial metrics; and\n**(vii)**\nany profits realized from the buying or selling of securities; and\n**(B)**\ndoes not include\u2014\n**(i)**\nroutine employee 401(k) plans; or\n**(ii)**\nemployee stock ownership plans.\n**(5) Large contractor**\nThe term large contractor means a contractor that received more than $250,000,000 in annual revenue from contracts or licenses from the Department of Defense in any of the previous 3 years.\n**(6) National securities exchange**\nThe term national securities exchange means an exchange registered as a national securities exchange in accordance with section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ).\n**(7) Short-term financial metrics**\nThe term short-term financial metrics means\u2014\n**(A)**\nfree cash flow;\n**(B)**\noperating cash flow; and\n**(C)**\nearnings per share driven by stock buy-backs.\n#### 3. Limitations on contractors of Department of Defense\n##### (a) In general\nThe Secretary of Defense may not enter into a contract with a large contractor for the procurement of goods or services unless such contractor agrees in writing that\u2014\n**(1)**\nthe entity shall not\u2014\n**(A)**\npurchase an equity security of such entity, or any parent entity of such entity, that is listed on a national securities exchange; or\n**(B)**\npay dividends or make any other capital distribution with respect to the equity securities of the entity; and\n**(2)**\nthe covered compensation of a covered employee of such entity shall\u2014\n**(A)**\ncomply with the requirements of section 3744 of title 10, United States Code;\n**(B)**\nnot be linked to short-term financial metrics; and\n**(C)**\nnot exceed $5,000,000 per calendar year.\n##### (b) Compliance plan and procedures\n**(1) In general**\nAny contractor subject to the requirements of subsection (a) shall develop and implement a plan to prevent the activities prohibited under that subsection.\n**(2) Certification**\nPrior to entering into a contract with the Department of Defense, and annually thereafter for the duration of the contract, a contractor shall submit to the contracting officer of the Department a certification that to the best of the knowledge of the contractor, neither the contractor nor any covered employee of the contractor is engaged in any of the activities prohibited under subsection (a).\n##### (c) Waiver authority\n**(1) Identification of contractors eligible for waiver**\nBeginning on the date of the enactment of this Act, and on a rolling basis thereafter, the Secretary of Defense\u2014\n**(A)**\nshall review and determine whether a large contractor meets the contractor metrics described in paragraph (4); and\n**(B)**\nfor any large contractor assessed by the Secretary to meet such metrics, may grant the contractor a waiver of the requirements of subsection (a).\n**(2) Notice**\nFor any waiver granted under paragraph (1), the Secretary shall submit to the appropriate congressional committees notification of the waiver that includes justification for the waiver.\n**(3) Annual review**\n**(A) In general**\nFor any contractor granted a waiver under paragraph (1), the Secretary shall conduct, not later than 1 year after the date on which the contractor was granted a waiver under such paragraph and not less frequently than once a year thereafter, a review to determine whether the contractor continues to meet the metrics described in paragraph (4).\n**(B) Authority to revoke waiver**\nThe Secretary may revoke a waiver issued to any contractor that the Secretary determines, during a review conducted pursuant to subparagraph (A), no longer meets the metrics described in paragraph (4).\n**(4) Contractor metrics**\nThe contractor metrics described in this paragraph are as follows:\n**(A)**\nNot less than 80 percent of the time during the preceding fiscal year, the contractor met contract requirements regarding delivery dates with demonstrated, fieldable capability or associated technical achievement.\n**(B)**\nNot less than 80 percent of the time during the preceding fiscal year, the contractor met contract readiness requirements.\n**(C)**\nNot less than 80 percent of the time during the preceding fiscal year, the contractor demonstrated technical performance metrics and regular value assessments with the user community.\n**(D)**\nNot less than 80 percent of the time during the preceding fiscal year, the contractor responded to requests for certified or uncertified cost or pricing data by the due date stated in the request for submissions.\n**(5) Rule of construction**\nNothing in this subsection may be construed to supersede existing limitations that restrict Federal funds from being used for contractor employee compensation.\n##### (d) Review and enforcement\n**(1) Establishment of formal review process**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Defense shall establish a formal review mechanism for identifying, on a continuing basis, Defense contractors that are in violation of the requirements of subsection (a).\n**(2) Renegotiation of existing contracts**\n**(A) Review and identification**\nThe Secretary shall review all contracts in existence on the day before the date of the enactment of this Act and identify any contract to be modified in the interest of the Department.\n**(B) Renegotiation**\nFor each contract identified by the Secretary pursuant to subparagraph (A), the Secretary shall renegotiate such contract in accordance with the requirements of this section.\n**(3) Evidence and notification of violation**\n**(A) In general**\nIf a contracting officer of the Department finds, or receives and substantiates, an allegation described in subparagraph (B), the Secretary shall\u2014\n**(i)**\nimmediately notify the contractor of the violation in writing; and\n**(ii)**\ntrack and continually update the allegation in the Contractor Performance Assessment Reporting System and the System for Award Management of the General Services Administration, for shared use across contracting officers.\n**(B) Allegation described**\nAn allegation described in this subparagraph is any allegation relating to\u2014\n**(i)**\na contractor of the Department or any covered employee of such contractor engaging in an activity prohibited under subsection (a), if the requirements of such subsection have not been waived under subsection (c)(1); or\n**(ii)**\na contractor who received a waiver under subsection (c)(1) that is underperforming with respect to prioritization, investment, or production such that the contractor no longer meets the contractor metrics described in subsection (c)(4).\n**(C) Contents of notice**\nThe notice issued under subparagraph (A)(i) shall include, depending on the basis of the violation, a description of\u2014\n**(i)**\nthe conduct of the contractor or the covered employee of the contractor that is prohibited under subsection (a); or\n**(ii)**\nthe nature of the underperformance or insufficient prioritization, investment, or production speed of the contractor that fails to meet the contractor metrics described in subsection (c)(4).\n**(4) Remediation**\n**(A) In general**\nNot later than 15 days after the date on which the contractor receives the notice of a violation under paragraph (3)(A)(i), the contractor may submit to the Secretary a remediation plan, approved by the board of directors of the contractor, for review by the Secretary.\n**(B) Content of plan**\nThe remediation plan submitted under subparagraph (A) shall include a description of the manner by which the contractor shall remedy the violation, including, if applicable, a strategy for meeting the contractor metrics described in subsection (c)(4).\n**(C) Identification of deficiencies**\nIf the Secretary identifies deficiencies in the remediation plan submitted under subparagraph (A), the Secretary shall engage with the contractor as needed to resolve such deficiencies.\n**(5) Penalties**\nIf a contractor engages in an activity prohibited under subsection (a) and was not granted a waiver under subsection (c)(1) or if the contractor was granted a waiver under subsection (c)(1) but no longer meets the contractor metrics described in subsection (c)(4), the contracting officer of the Department may take one or more of the following actions against the contractor:\n**(A)**\nSuspend payment under one or more contracts, at the discretion of the Department.\n**(B)**\nRevoke the waiver issued under subsection (c)(1).\n**(C)**\nTerminate the eligibility of the contractor to receive progress payments under section 3804 of title 10, United States Code.\n**(D)**\nTerminate the contract for default or cause in accordance with the termination clause for the contract.\n**(E)**\nRefer the matter to the Secretary to claw back all or part of the covered compensation given to a covered employee.\n**(F)**\nRefer the matter to the relevant suspension and debarment official.\n**(G)**\nRefer the matter to the Secretary for other administrative actions.\n**(H)**\nRefer the matter to the Attorney General for prosecution under any applicable law.\n**(I)**\nCease advocacy for the contractor for foreign military sales and direct commercial sales.\n**(J)**\nProhibit the Department from entering into a new contract with the contractor.\n##### (e) Reports to Congress\n**(1) Annual report**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary of Defense shall submit to the appropriate congressional committees a report that includes, for the one-year period preceding submission of the report\u2014\n**(i)**\na list of all contractors subject to the requirements of subsection (a);\n**(ii)**\nfor each contractor, a copy of the certification submitted under subsection (b)(2);\n**(iii)**\na list of all contractors granted a waiver under subsection (c)(1) and the justification for each waiver; and\n**(iv)**\na list of all entities that have violated the certification submitted under subsection (b)(2) or diverged from the practices that justified the granting of a waiver under subsection (c)(1).\n**(B) Publication**\nNot later than 30 days after the date of submission of the report under subparagraph (A), the Secretary shall make the report publicly available.\n**(2) Quarterly report**\nNot later than 90 days after the date of the enactment of this Act, and not less frequently than once every 90 days thereafter, the Secretary shall submit to the appropriate congressional committees a report that includes, for the period covered by the report\u2014\n**(A)**\na list of all of the contractors that submitted a request for a waiver under subsection (c)(1); and\n**(B)**\nthe unclassified summaries of the materials submitted by such contractors to the Department in support of the requests for a waiver.",
      "versionDate": "2026-03-25",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-15T01:25:57Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4212is.xml"
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
      "title": "Prioritizing the Warfighter in Defense Contracting Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prioritizing the Warfighter in Defense Contracting Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require contractors of the Department of Defense to prioritize meeting warfighter needs over the purchase of their own securities and executive compensation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:38Z"
    }
  ]
}
```
