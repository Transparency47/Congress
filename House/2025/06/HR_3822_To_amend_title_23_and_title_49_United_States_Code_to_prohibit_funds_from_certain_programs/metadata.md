# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3822
- Title: No Desire for Streetcars Act
- Congress: 119
- Bill type: HR
- Bill number: 3822
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-10-15T08:05:20Z
- Update date including text: 2025-10-15T08:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-07 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-07 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3822",
    "number": "3822",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "No Desire for Streetcars Act",
    "type": "HR",
    "updateDate": "2025-10-15T08:05:20Z",
    "updateDateIncludingText": "2025-10-15T08:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-07",
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
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-07T20:30:02Z",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3822ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3822\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Perry introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23 and title 49, United States Code, to prohibit funds from certain programs to be used to fund streetcars, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Desire for Streetcars Act .\n#### 2. Prohibition on streetcar funding\n##### (a) Surface transportation block grant program\nSection 133 of title 23, United States Code, is amended by adding at the end the following:\n(l) Prohibition on streetcar funding Notwithstanding any other provision of this section, amounts apportioned to a State for each fiscal year to carry out this section may not be used for the procurement, operation, or maintenance of a streetcar. .\n##### (b) Congestion mitigation and air quality improvement program\nSection 149(c) of title 23, United States Code, is amended by adding at the end the following:\n(5) Streetcars No funds may be provided under this section for a project for streetcars. .\n##### (c) Urbanized area formula grants\nSection 5307 of title 49, United States Code, is amended by adding at the end the following:\n(i) Prohibition on streetcar funding Notwithstanding any other provision of this section, grant funds provided under this section may not be used for the procurement, operation, or maintenance of a streetcar. .\n##### (d) Fixed guideway capital investment grants\nSection 5309 of title 49, United States Code, is amended by adding at the end the following:\n(s) Prohibition on streetcar funding Notwithstanding any other provision of this section, grant funds provided under this section may not be used for the procurement, operation, or maintenance of a streetcar. .",
      "versionDate": "2025-06-06",
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
        "updateDate": "2025-06-30T13:13:51Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3822ih.xml"
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
      "title": "No Desire for Streetcars Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Desire for Streetcars Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23 and title 49, United States Code, to prohibit funds from certain programs to be used to fund streetcars, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:11Z"
    }
  ]
}
```
