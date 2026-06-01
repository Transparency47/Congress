# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7683
- Title: VA Fiscal Management Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 7683
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-16T08:07:37Z
- Update date including text: 2026-05-16T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 13 - 10.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 13 - 10.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7683",
    "number": "7683",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "VA Fiscal Management Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:37Z",
    "updateDateIncludingText": "2026-05-16T08:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 13 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
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
      "actionDate": "2026-04-15",
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
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-15",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
            "date": "2026-05-14T20:58:06Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-25T14:06:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-15T13:30:20Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-15T12:50:16Z",
                "name": "Markup by"
              },
              {
                "date": "2026-03-25T19:28:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-24T18:02:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7683ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7683\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Bergman introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to clarify and expand the authority of the Assistant Secretary for Management of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Fiscal Management Modernization Act .\n#### 2. Clarification and expansion of authority of the Assistant Secretary for Management of the Department of Veterans Affairs\n##### (a) In general\nSection 309 of title 38, United States Code, is amended to read as follows (and the table of sections at the beginning of chapter 3 of such title is amended accordingly):\n309. Chief Financial Officer; Office of Management (a) Designation The Secretary shall designate the Assistant Secretary for Management, whose functions include budgetary and financial functions, as the Chief Financial Officer of the Department. (b) Duties The duties of the Chief Financial Officer include the following: (1) To advise the Secretary on financial management of the Department. (2) To formulate, justify, and execute the budget of the Department. (3) To control, account for, audit, and report on the finances of the Department. (4) To exercise the authority and carry out the functions specified in section 902 of title 31. (5) To ensure compliance with sections 1341, 1342, 1349, 1350, and 1511 through 1519 of title 31 (commonly referred to as the Antideficiency Act ). (6) To provide to Congress (or a congressional committee), upon request, information regarding the budget and finances of the Department. (7) To serve as the head of the Office of Management of the Department. (c) Deputy Assistant Secretaries (1) There is in the Department of Management a Deputy Assistant Secretary for Management for Financial Strategy and Budget. (2) There is in the Department of Management a Deputy Assistant Secretary for Management for Financial Operations and Internal Controls. Such Deputy Assistant Secretary shall be a career appointee (as that term is defined in section 3132(a) of title 5) within the Senior Executive Service of the Department. (d) Office of Management There is in the Department an Office of Management. (e) Legislative and Congressional Budget Information Office (1) There is within the Office of Management a Legislative and Congressional Budget Information Office (in this subsection referred to as the LCBI Office ). The Chief Financial Officer shall appoint a head of the LCBI Office who shall report exclusively to the Chief Financial Officer. (2) The sole function of the LCBI Office is to provide to Congress (or a congressional committee), accurate, timely, and certified information regarding the finances and budget of the Department. (3) Not more than 15 full-time equivalent employees, including supervisors, may be assigned to the LCBI Office. .\n##### (b) Increase to number of Deputy Assistant Secretaries\nSection 308(d)(1) of such title is amended by striking 19 and inserting 21 .\n##### (c) Financial employees\nSubchapter I of chapter 7 of such title is amended by inserting after section 728 the following new section (and the table of sections at the beginning of such chapter is amended accordingly):\n729. Employees with certain financial authority: management; limitation on authority to appoint (a) Management (1) An employee described in paragraph (2) shall report exclusively to the Chief Financial Officer of the Department designated under section 309 of this title. (2) An employee described in this paragraph is an employee of the Department\u2014 (A) whose position is that of chief financial officer of an Administration of the Department or Veterans Integrated Service Network; or (B) whose duties are substantially similar to a position described in subparagraph (A). (3) An employee described in paragraph (2) may not perform a programmatic or operational function in the Department. (b) Limitation on authority To appoint The Secretary may not establish a employee position\u2014 (1) that performs a function substantially similar to the function of the Legislative and Congressional Budget Information Office of the Department established under section 309(d) of this title; and (2) that is not within the Legislative and Congressional Budget Information Office. .\n##### (d) Implementation\nThe Secretary of Veterans Affairs shall carry out the amendments made by this section not later than 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-02-25",
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
        "updateDate": "2026-03-13T22:32:16Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7683ih.xml"
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
      "title": "VA Fiscal Management Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Fiscal Management Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to clarify and expand the authority of the Assistant Secretary for Management of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:48:32Z"
    }
  ]
}
```
