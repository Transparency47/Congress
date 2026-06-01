# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3106
- Title: Weatherizing Infrastructure in the North and Terrorism Emergency Readiness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3106
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-05-16T08:07:29Z
- Update date including text: 2026-05-16T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-05-01 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-05-01 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-05-01 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-05-01 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3106",
    "number": "3106",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Weatherizing Infrastructure in the North and Terrorism Emergency Readiness Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:29Z",
    "updateDateIncludingText": "2026-05-16T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-05-01T04:00:00Z",
                "name": "Referred to"
              }
            },
            "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
            "systemCode": "hshm05"
          },
          {
            "activities": {
              "item": {
                "date": "2025-05-01T04:00:00Z",
                "name": "Referred to"
              }
            },
            "name": "Emergency Management and Technology Subcommittee",
            "systemCode": "hshm12"
          }
        ]
      },
      "systemCode": "hshm00",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3106ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3106\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Kennedy of New York (for himself and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require the Secretary of Homeland Security to conduct a collective response to a terrorism exercise that includes the management of cascading effects on critical infrastructure during times of extreme cold weather, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weatherizing Infrastructure in the North and Terrorism Emergency Readiness Act of 2025 .\n#### 2. Exercise on terrorist attack during extreme cold\n##### (a) In general\nIn addition to, or as part of exercise programs currently carried out by the Department of Homeland Security, to enhance domestic preparedness for terrorism, promote the dissemination of homeland security information, and test the homeland security posture of the United States, the Secretary of Homeland Security, acting through appropriate offices and components of the Department, shall develop and conduct a collective response to terrorism exercise that includes management of cascading effects on critical infrastructure (as such term is defined in section 1016(e) of Public Law 107\u201356 ( 42 U.S.C. 5195c(e) )) in accordance with the requirements relating to a scenario specified in subsection (b).\n##### (b) Exercise requirements\nThe requirements relating to a scenario specified in this subsection are the following:\n**(1)**\nAn extreme cold weather event, such as an event caused by a polar vortex, with respect to access to critical services.\n**(2)**\nAny cascading effects on critical infrastructure.\n**(3)**\nHow the effects of a successful terrorist attack against critical infrastructure could be mitigated by emergency managers, State officials, and appropriate private sector and community stakeholders.\n**(4)**\nHow the resilience of communities that could be impacted by such an attack could be bolstered.\n**(5)**\nCoordination with appropriate Federal departments and agencies, and State, local, Tribal, and territorial agencies.\n**(6)**\nCoordination with appropriate private sector and community stakeholders.\n##### (c) Report\nNot later than 60 days after the completion of the exercise required under subsection (a), the Secretary of Homeland Security shall, consistent with the protection of classified information, submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate an after-action report presenting the initial findings of such exercise, any immediate and longer-term plans for incorporating lessons learned into future operations of the Department of Homeland Security, and any proposed legislative changes informed by such exercise.",
      "versionDate": "2025-04-30",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-29T12:25:46Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3106ih.xml"
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
      "title": "Weatherizing Infrastructure in the North and Terrorism Emergency Readiness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Weatherizing Infrastructure in the North and Terrorism Emergency Readiness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security to conduct a collective response to a terrorism exercise that includes the management of cascading effects on critical infrastructure during times of extreme cold weather, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:34Z"
    }
  ]
}
```
