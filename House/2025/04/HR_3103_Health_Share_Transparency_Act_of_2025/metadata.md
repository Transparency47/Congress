# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3103
- Title: Health Share Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3103
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-05-21T14:01:25Z
- Update date including text: 2025-05-21T14:01:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3103",
    "number": "3103",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Health Share Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-21T14:01:25Z",
    "updateDateIncludingText": "2025-05-21T14:01:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:05:00Z",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MD"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "TN"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3103ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3103\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Huffman (for himself, Mr. Raskin , Mr. Casten , Ms. Norton , Ms. Tlaib , Mr. Pocan , Mr. Moulton , Mr. Cohen , and Mr. Frost ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to establish requirements for the disclosure of certain information relating to health care sharing ministries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Share Transparency Act of 2025 .\n#### 2. Establishing requirements for the disclosure of certain information relating to health care sharing ministries\n##### (a) In general\nTitle XXVII of the Public Health Service Act ( 42 U.S.C. 300gg et seq. ) is amended by adding at the end the following new part:\nF Health Care Sharing Ministries 2799C\u20131. Disclosure of information (a) In general A health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) of the Internal Revenue Code of 1986)\u2014 (1) shall, not less frequently than annually, submit to the Secretary, the Commissioner of Internal Revenue, and the Director of the Bureau of Consumer Financial Protection the information described in subsection (b); (2) shall disclose to each individual seeking to enroll in the ministry, and each individual so enrolled, the information described in paragraph (1) of subsection (c) in the manner specified in paragraph (2) of such subsection; and (3) may not enter into a contract with an entity for purposes of enrolling an individual in such ministry, or otherwise provide remuneration to such an entity in exchange for enrolling an individual in such ministry, unless such entity meets the requirements described in subsection (d). (b) Disclosure of financial and appeals information (1) In general For purposes of subsection (a)(1), the information described in this subsection is, with respect to a health care sharing ministry, the following: (A) The amount of financial reserves held by such ministry. (B) The ratio of the amount of money collected from enrollees for purposes of reimbursing enrollees for medical claims that is expended by such ministry on costs described in paragraphs (1) and (2) of section 2718(a) to the total amount of money so collected for the preceding year. (C) The number of individuals enrolled in such ministry. (D) The total amount paid by individuals enrolled in such ministry for coverage under such ministry over the preceding year. (E) The total amount paid by such ministry for items and services for which benefits were available under such ministry over the preceding year. (F) The average out-of-pocket expenses incurred by individuals enrolled under such ministry for items and services for which benefits are available under such ministry over the preceding year. (G) A list of each State and county in which individuals who reside in such State or county may enroll in such ministry. (H) The percentage of claims made under such ministry during the preceding year which were denied. (I) Contact information for the operator (or a representative of the operator) of such ministry. (J) A specification of each health care provider with which such ministry has in effect a contractual relationship for furnishing items and services under such ministry. (K) The average amount of time such ministry took to reimburse a claim once submitted to such ministry during the preceding year. (2) Publication The Secretary shall publish the information submitted under subsection (a)(1) on a public website. (c) Disclosure of information to prospective and current enrollees (1) In general For purposes of subsection (a)(2), the information described in this paragraph is, with respect to a health care sharing ministry, the following: (A) How an enrollee may file a complaint or appeal a coverage determination, including a disclaimer that appeals may not be available to any entity other than such ministry. (B) Whether an enrollee must use arbitration in appealing a coverage determination or has other legal recourse. (C) An explanation that, unlike a group health plan or health insurance coverage, there is no guarantee that an enrollee will be reimbursed for any portion of claims submitted to such ministry, as well as a specification of whether any lifetime caps on health care sharing per enrollee are imposed under such ministry. (D) The information described in subsection (b)(1)(F). (E) The average amount paid per enrollee to such ministry for membership under such ministry over the preceding year. (F) With respect to claims made during the preceding year for items and services for which benefits were available under such ministry, the total amount paid by such ministry for such claims compared and the total amount for which individuals enrolled under such ministry were responsible in cost sharing. (G) A list of all items and services for which reimbursement is not available under such ministry, as well as, with respect to each item or service for which such reimbursement is so available, a specification of any conditions that would render such item or service nonreimbursable. (H) A list of any other requirements imposed on claims submitted for health care sharing under such ministry. (2) Manner of disclosure For purposes of subsection (a)(2), information described in paragraph (1) shall be\u2014 (A) disclosed in a prominent manner; (B) made available in multiple langauges; (C) provided immediately before enrollment of any individual in a health care sharing ministry; and (D) be written in at least 14 point font (or, if such enrollment is being made over the phone, be read out loud). (d) Entity requirements For purposes of subsection (a)(3), the requirements described in this subsection are, with respect to an entity with a contract in effect with a health care sharing ministry for purposes of enrolling an individual in such ministry (or otherwise receiving remuneration from such ministry in exchange for enrolling an individual in such ministry), that such entity provides to such individual\u2014 (1) an explanation of any tax credit that may be available to such individual under section 36B of the Internal Revenue Code of 1986 to purchase a qualified health plan (as defined in section 1301(a) of the Patient Protection and Affordable Care Act) through an Exchange established pursuant to such Act; (2) if such individual qualifies to enroll under a State plan (or waiver of such plan) under title XIX of the Social Security Act, or if such individual is entitled to benefits under part A or eligible to enroll under part B of title XVIII of such Act, an explanation of such qualification, entitlement, or eligibility; (3) an explanation of the types of benefits required to be provided under such plans and other protections applicable under such plans (such as limitations on cost sharing) compared to the benefits provided, and cost-sharing requirements imposed, under such ministry; and (4) an explanation that such ministry is not a group health plan or health insurance coverage and that benefits provided under such ministry are not guaranteed. (e) Enforcement In the case that the Secretary determines that a health care sharing ministry has failed to meet a requirement of this section, the Secretary may impose a civil monetary penalty on such ministry in an amount not to exceed $100 for each day for each individual with respect to which such a failure occurs. The provisions of subparagraphs (C) through (G) of paragraph (2) of section 2723 shall apply to a civil monetary penalty imposed under this subsection in the same manner as such provisions apply to a civil monetary penalty imposed under such section. (f) Definitions For purposes of this section, the Secretary may specify the meaning of any term used in relation to a health care sharing ministry and clarify the applicability of such term to such a ministry. .\n##### (b) Disclosures by Federal Trade Commission regarding consumer complaints\n**(1) In general**\nNot later than January 1 and July 1 of each year, the Federal Trade Commission shall publicly disclose on the Internet website of the Commission, and transmit to the Secretary of Health and Human Services and the Commissioner of Internal Revenue\u2014\n**(A)**\nthe number of consumer complaints regarding health care sharing ministries (as defined in section 5000A(d)(2)(B)(ii) of the Internal Revenue Code of 1986) received by the Commission during the period covered by the disclosure;\n**(B)**\nthe general categories (as determined by the Commission) of the complaints described in subparagraph (A); and\n**(C)**\nwith respect to each complaint described in subparagraph (A)\u2014\n**(i)**\nthe name of the health care sharing ministry against which the complaint was made; and\n**(ii)**\nsuch details as the Commission considers appropriate regarding the ownership, operation, and executive leadership of such ministry.\n**(2) Timing of initial disclosure**\nParagraph (1) shall apply beginning on the January 1 or July 1 that first occurs after the date that is 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-30",
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
        "name": "Health",
        "updateDate": "2025-05-21T14:01:25Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3103ih.xml"
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
      "title": "Health Share Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Share Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T06:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to establish requirements for the disclosure of certain information relating to health care sharing ministries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T06:18:41Z"
    }
  ]
}
```
