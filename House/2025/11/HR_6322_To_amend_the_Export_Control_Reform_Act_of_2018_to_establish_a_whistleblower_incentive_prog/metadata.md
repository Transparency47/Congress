# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6322
- Title: Stop Stealing our Chips Act
- Congress: 119
- Bill type: HR
- Bill number: 6322
- Origin chamber: House
- Introduced date: 2025-11-28
- Update date: 2026-04-28T08:05:50Z
- Update date including text: 2026-04-28T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-28: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.
- Latest action: 2025-11-28: Introduced in House

## Actions

- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-28",
    "latestAction": {
      "actionDate": "2025-11-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6322",
    "number": "6322",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Stop Stealing our Chips Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:50Z",
    "updateDateIncludingText": "2026-04-28T08:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-11-28",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-28",
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
            "date": "2026-04-22T20:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-28T15:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "TX"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "MI"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "MI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NJ"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AR"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6322ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6322\nIN THE HOUSE OF REPRESENTATIVES\nNovember 28, 2025 Mr. Kean (for himself and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to establish a whistleblower incentive program and provide protections to whistleblowers.\n#### 1. Short title\nThis Act may be cited as the Stop Stealing our Chips Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nViolations of the export control laws of the United States, especially the diversion of leading-edge artificial intelligence chips into countries that are adversaries of the United States, threaten the national security of the United States.\n**(2)**\nIndividuals who accurately report violations of United States export control laws play a significant role in helping authorities identify and mitigate such threats.\n**(3)**\nAn incentive program that rewards whistleblowers can significantly enhance enforcement efforts by encouraging individuals to provide high-value information on potential violations across all sectors.\n**(4)**\nSuch a program may also encourage stronger self-policing and internal compliance by firms, preventing violations before they occur.\n#### 3. Establishment of whistleblower incentive program and whistleblower protections\n##### (a) In general\nThe Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ) is amended by inserting after section 1761 the following:\n1761A. Whistleblower incentives and protections (a) Definitions In this section: (1) Original information The term original information means information that is\u2014 (A) derived from the independent knowledge or analysis of a whistleblower; (B) not known to the Secretary from any other source unless the whistleblower is the original source of the information; (C) not exclusively derived from an allegation made in a judicial or administrative hearing, a governmental report, hearing, audit, or investigation, or from news media, unless the whistleblower is the source of such allegation; and (D) provided to the Secretary voluntarily, without any request from the Secretary or any other government official. (2) Whistleblower (A) In general The term whistleblower means, except as provided by subparagraph (B), any individual (including an individual who is not a United States citizen) who provides, or 2 or more such individuals acting jointly who provide, to the Secretary information relating to a possible violation of this part or of any regulation, order, license, or other authorization issued under this part. (B) Exclusions The term whistleblower does not include\u2014 (i) a Federal employee acting within the scope of the duties of the employee; or (ii) an individual on any of the following lists: (I) The list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury; (II) The Denied Persons List maintained pursuant to section 764.3(a)(2) of the Export Administration Regulations; or (III) The Entity List under Supplement No. 4 to part 744 of the Export Administration Regulations. (3) Related action The term related action , when used with respect to any judicial or administrative action brought by the Department under the Export Administration Regulations, means any judicial or administrative action brought by a United States government entity that is based upon the original information provided by a whistleblower pursuant to this section that led to a successful export control enforcement action. (b) Whistleblower incentive program (1) Establishment Not later than 120 days after the date of the enactment of this section, the Secretary shall establish a whistleblower incentive program to reward individuals who provide original information that leads to\u2014 (A) the imposition of fines under this part on persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part; or (B) the forfeiture of any property under section 1761(j) if such forfeiture results in net proceeds to the Export Compliance Accountability Fund. (2) Whistleblower reports (A) Online portal Not later than 120 days after the date of the enactment of this section, the Secretary shall establish and maintain a secure portal, or update and maintain an existing secure portal, on a website accessible to the public, for the reporting of original information relating to\u2014 (i) persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part; and (ii) items that have been, are being, or are about to be exported, reexported, or in-country transferred in violation of this part or any regulation, order, license, or other authorization issued under this part. (B) Anonymity (i) In general As an alternative to submission through the portal required by subparagraph (A), an individual may submit a report of original information under this subsection anonymously, including through an attorney. (ii) Exception The Secretary may require that the identity of an individual be disclosed for the individual to receive an award under paragraph (3). (C) Expedited review (i) Initial review Not later than 60 days after the date of receipt of a report from a whistleblower, the Secretary shall\u2014 (I) determine whether the report is credible; and (II) if credible, initiate a formal investigation of the allegations contained in the report. (ii) Investigation The Secretary shall pursue any formal investigation under clause (i)(II) with urgency and conclude the investigation within a reasonable amount of time. (iii) Notification (I) In general Subject to the confidentiality requirements of section 1761(h), the Secretary shall update the whistleblower on the status of a report and, if applicable, the related investigation not later than 60 days after the date on which the whistleblower submitted the report and not less frequently than every 180 days thereafter. (II) Sensitive information The Secretary may omit from the updates required by subclause (I) any information that could compromise an ongoing investigation. (D) Avoidance of frivolous reports The Secretary may prohibit an individual from making reports under this subsection if the individual has previously submitted multiple reports under this subsection that the Secretary determined under subparagraph (C)(i) were not credible. (3) Awards (A) Eligibility Subject to subparagraph (B), the Secretary shall pay an award or awards to any whistleblower who provided original information that led to the imposition of a fine greater than $1,000,000 under this part on a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part or a related action, including when the underlying violation occurred before the date of the enactment of this section, so long as the whistleblower\u2019s report is submitted after such date of enactment. (B) Disqualification (i) In general Subject to clause (ii), the Secretary may not pay an award or awards to any whistleblower who provides original information with respect to a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part, if such information was obtained through\u2014 (I) the role of the whistleblower as\u2014 (aa) an officer, director, trustee, or partner of an entity that handles internal processes for legal violations for the person or persons; (bb) an employee of an entity that conducts compliance or internal audits for the person or persons; or (cc) an employee of a public accounting firm if the information was obtained while working on an engagement required by Federal law; or (II) any means that violates Federal or State criminal law. (ii) Exceptions Clause (i) shall not apply if\u2014 (I) the whistleblower had a reasonable basis to believe that disclosing the original information to the Secretary was necessary to stop conduct likely to cause significant financial harm; (II) the whistleblower had a reasonable basis to believe that the relevant entity was obstructing an investigation into the misconduct; or (III) not less than 120 days have elapsed since the whistleblower provided the information to the audit committee, chief legal officer, chief compliance officer (or their equivalent) of the relevant entity or the supervisor of the whistleblower. (C) Amount (i) In general The sum total of the awards issued for a particular action under subparagraph (A) shall be\u2014 (I) not less than 10 percent, in total, of the amount collected of the fine imposed under this part; and (II) not more than 30 percent, in total, of the amount collected of that fine. (ii) Jointly submitted report In the case of a report that was submitted jointly by 2 or more individuals, or separate reports related to the same action, any award issued under subparagraph (A) shall be split among the individuals at the Secretary\u2019s discretion. (D) Determination The Secretary shall determine the amount of an award made under subparagraph (A) taking into account, with respect to the information provided\u2014 (i) accuracy; (ii) relevance; (iii) timeliness; and (iv) usefulness. (E) Awards for related actions shall be paid at the discretion of the Secretary. (4) Publication (A) In general Not later than the date on which the online portal required by paragraph (2)(A) is complete, the Secretary shall develop and implement a plan to publicize the whistleblower incentive program established by paragraph (1). (B) Funding The Secretary shall pay any expenses incurred under subparagraph (A) from amounts authorized to be appropriated to the Bureau of Industry and Security. (c) Protection of whistleblowers (1) Prohibition against impending communication and retaliation (A) In general Except as provided in subparagraph (B), no employer may\u2014 (i) impede or attempt to impede an individual from communicating directly with the Department of Commerce regarding a possible violation of export control or related laws; or (ii) discharge, demote, suspend, threaten, harass, directly or indirectly, or in any other manner discriminate against a whistleblower in the terms and conditions of employment because of a lawful act done by the whistleblower\u2014 (I) in reporting violations to the employer or to a law enforcement agency; (II) in providing information to the Secretary in accordance with this section; or (III) in initiating, testifying in, or assisting in any investigation or judicial or administrative action based upon or related to such information. (B) Exception The protection against retaliation established by subparagraph (A) shall not apply to any individual who reports information under this section knowing that such information is false. (C) Enforcement (i) Cause of action An individual who alleges discharge or other discrimination in violation of subparagraph (A) may bring an action under this paragraph in the appropriate district court of the United States for the relief provided in subparagraph (D). (ii) Subpoenas A subpoena requiring the attendance of a witness at a trial or hearing conducted under this subparagraph may be served at any place in the United States. (iii) Statute of limitations (I) In general An action under this subparagraph shall not be entertained if commenced more than\u2014 (aa) 6 years after the date of the violation of subparagraph (A) occurred; or (bb) 3 years after the date when facts material to the right of action are known or reasonably should have been known by the employee alleging a violation of subparagraph (A). (II) Required action within 10 years Notwithstanding subclause (I), an action under this subparagraph may not in any circumstance be brought more than 10 years after the date on which the violation occurs. (D) Relief Relief for an individual prevailing in an action brought under subparagraph (C) shall include\u2014 (i) reinstatement with the same seniority status that the individual would have had, but for the discrimination; (ii) 2 times the amount of back pay otherwise owed to the individual, with interest; and (iii) compensation for litigation costs, expert witness fees, and reasonable attorneys\u2019 fees. (E) Scope of protection The protections under this subsection shall apply to any individual who engages in an act described in subparagraph (A), including reporting a potential violation internally to an employer or to a law enforcement agency, regardless of whether the individual has, at the time of the alleged retaliation, provided information to the Secretary under this section. Such protections shall also apply if the retaliation occurs before, or in the absence of, a formal report to the Department of Commerce. (2) Confidentiality (A) In general Except as provided in subparagraphs (B) and (C), the Secretary and any officer or employee of the Department of Commerce shall not disclose any information, including information provided by a whistleblower to the Secretary, that could reasonably be expected to reveal the identity of the whistleblower, except in accordance with the provisions of section 552a of title 5, United States Code, unless and until required to be disclosed to a defendant or respondent in connection with a public proceeding instituted by the Secretary or any entity described in subparagraph (D). (B) Exempted statute For purposes of section 552 of title 5, United States Code, this paragraph shall be considered a statute described in subsection (b)(3)(B) of such section. (C) Rule of construction Nothing in this section is intended to limit, or shall be construed to limit, the ability of the Attorney General to present such evidence to a grand jury or to share such evidence with potential witnesses or defendants in the course of an ongoing criminal investigation. (D) Availability to government agencies (i) In general Without the loss of its status as confidential in the hands of the Secretary, all information referred to in subparagraph (A) may, in the discretion of the Secretary, when determined by the Secretary to be necessary to accomplish the purposes of this part or any regulation, order, license, or other authorization issued under this part, be made available to\u2014 (I) a Federal law enforcement agency; (II) a national security agency; (III) an appropriate Federal or State regulatory authority or Federal investigative agency; and (IV) a foreign law enforcement authority. (ii) Confidentiality (I) In general Each of the entities described in subclauses (I) through (III) of clause (i) shall maintain such information as confidential in accordance with the requirements established under subparagraph (A). (II) Foreign authorities Each of the entities described in clause (i)(IV) shall maintain such information in accordance with such assurances of confidentiality as the Secretary determines appropriate. (d) Export compliance accountability fund (1) Establishment Not later than 90 days after the date of the enactment of this section, there shall be established in the Treasury of the United States a fund to be known as the Export Compliance Accountability Fund (in this subsection referred to as the Fund ). (2) Availability At the end of each fiscal year, any amounts deposited into the Fund under paragraph (3) that remain in the Fund after the payment, for that fiscal year, of all expenses under paragraph (3) shall be transferred to the general fund of the Treasury. The Fund shall retain an amount equivalent to $100,000,000 (adjusted for inflation) or the total amount necessary to satisfy any pending whistleblower award determinations, whichever is greater. (3) Use of fund The Fund shall be available to the Secretary, without further appropriation or fiscal year limitation, for\u2014 (A) paying awards to whistleblowers as provided in subsection (b)(3); (B) funding activities that support the whistleblower incentive program and whistleblower protections, including\u2014 (i) reviewing and investigating whistleblower reports; (ii) providing training and education on compliance with the confidentiality requirement under subsection (c)(2); and (iii) record keeping, IT expenses, and other expenses to maintain or update the portal as considered necessary by the Secretary; and (C) if all outstanding awards under subsection (b)(3) have been paid, expenses related to enforcement of this part or any regulation, order, license, or other authorization issued under this part. (4) Deposits and credits There shall be deposited into or credited to the Fund an amount equal to any fine collected by the Secretary on or after the date of the enactment of this section in any judicial or administrative action brought by the Secretary that depends on or was initiated because of original information submitted by a whistleblower. .\n#### 4. Rule of construction\nNothing in this Act, or any amendment made by this Act, may be construed to affect, reduce, or divert any amounts required by law to be deposited into the Crime Victims Fund ( 34 U.S.C. 20101 ) or the U.S. Victims of State Sponsored Terrorism Fund ( 34 U.S.C. 20144 ).",
      "versionDate": "2025-11-28",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1473",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Stealing our Chips Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-12-17T16:22:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-28",
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
          "measure-id": "id119hr6322",
          "measure-number": "6322",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-28",
          "originChamber": "HOUSE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6322v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2025-11-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS (1) imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization; or (2) requiring the forfeiture of property that\u00a0results in net proceeds.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill requires\u00a0BIS to pay an award to certain whistleblowers\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting\u00a0employers from impeding communication or retaliating against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>"
        },
        "title": "Stop Stealing our Chips Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6322.xml",
    "summary": {
      "actionDate": "2025-11-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS (1) imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization; or (2) requiring the forfeiture of property that\u00a0results in net proceeds.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill requires\u00a0BIS to pay an award to certain whistleblowers\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting\u00a0employers from impeding communication or retaliating against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119hr6322"
    },
    "title": "Stop Stealing our Chips Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS (1) imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization; or (2) requiring the forfeiture of property that\u00a0results in net proceeds.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill requires\u00a0BIS to pay an award to certain whistleblowers\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting\u00a0employers from impeding communication or retaliating against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119hr6322"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6322ih.xml"
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
      "title": "Stop Stealing our Chips Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Stealing our Chips Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 to establish a whistleblower incentive program and provide protections to whistleblowers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T12:18:15Z"
    }
  ]
}
```
