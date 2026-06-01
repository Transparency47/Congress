# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7843
- Title: No Free Rides Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7843
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-04-01T19:09:29Z
- Update date including text: 2026-04-01T19:09:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7843",
    "number": "7843",
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
    "title": "No Free Rides Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-01T19:09:29Z",
    "updateDateIncludingText": "2026-04-01T19:09:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:03:35Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
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
      "sponsorshipDate": "2026-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7843ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7843\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Perry (for himself, Mr. Moore of Alabama , Mr. Roy , Mr. Higgins of Louisiana , Mr. Gill of Texas , Mr. Harris of North Carolina , and Mr. Steil ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to prohibit universal free fare policies on public transportation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Free Rides Act of 2026 .\n#### 2. Prohibition on universal fare free policies\nSection 5323 of title 49, United States Code, is amended by adding at the end the following:\n(w) Prohibition on universal fare free policies (1) In general A recipient of assistance under this chapter may not provide a universal fare free policy that allows all users of a public transportation service provided by or on behalf of such recipient from using such service without paying a fare. (2) Exception Nothing in this subsection shall prevent an recipient described in paragraph (1) from providing a targeted fare policy that allows a certain group of riders to ride for free or reduced charge including for\u2014 (A) seniors; (B) low-income riders; (C) students; or (D) employees or members of an organization whereby use of such public transportation is paid for through an agreement between an entity and the designated recipient. (3) Waiver The Secretary of Transportation may waive the requirements of paragraph (1) if a recipient of assistance under this chapter is able to identify a dedicated source of operating revenue for such a universal fare free policy from a non-Federal source. .",
      "versionDate": "2026-03-05",
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
        "updateDate": "2026-04-01T19:09:29Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7843ih.xml"
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
      "title": "No Free Rides Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Free Rides Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to prohibit universal free fare policies on public transportation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T04:48:21Z"
    }
  ]
}
```
