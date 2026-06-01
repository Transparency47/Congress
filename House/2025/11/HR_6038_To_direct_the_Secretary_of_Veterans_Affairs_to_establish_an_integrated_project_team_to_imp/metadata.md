# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6038?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6038
- Title: Improving Veteran Access to Care Act
- Congress: 119
- Bill type: HR
- Bill number: 6038
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-02T09:05:50Z
- Update date including text: 2025-12-02T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6038",
    "number": "6038",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Improving Veteran Access to Care Act",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:50Z",
    "updateDateIncludingText": "2025-12-02T09:05:50Z"
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
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
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
          "date": "2025-11-12T17:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:32:55Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6038ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6038\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Mackenzie (for himself, Mr. Pappas , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish an integrated project team to improve the process for scheduling appointments for health care from the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Veteran Access to Care Act .\n#### 2. Implementation of and report on efforts of Department of Veterans Affairs to improve health care appointment scheduling\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the appropriate committees of Congress a plan to improve the process for scheduling appointments for health care from the Department of Veterans Affairs, including improvements for both patients and employees of the Department responsible for scheduling such appointments.\n##### (b) Elements of plan\n**(1) In general**\nThe plan required by subsection (a) shall include\u2014\n**(A)**\nsuch actions, resources, technology, and process improvements as the Secretary determines necessary to ensure the Department achieves, in a timely manner, improved delivery of health care, access to health care, customer experience and service relating to the receipt of health care, and efficiency with respect to the delivery of health care; and\n**(B)**\na proposed schedule and timeline to carry out such plan.\n**(2) Objectives**\n**(A) In general**\nThe Secretary shall ensure that the plan required by subsection (a) addresses the following objectives:\n**(i)**\nTo develop or continue the development of a scheduling system that enables both personnel and patients of the Department to view available appointments for care furnished by the Department, including primary care, mental health care, and all forms of specialty care.\n**(ii)**\nTo develop or continue the development of a self-service scheduling platform, available for use by all patients of the Department, which shall\u2014\n**(I)**\nenable such patients to view available appointments and, subject to the method provided under subclause (II), fully schedule appointments for all care furnished by the Department;\n**(II)**\nif a referral is required for an appointment, provide a method for the patient to request a referral and subsequently book an appointment if the referral is approved; and\n**(III)**\nprovide such patients with the ability to cancel or reschedule appointments.\n**(iii)**\nTo create a process through which all patients of the Department can telephonically speak with a scheduler who can assist the patient to determine appointment availability and can fully schedule appointments on behalf of the patient for all care furnished by the Department.\n**(iv)**\nTo carry out such other functions, oversight, metric development and tracking, change management, cross-Department coordination, and other related matters, including improvements to employee-facing information technology, training, and processes, as the Secretary determines appropriate as it relates to scheduling tools, functions, and operations with respect to health care appointments furnished by the Department.\n**(B) Explanation of inability to implement certain objectives, features, or services**\nIf the Secretary determines that an objective under subparagraph (A), or any feature or service in connection with that objective, cannot be implemented or otherwise incorporated into a final product pursuant to the plan required by subsection (a), the Secretary shall include with the plan submitted under such subsection a report containing\u2014\n**(i)**\nan explanation as to why that objective, feature, or service cannot be implemented or incorporated, as the case may be; and\n**(ii)**\na plan for implementing the plan required by subsection (a) without that objective, feature, or service.\n##### (c) Implementation\nNot later than two years after submitting to the appropriate committees of Congress the plan required by subsection (a), the Secretary shall fully implement the plan.\n##### (d) Coordination with Electronic Health Record Modernization Program\nIn developing the plan required by subsection (a), the Secretary shall ensure that the elements and objectives of such plan set forth under subsection (b) are developed in consideration of the deployment schedule and capabilities of the Electronic Health Record Modernization Program of the Department to ensure a smooth transition to using the tools and features under such plan as relevant and appropriate.\n##### (e) Implementation reports\nNot later than each of one year and two years after the date on which the Secretary submits the plan required by subsection (a), the Secretary shall submit to the appropriate committees of Congress a report on the progress of the Secretary in implementing such plan, including\u2014\n**(1)**\nthe costs incurred to implement the plan as of the date of the report;\n**(2)**\nthe expected costs to complete implementation of the plan (including costs for management and technology);\n**(3)**\nthe schedule for deployment of any capabilities developed pursuant to the plan; and\n**(4)**\nthe goals and metrics achieved, challenges, and lessons learned in implementing the plan.\n##### (f) Rule of construction\nNothing in this section shall be construed to require the Secretary to include in the plan required by subsection (a) any technology or process that would preclude or impede the ability of a veteran to contact or schedule an appointment directly with a facility or provider through a non-online scheduling process, should the veteran choose to do so.\n##### (g) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(2) Fully schedule**\nThe term fully schedule , with respect to an appointment for health care, means that the appointment booking is completed, rather than simply requested.",
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
        "updateDate": "2025-11-18T16:25:39Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6038ih.xml"
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
      "title": "Improving Veteran Access to Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Veteran Access to Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish an integrated project team to improve the process for scheduling appointments for health care from the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:20Z"
    }
  ]
}
```
