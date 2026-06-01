# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3983?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3983
- Title: Veterans Claims Quality Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3983
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-05-28T20:41:22Z
- Update date including text: 2026-05-28T20:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3983",
    "number": "3983",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veterans Claims Quality Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-28T20:41:22Z",
    "updateDateIncludingText": "2026-05-28T20:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-24T17:13:40Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-23T17:13:27Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3983ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3983\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Luttrell introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the quality of the adjudication of claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Claims Quality Improvement Act of 2025 .\n#### 2. Notice of avoidable deferrals of claims for benefits under laws administered by the Secretary of Veterans Affairs; study and report on certain opinions of Department of Veterans Affairs Office of General Counsel\n##### (a) Notice of avoidable deferrals\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall develop policies, procedures, and technological capabilities to ensure that each employee of the Veterans Benefits Administration that commits an avoidable deferral with respect to a claim for benefits under the laws administered by the Secretary of Veterans Affairs in the National Work Queue is notified of any avoidable deferrals that such employee commits with respect to the same claim.\n##### (b) Study and report on certain OGC opinions\n**(1) Study**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Office of the General Counsel of the Department of Veterans Affairs and the Chairman of the Board of Veterans\u2019 Appeals, shall complete a study to identify\u2014\n**(A)**\nissues about which an opinion from the Office of the General Counsel of the Department would foster consistency in the decisions of the Secretary with respect to claims for benefits under the laws administered by the Secretary; and\n**(B)**\nissues raised in appeals of such decisions to the United States Court of Appeals for Veterans Claims before the date of the enactment of this Act about which the Office of the General Counsel has had inconsistent opinions in matters involving substantially similar questions of law or fact.\n**(2) Report**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives a report that includes\u2014\n**(A)**\nthe findings of the study required by paragraph (1);\n**(B)**\na statement of which issues identified pursuant to such study about which the Office of the General Counsel of the Department intends to publish an opinion; and\n**(C)**\na timeline for the publication of any such opinion.\n#### 3. Improvements to system for adjudication of claims for benefits under laws administered by Secretary of Veterans Affairs\n##### (a) Program for quality assurance in decisions of Board of Veterans\u2019 Appeals; performance reviews\n**(1) In general**\nSection 7101 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(f) (1) The Chairman shall carry out a program to ensure quality in the decisions of the Board. Under such program, the Chairman shall\u2014 (A) develop policies and procedures for\u2014 (i) measuring quality in such decisions; (ii) maintaining data and identifying trends with respect to\u2014 (I) errors in such decisions; (II) errors in decisions remanded or returned to the Board by the Court of Appeals for Veterans Claims; and (III) specific members of the Board that issued decisions that were subsequently vacated by the Court of Appeals for Veterans Claims; and (iii) ensuring any such decision of the Board to remand a claim for a benefit under a law administered by the Secretary is necessary under any applicable law or regulation; (B) with respect to a claim for such a benefit that is remanded to the Board by the Court of Appeals for Veterans Claims\u2014 (i) inform any employee of the Board responsible for drafting the decision of the Board with respect to such claim that such decision was remanded; (ii) provide any such employee with a copy of the relevant order of the Court of Appeals for Veterans Claims (including a copy of any accompanying joint motion for remand); and (iii) provide incentives to such employees to review such relevant orders and joint motions for remand; and (C) ensure, to the maximum extent practicable, that any error identified by the Board under such program is corrected before the date on which the Board issues the final decision associated with such error. (2) In developing policies and procedures to measure quality in decisions of the Board pursuant to clause (i) of subparagraph (A) of paragraph (1), the Chairman shall consider the data and trends maintained and identified pursuant to clause (ii) of such subparagraph. (3) The Chairman may use technology, including artificial intelligence, to maintain such data and identify such trends. (4) The Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report on the program required by this subsection that includes, with respect to the period covered by the report, an identification of\u2014 (A) elements, if any of the process of the Board for reviewing an appeal under this chapter that lead to errors in decisions of the Board; and (B) the most common reasons that a claim for a benefit under a law administered by the Secretary was remanded to such Board by the Court of Appeals for Veterans Claims. .\n**(2) Deadline**\nThe Secretary shall submit the first report required by paragraph (2) of such section (as added by paragraph (1)) by not later than one year after the date of the enactment of this Act.\n##### (b) Training program for certain employees of Board of Veterans\u2019 Appeals; performance reviews\n**(1) Training program**\n**(A) In general**\nChapter 71 of such title (as amended by subsection (a)) is further amended by inserting after section 7101A the following new section:\n7101B. Training program for Members of Board on timely and correct adjudication of appeals (a) In general The Secretary, in conjunction with the Chairman of the Board of Veterans\u2019 Appeals, shall develop and carry out a program to provide Members of the Board training on timely and correct adjudication of appeals under this chapter. (b) Required considerations In carrying out the program required by subsection (a), the Secretary shall consider the following: (1) Feedback, if any, from members of the Board and covered employees with respect to such program. (2) Data on errors in decisions of the Board maintained pursuant to the program for quality assurance required by subsection (f) of section 7101 of this title. (3) Any decision of the Court of Appeals for Veterans Claims to remand a claim for benefits under the laws administered by the Secretary to the Board for further action, including a joint motion to remand such claim. (c) Assessments of effectiveness The Secretary, in conjunction with the Chairman of the Board of Veterans\u2019 Appeals, shall develop a method to assess, on an annual basis, the effectiveness of the training program under this section. In developing such method, the Secretary shall consider best practices for assessing the effectiveness of training programs, including the Kirkpatrick evaluation model. (d) Report The Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report on the program required by subsection (a) that includes, with respect to the period covered by the report\u2014 (1) a statement of the topics of the training provided pursuant to this section, disaggregated by\u2014 (A) mandatory training; and (B) non-mandatory training; and (2) the results of the assessment of the effectiveness of such program required under subsection (b). (e) Covered employee defined In this section, the term covered employee means an employee of the Board who is\u2014 (1) not a member of the Board; and (2) responsible for drafting decisions of the Board. .\n**(B) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 7101A the following new item:\n7101B. Training program for Members of Board on timely and correct adjudication of appeals. .\n**(2) Performance reviews of Members of the Board**\nSection 7101A of such title (as amended by paragraph (1)) is amended\u2014\n**(A)**\nin subparagraph (B) of subsection (c)(1) by striking not less often than once every three years and inserting not less often than annually ; and\n**(B)**\nby adding at the end the following new subsection:\n(h) (1) With respect to any performance review of a covered employee, the Secretary may not consider the timeliness or quality of work of any Member of the Board. (2) In this subsection, the term covered employee has the meaning given such term in section 7101B of this title. .\n##### (c) Decisions of Board to remand\n**(1) Information relating to decisions to remand**\nSection 7104 of such title is amended in subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (1) through (3) as paragraphs (2) through (4), respsectively; and\n**(B)**\nby inserting before paragraph (2) (as so redesignated), the following new paragraph:\n(1) with respect to a claim that the Board remands for further action, a statement of the specific reasons such claim was remanded, including any failure on the part of the Secretary to comply with\u2014 (A) the Secretary\u2019s duty to assist under section 5103A of this title; and (B) the Secretary\u2019s duty to notify under section 5103 of this title; .\n**(2) Notice of remanded decision for certain employees**\nSuch section is further amended in\u2014\n**(A)**\nsubsection (e)\u2014\n**(i)**\nby redesignating paragraphs (1) through (3) as subparagraphs (A) through (C), respectively;\n**(ii)**\nby striking After and inserting (1) After ; and\n**(iii)**\nby adding at the end the following new paragraph:\n(2) If, pursuant to a decision on an appeal, the Board remands a claim for a benefit under a law administered by the Secretary for further action, the Secretary shall, to the maximum extent practicable, issue a copy of such decision to each employee of the Veterans Benefits Administration who committed the error resulting in the decision of the Board to remand, when applicable. ; and\n**(B)**\nin subsection (f), by striking under subsection (e) and inserting under paragraph (1) of subsection (e) .\n##### (d) Annual reports for Board of Veterans\u2019 Appeals\n**(1) In general**\nChapter 71 of title 38, United States Code, is amended by inserting after section 7114 the following new section:\n7115. Annual report on Board of Veterans\u2019 Appeals The Chairman of the Board shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report that includes, for each decision of the Board to remand a claim for a benefit under a law administered by the Secretary to the Secretary for further adjudication during the period covered by the report, a statement of the reasons for such decision of the Board, disaggregated by decisions on\u2014 (1) claims with a rating decision dated on or after February 19, 2019; and (2) claims with a rating decision dated before such date. .\n**(2) Deadlines**\nThe Secretary shall submit the first reports required by subsections (a) and (b) of section 7115 of such title (as added by paragraph (1)) by not later than one year after the date of the enactment of this Act.\n**(3) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 7114 the following new item:\n7115. Annual report on Board of Veterans\u2019 Appeals .\n##### (e) Plan for improvements to quality in decisions of Board\n**(1) In general**\nNot later than six months after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Chairman of the Board of Veterans\u2019 Appeals and the head of the Office of Administrative Review of the Veterans Benefits Administration, shall develop a plan to\u2014\n**(A)**\nimprove the quality of decisions of the Board to remand, pursuant to section 7104 of title 38, United States Code, claims for a benefit under a law administered by the Secretary to the Secretary for further action; and\n**(B)**\nmitigate the number of such decisions that are unnecessary under any applicable law or regulation.\n**(2) Report**\nThe Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on such plan by not later than six months after the date of the enactment of this Act.",
      "versionDate": "2025-06-12",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-06-27T16:14:09Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-27T16:14:29Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-27T16:14:35Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-27T16:14:45Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-27T16:15:02Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-27T16:14:22Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-06-27T16:14:50Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-06-27T16:14:56Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-27T16:14:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T20:29:48Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3983ih.xml"
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
      "title": "Veterans Claims Quality Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Claims Quality Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the quality of the adjudication of claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:35Z"
    }
  ]
}
```
