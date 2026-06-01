# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1907
- Title: Defense Against Drones Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1907
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-06-05T18:57:34Z
- Update date including text: 2025-06-05T18:57:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-06 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-06 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1907",
    "number": "1907",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Defense Against Drones Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-05T18:57:34Z",
    "updateDateIncludingText": "2025-06-05T18:57:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-06T23:05:28Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1907ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1907\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Burchett introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo allow an individual to shoot an unmanned aircraft flying over property owned by the individual under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defense Against Drones Act of 2025 .\n#### 2. Protection of private property from unmanned aircraft\n##### (a) In general\nChapter 448 of title 49, United States Code, is amended by adding at the end the following:\n44815. Protection of private property from unmanned aircraft (a) In general Subject to applicable State law relating to the discharge of a firearm, an individual may shoot an unmanned aircraft using a legally obtained shotgun if the individual reasonably believes that such aircraft is flying not more than 200 feet above property owned by the individual. (b) Return of aircraft An individual may, but shall not be required to, return an unmanned aircraft shot down under subsection (a) to the owner of such aircraft upon request by such owner. (c) Reporting Not later than 60 days after an event in which an individual shoots an unmanned aircraft under subsection (a) and is able to identify the registration number of such aircraft, the individual shall report to the Administrator of the Federal Aviation Administration\u2014 (1) the address at which such event occurred; and (2) such registration number. (d) Regulations The Administrator shall issue such regulations as are necessary to carry out this section. (e) Definition of shotgun In this section, the term shotgun has the meaning given such term in section 921 of title 18, United States Code. (f) Rule of construction Nothing in this section shall be construed to preempt or otherwise have any effect on any State law relating to tort liability or criminal liability for an action taken under subsection (a). .\n##### (b) Clerical amendment\nThe analysis for chapter 448 of title 49, United States Code, is amended by adding at the end the following:\n44815. Protection of private property from unmanned aircraft. .",
      "versionDate": "2025-03-06",
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
        "updateDate": "2025-03-21T16:23:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "House",
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
          "measure-id": "id119hr1907",
          "measure-number": "1907",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-06-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1907v00",
            "update-date": "2025-06-05"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defense Against Drones Act of 2025</strong></p><p>This bill allows an individual to shoot an unmanned aircraft (i.e., drone) using a legally obtained shotgun if the individual reasonably believes the drone is flying not more than 200 feet above the individual's property. This is subject to applicable state law on the discharge of a firearm.</p><p>Not later than 60 days after an event in which an individual shoots a drone and is able to identify its registration number, the individual must report the event's location and the registration number to the Federal Aviation Administration (FAA). </p><p>An individual may, but shall not be required to, return the drone to the owner at the owner's request.</p><p>The FAA must issue such regulations as are necessary to carry out this bill.</p>"
        },
        "title": "Defense Against Drones Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1907.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defense Against Drones Act of 2025</strong></p><p>This bill allows an individual to shoot an unmanned aircraft (i.e., drone) using a legally obtained shotgun if the individual reasonably believes the drone is flying not more than 200 feet above the individual's property. This is subject to applicable state law on the discharge of a firearm.</p><p>Not later than 60 days after an event in which an individual shoots a drone and is able to identify its registration number, the individual must report the event's location and the registration number to the Federal Aviation Administration (FAA). </p><p>An individual may, but shall not be required to, return the drone to the owner at the owner's request.</p><p>The FAA must issue such regulations as are necessary to carry out this bill.</p>",
      "updateDate": "2025-06-05",
      "versionCode": "id119hr1907"
    },
    "title": "Defense Against Drones Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defense Against Drones Act of 2025</strong></p><p>This bill allows an individual to shoot an unmanned aircraft (i.e., drone) using a legally obtained shotgun if the individual reasonably believes the drone is flying not more than 200 feet above the individual's property. This is subject to applicable state law on the discharge of a firearm.</p><p>Not later than 60 days after an event in which an individual shoots a drone and is able to identify its registration number, the individual must report the event's location and the registration number to the Federal Aviation Administration (FAA). </p><p>An individual may, but shall not be required to, return the drone to the owner at the owner's request.</p><p>The FAA must issue such regulations as are necessary to carry out this bill.</p>",
      "updateDate": "2025-06-05",
      "versionCode": "id119hr1907"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1907ih.xml"
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
      "title": "Defense Against Drones Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defense Against Drones Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow an individual to shoot an unmanned aircraft flying over property owned by the individual under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:18Z"
    }
  ]
}
```
