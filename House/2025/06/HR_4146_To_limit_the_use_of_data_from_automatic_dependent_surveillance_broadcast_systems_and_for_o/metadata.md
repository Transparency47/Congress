# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4146
- Title: PAPA Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4146
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-05-04T18:53:40Z
- Update date including text: 2026-05-04T18:53:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-26 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-26 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4146",
    "number": "4146",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert F. [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "PAPA Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-04T18:53:40Z",
    "updateDateIncludingText": "2026-05-04T18:53:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-26T21:02:47Z",
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
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "AL"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "AR"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "OK"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SD"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "AK"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4146ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4146\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Onder introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo limit the use of data from automatic dependent surveillance-broadcast systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pilot and Aircraft Privacy Act of 2025 or the PAPA Act of 2025 .\n#### 2. Use of data from automatic dependent surveillance-broadcast\n##### (a) Limitation on use of data\nData from automatic dependent surveillance-broadcast may not be used by any person, governmental agency, or other entity to identify aircraft for the purpose of obtaining revenue from the owner or operator of such aircraft without the consent of such owner or operator.\n##### (b) Use of data by air traffic controllers\nAutomatic dependent surveillance-broadcast data\u2014\n**(1)**\nmay be used to assist air traffic controllers in tracking aircraft and improving air traffic safety and efficiency; and\n**(2)**\nmay not be used for any proposed purpose other than the purpose under paragraph (1) unless the Secretary of Transportation, after notice and an opportunity for public comment, determines that such data may be used for such proposed purposes consistent with this section.\n#### 3. Limit on use of ADS\u2013B data\nSection 46101(c) of title 49, United States Code, is amended by striking the Administrator of the Federal Aviation Administration may not and inserting neither the Administrator of the Federal Aviation Administration nor any other Federal, State, local, territorial, or Tribal official may .\n#### 4. Imposition of fees on general aviation aircraft\n##### (a) In general\nChapter 401 of title 49, United States Code, is amended by adding at the end the following:\n40133. Imposition of fees on general aviation aircraft (a) Public availability Prior to imposing a landing or takeoff fee on general aviation aircraft, the owner or operator of a public-use airport (as defined in section 47102) shall make available to the public\u2014 (1) all efforts such owner or operator has undertaken to reduce non-airside related expenses; (2) all efforts such owner or operator has undertaken to obtain revenues from sources other than general aviation aircraft; (3) the total cost estimate of the airside safety projects that such owner or operator plans to undertake, the amount or percentage of the fees imposed on general aviation aircraft that will be used to pay for such projects, and an estimated timeline to collect such amount; and (4) an assessment of the impact of any fees on the health and vitality of general aviation and on the pilots, students, nonprofit organizations and businesses that support or rely on general aviation in the area of the airport. (b) Use of fees Any revenues derived from fees imposed on general aviation aircraft described in subsection (a) may only be used for airside safety projects. (c) Regulations The Administrator of the Federal Aviation Administration may promulgate such regulations or impose such reporting requirements as may be necessary to implement this section. (d) General aviation aircraft defined In this section, the term general aviation aircraft means an aircraft that is being used for personal, recreational, flight training, or for purposes other than scheduled airline operations or military flights. .\n##### (b) Clerical amendment\nThe analysis for chapter 401 of title 49, United States Code, is amended by adding at the end the following:\n40133. Imposition of fees on general aviation aircraft. .",
      "versionDate": "2025-06-25",
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
        "updateDate": "2025-07-17T11:03:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-25",
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
          "measure-id": "id119hr4146",
          "measure-number": "4146",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-25",
          "originChamber": "HOUSE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4146v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2025-06-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pilot and Aircraft Privacy Act\u00a0or the PAPA Act of 2025</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and other government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>"
        },
        "title": "PAPA Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4146.xml",
    "summary": {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pilot and Aircraft Privacy Act\u00a0or the PAPA Act of 2025</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and other government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr4146"
    },
    "title": "PAPA Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pilot and Aircraft Privacy Act\u00a0or the PAPA Act of 2025</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and other government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr4146"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4146ih.xml"
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
      "title": "PAPA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAPA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pilot and Aircraft Privacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the use of data from automatic dependent surveillance-broadcast systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:21Z"
    }
  ]
}
```
