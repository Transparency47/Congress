# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7795
- Title: VA SUBCON Act
- Congress: 119
- Bill type: HR
- Bill number: 7795
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-01T20:31:46Z
- Update date including text: 2026-04-01T20:31:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7795",
    "number": "7795",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "VA SUBCON Act",
    "type": "HR",
    "updateDate": "2026-04-01T20:31:46Z",
    "updateDateIncludingText": "2026-04-01T20:31:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
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
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7795ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7795\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. King-Hinds introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish and maintain a database of certified veteran-owned small businesses and service-disabled veteran-owned small businesses to assist the Department of Veterans Affairs in meeting its subcontracting goals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Subcontractor Competition and Opportunity Network Act or the VA SUBCON Act .\n#### 2. Veterans Affairs Subcontractor Competition and Opportunity Network Database\n##### (a) Database required\n**(1) In general**\nThe Secretary of Veterans Affairs, acting through the Director of Small and Disadvantaged Business Utilization of the Department of Veterans Affairs (as established pursuant to section 15(k) of the Small Business Act ( 15 U.S.C. 644(k) )), shall establish and maintain a database of small business concerns certified by the Small Business Administration as small business concerns owned and controlled by veterans.\n**(2) Purpose**\nThe purpose of the database shall be to assist the Department in meeting the small business contracting goals established pursuant to subparagraphs (A) and (B) of section 8127(a)(1) of title 38, United States Code (relating to small business concerns owned and controlled by veterans), and in implementing the review mechanism required by section 8127(a)(4) of such title. As such, the database shall enable users to distinguish between\u2014\n**(A)**\nsmall business concerns owned and controlled by veterans who are not veterans with service-connected disabilities; and\n**(B)**\nsmall business concerns owned and controlled by veterans with service-connected disabilities.\n**(3) Exclusion**\nNotwithstanding paragraphs (1) and (2), the Secretary, acting through the Director, shall exclude from the database\u2014\n**(A)**\nany small business concern that is part of a mentor-proteg\u00e9 program or joint venture; and\n**(B)**\nany small business concern that has not had at least two past prime contracts for which the concern received an evaluation rating of Satisfactory or better pursuant to the Contractor Performance Assessment Reporting System (CPARS).\n##### (b) Availability\nThe Secretary, acting through the Director, shall make the database available to other-than-small businesses who are offerors on Department contracts (including subcontracts) at appropriate stages of the acquisition process for use by such businesses in formulating any required small business subcontracting plans.\n##### (c) Report\nNot later than 180 days after the date of the establishment of the database, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on the database. The report shall include\u2014\n**(1)**\na description of the extent to which the database has been made available to, and used by, businesses under subsection (b);\n**(2)**\nthe number of small business concerns owned and controlled by veterans who, since the date of the establishment of the database, have been selected as subcontractors on Department contracts, including the number of such concerns owned and controlled by veterans who are not veterans with service-connected disabilities and the number of such concerns owned and controlled by veterans with service-connected disabilities; and\n**(3)**\nthe recommendations of the Secretary for increasing the utilization of the database.\n##### (d) Use of existing resources\nThis section shall be implemented using existing personnel, systems, and funds. This section does not authorize additional appropriations or the establishment of a new program, office, or organizational entity.\n##### (e) Sunset\nThis section shall sunset on December 31, 2028.",
      "versionDate": "2026-03-04",
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
        "updateDate": "2026-04-01T20:31:46Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7795ih.xml"
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
      "title": "VA SUBCON Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA SUBCON Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Affairs Subcontractor Competition and Opportunity Network Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to establish and maintain a database of certified veteran-owned small businesses and service-disabled veteran-owned small businesses to assist the Department of Veterans Affairs in meeting its subcontracting goals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:24Z"
    }
  ]
}
```
