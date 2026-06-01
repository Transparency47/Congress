# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7049
- Title: Improving Mental Health Care and Coordination for Homeless Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 7049
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-02-25T09:06:39Z
- Update date including text: 2026-02-25T09:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-02 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7049",
    "number": "7049",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Improving Mental Health Care and Coordination for Homeless Veterans Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:39Z",
    "updateDateIncludingText": "2026-02-25T09:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
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
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:01:20Z",
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
                "date": "2026-02-24T21:59:24Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-24T14:02:45Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-02T19:41:46Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7049ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7049\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Valadao introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to provide certain assessments of veterans needing homeless program services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Mental Health Care and Coordination for Homeless Veterans Act .\n#### 2. Department of Veterans Affairs assessment of veterans needing homeless program services\n##### (a) In general\nSubchapter VII of chapter 20 of title 38, United States Code, is amended by adding at the end the following new section:\n2070. Assessment of veterans needing homeless program services (a) Assessments required Not later than three days after the date on which an employee of the homeless program of the Department identifies a veteran as needing homeless program services, the employee shall conduct an assessment of the veteran that shall include\u2014 (1) an assessment of the physical and mental health needs of the veteran; (2) a plan to address the immediate and long-term mental and physical needs of the veteran; and (3) an identification of appropriate housing in which to place the veteran. (b) Inclusion in EHR A homeless program employee who conducts an assessment under subsection (a) shall ensure that\u2014 (1) the information collected as part of the assessment is consistent with the information included in the electronic health record of the veteran; and (2) personally identifiable information is collected and maintained in accordance with the policies of the Department and the Veterans Health Administration, Federal law, and ethical practices. (c) Implementation monitoring The Director of the Homeless Program Office shall ensure that appropriate homeless program employees monitor the implementation of the plans developed pursuant to subsection (a)(2) to ensure that veterans who are homeless and at-risk for homelessness and who have mental health issues are getting the appropriate level and scope of services needed to address their immediate and long-term care and support needs. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 2069 the following new item:\n2070. Assessment of veterans needing homeless program services. .",
      "versionDate": "2026-01-13",
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
        "updateDate": "2026-02-03T17:26:43Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7049ih.xml"
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
      "title": "Improving Mental Health Care and Coordination for Homeless Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-30T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Mental Health Care and Coordination for Homeless Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-30T04:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to provide certain assessments of veterans needing homeless program services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-30T04:03:28Z"
    }
  ]
}
```
