# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/961
- Title: Veterans Access to Direct Primary Care Act
- Congress: 119
- Bill type: HR
- Bill number: 961
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-04-29T08:06:13Z
- Update date including text: 2025-04-29T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/961",
    "number": "961",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veterans Access to Direct Primary Care Act",
    "type": "HR",
    "updateDate": "2025-04-29T08:06:13Z",
    "updateDateIncludingText": "2025-04-29T08:06:13Z"
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
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-06T22:43:11Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "CO"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr961ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 961\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Roy (for himself and Mr. Crane ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish a pilot program to provide veteran health savings accounts to allow veterans to receive primary care furnished under non-Department direct primary care service arrangements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Access to Direct Primary Care Act .\n#### 2. Pilot program on establishment of veteran health savings accounts to allow veterans to access direct primary care service arrangements\n##### (a) Establishment\nBeginning one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall carry out a five-year pilot program under which the Secretary shall provide eligible veterans with the option to choose to receive primary care services furnished by a non-Department of Veterans Affairs health care provider under a direct primary care service arrangement through the use of a veteran health savings account described in subsection (c). The pilot program shall be conducted under the Center for Innovation for Care and Payment under section 1703E of title 38, United States Code.\n##### (b) Eligible veteran\nFor purposes of the pilot program under this section, an eligible veteran is a veteran who is enrolled in the patient enrollment system of the Department of Veterans Affairs under section 1705 of title 38, United States Code.\n##### (c) Veteran health savings accounts\nThe Secretary shall provide to an eligible veteran who participates in the pilot program a veterans health savings account that may be used\u2014\n**(1)**\nto purchase primary care services furnished through a non-Department direct primary care service arrangement; and\n**(2)**\nfor associated costs, including\u2014\n**(A)**\nperiodic fees paid to a physician for a defined set of medical services or for the right to receive medical services on an as-needed basis;\n**(B)**\namounts paid or prepaid for medical services designed to screen for, diagnose, cure, mitigate, treat, or prevent disease and promote wellness; and\n**(C)**\nprescription or non-prescription medicines or drugs.\n##### (d) Eligibility for Department medical care\nA veteran who chooses to receive a veteran health savings account described under subsection (c) may not receive medical care furnished by the Department of Veterans Affairs that is included in the direct primary care service arrangement described in such subsection during the period the veteran participates in the pilot program.\n##### (e) Prevention of fraudulent activity\nThe Secretary shall establish a mechanism to prevent fraudulent activity in connection with payments made under this section and to ensure participating veterans use health savings accounts only as authorized under this section.\n##### (f) Amounts deposited in accounts\nThe Secretary of Veterans Affairs shall\u2014\n**(1)**\ndetermine the annual amount to be deposited in a veteran health savings account described in subsection (c) using calculations conducted by the Secretary and in consultation with an actuarial service; and\n**(2)**\nensure that each participating eligible veteran receives such amount on an annual basis during the period the veteran participates in the pilot program.\n##### (g) Direct primary care service arrangement\nIn this section, the term direct primary care service arrangement means an agreement under which a defined set of medical services are provided to a patient by a physician for fixed periodic fees.\n##### (h) Reports\n**(1) Implementation reports**\nFor each calendar quarter during the two-year period beginning on the date of the enactment of this Act, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the implementation of this section. One such report shall include a description of the final design of the pilot program.\n**(2) Annual reports**\nNot later than one year after the date on which the final implementation report required by paragraph (1) is submitted, and annually thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the results of the pilot program under this section.\n##### (i) No additional appropriations\nAmounts required to carry out this section shall be made available from amounts otherwise authorized to be appropriated for the Veterans Health Administration.\n##### (j) Termination\nThe authority of the Secretary to deposit funds in a veteran health savings account under this section shall terminate on the date that is five years after the date of the enactment of this Act.",
      "versionDate": "2025-02-04",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-11T18:13:56Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-11T18:13:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T18:48:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr961",
          "measure-number": "961",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr961v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Access to Direct Primary Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a five-year pilot program to provide veterans who are enrolled in the VA health care system with the option to receive primary care services from a non-VA health care provider under a direct primary care service arrangement and pay using a veteran health savings account.</p>"
        },
        "title": "Veterans Access to Direct Primary Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr961.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Access to Direct Primary Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a five-year pilot program to provide veterans who are enrolled in the VA health care system with the option to receive primary care services from a non-VA health care provider under a direct primary care service arrangement and pay using a veteran health savings account.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr961"
    },
    "title": "Veterans Access to Direct Primary Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Access to Direct Primary Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a five-year pilot program to provide veterans who are enrolled in the VA health care system with the option to receive primary care services from a non-VA health care provider under a direct primary care service arrangement and pay using a veteran health savings account.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr961"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr961ih.xml"
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
      "title": "Veterans Access to Direct Primary Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Access to Direct Primary Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish a pilot program to provide veteran health savings accounts to allow veterans to receive primary care furnished under non-Department direct primary care service arrangements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:19Z"
    }
  ]
}
```
