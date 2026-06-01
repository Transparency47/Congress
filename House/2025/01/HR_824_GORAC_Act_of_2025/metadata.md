# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/824?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/824
- Title: GORAC Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 824
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-03T20:12:23Z
- Update date including text: 2025-03-03T20:12:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/824",
    "number": "824",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "GORAC Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-03T20:12:23Z",
    "updateDateIncludingText": "2025-03-03T20:12:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:07:45Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "GU"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr824ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 824\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Van Duyne (for herself, Ms. Tenney , Mr. Fallon , Mr. Gill of Texas , Mr. Weber of Texas , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the evaluation of Federal agencies and programs for duplicative, wasteful, or outdated functions, and to recommend the elimination or realignment of such functions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Government Office Realignment And Closure Act of 2025 or the GORAC Act of 2025 .\n#### 2. Evaluation of Federal agencies and programs for duplicative, wasteful, or outdated functions\n##### (a) Evaluation\n**(1) Requirement**\nNot later than 1 year after the date of the enactment of this Act, and every 10 years thereafter, the Comptroller General shall, in accordance with paragraph (2), conduct an evaluation of each Federal program carried out in the preceding 10-year period.\n**(2) Use of non-Federal auditor**\n**(A) In general**\nThe Comptroller General shall\u2014\n**(i)**\nprocure the services of a non-Federal auditor to\u2014\n**(I)**\nconduct the evaluation required by paragraph (1) on behalf of the Comptroller General; and\n**(II)**\nmake recommendations in accordance with paragraph (3) on Federal agencies and Federal programs that should be realigned or eliminated; and\n**(ii)**\ntake appropriate steps to assure that any work performed by the non-Federal auditor complies with the standards established by the Comptroller General for audits of Federal establishments, organizations, programs, activities, and functions.\n**(B) Deadline for procuring of services for initial evaluation**\nWith respect to the evaluation required to be conducted not later than 1 year after the date of the enactment of this Act, the Comptroller General shall procure the services of a non-Federal auditor in accordance with subparagraph (A)(i) not later than 30 days after the date of the enactment of this Act.\n**(3) Evaluation criteria**\nThe non-Federal auditor shall recommend under paragraph (2)(A)(ii)\u2014\n**(A)**\nthe realignment of 2 or more Federal agencies or Federal programs into a single consolidated or streamlined Federal agency or Federal program, if\u2014\n**(i)**\nsuch Federal agencies or Federal programs have the same essential function; and\n**(ii)**\nsuch function can be carried out through a single consolidated or streamlined Federal agency or Federal program;\n**(B)**\nthe realignment or elimination of any Federal agency or Federal program that has wasted Federal funds in the 10 year period preceding the evaluation by\u2014\n**(i)**\negregious spending;\n**(ii)**\nmismanagement of resources and personnel; or\n**(iii)**\nuse of such funds for personal benefit or the benefit of a special interest group; and\n**(C)**\nthe elimination of any Federal agency or Federal program that during any time in the 10 year period preceding the evaluation\u2014\n**(i)**\ncompleted its intended purpose;\n**(ii)**\nbecame irrelevant; or\n**(iii)**\nfailed to meet its objectives.\n**(4) Non-Federal auditor report**\nNot later than 1 year after the non-Federal auditor begins conducting an evaluation under this subsection, the non-Federal auditor shall submit to the Comptroller General a report containing the recommendations described under paragraph (2)(A)(ii) with respect to such evaluation.\n##### (b) Report to Congress\nNot later than 30 days after the non-Federal audit submits a report required by subsection (a)(4), the Comptroller General shall submit to Congress a report that includes\u2014\n**(1)**\nthe recommendations included in the report, with supporting documentation for all recommendations; and\n**(2)**\nthe proposed legislation described under subsection (c).\n##### (c) Proposed Legislation\n**(1) In general**\nThe Comptroller General shall propose legislation in accordance with paragraphs (2) and (3) to implement the recommendations included in the report submitted subsection (a)(4).\n**(2) Use of savings**\nThe legislation proposed under paragraph (1) shall provide that all funds saved by the implementation of the recommendations described in the report submitted under subsection (a)(3) shall be pay down the national debt.\n**(3) Relocation of federal employees**\nThe legislation proposed under paragraph (1) shall provide that if the position of an employee of a Federal agency is eliminated as a result of the implementation of the recommendations included in the report, the head of the agency shall make reasonable efforts to relocate such employee to another position within the agency or within another Federal agency.\n##### (d) Additional authorities\n**(1) Hearings**\nThe non-Federal auditor may request that the Comptroller General for the purpose of carrying out this section require, by subpoena or otherwise, the attendance and testimony of such witnesses as any member of the Comptroller considers advisable.\n**(2) Production of certain materials**\n**(A) In general**\nThe non-Federal auditor may request that the Comptroller General for the purpose of carrying out this section require, by subpoena or otherwise, the production of such books, records, correspondence, memoranda, papers, documents, tapes, and other evidentiary materials relating to any matter under investigation by the non-Federal auditor.\n**(B) Authority to decline request**\nThe Comptroller General may decline a request described under subparagraph (A).\n**(C) Issuance**\nSubpoenas issued under subparagraph (A) shall bear the signature of the Comptroller General and shall be served by any person or class of persons designated by the chairperson for that purpose.\n**(D) Enforcement**\nIn the case of contumacy or failure to obey a subpoena issued under subparagraph (A), the United States district court for the judicial district in which the subpoenaed person resides, is served, or may be found, may issue an order requiring such person to appear at any designated place to testify or to produce documentary or other evidence. Any failure to obey the order of the court may be punished by the court as a contempt of that court.\n**(E) Information from federal agencies**\nThe Comptroller General may secure directly from any Federal department or agency such information as the non-Federal auditor considers necessary to carry out this section. Upon a request made to the Comptroller General from the non-Federal auditor, the head of an agency shall furnish such information to the auditor.\n##### (e) Definitions\nIn this section:\n**(1) Entitlement program**\nThe term entitlement program means any program that makes payments (including loans and grants), the budget authority for which is not provided for in advance by appropriation Acts, to any person or government if, under the provisions of the law containing such authority, the United States is obligated to make such payments to persons or governments who meet the requirements established by such law.\n**(2) Federal agency**\n**(A) In general**\nExcept as provided in subparagraph (B), the term Federal agency has the meaning given the term Executive agency under section 105 of title 5, United States Code.\n**(B) Exceptions**\nThe term Federal agency does not include\u2014\n**(i)**\na military installation, as such term is defined in section 2801(c)(4) of title 10, United States Code; or\n**(ii)**\nany agency that solely administers entitlement programs.\n**(3) Federal program**\n**(A) In general**\nExcept as provided in subparagraph (B), the term program means any activity or function of an agency.\n**(B) Exception**\nThe term program does not include entitlement programs.\n**(4) Non-Federal auditor**\nThe term non-Federal auditor means the non-Federal auditor from which the Comptroller General procures services under subsection (a).\n#### 3. Congressional consideration of reform proposals\n##### (a) Introduction; referral; and report or discharge\n**(1) Introduction**\nOn the fifteenth calendar day on which both Houses are in session, on or immediately following the date on which the report is submitted to Congress under section 2(b), a single implementation bill shall be introduced (by request)\u2014\n**(A)**\nin the Senate by the Chair of the Committee on Homeland Security and Governmental Affairs; and\n**(B)**\nin the House of Representatives by the Chair of the Committee on Oversight and Government Reform of the House of Representatives.\n**(2) Referral**\n**(A) To the appropriate committee of jurisdiction**\nThe implementation bills introduced under paragraph (1) shall be referred to any appropriate committee of jurisdiction in the Senate and any appropriate committee of jurisdiction in the House of Representatives.\n**(B) Authority over implementation bill**\nA committee to which an implementation bill is referred under this paragraph may review and report on such bill, may report such bill to the respective House, and may not amend such bill.\n**(3) Report or discharge**\nIf a committee to which an implementation bill is referred has not reported such bill by the end of the 15th calendar day after the date of the introduction of such bill, such committee shall be immediately discharged from further consideration of such bill, and upon being reported or discharged from the committee, such bill shall be placed on the appropriate calendar.\n##### (b) Floor consideration\n**(1) In general**\nWhen the committee to which an implementation bill is referred has reported, or has been discharged under subsection (b)(3), it is at any time thereafter in order (even though a previous motion to the same effect has been disagreed to) for any Member of the respective House to move to proceed to the consideration of the implementation bill, and all points of order against the implementation bill (and against consideration of the implementation bill) are waived. The motion is highly privileged in the House of Representatives and is privileged in the Senate and is not debatable. The motion is not subject to amendment, or to a motion to postpone, or to a motion to proceed to the consideration of other business. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the implementation bill is agreed to, the implementation bill shall remain the unfinished business of the respective House until disposed of.\n**(2) Amendments**\nAn implementation bill may not be amended in the Senate or the House of Representatives.\n**(3) Debate**\nDebate on the implementation bill, and on all debatable motions and appeals in connection therewith, shall be limited to not more than 10 hours, which shall be divided equally between those favoring and those opposing the resolution. A motion further to limit debate is in order and not debatable. An amendment to, or a motion to postpone, or a motion to proceed to the consideration of other business, or a motion to recommit the implementation bill is not in order. A motion to reconsider the vote by which the implementation bill is agreed to or disagreed to is not in order.\n**(4) Vote on final passage**\nImmediately following the conclusion of the debate on an implementation bill, and a single quorum call at the conclusion of the debate if requested in accordance with the rules of the appropriate House, the vote on final passage of the implementation bill shall occur.\n**(5) Rulings of the chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate or the House of Representatives, as the case may be, to the procedure relating to an implementation bill shall be decided without debate.\n##### (c) Coordination with action by other house\nIf, before the passage by 1 House of an implementation bill of that House, that House receives from the other House an implementation bill, then the following procedures shall apply:\n**(1) Nonreferral**\nThe implementation bill of the other House shall not be referred to a committee.\n**(2) Vote on bill of other house**\n**(A) In general**\nIf prior to the passage by one House of an implementing bill of that House, that House receives the same implementing bill from the other House, then\u2014\n**(i)**\nthe procedure in that House shall be the same as if no implementing bill had been received from the other House; and\n**(ii)**\nthe vote on final passage shall be on the implementing bill of the other House.\n**(B) Exception for revenue measures received in Senate**\nThe provisions of subparagraph (A) shall not apply in the Senate to an implementing revenue bill.\n##### (d) Rules of senate and house of representatives\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and as such it is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of an implementation bill described in subsection (a), and it supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n##### (e) Definitions\nIn this section:\n**(1) Calendar day**\nThe term calendar day means a calendar day other than 1 on which either House is not in session because of an adjournment of more than 3 days to a date certain.\n**(2) Implementation bill**\nThe term implementation bill means only a bill which is introduced as provided under subsection (a), and contains the proposed legislation included in the report submitted to Congress under section 2(d), without modification.",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-03-03T20:12:23Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr824ih.xml"
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
      "title": "GORAC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GORAC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Government Office Realignment And Closure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the evaluation of Federal agencies and programs for duplicative, wasteful, or outdated functions, and to recommend the elimination or realignment of such functions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:28Z"
    }
  ]
}
```
