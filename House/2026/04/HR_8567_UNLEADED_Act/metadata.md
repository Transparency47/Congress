# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8567
- Title: UNLEADED Act
- Congress: 119
- Bill type: HR
- Bill number: 8567
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-21T17:00:11Z
- Update date including text: 2026-05-21T17:00:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8567",
    "number": "8567",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "UNLEADED Act",
    "type": "HR",
    "updateDate": "2026-05-21T17:00:11Z",
    "updateDateIncludingText": "2026-05-21T17:00:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8567ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8567\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Beyer (for himself, Mr. Obernolte , Mr. Garcia of California , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Administrator of the Federal Aviation Administration to establish an education program on unleaded aviation gasoline, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Undoing National Lead Emissions through Authorizing Directed Education from DOT Act or the UNLEADED Act .\n#### 2. Education program on unleaded gasoline\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall establish and disseminate an education program to provide general aviation pilots, flight schools, airport managers and operators, aircraft maintenance technicians, fixed-base operators, and other members of the general aviation community with information about new unleaded aviation gasoline authorized for use in aircraft and aircraft engines by the Administrator.\n##### (b) Requirements\n**(1) In general**\nIn establishing the education program under subsection (a), the Administrator shall publish on a website of the Administration, or a public website, information about unleaded aviation gasoline authorized for use in aircraft and aircraft engines, including\u2014\n**(A)**\ninformation about the compatibility of such gasoline with aircraft and aircraft engines;\n**(B)**\nthe status of all variations of unleaded aviation gasoline undergoing evaluation and authorization for use by the Administrator;\n**(C)**\nto the extent feasible, information about when unleaded aviation gasoline products become available for purchase;\n**(D)**\na list of any relevant information, including supplemental type certificates, required for a general aviation pilot to use such gasoline;\n**(E)**\neducational information on unleaded aviation gasoline safety; and\n**(F)**\ninformation about the availability of any Federal initiatives or incentives (including tax credits) relating to such gasoline.\n**(2) Authorization tracking mechanism**\nThe Administrator shall make the information described in paragraph (1)(B) available through a publicly available and continuously updated authorization tracking mechanism.\n**(3) Public availability**\nThe Administrator shall continuously update the information described in paragraph (1) and ensure such information is made available to\u2014\n**(A)**\nflight instructors, pilot schools, and other pilot training providers;\n**(B)**\nfixed-base operators and the employees of such operators;\n**(C)**\ngeneral aviation aircraft users, aircraft owners, aircraft pilots, and aircraft operators; and\n**(D)**\nthe general public.\n##### (c) Training\nThe Administrator shall coordinate with general aviation industry, fuel providers, and fixed-based operators to facilitate annual education and training for leadership and staff of fixed-base operators to ensure that individuals assisting with transporting and handling unleaded aviation gasoline are informed of fuel type differences and the impacts such fuels have on airplanes.\n##### (d) Existing partnership\nThe Administrator may use an existing partnership, including the EAGLE Initiative, to carry out this Act.\n##### (e) Termination\nThe education program established under subsection (a) shall terminate on December 31, 2036.\n##### (f) Briefing\nNot later than 6 months after the Administrator establishes the education program under subsection (a), and periodically thereafter until the termination date described in subsection (e), the Administrator shall provide to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee of Commerce, Science, and Transportation of the Senate a briefing containing the status of, and any findings with respect to, such program, including the following elements:\n**(1)**\nA year-to-date frequency of updates to the Administration website and information rollout to flight schools and fixed-base operators.\n**(2)**\nThe progress of unleaded aviation gasoline currently undergoing an evaluation and authorization or approval process by the Administrator for use in aircraft and aircraft engines.\n**(3)**\nAn estimated total number of gallons of unleaded fuel sold per year compared with the number of gallons sold per year of 100LL.",
      "versionDate": "2026-04-29",
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
        "updateDate": "2026-05-21T17:00:11Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8567ih.xml"
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
      "title": "UNLEADED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UNLEADED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Undoing National Lead Emissions through Authorizing Directed Education from DOT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Federal Aviation Administration to establish an education program on unleaded aviation gasoline, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:44Z"
    }
  ]
}
```
