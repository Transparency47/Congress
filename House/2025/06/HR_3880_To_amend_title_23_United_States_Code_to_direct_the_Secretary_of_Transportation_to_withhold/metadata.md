# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3880
- Title: Clear the ROADS Act
- Congress: 119
- Bill type: HR
- Bill number: 3880
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2025-07-15T08:06:22Z
- Update date including text: 2025-07-15T08:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-11 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-11 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3880",
    "number": "3880",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Clear the ROADS Act",
    "type": "HR",
    "updateDate": "2025-07-15T08:06:22Z",
    "updateDateIncludingText": "2025-07-15T08:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-11T20:47:26Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3880ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3880\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Huizenga (for himself, Mr. Kustoff , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to direct the Secretary of Transportation to withhold from States certain apportionments if the States do not make reasonable efforts to prohibit certain roadway obstruction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clear the Reckless Obstructions And Dangers on Streets Act or the Clear the ROADS Act .\n#### 2. Roadway obstruction\n##### (a) Withholding of apportionments for noncompliance\n**(1) In general**\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Roadway obstruction (a) Withholding of apportionments for noncompliance Beginning not later than the first October 1 after the Secretary of Transportation has issued such regulations as are necessary to carry out this section or the first October 1 after a State has held a legislative session, whichever is later, and each October 1 thereafter, the Secretary shall withhold an amount equal to 10 percent of the funds to be apportioned to a State on that date under each of paragraphs (1) and (2) of section 104(b), unless the Secretary has certified on or before that date that the State has met the requirement described in subsection (b). (b) Requirement A State meets the requirement of this subsection if the Secretary determines the State has made reasonable efforts to prohibit individuals who are not performing work on behalf of a Federal, State, or local government from knowingly and recklessly obstructing lawful vehicle transportation on Federal-aid highways in the State in a manner that endangers the safety or health of the public. .\n**(2) Clerical amendment**\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Roadway obstruction. .\n##### (b) Rulemaking\nNot later than 180 days after the date of enactment of this section, the Secretary of Transportation shall issue such regulations as are necessary to carry out section 180 of title 23, United States Code (as added by this section).",
      "versionDate": "2025-06-10",
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
        "updateDate": "2025-06-27T13:27:28Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3880ih.xml"
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
      "title": "Clear the ROADS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clear the ROADS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clear the Reckless Obstructions And Dangers on Streets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to direct the Secretary of Transportation to withhold from States certain apportionments if the States do not make reasonable efforts to prohibit certain roadway obstruction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:18Z"
    }
  ]
}
```
