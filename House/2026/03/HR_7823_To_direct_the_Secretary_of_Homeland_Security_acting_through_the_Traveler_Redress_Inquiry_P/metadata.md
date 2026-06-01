# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7823
- Title: To direct the Secretary of Homeland Security, acting through the Traveler Redress Inquiry Program of the Department of Homeland Security, to provide to individuals whose enrollment in a Trusted Traveler program is denied, suspended, or early terminated an option to appeal such denial, suspension, or early termination, as the case may be, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7823
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-16T08:07:18Z
- Update date including text: 2026-05-16T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-06 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-06 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7823",
    "number": "7823",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "To direct the Secretary of Homeland Security, acting through the Traveler Redress Inquiry Program of the Department of Homeland Security, to provide to individuals whose enrollment in a Trusted Traveler program is denied, suspended, or early terminated an option to appeal such denial, suspension, or early termination, as the case may be, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:18Z",
    "updateDateIncludingText": "2026-05-16T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-06",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-06T20:53:14Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-05T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7823ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7823\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Ms. Escobar introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Homeland Security, acting through the Traveler Redress Inquiry Program of the Department of Homeland Security, to provide to individuals whose enrollment in a Trusted Traveler program is denied, suspended, or early terminated an option to appeal such denial, suspension, or early termination, as the case may be, and for other purposes.\n#### 1. Denial, suspension, or early termination of enrollment in a Trusted Traveler program\n##### (a) In general\nUpon denying, suspending, or early terminating an individual\u2019s enrollment in a program specified in subsection (d), the Secretary of Homeland Security (in this section referred to as the Secretary ), acting through the Traveler Redress Inquiry Program (TRIP) of the Department of Homeland Security, shall carry out the following:\n**(1)**\nProvide to such individual an option to appeal such denial, suspension, or early termination, as the case may be.\n**(2)**\nProvide in writing to such individual information relating to the following:\n**(A)**\nThe reason for such denial, suspension, or early termination, as the case may be.\n**(B)**\nThe option under paragraph (1), including relevant dates and associated time frames relating to such option.\n**(C)**\nAny other options of which the Secretary may be aware for such individual to so appeal, including relevant dates and associated time frames relating to any such other options.\n**(D)**\nAny options for such individual to reapply for such enrollment, including relevant dates and associated time frames relating to any such options.\n##### (b) Publicly available information\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall make publicly available on a website of the Department of Homeland Security the following:\n**(1)**\nInformation relating to the options referred to in subparagraphs (B) through (D) of subsection (a)(2).\n**(2)**\nAn identification of a telephone number of the Department that an individual pursuing an appeal under subsection (a)(1) may call for information relating to such appeal, including the status of such appeal.\n##### (c) Status updates\nIf an individual appeals through TRIP regarding the denial, suspension, or early termination of such individual\u2019s enrollment in a program specified in subsection (d), not less than frequently than every 30 days during the period in which such appeal is pending, the Secretary shall provide in writing to such individual an update on the status of such appeal.\n##### (d) Programs specified\nA program specified in this subsection is any of the following:\n**(1)**\nThe PreCheck Program under section 44919 of title 49, United States Code.\n**(2)**\nThe Global Entry, SENTRI, and FAST programs under subsection (k) of section 7208 of the Intelligence Reform and Terrorism Prevention Act of 2004 ( Public Law 108\u2013458 ; 8 U.S.C. 1365b ).\n**(3)**\nThe NEXUS program under section 404 of the Enhanced Border Security and Visa Entry Reform Act of 2002 ( Public Law 107\u2013173 ; 8 U.S.C. 1753 ).\n**(4)**\nThe Asia-Pacific Economic Cooperation Business Travel Card program under section 418 of the Homeland Security Act of 2002 ( 6 U.S.C. 218 ).",
      "versionDate": "2026-03-05",
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
        "name": "Immigration",
        "updateDate": "2026-04-01T16:32:36Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7823ih.xml"
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
      "title": "To direct the Secretary of Homeland Security, acting through the Traveler Redress Inquiry Program of the Department of Homeland Security, to provide to individuals whose enrollment in a Trusted Traveler program is denied, suspended, or early terminated an option to appeal such denial, suspension, or early termination, as the case may be, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:29Z"
    },
    {
      "title": "To direct the Secretary of Homeland Security, acting through the Traveler Redress Inquiry Program of the Department of Homeland Security, to provide to individuals whose enrollment in a Trusted Traveler program is denied, suspended, or early terminated an option to appeal such denial, suspension, or early termination, as the case may be, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T09:06:45Z"
    }
  ]
}
```
