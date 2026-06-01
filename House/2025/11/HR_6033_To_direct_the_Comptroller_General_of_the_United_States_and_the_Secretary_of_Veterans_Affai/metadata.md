# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6033
- Title: STRIVE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6033
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-02T09:05:57Z
- Update date including text: 2025-12-02T09:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6033",
    "number": "6033",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "STRIVE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:57Z",
    "updateDateIncludingText": "2025-12-02T09:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:33:53Z",
              "name": "Referred to"
            }
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6033ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6033\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Horsford introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Comptroller General of the United States and the Secretary of Veterans Affairs to each report on certain disparities that affect the receipt of certain benefits administered by the Secretary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Transparent Reporting to Improve Veteran Equality Act of 2025 or the STRIVE Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to an internal report of the Department of Defense, Black members of the Armed Forces are more likely than White members to be the subject of\u2014\n**(A)**\nan administrative action, including an investigation into alleged misconduct;\n**(B)**\na nonjudicial punishment; or\n**(C)**\na trial by court-martial.\n**(2)**\nCertain administrative actions, nonjudicial punishments, and court-martial sentences may adversely affect the eligibility of a former member of the Armed Forces to receive disability benefits administered by the Secretary of Veterans Affairs.\n**(3)**\nAccording to the report titled VA Disability Benefits: Actions Needed to Further Examine Racial and Ethnic Disparities in Compensation (GAO\u201323\u2013106097), published on July 26, 2023\u2014\n**(A)**\nBlack, non-Hispanic applicants for such benefits experience the lowest rate of approval for such benefits compared to applicants of other races or ethnicities;\n**(B)**\na Black, non-Hispanic applicant is 14 percent less likely to be approved for such benefits than a White, non-Hispanic applicant; and\n**(C)**\nthe rates of approval for such benefits for Black, male applicants are between 3 and 22 percent lower than the rates of approval for applicants of other races or genders.\n**(4)**\nFemale former members of the Armed Forces are less likely to apply for such benefits than male former members.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\neach former member of the Armed Forces made heroic sacrifices while serving in the Armed Forces, such as risking the life of the former member, to preserve the freedom of the United States; and\n**(2)**\nthe collection and publication by the Secretary of accurate data regarding the race, ethnicity, and gender of all applicants for, and recipients of, disability benefits administered by the Secretary would enable the Secretary and Congress to identify and address any disparity based on the race, ethnicity, or gender of a former member of the Armed Forces, with respect to the receipt of such benefits.\n#### 3. Reports on racial, ethnic, and gender disparities with respect to disability benefits administered by the Secretary of Veterans Affairs\n##### (a) Government Accountability Office report\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees a report that includes the following elements:\n**(1)**\nStatistics for the 15-year period immediately prior to the date of the enactment of this Act that describe\u2014\n**(A)**\nthe characterization of discharge or dismissal of each former member of the Armed Forces who separated from the Armed Forces during such period, disaggregated by the race, ethnicity, and gender of the former member; and\n**(B)**\nthe number of such former members, disaggregated by the race, ethnicity, and gender of each such former member, who\u2014\n**(i)**\nrequested review of the characterization of discharge or dismissal by an appropriate board;\n**(ii)**\nreceived review of the characterization of discharge or dismissal by an appropriate board;\n**(iii)**\nreceived a change to the characterization of discharge or dismissal as a result of a decision by an appropriate board;\n**(iv)**\napplied for disability benefits administered by the Secretary of Veterans Affairs;\n**(v)**\napplied for and received such benefits; and\n**(vi)**\napplied for and were denied such benefits for reason of characterization of discharge or dismissal.\n**(2)**\nThe determination of the Comptroller General whether there is a disparity based on the race, ethnicity, or gender of a former member, with respect to the receipt of\u2014\n**(A)**\nreview of the characterization of discharge or dismissal by an appropriate board; or\n**(B)**\na change to the characterization of discharge or dismissal as a result of a decision by an appropriate board.\n**(3)**\nThe assessment of the Comptroller General whether there is a relationship between\u2014\n**(A)**\nany disparity determined under paragraph (2); and\n**(B)**\nany disparity determined by the Comptroller General in the covered report, with respect to disability benefits administered by the Secretary.\n##### (b) Secretary of Veterans Affairs: reports; plan; implementation\n**(1) Initial report**\nNot later than 365 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives, and make available on a publicly accessible website of the Department of Veterans Affairs, a report that includes the following elements:\n**(A)**\nA description of any specific actions taken or processes implemented by the Secretary to address the limitations identified by the Comptroller General in the covered report, with respect to the collection and availability of data regarding each racial and ethnic group to which a former member of the Armed Forces belongs.\n**(B)**\nAn identification by the Secretary, based on information in the covered report, of every significant cause of a racial, ethnic, or gender disparity with respect to disability benefits administered by the Secretary.\n**(C)**\nThe three-year plan of the Secretary to address each significant cause identified under subparagraph (B).\n**(2) Implementation of plan; annual report**\nThe Secretary shall\u2014\n**(A)**\nimplement the plan under paragraph (1)(C) not later than one day after the submission of the report under paragraph (1); and\n**(B)**\nannually for each year during which the Secretary is carrying out such plan, make available on a publicly accessible website of the Department a report summarizing, for the period covered by the report, the actions of the Secretary pursuant to such plan.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term appropriate board means\u2014\n**(A)**\na board for the correction of military records under section 1552 of title 10, United States Code; or\n**(B)**\na board of review under section 1553 of such title.\n**(2)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services of the Senate;\n**(B)**\nthe Committee on Armed Services of the House of Representatives;\n**(C)**\nthe Committee on Veterans\u2019 Affairs of the Senate; and\n**(D)**\nthe Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(3)**\nThe term covered report means the report titled VA Disability Benefits: Actions Needed to Further Examine Racial and Ethnic Disparities in Compensation (GAO\u201323\u2013106097), published on July 26, 2023.",
      "versionDate": "2025-11-12",
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
        "updateDate": "2025-11-25T19:15:36Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6033ih.xml"
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
      "title": "STRIVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STRIVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Transparent Reporting to Improve Veteran Equality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General of the United States and the Secretary of Veterans Affairs to each report on certain disparities that affect the receipt of certain benefits administered by the Secretary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:19Z"
    }
  ]
}
```
