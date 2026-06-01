# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3477
- Title: Ensuring Airline Resiliency to Reduce Delays and Cancellations Act
- Congress: 119
- Bill type: HR
- Bill number: 3477
- Origin chamber: House
- Introduced date: 2025-05-17
- Update date: 2025-07-17T19:50:18Z
- Update date including text: 2025-07-17T19:50:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-17: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-18 - Committee: Referred to the Subcommittee on Aviation.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 57 - 7.
- 2025-06-11 - Committee: Subcommittee on Aviation Discharged
- Latest action: 2025-05-17: Introduced in House

## Actions

- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-18 - Committee: Referred to the Subcommittee on Aviation.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 57 - 7.
- 2025-06-11 - Committee: Subcommittee on Aviation Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-17",
    "latestAction": {
      "actionDate": "2025-05-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3477",
    "number": "3477",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000560",
        "district": "2",
        "firstName": "Rick",
        "fullName": "Rep. Larsen, Rick [D-WA-2]",
        "lastName": "Larsen",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Ensuring Airline Resiliency to Reduce Delays and Cancellations Act",
    "type": "HR",
    "updateDate": "2025-07-17T19:50:18Z",
    "updateDateIncludingText": "2025-07-17T19:50:18Z"
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
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 57 - 7.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Aviation Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
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
      "actionDate": "2025-05-18",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-17",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-17",
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
            "date": "2025-06-11T14:46:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-11T14:46:00Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-05-17T14:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-18T14:28:27Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-05-17",
      "state": "TN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3477ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3477\nIN THE HOUSE OF REPRESENTATIVES\nMay 17, 2025 Mr. Larsen of Washington (for himself and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to require certain air carriers to develop and regularly update an operational resiliency strategy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Airline Resiliency to Reduce Delays and Cancellations Act .\n#### 2. Airline operational resiliency plans\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall require a covered carrier to develop and regularly update an operational resiliency strategy to prevent or limit the impact of future flight disruptions on passengers.\n##### (b) Operational resiliency strategy\nIn each operational resiliency strategy developed under subsection (a), a covered carrier shall include a description of\u2014\n**(1)**\nthe potential impact of severe weather and other reasonably anticipated disruptive events on the operations of the carrier and how the carrier seeks to prevent or limit the impact of such events on passengers;\n**(2)**\nthe potential impact of severe weather events and other reasonably anticipated disruptive events on\u2014\n**(A)**\nstaffing models, including the ability of such models to ensure the workforce is able to adequately respond to such events and reschedule passengers, flight crews, operations staff, and other appropriate personnel; and\n**(B)**\nthe current information and technology systems of the carrier, including crew scheduling systems, and the preparedness of such systems to continue operations after such an event or disruption;\n**(3)**\nthe preparedness of the carrier to maintain operations and limit or prevent the impact of other potential disruptive events identified by the carrier;\n**(4)**\nthe extent to which the carrier addresses known cybersecurity risks and information technology deficiencies and vulnerabilities to prevent potential flight disruptions; and\n**(5)**\nany other issues the Secretary determines appropriate to protect consumers and maintain the operational stability of the airline industry.\n##### (c) Proprietary information\nThe Secretary shall develop a method to protect the confidentiality of any trade secret or proprietary information submitted in an operational resiliency strategy under subsection (b).\n##### (d) Evaluation\n**(1) Audit**\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall initiate an audit to evaluate the effectiveness of the operational resiliency strategies developed under this section by covered air carriers.\n**(2) Stakeholder feedback**\nUpon completion of the audit under paragraph (1), the Comptroller General shall solicit responses from the covered carriers regarding the findings of the audit and include any such responses in the report in paragraph (3).\n**(3) Report**\nNot later than 1 year after completion of the audit conducted under paragraph (1), the Comptroller General shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the findings of the audit.\n##### (e) Rule of construction\nNothing in this section shall be construed to\u2014\n**(1)**\ngrant additional authority to the Secretary beyond the authority to require a covered air carrier to develop or update an operational resiliency strategy in accordance with this Act; or\n**(2)**\nprevent the Secretary from assessing an operational resiliency strategy and providing guidance and technical assistance to a covered carrier in developing and updating such a strategy required under this Act.\n##### (f) Covered carrier\nIn this section, the term covered carrier has the meaning given such term in section 259.3 of title 14, Code of Federal Regulations (or successor regulations).",
      "versionDate": "2025-05-17",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-06-18T19:37:37Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-06-18T19:37:37Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-06-18T19:37:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-18T19:37:37Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-18T19:37:37Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-06-18T19:37:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-27T15:02:20Z"
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
      "date": "2025-05-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3477ih.xml"
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
      "title": "Ensuring Airline Resiliency to Reduce Delays and Cancellations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Airline Resiliency to Reduce Delays and Cancellations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to require certain air carriers to develop and regularly update an operational resiliency strategy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:32Z"
    }
  ]
}
```
