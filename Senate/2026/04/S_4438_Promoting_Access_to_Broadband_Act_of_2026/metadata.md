# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4438?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4438
- Title: Promoting Access to Broadband Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4438
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-14T17:00:47Z
- Update date including text: 2026-05-14T17:00:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2131-2132)
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2131-2132)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4438",
    "number": "4438",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Promoting Access to Broadband Act of 2026",
    "type": "S",
    "updateDate": "2026-05-14T17:00:47Z",
    "updateDateIncludingText": "2026-05-14T17:00:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2131-2132)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T20:34:35Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4438is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4438\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Durbin (for himself, Mr. Padilla , Mr. Blumenthal , Mr. Markey , Ms. Klobuchar , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Federal Communications Commission to establish a program to make grants available to States to inform individuals of potential eligibility for the Lifeline program of the Commission, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Access to Broadband Act of 2026 .\n#### 2. Lifeline enrollment outreach grants\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Covered individual**\nThe term covered individual means an individual who\u2014\n**(A)**\nis an eligible-but-not-enrolled individual; or\n**(B)**\nhas the potential to be a qualifying low-income consumer under 54.409 of title 47, Code of Federal Regulations, or any successor regulation, due to the eligibility of the individual, a dependent of the individual, or the household of the individual to receive benefits from or participate in, as applicable, a program described in such section 54.409.\n**(3) Eligible-but-not-enrolled individual**\nThe term eligible-but-not-enrolled individual means an individual who is a qualifying low-income consumer under section 54.409 of title 47, Code of Federal Regulations, or any successor regulation, but is not enrolled in the Lifeline program.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term Indian tribe in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(5) Lifeline program**\nThe term Lifeline program means the program set forth in subpart E of part 54 of title 47, Code of Federal Regulations, or any successor regulation.\n**(6) Reach**\nThe term reach means, with respect to an individual, to inform the individual of potential eligibility for the Lifeline program and to provide the individual with information about the Lifeline program, as described in subsection (e).\n**(7) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each Indian Tribe.\n##### (b) Establishment\nThe Commission shall establish a competitive program to make grants available to States to inform covered individuals of potential eligibility for the Lifeline program.\n##### (c) Application\n**(1) In general**\nThe Commission may only award a grant under this section to a State that submits an application at such time, in such form, and with such information and assurances as the Commission may require.\n**(2) Matters required to be included**\nAn application submitted by a State under paragraph (1) shall include\u2014\n**(A)**\nthe number of covered individuals in the State;\n**(B)**\na plan for the activities that the State will conduct using grant funds, including a list of each agency within the State that will assist in carrying out those activities; and\n**(C)**\nan estimate of the percentage of eligible-but-not-enrolled individuals in the State who will be reached by those activities.\n##### (d) Selection\n**(1) Minimum number of States**\nThe Commission shall award grants under this section to not fewer than 25 percent of the States that submit an application under subsection (c).\n**(2) Factors for consideration**\nIn awarding grants under this section, the Commission shall give favorable consideration to\u2014\n**(A)**\nStates that have higher numbers of covered individuals; and\n**(B)**\nStates proposing, in the plans submitted under subsection (c)(2)(B), to conduct activities that have the potential to reach higher percentages of eligible-but-not-enrolled individuals in those States, as determined by the Commission, taking into consideration the estimates submitted under subsection (c)(2)(C).\n**(3) Geographic diversity**\nIn awarding grants under this section, the Commission shall, to the maximum extent practicable, select States from different geographic regions of the United States.\n##### (e) Use of funds\n**(1) In general**\nA State that receives a grant under this section shall use grant funds, in accordance with the plan included in the application of the State under subsection (c)(2)(B), to\u2014\n**(A)**\ninform covered individuals and organizations or agencies that serve covered individuals, as the case may be under the terms of the grant awarded to the State, of potential eligibility for the Lifeline program;\n**(B)**\nprovide covered individuals with information about the Lifeline program, including\u2014\n**(i)**\nhow to apply for the Lifeline program; and\n**(ii)**\na description of the prohibition on more than 1 subscriber in each household receiving a service provided under the Lifeline program; and\n**(C)**\npartner with nonprofit and community-based organizations that have a proven track record of working with covered individuals in implementing digital inclusion initiatives to provide covered individuals with\u2014\n**(i)**\nassistance applying for the Lifeline program; and\n**(ii)**\ninformation about product and technology choices.\n**(2) Multiple State agencies**\nA State that receives a grant under this section may provide grant funds to 1 or more agencies located within the State, as identified under subsection (c)(2)(B), to carry out the activities under the grant.\n##### (f) Outreach to States regarding grant program\nBefore accepting applications for the grant program established under this section, the Commission shall conduct outreach to States to ensure that States are aware of the grant program and how to apply for a grant under the grant program.\n##### (g) Regulations required\nNot later than 30 days after the date of enactment of this Act, the Commission shall promulgate regulations to implement this section.\n##### (h) Enforcement\n**(1) In general**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) or a regulation promulgated under that Act.\n**(2) Manner of enforcement**\nThe Commission shall enforce this section and the regulations promulgated under this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) were incorporated into and made a part of this section.\n##### (i) Exemptions\n**(1) Certain rulemaking requirements**\nSection 553 of title 5, United States Code, shall not apply to a regulation promulgated under this section or a rulemaking proceeding to promulgate such a regulation.\n**(2) Paperwork Reduction Act requirements**\nA collection of information conducted or sponsored under the regulations required under this section shall not constitute a collection of information for the purposes of subchapter I of chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ).\n##### (j) Report to Congress\n**(1) In general**\nNot later than 3 years after establishing the grant program under this section, the Commission shall submit to Congress a report evaluating the effectiveness of the grant program.\n**(2) Contents**\nThe report submitted under paragraph (1) shall include\u2014\n**(A)**\nthe number of individuals notified of Lifeline program eligibility by States receiving grants under this section;\n**(B)**\nthe number of new applicants to the Lifeline program from States receiving grants under this section, including the number of those applicants who enrolled in the Lifeline program; and\n**(C)**\nthe cost-effectiveness of the grant program established under this section.\n##### (k) Authorization of appropriations\nThere is authorized to be appropriated to the Commission such sums as may be necessary to carry out this section for the first 5 full fiscal years beginning after the establishment of the grant program under this section.\n#### 3. Grants to States to strengthen National Lifeline Eligibility Verifier\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Eligible entity**\nThe term eligible entity means a State that, not later than 30 days after the date of enactment of this Act, submits to the Commission an application for a grant under this section containing such information as the Commission may require.\n**(3) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n##### (b) Establishment\nNot later than 90 days after the date of enactment of this Act, the Commission shall establish a program to provide a grant, from amounts appropriated under subsection (e), to each eligible entity for the purpose described in subsection (c).\n##### (c) Purpose\nThe Commission shall make a grant to each eligible entity for the purpose of establishing, renewing, reestablishing, or maintaining or amending a connection between the databases of the eligible entity that contain information concerning the receipt by a household, or a member of a household, of benefits under a program administered by the eligible entity (including any benefit provided under the supplemental nutrition assistance program under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. )) and the National Lifeline Eligibility Verifier so that the receipt by a household, or a member of a household, of benefits under the benefits program\u2014\n**(1)**\nis reflected in the National Lifeline Eligibility Verifier; and\n**(2)**\ncan be used to verify eligibility for the Lifeline program set forth in subpart E, part 54, of title 47, Code of Federal Regulations, or any successor regulation.\n##### (d) Disbursement of grant funds\nNot later than 120 days after the date on which the Commission establishes the program under subsection (b), funds provided under each grant made under that subsection shall be disbursed to the eligible entity receiving the grant.\n##### (e) Authorization of appropriation\nThere is authorized to be appropriated such sums as may be necessary to carry out this section.",
      "versionDate": "2026-04-29",
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8576",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Promoting Access to Broadband Act of 2026",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-05-14T17:00:47Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4438is.xml"
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
      "title": "Promoting Access to Broadband Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Access to Broadband Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Federal Communications Commission to establish a program to make grants available to States to inform individuals of potential eligibility for the Lifeline program of the Commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:42Z"
    }
  ]
}
```
