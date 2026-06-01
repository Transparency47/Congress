# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1432?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1432
- Title: LIABLE Act
- Congress: 119
- Bill type: HR
- Bill number: 1432
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-07-09T14:20:58Z
- Update date including text: 2025-07-09T14:20:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1432",
    "number": "1432",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "LIABLE Act",
    "type": "HR",
    "updateDate": "2025-07-09T14:20:58Z",
    "updateDateIncludingText": "2025-07-09T14:20:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "KY"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "OK"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "LA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AZ"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "SC"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1432ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1432\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Roy (for himself, Mr. Massie , Mr. Brecheen , Mr. Cloud , Mr. Higgins of Louisiana , Mr. Crane , Mr. Gosar , and Mr. Perry ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit any Federal law from making the manufacturer of a COVID\u201319 vaccine immune from suit or liability, or limiting the liability of such a manufacturer, with respect to claims for loss caused by, arising out of, relating to, or resulting from the administration to or the use by an individual of a COVID\u201319 vaccine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Let Injured Americans Be Legally Empowered Act or the LIABLE Act .\n#### 2. No Federal immunity from, or limitation on, liability for manufacturers for loss caused by a COVID\u201319 vaccine\n##### (a) In general\nNo Federal law, including sections 319F\u20133, 2111, and 2122 of the Public Health Service Act (42 U.S.C. 247d\u20136d, 300aa\u201311, 300aa\u201322), may make the manufacturer of a COVID\u201319 vaccine immune from suit or liability, or limit the liability of such a manufacturer, with respect to claims for loss caused by, arising out of, relating to, or resulting from the administration to or the use by an individual of a COVID\u201319 vaccine.\n##### (b) Rule of construction\nNothing in this Act shall be construed to prohibit an individual from seeking compensation through the Countermeasures Injury Compensation Program under section 319F\u20134 of the Public Health Service Act ( 42 U.S.C. 247d\u20136e ) or the National Vaccine Injury Compensation Program under subtitle 2 of title XXI of such Act ( 42 U.S.C. 300aa\u201310 et seq. ).\n##### (c) Relation to other programs\nAn individual shall not be precluded from bringing a civil action for claims described in subsection (a) on the basis of such individual having sought or received compensation through the Countermeasures Injury Compensation Program under section 319F\u20134 of the Public Health Service Act ( 42 U.S.C. 247d\u20136e ) or the National Vaccine Injury Compensation Program under subtitle 2 of title XXI of such Act ( 42 U.S.C. 300aa\u201310 et seq. ).\n##### (d) Definition\nThe term COVID\u201319 vaccine means a vaccine licensed or otherwise authorized by the Food and Drug Administration to prevent, mitigate, or limit\u2014\n**(1)**\nthe harm from COVID\u201319; or\n**(2)**\nthe transmission of SARS\u2013CoV\u20132 or a virus mutating therefrom.\n##### (e) Retroactive applicability\nThis Act applies without regard to whether the adminstration or use of a COVID\u201319 vaccine occurs before, on, or after the date of enactment of this Act.",
      "versionDate": "2025-02-18",
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-07-09T14:20:41Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-09T14:20:51Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-07-09T14:19:41Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-07-09T14:20:45Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-09T14:20:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T13:53:50Z"
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
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1432ih.xml"
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
      "title": "LIABLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIABLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Let Injured Americans Be Legally Empowered Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit any Federal law from making the manufacturer of a COVID-19 vaccine immune from suit or liability, or limiting the liability of such a manufacturer, with respect to claims for loss caused by, arising out of, relating to, or resulting from the administration to or the use by an individual of a COVID-19 vaccine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:37Z"
    }
  ]
}
```
