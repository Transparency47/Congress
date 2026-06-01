# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5943?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5943
- Title: THRIVE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5943
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-05T16:51:39Z
- Update date including text: 2025-12-05T16:51:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5943",
    "number": "5943",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000301",
        "district": "3",
        "firstName": "Sarah",
        "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
        "lastName": "Elfreth",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "THRIVE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T16:51:39Z",
    "updateDateIncludingText": "2025-12-05T16:51:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:30:52Z",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5943ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5943\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Ms. Elfreth (for herself and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish a Task Force on Complementary and Integrative Health/Whole Health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transforming Healing, Resilience, and Integrative Veteran Engagement Act of 2025 or the THRIVE Act of 2025 .\n#### 2. Interagency Task Force on Complementary and Integrative Health\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a task force, to be known as the Task Force on Complementary and Integrative Health/Whole Health .\n##### (b) Members\nThe task force shall be composed of the following individuals or their designees:\n**(1)**\nThe Secretary of Veterans Affairs, who shall serve as the Chair.\n**(2)**\nThe Executive Director of the Office of Mental Health and Suicide Prevention of the Department of Veterans Affairs.\n**(3)**\nThe Director of the Research and Development Office of the Department.\n**(4)**\nThe Executive Director of the Office of Patient-Centered Care and Cultural Transformation of the Department.\n**(5)**\nAt least one representative from an academic institution who specializes in complementary and integrative health research.\n**(6)**\nAt least one clinician of the Department who has experience treating veterans with one or more of the following conditions:\n**(A)**\nPost-traumatic stress disorder.\n**(B)**\nTraumatic brain injury.\n**(C)**\nDepression.\n**(D)**\nAnxiety.\n**(7)**\nAt least one representative from a veterans service organization focused on\u2014\n**(A)**\ntreatment for post-traumatic stress disorder, depression, and anxiety; or\n**(B)**\nsuicide prevention.\n**(8)**\nAt least one representative from another relevant organization involved in researching, diagnosing, or treating post-traumatic stress disorder, traumatic brain injury, depression, anxiety, or suicide prevention that the Secretary of Veterans Affairs determines is necessary.\n**(9)**\nAt least one representative from a community-based program with demonstrated success in improving veterans\u2019 mental health and well-being through complementary, integrative, or peer-led approaches.\n##### (c) Responsibilities\nThe task force shall carry out the following responsibilities:\n**(1)**\nAssessing the current access of veterans who receive medical care at Department of Veterans Affairs medical facilities to complementary and integrative health/whole health therapies and program for veterans and how to make such therapies and programs more accessible to such veterans at such facilities.\n**(2)**\nDeveloping a framework to determine\u2014\n**(A)**\nthe effectiveness of complementary and integrative health therapies, including acupuncture, biofeedback, clinical hypnosis, guided imagery, massage therapy, meditation, tai chi, qigong, and yoga, peer-supported programs, and health and wellness coaching programs as treatments for post-traumatic stress disorder, traumatic brain injury, depression, and anxiety, and for suicide prevention; and\n**(B)**\nwhether and how the Department of Veterans Affairs should expand or modify access to such therapies and programs.\n**(3)**\nIdentifying gaps in research and implementation of complementary and integrative health/whole health therapies at Department of Veterans Affairs medical facilities, including gaps in knowledge of effectiveness or safety, provider training, and availability of services.\n**(4)**\nDetermining how to integrate emerging complementary and integrative health/whole health therapies, including peer-led models and health and wellness coaching models, into the continuum of care of the Department.\n**(5)**\nAnalyzing any factors contributing to treatment dropout, low retention, or relapse among veterans and how the Department can improve outcomes for such veterans.\n**(6)**\nIdentifying any additional resources or authorities the Department needs from Congress to improve accessibility of complementary and integrative health/whole health therapies.\n##### (d) Recommendations\nNot later than one year after the date of the establishment of the task force, the task force shall submit to the Secretary of Veterans Affairs the recommendations of the task force with respect to the responsibilities under subsection (c).\n##### (e) Reporting\n**(1) Initial report**\nNot later than 90 days after the date on which the Secretary of Veterans Affairs receives the recommendations of the task force under subsection (d), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on such recommendations.\n**(2) Final report**\nNot later than 180 days after the date of submission of the report under paragraph (1), the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report containing a plan to address such recommendations.\n##### (f) Termination\nThe task force shall terminate on the date on which the task force submits the recommendations to the Secretary of Veterans Affairs under subsection (d).\n##### (g) Definitions\nIn this section:\n**(1)**\nThe terms peer-led model and peer-supported program mean a program or approach in which veterans with lived experience are trained and engaged to provide counseling, mentoring, training, or support services to other veterans, as a complement or alternative to services provided by clinical professionals.\n**(2)**\nThe term community-based program \u2014\n**(A)**\nmeans a program providing health or wellness services that is operated by a non-governmental or nonprofit entity in a local community setting, rather than directly by a Federal agency; and\n**(B)**\nincludes programs that receive funding from the Department of Veterans Affairs through grant programs or partnerships to enhance veterans\u2019 mental health, suicide prevention, or overall well-being.",
      "versionDate": "2025-11-07",
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
        "updateDate": "2025-12-05T16:51:39Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5943ih.xml"
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
      "title": "THRIVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "THRIVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transforming Healing, Resilience, and Integrative Veteran Engagement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish a Task Force on Complementary and Integrative Health/Whole Health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:16Z"
    }
  ]
}
```
