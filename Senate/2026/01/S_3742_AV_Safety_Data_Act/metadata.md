# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3742
- Title: AV Safety Data Act
- Congress: 119
- Bill type: S
- Bill number: 3742
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-20T15:40:50Z
- Update date including text: 2026-02-20T15:40:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3742",
    "number": "3742",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "AV Safety Data Act",
    "type": "S",
    "updateDate": "2026-02-20T15:40:50Z",
    "updateDateIncludingText": "2026-02-20T15:40:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-01-29T22:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3742is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3742\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Markey introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve incident reporting with respect to certain autonomous vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AV Safety Data Act .\n#### 2. Incident reporting with respect to certain autonomous vehicles\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Highway Traffic Safety Administration.\n**(2) Covered entity**\nThe term covered entity means a manufacturer or operator that is subject to the requirements of the Third Amended Standing General Order 2021-01.\n**(3) Covered vehicle**\nThe term covered vehicle means a vehicle with an Automated Driving System or a Level 2 Advanced Driver Assistance System.\n**(4) Third Amended Standing General Order 2021-01**\nThe term Third Amended Standing General Order 2021-01 means the Third Amended Standing General Order 2021-01 (relating to Incident Reporting for Automated Driving Systems (ADS) and Level 2 Advanced Driver Assistance Systems (ADAS)) of the National Highway Traffic Safety Administration with an effective date of June 16, 2025.\n**(5) Third Amended Standing General Order 2021-01 terms**\nThe terms Advanced Driver Assistance System , Automated Driving System , Level 2 , manufacturer , and operator have the meanings given those terms in the Third Amended Standing General Order 2021-01.\n**(6) Unplanned stoppage event**\nThe term unplanned stoppage event means an event, other than a collision or an incident intentionally caused by a human driver, during which, as a result of an Automated Driving System or Level 2 Advanced Driver Assistance System (or if such a System was engaged or an attempt was made to engage such a System during the 30-second period preceding the event), a covered vehicle\u2014\n**(A)**\nstops on a public road in a travel lane and is unable to proceed without retrieval, manual intervention, or the assistance of a remote operator;\n**(B)**\ninterferes with the normal functioning of public transit or public transit vehicles, including light rail;\n**(C)**\ninterferes with the activities of law enforcement or first responders; or\n**(D)**\ninterferes with a construction or work zone.\n**(7) Vulnerable road user**\nThe term vulnerable road user has the meaning given the term in section 148(a) of title 23, United States Code.\n##### (b) Reporting to National Highway Traffic Safety Administration\nNot later than 90 days after the date of enactment of this Act, the Administrator shall promulgate regulations to require each covered entity to submit to the National Highway Traffic Safety Administration\u2014\n**(1)**\ninformation as required by the Third Amended Standing General Order 2021-01; and\n**(2)**\na monthly report that includes, with respect to the preceding month\u2014\n**(A)**\nthe number of miles traveled on public roads by covered vehicles manufactured or operated by the covered entity, disaggregated by make, model, model year, major software version, road type (freeway or non-freeway), location (including State and county), and whether an occupant was present in the vehicle;\n**(B)**\ninformation on any event during which a collision with a covered vehicle manufactured or operated by the covered entity resulted in an injury to a vulnerable road user or an occupant of a vehicle other than the covered vehicle; and\n**(C)**\ninformation on any unplanned stoppage event that involved a covered vehicle manufactured or operated by the covered entity, including\u2014\n**(i)**\nthe license plate number and vehicle identification number of the vehicle;\n**(ii)**\nthe make, model, model year, and major software version of the vehicle;\n**(iii)**\nthe date, time, and location (including State, county, and latitude and longitude) with respect to the event;\n**(iv)**\nthe type of road (freeway or non-freeway) on which the event occurred;\n**(v)**\na description of the event;\n**(vi)**\ninformation about any environmental conditions (including geography and weather) affecting the operation of the vehicle with respect to the event;\n**(vii)**\ninformation about any involvement of law enforcement, first responders, or public transit authorities with respect to the event;\n**(viii)**\ninformation about the impact of the event on passengers, vulnerable road users, or other vehicles;\n**(ix)**\ninformation about the resolution of the event;\n**(x)**\ninformation about any intervention by the covered entity with respect to the event; and\n**(xi)**\nthe amount of time, in seconds, between the beginning and resolution of the event and, if the covered entity intervened in the event, the amount of time, in seconds, between the beginning of the event and the intervention by the covered entity.\n##### (c) Scope of Level 2 Advanced Driver Assistance System reporting\nWith respect to the monthly report required under subsection (b)(2), a covered entity may only submit data from a covered vehicle with a Level 2 Advanced Driver Assistance System if the data\u2014\n**(1)**\nwas collected\u2014\n**(A)**\nwhile the Level 2 Advanced Driver Assistance System was engaged; or\n**(B)**\nduring the 30-second period preceding an unplanned stoppage event; and\n**(2)**\ndoes not contain personally identifiable information about a human driver of the vehicle.\n##### (d) Public availability\nBeginning on the date that is 120 days after the date of enactment of this Act, the Administrator shall make publicly available on the website of the National Highway Traffic Safety Administration, in a machine-readable format that includes datasets, any information and reports submitted pursuant to subsection (b).\n##### (e) Revision of regulations\n**(1) In general**\nBeginning on the date that is 10 years after the date of enactment of this Act, and not before that date, the Administrator may rescind the regulations required by subsection (b) or revise those regulations to reduce the frequency and scope of information required to be submitted pursuant to that subsection.\n**(2) Rule of construction**\nNothing in paragraph (1) prevents the Administrator, at any time, from revising the regulations required by subsection (b) in a manner consistent with that subsection.",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-20T15:40:50Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3742is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-02-19T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AV Safety Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve incident reporting with respect to certain autonomous vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:33Z"
    }
  ]
}
```
