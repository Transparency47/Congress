# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1984
- Title: BLOC Act
- Congress: 119
- Bill type: HR
- Bill number: 1984
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-12-05T22:54:57Z
- Update date including text: 2025-12-05T22:54:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-10 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-10 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1984",
    "number": "1984",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001137",
        "district": "5",
        "firstName": "Jeff",
        "fullName": "Rep. Crank, Jeff [R-CO-5]",
        "lastName": "Crank",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "BLOC Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:57Z",
    "updateDateIncludingText": "2025-12-05T22:54:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-10T20:42:37Z",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1984ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1984\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Crank (for himself and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to limit certain Federal funding to States that do not have a process to notify the Secretary of Homeland Security of the release from custody or detainment certain aliens under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Blocking Lawless Open Border Cities and States Act of 2025 or the BLOC Act .\n#### 2. Ineligibility of sanctuary jurisdictions for certain Federal funds\n##### (a) In general\nChapter 6 of title 23, United States Code, is amended by adding at the end the following:\n612. Ineligibility of sanctuary jurisdictions for certain Federal funds (a) In general The Secretary of Transportation shall not obligate or award funds for any infrastructure project, including for highway construction, to a political subdivision of a State, nor shall any funds obligated or awarded to a State, go to any political subdivision of a State that does not have in effect not later than 1 year after the date of enactment of the BLOC Act a statute, ordinance, policy, or practice requiring an entity or official of such political subdivision to notify the Secretary of Homeland Security (or designee thereof) not later than 48 hours before of the release from custody or detainment of an alien if\u2014 (1) the Secretary of Homeland Security (or designee thereof) has determined that such alien is not lawfully present in the United States; (2) not later than 48 hours before such release, the Secretary of Homeland Security (or designee thereof) has notified the sheriff or detaining entity of such State or political subdivision of the legal status of such alien; and (3) such alien has been in custody or detainment for not less than 48 hours before such release. (b) Definition of infrastructure project In this section, the term infrastructure project has the meaning given such term in section 184.3 of title 2, Code of Federal Regulations (as in effect on the date of enactment of the BLOC Act). .\n##### (b) Clerical amendment\nThe analysis for chapter 6 of title 23, United States Code, is amended by adding at the end the following:\n612. Ineligibility of sanctuary jurisdictions for certain Federal funds. .",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "1913",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BLOC Act",
      "type": "HR"
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
        "updateDate": "2025-03-26T12:39:34Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1984ih.xml"
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
      "title": "BLOC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T07:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BLOC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Blocking Lawless Open Border Cities and States Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to limit certain Federal funding to States that do not have a process to notify the Secretary of Homeland Security of the release from custody or detainment certain aliens under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T07:33:29Z"
    }
  ]
}
```
