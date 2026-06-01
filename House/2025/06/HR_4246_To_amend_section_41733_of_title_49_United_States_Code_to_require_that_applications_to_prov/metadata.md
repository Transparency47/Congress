# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4246?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4246
- Title: Essential Air Service Reliability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4246
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-09-11T08:06:28Z
- Update date including text: 2025-09-11T08:06:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-28 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-28 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4246",
    "number": "4246",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Essential Air Service Reliability Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:28Z",
    "updateDateIncludingText": "2025-09-11T08:06:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-28",
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
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-28T16:57:56Z",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "AK"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MI"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MP"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4246ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4246\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Ms. Tokuda (for herself, Mr. Begich , Ms. Scholten , and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend section 41733 of title 49, United States Code, to require that applications to provide compensated basic essential air service include a contingency plan to continue air service in the event of a disruption, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Essential Air Service Reliability Act of 2025 .\n#### 2. Basic essential air service availability of compensation\n##### (a) In general\nSection 41733(c) of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (4);\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nby striking (1) If the Secretary and inserting the following:\n(1) Application If the Secretary ;\n**(B)**\nby inserting after compensation under this section. the following new paragraph:\n(2) Requirement For any application submitted pursuant to paragraph (1), such application shall include a contingency plan that provides for the continuation of air service to the eligible place in the event of a disruption that is not related to weather. ; and\n**(C)**\nby striking In selecting an applicant, and inserting the following:\n(3) Considerations In selecting an applicant, ; and\n**(3)**\nin paragraph (4), as so redesignated, by striking Under guidelines and inserting Rate of compensation. \u2014Under guidelines .\n##### (b) Applicability\nThe Secretary of Transportation shall ensure that the amendment made by section 2(a)(2)(B) shall apply not later than 180 days after the date of enactment of this Act.\n##### (c) Conforming amendment\nSection 41736(c)(2)(A) of title 49, United States Code, is amended by striking section 41733(c)(1) and inserting section 41733(c) .",
      "versionDate": "2025-06-27",
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
        "updateDate": "2025-07-28T11:01:00Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4246ih.xml"
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
      "title": "Essential Air Service Reliability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Essential Air Service Reliability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T10:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 41733 of title 49, United States Code, to require that applications to provide compensated basic essential air service include a contingency plan to continue air service in the event of a disruption, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T10:48:23Z"
    }
  ]
}
```
