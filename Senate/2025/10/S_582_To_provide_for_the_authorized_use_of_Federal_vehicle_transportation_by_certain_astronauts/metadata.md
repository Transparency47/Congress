# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/582?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/582
- Title: Astronaut Ground Travel Support Act
- Congress: 119
- Bill type: S
- Bill number: 582
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-02-04T05:06:15Z
- Update date including text: 2026-02-04T05:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-10-20 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.
- 2025-10-20 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.
- 2025-10-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 193.
- 2025-10-29 - Floor: Star Print ordered on report 119-82.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-10-20 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.
- 2025-10-20 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.
- 2025-10-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 193.
- 2025-10-29 - Floor: Star Print ordered on report 119-82.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/582",
    "number": "582",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Astronaut Ground Travel Support Act",
    "type": "S",
    "updateDate": "2026-02-04T05:06:15Z",
    "updateDateIncludingText": "2026-02-04T05:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on report 119-82.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 193.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-82.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
        "item": [
          {
            "date": "2025-10-20T20:32:50Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-13T18:07:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s582is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 582\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Cruz (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo provide for the authorized use of Federal vehicle transportation by certain astronauts.\n#### 1. Short title\nThis Act may be cited as the Astronaut Ground Travel Support Act .\n#### 2. Passenger carrier use for astronaut transportation\n##### (a) In general\nSubchapter III of chapter 201 of title 51, United States Code, is amended by adding at the end the following:\n20150. Passenger carrier use for astronaut transportation (a) Definitions In this section: (1) Government astronaut; international partner astronaut; space flight participant; space support vehicle The terms government astronaut , international partner astronaut , space flight participant , and space support vehicle have the meanings given such terms in section 50902. (2) Mission The term mission means an assignment to a space support vehicle of one or more\u2014 (A) government astronauts in the course of their employment; or (B) space flight participants. (3) Official purpose With respect to transportation, the term official purpose means transportation necessary for post-mission activities, including medical research, monitoring, diagnosis, and treatment of a government astronaut or space flight participant before receiving post-mission medical clearance to operate a motor vehicle. (4) Passenger carrier The term passenger carrier means a passenger motor vehicle, aircraft, boat, vessel, or other similar means of transportation that is owned or leased by the United States Government. (b) Authority (1) In general The Administrator may authorize the use of a passenger carrier to transport a government astronaut or space flight participant between the residence of the individual and various locations if\u2014 (A) such transportation is provided for an official purpose; and (B) the Chief of the Astronaut Office has approved, in writing, post-mission transportation of government astronauts and space flight participants under this section. (2) Maintenance, operation, and repair The Administrator may maintain, operate, and repair one or more passenger carriers for the purpose of providing transportation pursuant to the authority provided in paragraph (1). (c) Reimbursement Transportation under subsection (b)(1) of an international partner astronaut or a space flight participant who is not an employee of the United States Government shall be subject to reimbursement to the Treasury. (d) Regulations The Administrator shall promulgate such regulations as are necessary to carry out this section. (e) Applicability of section 1344 of title 31 In carrying out subsection (b), the Administrator may expend funds available to the Administration, by appropriation or otherwise, notwithstanding section 1344(a) of title 31. .\n##### (b) Clerical amendment\nThe table of contents for chapter 201 of title 51, United States Code, is amended by inserting after the item relating to section 20149 the following:\n20150. Passenger carrier use for astronaut transportation. .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s582rs.xml",
      "text": "II\nCalendar No. 193\n119th CONGRESS\n1st Session\nS. 582\n[Report No. 119\u201382]\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Cruz (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nOctober 20, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo provide for the authorized use of Federal vehicle transportation by certain astronauts.\n#### 1. Short title\nThis Act may be cited as the Astronaut Ground Travel Support Act .\n#### 2. Passenger carrier use for astronaut transportation\n##### (a) In general\nSubchapter III of chapter 201 of title 51, United States Code, is amended by adding at the end the following:\n20150. Passenger carrier use for astronaut transportation (a) Definitions In this section: (1) Government astronaut; international partner astronaut; space flight participant; space support vehicle The terms government astronaut , international partner astronaut , space flight participant , and space support vehicle have the meanings given such terms in section 50902. (2) Mission The term mission means an assignment to a space support vehicle of one or more\u2014 (A) government astronauts in the course of their employment; or (B) space flight participants. (3) Official purpose With respect to transportation, the term official purpose means transportation necessary for post-mission activities, including medical research, monitoring, diagnosis, and treatment of a government astronaut or space flight participant before receiving post-mission medical clearance to operate a motor vehicle. (4) Passenger carrier The term passenger carrier means a passenger motor vehicle, aircraft, boat, vessel, or other similar means of transportation that is owned or leased by the United States Government. (b) Authority (1) In general The Administrator may authorize the use of a passenger carrier to transport a government astronaut or space flight participant between the residence of the individual and various locations if\u2014 (A) such transportation is provided for an official purpose; and (B) the Chief of the Astronaut Office has approved, in writing, post-mission transportation of government astronauts and space flight participants under this section. (2) Maintenance, operation, and repair The Administrator may maintain, operate, and repair one or more passenger carriers for the purpose of providing transportation pursuant to the authority provided in paragraph (1). (c) Reimbursement Transportation under subsection (b)(1) of an international partner astronaut or a space flight participant who is not an employee of the United States Government shall be subject to reimbursement to the Treasury. (d) Regulations The Administrator shall promulgate such regulations as are necessary to carry out this section. (e) Applicability of section 1344 of title 31 In carrying out subsection (b), the Administrator may expend funds available to the Administration, by appropriation or otherwise, notwithstanding section 1344(a) of title 31. .\n##### (b) Clerical amendment\nThe table of contents for chapter 201 of title 51, United States Code, is amended by inserting after the item relating to section 20149 the following:\n20150. Passenger carrier use for astronaut transportation. .",
      "versionDate": "2025-10-20",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "933",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NASA Transition Authorization Act of 2025",
      "type": "S"
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
            "name": "Commuting",
            "updateDate": "2025-03-19T14:54:46Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-19T14:54:55Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-03-19T14:55:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-10T18:09:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s582",
          "measure-number": "582",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-04-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s582v00",
            "update-date": "2025-04-30"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Astronaut Ground Travel Support Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to use government-owned passenger vehicles to transport astronauts and other space flight participants to and from post-mission medical research and treatment activities. (After returning to earth, astronauts generally undergo a post-mission medical recovery program and may be prohibited from driving motor vehicles for varying periods of time.)\u00a0</p><p>Under the bill, transportation may be provided to necessary post-mission activities including medical research and the monitoring, diagnosis, and treatment of an astronaut or space flight participant before they receive post-mission clearance to operate a motor vehicle. Only astronauts employed by the U.S. government, certain international partner astronauts, and other individuals carried in launch or reentry vehicles are eligible for transportation.\u00a0</p><p>The bill also permits NASA to maintain, operate, and repair one or more passenger vehicles, including motor vehicles, aircraft, and other means of transportation, for the purpose of providing such post-mission transportation.\u00a0</p><p>The cost of transporting international partner astronauts and space flight participants not employed by the U.S. government must be reimbursed to the Department of the Treasury.\u00a0</p>"
        },
        "title": "Astronaut Ground Travel Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s582.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Astronaut Ground Travel Support Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to use government-owned passenger vehicles to transport astronauts and other space flight participants to and from post-mission medical research and treatment activities. (After returning to earth, astronauts generally undergo a post-mission medical recovery program and may be prohibited from driving motor vehicles for varying periods of time.)\u00a0</p><p>Under the bill, transportation may be provided to necessary post-mission activities including medical research and the monitoring, diagnosis, and treatment of an astronaut or space flight participant before they receive post-mission clearance to operate a motor vehicle. Only astronauts employed by the U.S. government, certain international partner astronauts, and other individuals carried in launch or reentry vehicles are eligible for transportation.\u00a0</p><p>The bill also permits NASA to maintain, operate, and repair one or more passenger vehicles, including motor vehicles, aircraft, and other means of transportation, for the purpose of providing such post-mission transportation.\u00a0</p><p>The cost of transporting international partner astronauts and space flight participants not employed by the U.S. government must be reimbursed to the Department of the Treasury.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119s582"
    },
    "title": "Astronaut Ground Travel Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Astronaut Ground Travel Support Act</strong></p><p>This bill permits the National Aeronautics and Space Administration (NASA) to use government-owned passenger vehicles to transport astronauts and other space flight participants to and from post-mission medical research and treatment activities. (After returning to earth, astronauts generally undergo a post-mission medical recovery program and may be prohibited from driving motor vehicles for varying periods of time.)\u00a0</p><p>Under the bill, transportation may be provided to necessary post-mission activities including medical research and the monitoring, diagnosis, and treatment of an astronaut or space flight participant before they receive post-mission clearance to operate a motor vehicle. Only astronauts employed by the U.S. government, certain international partner astronauts, and other individuals carried in launch or reentry vehicles are eligible for transportation.\u00a0</p><p>The bill also permits NASA to maintain, operate, and repair one or more passenger vehicles, including motor vehicles, aircraft, and other means of transportation, for the purpose of providing such post-mission transportation.\u00a0</p><p>The cost of transporting international partner astronauts and space flight participants not employed by the U.S. government must be reimbursed to the Department of the Treasury.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119s582"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s582is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s582rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Astronaut Ground Travel Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T12:03:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Astronaut Ground Travel Support Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-22T03:38:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Astronaut Ground Travel Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the authorized use of Federal vehicle transportation by certain astronauts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:22Z"
    }
  ]
}
```
