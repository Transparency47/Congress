# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2175
- Title: Pilot and Aircraft Privacy Act
- Congress: 119
- Bill type: S
- Bill number: 2175
- Origin chamber: Senate
- Introduced date: 2025-06-25
- Update date: 2026-03-19T16:46:16Z
- Update date including text: 2026-03-19T16:46:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-25: Introduced in Senate
- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-25: Introduced in Senate

## Actions

- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2175",
    "number": "2175",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Pilot and Aircraft Privacy Act",
    "type": "S",
    "updateDate": "2026-03-19T16:46:16Z",
    "updateDateIncludingText": "2026-03-19T16:46:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
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
            "date": "2025-06-25T22:53:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-25T22:53:24Z",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "AK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "MT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2175is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2175\nIN THE SENATE OF THE UNITED STATES\nJune 25 (legislative day, June 24), 2025 Mr. Budd (for himself, Mr. Sullivan , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish requirements and limitations regarding the use of automatic dependent surveillance-broadcast data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pilot and Aircraft Privacy Act .\n#### 2. Use of automatic dependent surveillance-broadcast data\n##### (a) In general\nChapter 447 of title 49, United States Code, is amended by adding at the end the following new section:\n44749. Use of automatic dependent surveillance-broadcast data (a) Limitation on use of ADS\u2013B data No person (including a government agency) may use automatic dependent surveillance-broadcast data to identify any aircraft in order to assess a fee or otherwise impose a charge on the owner or operator of such aircraft. (b) Use by air traffic controllers An air traffic controller may only use automatic dependent surveillance-broadcast data\u2014 (1) to assist in tracking aircraft and improving air traffic safety and efficiency; or (2) for any other purpose determined appropriate by the Secretary of Transportation after notice and an opportunity for public comment. .\n##### (b) Clerical amendment\nThe analysis for chapter 447 of title 49, United States Code, is amended by inserting after the item relating to section 44748 the following:\n44749. Use of automatic dependent surveillance-broadcast data. .\n#### 3. Limitation on use of ADS\u2013B data in investigations\nSection 46101(c)(1) of title 49, United States Code, is amended by striking the Administrator of the Federal Aviation may not and inserting neither the Administrator of the Federal Aviation Administration nor any other Federal, State, local, territorial, or Tribal official may .\n#### 4. Imposition of fees on general aviation aircraft\n##### (a) In general\nChapter 401 of title 49, United States Code, is amended by adding at the end the following new section:\n40133. Imposition of fees on general aviation aircraft (a) Disclosure required Prior to imposing a landing or take-off fee on any general aviation aircraft (as defined in subsection (d)), the owner or operator of a public-use airport (as defined in section 47102) shall make available to the public the following information: (1) Any efforts the airport owner or operator has undertaken to reduce non-airside related expenses. (2) Any efforts the airport owner or operator has undertaken to obtain revenues from sources other than general aviation aircraft. (3) The total cost estimate of the airside safety projects that the airport owner or operator plans to undertake, the amount or percentage of the fees imposed on general aviation aircraft that will be used to pay for such project, and an estimated timeline to collect such amount. (4) An assessment of the impact of any fees on the health and vitality of general aviation and on the pilots, students, charities, and businesses that support or rely on general aviation in the area of the airport. (b) Restriction on use of funds Any revenues derived from fees imposed on general aviation aircraft may only be used for airside safety projects. (c) Rulemaking and reporting The Administrator of the Federal Aviation Administration may promulgate such regulations or impose such reporting requirements as may be necessary to carry out this section. (d) General aviation aircraft defined For purposes of this section, the term general aviation aircraft means an aircraft that is being used for\u2014 (1) personal, recreational, or flight training purposes; or (2) purposes other than scheduled airline operations or military flights. .\n##### (b) Clerical amendment\nThe analysis for chapter 401 of title 49, United States Code, is amended by inserting after the item relating to section 40132 the following:\n40133. Imposition of fees on general aviation aircraft. .",
      "versionDate": "2025-06-25",
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
        "updateDate": "2025-07-14T15:58:31Z"
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
          "measure-id": "id119s2175",
          "measure-number": "2175",
          "measure-type": "s",
          "orig-publish-date": "2025-06-25",
          "originChamber": "SENATE",
          "update-date": "2026-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2175v00",
            "update-date": "2026-03-19"
          },
          "action-date": "2025-06-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pilot and Aircraft Privacy Act</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.\u00a0\u00a0</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to assess a fee or otherwise impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>"
        },
        "title": "Pilot and Aircraft Privacy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2175.xml",
    "summary": {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pilot and Aircraft Privacy Act</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.\u00a0\u00a0</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to assess a fee or otherwise impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s2175"
    },
    "title": "Pilot and Aircraft Privacy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pilot and Aircraft Privacy Act</strong></p><p>This bill limits how Automatic Dependent Surveillance-Broadcast (ADS-B) data may be used by the Federal Aviation Administration (FAA) and government agencies. The bill also establishes disclosure requirements for certain user fees imposed on general aviation\u00a0aircraft at public-use airports and limits the purposes for which the fees may be used.\u00a0\u00a0</p><p>As background, ADS-B transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>The bill prohibits a person or government agency from using ADS-B data to identify an aircraft in order to assess a fee or otherwise impose a charge on the aircraft owner or operator.</p><p>The bill also specifies that air traffic controllers may only use\u00a0ADS-B data to assist in tracking aircraft and improving air traffic safety and efficiency, or for other purposes determined appropriate by the Department of Transportation after notice and public comment.</p><p>Further, the bill prohibits any federal, state, local, territorial, or tribal official from\u00a0initiating an investigation (excluding a criminal investigation) of a person based exclusively on ADS-B data. Under current law, this prohibition only applies to the FAA.\u00a0</p><p>In addition, owners and operators of public-use airports must publicly disclose financial information about certain expenses and cost estimates for\u00a0airside safety projects (e.g., runway or taxiway safety improvements)\u00a0prior to charging landing or takeoff fees for general aviation aircraft (e.g., aircraft used for personal, recreational, or flight training purposes). Further, any revenue from these fees may only be used for airside safety projects.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s2175"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2175is.xml"
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
      "title": "Pilot and Aircraft Privacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pilot and Aircraft Privacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish requirements and limitations regarding the use of automatic dependent surveillance-broadcast data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T02:18:32Z"
    }
  ]
}
```
