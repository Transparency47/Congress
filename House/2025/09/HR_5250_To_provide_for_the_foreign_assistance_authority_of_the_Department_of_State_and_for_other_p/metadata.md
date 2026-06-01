# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5250
- Title: To provide for the foreign assistance authority of the Department of State, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5250
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-12-15T21:52:41Z
- Update date including text: 2025-12-15T21:52:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5250",
    "number": "5250",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "To provide for the foreign assistance authority of the Department of State, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-15T21:52:41Z",
    "updateDateIncludingText": "2025-12-15T21:52:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
            "date": "2025-09-18T18:18:43Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-17T18:17:51Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-10T14:07:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5250ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5250\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Smith of New Jersey introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for the foreign assistance authority of the Department of State, and for other purposes.\nVI\nFOREIGN ASSISTANCE\n#### 601. Under Secretary for Foreign Assistance\n##### (a) Establishment\nThere shall be in the Department an Under Secretary for Foreign Assistance who shall be responsible to the Secretary of State for matters pertaining to the creation and maintenance of allies and partners to United States interests abroad, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Under Secretary for Foreign Assistance shall maintain continuous observation and coordination of all matters pertaining to assistance to foreign allies and partners in the conduct of foreign policy, including, as appropriate\u2014\n**(1)**\nproviding the strategic policy direction for, and policy and programmatic oversight of, funds and bureaus within the Under Secretary\u2019s assigned jurisdiction; and\n**(2)**\noverseeing and reviewing all matters pertaining to human rights and humanitarian affairs, including matters relating to prisoners of war and members of the United States Armed Forces Missing in Action.\n#### 602. Director of Foreign Assistance Oversight\n##### (a) Establishment\nThere is authorized to be established in the Department a Director of United States Foreign Assistance Oversight, who shall be responsible to the Under Secretary for Foreign Assistance for matters pertaining to coordination and strategic oversight of all foreign assistance activities across the Department of State, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described in subsection (a), the Director of United States Foreign Assistance Oversight shall coordinate and oversee the strategic direction, planning, and budgeting of foreign assistance programs in the conduct of foreign policy, including, as appropriate\u2014\n**(1)**\ndeveloping and implementing comprehensive foreign assistance strategies;\n**(2)**\ncoordinating interagency assistance planning;\n**(3)**\nproviding senior-level leadership for the planning, operational management, and oversight of foreign aid programming across the United States Government;\n**(4)**\nimproving strategic coordination of, and oversight over, all foreign assistance funding, focusing on efficacy and strategy;\n**(5)**\nintegrating foreign assistance strategies with the broader objectives of United States foreign policy, including security, diplomacy, and development coherence;\n**(6)**\nsupporting interagency collaboration on foreign assistance programs and policies of other agencies and entities, including the Millennium Challenge Corporation, the United States International Development Finance Corporation, United States Department of the Treasury, Trade and Development Agency, and Export-Import Bank;\n**(7)**\ngenerating data-driven performance assessments and policy diagnostics for dissemination to Congress and the Executive Office of the President;\n**(8)**\nleading coordination and oversight of vetting of foreign recipients of assistance, to ensure compliance, accountability, and alignment with United States foreign assistance policies; and\n**(9)**\nsuch other related duties as the Under Secretary for Foreign Assistance may from time to time designate.\n#### 603. Office of Foreign Assistance Oversight\n##### (a) Establishment\nThe Secretary of State shall establish an Office of Foreign Assistance Oversight, which shall perform such functions related to department-wide management of foreign assistance as the Under Secretary for Foreign Assistance may prescribe.\n##### (b) Head of office\nThe Director of Foreign Assistance Oversight shall be the head of the Office of Foreign Assistance Oversight.\n##### (c) Functions\nThe Office of Foreign Assistance Oversight shall, as appropriate\u2014\n**(1)**\nsupport the Director of Foreign Assistance Oversight in the development and implementation of comprehensive foreign assistance strategies;\n**(2)**\ncoordinate interagency assistance planning and align bilateral cooperation frameworks;\n**(3)**\ncoordinate and allocate United States foreign assistance funding across thematic and regional areas;\n**(4)**\ncontinually improve strategic coordination of and oversight over all foreign assistance funding, focusing on efficacy and strategy;\n**(5)**\ngenerate data-driven performance assessments and policy diagnostics for dissemination to Congress and the Executive Office of the President;\n**(6)**\nensure monitoring, evaluation, and transparency of foreign assistance programs; and\n**(7)**\nperform such other duties as the Director may from time to time designate.\n#### 604. Authorization of appropriations for foreign assistance\nOf the funds authorized to be appropriated to the Secretary of State under section 141, the Under Secretary for Foreign Assistance shall receive the funds necessary to fulfill the Under Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 605. Classification in United States Code\nThe Office of Law Revision Counsel shall\u2014\n**(1)**\nutilize sections 160\u2013190 of title 22, United States Code, to classify the sections of this title; and\n**(2)**\nmaintain the legislative history, under editorial notes, of repealed law which previously occupied the corresponding sections of United States Code.",
      "versionDate": "2025-09-10",
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
            "name": "Department of State",
            "updateDate": "2025-12-15T21:52:04Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-15T21:52:24Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-15T21:52:10Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-12-15T21:52:18Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-12-15T21:52:41Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-12-15T21:52:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-11T21:39:54Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5250ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the foreign assistance authority of the Department of State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T10:18:21Z"
    },
    {
      "title": "To provide for the foreign assistance authority of the Department of State, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:30Z"
    }
  ]
}
```
