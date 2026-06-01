# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5949
- Title: Rural Veterans Dental Care Act
- Congress: 119
- Bill type: HR
- Bill number: 5949
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-05T16:47:41Z
- Update date including text: 2025-12-05T16:47:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5949",
    "number": "5949",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Rural Veterans Dental Care Act",
    "type": "HR",
    "updateDate": "2025-12-05T16:47:41Z",
    "updateDateIncludingText": "2025-12-05T16:47:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:37:55Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5949ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5949\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo establish a pilot program to furnish dental care to veterans who reside in rural and highly rural areas.\n#### 1. Short title\nThis Act may be cited as the Rural Veterans Dental Care Act .\n#### 2. Pilot program to furnish dental care to veterans who reside in rural areas\n##### (a) Establishment\nOn October 1, 2026, the Secretary of Veterans Affairs shall carry out a pilot program to furnish dental care to veterans who reside in rural and highly rural areas (as determined by the Director of the Office of Rural Health of the Department of Veterans Affairs).\n##### (b) Methods\nTo carry out the pilot program, the Secretary may use the following methods:\n**(1)**\nVans equipped with full diagnostic and treatment dental equipment.\n**(2)**\nModular or containerized mobile dental clinics\u2014\n**(A)**\nat community-based outpatient clinics of the Department; or\n**(B)**\nrural health fairs.\n**(3)**\nTents or other temporary structures at outreach events of the Department.\n##### (c) Priority\nIn selecting locations to carry out the pilot program, the Secretary shall give priority to locations\u2014\n**(1)**\nlocated more than 75 miles from the dental clinic operated by the Secretary;\n**(2)**\nthat have a high concentration of veterans with unmet dental needs; and\n**(3)**\nrural and highly rural areas (as such terms are used by the Office of Rural Health of the Veterans Health Administration) that have large populations of veterans.\n##### (d) Duration\nThe pilot program shall terminate on September 30, 2029.\n##### (e) Reporting\nNot later than September 30 of 2027, 2028, and 2029, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the pilot program. Such a report shall include the following elements:\n**(1)**\nThe number of veterans who received dental care through the pilot program.\n**(2)**\nLocations where the Secretary carried out the pilot program.\n**(3)**\nThe costs for operating each method under subsection (b).\n**(4)**\nThe recommendation of the Secretary whether to improve or make permanent the pilot program.",
      "versionDate": "2025-11-07",
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
        "updateDate": "2025-12-05T16:47:41Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5949ih.xml"
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
      "title": "Rural Veterans Dental Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T07:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Veterans Dental Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program to furnish dental care to veterans who reside in rural and highly rural areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:04:28Z"
    }
  ]
}
```
