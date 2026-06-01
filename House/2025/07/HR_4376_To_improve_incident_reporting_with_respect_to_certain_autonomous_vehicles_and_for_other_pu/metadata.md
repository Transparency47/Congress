# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4376
- Title: AV Safety Data Act
- Congress: 119
- Bill type: HR
- Bill number: 4376
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2025-07-31T12:06:07Z
- Update date including text: 2025-07-31T12:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4376",
    "number": "4376",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "AV Safety Data Act",
    "type": "HR",
    "updateDate": "2025-07-31T12:06:07Z",
    "updateDateIncludingText": "2025-07-31T12:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4376ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4376\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Mullin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve incident reporting with respect to certain autonomous vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AV Safety Data Act .\n#### 2. Incident reporting with respect to certain autonomous vehicles\n##### (a) Reporting to National Highway Traffic Safety Administration\nNot later than 90 days after the date of the enactment of this Act, the Administrator of the National Highway Traffic Safety Administration shall promulgate regulations to require each covered entity to submit to the National Highway Traffic Safety Administration\u2014\n**(1)**\ninformation as required by the Third Amended Standing General Order 2021-01; and\n**(2)**\na monthly report that includes, with respect to the preceding month\u2014\n**(A)**\nthe number of miles traveled on public roads by covered vehicles manufactured or operated by such covered entity, disaggregated by make, model, model year, major software version, road type (freeway or non-freeway), location (including State and county), and whether an occupant was present in the vehicle;\n**(B)**\ninformation on any event during which a collision with a covered vehicle manufactured or operated by such covered entity resulted in an injury to a vulnerable road user or an occupant of a vehicle other than such covered vehicle; and\n**(C)**\ninformation on any unplanned stoppage event that involved a covered vehicle manufactured or operated by such covered entity, including\u2014\n**(i)**\nthe license plate number and vehicle identification number of such vehicle;\n**(ii)**\nthe make, model, model year, and major software version of such vehicle;\n**(iii)**\nthe date, time, and location (including State, county, and latitude and longitude) with respect to such event;\n**(iv)**\nthe type of road (freeway or non-freeway) on which such event occurred;\n**(v)**\na description of such event;\n**(vi)**\ninformation about any environmental conditions (including geography and weather) affecting the operation of such vehicle with respect to such event;\n**(vii)**\ninformation about any involvement of law enforcement, first responders, or public transit authorities with respect to such event;\n**(viii)**\ninformation about the impact of such event on passengers, vulnerable road users, or other vehicles;\n**(ix)**\ninformation about the resolution of such event;\n**(x)**\ninformation about any intervention by such covered entity with respect to such event; and\n**(xi)**\nthe amount of time in seconds between the beginning and resolution of such event and, if such covered entity intervened in such event, the amount of time in seconds between the beginning of such event and the intervention by such covered entity.\n##### (b) Scope of Level 2 Advanced Driver Assistance System reporting\nWith respect to the monthly report required under subsection (a)(2), a covered entity may only submit data from a covered vehicle with a Level 2 Advanced Driver Assistance System if such data\u2014\n**(1)**\nwas collected while such System was engaged or during the 30-second period preceding an unplanned stoppage event; and\n**(2)**\ndoes not contain personally identifiable information about a human driver of such vehicle.\n##### (c) Public availability\nBeginning on the date that is 120 days after the date of the enactment of this Act, the Administrator of the National Highway Traffic Safety Administration shall make publicly available on the website of the National Highway Traffic Safety Administration, in a machine-readable format that includes datasets, any information and reports submitted pursuant to subsection (a).\n##### (d) Amendment of regulations\n**(1) In general**\nBeginning on the date that is 10 years after the date of the enactment of this Act, and not before such date, the Administrator of the National Highway Traffic Safety Administration may rescind the regulations required by subsection (a) or amend such regulations so as to reduce the frequency and scope of information required to be submitted pursuant to such subsection.\n**(2) Rule of construction**\nNothing in paragraph (1) may be construed to prevent the Administrator of the National Highway Traffic Safety Administration, at any time, from amending the regulations required by subsection (a) in a manner consistent with such subsection.\n##### (e) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means a manufacturer or operator that is subject to the requirements of the Third Amended Standing General Order 2021-01.\n**(2) Covered vehicle**\nThe term covered vehicle means a vehicle with an Automated Driving System or a Level 2 Advanced Driver Assistance System.\n**(3) Third Amended Standing General Order 2021-01**\nThe term Third Amended Standing General Order 2021-01 means the Third Amended Standing General Order 2021-01 (relating to Incident Reporting for Automated Driving Systems (ADS) and Level 2 Advanced Driver Assistance Systems (ADAS)) of the National Highway Traffic Safety Administration with an effective date of June 16, 2025.\n**(4) Unplanned stoppage event**\nThe term unplanned stoppage event means an event, other than a collision or an incident intentionally caused by a human driver, during which, as a result of an Automated Driving System or Level 2 Advanced Driver Assistance System (or if such a System was engaged or an attempt was made to engage such a System during the 30-second period preceding such event), a covered vehicle\u2014\n**(A)**\nstops on a public road in a travel lane and is unable to proceed without retrieval, manual intervention, or the assistance of a remote operator;\n**(B)**\ninterferes with the normal functioning of public transit or public transit vehicles, including light rail;\n**(C)**\ninterferes with the activities of law enforcement or first responders; or\n**(D)**\ninterferes with a construction or work zone.\n**(5) Vulnerable road user**\nThe term vulnerable road user has the meaning given such term in section 148(a) of title 23, United States Code.\n**(6) Terms defined in Third Amended Standing General Order 2021-01**\nThe terms Advanced Driver Assistance System , Automated Driving System , Level 2 , manufacturer , and operator have the meaning given such terms in the Third Amended Standing General Order 2021-01.",
      "versionDate": "2025-07-14",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-31T12:06:07Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4376ih.xml"
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
      "title": "AV Safety Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AV Safety Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve incident reporting with respect to certain autonomous vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:27Z"
    }
  ]
}
```
