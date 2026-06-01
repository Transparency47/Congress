# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1473
- Title: Stop Stealing our Chips Act
- Congress: 119
- Bill type: S
- Bill number: 1473
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-05-27T11:22:16Z
- Update date including text: 2026-05-27T11:22:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-05-20 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S2424-2426)
- 2026-05-20 - Floor: Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S2424-2426)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-05-21 - Floor: Message on Senate action sent to the House.
- 2026-05-21 15:18:41 - Floor: Received in the House.
- 2026-05-21 15:30:23 - Floor: Held at the desk.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-05-20 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S2424-2426)
- 2026-05-20 - Floor: Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S2424-2426)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-05-21 - Floor: Message on Senate action sent to the House.
- 2026-05-21 15:18:41 - Floor: Received in the House.
- 2026-05-21 15:30:23 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1473",
    "number": "1473",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Stop Stealing our Chips Act",
    "type": "S",
    "updateDate": "2026-05-27T11:22:16Z",
    "updateDateIncludingText": "2026-05-27T11:22:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-21",
      "actionTime": "15:30:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-21",
      "actionTime": "15:18:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text of amendment in the nature of a substitute: CR S2424-2426)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S2424-2426)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5445 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5445 proposed by Senator Barrasso for Senator Rounds. (consideration: CR S2424)",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 5445 proposed by Senator Barrasso for Senator Rounds.",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 5445 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-05-20",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "1473",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "Stop Stealing our Chips Act",
          "type": "S",
          "updateDateIncludingText": "2026-05-27"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-05-20",
          "links": {
            "link": {
              "name": "SA 5445",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/5445"
            }
          },
          "text": "Amendment SA 5445 agreed to in Senate by Unanimous Consent."
        },
        "number": "5445",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "B001261",
              "firstName": "John",
              "fullName": "Sen. Barrasso, John [R-WY]",
              "lastName": "Barrasso",
              "party": "R",
              "state": "WY",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "B001261",
              "firstName": "John",
              "fullName": "Sen. Barrasso, John [R-WY]",
              "lastName": "Barrasso",
              "party": "R",
              "state": "WY",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2026-05-20T04:00:00Z",
        "purpose": "In the nature of a substitute.",
        "sponsors": {
          "item": {
            "bioguideId": "R000605",
            "firstName": "Mike",
            "fullName": "Sen. Rounds, Mike [R-SD]",
            "lastName": "Rounds",
            "party": "R",
            "state": "SD"
          }
        },
        "submittedDate": "2026-05-20T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-05-23T11:08:28Z"
      }
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
            "date": "2026-05-20T22:00:12Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-04-10T20:16:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1473is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1473\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Rounds (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to establish a whistleblower incentive program and provide protections to whistleblowers.\n#### 1. Short title\nThis Act may be cited as the Stop Stealing our Chips Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nViolations of the export control laws of the United States, especially the diversion of leading-edge artificial intelligence chips into countries that are adversaries of the United States, threaten the national security of the United States.\n**(2)**\nIndividuals who accurately report violations of United States export control laws play a significant role in helping authorities identify and mitigate such threats.\n**(3)**\nAn incentive program that rewards whistleblowers can significantly enhance enforcement efforts by encouraging individuals to provide high-value information on potential violations.\n#### 3. Establishment of Whistleblower Incentive Program and Whistleblower Protections\n##### (a) In general\nThe Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ) is amended by inserting after section 1761 the following:\n1761A. Whistleblower Incentives and Protections (a) Definitions In this section: (1) Original information The term original information means information that is\u2014 (A) derived from the independent knowledge or analysis of a whistleblower; (B) not known to the Secretary from any other source; (C) not exclusively derived from an allegation made in a judicial or administrative hearing, a governmental report, hearing, audit, or investigation, or from news media, unless the whistleblower is the source of such allegation; and (D) provided to the Secretary voluntarily, without any request from the Secretary or any other government official. (2) Whistleblower (A) In general The term whistleblower means, except as provided by subparagraph (B), any individual (including an individual who is not a United States citizen) who provides, or 2 or more such individuals acting jointly who provide, to the Secretary information relating to a possible violation of this part or of any regulation, order, license, or other authorization issued under this part. (B) Exclusions The term whistleblower does not include\u2014 (i) a Federal employee acting within the scope of the duties of the employee; or (ii) an individual on the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury. (b) Whistleblower Incentive Program (1) Establishment Not later than 120 days after the date of the enactment of this section, the Secretary shall establish a whistleblower incentive program to reward individuals who provide original information that leads to the imposition of fines under this part on persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part. (2) Whistleblower reports (A) Online portal Not later than 120 days after the date of the enactment of this section, the Secretary shall develop, implement, and maintain a secure portal, on a website accessible to the public, for the reporting of original information relating to persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part. (B) Anonymity (i) In general As an alternative to submission through the portal required by subparagraph (A), an individual may submit a report of original information under this subsection anonymously, including through an attorney. (ii) Exception The Secretary may require that the identity of an individual be disclosed for the individual to receive an award under paragraph (3). (C) Expedited review (i) Initial review Not later than 60 days after the date of receipt of a report from a whistleblower, the Secretary shall\u2014 (I) determine whether the report is credible; and (II) if credible, initiate a formal investigation of the allegations contained in the report. (ii) Investigation Unless the Secretary determines that the investigation is particularly complex, the Secretary shall conclude the investigation not later than 180 days after the date on which a formal investigation has been initiated under clause (i). (iii) Notification (I) In general The Secretary shall update the whistleblower on the status of a report and, if applicable, the related investigation not later than 30 days after the date on which the whistleblower submitted the report and not less frequently than every 30 days thereafter. (II) Sensitive information The Secretary may omit from the updates required by subclause (I) any information that could compromise an ongoing investigation. (D) Avoidance of frivolous reports The Secretary may prohibit an individual from making reports under this subsection if the individual has previously submitted multiple reports under this subsection that the Secretary determined under subparagraph (C)(i) were not credible. (3) Awards (A) Eligibility Subject to subparagraph (B), the Secretary may pay an award or awards to any whistleblower who provided original information that led to the imposition of a fine under this part on a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part. (B) Disqualification (i) In general Subject to clause (ii), the Secretary may not pay an award or awards to any whistleblower who provides original information with respect to a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part, if such information was obtained through\u2014 (I) the role of the whistleblower as\u2014 (aa) an officer, director, trustee, or partner of an entity that handles internal processes for legal violations for the person or persons; (bb) an employee of an entity that conducts compliance or internal audits for the person or persons; (cc) an employee of a public accounting firm if the information was obtained while working on an engagement required by Federal securities laws, other than specific audits; or (II) any means that violates Federal or State criminal law. (ii) Exceptions Clause (i) shall not apply if\u2014 (I) the whistleblower had a reasonable basis to believe that disclosing the original information to the Secretary was necessary to stop conduct likely to cause significant financial harm; (II) the whistleblower had a reasonable basis to believe that the relevant entity was obstructing an investigation into the misconduct; or (III) not less than 120 days have elapsed since the whistleblower provided the information to the audit committee, chief legal officer, chief compliance officer (or their equivalent) of the relevant entity or the supervisor of the whistleblower. (C) Amount (i) In general An award issued under subparagraph (A) shall be\u2014 (I) not less than 10 percent, in total, of the amount collected of the fine imposed under this part; and (II) not more than 30 percent, in total, of the amount collected of that fine. (ii) Jointly submitted report In the case of a report that was submitted jointly by 2 or more individuals, any award issued under subparagraph (A) shall be split equally among the individuals. (D) Determination The Secretary shall determine the amount of an award made under subparagraph (A) taking into account, with respect to the information provided\u2014 (i) accuracy; (ii) relevance; (iii) timeliness; and (iv) usefulness. (4) Publication (A) In general Not later than the date on which the online portal required by paragraph (2)(A) is complete, the Secretary shall develop and implement a plan to publicize the whistleblower incentive program established by paragraph (1). (B) Funding The Secretary shall pay any expenses incurred under subparagraph (A) from amounts authorized to be appropriated to the Bureau of Industry and Security. (c) Protection of whistleblowers (1) Prohibition against retaliation (A) In general Except as provided in subparagraph (B), no employer may discharge, demote, suspend, threaten, harass, directly or indirectly, or in any other manner discriminate against a whistleblower in the terms and conditions of employment because of a lawful act done by the whistleblower\u2014 (i) in reporting violations to the employer or to a law enforcement agency; (ii) in providing information to the Secretary in accordance with this section; or (iii) in initiating, testifying in, or assisting in any investigation or judicial or administrative action based upon or related to such information. (B) Exception The protection against retaliation established by subparagraph (A) shall not apply to any individual who reports information under this section knowing that such information is false. (C) Enforcement (i) Cause of action An individual who alleges discharge or other discrimination in violation of subparagraph (A) may bring an action under this paragraph in the appropriate district court of the United States for the relief provided in subparagraph (D). (ii) Subpoenas A subpoena requiring the attendance of a witness at a trial or hearing conducted under this subparagraph may be served at any place in the United States. (iii) Statute of limitations (I) In general An action under this subparagraph shall not be entertained if commenced more than\u2014 (aa) 6 years after the date of the violation of subparagraph (A) occurred; or (bb) 3 years after the date when facts material to the right of action are known or reasonably should have been known by the employee alleging a violation of subparagraph (A). (II) Required action within 10 years Notwithstanding subclause (I), an action under this subparagraph may not in any circumstance be brought more than 10 years after the date on which the violation occurs. (D) Relief Relief for an individual prevailing in an action brought under subparagraph (C) shall include\u2014 (i) reinstatement with the same seniority status that the individual would have had, but for the discrimination; (ii) 2 times the amount of back pay otherwise owed to the individual, with interest; and (iii) compensation for litigation costs, expert witness fees, and reasonable attorneys' fees. (2) Confidentiality (A) In general Except as provided in subparagraphs (B) and (C), the Secretary and any officer or employee of the Department of Commerce shall not disclose any information, including information provided by a whistleblower to the Secretary, that could reasonably be expected to reveal the identity of the whistleblower, except in accordance with the provisions of section 552a of title 5, United States Code, unless and until required to be disclosed to a defendant or respondent in connection with a public proceeding instituted by the Secretary or any entity described in subparagraph (D). (B) Exempted statute For purposes of section 552 of title 5, United States Code, this paragraph shall be considered a statute described in subsection (b)(3)(B) of such section. (C) Rule of construction Nothing in this section is intended to limit, or shall be construed to limit, the ability of the Attorney General to present such evidence to a grand jury or to share such evidence with potential witnesses or defendants in the course of an ongoing criminal investigation. (D) Availability to government agencies (i) In general Without the loss of its status as confidential in the hands of the Secretary, all information referred to in subparagraph (A) may, in the discretion of the Secretary, when determined by the Secretary to be necessary to accomplish the purposes of this part or any regulation, order, license, or other authorization issued under this part, be made available to\u2014 (I) a Federal law enforcement agency; (II) a national security agency; (III) an appropriate regulatory authority; (IV) a self-regulatory organization; and (V) a foreign law enforcement authority. (ii) Confidentiality (I) In general Each of the entities described in subclauses (I) through (IV) of clause (i) shall maintain such information as confidential in accordance with the requirements established under subparagraph (A). (II) Foreign authorities Each of the entities described in clause (i)(V) shall maintain such information in accordance with such assurances of confidentiality as the Secretary determines appropriate. (d) Export Compliance Accountability Fund (1) Establishment Not later than 90 days after the date of the enactment of this section, there shall be established in the Treasury of the United States a fund to be known as the Export Compliance Accountability Fund (in this subsection referred to as the Fund ). (2) Availability At the end of each fiscal year, any amounts deposited into the Fund under paragraph (3) that remain in the Fund after the payment, for that fiscal year, of all expenses under paragraph (3) shall be transferred to the general fund of the Treasury. (3) Use of Fund The Fund shall be available to the Secretary, without further appropriation or fiscal year limitation, for\u2014 (A) paying awards to whistleblowers as provided in subsection (b)(3); (B) funding activities that support the whistleblower incentive program and whistleblower protections, including\u2014 (i) reviewing and investigating whistleblower reports; (ii) providing training and education on compliance with the confidentiality requirement under subsection (c)(2); and (iii) record keeping, as considered necessary by the Secretary; and (C) if all outstanding awards under subsection (b)(3) have been paid, expenses related to enforcement of this part or any regulation, order, license, or other authorization issued under this part. (4) Deposits and credits There shall be deposited into or credited to the Fund an amount equal to any fine collected by the Secretary on or after the date of the enactment of this section in any judicial or administrative action brought by the Secretary that depends on or was initiated because of original information submitted by a whistleblower. (e) Initial funding The Secretary shall pay, from amounts otherwise available to the Bureau of Industry and Security, any expenses incurred under this section before the Export Compliance Accountability Fund is established under subsection (d) and has received deposits under paragraph (3) of that subsection. .\n##### (b) Conforming amendment\nSection 1402(b)(1)(B) of the Victims of Crime Act of 1984 ( 34 U.S.C. 20101(b)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iii), by striking ; and and inserting a semicolon;\n**(2)**\nin clause (iv), by striking the semicolon and inserting ; and ; and\n**(3)**\nby adding at the end the following;\n(v) the Export Compliance Accountability Fund pursuant to section 1761A(e) of the Export Control Reform Act of 2018. .",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1473es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 1473\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Export Control Reform Act of 2018 to establish a whistleblower incentive program and provide protections to whistleblowers.\n#### 1. Short title\nThis Act may be cited as the Stop Stealing our Chips Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nViolations of the export control laws of the United States, especially the diversion of leading-edge artificial intelligence chips into countries that are adversaries of the United States, threaten the national security of the United States.\n**(2)**\nIndividuals who accurately report violations of United States export control laws play a significant role in helping authorities identify and mitigate such threats.\n**(3)**\nAn incentive program that rewards whistleblowers can significantly enhance enforcement efforts by encouraging individuals to provide high-value information on potential violations.\n#### 3. Establishment of Whistleblower Incentive Program and Whistleblower Protections\n##### (a) Establishment of Whistleblower Incentive Program and Whistleblower Protections\nThe Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ) is amended by inserting after section 1761 the following:\n1761A. Whistleblower Incentives and Protections (a) Definitions In this section: (1) Original information The term original information means information that is\u2014 (A) derived from the independent knowledge or analysis of a whistleblower; (B) not known to the Secretary from any other source; (C) not exclusively derived from an allegation made in a judicial or administrative hearing, a governmental report, hearing, audit, or investigation, or from news media, unless the whistleblower is the source of such allegation; and (D) provided to the Secretary voluntarily, without any request from the Secretary or any other government official. (2) Whistleblower (A) In general The term whistleblower means, except as provided by subparagraph (B), any individual (including an individual who is not a United States citizen) who provides, or 2 or more such individuals acting jointly who provide, to the Secretary information relating to a possible violation of this part or of any regulation, order, license, or other authorization issued under this part. (B) Exclusions The term whistleblower does not include\u2014 (i) a Federal employee acting within the scope of the duties of the employee; or (ii) an individual on any of the following lists: (I) The list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury. (II) The Denied Persons List maintained pursuant to section 764.3(a)(2) of the Export Administration Regulations. (III) The Entity List set forth in Supplement No. 4 to part 744 of the Export Administration Regulations. (b) Whistleblower Incentive Program (1) Establishment Not later than 120 days after the date of the enactment of this section, the Secretary shall establish a whistleblower incentive program to reward individuals who provide original information that leads to\u2014 (A) the imposition of fines under this part on persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part; or (B) the forfeiture of any property under section 1761(j). (2) Whistleblower reports (A) Online portal Not later than 120 days after the date of the enactment of this section, the Secretary shall develop, implement, and maintain a secure portal, or update and maintain an existing secure portal, on a website accessible to the public, for the reporting of original information relating to\u2014 (i) persons that violate, attempt to violate, conspire to violate, or cause a violation of this part or any regulation, order, license, or other authorization issued under this part; and (ii) items that have been, are being, or are about to be exported, reexported, or in-country transferred in violation of this part or any regulation, order, license, or other authorization issued under this part. (B) Anonymity (i) In general As an alternative to submission through the portal required by subparagraph (A), an individual may submit a report of original information under this subsection anonymously, including through an attorney. (ii) Exception The Secretary may require that the identity of an individual be disclosed for the individual to receive an award under paragraph (3). (C) Expedited review (i) Initial review Not later than 60 days after the date of receipt of a report from a whistleblower, the Secretary shall\u2014 (I) determine whether the report is credible; and (II) if credible, initiate a formal investigation of the allegations contained in the report. (ii) Investigation The Secretary shall pursue any formal investigation initiated under clause (i)(II) with urgency and conclude the investigation within a reasonable amount of time. (iii) Notification (I) In general Subject to the confidentiality requirements of section 1761(h), the Secretary shall update the whistleblower on the status of a report and, if applicable, the related investigation not later than 90 days after the date on which the whistleblower submitted the report and not less frequently than every 90 days thereafter. (II) Sensitive information The Secretary may omit from the updates required by subclause (I) any information that could compromise an ongoing investigation, including confirmation of the existence of any specific investigation. (D) Avoidance of frivolous reports The Secretary may prohibit an individual from making reports under this subsection if the individual has previously submitted multiple reports under this subsection that the Secretary determined under subparagraph (C)(i) were not credible. (3) Awards (A) Eligibility Subject to subparagraph (B), the Secretary may pay an award or awards to any whistleblower who provided original information that led to the imposition of a fine under this part on a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part. (B) Disqualification (i) In general Subject to clause (ii), the Secretary may not pay an award or awards to any whistleblower who provides original information with respect to a person or persons that violated, attempted to violate, conspired to violate, or caused a violation of this part or any regulation, order, license, or other authorization issued under this part, if such information was obtained through\u2014 (I) the role of the whistleblower as\u2014 (aa) an officer, director, trustee, or partner of an entity that handles internal processes for legal violations for the person or persons; (bb) an employee of an entity that conducts compliance or internal audits for the person or persons; (cc) an employee of a public accounting firm if the information was obtained while working on an engagement required by Federal securities laws, other than specific audits; or (II) any means that violates Federal or State criminal law. (ii) Exceptions Clause (i) shall not apply if\u2014 (I) the whistleblower had a reasonable basis to believe that disclosing the original information to the Secretary was necessary to stop conduct likely to cause significant financial harm; (II) the whistleblower had a reasonable basis to believe that the relevant entity was obstructing an investigation into the misconduct; or (III) not less than 120 days have elapsed since the whistleblower provided the information to the audit committee, chief legal officer, chief compliance officer (or their equivalent) of the relevant entity or the supervisor of the whistleblower. (C) Amount (i) In general An award issued under subparagraph (A) shall be\u2014 (I) not less than 10 percent, in total, of the amount collected of the fine imposed under this part; and (II) not more than 30 percent, in total, of the amount collected of that fine. (ii) Jointly submitted report In the case of a report that was submitted jointly by 2 or more individuals, any award issued under subparagraph (A) shall be split equally among the individuals. (D) Determination The Secretary shall determine the amount of an award made under subparagraph (A) taking into account, with respect to the information provided\u2014 (i) accuracy; (ii) relevance; (iii) timeliness; and (iv) usefulness. (E) Submission of information No award may be made under this paragraph based on information submitted to the Secretary unless such information is submitted under penalty of perjury. (4) Publication (A) In general Not later than the date on which the online portal required by paragraph (2)(A) is operational, the Secretary shall develop and implement a plan to publicize the whistleblower incentive program established by paragraph (1). (B) Funding The Secretary shall pay any expenses incurred under subparagraph (A) from amounts authorized to be appropriated to the Bureau of Industry and Security. (c) Protection of whistleblowers (1) Prohibition against retaliation (A) In general Except as provided in subparagraph (B), no employer may discharge, demote, suspend, threaten, harass, directly or indirectly, or in any other manner discriminate against a whistleblower in the terms and conditions of employment because of a lawful act done by the whistleblower\u2014 (i) in reporting violations to the employer or to a law enforcement agency; (ii) in providing information to the Secretary in accordance with this section; or (iii) in initiating, testifying in, or assisting in any investigation or judicial or administrative action based upon or related to such information. (B) Exception The protection against retaliation established by subparagraph (A) shall not apply to any individual who reports information under this section knowing that such information is false. (C) Enforcement (i) Cause of action An individual who alleges discharge or other discrimination in violation of subparagraph (A) may bring an action under this paragraph in the appropriate district court of the United States for the relief provided in subparagraph (D). (ii) Subpoenas A subpoena requiring the attendance of a witness at a trial or hearing conducted under this subparagraph may be served at any place in the United States. (iii) Statute of limitations (I) In general An action under this subparagraph shall not be entertained if commenced more than\u2014 (aa) 6 years after the date of the violation of subparagraph (A) occurred; or (bb) 3 years after the date when facts material to the right of action are known or reasonably should have been known by the employee alleging a violation of subparagraph (A). (II) Required action within 10 years Notwithstanding subclause (I), an action under this subparagraph may not in any circumstance be brought more than 10 years after the date on which the violation occurs. (D) Relief Relief for an individual prevailing in an action brought under subparagraph (C) shall include\u2014 (i) reinstatement with the same seniority status that the individual would have had, but for the discrimination; (ii) 2 times the amount of back pay otherwise owed to the individual, with interest; and (iii) compensation for litigation costs, expert witness fees, and reasonable attorneys' fees. (2) Confidentiality (A) In general Except as provided in subparagraphs (B) and (C), the Secretary and any officer or employee of the Department of Commerce shall not disclose any information, including information provided by a whistleblower to the Secretary, that could reasonably be expected to reveal the identity of the whistleblower, except in accordance with the provisions of section 552a of title 5, United States Code, unless and until required to be disclosed to a defendant or respondent in connection with a public proceeding instituted by the Secretary or any entity described in subparagraph (D). (B) Exempted statute For purposes of section 552 of title 5, United States Code, this paragraph shall be considered a statute described in subsection (b)(3)(B) of such section. (C) Rule of construction Nothing in this section is intended to limit, or shall be construed to limit, the ability of the Attorney General to present such evidence to a grand jury or to share such evidence with potential witnesses or defendants in the course of an ongoing criminal investigation. (D) Availability to government agencies (i) In general Without the loss of its status as confidential in the hands of the Secretary, all information referred to in subparagraph (A) may, in the discretion of the Secretary, when determined by the Secretary to be necessary to accomplish the purposes of this part or any regulation, order, license, or other authorization issued under this part, be made available to\u2014 (I) a Federal law enforcement agency; (II) a national security agency; (III) an appropriate regulatory authority or Federal investigative agency; (IV) a self-regulatory organization; and (V) a foreign law enforcement authority. (ii) Confidentiality (I) In general Each of the entities described in subclauses (I) through (IV) of clause (i) shall maintain such information as confidential in accordance with the requirements established under subparagraph (A). (II) Foreign authorities An entity described in clause (i)(V) shall maintain such information in accordance with such assurances of confidentiality as the Secretary determines appropriate. (d) Export Compliance Accountability Fund (1) Establishment Not later than 90 days after the date of the enactment of this section, there shall be established in the Treasury of the United States a fund to be known as the Export Compliance Accountability Fund (in this subsection referred to as the Fund ). (2) Availability At the end of each fiscal year, any amounts deposited into the Fund under paragraph (4) that remain in the Fund after the payment, for that fiscal year, of all expenses under paragraph (3), excluding the amount estimated for outstanding awards, shall be transferred to the general fund of the Treasury. (3) Use of Fund The Fund shall be available to the Secretary, without further appropriation or fiscal year limitation, for\u2014 (A) paying awards to whistleblowers as provided in subsection (b)(3); (B) funding activities that support the whistleblower incentive program and whistleblower protections, including\u2014 (i) reviewing and investigating whistleblower reports; (ii) providing training and education on compliance with the confidentiality requirement under subsection (c)(2); and (iii) record keeping and maintaining the portal under subsection (b)(2)(A), as considered necessary by the Secretary; and (C) if all outstanding awards under subsection (b)(3) have been paid, expenses related to enforcement of this part or any regulation, order, license, or other authorization issued under this part. (4) Deposits and credits (A) In general There shall be deposited into or credited to the Fund an amount equal to any fine collected by the Secretary on or after the date of the enactment of this section in any judicial or administrative action brought by the Secretary that depends on or was initiated because of original information submitted by a whistleblower. (B) Exception No amounts to be deposited or transferred into the United States Victims of State Sponsored Terrorism Fund pursuant to the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144 ) or the Crime Victims Fund pursuant section 1402 of the Victims of Crime Act of 1984 ( 34 U.S.C. 20101 ) shall be deposited into or credited to the Fund. (e) Initial funding The Secretary shall pay, from amounts otherwise available to the Bureau of Industry and Security, any expenses incurred under this section before the Export Compliance Accountability Fund is established under subsection (d) and has received deposits under paragraph (4) of that subsection. .\n##### (b) Conforming amendment\nSection 1402(b)(1)(B) of the Victims of Crime Act of 1984 ( 34 U.S.C. 20101(b)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iii), by striking ; and and inserting a semicolon;\n**(2)**\nin clause (iv), by striking the semicolon and inserting ; and ; and\n**(3)**\nby adding at the end the following;\n(v) the Export Compliance Accountability Fund pursuant to section 1761A(d) of the Export Control Reform Act of 2018. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2026-04-22",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1."
      },
      "number": "6322",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Stealing our Chips Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2026-05-22T19:13:55Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2026-05-22T19:11:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-22T19:14:06Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-05-22T19:14:21Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-22T19:14:01Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-05-22T19:14:15Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-22T19:13:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-27T15:48:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s1473",
          "measure-number": "1473",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1473v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill authorizes\u00a0BIS to pay an award to any whistleblower\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting retaliation against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>"
        },
        "title": "Stop Stealing our Chips Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1473.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill authorizes\u00a0BIS to pay an award to any whistleblower\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting retaliation against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1473"
    },
    "title": "Stop Stealing our Chips Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Stealing our Chips Act</strong></p><p>This bill creates a\u00a0whistleblower incentive program and establishes whistleblower protections for individuals who provide information to the Department of Commerce's Bureau of Industry and Security (BIS) related to violations of U.S. export control laws.\u00a0</p><p>Currently, BIS administers and enforces controls on the export of dual-use goods (e.g., items with both civilian and military uses) and certain military parts and components. These export controls are implemented primarily under the Export Control Reform Act of 2018 (ECRA) through the Export Administration Regulations.</p><p>Under the bill, BIS\u00a0must establish a\u00a0whistleblower incentive program to reward individuals who voluntarily report original information that results in BIS imposing fines under ECRA\u00a0on persons that violate, attempt to violate, conspire to violate, or cause a violation of ECRA or any related regulation, order, license, or authorization.</p><p>Additionally, BIS must establish a secure online portal for whistleblowers to report violations of ECRA. The bill outlines requirements for BIS to review, investigate, and provide status updates related to these reports.</p><p>The bill authorizes\u00a0BIS to pay an award to any whistleblower\u00a0who voluntarily reported original information that led to the imposition of a fine under\u00a0ECRA. The bill establishes the Export Compliance Accountability Fund for paying these awards and funding related activities.</p><p>The bill also sets forth\u00a0whistleblower protections by (1) prohibiting retaliation against individuals who act as\u00a0whistleblowers, and (2) establishing confidentiality requirements.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1473"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1473is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1473es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stop Stealing our Chips Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-22T02:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Stealing our Chips Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Export Control Reform Act of 2018 to establish a whistleblower incentive program and provide protections to whistleblowers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:28Z"
    }
  ]
}
```
