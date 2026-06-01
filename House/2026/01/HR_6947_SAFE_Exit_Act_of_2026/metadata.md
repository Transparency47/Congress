# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6947
- Title: SAFE Exit Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6947
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-03-18T16:14:34Z
- Update date including text: 2026-03-18T16:14:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-06 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-06 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6947",
    "number": "6947",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "SAFE Exit Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-18T16:14:34Z",
    "updateDateIncludingText": "2026-03-18T16:14:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2026-01-06",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T23:30:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T21:14:39Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T21:14:19Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-06T21:13:59Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6947ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6947\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Ms. Kelly of Illinois introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title 49, United States Code, to require each new motor vehicle to be equipped with a manual door release allowing timely exit regardless of failure of any electrical system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Accessible Funtional Emergency Exit Act of 2026 or the SAFE Exit Act of 2026 .\n#### 2. Vehicle standard for manual door release\n##### (a) Manual door release\nSubchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following new section:\n30130. Manual door release (a) In general Not later than 2 years after the date of the enactment of this section, the Secretary of Transportation shall issue a final rule amending Standard 206 to establish performance and labeling requirements for motor vehicles equipped with an electronic door latch system, including manufacture requirements for\u2014 (1) a power independent, easy-to-find manual release for each door providing occupant egress, which shall be intuitive to use and readily accessible for the occupant; and (2) means for emergency responder access to the occupant compartment when vehicle electrical power is lost. (b) Compliance date The compliance date of the revised rule issued under subsection (a) shall be not later than 2 years after the date on which that rule is issued. (c) Definitions In this section: (1) Electronic door latch The term electronic door latch means a door-locking or door-latching mechanism that relies on electrical power to release or secure a vehicle door. (2) Manual release The term manual release means a mechanical device intended for occupant egress that directly disengages the door latch without electrical power. (3) Standard 206 The term Standard 206 means Federal Motor Vehicle Safety Standard Number 206, contained in section 571.206 of title 49, Code of Federal Regulations. .\n##### (b) Clerical amendment\nThe table of sections for subchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following:\nSec. 30130. Manual door release. .",
      "versionDate": "2026-01-06",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-03-18T16:13:42Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-03-18T16:14:18Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2026-03-18T16:13:51Z"
          },
          {
            "name": "Hybrid, electric, and advanced technology vehicles",
            "updateDate": "2026-03-18T16:13:36Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-03-18T16:14:12Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-03-18T16:14:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-26T13:40:23Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6947ih.xml"
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
      "title": "SAFE Exit Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Exit Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Accessible Funtional Emergency Exit Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require each new motor vehicle to be equipped with a manual door release allowing timely exit regardless of failure of any electrical system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:20Z"
    }
  ]
}
```
