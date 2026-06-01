# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7274
- Title: Federal Acquisition Security Council Improvement Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7274
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-03-10T08:05:47Z
- Update date including text: 2026-03-10T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 1.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7274",
    "number": "7274",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000480",
        "district": "4",
        "firstName": "William",
        "fullName": "Rep. Timmons, William R. [R-SC-4]",
        "lastName": "Timmons",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Federal Acquisition Security Council Improvement Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:47Z",
    "updateDateIncludingText": "2026-03-10T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
        "item": [
          {
            "date": "2026-02-04T14:57:41Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-30T15:33:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7274ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7274\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Timmons (for himself, Mr. Subramanyam , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 41, United States Code, to make changes with respect to the Federal Acquisition Security Council, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Acquisition Security Council Improvement Act of 2026 .\n#### 2. Changes with respect to the federal acquisition security council\n##### (a) Definition of source of concern, covered source of concern, recommended order, and designated order\nSection 1321 of title 41, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (5) through (8) as paragraphs (7) through (10);\n**(2)**\nby inserting after paragraph (4) the following:\n(5) Covered source of concern The term covered source of concern means a source of concern that is specifically designated as a covered source of concern by a statute that states that such designation is for the purposes of this subchapter. (6) Designated order The term designated order means an order described under section 1323(c)(3). ; and\n**(3)**\nby adding at the end the following:\n(11) Recommended order The term recommended order means an order recommended under section 1323(c)(2). (12) Source of concern (A) In general The term source of concern means a source\u2014 (i) subject to the jurisdiction, direction, or control of the government of a foreign adversary, or operates on behalf of the government of a foreign adversary; or (ii) that poses a risk to the national security of the United States based on collaboration with, whole or partial ownership or control by, or being affiliated with a military, internal security force, or intelligence agency of a foreign adversary. (B) Foreign adversary defined In this paragraph, the term foreign adversary has the meaning given the term covered nation in section 4872(d) of title 10. .\n##### (b) Establishment and members of council\nSection 1322 of title 41, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking executive branch and inserting Executive Office of the President ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) In general The members of the Council shall be as follows: (A) The Administrator for Federal Procurement Policy. (B) The Deputy Director for Management of the Office of Management and Budget. (C) The following officials, each of whom shall occupy a position at the level of Assistant Secretary or Deputy Assistant Secretary (or equivalent): (i) Two officials from the Office of the Director of National Intelligence, one of which shall be from the National Counterintelligence and Security Center. (ii) Two officials from the Department of Defense, one of which shall be one from the National Security Agency. (iii) Two officials from the Department of Homeland Security, one of which shall be one from the Cybersecurity and Infrastructure Security Agency. (iv) An official from the General Services Administration. (v) An official from the Office of the National Cyber Director. (vi) Two officials from the Department of Justice, one of which shall be one from the Federal Bureau of Investigation. (vii) Two officials from the Department of Commerce, one of which shall be from the National Institute of Standards and Technology and one of which shall be from the Bureau of Industry and Security. (viii) An official from any executive agency not listed under clauses (i) through (vii) whose temporary or permanent participation is determined by the Chairperson of the Council to be necessary to carry out the functions of the Council while maintaining the intended balance in subject matter expertise. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking Lead representatives and inserting Members ;\n**(ii)**\nby amending subparagraph (A)(i) to read as follows:\n(i) In general The head of each executive agency listed under paragraph (1)(C) shall designate the official or officials from that agency who shall serve on the Council in accordance with such paragraph. ;\n**(iii)**\nby amending subparagraph (A)(ii) to read as follows:\n(ii) Requirements To the extent feasible, any official designated under clause (i) shall have expertise in supply chain risk management, acquisitions, law, or information and communications technology. ;\n**(iv)**\nby amending subparagraph (B) to read as follows:\n(B) Functions A member of the Council shall\u2014 (i) regularly participate in the activities of the Council; (ii) ensure that any information requested by the Council from the agency represented by the member is provided to the Council; and (iii) ensure that the head of the agency represented by the member and other appropriate personnel of the agency are aware of the activities of the Council. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) In general The President shall a designate a member of the Council to serve as Chairperson of the Council. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking (b)(1)(H) and inserting (b)(1)(C)(viii) ; and\n**(ii)**\nin subparagraph (C), by striking lead representative of each agency represented on the Council and inserting members of the Council ; and\n**(4)**\nin subsection (d)\u2014\n**(A)**\nby striking The Council and inserting the following:\n(1) Council meetings The Council ; and\n**(B)**\nby adding at the end the following:\n(2) Other meetings The Chairperson of the Council shall meet, not less frequently than semiannually, with\u2014 (A) the Secretary of Homeland Security, Secretary of Defense, and Director of National Intelligence; or (B) in the case that any of the officials under subparagraph (A) delegated authority to an official under section 1323(c)(6)(C), with the delegated official. .\n##### (c) Functions and authorities\nSection 1323 of title 41, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking supply chain each place it appears and inserting acquisition security and supply chain ;\n**(B)**\nin paragraph (1), as amended by subparagraph (A), by striking , particularly and inserting that arise ;\n**(C)**\nin paragraph (2), as amended by subparagraph (A), by inserting associated with the acquisition and use of covered articles after risk ;\n**(D)**\nin paragraph (6), as amended by subparagraph (A)\u2014\n**(i)**\nby striking posed by and inserting associated with ; and\n**(ii)**\nby inserting and use before of covered articles ;\n**(E)**\nin paragraph (7), by striking posed by acquisitions and inserting associated with the acquisition ;\n**(F)**\nby redesignating paragraph (7) as paragraph (12); and\n**(G)**\nby inserting after paragraph (6) the following:\n(7) Implementing a prioritization scheme for evaluating the security risks associated with the acquisition and use of covered articles provided or produced by a covered source of concern. (8) Evaluating each covered source of concern to determine whether to issue a designated order with respect to the covered source of concern or a covered article produced or provided by the covered source of concern. (9) Evaluating sources of concern to determine whether to issue a recommended order with respect to the source of concern, or any covered article produced or provided by the source of concern. (10) Monitoring and evaluating compliance by the Secretary of Homeland Security, Secretary of Defense, and Director of National Intelligence with the requirement to issue designated orders under subsection (c)(6)(B). (11) Reporting to Congress annually on the security risks associated with the acquisition and use of covered articles produced or provided by sources of concern. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking The Council and inserting the following:\n(1) In general The Council ;\n**(B)**\nin paragraph (1), as so redesignated, by striking a program office and ; and\n**(C)**\nby adding at the end the following:\n(2) Federal acquisition security council program office (A) Establishment The President shall establish a Federal Acquisition Security Council Program Office (referred to in this paragraph as the Program Office ) within the Executive Office of the President to carry out the duties described under subparagraph (B). (B) Duties The Program Office shall provide to the Council, including any committees, working groups, or other constituent bodies established by the Council under paragraph (1)\u2014 (i) administrative, legal, and policy support; and (ii) analysis and subject matter expertise on information communications technology, acquisition security, and supply chain risk. (C) Structure The head of the Program Office shall be designated by the Chairperson of the Council. (D) Prohibition The Program Office may not provide administrative support to the Council for any activities of the Council carried out pursuant to a provision of law other than a provision of law under this subchapter. (E) Funding and resources The Program Office may use the staff and resources of the Executive Office of the President or maintain dedicated staff and resources, as appropriate, in the performance of the duties of the Office. (F) Shared staffing authority (i) In general The Program Office may accept officers or employees of the United States or members of the Armed Forces on a detail from an element of the intelligence community (as such term is defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )) or from another element of the Federal Government on a nonreimbursable basis, as jointly agreed to by the heads of the receiving and detailing elements, for a period not to exceed three years. (ii) Rule of construction Nothing in this subparagraph may be construed as imposing any limitation on any other authority for reimbursable or nonreimbursable details. (iii) Nonreimbursable detail A nonreimbursable detail made under this subparagraph shall not be considered an augmentation of the appropriations of the receiving element of the Program Office. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking supply chain risk and inserting acquisition security and supply chain risk associated with the acquisition of covered articles ;\n**(ii)**\nin subparagraph (A), by inserting recommended before exclusion orders ;\n**(iii)**\nin subparagraph (B), by inserting recommended before removal orders ;\n**(iv)**\nin subparagraph (C), by striking ; and and inserting a semicolon;\n**(v)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(vi)**\nby adding at the end the following:\n(E) issuing designated orders. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking Recommendations and inserting Recommended Orders ;\n**(ii)**\nby striking use and inserting , using ;\n**(iii)**\nby striking subsection (a)(3) and inserting subsection (a)(4) ;\n**(iv)**\nby striking to issue recommendations and inserting , recommend orders ;\n**(v)**\nby striking Such recommendations and inserting Any such order recommended ;\n**(vi)**\nby inserting to the officials described under clause (iii) of paragraph (6)(A) for issuance under such paragraph after thereof, ;\n**(vii)**\nin subparagraph (D), by striking supply chain risk and inserting acquisition security and supply chain risk associated with the acquisition of covered articles ; and\n**(viii)**\nin subparagraph (E), by striking exclusion or removal ;\n**(C)**\nby redesignating paragraphs (3) through (7) as paragraphs (4) through (8);\n**(D)**\nby inserting after paragraph (2) the following:\n(3) Designated orders (A) Exclusion or removal of covered sources of concern (i) In general Not later than 270 days after a source of concern is designated as a covered source of concern, the Council\u2014 (I) shall provide to the officials described under clause (iii) of paragraph (6)(B) for issuance under such paragraph orders requiring\u2014 (aa) the exclusion of the covered source of concern from any executive agency procurement action, including source selection and consent for a contractor; or (bb) the removal of covered articles produced or provided by the covered source of concern from the information system of executive agencies; or (II) report to Congress why the Council has determined to not issue an order described under subclause (I) with respect to the covered source of concern or covered articles produced or provided by the covered source of concern. (ii) Contents of order Any order provided under clause (i) shall include\u2014 (I) information regarding the scope and applicability of the order, including any information necessary to positively identify the covered source of concern or covered articles produced or provided by the covered source of concern required to be excluded or removed under the order; (II) a summary of any risk assessment reviewed or conducted in support of the order; (III) a summary of the basis for the order, including a discussion of less intrusive measures that were considered and why such measures were not reasonably available to reduce security risk; (IV) a description of the actions necessary to implement the order; and (V) where practicable, in the Council\u2019s sole and unreviewable discretion, a description of mitigation steps that could be taken by the covered source of concern that may result in the Council rescinding the order. (B) Exclusion or removal of second order sources or covered articles (i) Issuance In the case that the Council provides an order under subparagraph (A), the Council may also provide an order to the officials described under paragraph (6)(A)(iii) requiring the exclusion of sources or covered articles from executive agency procurement actions or removal of covered articles from executive agency information systems if\u2014 (I) such covered articles or such sources use a covered source of concern in the performance of a contract with the executive agency; or (II) such sources enter into a contract, the performance of which such source knows or has reason to believe will require, in the performance of a contract with the executive agency, the use of a covered source of concern or the use of a covered article produced or provided by a covered source of concern. (ii) Effective date considerations Any effective date prescribed by the Council for an order issued pursuant to clause (i) shall take into account\u2014 (I) the risk posed by the covered source of concern or the covered article produced or provided by the covered source of concern to the national security of the United States; (II) the likelihood of the covered source of concern or the covered article produced or provided by the covered source of concern causing imminent threat to public health and safety; (III) the availability of an alternative source or covered article produced or provided by an alternative source; and (IV) an assessment of the potential direct or quantifiable costs that may be incurred by the Federal Government, a State, local, or Tribal government, or by the private sector, as a result of compliance by the head of an executive agency with such an exclusion or removal order. ;\n**(E)**\nin paragraph (4), as so redesignated\u2014\n**(i)**\nin the heading, by striking of recommendation and review and inserting and review of recommended and designated orders ;\n**(ii)**\nby striking the recommendation each place the term appears, and inserting the order ;\n**(iii)**\nin the matter preceding subparagraph (A), by striking A notice of the Council\u2019s recommendation under paragraph (2) and inserting Before the Council recommends an order under paragraph (2) or issues an order under paragraph (3), a notice ;\n**(iv)**\nin subparagraph (A), by striking a recommendation has been made and inserting the order will be recommended or issued ;\n**(v)**\nin subparagraph (D), by striking paragraph (5) and inserting paragraph (6) ; and\n**(vi)**\nby inserting a new subparagraph to read as follows:\n(F) Until an order is issued pursuant to paragraph (6), information collected under this paragraph shall be exempt from public disclosure and shall be exempt from disclosure under section 552(b)(3)(B) of title 5, United States Code (commonly referred to as the Freedom of Information Act ). ;\n**(F)**\nin paragraph (5), as so redesignated\u2014\n**(i)**\nby striking paragraph (3) and inserting paragraph (4) ;\n**(ii)**\nin subparagraph (A), by striking paragraph (5) and inserting paragraph (6) ; and\n**(iii)**\nin subparagraph (B), by striking paragraph (6) and inserting paragraph (7) ;\n**(G)**\nin paragraph (6), as so redesignated\u2014\n**(i)**\nby amending subparagraph (A) to read as follows:\n(A) Issuance of recommended orders (i) Modifications to order After considering any response properly submitted by a source under paragraph (4) related to an order to be recommended under paragraph (2), the Council shall\u2014 (I) make such modifications to the order as the Council considers appropriate; and (II) provide the order (together with any information submitted by a source under paragraph (4) related to such order) to the officials described under clause (iii). (ii) Order Not later than 90 days after receiving a recommended order, the officials described under clause (iii) shall\u2014 (I) issue the order to the heads of the applicable agencies; or (II) submit a notification to the Council that the order will not be issued, that includes in the notification to the Council, all the reasons for why the order will not be issued. (iii) Officials The officials described in this clause are as follows: (I) The Secretary of Homeland Security, for exclusion and removal orders applicable to civilian agencies, to the extent not covered by subclause (II) or (III). (II) The Secretary of Defense, for exclusion and removal orders applicable to the Department of Defense and national security systems other than sensitive compartmented information systems. (III) The Director of National Intelligence, for exclusion and removal orders applicable to the intelligence community and sensitive compartmented information systems, to the extent not covered by subclause (II). ;\n**(ii)**\nby redesignating subparagraphs (B) through (E) as subparagraphs (C) through (F), respectively;\n**(iii)**\nby inserting after subparagraph (A) the following;\n(B) Issuance of designated order (i) Modifications After considering any response properly submitted by a source under paragraph (4) related to a designated order, the Council shall\u2014 (I) (aa) make any such modifications to the order as the Council considers appropriate; or (bb) if the Council determines that the issuance of a designated order is not warranted, rescind the designated order and notify the source of the rescission; and (II) except in the case that the Council rescinds the designated order under subclause (I)(bb), provide the designated order (including any modifications made to such order by the Council) to the officials described in clause (iii). (ii) Issuance The officials described in clause (iii) shall, not later than 90 days after receiving a designated order, issue the order to the heads of the applicable agencies. (iii) Officials The officials described in this clause are as follows: (I) The Secretary of Homeland Security, for exclusion and removal orders applicable to civilian agencies, to the extent not covered by subclause (II) or (III). (II) The Secretary of Defense, for exclusion and removal orders applicable to the Department of Defense and national security systems other than sensitive compartmented information systems. (III) The Director of National Intelligence, for exclusion and removal orders applicable to the intelligence community and sensitive compartmented information systems, to the extent not covered by subclause (II). (iv) Waiver An official described under clause (iii) may waive for a period of not more than 365 days the application of an order issued by such official under clause (ii) with respect to a covered source of concern or a covered article produced or provided by a covered source of concern if the official submits, not later than 30 days after making such waiver, a written notification to the Council, appropriate congressional committees, and leadership that contains the justification for such waiver. (v) Renewal of waiver An official described under clause (iii) may renew a waiver under clause (iv) for an additional period of not more than 180 days if\u2014 (I) the renewal of the waiver is in the national security interests of the United States; and (II) the official submits, not later than 30 days after renewing such waiver, a written notification to the Council, appropriate congressional committees, and leadership that includes the justification for renewing the wavier. (vi) National security waiver An official described under clause (iii) may waive the application of an order issued by such official under clause (ii) with respect to a covered source of concern or a covered article produced or provided by a covered source of concern for any activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States. (vii) Rescission of order An exclusion or removal order issued under this subparagraph by an official may be rescinded only by the Council. ;\n**(iv)**\nin subparagraph (C), as so redesignated\u2014\n**(I)**\nby striking subparagraph (A) and inserting subparagraph (A)(iii) or (B)(iii) ;\n**(II)**\nby striking this subparagraph and inserting subparagraph (A)(iii) or (B)(iii) ; and\n**(III)**\nby striking , except and all that follows before the period at the end;\n**(v)**\nin subparagraph (D), as so redesignated\u2014\n**(I)**\nby striking this paragraph and inserting subparagraph (A)(iii) or (B)(iii) ; and\n**(II)**\nby striking help ;\n**(vi)**\nin subparagraph (E), as so redesignated, by striking this paragraph and inserting subparagraph (A) ; and\n**(vii)**\nby adding after subparagraph (F), as so redesignated, the following:\n(G) Effective date of orders The effective date of an order issued under this paragraph may not be more than 365 days after the order is issued. ;\n**(H)**\nin paragraph (7), as so redesignated, by striking paragraph (5)(A) and inserting subparagraph (A) or (B) of paragraph (6) ; and\n**(I)**\nin paragraph (8), as so redesignated, by striking paragraph (5) and inserting paragraph (6) ;\n**(4)**\nin subsection (e), by inserting the Chief Data Officers Council, before the Chief Acquisition ; and\n**(5)**\nin subsection (f)(2), by striking the period at the end and inserting unless such source is specifically designated by statute as a covered source of concern for the purposes of this subchapter. .\n##### (d) Strategic plan\nSection 1324(a) of title 41, United States Code, is amended\u2014\n**(1)**\nby inserting , and periodically thereafter after 2018 ;\n**(2)**\nin the matter preceding paragraph (1), by inserting acquisition security and before supply chain risks ;\n**(3)**\nin paragraph (8), by inserting acquisition security and before supply chain risks ; and\n**(4)**\nin paragraph (9)(A), by inserting acquisition security and before supply chain risk .\n##### (e) Requirements for executive agencies\nSection 1326 of title 41, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) providing any information requested by the Chairperson of the Council for the purpose of carrying out activities of this subchapter, subject to applicable law or policy on the control and handling of classified, sensitive, or proprietary information. ;\n**(2)**\nby striking supply chain each place such term appears and inserting security and supply chain ; and\n**(3)**\nin subsection (b)(6), by striking supply chain and inserting security or supply chain .\n##### (f) Judicial procedure\nSection 1327(b) of title 41, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking section 1323(c)(6) and inserting section 1323(c)(7) ;\n**(2)**\nin paragraph (3), by striking section 1323(c)(5) and inserting sections 1323(c)(6) ; and\n**(3)**\nin paragraph (4), by amending subparagraph (B)(i) to read as follows:\n(i) Filing of record The United States shall file with the court an administrative record, which shall consist of\u2014 (I) the information the Council relied upon in issuing a designated order under 1323(c)(6); and (II) the information that the appropriate official relied upon in issuing an exclusion or removal order under section 1323(c)(6) or a covered procurement action under section 4713. .\n##### (g) Additional provisions\nSubchapter III of chapter 13 of title 41, United States Code, is amended by adding at the end the following:\n1329. Additional provisions (a) Compliance with existing prohibitions In implementing this subchapter, the Council shall coordinate, as applicable and practicable, with the head of an agency to assist with compliance by the agency with\u2014 (1) section 889 of the John S. McCain National Defense Authorization Act of 2019 ( Public Law 115\u2013232 ; 41 U.S.C. 3901 note); (2) section 5949 of the James M. Inhofe National Defense Authorization Act of 2023 ( Public Law 117\u2013263 ; 41 U.S.C. 4713 note); and (3) sections 1821 through 1833 of the American Security Drone Act of 2023 ( Public Law 118\u201331 ). (b) Update to regulations The Federal Acquisition Security Council shall update, within two years after the date of the enactment of this section, any regulations of the Council as necessary. .\n##### (h) Reallocating existing resources\nSection 5949(l)(1) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ) is amended by inserting before the period at the end the following: and the Federal Acquisition Security Council Program Office established under section 1323(b)(2) of title 41, United States Code .\n##### (i) Technical and conforming changes\nSubchapter III of chapter 13 of title 41, United States Code, is amended\u2014\n**(1)**\nin the table of sections for the subchapter by adding after the item related to section 1328 the following:\n1329. Additional provisions. ;\nand\n**(2)**\nby striking of this title each place the term appears.",
      "versionDate": "2026-01-30",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-24T01:56:13Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7274ih.xml"
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
      "title": "Federal Acquisition Security Council Improvement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Acquisition Security Council Improvement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 41, United States Code, to make changes with respect to the Federal Acquisition Security Council, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:38Z"
    }
  ]
}
```
