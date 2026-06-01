# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3185
- Title: Personnel Integrity in Veterans Affairs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3185
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2025-06-25T08:06:26Z
- Update date including text: 2025-06-25T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3185",
    "number": "3185",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Personnel Integrity in Veterans Affairs Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-25T08:06:26Z",
    "updateDateIncludingText": "2025-06-25T08:06:26Z"
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
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:03:15Z",
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
                "date": "2025-06-11T13:37:44Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-21T13:35:57Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3185ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3185\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Scott Franklin of Florida introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require a notation in the personnel record file of certain employees of the Department of Veterans Affairs who resign from Government employment under certain conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Personnel Integrity in Veterans Affairs Act of 2025 .\n#### 2. Submission to Congress of annual performance plans for Department of Veterans Affairs political appointees\nSection 725 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Submission to Congress Not later than 30 days after the date of the completion of an annual performance under subsection (a), the Secretary shall submit the plan to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives. .\n#### 3. Notation in Department of Veterans Affairs employee personnel record file of personnel investigation required\n##### (a) In general\nSubchapter I of chapter 7 of title 38, United States Code, is amended by adding at the end the following new section:\n729. Notation in Department of Veterans Affairs employee personnel record file of eligible personnel investigation (a) Notation required Notwithstanding section 3322 of title 5 or chapter 74 of this title, with respect to a covered employee who is the subject of an eligible personnel investigation and who resigns, retires, transfers, or otherwise separates from employment with the Department prior to the resolution of such eligible personnel investigation, the Secretary shall\u2014 (1) continue such eligible personnel investigation until it is completed; and (2) not later than 40 days after the date such eligible personnel investigation is completed, make a permanent notation of such eligible personnel investigation in the official personnel record file of such covered employee. (b) Certain consideration prohibited In carrying out an eligible personnel investigation, the Secretary may not consider the resignation, retirement, transfer, or any other separation from employment with the Department of the covered employee subject to such eligible personnel investigation. (c) Notification required Prior to making a permanent notation in the official personnel record of a covered employee under subsection (a), the Secretary shall\u2014 (1) notify the employee in writing within 5 days of the resolution of the eligible personnel investigation and provide such covered employee a copy of the adverse finding and any supporting documentation; (2) provide the covered employee with a reasonable time, but not less than 30 days, to respond in writing and to furnish affidavits and other documentary evidence to show why the adverse finding was unfounded (a summary of which shall be included in any notation made to the personnel file of such employee under subsection (e)); and (3) provide a written decision and the specific reasons therefore to the employee at the earliest practicable date. (d) Right To appeal A covered employee is entitled to appeal the decision of the Secretary to make a permanent notation under subsection (a) to\u2014 (1) the Merit Systems Protection Board under section 7701 of title 5; and (2) a Disciplinary Appeals Board under section 7464 of this title. (e) Notation of appeal (1) If a covered employee files an appeal with the Merit Systems Protection Board pursuant to subsection (c), the Secretary shall make a notation in the official personnel record file of the covered employee indicating that an appeal disputing the notation is pending not later than 2 weeks after the date on which such appeal was filed. (2) If the Secretary is the prevailing party on appeal, not later than 2 weeks after the date that the Board issues the appeal decision, the Secretary shall remove the notation made under paragraph (1) from the official personnel record file of the covered employee. (3) If the covered employee is the prevailing party on appeal, not later than 2 weeks after the date that the Board issues the appeal decision, the Secretary shall remove the notation made under paragraph (1) and the notation of an adverse finding made under subsection (a) from the official personnel record file of the covered employee. (f) Definitions In this section: (1) The term covered employee means an employee in the competitive service, the excepted service, or the Senior Executive Service within the Department. (2) The term eligible personnel investigation \u2014 (A) means a personnel investigation that commences not later than 60 days after the date on which the covered employee subject to such personnel investigation resigns, retires, transfers, or otherwise separates from employment with the Department; and (B) includes\u2014 (i) an investigation by an Inspector General; and (ii) a prospective investigation that may recommend an adverse personnel action as a result of alleged performance, misconduct, or for such cause as will promote the efficiency of the service under\u2014 (I) chapter 43 of title 5; (II) chapter 75 of such title; (III) chapter 74 of this title; or (IV) section 501 of this title; (iii) an adverse personnel action as a result of performance, misconduct, or for such cause as will promote the efficiency of the service under the provisions specified in subclauses (I) through (IV) of clause (ii); (iv) an internal investigation carried out by the Secretary, including through\u2014 (I) the Office of Accountability and Whistleblower Protection of the Department; (II) the Office of the Medical Inspector of the Veterans Health Administration; and (III) the General Counsel of the Department; and (v) an investigation carried out by the head of any other Federal agency responsible for investigation allegations of employee misconduct, including the head of\u2014 (I) the Office of the Special Counsel; and (II) the Equal Employment Opportunity Commission. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 728 the following new item:\n729. Notation in Department of Veterans Affairs employee personnel record file of personnel investigation. .",
      "versionDate": "2025-05-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:23:03Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3185ih.xml"
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
      "title": "Personnel Integrity in Veterans Affairs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Personnel Integrity in Veterans Affairs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require a notation in the personnel record file of certain employees of the Department of Veterans Affairs who resign from Government employment under certain conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:54Z"
    }
  ]
}
```
