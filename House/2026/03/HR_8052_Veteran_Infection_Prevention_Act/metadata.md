# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8052
- Title: Veteran Infection Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 8052
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-05-16T08:07:43Z
- Update date including text: 2026-05-16T08:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-25 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by Voice Vote.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-25 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8052",
    "number": "8052",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Veteran Infection Prevention Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:43Z",
    "updateDateIncludingText": "2026-05-16T08:07:43Z"
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
      "text": "Ordered to be Reported in the Nature of a Substitute by Voice Vote.",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
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
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
            "date": "2026-05-14T21:10:17Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-24T16:03:05Z",
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
                "date": "2026-04-15T13:30:40Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-15T13:09:25Z",
                "name": "Markup by"
              },
              {
                "date": "2026-03-25T13:08:37Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8052ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8052\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mrs. Kiggans of Virginia introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require that a sterile processing technician of the Veterans Health Administration holds an appropriate professional certification, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Infection Prevention Act .\n#### 2. Professional certification requirement for sterile processing technicians of the Veterans Health Administration\n##### (a) Requirement\nSection 7402(b) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (14) as (15); and\n**(2)**\nby inserting after paragraph (13) the following new paragraph:\n(14) Sterile processing technician To be eligible to be appointed to a sterile processing technician position (except for such a position that the Secretary determines is entry level), a person must be certified as a sterile processing technician by an accredited institution engaged in providing sterile processing technician training not later than two years after such an appointment. .\n##### (b) Current employees\n**(1) Applicability**\nThe amendment made by subsection (a) shall apply to a covered employee two years after the date of the enactment of this Act.\n**(2) Employee Incentive Scholarship Program**\n**(A) Requirement**\nThe Secretary of Veterans Affairs shall award to a covered employee a scholarship under subchapter VI of chapter 76 of title 38, United States Code, for certification described in of section 7402(b)(14) of such title, as amended by subsection (a).\n**(B) Period of obligated service**\nNotwithstanding section 7672(e) of such title, the period of obligated service of a covered employee awarded a scholarship pursuant to subparagraph (A) shall be a period of two years beginning on the day that the covered employee receives such certification.\n**(3) Covered employee defined**\nIn this subsection, the term covered employee means a person\u2014\n**(A)**\noccupying a sterile processing technician position in the Veterans Health Administration on the date of the enactment of this Act; and\n**(B)**\nwho, on such date, is not certified as a sterile processing technician by an accredited institution engaged in providing sterile processing technician training.",
      "versionDate": "2026-03-24",
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
        "updateDate": "2026-04-09T20:59:30Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8052ih.xml"
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
      "title": "Veteran Infection Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Infection Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require that a sterile processing technician of the Veterans Health Administration holds an appropriate professional certification, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:24Z"
    }
  ]
}
```
